from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from build_plugin import copy_skill, discover_skills


PLUGIN_NAME = "arek-ai-skills-lab"
PLUGIN_VERSION = "0.1.0"


def add_oaf_health_check(root: Path, skills_out: Path) -> None:
    workflow = root / "workflows" / "oaf-health-check" / "WORKFLOW.md"
    if not workflow.exists():
        raise SystemExit(f"Missing workflow source: {workflow}")

    dst = skills_out / "oaf-health-check"
    dst.mkdir(parents=True, exist_ok=True)
    refs = dst / "references"
    refs.mkdir(parents=True, exist_ok=True)
    shutil.copy2(workflow, refs / "WORKFLOW.md")

    skill_md = """---
name: oaf-health-check
description: >
  Run the OAF Health Check workflow as a selective cross-domain organisational architecture diagnostic.
  Use when the user asks for a broad diagnosis spanning strategy execution, operating model, decision rights,
  governance, enterprise architecture, portfolio/execution or evidence loops. Do not use for a narrow issue
  that should route directly to one specialist OAF skill.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# OAF Health Check Runtime Entrypoint

## Purpose

Expose the repository workflow to the skill runtime without duplicating the workflow logic.

## Procedure

1. Load `references/WORKFLOW.md`.
2. Follow it as the authoritative orchestration procedure.
3. Route only to OAF specialist skills that are actually needed.
4. Diagnose before using design skills such as `governance-design` or `transformation-blueprint`.
5. Stop when adding another OAF domain would not improve the decision.

## Output contract

Use the workflow's output contract exactly:
- Executive diagnosis
- OAF heatmap
- Cross-domain causes
- Critical unknowns
- Recommended next action

## Quality checks

- [ ] Specialist skills were selected selectively.
- [ ] Diagnosis preceded design.
- [ ] Evidence and uncertainty are explicit.
- [ ] No domain was added merely for completeness.
"""
    (dst / "SKILL.md").write_text(skill_md, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="plugins/arek-ai-skills-lab")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    out = root / args.output
    skills_out = out / "skills"

    if out.exists():
        shutil.rmtree(out)
    skills_out.mkdir(parents=True, exist_ok=True)

    selected = discover_skills(root, "candidate")
    if not selected:
        raise SystemExit("No candidate skills found; refusing to build empty lab plugin")

    for skill_dir in selected:
        copy_skill(skill_dir, skills_out)

    add_oaf_health_check(root, skills_out)

    manifest = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": PLUGIN_NAME,
        "version": PLUGIN_VERSION,
        "description": "Candidate skills and workflow entrypoints for controlled behavioral testing.",
        "skills": "./skills/",
        "author": {"name": "Arkadiusz Kamrowski"},
        "repository": "https://github.com/aras-2003/ai-skills",
        "keywords": ["skills", "lab", "candidate", "oaf", "career"],
        "extensions": {
            "com.openai": {
                "interface": {
                    "displayName": "Arek AI Skills Lab",
                    "shortDescription": "Candidate skills for runtime evaluation before production.",
                    "longDescription": "A non-production lab package built from candidate skills on main for controlled Work/Codex behavioral and workflow testing."
                }
            }
        }
    }
    (out / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    compat_dir = out / ".codex-plugin"
    compat_dir.mkdir(parents=True, exist_ok=True)
    (compat_dir / "plugin.json").write_text(
        json.dumps(
            {
                "name": PLUGIN_NAME,
                "version": PLUGIN_VERSION,
                "description": manifest["description"],
                "skills": "./skills/"
            },
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )

    print(f"Packaged {len(selected)} candidate skills + oaf-health-check into {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
