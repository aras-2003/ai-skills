from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

REQUIRED_FIELDS = {
    "schema_version",
    "case_id",
    "case_digest",
    "component",
    "component_version",
    "component_digest",
    "source_revision",
    "runtime",
    "mode",
    "input",
    "rubric",
    "result",
    "reviewer",
    "timestamp",
}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_rubric(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: rubric must be a mapping")
    return data


def validate_receipt(data: dict[str, Any], root: Path | None = None) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED_FIELDS - set(data))
    if missing:
        errors.append("missing fields: " + ", ".join(missing))

    if data.get("result") not in {"PASS", "FAIL", "NOT_RUN", "PENDING_REVIEW"}:
        errors.append("result must be PASS, FAIL, NOT_RUN or PENDING_REVIEW")
    if data.get("mode") not in {"explicit", "natural-routing", "real-use"}:
        errors.append("mode must be explicit, natural-routing or real-use")

    inp = data.get("input") or {}
    rubric = data.get("rubric") or {}
    if not isinstance(inp, dict) or not inp.get("path") or not inp.get("digest"):
        errors.append("input.path and input.digest are required")
    if not isinstance(rubric, dict) or not rubric.get("path") or not rubric.get("digest"):
        errors.append("rubric.path and rubric.digest are required")

    runtime = data.get("runtime") or {}
    if not isinstance(runtime, dict):
        errors.append("runtime must be a mapping")
    elif data.get("result") != "NOT_RUN":
        for key in ("provider", "model_id"):
            if not runtime.get(key):
                errors.append(f"runtime.{key} is required for executed runs")

    if root and isinstance(inp, dict) and inp.get("path"):
        p = root / str(inp["path"])
        if p.exists() and inp.get("digest") != sha256_file(p):
            errors.append("input digest does not match current file")
    if root and isinstance(rubric, dict) and rubric.get("path"):
        p = root / str(rubric["path"])
        if p.exists() and rubric.get("digest") != sha256_file(p):
            errors.append("rubric digest does not match current file")

    component = data.get("component") or {}
    if not isinstance(component, dict) or not component.get("name") or not component.get("path"):
        errors.append("component.name and component.path are required")
    elif root and component.get("path"):
        p = root / str(component["path"])
        if p.exists() and data.get("component_digest") != sha256_file(p):
            errors.append("component digest does not match current file")

    return errors


def make_not_run_receipt(
    *,
    case_id: str,
    input_path: Path,
    rubric_path: Path,
    component_name: str,
    component_path: Path,
    component_version: str,
    source_revision: str,
    root: Path,
    reason: str,
) -> dict[str, Any]:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    return {
        "schema_version": "1.0",
        "case_id": case_id,
        "case_digest": sha256_file(input_path),
        "component": {"name": component_name, "path": component_path.relative_to(root).as_posix()},
        "component_version": component_version,
        "component_digest": sha256_file(component_path),
        "source_revision": source_revision,
        "runtime": {"provider": None, "model_id": None, "reasoning": None},
        "mode": "explicit",
        "prompt": None,
        "available_catalog": [],
        "input": {"path": input_path.relative_to(root).as_posix(), "digest": sha256_file(input_path)},
        "output": None,
        "trace": [],
        "rubric": {"path": rubric_path.relative_to(root).as_posix(), "digest": sha256_file(rubric_path)},
        "assertions": [],
        "result": "NOT_RUN",
        "reviewer": "pending",
        "assisted": False,
        "timestamp": now,
        "notes": reason,
    }


def write_receipt(path: Path, receipt: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
