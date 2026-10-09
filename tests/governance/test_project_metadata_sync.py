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

    def test_real_migrated_issue_header(self):
        header = ("## Legacy backlog source\\n- ID: `PRO-05`; historical priority: "
                  "**P2**; epic: Professional work; historical status: PROPOSED; size: M")
        self.assertEqual(mod.values("[PRO-05] AI review", header, []),
                         {"Priority": "P2", "Size": "M", "Area": "Other"})

    def test_header_without_metadata_does_not_infer_priority(self):
        self.assertEqual(mod.values("[ENG-18] anything", "Priority should be decided", []),
                         {"Area": "Engineering"})

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

    def test_explicit_project_status_body(self):
        result = mod.values("[ENG-01] review", "Historical status: PROPOSED\\nProject status: In Progress", [])
        self.assertEqual(result["Status"], "In Progress")

    def test_explicit_project_status_label(self):
        result = mod.values("[ENG-03] review", "", ["status:blocked"])
        self.assertEqual(result["Status"], "Blocked")

    def test_historical_status_not_taken_as_live_status(self):
        self.assertNotIn("Status", mod.values("[ENG-03] review", "historical status: PROPOSED", []))

    def test_conflicting_project_status_refuses_write(self):
        with self.assertRaises(ValueError):
            mod.values("[ENG-03] review", "Project status: In Progress", ["status:blocked"])


if __name__ == "__main__":
    unittest.main()
