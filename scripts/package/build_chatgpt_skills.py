from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path

from build_utils import (
    atomic_output,
    copy_runtime_support,
    package_version,
    sha256_file,
    source_revision,
    write_json,
)
from portable import read_frontmatter, render_portable_skill
from workflow_entrypoints import load_registry

ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
ZIP_MODE = 0o100644 << 16


def discover_skills(root: Path, maturity: str) -> list[Path]:
    selected: list[Path] = []
    for skill_md in sorted((root / "skills").rglob("SKILL.md")):
        fm, _ = read_frontmatter(skill_md)
        metadata = fm.get("metadata") or {}
        if metadata.get("maturity") == maturity:
            selected.append(skill_md.parent)
    return selected


def _write_deterministic_zip(source_dir: Path, zip_path: Path, top_level: str) -> None:
    files = sorted(p for p in source_dir.rglob("*") if p.is_file())
    with zipfile.ZipFile(
        zip_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as zf:
        for path in files:
            rel = path.relative_to(source_dir).as_posix()
            info = zipfile.ZipInfo(f"{top_level}/{rel}", date_time=ZIP_TIMESTAMP)
            info.create_system = 3
            info.external_attr = ZIP_MODE
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def build_skill_bundle(skill_dir: Path, output_dir: Path) -> dict:
    fm, _ = read_frontmatter(skill_dir / "SKILL.md")
    name = fm.get("name")
    metadata = fm.get("metadata") or {}
    if not isinstance(name, str) or not name:
        raise ValueError(f"{skill_dir}: missing skill name")

    staging = output_dir / "_staging" / name
    staging.mkdir(parents=True, exist_ok=False)
    (staging / "SKILL.md").write_text(
        render_portable_skill(skill_dir / "SKILL.md"),
        encoding="utf-8",
    )
    inventory = ["SKILL.md"] + copy_runtime_support(skill_dir, staging)

    zip_path = output_dir / f"{name}.zip"
    _write_deterministic_zip(staging, zip_path, name)
    return {
        "name": name,
        "kind": "skill",
        "version": str(metadata.get("version", "unknown")),
        "maturity": str(metadata.get("maturity", "unknown")),
        "description": str(fm.get("description", "")).strip(),
        "zip": zip_path.name,
        "sha256": sha256_file(zip_path),
        "inventory": sorted(inventory),
    }


def build(root: Path, output_dir: Path, maturity: str, allow_empty: bool = False) -> dict:
    selected = discover_skills(root, maturity)
    if not selected and not allow_empty:
        raise ValueError(f"No skills with maturity={maturity!r}; refusing to build empty package set")

    with atomic_output(root, output_dir) as stage:
        (stage / "_staging").mkdir()
        skills = [build_skill_bundle(skill_dir, stage) for skill_dir in selected]

        unavailable_workflows = []
        for workflow in load_registry(root):
            metadata = workflow.get("metadata") or {}
            if metadata.get("maturity") != maturity:
                continue
            channel_state = (workflow.get("channels") or {}).get("chatgpt-zip")
            if channel_state != "supported":
                unavailable_workflows.append(
                    {
                        "name": workflow.get("name"),
                        "status": "unavailable",
                        "reason": "This channel packages standalone skill ZIPs only. Use the plugin/Lab channel for workflow orchestration.",
                        "dependencies": workflow.get("dependencies") or {},
                    }
                )

        revision = source_revision(root)
        index = {
            "schema_version": "2.0",
            "format": "chatgpt-personal-skills",
            "channel": "chatgpt-zip",
            "package_version": package_version(root, "package"),
            "source_revision": revision,
            "maturity": maturity,
            "capabilities": skills + sorted(unavailable_workflows, key=lambda x: str(x["name"])),
        }
        staging_dir = stage / "_staging"
        for path in sorted(staging_dir.iterdir()):
            if path.is_dir():
                for child in sorted(path.rglob("*"), reverse=True):
                    if child.is_file():
                        child.unlink()
                    elif child.is_dir():
                        child.rmdir()
                path.rmdir()
        staging_dir.rmdir()
        write_json(stage / "index.json", index)
        write_json(
            stage / "release-manifest.json",
            {
                "schema_version": "1.0",
                "package": "arek-ai-skills",
                "version": package_version(root, "package"),
                "channel": "chatgpt-zip",
                "source_revision": revision,
                "artifacts": {
                    item["zip"]: item["sha256"]
                    for item in skills
                },
            },
        )

    return {"skills": skills, "source_revision": source_revision(root)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maturity", default="production")
    parser.add_argument("--output", default="dist/chatgpt-skills")
    parser.add_argument("--allow-empty", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    output_dir = root / args.output
    result = build(root, output_dir, args.maturity, allow_empty=args.allow_empty)

    print(f"Packaged {len(result['skills'])} deterministic skill ZIPs into {output_dir}")
    for item in result["skills"]:
        print(f" - {item['name']} {item['version']} -> {item['zip']} {item['sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
