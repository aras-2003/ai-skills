from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

import yaml

HERE = Path(__file__).resolve()
VALIDATE_DIR = HERE.parents[1]
if str(VALIDATE_DIR) not in sys.path:
    sys.path.insert(0, str(VALIDATE_DIR))

from common import load_json
from validate_runtime import validate_portable, validate_runtime
from validate_skill import validate_skill
from validate_tests import validate_cases


def skill_text(
    name: str = "good-skill",
    description: str = "Use for a concrete repeatable task when the user needs this bounded procedure.",
    metadata: bool = True,
    body: str = "## Purpose\nP\n\n## Procedure\n1. Do.\n\n## Output contract\nReturn result.\n",
) -> str:
    meta = ""
    if metadata:
        meta = """metadata:
  owner: test-owner
  version: "1.0.0"
  maturity: production
  risk: low
  last_reviewed: "2026-09-30"
"""
    return f"""---
name: {name}
description: >-
  {description}
{meta}---
{body}
"""


class SkillMutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = load_json(VALIDATE_DIR / "schemas" / "skill.schema.json")
        cls.test_schema = load_json(VALIDATE_DIR / "schemas" / "test-case.schema.json")

    def _skill_dir(self, root: Path, text: str, name: str = "good-skill", with_tests: bool = True) -> Path:
        d = root / "skills" / "test" / name
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(text, encoding="utf-8")
        if with_tests:
            td = d / "tests"
            td.mkdir()
            (td / "cases.yaml").write_text(
                """cases:
  - id: good-001
    case: positive
    input: "Do the thing."
    expected:
      should_trigger: true
      must:
        - return the bounded result
  - id: good-002
    case: near-miss
    input: "Do something adjacent."
    expected:
      should_trigger: false
      must_not:
        - run this skill
""",
                encoding="utf-8",
            )
        return d

    def test_missing_reference_is_blocker(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            d = self._skill_dir(
                root,
                skill_text(body="## Purpose\nP\n\n## Procedure\nLoad `references/nonexistent.md`.\n\n## Output contract\nR.\n"),
            )
            issues = validate_skill(d, self.schema, root=root)
            self.assertTrue(any("does not exist" in i.message and i.severity == "blocker" for i in issues))

    def test_missing_production_suite_is_blocker(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            d = self._skill_dir(root, skill_text(), with_tests=False)
            issues = validate_skill(d, self.schema, root=root)
            self.assertTrue(any("must include tests/cases.yaml" in i.message for i in issues))

    def test_missing_release_metadata_is_blocker(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            d = self._skill_dir(root, skill_text(metadata=False))
            issues = validate_skill(d, self.schema, root=root)
            self.assertTrue(any("release metadata is required" in i.message for i in issues))

    def test_overlong_description_is_blocker(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            d = self._skill_dir(root, skill_text(description="x" * 1100))
            issues = validate_skill(d, self.schema, root=root)
            self.assertTrue(any("schema violation" in i.message.lower() for i in issues))

    def test_empty_assertions_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "cases.yaml"
            p.write_text(
                """cases:
  - id: empty-001
    case: empty
    input: "x"
    expected:
      should_trigger: true
""",
                encoding="utf-8",
            )
            issues = validate_cases(p, self.test_schema)
            self.assertTrue(any(i.severity in {"blocker", "high"} for i in issues))

    def test_use_for_description_is_not_high_severity(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            d = self._skill_dir(root, skill_text())
            issues = validate_skill(d, self.schema, root=root)
            self.assertFalse(any(i.severity in {"blocker", "high"} for i in issues), [str(i) for i in issues])


class RuntimeContractTests(unittest.TestCase):
    def _root(self) -> Path:
        root = Path(tempfile.mkdtemp())
        skill = root / "skills" / "test" / "alpha"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text(skill_text(name="alpha"), encoding="utf-8")
        tests = skill / "tests"
        tests.mkdir()
        (tests / "cases.yaml").write_text(
            """cases:
  - id: alpha-001
    case: positive
    input: "alpha"
    expected:
      should_trigger: true
      must:
        - do alpha
  - id: alpha-002
    case: negative
    input: "beta"
    expected:
      should_trigger: false
      must_not:
        - do alpha
""",
            encoding="utf-8",
        )
        wf_dir = root / "workflows" / "wf"
        wf_dir.mkdir(parents=True)
        (wf_dir / "WORKFLOW.md").write_text("# Workflow\n", encoding="utf-8")
        (root / "workflows" / "runtime-registry.yaml").write_text(
            """workflows:
  - name: wf
    workflow: workflows/wf/WORKFLOW.md
    description: "Use when a workflow is needed for alpha."
    channels:
      plugin: supported
      lab: supported
      chatgpt-zip: unavailable
    dependencies:
      required:
        - alpha
      optional: []
    metadata:
      owner: test-owner
      version: "1.0.0"
      maturity: production
      risk: low
      last_reviewed: "2026-09-30"
""",
            encoding="utf-8",
        )
        ev = root / "evals"
        ev.mkdir()
        (ev / "case.input.md").write_text("# Scenario\nalpha\n", encoding="utf-8")
        (ev / "case.rubric.yaml").write_text(
            """schema_version: "1.0"
id: case-001
target: wf
mode: explicit
assertions:
  manual:
    - do alpha
""",
            encoding="utf-8",
        )
        (ev / "runtime-fixtures.yaml").write_text(
            """schema_version: "2.0"
targets:
  wf:
    - id: case-001
      mode: explicit
      input: evals/case.input.md
      rubric: evals/case.rubric.yaml
""",
            encoding="utf-8",
        )
        return root

    def test_valid_runtime_contract_passes(self) -> None:
        root = self._root()
        issues = validate_runtime(root)
        self.assertFalse(any(i.severity in {"blocker", "high"} for i in issues), [str(i) for i in issues])

    def test_unknown_dependency_is_rejected(self) -> None:
        root = self._root()
        path = root / "workflows" / "runtime-registry.yaml"
        text = path.read_text(encoding="utf-8").replace("- alpha", "- missing-skill")
        path.write_text(text, encoding="utf-8")
        issues = validate_runtime(root)
        self.assertTrue(any("unknown required dependency" in i.message for i in issues))

    def test_invalid_registry_channel_is_rejected(self) -> None:
        root = self._root()
        path = root / "workflows" / "runtime-registry.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace("plugin: supported", "plugin: maybe"), encoding="utf-8")
        issues = validate_runtime(root)
        self.assertTrue(any("invalid channel state" in i.message for i in issues))

    def test_stale_fixture_target_is_rejected(self) -> None:
        root = self._root()
        rubric = root / "evals" / "case.rubric.yaml"
        rubric.write_text(rubric.read_text(encoding="utf-8").replace("target: wf", "target: alpha"), encoding="utf-8")
        issues = validate_runtime(root)
        self.assertTrue(any("stale fixture target" in i.message for i in issues))

    def test_duplicate_entrypoint_is_rejected(self) -> None:
        root = self._root()
        path = root / "workflows" / "runtime-registry.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace("name: wf", "name: alpha"), encoding="utf-8")
        issues = validate_runtime(root)
        self.assertTrue(any("collides with skill" in i.message for i in issues))

    def test_invalid_portable_metadata_is_rejected(self) -> None:
        issues = validate_portable(
            {
                "name": "a" * 65,
                "description": "Use for valid routing when needed.",
                "metadata": {"owner": "x"},
            },
            "synthetic",
        )
        self.assertTrue(any(i.severity == "blocker" for i in issues))


if __name__ == "__main__":
    unittest.main()
