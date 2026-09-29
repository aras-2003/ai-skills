from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

import yaml


ALLOWED_SUPPORT_DIRS = ("references", "scripts", "assets")


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
    selected: list[Path] = []
    for skill_md in sorted((root / "skills").rglob("SKILL.md")):
        fm = read_frontmatter(skill_md)
        metadata = fm.get("metadata") or {}
        if metadata.get("maturity") == maturity:
            selected.append(skill_md.parent)
    return selected


def build_skill_bundle(skill_dir: Path, output_dir: Path) -> dict:
    fm = read_frontmatter(skill_dir / "SKILL.md")
    name = fm.get("name")
    metadata = fm.get("metadata") or {}
    if not isinstance(name, str) or not name:
        raise ValueError(f"{skill_dir}: missing skill name")

    staging = output_dir / "_staging" / name
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True, exist_ok=True)

    shutil.copy2(skill_dir / "SKILL.md", staging / "SKILL.md")
    for dirname in ALLOWED_SUPPORT_DIRS:
        src = skill_dir / dirname
        if src.exists():
            shutil.copytree(src, staging / dirname)

    zip_path = output_dir / f"{name}.zip"
    if zip_path.exists():
        zip_path.unlink()

    # ChatGPT/API skill bundles use exactly one top-level folder.
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(staging.rglob("*")):
            if path.is_file():
                arcname = Path(name) / path.relative_to(staging)
                zf.write(path, arcname.as_posix())

    digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    return {
        "name": name,
        "version": str(metadata.get("version", "unknown")),
        "maturity": str(metadata.get("maturity", "unknown")),
        "description": str(fm.get("description", "")).strip(),
        "zip": zip_path.name,
        "sha256": digest,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maturity", default="production")
    parser.add_argument("--output", default="dist/chatgpt-skills")
    parser.add_argument("--allow-empty", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    output_dir = root / args.output

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    selected = discover_skills(root, args.maturity)
    if not selected and not args.allow_empty:
        raise SystemExit(f"No skills with maturity={args.maturity!r}; refusing to build empty package set")

    index = {
        "format": "chatgpt-personal-skills",
        "maturity": args.maturity,
        "skills": [build_skill_bundle(skill_dir, output_dir) for skill_dir in selected],
    }

    staging = output_dir / "_staging"
    if staging.exists():
        shutil.rmtree(staging)

    (output_dir / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Packaged {len(index['skills'])} skills into {output_dir}")
    for item in index["skills"]:
        print(f" - {item['name']} {item['version']} -> {item['zip']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
