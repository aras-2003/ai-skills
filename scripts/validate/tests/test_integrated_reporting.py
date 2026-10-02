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
        self.assertIn("The report is the product", composer)
        self.assertIn("inline visual", composer.lower())
        self.assertIn("in the chat response by default", composer)
        self.assertIn("Do not create an HTML/PDF/Figma/deck/file unless the user explicitly requests", composer)
        self.assertIn("does not own the structure of a full report", renderer)
        self.assertIn("external-artifact renderer", renderer)

    def test_external_artifact_is_opt_in_not_fallback(self) -> None:
        composer = (ROOT / "skills/meta/report-composer/SKILL.md").read_text(encoding="utf-8")
        routing = (ROOT / "skills/meta/visual-output-design/references/tool-routing.md").read_text(encoding="utf-8")
        composition = (ROOT / "skills/meta/report-composer/references/composition-rules.md").read_text(encoding="utf-8")
        self.assertIn("Never generate an external file merely as a fallback", composer)
        self.assertIn("Never create HTML/PDF/Figma/deck/file output merely because", routing)
        self.assertIn("Default delivery is the report itself in the chat response", composition)

    def test_quality_standard_is_intrinsic(self) -> None:
        composer = (ROOT / "skills/meta/report-composer/SKILL.md").read_text(encoding="utf-8")
        standard = (ROOT / "skills/meta/report-composer/references/report-quality-standard.md").read_text(encoding="utf-8")
        renderer = (ROOT / "skills/meta/visual-output-design/SKILL.md").read_text(encoding="utf-8")
        design = (ROOT / "skills/meta/visual-output-design/references/design-system.md").read_text(encoding="utf-8")
        self.assertIn("report-quality-standard.md", composer)
        self.assertIn("without requiring the user to spell out formatting", composer)
        self.assertIn("Start with an executive summary of 3–5", standard)
        self.assertIn("default to 2–3 detailed candidates", standard)
        self.assertIn("Do not expose raw Mermaid code fences", renderer)
        self.assertIn("Mermaid xychart", design)
        self.assertIn("external market data", standard.lower())

    def test_visual_floor_is_intrinsic(self) -> None:
        composer = (ROOT / "skills/meta/report-composer/SKILL.md").read_text(encoding="utf-8")
        standard = (ROOT / "skills/meta/report-composer/references/report-quality-standard.md").read_text(encoding="utf-8")
        profiles = (ROOT / "skills/meta/report-composer/references/report-profiles.md").read_text(encoding="utf-8")
        renderer = (ROOT / "skills/meta/visual-output-design/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("visual-floor rule", composer)
        self.assertIn("Visual floor:", standard)
        self.assertIn("include at least one portfolio-composition/concentration visual", standard)
        self.assertIn("required visual-floor slot", profiles)
        self.assertIn("text-only is not a successful substitute", renderer)

    def test_required_visuals_fail_closed_without_renderer(self) -> None:
        composer = (ROOT / "skills/meta/report-composer/SKILL.md").read_text(encoding="utf-8")
        standard = (ROOT / "skills/meta/report-composer/references/report-quality-standard.md").read_text(encoding="utf-8")
        routing = (ROOT / "skills/meta/visual-output-design/references/tool-routing.md").read_text(encoding="utf-8")
        renderer = (ROOT / "skills/meta/visual-output-design/SKILL.md").read_text(encoding="utf-8")
        quality_cases = (ROOT / "skills/meta/report-composer/tests/quality-cases.yaml").read_text(encoding="utf-8")

        for text in (composer, standard, routing, renderer, quality_cases):
            self.assertIn("BLOCKED_NO_RENDERER", text)

        self.assertIn("capability_preflight", composer)
        self.assertIn("capability_preflight", renderer)
        self.assertIn("qualifying deterministic data renderer", routing)
        self.assertIn("image generation", routing)
        self.assertIn("diagnostic fallback", standard)
        self.assertIn("report PASS for a text-only fallback", quality_cases)

    def test_render_success_requires_payload_and_ui_confirmation(self) -> None:
        composer = (ROOT / "skills/meta/report-composer/SKILL.md").read_text(encoding="utf-8")
        renderer = (ROOT / "skills/meta/visual-output-design/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("PAYLOAD_RENDERED", composer)
        self.assertIn("UI_CONFIRMED", composer)
        self.assertIn("UI_RENDER_UNCONFIRMED", composer)
        self.assertIn("successful renderer call is not enough for PASS", composer)
        self.assertIn("PAYLOAD_RENDERED", renderer)
        self.assertIn("UI_RENDER_UNCONFIRMED", renderer)
        self.assertIn("Tool success alone is not called UI-rendered", renderer)
        self.assertIn("PASS_WITH_LIMITATIONS", composer)
        self.assertIn("PASS is permitted only when that slot reaches `UI_CONFIRMED`", composer)

        quality_cases = (ROOT / "skills/meta/report-composer/tests/quality-cases.yaml").read_text(encoding="utf-8")
        self.assertIn("quality-payload-without-ui-confirmation", quality_cases)
        self.assertIn("report_status UI_RENDER_UNCONFIRMED", quality_cases)
        self.assertIn("report PASS_WITH_LIMITATIONS", quality_cases)


if __name__ == "__main__":
    unittest.main()
