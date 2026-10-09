"""No-network contract tests for the Project metadata mapper."""
import importlib.util
import pathlib
import unittest

PATH = pathlib.Path(__file__).resolve().parents[2] / "scripts/governance/sync_project_metadata.py"
spec = importlib.util.spec_from_file_location("sync_project_metadata", PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class MappingTest(unittest.TestCase):
    def test_legacy_metadata(self):
        result = mod.values("[ENG-18] skill improvement", "- historical priority: **P1**; epic: Foo; historical status: PROPOSED; size: L", [])
        self.assertEqual(result, {"Priority": "P1", "Size": "L", "Area": "Engineering"})

    def test_explicit_labels(self):
        result = mod.values("Some new issue", "", ["priority:P0", "area:Commerce", "size:XS"])
        self.assertEqual(result, {"Priority": "P0", "Area": "Commerce", "Size": "XS"})

    def test_unknown_stays_blank(self):
        self.assertEqual(mod.values("No metadata", "Please handle soon", []), {})

    def test_conflicts_fail_closed(self):
        with self.assertRaises(ValueError):
            mod.values("Conflict", "", ["priority:P0", "priority:P2"])

    def test_e2e_prefix(self):
        self.assertEqual(mod.values("[E2E-05] rendering", "", [])["Area"], "E2E & Quality")


if __name__ == "__main__":
    unittest.main()
