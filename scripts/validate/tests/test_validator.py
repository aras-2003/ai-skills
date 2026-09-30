from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

HERE = Path(__file__).resolve()
VALIDATE_DIR = HERE.parents[1]
PACKAGE_DIR = HERE.parents[2] / "package"
sys.path.insert(0, str(VALIDATE_DIR))
sys.path.insert(0, str(PACKAGE_DIR))

from validate_skill import validate_skill
from validate_tests import validate_cases
from validate_runtime import validate_runtime, validate_portable
from portable import portable_frontmatter

SKILL_SCHEMA = json.loads((VALIDATE_DIR / "schemas" / "skill.schema.json").read_text(encoding="utf-8"))
TEST_SCHEMA = json.loads((VALIDATE_DIR / "schemas" / "test-case.schema.json").read_text(encoding="utf-8"))

def write_skill(root: Path, name: str = "demo-skill", maturity: str = "candidate") -> Path:
    d = root / "skills" / "demo" / name
    d.mkdir(parents=True)
    text = f"""---
name: {name}
description: Use for a realistic demo task when a repeatable review is requested.
metadata:
  owner: owner
  version: "1.0.0"
  maturity: {maturity}
  risk: medium
  last_reviewed: "2026-09-30"
---
# Demo
## Purpose
Demo.
## Procedure
Do the task.
## Output contract
Return a result.
"""
    (d / "SKILL.md").write_text(text, encoding="utf-8")
    return d

class ValidatorMutationTests(unittest.TestCase):
    def test_missing_local_reference_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            d = write_skill(root)
            p = d / "SKILL.md"
            p.write_text(p.read_text(encoding="utf-8") + "\nUse `references/nonexistent.md`.\n", encoding="utf-8")
            issues = validate_skill(d, SKILL_SCHEMA, root=root)
            self.assertTrue(any("referenced local resource does not exist" in i.message for i in issues))

    def test_production_without_suite_is_blocked_without_waiver(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            d = write_skill(root, maturity="production")
            issues = validate_skill(d, SKILL_SCHEMA, root=root)
            self.assertTrue(any("production skill must include tests/cases.yaml" in i.message for i in issues))

    def test_missing_release_metadata_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            d = root / "skills" / "demo" / "demo-skill"
            d.mkdir(parents=True)
            (d / "SKILL.md").write_text("""---
name: demo-skill
description: Use for a valid task when testing missing metadata.
metadata:
  maturity: candidate
---
# Demo
## Purpose
x
## Procedure
x
## Output contract
x
""", encoding="utf-8")
            issues = validate_skill(d, SKILL_SCHEMA, root=root)
            self.assertTrue(any("release metadata missing required field" in i.message for i in issues))

    def test_too_long_description_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            d = write_skill(root)
            p = d / "SKILL.md"
            text = p.read_text(encoding="utf-8")
            start = text.index("description:")
            end = text.index("\nmetadata:")
            text = text[:start] + 'description: "' + ("x" * 1025) + '"\n' + text[end + 1:]
            p.write_text(text, encoding="utf-8")
            issues = validate_skill(d, SKILL_SCHEMA, root=root)
            self.assertTrue(any("Frontmatter schema violation" in i.message for i in issues))

    def test_empty_behavior_assertions_are_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "cases.yaml"
            p.write_text("""cases:
  - id: demo-1
    case: demo
    input: hello
    expected:
      should_trigger: true
      must: []
      must_not: []
  - id: demo-2
    case: near miss
    input: no
    expected:
      should_trigger: false
      must: []
      must_not:
        - do not trigger
""", encoding="utf-8")
            issues = validate_cases(p, TEST_SCHEMA)
            self.assertTrue(any("behavioral case must include non-empty" in i.message for i in issues))

    def test_use_for_description_is_not_false_trigger_warning(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            d = write_skill(root)
            issues = validate_skill(d, SKILL_SCHEMA, root=root)
            self.assertFalse(any("routing context" in i.message for i in issues))

    def test_portable_metadata_is_string_only(self) -> None:
        fm = {
            "name": "demo-skill",
            "description": "Use for demo.",
            "metadata": {
                "owner": "owner",
                "version": "1.0.0",
                "maturity": "production",
                "risk": "medium",
                "last_reviewed": "2026-09-30",
                "execution": {"model": "x"},
            },
        }
        portable = portable_frontmatter(fm)
        self.assertNotIn("execution", portable["metadata"])
        self.assertTrue(all(isinstance(v, str) for v in portable["metadata"].values()))
        self.assertEqual([], validate_portable(fm, "demo"))

    def test_unknown_dependency_and_stale_fixture_are_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            skill = write_skill(root, maturity="production")
            tests = skill / "tests"
            tests.mkdir()
            (tests / "cases.yaml").write_text("""cases:
  - id: a
    case: ok
    input: x
    expected: {should_trigger: true, must: [do x]}
  - id: b
    case: no
    input: y
    expected: {should_trigger: false, must_not: [do x]}
""", encoding="utf-8")
            (root / "workflows" / "wf").mkdir(parents=True)
            (root / "workflows" / "wf" / "WORKFLOW.md").write_text("# wf", encoding="utf-8")
            (root / "workflows" / "runtime-registry.yaml").write_text("""workflows:
  - name: wf
    workflow: workflows/wf/WORKFLOW.md
    channels: {plugin: supported}
    dependencies:
      required: [missing-skill]
      optional: []
    description: Use when running the demo workflow.
    metadata:
      owner: owner
      version: "1.0.0"
      maturity: production
      risk: medium
      last_reviewed: "2026-09-30"
""", encoding="utf-8")
            (root / "evals").mkdir()
            (root / "evals" / "x.input.md").write_text("# input", encoding="utf-8")
            (root / "evals" / "x.rubric.yaml").write_text("""id: wrong
target: demo-skill
assertions:
  manual: [check]
""", encoding="utf-8")
            (root / "evals" / "runtime-fixtures.yaml").write_text("""targets:
  demo-skill:
    - id: x
      mode: explicit
      input: evals/x.input.md
      rubric: evals/x.rubric.yaml
""", encoding="utf-8")
            issues = validate_runtime(root)
            self.assertTrue(any("unknown required dependency" in i.message for i in issues))
            self.assertTrue(any("stale fixture id" in i.message for i in issues))

    def test_duplicate_runtime_entrypoint_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_skill(root, name="wf")
            (root / "workflows" / "wf").mkdir(parents=True)
            (root / "workflows" / "wf" / "WORKFLOW.md").write_text("# wf", encoding="utf-8")
            (root / "workflows" / "runtime-registry.yaml").write_text("""workflows:
  - name: wf
    workflow: workflows/wf/WORKFLOW.md
    channels: {plugin: supported}
    dependencies: {required: [], optional: []}
    description: Use when running wf.
    metadata:
      owner: owner
      version: "1.0.0"
      maturity: candidate
      risk: low
      last_reviewed: "2026-09-30"
""", encoding="utf-8")
            (root / "evals").mkdir()
            (root / "evals" / "runtime-fixtures.yaml").write_text("targets: {}\n", encoding="utf-8")
            issues = validate_runtime(root)
            self.assertTrue(any("collides with skill" in i.message for i in issues))

if __name__ == "__main__":
    unittest.main()
