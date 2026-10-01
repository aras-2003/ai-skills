from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_utils import (
    atomic_output,
    copy_runtime_support,
    ensure_source_valid,
    package_version,
    sha256_tree,
    source_revision,
    write_json,
)
from portable import read_frontmatter, render_portable_skill
from workflow_entrypoints import add_workflow_entrypoints, load_registry

PLUGIN_NAME = "arek-ai-skills"


def discover_skills(root: Path, maturity: str) -> list[Path]:
    skills = []
    for skill_md in sorted((root / "skills").rglob("SKILL.md")):
        fm, _ = read_frontmatter(skill_md)
        metadata = fm.get("metadata") or {}
        if metadata.get("maturity") == maturity:
            skills.append(skill_md.parent)
    return skills


def copy_skill(src: Path, dst_root: Path) -> dict:
    fm, _ = read_frontmatter(src / "SKILL.md")
    name = fm.get("name")
    metadata = fm.get("metadata") or {}
    if not isinstance(name, str) or not name:
        raise ValueError(f"{src}: missing skill name")
    dst = dst_root / name
    if dst.exists():
        raise ValueError(f"duplicate packaged skill name: {name}")
    dst.mkdir(parents=True)
    (dst / "SKILL.md").write_text(render_portable_skill(src / "SKILL.md"), encoding="utf-8")
    inventory = ["SKILL.md"] + copy_runtime_support(src, dst)
    return {
        "name": name,
        "kind": "skill",
        "version": str(metadata.get("version", "unknown")),
        "maturity": str(metadata.get("maturity", "unknown")),
        "inventory": sorted(inventory),
        "content_sha256": sha256_tree(dst),
    }


def build(root: Path, out: Path, maturity: str, allow_empty: bool = False) -> dict:
    ensure_source_valid(root)
    selected = discover_skills(root, maturity)
    if not selected and not allow_empty:
        raise ValueError(f"No skills with maturity={maturity!r}; refusing to build empty plugin")

    with atomic_output(root, out) as stage:
        skills_out = stage / "skills"
        skills_out.mkdir(parents=True)
        capabilities = [copy_skill(skill_dir, skills_out) for skill_dir in selected]
        available_names = {item["name"] for item in capabilities}
        workflow_names = add_workflow_entrypoints(
            root,
            maturity,
            skills_out,
            channel="plugin",
            available_names=available_names,
        )
        registry_by_name = {
            str(item.get("name")): item
            for item in load_registry(root)
            if isinstance(item, dict) and item.get("name")
        }
        capabilities.extend(
            {
                "name": name,
                "kind": "workflow",
                "maturity": maturity,
                "version": str((registry_by_name[name].get("metadata") or {}).get("version") or ""),
                "content_sha256": sha256_tree(skills_out / name),
            }
            for name in workflow_names
        )

        version = package_version(root, "package")
        manifest = {
            "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "name": PLUGIN_NAME,
            "version": version,
            "description": "Validated production AI skills for Arkadiusz Kamrowski workflows.",
            "skills": "./skills/",
            "author": {"name": "Arkadiusz Kamrowski"},
            "repository": "https://github.com/aras-2003/ai-skills",
            "keywords": ["skills", "productivity", "career", "strategy", "research"],
            "extensions": {
                "com.openai": {
                    "interface": {
                        "displayName": "Arek AI Skills",
                        "shortDescription": "Validated reusable workflows from the ai-skills production catalog.",
                        "longDescription": "A governed collection of production-ready reusable AI skills maintained in GitHub and packaged for ChatGPT/Codex."
                    }
                }
            }
        }
        write_json(stage / "plugin.json", manifest)
        compat_dir = stage / ".codex-plugin"
        compat_dir.mkdir(parents=True)
        write_json(
            compat_dir / "plugin.json",
            {
                "name": PLUGIN_NAME,
                "version": version,
                "description": manifest["description"],
                "skills": "./skills/",
            },
        )
        revision = source_revision(root)
        write_json(
            stage / "capabilities.json",
            {
                "schema_version": "1.0",
                "channel": "plugin",
                "source_revision": revision,
                "capabilities": sorted(capabilities, key=lambda x: x["name"]),
            },
        )
        payload_digest = sha256_tree(stage)
        write_json(
            stage / "release-manifest.json",
            {
                "schema_version": "1.0",
                "release_id": f"{version}+{revision[:12]}",
                "package": PLUGIN_NAME,
                "version": version,
                "channel": "plugin",
                "source_revision": revision,
                "payload_content_sha256": payload_digest,
                "components": [
                    {
                        "name": item["name"],
                        "kind": item["kind"],
                        "maturity": item.get("maturity"),
                        "version": item.get("version"),
                        "content_sha256": item.get("content_sha256"),
                    }
                    for item in sorted(capabilities, key=lambda x: x["name"])
                ],
            },
        )

    return {
        "skills": len(selected),
        "workflows": len(workflow_names),
        "version": package_version(root, "package"),
        "source_revision": source_revision(root),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maturity", default="production")
    parser.add_argument("--output", default="plugins/arek-ai-skills")
    parser.add_argument("--allow-empty", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    out = root / args.output
    result = build(root, out, args.maturity, allow_empty=args.allow_empty)
    print(
        f"Packaged {result['skills']} skills + {result['workflows']} workflow entrypoints "
        f"as {result['version']} from {result['source_revision']} into {out}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
