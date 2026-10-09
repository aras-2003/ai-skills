from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts/capabilities"))
from contract import assessment_for, load_contract  # noqa: E402
from validate_contract import validate  # noqa: E402


class CapabilityContractTests(unittest.TestCase):
    def test_unreviewed_component_is_not_misrepresented_as_no_capabilities(self) -> None:
        contract = load_contract(ROOT)
        result = assessment_for(contract, "job-discovery")
        self.assertEqual("UNASSESSED", result["status"])
        self.assertTrue(all(value == "unassessed" for value in result["requirements"].values()))

    def test_partial_capability_declaration_is_not_reported_as_assessed(self) -> None:
        contract = load_contract(ROOT)
        partial = dict(contract)
        partial["component_declarations"] = {
            "example": {
                "requirements": {
                    "network": "read",
                    "filesystem": "none",
                    "shell_exec": "none",
                    "credentials": "unassessed",
                    "external_actions": "none",
                }
            }
        }
        result = assessment_for(partial, "example")
        self.assertEqual("UNASSESSED", result["status"])

    def test_fully_reviewed_declaration_remains_declared(self) -> None:
        contract = load_contract(ROOT)
        reviewed = dict(contract)
        reviewed["component_declarations"] = {
            "example": {
                "requirements": {
                    "network": "read",
                    "filesystem": "none",
                    "shell_exec": "none",
                    "credentials": "none",
                    "external_actions": "approval_required",
                }
            }
        }
        result = assessment_for(reviewed, "example")
        self.assertEqual("DECLARED", result["status"])

    def test_report_covers_skills_and_workflows_without_claiming_runtime_support(self) -> None:
        report, errors = validate(ROOT)
        self.assertFalse(errors)
        self.assertGreater(report["component_count"], 60)
        self.assertEqual(report["component_count"], report["unassessed_count"])
        self.assertIn("not evidence of no permissions", report["assessment_semantics"])


if __name__ == "__main__":
    unittest.main()
