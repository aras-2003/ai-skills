from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

FORBIDDEN_EXECUTOR_HEADINGS = (
    "## expected routing",
    "## expected output",
    "## expected behavior",
    "## expected behaviours",
    "## failure conditions",
    "## pass",
    "## pass criteria",
)

ALLOWED_STATUSES = {"NOT_RUN", "PASS", "FAIL", "REVIEW_REQUIRED"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_registry(root: Path) -> dict[str, list[dict[str, Any]]]:
    path = root / "evals" / "runtime-fixtures.yaml"
    data = load_yaml(path) or {}
    if data.get("schema_version") != "2.0":
        raise ValueError(f"{path}: expected schema_version 2.0")
    targets = data.get("targets")
    if not isinstance(targets, dict):
        raise ValueError(f"{path}: targets must be a mapping")
    return targets


def validate_executor_input(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lowered = text.lower()
    for heading in FORBIDDEN_EXECUTOR_HEADINGS:
        if heading in lowered:
            errors.append(f"{path}: executor input exposes evaluator section {heading!r}")
    return errors


def validate_registry(root: Path) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    for target, fixtures in load_registry(root).items():
        if not isinstance(fixtures, list) or not fixtures:
            errors.append(f"{target}: fixtures must be a non-empty list")
            continue
        for fixture in fixtures:
            if not isinstance(fixture, dict):
                errors.append(f"{target}: fixture must be a mapping")
                continue
            case_id = fixture.get("id")
            mode = fixture.get("mode")
            input_rel = fixture.get("input")
            rubric_rel = fixture.get("rubric")
            if not all(isinstance(x, str) and x for x in (case_id, mode, input_rel, rubric_rel)):
                errors.append(f"{target}: fixture requires id/mode/input/rubric strings")
                continue
            if case_id in seen_ids:
                errors.append(f"duplicate eval case id: {case_id}")
            seen_ids.add(case_id)
            if mode not in {"explicit", "natural-routing"}:
                errors.append(f"{case_id}: unsupported mode {mode!r}")
            input_path = root / input_rel
            rubric_path = root / rubric_rel
            if not input_path.exists():
                errors.append(f"{case_id}: missing input {input_rel}")
            else:
                errors.extend(validate_executor_input(input_path))
            if not rubric_path.exists():
                errors.append(f"{case_id}: missing rubric {rubric_rel}")
            elif input_path.resolve() == rubric_path.resolve():
                errors.append(f"{case_id}: input and rubric must be different files")
            if ".rubric." in Path(input_rel).name:
                errors.append(f"{case_id}: rubric path used as executor input")
    return errors


def build_execution_payload(root: Path, target: str, case_id: str) -> dict[str, Any]:
    fixtures = load_registry(root).get(target) or []
    fixture = next((x for x in fixtures if x.get("id") == case_id), None)
    if fixture is None:
        raise KeyError(f"Unknown eval target/case: {target}/{case_id}")
    input_path = root / fixture["input"]
    errors = validate_executor_input(input_path)
    if errors:
        raise ValueError("; ".join(errors))
    return {
        "case_id": case_id,
        "target": target,
        "mode": fixture["mode"],
        "input_path": fixture["input"],
        "input_sha256": sha256_file(input_path),
        "input": input_path.read_text(encoding="utf-8"),
    }


def evaluate_deterministic_assertions(output: str, rubric: dict[str, Any]) -> dict[str, Any]:
    rules = ((rubric.get("assertions") or {}).get("deterministic") or [])
    results: list[dict[str, Any]] = []
    for rule in rules:
        if not isinstance(rule, dict):
            results.append({"pass": False, "error": "assertion must be a mapping"})
            continue
        kind = rule.get("type")
        value = str(rule.get("value") or "")
        if kind == "contains":
            ok = value in output
        elif kind == "not_contains":
            ok = value not in output
        else:
            results.append({"pass": False, "error": f"unsupported assertion type: {kind}"})
            continue
        results.append({"type": kind, "value": value, "pass": ok})
    return {"passed": all(x.get("pass") is True for x in results), "results": results}


def new_not_run_receipt(
    *,
    root: Path,
    target: str,
    case_id: str,
    source_revision: str,
    component_version: str,
    component_digest: str,
    runtime_id: str = "NOT_AVAILABLE",
    reason: str,
) -> dict[str, Any]:
    payload = build_execution_payload(root, target, case_id)
    fixture = next(x for x in load_registry(root)[target] if x["id"] == case_id)
    rubric_path = root / fixture["rubric"]
    return {
        "schema_version": "1.0",
        "case_id": case_id,
        "target": target,
        "mode": payload["mode"],
        "status": "NOT_RUN",
        "assisted": False,
        "reason": reason,
        "source_revision": source_revision,
        "component_version": component_version,
        "component_digest": component_digest,
        "input_path": payload["input_path"],
        "input_sha256": payload["input_sha256"],
        "rubric_path": fixture["rubric"],
        "rubric_sha256": sha256_file(rubric_path),
        "runtime": {
            "id": runtime_id,
            "model": None,
            "reasoning": None,
        },
        "actual_output": None,
        "tool_trace": [],
        "assertions": [],
        "reviewer": None,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def validate_receipt(receipt: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version", "case_id", "target", "mode", "status", "assisted",
        "source_revision", "component_version", "component_digest",
        "input_path", "input_sha256", "rubric_path", "rubric_sha256",
        "runtime", "actual_output", "tool_trace", "assertions", "timestamp",
    }
    missing = sorted(required - set(receipt))
    if missing:
        errors.append("missing receipt fields: " + ", ".join(missing))
    status = receipt.get("status")
    if status not in ALLOWED_STATUSES:
        errors.append(f"invalid receipt status: {status!r}")
    if status == "NOT_RUN" and receipt.get("actual_output") is not None:
        errors.append("NOT_RUN receipt must not contain actual_output")
    if status in {"PASS", "FAIL"} and not receipt.get("actual_output"):
        errors.append(f"{status} receipt requires actual_output")
    return errors


def dumps_receipt(receipt: dict[str, Any]) -> str:
    return json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
