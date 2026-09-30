from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1]))

import routing_proxy


class RoutingProxyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = HERE.parents[3]

    def test_good_selection_passes(self) -> None:
        ok, _ = routing_proxy.evaluate_selection(
            self.root, "career-company-facts-pl", "company-context-research"
        )
        self.assertTrue(ok)

    def test_competing_wrong_selection_fails(self) -> None:
        ok, message = routing_proxy.evaluate_selection(
            self.root, "career-company-facts-pl", "executive-role-evaluator"
        )
        self.assertFalse(ok)
        self.assertIn("expected", message)

    def test_oaf_wrong_design_escalation_fails(self) -> None:
        ok, _ = routing_proxy.evaluate_selection(
            self.root, "oaf-decision-pl", "governance-design"
        )
        self.assertFalse(ok)

    def test_unknown_case_fails(self) -> None:
        ok, _ = routing_proxy.evaluate_selection(self.root, "missing", "anything")
        self.assertFalse(ok)


if __name__ == "__main__":
    unittest.main()
