from __future__ import annotations

import argparse
import json
import os
import tempfile
import unittest
from pathlib import Path
import sys

HERE = Path(__file__).resolve()
EVAL_DIR = HERE.parents[1]
ROOT = HERE.parents[3]
if str(EVAL_DIR) not in sys.path:
    sys.path.insert(0, str(EVAL_DIR))

import campaign
import receipt
from common import load_campaign_cases


class RuntimeCampaignTests(unittest.TestCase):
    def setUp(self) -> None:
        (ROOT / ".tmp").mkdir(exist_ok=True)

    def test_campaign_resolves_exact_scope_and_isolation(self) -> None:
        self.assertEqual([], campaign.validate_campaign())
        cases = load_campaign_cases(ROOT)
        self.assertEqual(38, len(cases))
        counts = {}
        for case in cases.values():
            counts[case["suite"]] = counts.get(case["suite"], 0) + 1
        self.assertEqual(
            {"commerce": 6, "routing": 16, "executive-role": 14, "production-fallback": 2},
            counts,
        )

    def test_prepare_locks_package_catalog_components_and_fallback_absence(self) -> None:
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            out = Path(td) / "campaign"
            campaign.prepare(out)
            lock = json.loads((out / "lock.json").read_text(encoding="utf-8"))
            self.assertEqual("ff012e494f5b2f71803f850d71d20f54a3315e2b", lock["behavior_source_revision"])
            self.assertEqual("arek-ai-skills", lock["packages"]["production"]["name"])
            self.assertEqual("1.8.0", lock["packages"]["production"]["version"])
            self.assertEqual("arek-ai-skills-lab", lock["packages"]["lab"]["name"])
            self.assertEqual("0.3.0", lock["packages"]["lab"]["version"])
            self.assertNotIn("strategy-to-execution-diagnostic", lock["expected_catalogs"]["production"])
            self.assertNotIn("organizational-interface-review", lock["expected_catalogs"]["production"])
            self.assertIn("organizational-interface-review", lock["expected_catalogs"]["lab"])
            self.assertTrue(lock["components"])
            self.assertTrue(all(x.get("version") and x.get("content_sha256") for x in lock["components"]))
            self.assertEqual("production", lock["case_channels"]["fallback-strategy-production-001"])
            self.assertEqual("production", lock["case_channels"]["fallback-interface-production-001"])

    def test_smoke_rejects_simultaneous_production_and_lab(self) -> None:
        lock = {
            "packages": {
                "production": {"name": "arek-ai-skills", "version": "1.8.0"},
                "lab": {"name": "arek-ai-skills-lab", "version": "0.3.0"},
            },
            "expected_catalogs": {"production": ["a", "b"], "lab": ["c"]},
        }
        observed = {
            "channel": "production",
            "package": {"name": "arek-ai-skills", "version": "1.8.0"},
            "enabled_packages": ["arek-ai-skills", "arek-ai-skills-lab"],
            "catalog": ["a", "b"],
            "runtime": {
                "provider": "provider",
                "model_id": "model",
                "reasoning": "medium",
                "available_tools": [],
            },
        }
        with tempfile.TemporaryDirectory() as td:
            lp = Path(td) / "lock.json"
            op = Path(td) / "observed.json"
            lp.write_text(json.dumps(lock), encoding="utf-8")
            op.write_text(json.dumps(observed), encoding="utf-8")
            errors = campaign.verify_smoke(lp, op)
        self.assertTrue(any("simultaneously enabled" in e for e in errors))

    def test_receipt_paths_are_portable_and_trace_is_hashed(self) -> None:
        cfg = campaign.config()
        cases = load_campaign_cases(ROOT)
        case = cases["case-001-premium-vs-generic"]
        version, digest = receipt.current_component_identity(ROOT, case["target"])
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            run = Path(td)
            output = run / "output.md"
            trace = run / "trace.json"
            output.write_text("runtime output\n", encoding="utf-8")
            trace.write_text(json.dumps({"selected_capabilities": [case["target"]]}), encoding="utf-8")
            ns = argparse.Namespace(
                case_id=case["id"],
                status="REVIEW_REQUIRED",
                evidence_scope="current-version",
                source_revision=cfg["behavior_source_revision"],
                component=case["target"],
                component_version=version,
                component_digest=digest,
                provider="provider",
                model_id="model",
                reasoning="medium",
                catalog=[case["target"]],
                tools=["web"],
                prompt=(ROOT / case["input"]).read_text(encoding="utf-8"),
                output=str(output),
                tool_trace=str(trace),
                reviewer="unit-test",
                assisted=False,
                note=None,
            )
            old = os.environ.get("SOURCE_REVISION")
            os.environ["SOURCE_REVISION"] = cfg["behavior_source_revision"]
            try:
                record = receipt.create_receipt(ns)
            finally:
                if old is None:
                    os.environ.pop("SOURCE_REVISION", None)
                else:
                    os.environ["SOURCE_REVISION"] = old
            self.assertFalse(Path(record["execution"]["actual_output_path"]).is_absolute())
            self.assertFalse(Path(record["execution"]["tool_trace_path"]).is_absolute())
            self.assertEqual(64, len(record["execution"]["tool_trace_sha256"]))
            errors = receipt.validate_receipt_data(
                record,
                root=ROOT,
                current_revision=record["source_revision"],
            )
            self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
