from __future__ import annotations

import importlib.util
import os
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "runtime" / "mcp" / "skill_catalog.py"


def load_catalog():
    spec = importlib.util.spec_from_file_location("skills_factory_skill_catalog", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load skill catalog")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SkillCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog()

    def test_catalog_lists_packaged_lab_skills(self) -> None:
        result = self.catalog.list_skills()
        names = {item["name"] for item in result["skills"]}
        self.assertIn("skill-test-design", names)
        self.assertIn("skill-evaluation", names)
        self.assertTrue(result["catalog_digest"])

    def test_load_skill_returns_exact_instructions_and_digest(self) -> None:
        result = self.catalog.load_skill("skill-test-design")
        self.assertIn("Skill Test Design", result["instructions"])
        self.assertEqual("host_model_executes_loaded_instructions", result["execution_mode"])
        self.assertTrue(result["content_sha256"])

    def test_skill_name_cannot_escape_catalog(self) -> None:
        with self.assertRaises(ValueError):
            self.catalog.load_skill("../README")

    def test_configured_catalog_root_is_supported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "skills"
            skill = root / "example"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "---\nname: example\ndescription: Example\nmetadata:\n  version: '1'\n  maturity: candidate\n---\n\n# Example\n",
                encoding="utf-8",
            )
            previous = os.environ.get("SKILLS_FACTORY_SKILLS_ROOT")
            os.environ["SKILLS_FACTORY_SKILLS_ROOT"] = str(root)
            try:
                result = self.catalog.list_skills()
                self.assertEqual(["example"], [item["name"] for item in result["skills"]])
            finally:
                if previous is None:
                    os.environ.pop("SKILLS_FACTORY_SKILLS_ROOT", None)
                else:
                    os.environ["SKILLS_FACTORY_SKILLS_ROOT"] = previous


if __name__ == "__main__":
    unittest.main()
