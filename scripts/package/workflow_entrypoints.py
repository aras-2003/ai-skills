from __future__ import annotations

from pathlib import Path
import shutil
import yaml

from portable import portable_metadata


def load_registry(root: Path) -> list[dict]:
    path = root / "workflows" / "runtime-registry.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    items = data.get("workflows") or []
    if not isinstance(items, list):
        raise ValueError("workflows/runtime-registry.yaml: workflows must be a list")
    return items


def select_workflows(root: Path, maturity: str) -> list[dict]:
    selected = []
    for item in load_registry(root):
        metadata = item.get("metadata") or {}
        if metadata.get("maturity") == maturity:
            selected.append(item)
    return selected


def build_entrypoint(root: Path, item: dict, skills_out: Path) -> str:
    name = item.get("name")
    workflow_rel = item.get("workflow")
    description = str(item.get("description") or "").strip()
    metadata = item.get("metadata") or {}

    if not name or not workflow_rel or not description:
        raise ValueError(f"Invalid workflow registry item: {item}")

    workflow = root / workflow_rel
    if not workflow.exists():
        raise FileNotFoundError(f"Missing workflow source: {workflow}")

    dst = skills_out / name
    if dst.exists():
        raise ValueError(f"duplicate runtime skill/workflow name: {name}")

    refs = dst / "references"
    refs.mkdir(parents=True, exist_ok=True)
    shutil.copy2(workflow, refs / "WORKFLOW.md")

    fm = yaml.safe_dump(
        {
            "name": name,
            "description": description,
            "metadata": portable_metadata(metadata),
        },
        sort_keys=False,
        allow_unicode=True,
    ).strip()

    skill_md = f"""---
{fm}
---

# {name.replace('-', ' ').title()} Runtime Entrypoint

## Purpose

Expose a repository workflow to the skill runtime without duplicating its orchestration logic.

## Procedure

1. Load `references/WORKFLOW.md`.
2. Follow it as the authoritative orchestration procedure.
3. Route only to specialist skills that the workflow actually requires.
4. Preserve workflow gates, stop conditions and evidence discipline.
5. Do not replace the workflow with a generic best-practice answer.

## Output contract

Use the output contract defined in `references/WORKFLOW.md`.

## Quality checks

- [ ] The workflow source was loaded.
- [ ] Specialist skills were selected selectively.
- [ ] Workflow stage order and gates were preserved.
- [ ] Evidence and uncertainty remain explicit.
- [ ] No extra domain was added merely for completeness.
"""
    (dst / "SKILL.md").write_text(skill_md, encoding="utf-8")
    return name


def add_workflow_entrypoints(root: Path, maturity: str, skills_out: Path) -> list[str]:
    names = []
    for item in select_workflows(root, maturity):
        names.append(build_entrypoint(root, item, skills_out))
    return names
