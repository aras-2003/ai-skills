from __future__ import annotations

import argparse
import json
import tempfile
import unittest
from pathlib import Path
import sys

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1]))

import receipt
import validate_isolation


class EvalProtocolTests(unittest.TestCase):
    def test_registry_inputs_are_isolated(self) -> None:
        errors = validate_isolation.validate_registry(HERE.parents[3])
        self.assertEqual([], errors)

    def test_assisted_pass_is_rejected(self) -> None:
        args = argparse.Namespace(
            case_id="case-001-premium-vs-generic",
            status="PASS",
            source_revision="abcdef1234567",
            component="commerce-product-deep-dive",
            component_version="1.0.0",
            component_digest=None,
            provider="test",
            model_id="test",
            reasoning="none",
            catalog=[],
            prompt="test",
            output=__file__,
            tool_trace=None,
            reviewer="unit-test",
            assisted=True,
            note=None,
        )
        with self.assertRaisesRegex(ValueError, "assisted runs cannot be recorded as PASS"):
            receipt.create_receipt(args)

    def test_not_run_does_not_need_output(self) -> None:
        args = argparse.Namespace(
            case_id="case-001-premium-vs-generic",
            status="NOT_RUN",
            source_revision="abcdef1234567",
            component="commerce-product-deep-dive",
            component_version="1.0.0",
            component_digest=None,
            provider=None,
            model_id=None,
            reasoning=None,
            catalog=[],
            prompt=None,
            output=None,
            tool_trace=None,
            reviewer=None,
            assisted=False,
            note="runtime unavailable",
        )
        record = receipt.create_receipt(args)
        self.assertEqual("NOT_RUN", record["evaluation"]["status"])
        self.assertIsNone(record["execution"]["actual_output_path"])

    def test_stale_input_digest_is_detected(self) -> None:
        args = argparse.Namespace(
            case_id="case-001-premium-vs-generic",
            status="NOT_RUN",
            source_revision="abcdef1234567",
            component="commerce-product-deep-dive",
            component_version="1.0.0",
            component_digest=None,
            provider=None,
            model_id=None,
            reasoning=None,
            catalog=[],
            prompt=None,
            output=None,
            tool_trace=None,
            reviewer=None,
            assisted=False,
            note=None,
        )
        record = receipt.create_receipt(args)
        record["case"]["input_sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "receipt.json"
            p.write_text(json.dumps(record), encoding="utf-8")
            errors = receipt.validate_receipt(p)
        self.assertTrue(any("input digest mismatch" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
