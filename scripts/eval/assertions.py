from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml


def evaluate(output: str, rubric: dict[str, Any]) -> tuple[bool, list[str]]:
    checks = ((rubric.get("assertions") or {}).get("deterministic") or [])
    failures: list[str] = []
    for index, check in enumerate(checks, start=1):
        if not isinstance(check, dict) or len(check) != 1:
            failures.append(f"assertion {index}: invalid assertion shape")
            continue
        kind, value = next(iter(check.items()))
        if kind == "contains":
            if str(value).lower() not in output.lower():
                failures.append(f"assertion {index}: missing required text {value!r}")
        elif kind == "not_contains":
            if str(value).lower() in output.lower():
                failures.append(f"assertion {index}: prohibited text present {value!r}")
        elif kind == "regex":
            if re.search(str(value), output, flags=re.IGNORECASE | re.MULTILINE) is None:
                failures.append(f"assertion {index}: regex did not match {value!r}")
        elif kind == "max_occurrences":
            if not isinstance(value, dict) or "text" not in value or "max" not in value:
                failures.append(f"assertion {index}: invalid max_occurrences")
            else:
                count = output.lower().count(str(value["text"]).lower())
                if count > int(value["max"]):
                    failures.append(
                        f"assertion {index}: {value['text']!r} occurs {count}, max {value['max']}"
                    )
        else:
            failures.append(f"assertion {index}: unknown assertion type {kind!r}")
    return not failures, failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rubric", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    rubric = yaml.safe_load(args.rubric.read_text(encoding="utf-8")) or {}
    output = args.output.read_text(encoding="utf-8")
    ok, failures = evaluate(output, rubric)
    for failure in failures:
        print(f"[FAIL] {failure}")
    if ok:
        print("Deterministic assertions: PASS")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
