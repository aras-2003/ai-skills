from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from common import ValidationIssue, load_json, repo_root_from


# Definition validation only: this module validates test-suite structure/contracts.
# It does not execute behavioral assertions against a model/runtime.


def validate_cases(path: Path, schema: dict) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [ValidationIssue("blocker", str(path), f"Invalid YAML: {exc}")]

    validator = Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        where = ".".join(str(x) for x in error.path)
        suffix = f" at {where}" if where else ""
        issues.append(ValidationIssue("blocker", str(path), f"Test schema violation{suffix}: {error.message}"))

    if not isinstance(data, dict) or not isinstance(data.get("cases"), list):
        return issues

    ids: set[str] = set()
    has_positive = False
    has_negative = False

    for case in data["cases"]:
        if not isinstance(case, dict):
            continue
        cid = case.get("id")
        if isinstance(cid, str):
            if cid in ids:
                issues.append(ValidationIssue("blocker", str(path), f"Duplicate test id: {cid}"))
            ids.add(cid)

        expected = case.get("expected", {})
        if isinstance(expected, dict):
            trigger = expected.get("should_trigger")
            has_positive = has_positive or trigger is True
            has_negative = has_negative or trigger is False
            must = expected.get("must") or []
            must_not = expected.get("must_not") or []
            if not must and not must_not:
                issues.append(
                    ValidationIssue(
                        "high",
                        str(path),
                        f"{cid or '<unknown>'}: behavioral case must include non-empty must or must_not assertions",
                    )
                )

    if not has_positive:
        issues.append(ValidationIssue("high", str(path), "Test suite has no should-trigger case"))
    if not has_negative:
        issues.append(ValidationIssue("medium", str(path), "Test suite has no should-not-trigger case"))

    return issues


def discover_case_paths(root: Path) -> list[Path]:
    paths = set((root / "skills").rglob("tests/cases.yaml"))
    paths.update((root / "workflows").rglob("tests/cases.yaml"))
    return sorted(paths)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="cases.yaml files; defaults to all skill and workflow test suites")
    args = parser.parse_args()

    root = repo_root_from(__file__)
    schema = load_json(root / "scripts/validate/schemas/test-case.schema.json")
    paths = [Path(p).resolve() for p in args.paths] if args.paths else discover_case_paths(root)

    issues: list[ValidationIssue] = []
    for path in paths:
        issues.extend(validate_cases(path, schema))

    for issue in issues:
        print(issue)

    return 1 if any(i.severity in {"blocker", "high"} for i in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
