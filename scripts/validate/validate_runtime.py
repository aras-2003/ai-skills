from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

from common import NAME_RE, ValidationIssue, repo_root_from, split_frontmatter

PACKAGE_DIR = Path(__file__).resolve().parents[1] / "package"
if str(PACKAGE_DIR) not in sys.path:
    sys.path.insert(0, str(PACKAGE_DIR))

from portable import portable_frontmatter  # noqa: E402

ALLOWED_CHANNEL_STATES = {"supported", "unavailable"}


def load_skill_index(root: Path) -> dict[str, dict[str, Any]]:
    skills: dict[str, dict[str, Any]] = {}
    for skill_file in sorted((root / "skills").rglob("SKILL.md")):
        fm, _ = split_frontmatter(skill_file.read_text(encoding="utf-8"))
        name = fm.get("name")
        if not isinstance(name, str):
            continue
        metadata = fm.get("metadata") or {}
        skills[name] = {
            "path": skill_file,
            "maturity": metadata.get("maturity"),
            "frontmatter": fm,
        }
    return skills


def load_workflows(root: Path) -> list[dict[str, Any]]:
    path = root / "workflows" / "runtime-registry.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    workflows = data.get("workflows")
    if not isinstance(workflows, list):
        raise ValueError(f"{path}: workflows must be a list")
    return workflows


def validate_portable(frontmatter: dict[str, Any], path: str) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    try:
        portable = portable_frontmatter(frontmatter)
    except Exception as exc:
        return [ValidationIssue("blocker", path, f"portable metadata conversion failed: {exc}")]

    name = portable.get("name")
    description = portable.get("description")
    if not isinstance(name, str) or not (1 <= len(name) <= 64) or not NAME_RE.match(name):
        issues.append(ValidationIssue("blocker", path, "portable name is invalid"))
    if not isinstance(description, str) or not (1 <= len(description) <= 1024):
        issues.append(ValidationIssue("blocker", path, "portable description must be 1..1024 characters"))
    compatibility = portable.get("compatibility")
    if compatibility is not None and (not isinstance(compatibility, str) or len(compatibility) > 500):
        issues.append(ValidationIssue("blocker", path, "portable compatibility must be <=500 characters"))
    metadata = portable.get("metadata") or {}
    if not isinstance(metadata, dict) or not all(
        isinstance(k, str) and isinstance(v, str) for k, v in metadata.items()
    ):
        issues.append(ValidationIssue("blocker", path, "portable metadata must be string -> string"))
    return issues


def _dependency_sets(item: dict[str, Any]) -> tuple[list[str], list[dict[str, Any]]]:
    deps = item.get("dependencies") or {}
    required = deps.get("required") or []
    optional = deps.get("optional") or []
    if not isinstance(required, list):
        raise ValueError("dependencies.required must be a list")
    if not isinstance(optional, list):
        raise ValueError("dependencies.optional must be a list")
    return required, optional


def _detect_required_cycles(workflows: dict[str, dict[str, Any]]) -> list[list[str]]:
    graph: dict[str, list[str]] = {}
    for name, item in workflows.items():
        required, _ = _dependency_sets(item)
        graph[name] = [dep for dep in required if dep in workflows]

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()
    stack: list[str] = []

    def visit(node: str) -> None:
        if node in visited:
            return
        if node in visiting:
            if node in stack:
                i = stack.index(node)
                cycles.append(stack[i:] + [node])
            return
        visiting.add(node)
        stack.append(node)
        for nxt in graph.get(node, []):
            visit(nxt)
        stack.pop()
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node)
    return cycles


