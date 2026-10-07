from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
RUNTIME = ROOT / "runtime" / "mcp" / "investment_runtime.py"


def load_runtime():
    spec = importlib.util.spec_from_file_location("skills_factory_investment_runtime", RUNTIME)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load investment runtime")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class InvestmentRuntimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.runtime = load_runtime()

    def assert_route(self, prompt: str, route: str, child: str) -> None:
        result = self.runtime.route_investment_request(prompt)
        self.assertTrue(result["is_investment_request"])
        self.assertEqual(route, result["route"])
        self.assertEqual(child, result["child_workflow"])
        self.assertTrue(result["must_invoke_child_workflow"])

    def test_server_instructions_require_pre_analysis_routing(self) -> None:
        instructions = self.runtime.SERVER_INSTRUCTIONS
        self.assertIn("Before substantive investment analysis", instructions)
        self.assertIn("route_investment_request", instructions)
        self.assertIn("investment-portfolio-review", instructions)
        self.assertIn("Do not replace", instructions)

    def test_routes_portfolio_weights(self) -> None:
        self.assert_route(
            "Review this portfolio: ACN 25.26%, IUIT 22.16%, SMH 5.68%. What requires attention?",
            "portfolio",
            "investment-portfolio-review",
        )

    def test_routes_single_security(self) -> None:
        self.assert_route(
            "Review MU end to end: thesis, valuation, downside and portfolio fit.",
            "security",
            "investment-security-review",
        )

    def test_ambiguous_share_ownership_requests_front_door_clarification(self) -> None:
        for prompt in (
            "Mam akcje. Co zrobić?",
            "Mam akcje kilku spółek. Co powinienem z nimi zrobić?",
            "I own some shares. What should I do?",
        ):
            with self.subTest(prompt=prompt):
                result = self.runtime.route_investment_request(prompt)
                self.assertTrue(result["is_investment_request"])
                self.assertEqual("unknown", result["route"])
                self.assertEqual("investment-os-review", result["child_workflow"])
                self.assertIn("ambiguous", result["reason"])
                self.assertTrue(result["must_invoke_child_workflow"])

    def test_direct_stock_review_still_routes(self) -> None:
        self.assert_route("Review stock ACN", "security", "investment-security-review")

    def test_routes_opportunity_discovery(self) -> None:
        self.assert_route(
            "Chcę znaleźć kilka nowych spółek do dalszego researchu. Nie mam konkretnego tickera.",
            "opportunity",
            "investment-opportunity-hunter",
        )

    def test_routes_theme_research(self) -> None:
        self.assert_route(
            "Research investment themes around AI infrastructure and second-order beneficiaries.",
            "theme",
            "investment-theme-discovery",
        )

    def test_routes_attention_triage(self) -> None:
        self.assert_route(
            "Pojawiły się nowe informacje o mojej spółce. Czy to zmienia tezę inwestycyjną?",
            "attention",
            "investment-attention-review",
        )

    def test_routes_policy_design(self) -> None:
        self.assert_route(
            "Pomóż mi ustalić zasady portfela: maksymalny udział jednej spółki i limity sektorowe.",
            "policy",
            "investment-policy-design",
        )

    def test_empty_request_does_not_force_child(self) -> None:
        result = self.runtime.route_investment_request("   ")
        self.assertFalse(result["is_investment_request"])
        self.assertFalse(result["must_invoke_child_workflow"])


if __name__ == "__main__":
    unittest.main()
