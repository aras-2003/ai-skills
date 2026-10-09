from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "audit_workflow_lifecycle.py"
spec = importlib.util.spec_from_file_location("audit_workflow_lifecycle", SCRIPT)
mod = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(mod)


class WorkflowProcessAuditTests(unittest.TestCase):
    def test_all_registered_workflows_and_runtime_remain_unverified(self):
        root = SCRIPT.parents[2]
        report = mod.audit(root)
        self.assertEqual(16, report["total"])
        self.assertEqual(16, len({x["name"] for x in report["workflows"]}))
        self.assertEqual("NOT_RUN", report["runtime"])
        self.assertEqual("REQUIRED", report["semantic_review"])
        self.assertFalse(report["statuses"].get("STATIC_BLOCKER", 0), report["workflows"])
        self.assertTrue(all(x["runtime_evidence"] == "NOT_RUN" and x["runtime_outcome"] is None
                            for x in report["workflows"]))

    def test_invalid_missing_path_or_metadata_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "workflows").mkdir()
            (root / "workflows" / "runtime-registry.yaml").write_text(
                'workflows:\n  - name: bad\n    workflow: workflows/missing/WORKFLOW.md\n'
                '    channels: {plugin: supported}\n'
                '    dependencies: {required: [], optional: []}\n'
                '    description: "Use this workflow for a real request."\n',
                encoding="utf-8",
            )
            r = mod.audit(root)
            self.assertEqual(1, r["statuses"]["STATIC_BLOCKER"])
            self.assertIn("registered WORKFLOW.md missing", r["workflows"][0]["errors"])

    def test_unregistered_workflow_is_not_silently_included(self):
        root = SCRIPT.parents[2]
        r = mod.audit(root)
        self.assertNotIn("skill-development", [x["name"] for x in r["workflows"]])
        self.assertTrue((root / "workflows/skill-development/WORKFLOW.md").is_file())


if __name__ == "__main__":
    unittest.main()
