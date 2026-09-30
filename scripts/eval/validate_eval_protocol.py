from __future__ import annotations

import json
import sys
from pathlib import Path

from protocol import validate_receipt, validate_registry


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    errors = validate_registry(root)

    results_dir = root / "evals" / "results"
    if results_dir.exists():
        for path in sorted(results_dir.glob("*.json")):
            try:
                receipt = json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"{path}: invalid JSON: {exc}")
                continue
            for error in validate_receipt(receipt):
                errors.append(f"{path}: {error}")

    for error in errors:
        print(f"[BLOCKER] {error}")
    if not errors:
        print("Eval protocol: isolated inputs/rubrics and receipts are structurally valid")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
