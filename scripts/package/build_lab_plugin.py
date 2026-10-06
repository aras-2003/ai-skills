from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

import yaml

from build_utils import atomic_output, capability_assessment, capability_contract_metadata, ensure_source_valid, package_runtime_mcp, package_version, sha256_tree, source_revision, write_json
from build_plugin import copy_skill, discover_skills
from workflow_entrypoints import add_workflow_entrypoints, load_registry


PLUGIN_NAME = "skills-factory-lab"
PLUGIN_VERSION = "0.2.1"

def discover_draft_test_skills(root: Path) -> list[Path]:
    package = yaml.safe_load((root / "release" / "package.yaml").read_text(encoding="utf-8")) or {}
    lab = package.get("lab") or {}
    targets = lab.get("draft_test_targets") or []
    if not isinstance(targets, list) or not targets or not all(isinstance(name, str) and name for name in targets):
        raise ValueError("release/package.yaml: lab.draft_test_targets must be a non-empty list of names")
    if len(targets) != len(set(targets)):
        raise ValueError("release/package.yaml: lab.draft_test_targets must be unique")

    drafts = {path.name: path for path in discover_skills(root, "draft")}
    missing = sorted(set(targets) - drafts.keys())
    if missing:
        raise ValueError("Lab draft test targets are missing or not draft: " + ", ".join(missing))
    return [drafts[name] for name in targets]


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
    parser.add_argument("--output", default="plugins/skills-factory-lab")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    ensure_source_valid(root)
    out = root / args.output

    candidate_skills = discover_skills(root, "candidate")
    production_skills = discover_skills(root, "production")
    draft_test_skills = discover_draft_test_skills(root)
    if not candidate_skills:
        raise SystemExit("No candidate skills found; refusing to build empty lab plugin")

    with atomic_output(root, out) as stage:
        skills_out = stage / "skills"
        skills_out.mkdir(parents=True)

        skill_capabilities: dict[str, dict] = {}
        for skill_dir in candidate_skills + production_skills + draft_test_skills:
            item = copy_skill(skill_dir, skills_out)
            skill_capabilities[item["name"]] = item

        available_names = {p.name for p in skills_out.iterdir() if p.is_dir()}
        candidate_workflows = add_workflow_entrypoints(
            root, "candidate", skills_out, channel="lab", available_names=available_names
        )
        available_names.update(candidate_workflows)
        production_workflows = add_workflow_entrypoints(
            root, "production", skills_out, channel="lab", available_names=available_names
        )
        workflow_names = candidate_workflows + production_workflows

        runtime_eval_fixtures = add_runtime_eval_fixtures(root, skills_out)

        registry_by_name = {
            str(item.get("name")): item
            for item in load_registry(root)
            if isinstance(item, dict) and item.get("name")
        }
        capabilities: list[dict] = []
        for name, item in skill_capabilities.items():
            final_dir = skills_out / name
            final_inventory = sorted(
                p.relative_to(final_dir).as_posix()
                for p in final_dir.rglob("*")
                if p.is_file()
            )
            refreshed = dict(item)
            refreshed["inventory"] = final_inventory
            refreshed["content_sha256"] = sha256_tree(final_dir)
            capabilities.append(refreshed)

        for name in workflow_names:
            registry_item = registry_by_name.get(name)
            if registry_item is None:
                raise ValueError(f"workflow registry item missing after packaging: {name}")
            metadata = registry_item.get("metadata") or {}
            final_dir = skills_out / name
            capabilities.append(
                {
                    "name": name,
                    "kind": "workflow",
                    "maturity": metadata.get("maturity"),
                    "version": metadata.get("version"),
                    "inventory": sorted(
                        p.relative_to(final_dir).as_posix()
                        for p in final_dir.rglob("*")
                        if p.is_file()
                    ),
                    "content_sha256": sha256_tree(final_dir),
                    "capability_assessment": capability_assessment(root, name),
                }
            )

        version = package_version(root, "lab")
        interface = {
            "displayName": "Skills Factory Lab",
            "shortDescription": "Candidate skills for runtime evaluation and discovery.",
            "longDescription": "A self-contained non-production lab package built from main for isolated behavioral testing, including only explicitly selected draft test targets. Do not enable it in the same session as the production plugin because duplicate capability names may compete.",
            "websiteURL": "https://aras-2003.github.io/skills-factory/",
            "brandColor": "#C6812C",
            "brandColorDark": "#F0C982",
            "logo": "./assets/brand-mark.svg",
            "composerIcon": "./assets/brand-mark.svg",
        }
        manifest = {
            "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "name": PLUGIN_NAME,
            "version": version,
            "description": "Isolated lab package with candidate targets, explicitly selected draft test targets, and their production dependencies for controlled behavioral testing.",
            "skills": "./skills/",
            "author": {"name": "Arkadiusz Kamrowski"},
            "repository": "https://github.com/aras-2003/skills-factory",
            "keywords": ["skills", "lab", "candidate", "oaf", "career"],
            "extensions": {
                "com.openai": {
                    "interface": interface
                }
            }
        }
        logo_source = root / "docs" / "assets" / "brand-mark.svg"
        if not logo_source.is_file():
            raise FileNotFoundError(f"Missing plugin brand asset: {logo_source}")
        assets_out = stage / "assets"
        assets_out.mkdir(parents=True, exist_ok=True)
        shutil.copy2(logo_source, assets_out / "brand-mark.svg")
        write_json(stage / "plugin.json", manifest)
        runtime_tools = package_runtime_mcp(root, stage)
        compat_dir = stage / ".codex-plugin"
        compat_dir.mkdir(parents=True)
        write_json(
            compat_dir / "plugin.json",
            {
                "name": PLUGIN_NAME,
                "version": version,
                "description": manifest["description"],
                "skills": "./skills/",
                "mcpServers": "./.mcp.json",
                "interface": interface,
            },
        )
        revision = source_revision(root)
        fixture_registry = yaml.safe_load((root / "evals" / "runtime-fixtures.yaml").read_text(encoding="utf-8")) or {}
        fixture_targets = set((fixture_registry.get("targets") or {}).keys())
        packaged_names = {item["name"] for item in capabilities}
        fixture_status = [
            {
                "target": target,
                "status": "packaged" if target in packaged_names else "error",
            }
            for target in sorted(fixture_targets)
        ]
        if any(item["status"] == "error" for item in fixture_status):
            missing = [item["target"] for item in fixture_status if item["status"] == "error"]
            raise ValueError("runtime fixture target not packaged in lab: " + ", ".join(missing))

        write_json(
            stage / "capabilities.json",
            {
                "schema_version": "1.0",
                "channel": "lab",
                "source_revision": revision,
                "capability_contract": capability_contract_metadata(),
                "session_rule": "Use this isolated Lab without the production plugin in the same runtime session.",
                "capabilities": sorted(capabilities, key=lambda x: x["name"]),
                "runtime_fixture_targets": fixture_status,
                "runtime_tools": runtime_tools,
            },
        )
        digest = sha256_tree(stage)
        write_json(
            stage / "release-manifest.json",
            {
                "schema_version": "1.0",
                "release_id": f"{version}+{revision[:12]}",
                "package": PLUGIN_NAME,
                "version": version,
                "channel": "lab",
                "source_revision": revision,
                "capability_contract": capability_contract_metadata(),
                "payload_content_sha256": digest,
                "components": [
                    {
                        "name": item["name"],
                        "kind": item["kind"],
                        "maturity": item.get("maturity"),
                        "version": item.get("version"),
                        "content_sha256": item.get("content_sha256"),
                        "capability_assessment": item.get("capability_assessment"),
                    }
                    for item in sorted(capabilities, key=lambda x: x["name"])
                ],
            },
        )

    print(
        f"Packaged {len(candidate_skills)} candidate + {len(production_skills)} production dependency skills + "
        f"{len(candidate_workflows) + len(production_workflows)} workflow entrypoints + "
        f"{runtime_eval_fixtures} runtime eval inputs into {out}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
