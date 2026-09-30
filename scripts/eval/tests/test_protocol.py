from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1]))

from protocol import (  # noqa: E402
    evaluate_deterministic_assertions,
    new_not_run_receipt,
    validate_executor_input,
    validate_receipt,
)


class EvalProtocolTests(unittest.TestCase):
    def test_executor_input_rejects_rubric_sections(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "case.input.md"
            path.write_text("# Case\n\n## Scenario\nX\n\n## Expected routing\nsecret\n", encoding="utf-8")
            self.assertTrue(validate_executor_input(path))

    def test_deterministic_assertions_distinguish_good_and_bad_output(self) -> None:
        rubric = {
            "assertions": {
                "deterministic": [
                    {"type": "contains", "value": "UNKNOWN"},
                    {"type": "not_contains", "value": "invented-value"},
                ]
            }
        }
        self.assertTrue(evaluate_deterministic_assertions("Price: UNKNOWN", rubric)["passed"])
        self.assertFalse(evaluate_deterministic_assertions("Price: invented-value", rubric)["passed"])

    def test_not_run_is_visible_and_cannot_carry_output(self) -> None:
        receipt = {
            "schema_version": "1.0",
            "case_id": "x",
            "target": "x",
            "mode": "explicit",
            "status": "NOT_RUN",
            "assisted": False,
            "source_revision": "abc",
            "component_version": "1.0.0",
            "component_digest": "123",
            "input_path": "x.input.md",
            "input_sha256": "a",
            "rubric_path": "x.rubric.yaml",
            "rubric_sha256": "b",
            "runtime": {"id": "NOT_AVAILABLE", "model": None, "reasoning": None},
            "actual_output": None,
            "tool_trace": [],
            "assertions": [],
            "timestamp": "2026-09-30T00:00:00+00:00",
        }
        self.assertEqual(validate_receipt(receipt), [])
        receipt["actual_output"] = "fake"
        self.assertTrue(validate_receipt(receipt))


if __name__ == "__main__":
    unittest.main()
