from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class WorkflowSupplyChainTests(unittest.TestCase):
    def test_actions_are_pinned_to_full_commit_sha(self) -> None:
        pattern = re.compile(r"^\s*uses:\s*([^\s]+)", re.MULTILINE)
        workflows = sorted((ROOT / ".github/workflows").glob("*.yml"))
        refs = [ref for workflow in workflows for ref in pattern.findall(workflow.read_text())]
        self.assertTrue(refs, "expected workflow actions")
        for ref in refs:
            if ref.startswith("./"):
                continue
            self.assertRegex(ref, r"^[^@]+@[0-9a-f]{40}$", f"mutable action reference: {ref}")

    def test_workflows_install_from_hash_locked_requirements(self) -> None:
        for workflow in sorted((ROOT / ".github/workflows").glob("*.yml")):
            source = workflow.read_text()
            if "pip install" in source:
                self.assertIn("--require-hashes -r requirements-dev.lock", source, workflow.name)

        lock_lines = (ROOT / "requirements-dev.lock").read_text().splitlines()
        entries = [line for line in lock_lines if re.match(r"^[A-Za-z0-9_.-]+==[^\\ ]+", line)]
        self.assertTrue(entries, "lock file contains no pinned packages")
        for entry in entries:
            following = "\n".join(lock_lines[lock_lines.index(entry) + 1 :])
            self.assertIn("--hash=sha256:", following.split("\n    # via", 1)[0], entry)

    def test_runtime_script_dependencies_are_exactly_pinned(self) -> None:
        scripts = [ROOT / "runtime/mcp/investment_runtime.py", ROOT / "runtime/mcp/chart_renderer.py"]
        for script in scripts:
            source = script.read_text()
            metadata = source.split("# dependencies = [", 1)[1].split("# ]", 1)[0]
            for dependency in re.findall(r'"([A-Za-z0-9_.-]+[^"\n]*)"', metadata):
                self.assertRegex(dependency, r"^[A-Za-z0-9_.-]+==[0-9][A-Za-z0-9.!+_-]*$", str(script))


if __name__ == "__main__":
    unittest.main()
