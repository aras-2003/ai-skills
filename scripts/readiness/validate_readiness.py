from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

HERE = Path(__file__).resolve()
VALIDATE = HERE.parents[1] / "validate"
sys.path.insert(0, str(VALIDATE))
from common import split_frontmatter  # noqa: E402


def production_components(root: Path) -> dict[str, tuple[str, str, str]]:
    result: dict[str, tuple[str, str, str]] = {}
    for skill_file in sorted((root / "skills").rglob("SKILL.md")):
        fm, _ = split_frontmatter(skill_file.read_text(encoding="utf-8"))
        metadata = fm.get("metadata") or {}
        if metadata.get("maturity") == "production":
            result[str(fm["name"])] = (
                "skill",
                str(metadata.get("version") or ""),
                skill_file.relative_to(root).as_posix(),
            )

    registry = yaml.safe_load((root / "workflows" / "runtime-registry.yaml").read_text(encoding="utf-8")) or {}
    for item in registry.get("workflows") or []:
        if not isinstance(item, dict):
            continue
        metadata = item.get("metadata") or {}
        if metadata.get("maturity") == "production":
            result[str(item.get("name"))] = (
                "workflow",
                str(metadata.get("version") or ""),
                str(item.get("workflow") or ""),
            )
    return result


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / "release" / "production-readiness.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    records = data.get("components") or []
    if not isinstance(records, list):
        return ["components must be a list"]

    actual = production_components(root)
    seen: dict[str, dict[str, Any]] = {}
    for rec in records:
        if not isinstance(rec, dict):
            errors.append("readiness record must be a mapping")
            continue
        name = str(rec.get("name") or "")
        if not name:
            errors.append("readiness record missing name")
            continue
        if name in seen:
            errors.append(f"duplicate readiness record: {name}")
        seen[name] = rec

        if rec.get("current_runtime_receipt") not in {"pending", "verified", "not-required"}:
            errors.append(f"{name}: invalid current_runtime_receipt")
        if not rec.get("maturity_disposition"):
            errors.append(f"{name}: missing maturity_disposition")
        if rec.get("current_runtime_receipt") == "pending":
            for field in ("evidence_gap", "limitation", "exception_owner", "exception_expires"):
                if not rec.get(field):
                    errors.append(f"{name}: pending evidence requires {field}")

    missing = sorted(set(actual) - set(seen))
    extra = sorted(set(seen) - set(actual))
    if missing:
        errors.append("missing production readiness records: " + ", ".join(missing))
    if extra:
        errors.append("readiness records for non-production components: " + ", ".join(extra))

    for name, (kind, version, source) in actual.items():
        rec = seen.get(name)
        if not rec:
            continue
        if rec.get("kind") != kind:
            errors.append(f"{name}: kind mismatch")
        if str(rec.get("version")) != version:
            errors.append(f"{name}: version mismatch ({rec.get('version')} != {version})")
        if rec.get("source") != source:
            errors.append(f"{name}: source mismatch")
    return errors


def main() -> int:
    root = HERE.parents[2]
    errors = validate(root)
    for error in errors:
        print(f"[BLOCKER] release/production-readiness.yaml: {error}")
    if not errors:
        print("Production readiness registry: OK")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
