from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

import yaml

from build_plugin import copy_skill, discover_skills
from workflow_entrypoints import add_workflow_entrypoints


PLUGIN_NAME = "arek-ai-skills-lab"
PLUGIN_VERSION = "0.2.1"

def add_runtime_eval_fixtures(root: Path, skills_out: Path) -> int:
    registry = root / "evals" / "runtime-fixtures.yaml"
    if not registry.exists():
        return 0

    data = yaml.safe_load(registry.read_text(encoding="utf-8")) or {}
    targets = data.get("targets") or {}
    if not isinstance(targets, dict):
        raise ValueError("evals/runtime-fixtures.yaml: targets must be a mapping")

    copied = 0
    for target, cases in targets.items():
        target_dir = skills_out / target
        if not target_dir.exists():
            continue

        refs = target_dir / "references" / "evals"
        refs.mkdir(parents=True, exist_ok=True)
        lines = [
            "# Runtime Eval Inputs",
            "",
            "Only executor inputs are packaged here. Rubrics remain repository-side and must never be loaded into the executor context.",
            "",
        ]
        packaged_names: list[str] = []
        for case in cases or []:
            if not isinstance(case, dict):
                raise ValueError(f"evals/runtime-fixtures.yaml: {target} entries must be mappings")
            case_id = str(case.get("id") or "").strip()
            input_rel = str(case.get("input") or "").strip()
            rubric_rel = str(case.get("rubric") or "").strip()
            mode = str(case.get("mode") or "").strip()
            if not case_id or not input_rel or not rubric_rel or mode not in {"explicit", "natural-routing"}:
                raise ValueError(f"evals/runtime-fixtures.yaml: invalid case for {target}: {case}")

            src = root / input_rel
            rubric = root / rubric_rel
            if not src.exists():
                raise FileNotFoundError(f"Missing runtime eval input: {src}")
            if not rubric.exists():
                raise FileNotFoundError(f"Missing runtime eval rubric: {rubric}")
            if not src.name.endswith(".input.md"):
                raise ValueError(f"Runtime eval input must use .input.md suffix: {src}")
            if not rubric.name.endswith(".rubric.yaml"):
                raise ValueError(f"Runtime eval rubric must use .rubric.yaml suffix: {rubric}")

            dst = refs / src.name
            shutil.copy2(src, dst)
            copied += 1
            packaged_names.append(src.name)
            lines.append(f"- `{src.name}` — case: `{case_id}`, mode: `{mode}`")

        (refs / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

        skill_md = target_dir / "SKILL.md"
        if skill_md.exists() and packaged_names:
            appendix = [
                "",
                "## Lab runtime eval inputs",
                "",
                "When the user explicitly asks to run one of the exact lab eval cases below, load only the corresponding input file from `references/evals/`. The evaluator rubric is intentionally unavailable to the executor.",
                "",
            ]
            appendix.extend(f"- `references/evals/{name}`" for name in packaged_names)
            appendix.append("")
            skill_md.write_text(
                skill_md.read_text(encoding="utf-8").rstrip() + "\n" + "\n".join(appendix),
                encoding="utf-8",
            )
    return copied


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

    candidate_skills = discover_skills(root, "candidate")
    production_skills = discover_skills(root, "production")
    if not candidate_skills:
        raise SystemExit("No candidate skills found; refusing to build empty lab plugin")

    selected = candidate_skills + production_skills
    for skill_dir in selected:
        copy_skill(skill_dir, skills_out)

    available_names = {p.name for p in skills_out.iterdir() if p.is_dir()}
    candidate_workflows = add_workflow_entrypoints(
        root, "candidate", skills_out, channel="lab", available_names=available_names
    )
    available_names.update(candidate_workflows)
    production_workflows = add_workflow_entrypoints(
        root, "production", skills_out, channel="lab", available_names=available_names
    )
    runtime_eval_fixtures = add_runtime_eval_fixtures(root, skills_out)

    manifest = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": PLUGIN_NAME,
        "version": PLUGIN_VERSION,
        "description": "Isolated lab package with candidate targets plus their production dependencies for controlled behavioral testing.",
        "skills": "./skills/",
        "author": {"name": "Arkadiusz Kamrowski"},
        "repository": "https://github.com/aras-2003/ai-skills",
        "keywords": ["skills", "lab", "candidate", "oaf", "career"],
        "extensions": {
            "com.openai": {
                "interface": {
                    "displayName": "Arek AI Skills Lab",
                    "shortDescription": "Candidate skills for runtime evaluation before production.",
                    "longDescription": "A self-contained non-production lab package built from main for isolated behavioral testing. Do not enable it in the same session as the production plugin because duplicate capability names may compete."
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

    print(f"Packaged {len(candidate_skills)} candidate + {len(production_skills)} production dependency skills + {len(candidate_workflows) + len(production_workflows)} workflow entrypoints + {runtime_eval_fixtures} runtime eval inputs into {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
