from __future__ import annotations

import os
import shutil
import tempfile
import unittest
from pathlib import Path
import sys

HERE = Path(__file__).resolve()
PACKAGE_DIR = HERE.parents[1]
ROOT = HERE.parents[3]
sys.path.insert(0, str(PACKAGE_DIR))

import artifact_validation
import build_chatgpt_skills
import build_lab_plugin
import build_plugin
from build_utils import assert_source_revision, validate_output_path
from workflow_entrypoints import dependency_availability


class PackagingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.old_revision = os.environ.get("SOURCE_REVISION")
        os.environ["SOURCE_REVISION"] = "0123456789abcdef0123456789abcdef01234567"
        (ROOT / ".tmp").mkdir(exist_ok=True)

    def tearDown(self) -> None:
        if self.old_revision is None:
            os.environ.pop("SOURCE_REVISION", None)
        else:
            os.environ["SOURCE_REVISION"] = self.old_revision

    def test_optional_dependency_has_explicit_missing_behavior(self) -> None:
        item = {
            "name": "workflow-x",
            "dependencies": {
                "required": ["required-skill"],
                "optional": [
                    {
                        "name": "optional-skill",
                        "on_missing": "Continue in reduced scope and disclose that optional-skill did not run.",
                    }
                ],
            },
        }
        missing_required, missing_optional = dependency_availability(item, {"required-skill"})
        self.assertEqual([], missing_required)
        self.assertEqual("optional-skill", missing_optional[0]["name"])
        self.assertIn("reduced scope", missing_optional[0]["on_missing"])

    def test_required_dependency_is_detected(self) -> None:
        item = {
            "name": "workflow-x",
            "dependencies": {"required": ["required-skill"], "optional": []},
        }
        missing_required, missing_optional = dependency_availability(item, set())
        self.assertEqual(["required-skill"], missing_required)
        self.assertEqual([], missing_optional)

    def test_stale_source_revision_is_rejected(self) -> None:
        assert_source_revision("abc", "abc")
        with self.assertRaises(RuntimeError):
            assert_source_revision("abc", "def")

    def test_prebuild_failure_preserves_previous_output(self) -> None:
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            out = Path(td) / "plugin"
            out.mkdir()
            sentinel = out / "sentinel.txt"
            sentinel.write_text("keep", encoding="utf-8")
            original = build_plugin.ensure_source_valid
            build_plugin.ensure_source_valid = lambda _root: (_ for _ in ()).throw(ValueError("broken reference"))
            try:
                with self.assertRaisesRegex(ValueError, "broken reference"):
                    build_plugin.build(ROOT, out, "production")
            finally:
                build_plugin.ensure_source_valid = original
            self.assertEqual("keep", sentinel.read_text(encoding="utf-8"))

    def test_invalid_maturity_preserves_previous_plugin_output(self) -> None:
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            out = Path(td) / "plugin"
            out.mkdir()
            sentinel = out / "sentinel.txt"
            sentinel.write_text("keep", encoding="utf-8")
            with self.assertRaises(ValueError):
                build_plugin.build(ROOT, out, "does-not-exist")
            self.assertEqual("keep", sentinel.read_text(encoding="utf-8"))

    def test_invalid_maturity_preserves_previous_zip_output(self) -> None:
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            out = Path(td) / "zips"
            out.mkdir()
            sentinel = out / "sentinel.txt"
            sentinel.write_text("keep", encoding="utf-8")
            with self.assertRaises(ValueError):
                build_chatgpt_skills.build(ROOT, out, "does-not-exist")
            self.assertEqual("keep", sentinel.read_text(encoding="utf-8"))

    def test_unsafe_output_paths_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td).resolve()
            (root / ".git").mkdir()
            (root / "skills" / "career").mkdir(parents=True)
            for out in (root, root / ".git", root / "skills", root / "skills" / "career", Path("/")):
                with self.assertRaises(ValueError):
                    validate_output_path(root, out)

    def test_deterministic_zip_bytes(self) -> None:
        a = build_chatgpt_skills._zip_bytes([
            ("x/SKILL.md", b"hello"),
            ("x/references/a.md", b"world"),
        ])
        b = build_chatgpt_skills._zip_bytes([
            ("x/references/a.md", b"world"),
            ("x/SKILL.md", b"hello"),
        ])
        self.assertEqual(a, b)
        changed = build_chatgpt_skills._zip_bytes([
            ("x/SKILL.md", b"HELLO"),
            ("x/references/a.md", b"world"),
        ])
        self.assertNotEqual(a, changed)

    def test_plugin_runtime_allowlist_excludes_tests_and_eval_reports(self) -> None:
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            out = Path(td) / "plugin"
            build_plugin.build(ROOT, out, "production")
            paths = [p.relative_to(out).as_posix() for p in out.rglob("*") if p.is_file()]
            self.assertFalse(any("/tests/" in f"/{p}/" for p in paths))
            self.assertFalse(any("/evals/" in f"/{p}/" for p in paths))
            self.assertFalse(any(p.endswith(".rubric.yaml") for p in paths))
            self.assertTrue((out / "capabilities.json").is_file())
            self.assertTrue((out / "release-manifest.json").is_file())

    def test_lab_manifests_match_final_fixture_mutated_artifact(self) -> None:
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            out = Path(td) / "lab"
            old_argv = sys.argv
            try:
                sys.argv = ["build_lab_plugin.py", "--output", str(out.relative_to(ROOT))]
                self.assertEqual(0, build_lab_plugin.main())
            finally:
                sys.argv = old_argv

            errors = artifact_validation.validate_tree(out, allow_lab_evals=True)
            self.assertEqual([], errors)

            import json
            capabilities = json.loads((out / "capabilities.json").read_text(encoding="utf-8"))
            workflows = [x for x in capabilities["capabilities"] if x.get("kind") == "workflow"]
            self.assertTrue(workflows)
            self.assertTrue(all(x.get("version") for x in workflows))

            fixture_component = next(
                x for x in capabilities["capabilities"]
                if (out / "skills" / x["name"] / "references" / "evals").is_dir()
            )
            skill_md = out / "skills" / fixture_component["name"] / "SKILL.md"
            skill_md.write_text(skill_md.read_text(encoding="utf-8") + "\nmutation\n", encoding="utf-8")
            errors = artifact_validation.validate_tree(out, allow_lab_evals=True)
            self.assertTrue(any("content_sha256 mismatch" in e for e in errors))

    def test_chatgpt_channel_manifest_declares_workflow_limitations(self) -> None:
        with tempfile.TemporaryDirectory(dir=(ROOT / ".tmp")) as td:
            out1 = Path(td) / "zip1"
            out2 = Path(td) / "zip2"
            build_chatgpt_skills.build(ROOT, out1, "production")
            build_chatgpt_skills.build(ROOT, out2, "production")
            index1 = (out1 / "index.json").read_bytes()
            index2 = (out2 / "index.json").read_bytes()
            self.assertEqual(index1, index2)
            import json
            data = json.loads(index1)
            self.assertTrue(data["workflows"])
            self.assertTrue(all(x["status"] == "unavailable" for x in data["workflows"]))
            zips1 = sorted(p for p in out1.glob("*.zip"))
            for p1 in zips1:
                p2 = out2 / p1.name
                self.assertEqual(p1.read_bytes(), p2.read_bytes())


if __name__ == "__main__":
    unittest.main()
