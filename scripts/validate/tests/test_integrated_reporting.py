from __future__ import annotations

from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[3]

TARGET_WORKFLOWS = [
    "investment-opportunity-hunter",
    "investment-security-review",
    "investment-portfolio-review",
    "investment-attention-review",
    "investment-theme-discovery",
    "oaf-health-check",
    "oaf-operating-model-redesign",
    "oaf-governance-redesign",
    "oaf-enterprise-architecture-review",
    "oaf-transformation-design",
    "commerce-opportunity-review",
    "commerce-product-deep-dive",
]


class IntegratedReportingTests(unittest.TestCase):
    def test_target_workflows_use_integrated_report_section(self) -> None:
        for name in TARGET_WORKFLOWS:
            with self.subTest(name=name):
                text = (ROOT / "workflows" / name / "WORKFLOW.md").read_text(encoding="utf-8")
                self.assertIn("## Integrated report presentation", text)
                self.assertIn("report-composer", text)
                self.assertIn("directly in the chat response by default", text)
                self.assertIn("only when the user explicitly requests", text)
                self.assertNotIn("## Visual presentation", text)

    def test_runtime_registry_exposes_composer_before_renderer(self) -> None:
        registry = yaml.safe_load((ROOT / "workflows" / "runtime-registry.yaml").read_text(encoding="utf-8"))
        by_name = {item["name"]: item for item in registry["workflows"]}
        for name in TARGET_WORKFLOWS:
            with self.subTest(name=name):
                optional = [item["name"] for item in by_name[name]["dependencies"]["optional"]]
                self.assertIn("report-composer", optional)
                self.assertIn("visual-output-design", optional)
                self.assertLess(optional.index("report-composer"), optional.index("visual-output-design"))

    def test_composer_and_renderer_contracts_are_separate(self) -> None:
        composer = (ROOT / "skills/meta/report-composer/SKILL.md").read_text(encoding="utf-8")
        renderer = (ROOT / "skills/meta/visual-output-design/SKILL.md").read_text(encoding="utf-8")
        contract = (ROOT / "skills/meta/report-composer/references/report-state-and-evidence-contract.md").read_text(encoding="utf-8")
        quality_cases = (ROOT / "skills/meta/report-composer/tests/quality-cases.yaml").read_text(encoding="utf-8")

        self.assertIn("PAYLOAD_RENDERED", composer)
        self.assertIn("NOT_OBSERVABLE", composer)
        self.assertIn("analysis_state", composer)
        self.assertNotIn("report_status: PASS", composer)
        self.assertIn("PAYLOAD_RENDERED", renderer)
        self.assertIn("client display is always `NOT_OBSERVABLE`", renderer.lower())
        self.assertIn("PENDING_CLIENT_VALIDATION", contract)
        self.assertIn("USER_PROVIDED", contract)
        self.assertIn("causal attribution", contract.lower())
        self.assertIn("quality-payload-client-not-observable", quality_cases)
        self.assertIn("quality-user-provided-unreproducible-metric", quality_cases)

    def test_portfolio_attribution_fails_closed_without_causal_evidence(self) -> None:
        workflow = (ROOT / "workflows/investment-portfolio-review/WORKFLOW.md").read_text(encoding="utf-8")
        state = (ROOT / "skills/investing/portfolio-state-review/SKILL.md").read_text(encoding="utf-8")
        cases = (ROOT / "skills/investing/portfolio-state-review/tests/cases.yaml").read_text(encoding="utf-8")
        self.assertIn("attribution `UNKNOWN`", workflow)
        self.assertIn("Absence of observed transactions is not evidence", workflow)
        self.assertIn("never infer \"market-driven\"", state)
        self.assertIn("portfolio-attribution-insufficient", cases)


if __name__ == "__main__":
    unittest.main()
