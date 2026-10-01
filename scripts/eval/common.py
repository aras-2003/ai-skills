from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import yaml


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_registry(root: Path | None = None) -> dict[str, list[dict[str, Any]]]:
    root = root or repo_root()
    path = root / "evals" / "runtime-fixtures.yaml"
    data = load_yaml(path) or {}
    targets = data.get("targets")
    if not isinstance(targets, dict):
        raise ValueError(f"{path}: targets must be a mapping")
    return targets


def load_campaign_cases(root: Path | None = None) -> dict[str, dict[str, Any]]:
    root = root or repo_root()
    config_path = root / "evals" / "campaigns" / "runtime-validation-2026-10" / "campaign.yaml"
    if not config_path.is_file():
        return {}
    config = load_yaml(config_path) or {}
    result: dict[str, dict[str, Any]] = {}

    runtime_targets = load_registry(root)
    wanted = set(config.get("commerce_case_ids") or [])
    for target, cases in runtime_targets.items():
        for case in cases:
            if case.get("id") in wanted:
                result[str(case["id"])] = {
                    **case,
                    "target": target,
                    "suite": "commerce",
                }

    routing_path = root / str(config.get("routing_registry") or "")
    routing = load_yaml(routing_path) or {}
    for case in routing.get("cases") or []:
        if not isinstance(case, dict):
            continue
        rubric_path = root / str(case.get("rubric") or "")
        rubric = load_yaml(rubric_path) or {}
        cid = str(case.get("id") or "")
        if cid:
            result[cid] = {
                "id": cid,
                "target": str(rubric.get("expected_target") or "runtime-routing"),
                "mode": "natural-routing",
                "input": str(case.get("input") or ""),
                "rubric": str(case.get("rubric") or ""),
                "suite": "routing",
            }

    base = root / "evals" / "campaigns" / "runtime-validation-2026-10" / "executive"
    for cid in config.get("executive_case_ids") or []:
        cid = str(cid)
        result[cid] = {
            "id": cid,
            "target": "executive-role-evaluator",
            "mode": "natural-routing",
            "input": (base / f"{cid}.input.md").relative_to(root).as_posix(),
            "rubric": (base / f"{cid}.rubric.yaml").relative_to(root).as_posix(),
            "suite": "executive-role",
        }

    for case in config.get("fallback_cases") or []:
        if not isinstance(case, dict):
            continue
        cid = str(case.get("id") or "")
        if cid:
            result[cid] = {
                "id": cid,
                "target": str(case.get("target") or ""),
                "mode": "explicit",
                "input": str(case.get("input") or ""),
                "rubric": str(case.get("rubric") or ""),
                "suite": "production-fallback",
            }
    return result
