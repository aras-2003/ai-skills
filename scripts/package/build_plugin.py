from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

import yaml


def read_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{skill_md}: missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{skill_md}: unterminated frontmatter")
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{skill_md}: frontmatter must be a mapping")
    return data


def discover_skills(root: Path, maturity: str) -> list[Path]:
    skills = []
    for skill_md in sorted((root / "skills").rglob("SKILL.md")):
        fm = read_frontmatter(skill_md)
        metadata = fm.get("metadata") or {}
        if metadata.get("maturity") == maturity:
            skills.append(skill_md.parent)
    return skills


def copy_skill(src: Path, dst_root: Path) -> None:
    name = read_frontmatter(src / "SKILL.md").get("name")
    if not isinstance(name, str) or not name:
        raise ValueError(f"{src}: missing skill name")
    dst = dst_root / name
    if dst.exists():
        raise ValueError(f"duplicate packaged skill name: {name}")
    shutil.copytree(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maturity", default="production")
    parser.add_argument("--output", default="plugins/arek-ai-skills")
    parser.add_argument("--allow-empty", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    out = root / args.output
    skills_out = out / "skills"

    if out.exists():
        shutil.rmtree(out)
    skills_out.mkdir(parents=True, exist_ok=True)

    selected = discover_skills(root, args.maturity)
    if not selected and not args.allow_empty:
        raise SystemExit(f"No skills with maturity={args.maturity!r}; refusing to build empty plugin")

    for skill_dir in selected:
        copy_skill(skill_dir, skills_out)

    manifest = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": "arek-ai-skills",
        "version": "1.0.1",
        "description": "Validated production AI skills for Arkadiusz Kamrowski workflows.",
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
    (out / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    # Compatibility overlay for ChatGPT/Codex clients that still rely on
    # the legacy plugin manifest. The root portable plugin.json remains
    # canonical, while this explicitly exposes the bundled skills directory.
    compat_dir = out / ".codex-plugin"
    compat_dir.mkdir(parents=True, exist_ok=True)
    compat_manifest = {
        "name": "arek-ai-skills",
        "version": "1.0.1",
        "description": "Validated production AI skills for Arkadiusz Kamrowski workflows.",
        "skills": "./skills/"
    }
    (compat_dir / "plugin.json").write_text(
        json.dumps(compat_manifest, indent=2) + "\n",
        encoding="utf-8"
    )

    print(f"Packaged {len(selected)} production skills into {out}")
    for item in selected:
        print(f" - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
