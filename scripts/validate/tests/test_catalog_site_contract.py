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

    def test_default_page_is_area_first_and_discloses_versions(self) -> None:
        page = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        self.assertIn('data-view="areas" aria-pressed="true"', page)
        self.assertIn('id="areas-view"', page)
        self.assertIn('id="source-versions"', page)
        self.assertIn('id="source-revision"', page)
        self.assertIn('data-view="catalog"', page)
        self.assertIn("./processes.json", page)
        self.assertIn('id="area-cards"', page)

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
