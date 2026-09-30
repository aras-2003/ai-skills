from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from common import load_registry, repo_root, sha256_file

VALID_STATUSES = {"NOT_RUN", "REVIEW_REQUIRED", "PASS", "FAIL"}


def find_case(root: Path, case_id: str) -> tuple[str, dict[str, Any]]:
    for target, cases in load_registry(root).items():
        for case in cases:
            if case.get("id") == case_id:
                return target, case
    raise KeyError(f"unknown case id: {case_id}")


def create_receipt(args: argparse.Namespace) -> dict[str, Any]:
    root = repo_root()
    target, case = find_case(root, args.case_id)
    input_path = root / case["input"]
    rubric_path = root / case["rubric"]

    status = args.status
    if status not in VALID_STATUSES:
        raise ValueError(f"invalid status: {status}")
    if status in {"PASS", "FAIL", "REVIEW_REQUIRED"} and not args.output:
        raise ValueError(f"{status} requires --output")
    if status in {"PASS", "FAIL", "REVIEW_REQUIRED"}:
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

    output_path = Path(args.output).resolve() if args.output else None
    record = {
        "schema_version": "1.0",
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
            "name": args.component or target,
            "version": args.component_version,
            "content_sha256": args.component_digest,
        },
        "source_revision": args.source_revision,
        "runtime": {
            "provider": args.provider,
            "model_id": args.model_id,
            "reasoning": args.reasoning,
            "catalog": args.catalog,
        },
        "execution": {
            "assisted": bool(args.assisted),
            "prompt": args.prompt,
            "actual_output_path": str(output_path) if output_path else None,
            "actual_output_sha256": sha256_file(output_path) if output_path else None,
            "tool_trace_path": args.tool_trace,
        },
        "evaluation": {
            "status": status,
            "rubric_version": "1.0",
            "reviewer": args.reviewer,
            "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "note": args.note,
        },
    }

    schema = json.loads((root / "scripts/eval/schemas/evidence-record.schema.json").read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(record), key=lambda e: list(e.path))
    if errors:
        raise ValueError("; ".join(e.message for e in errors))
    return record


def validate_receipt(path: Path) -> list[str]:
    root = repo_root()
    data = json.loads(path.read_text(encoding="utf-8"))
    schema = json.loads((root / "scripts/eval/schemas/evidence-record.schema.json").read_text(encoding="utf-8"))
    errors = [f"schema: {e.message}" for e in Draft202012Validator(schema).iter_errors(data)]
    case = data.get("case", {})
    try:
        _, current = find_case(root, case.get("id", ""))
    except KeyError as exc:
        return errors + [str(exc)]
    input_path = root / current["input"]
    rubric_path = root / current["rubric"]
    if case.get("input_sha256") != sha256_file(input_path):
        errors.append("stale evidence: input digest mismatch")
    if case.get("rubric_sha256") != sha256_file(rubric_path):
        errors.append("stale evidence: rubric digest mismatch")
    if data.get("evaluation", {}).get("status") == "PASS" and data.get("execution", {}).get("assisted"):
        errors.append("assisted run cannot be PASS")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    create = sub.add_parser("create")
    create.add_argument("--case-id", required=True)
    create.add_argument("--status", required=True, choices=sorted(VALID_STATUSES))
    create.add_argument("--source-revision", required=True)
    create.add_argument("--component")
    create.add_argument("--component-version")
    create.add_argument("--component-digest")
    create.add_argument("--provider")
    create.add_argument("--model-id")
    create.add_argument("--reasoning")
    create.add_argument("--catalog", nargs="*", default=[])
    create.add_argument("--prompt")
    create.add_argument("--output")
    create.add_argument("--tool-trace")
    create.add_argument("--reviewer")
    create.add_argument("--assisted", action="store_true")
    create.add_argument("--note")
    create.add_argument("--write", required=True)

    validate = sub.add_parser("validate")
    validate.add_argument("paths", nargs="+")

    args = parser.parse_args()
    if args.cmd == "create":
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
