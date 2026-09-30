from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml


def load_registry(root: Path) -> dict[str, dict[str, Any]]:
    data = yaml.safe_load((root / "evals" / "routing" / "registry.yaml").read_text(encoding="utf-8")) or {}
    cases = data.get("cases") or []
    return {str(item["id"]): item for item in cases if isinstance(item, dict) and item.get("id")}


def evaluate_selection(root: Path, case_id: str, selected_target: str) -> tuple[bool, str]:
    cases = load_registry(root)
    if case_id not in cases:
        return False, f"unknown routing case: {case_id}"
    case = cases[case_id]
    rubric_path = root / str(case.get("rubric") or "")
    rubric = yaml.safe_load(rubric_path.read_text(encoding="utf-8")) or {}
    expected = str(rubric.get("expected_target") or "").strip()
    if not expected:
        return False, f"{case_id}: rubric has no expected_target"
    if selected_target != expected:
        return False, f"{case_id}: selected {selected_target!r}, expected {expected!r}"
    return True, f"{case_id}: selection matches expected target {expected}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic routing-selection checker. This is a proxy assertion only; it does not execute native runtime routing."
    )
    parser.add_argument("--case-id", required=True)
    parser.add_argument("--selected-target", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    ok, message = evaluate_selection(root, args.case_id, args.selected_target)
    print(message)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
