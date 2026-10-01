from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

from common import find_campaign_case, load_registry, repo_root, sha256_file

VALID_STATUSES = {"NOT_RUN", "REVIEW_REQUIRED", "PASS", "FAIL"}
VALID_EVIDENCE_SCOPES = {"current-version", "historical"}
RUNTIME_STATUSES = {"REVIEW_REQUIRED", "PASS", "FAIL"}


def find_case(root: Path, case_id: str) -> tuple[str, dict[str, Any]]:
    for target, cases in load_registry(root).items():
        for case in cases:
            if case.get("id") == case_id:
                return target, case
    campaign_case = find_campaign_case(root, case_id)
    if campaign_case is not None:
        return str(campaign_case["target"]), campaign_case
    raise KeyError(f"unknown case id: {case_id}")


def _split_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: unterminated frontmatter")
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: frontmatter must be a mapping")
    return data


def _source_tree_digest(path: Path) -> str:
    h = hashlib.sha256()
    files: list[Path] = []
    for item in path.rglob("*"):
        if not item.is_file():
            continue
        rel = item.relative_to(path)
        if rel.parts and rel.parts[0] in {"tests", "evals", "__pycache__"}:
            continue
        if item.name.endswith((".pyc", ".pyo")):
            continue
        files.append(item)
    for item in sorted(files):
        rel = item.relative_to(path).as_posix().encode()
        h.update(len(rel).to_bytes(4, "big"))
        h.update(rel)
        data = item.read_bytes()
        h.update(len(data).to_bytes(8, "big"))
        h.update(data)
    return h.hexdigest()


def current_component_identity(root: Path, name: str) -> tuple[str, str]:
    for skill_md in sorted((root / "skills").rglob("SKILL.md")):
        fm = _split_frontmatter(skill_md)
        if fm.get("name") != name:
            continue
        metadata = fm.get("metadata") or {}
        version = metadata.get("version")
        if not isinstance(version, str) or not version:
            raise ValueError(f"{skill_md}: missing component version")
        return version, _source_tree_digest(skill_md.parent)

    registry_path = root / "workflows" / "runtime-registry.yaml"
    data = yaml.safe_load(registry_path.read_text(encoding="utf-8")) or {}
    for item in data.get("workflows") or []:
        if not isinstance(item, dict) or item.get("name") != name:
            continue
        metadata = item.get("metadata") or {}
        version = metadata.get("version")
        workflow_rel = item.get("workflow")
        if not isinstance(version, str) or not version:
            raise ValueError(f"{registry_path}: {name} missing version")
        if not isinstance(workflow_rel, str) or not workflow_rel:
            raise ValueError(f"{registry_path}: {name} missing workflow path")
        workflow_path = root / workflow_rel
        if not workflow_path.is_file():
            raise ValueError(f"{registry_path}: {name} workflow path missing: {workflow_rel}")
        h = hashlib.sha256()
        h.update(_source_tree_digest(workflow_path.parent).encode())
        h.update(json.dumps(item, sort_keys=True, default=str, ensure_ascii=False).encode("utf-8"))
        return version, h.hexdigest()
    raise KeyError(f"unknown component: {name}")