def validate_runtime(root: Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    skills = load_skill_index(root)
    workflow_path = root / "workflows" / "runtime-registry.yaml"

    try:
        items = load_workflows(root)
    except Exception as exc:
        return [ValidationIssue("blocker", str(workflow_path), str(exc))]

    workflows: dict[str, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict):
            issues.append(ValidationIssue("blocker", str(workflow_path), "workflow item must be a mapping"))
            continue
        name = str(item.get("name") or "").strip()
        if not name:
            issues.append(ValidationIssue("blocker", str(workflow_path), "workflow name is required"))
            continue
        if name in workflows:
            issues.append(ValidationIssue("blocker", str(workflow_path), f"duplicate workflow: {name}"))
        workflows[name] = item
        if name in skills:
            issues.append(
                ValidationIssue(
                    "blocker",
                    str(workflow_path),
                    f"duplicate runtime entrypoint name collides with skill: {name}",
                )
            )
        source = root / str(item.get("workflow") or "")
        if not source.is_file():
            issues.append(ValidationIssue("blocker", str(workflow_path), f"{name}: missing workflow source {source}"))

        channels = item.get("channels")
        if not isinstance(channels, dict) or not channels:
            issues.append(ValidationIssue("blocker", str(workflow_path), f"{name}: channels mapping is required"))
        else:
            for channel, state in channels.items():
                if state not in ALLOWED_CHANNEL_STATES:
                    issues.append(
                        ValidationIssue(
                            "blocker",
                            str(workflow_path),
                            f"{name}: invalid channel state {channel}={state!r}",
                        )
                    )

        metadata = item.get("metadata") or {}
        maturity = metadata.get("maturity")
        for field in ("owner", "version", "maturity", "risk", "last_reviewed"):
            if metadata.get(field) in (None, ""):
                issues.append(
                    ValidationIssue("blocker", str(workflow_path), f"{name}: missing metadata.{field}")
                )

        issues.extend(validate_portable(
            {"name": name, "description": item.get("description"), "metadata": metadata},
            f"{workflow_path}:{name}",
        ))

        try:
            required, optional = _dependency_sets(item)
        except Exception as exc:
            issues.append(ValidationIssue("blocker", str(workflow_path), f"{name}: {exc}"))
            continue

        all_known = set(skills) | set(workflows) | {
            str(x.get("name") or "") for x in items if isinstance(x, dict)
        }
        for dep in required:
            if not isinstance(dep, str) or not dep:
                issues.append(ValidationIssue("blocker", str(workflow_path), f"{name}: invalid required dependency"))
                continue
            if dep not in all_known:
                issues.append(ValidationIssue("blocker", str(workflow_path), f"{name}: unknown required dependency {dep}"))
        for dep in optional:
            if not isinstance(dep, dict):
                issues.append(ValidationIssue("blocker", str(workflow_path), f"{name}: optional dependency must be mapping"))
                continue
            dep_name = str(dep.get("name") or "").strip()
            on_missing = str(dep.get("on_missing") or "").strip()
            if dep_name not in all_known:
                issues.append(ValidationIssue("blocker", str(workflow_path), f"{name}: unknown optional dependency {dep_name}"))
            if not on_missing:
                issues.append(ValidationIssue("blocker", str(workflow_path), f"{name}/{dep_name}: on_missing is required"))

        if maturity == "production" and isinstance(channels, dict) and channels.get("plugin") == "supported":
            prod_capabilities = {
                n for n, s in skills.items() if s.get("maturity") == "production"
            } | {
                str(x.get("name")) for x in items
                if isinstance(x, dict)
                and (x.get("metadata") or {}).get("maturity") == "production"
                and (x.get("channels") or {}).get("plugin") == "supported"
            }
            for dep in required:
                if isinstance(dep, str) and dep not in prod_capabilities:
                    issues.append(
                        ValidationIssue(
                            "blocker",
                            str(workflow_path),
                            f"{name}: production required dependency unavailable in plugin channel: {dep}",
                        )
                    )

    for cycle in _detect_required_cycles(workflows):
        issues.append(
            ValidationIssue("blocker", str(workflow_path), "required dependency cycle: " + " -> ".join(cycle))
        )

    for info in skills.values():
        issues.extend(validate_portable(info["frontmatter"], str(info["path"])))

    fixture_path = root / "evals" / "runtime-fixtures.yaml"
    try:
        fixture_data = yaml.safe_load(fixture_path.read_text(encoding="utf-8")) or {}
        targets = fixture_data.get("targets")
        if not isinstance(targets, dict):
            raise ValueError("targets must be a mapping")
    except Exception as exc:
        issues.append(ValidationIssue("blocker", str(fixture_path), f"invalid fixture registry: {exc}"))
        return issues

    known_targets = set(skills) | set(workflows)
    seen_case_ids: set[str] = set()
    for target, cases in targets.items():
        if target not in known_targets:
            issues.append(ValidationIssue("blocker", str(fixture_path), f"unknown fixture target: {target}"))
        if not isinstance(cases, list) or not cases:
            issues.append(ValidationIssue("blocker", str(fixture_path), f"{target}: cases must be a non-empty list"))
            continue
        for case in cases:
            if not isinstance(case, dict):
                issues.append(ValidationIssue("blocker", str(fixture_path), f"{target}: case must be mapping"))
                continue
            cid = str(case.get("id") or "").strip()
            if not cid:
                issues.append(ValidationIssue("blocker", str(fixture_path), f"{target}: missing case id"))
            elif cid in seen_case_ids:
                issues.append(ValidationIssue("blocker", str(fixture_path), f"duplicate fixture id: {cid}"))
            seen_case_ids.add(cid)
            input_path = root / str(case.get("input") or "")
            rubric_path = root / str(case.get("rubric") or "")
            if not input_path.is_file():
                issues.append(ValidationIssue("blocker", str(fixture_path), f"{cid}: missing input {input_path}"))
            if not rubric_path.is_file():
                issues.append(ValidationIssue("blocker", str(fixture_path), f"{cid}: missing rubric {rubric_path}"))
                continue
            try:
                rubric = yaml.safe_load(rubric_path.read_text(encoding="utf-8")) or {}
            except Exception as exc:
                issues.append(ValidationIssue("blocker", str(rubric_path), f"invalid rubric: {exc}"))
                continue
            if rubric.get("id") != cid:
                issues.append(ValidationIssue("blocker", str(rubric_path), f"stale fixture id: expected {cid!r}"))
            if rubric.get("target") != target:
                issues.append(
                    ValidationIssue("blocker", str(rubric_path), f"stale fixture target: expected {target!r}")
                )
            assertions = rubric.get("assertions") or {}
            if not isinstance(assertions, dict) or not any(assertions.get(k) for k in ("manual", "deterministic")):
                issues.append(ValidationIssue("blocker", str(rubric_path), "rubric assertions must be non-empty"))

    return issues


def main() -> int:
    root = repo_root_from(__file__)
    issues = validate_runtime(root)
    for issue in issues:
        print(issue)
    return 1 if any(i.severity in {"blocker", "high"} for i in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
