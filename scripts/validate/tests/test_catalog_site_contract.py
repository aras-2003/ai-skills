from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from scripts.catalog.generate_site_catalog import build_catalog  # noqa: E402


class SiteCatalogContractTests(unittest.TestCase):
    def test_generated_catalog_carries_package_versions_and_source_identity(self) -> None:
        markdown = (ROOT / "CATALOG.md").read_text(encoding="utf-8")
        package_manifest = (ROOT / "release/package.yaml").read_text(encoding="utf-8")
        catalog = build_catalog(markdown, package_manifest, "abcdef1234567890")

        self.assertEqual("abcdef123456", catalog["metadata"]["source_revision"])
        self.assertEqual("arek-ai-skills", catalog["metadata"]["packages"]["production"]["name"])
        self.assertEqual("arek-ai-skills-lab", catalog["metadata"]["packages"]["lab"]["name"])
        self.assertTrue(catalog["metadata"]["packages"]["production"]["version"])
        self.assertTrue(catalog["metadata"]["packages"]["lab"]["version"])
        self.assertTrue(catalog["skills"])

    def test_catalog_rejects_missing_package_or_revision_provenance(self) -> None:
        markdown = """| Skill | Domain | Maturity | Version | Description | Source |
|---|---|---|---|---|---|
| sample | meta | draft | 0.1.0 | Example | skills/meta/sample/SKILL.md |
"""
        valid_manifest = """package:
  name: arek-ai-skills
  version: "1.0.0"
lab:
  name: arek-ai-skills-lab
  version: "0.1.0"
"""

        with self.assertRaisesRegex(ValueError, "Source revision"):
            build_catalog(markdown, valid_manifest, " ")
        with self.assertRaisesRegex(ValueError, "Missing lab"):
            build_catalog(markdown, """package:
  name: arek-ai-skills
  version: "1.0.0"
""", "abc")

    def test_published_catalog_versions_match_package_source(self) -> None:
        markdown = (ROOT / "CATALOG.md").read_text(encoding="utf-8")
        package_manifest = (ROOT / "release/package.yaml").read_text(encoding="utf-8")
        source_catalog = build_catalog(markdown, package_manifest, "revision")
        published = json.loads((ROOT / "docs/catalog.json").read_text(encoding="utf-8"))

        self.assertEqual(source_catalog["metadata"]["packages"], published["metadata"]["packages"])
        self.assertEqual(source_catalog["skills"], published["skills"])
        self.assertTrue(published["metadata"]["source_revision"])
        by_name = {skill["name"]: skill for skill in published["skills"]}
        for name, version in (
            ("skill-evaluation", "0.3.1"),
            ("skill-release-review", "0.3.0"),
            ("skill-test-design", "0.3.0"),
        ):
            self.assertEqual(version, by_name[name]["version"])
            self.assertEqual("draft", by_name[name]["maturity"])

    def test_default_page_is_area_first_and_discloses_versions(self) -> None:
        page = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        for marker in (
            'data-view="areas" aria-pressed="true"',
            'id="areas-view"',
            'id="source-versions"',
            'id="source-revision"',
            'data-view="catalog"',
            "./processes.json",
            'id="area-cards"',
            "area-status-bar",
            "area-flows",
            "Pokaż ścieżki",
            "Production",
            "Candidate",
            "Draft",
        ):
            self.assertIn(marker, page)

    def test_site_lab_receipt_matches_the_exact_packaged_lab_identity(self) -> None:
        receipt = json.loads((ROOT / "docs/lab-release.json").read_text(encoding="utf-8"))
        manifest = json.loads((ROOT / "plugins/arek-ai-skills-lab/release-manifest.json").read_text(encoding="utf-8"))
        for field in ("channel", "version", "release_id", "source_revision", "payload_content_sha256"):
            self.assertEqual(manifest[field], receipt[field], field)
        self.assertEqual("lab", receipt["channel"])

    def test_lab_packager_refreshes_the_public_release_receipt(self) -> None:
        workflow = (ROOT / ".github/workflows/package-main-lab-plugin.yml").read_text(encoding="utf-8")
        self.assertIn("cp plugins/arek-ai-skills-lab/release-manifest.json docs/lab-release.json", workflow)
        self.assertIn("git add plugins/arek-ai-skills-lab docs/lab-release.json", workflow)

    def test_page_distinguishes_catalog_revision_from_lab_build_revision(self) -> None:
        page = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        self.assertIn('id="source-revision"', page)
        self.assertIn('id="lab-source-revision"', page)
        self.assertIn('id="lab-release-link"', page)
        self.assertIn('fetch("./lab-release.json")', page)

    def test_process_data_has_domain_scoped_flows(self) -> None:
        catalog = json.loads((ROOT / "docs/catalog.json").read_text(encoding="utf-8"))
        processes = json.loads((ROOT / "docs/processes.json").read_text(encoding="utf-8"))
        domains = {skill["domain"] for skill in catalog["skills"]}
        flow_domains = {flow["domain"] for flow in processes["processes"]}

        self.assertTrue(domains)
        self.assertTrue(flow_domains)
        self.assertTrue(flow_domains <= domains)
        for process in processes["processes"]:
            self.assertTrue(process["title"])
            self.assertTrue(process["lanes"])


if __name__ == "__main__":
    unittest.main()
