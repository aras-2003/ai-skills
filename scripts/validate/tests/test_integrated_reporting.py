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
        self.assertIn("The report is the product", composer)
        self.assertIn("inline visual", composer.lower())
        self.assertIn("does not own the structure of a full report", renderer)


if __name__ == "__main__":
    unittest.main()
