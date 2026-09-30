from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from build_plugin import copy_skill, discover_skills
from workflow_entrypoints import add_workflow_entrypoints


PLUGIN_NAME = "arek-ai-skills-lab"
PLUGIN_VERSION = "0.1.0"


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

    candidate_workflows = add_workflow_entrypoints(root, "candidate", skills_out)
    production_workflows = add_workflow_entrypoints(root, "production", skills_out)

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

    print(f"Packaged {len(selected)} candidate skills + {len(candidate_workflows) + len(production_workflows)} workflow entrypoints into {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