def component_identity_at_revision(root: Path, name: str, revision: str) -> tuple[str, str]:
    try:
        subprocess.run(
            ["git", "cat-file", "-e", revision + "^{commit}"],
            cwd=root,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        current = current_component_identity(root, name)
        return current

    import tempfile

    with tempfile.TemporaryDirectory() as td:
        snapshot = Path(td) / "snapshot"
        snapshot.mkdir()
        archive = subprocess.Popen(
            ["git", "archive", "--format=tar", revision, "skills", "workflows"],
            cwd=root,
            stdout=subprocess.PIPE,
        )
        extract = subprocess.run(
            ["tar", "-xf", "-", "-C", str(snapshot)],
            stdin=archive.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=False,
        )
        if archive.stdout is not None:
            archive.stdout.close()
        rc = archive.wait()
        if rc != 0 or extract.returncode != 0:
            raise ValueError(f"cannot materialize source revision {revision}")
        return current_component_identity(snapshot, name)


def current_source_revision(root: Path) -> str:
    override = os.environ.get("SOURCE_REVISION")
    if override:
        return override
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    except Exception:
        return "unknown"


def _validate_status_contract(data: dict[str, Any], errors: list[str]) -> None:
    status = data.get("evaluation", {}).get("status")
    runtime = data.get("runtime", {})
    execution = data.get("execution", {})
    component = data.get("component", {})
    runtime_artifact = data.get("runtime_artifact") or {}
    if status not in VALID_STATUSES:
        errors.append(f"invalid status: {status}")
        return

    if status in RUNTIME_STATUSES:
        required = {
            "component.version": component.get("version"),
            "component.content_sha256": component.get("content_sha256"),
            "runtime.provider": runtime.get("provider"),
            "runtime.model_id": runtime.get("model_id"),
            "execution.actual_output_path": execution.get("actual_output_path"),
            "execution.actual_output_sha256": execution.get("actual_output_sha256"),
        }
        if runtime_artifact:
            required.update({
                "runtime_artifact.channel": runtime_artifact.get("channel"),
                "runtime_artifact.package_name": runtime_artifact.get("package_name"),
                "runtime_artifact.package_version": runtime_artifact.get("package_version"),
                "runtime_artifact.release_id": runtime_artifact.get("release_id"),
                "runtime_artifact.source_revision": runtime_artifact.get("source_revision"),
                "runtime_artifact.payload_content_sha256": runtime_artifact.get("payload_content_sha256"),
                "runtime_artifact.component_content_sha256": runtime_artifact.get("component_content_sha256"),
            })
        missing = [name for name, value in required.items() if not value]
        if missing:
            errors.append(f"{status} requires runtime/component/output identity: {', '.join(missing)}")
    if status == "PASS" and execution.get("assisted"):
        errors.append("assisted run cannot be PASS")


def _stored_path(root: Path, path: Path | None) -> str | None:
    if path is None:
        return None
    resolved = path.resolve()
    try:
        return resolved.relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(resolved)


def _resolve_stored_path(root: Path, raw: str | None) -> Path | None:
    if not raw:
        return None
    path = Path(raw)
    return path if path.is_absolute() else root / path


def create_receipt(args: argparse.Namespace) -> dict[str, Any]:
    root = repo_root()
    target, case = find_case(root, args.case_id)
    input_path = root / case["input"]
    rubric_path = root / case["rubric"]

    status = args.status
    if status not in VALID_STATUSES:
        raise ValueError(f"invalid status: {status}")
    evidence_scope = getattr(args, "evidence_scope", "current-version")
    if evidence_scope not in VALID_EVIDENCE_SCOPES:
        raise ValueError(f"invalid evidence scope: {evidence_scope}")
    if status in RUNTIME_STATUSES and not args.output:
        raise ValueError(f"{status} requires --output")
    if status in RUNTIME_STATUSES:
        required_runtime = {
            "component_version": args.component_version,
            "component_digest": args.component_digest,
            "provider": args.provider,
            "model_id": args.model_id,
        }
        missing = [name for name, value in required_runtime.items() if not value]
        if missing:
            raise ValueError(f"{status} requires runtime/component identity: {', '.join(missing)}")
    if status == "PASS" and args.assisted:
        raise ValueError("assisted runs cannot be recorded as PASS")

    component_name = args.component or target
    if evidence_scope == "current-version" and status in RUNTIME_STATUSES:
        current_version, current_digest = current_component_identity(root, component_name)
        if args.component_version != current_version:
            raise ValueError(
                f"current-version evidence component version mismatch: {args.component_version} != {current_version}"
            )
        if args.component_digest != current_digest:
            raise ValueError("current-version evidence component content digest mismatch")
        current_revision = current_source_revision(root)
        if current_revision != "unknown" and args.source_revision != current_revision:
            raise ValueError(
                f"current-version evidence source revision mismatch: {args.source_revision} != {current_revision}"
            )

    output_path = Path(args.output).resolve() if args.output else None
    trace_path = Path(args.tool_trace).resolve() if args.tool_trace else None
    record = {
        "schema_version": "1.0",
        "evidence_scope": evidence_scope,
        "case": {
            "id": args.case_id,
            "target": target,
            "mode": case["mode"],
            "input_path": case["input"],
            "input_sha256": sha256_file(input_path),
            "rubric_path": case["rubric"],
            "rubric_sha256": sha256_file(rubric_path),
        },
        "component": {
            "name": component_name,
            "version": args.component_version,
            "content_sha256": args.component_digest,
        },
        "source_revision": args.source_revision,
        "runtime_artifact": getattr(args, "runtime_artifact", None),
        "runtime": {
            "provider": args.provider,
            "model_id": args.model_id,
            "reasoning": args.reasoning,
            "catalog": args.catalog,
            "tools": list(getattr(args, "tools", []) or []),
        },
        "execution": {
            "assisted": bool(args.assisted),
            "prompt": args.prompt,
            "actual_output_path": _stored_path(root, output_path),
            "actual_output_sha256": sha256_file(output_path) if output_path else None,
            "tool_trace_path": _stored_path(root, trace_path),
            "tool_trace_sha256": sha256_file(trace_path) if trace_path else None,
            "selection_findings": list(getattr(args, "selection_findings", []) or []),
            "evidence_origin": str(getattr(args, "evidence_origin", "runtime")),
        },
        "evaluation": {
            "status": status,
            "rubric_version": "1.0",
            "reviewer": args.reviewer,
            "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "note": args.note,
        },
    }

    errors = validate_receipt_data(record, root=root, current_revision=current_source_revision(root))
    if errors:
        raise ValueError("; ".join(errors))
    return record


def validate_receipt_data(
    data: dict[str, Any],
    *,
    root: Path | None = None,
    current_revision: str | None = None,
) -> list[str]:
    root = root or repo_root()
    schema = json.loads((root / "scripts/eval/schemas/evidence-record.schema.json").read_text(encoding="utf-8"))
    errors = [f"schema: {e.message}" for e in Draft202012Validator(schema).iter_errors(data)]
    _validate_status_contract(data, errors)

    case = data.get("case", {})
    try:
        target, current = find_case(root, case.get("id", ""))
    except KeyError as exc:
        return errors + [str(exc)]
    input_path = root / current["input"]
    rubric_path = root / current["rubric"]
    if case.get("target") != target:
        errors.append("stale evidence: case target mismatch")
    if case.get("input_path") != current["input"]:
        errors.append("stale evidence: input path mismatch")
    if case.get("rubric_path") != current["rubric"]:
        errors.append("stale evidence: rubric path mismatch")
    if case.get("input_sha256") != sha256_file(input_path):
        errors.append("stale evidence: input digest mismatch")
    if case.get("rubric_sha256") != sha256_file(rubric_path):
        errors.append("stale evidence: rubric digest mismatch")

    status = data.get("evaluation", {}).get("status")
    execution = data.get("execution", {})
    if status in RUNTIME_STATUSES:
        raw_output = execution.get("actual_output_path")
        if raw_output:
            output_path = _resolve_stored_path(root, raw_output)
            if output_path is None or not output_path.is_file():
                errors.append("runtime evidence output is missing")
            elif execution.get("actual_output_sha256") != sha256_file(output_path):
                errors.append("runtime evidence output digest mismatch")
        raw_trace = execution.get("tool_trace_path")
        if raw_trace:
            trace_path = _resolve_stored_path(root, raw_trace)
            if trace_path is None or not trace_path.is_file():
                errors.append("runtime evidence tool trace is missing")
            elif execution.get("tool_trace_sha256") != sha256_file(trace_path):
                errors.append("runtime evidence tool trace digest mismatch")

    scope = data.get("evidence_scope")
    if scope == "current-version" and status in RUNTIME_STATUSES:
        component = data.get("component", {})
        component_name = component.get("name") or ""
        identity_revision = str(data.get("source_revision") or "")
        try:
            version, digest = component_identity_at_revision(root, component_name, identity_revision)
        except (KeyError, ValueError) as exc:
            errors.append(str(exc))
        else:
            if component.get("version") != version:
                errors.append("stale evidence: component version mismatch")
            if component.get("content_sha256") != digest:
                errors.append("stale evidence: component content digest mismatch")
        runtime_artifact = data.get("runtime_artifact") or {}
        artifact_revision = runtime_artifact.get("source_revision")
        if artifact_revision and artifact_revision != identity_revision:
            errors.append("runtime artifact/source evidence revision mismatch")
        current_revision = current_revision if current_revision is not None else current_source_revision(root)
        if current_revision != "unknown" and data.get("source_revision") != current_revision:
            errors.append("stale evidence: source revision mismatch")
    return errors


def validate_receipt(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return validate_receipt_data(data)


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    create = sub.add_parser("create")
    create.add_argument("--case-id", required=True)
    create.add_argument("--status", required=True, choices=sorted(VALID_STATUSES))
    create.add_argument("--evidence-scope", choices=sorted(VALID_EVIDENCE_SCOPES), default="current-version")
    create.add_argument("--source-revision", required=True)
    create.add_argument("--component")
    create.add_argument("--component-version")
    create.add_argument("--component-digest")
    create.add_argument("--runtime-artifact-json")
    create.add_argument("--provider")
    create.add_argument("--model-id")
    create.add_argument("--reasoning")
    create.add_argument("--catalog", nargs="*", default=[])
    create.add_argument("--tools", nargs="*", default=[])
    create.add_argument("--prompt")
    create.add_argument("--output")
    create.add_argument("--tool-trace")
    create.add_argument("--reviewer")
    create.add_argument("--assisted", action="store_true")
    create.add_argument("--selection-finding", action="append", default=[])
    create.add_argument("--evidence-origin", choices=["runtime", "offline"], default="runtime")
    create.add_argument("--note")
    create.add_argument("--write", required=True)

    validate = sub.add_parser("validate")
    validate.add_argument("paths", nargs="+")

    args = parser.parse_args()
    if args.cmd == "create":
        args.runtime_artifact = (
            json.loads(Path(args.runtime_artifact_json).read_text(encoding="utf-8"))
            if args.runtime_artifact_json else None
        )
        args.selection_findings = args.selection_finding
        record = create_receipt(args)
        dest = Path(args.write)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(dest)
        return 0

    failed = False
    for raw in args.paths:
        path = Path(raw)
        errors = validate_receipt(path)
        if errors:
            failed = True
            for err in errors:
                print(f"[BLOCKER] {path}: {err}")
        else:
            print(f"{path}: OK")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
