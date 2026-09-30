from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

import yaml

FORBIDDEN_PARTS = {"tests", "__pycache__", "evals"}
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def validate_skill_text(text: str, label: str) -> list[str]:
    errors: list[str] = []
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return [f"{label}: missing portable frontmatter"]
    end = text.find("\n---\n", 4)
    try:
        fm = yaml.safe_load(text[4:end]) or {}
    except Exception as exc:
        return [f"{label}: invalid YAML frontmatter: {exc}"]
    name = fm.get("name")
    description = fm.get("description")
    if not isinstance(name, str) or not (1 <= len(name) <= 64):
        errors.append(f"{label}: portable name must be 1..64 characters")
    if not isinstance(description, str) or not (1 <= len(description) <= 1024):
        errors.append(f"{label}: portable description must be 1..1024 characters")
    compatibility = fm.get("compatibility")
    if compatibility is not None and (not isinstance(compatibility, str) or len(compatibility) > 500):
        errors.append(f"{label}: portable compatibility must be <=500 characters")
    metadata = fm.get("metadata") or {}
    if not isinstance(metadata, dict) or not all(
        isinstance(k, str) and isinstance(v, str) for k, v in metadata.items()
    ):
        errors.append(f"{label}: portable metadata must be string -> string")
    return errors


def validate_manifests(path: Path) -> list[str]:
    errors: list[str] = []
    release = path / "release-manifest.json"
    capabilities = path / "capabilities.json"
    if not release.is_file():
        errors.append(f"missing release-manifest.json in {path}")
    if not capabilities.is_file():
        errors.append(f"missing capabilities.json in {path}")
    if release.is_file() and capabilities.is_file():
        r = json.loads(release.read_text(encoding="utf-8"))
        c = json.loads(capabilities.read_text(encoding="utf-8"))
        if r.get("source_revision") != c.get("source_revision"):
            errors.append("release/capabilities source_revision mismatch")
        if not r.get("release_id"):
            errors.append("release manifest missing immutable release_id")
    return errors


def validate_tree(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing artifact: {path}"]
    errors.extend(validate_manifests(path))
    for file in path.rglob("*"):
        if not file.is_file():
            continue
        rel = file.relative_to(path)
        if any(part in FORBIDDEN_PARTS for part in rel.parts):
            errors.append(f"forbidden runtime content: {rel}")
        if file.name.endswith(".rubric.yaml"):
            errors.append(f"rubric leaked into runtime artifact: {rel}")
        if file.name == "SKILL.md":
            errors.extend(validate_skill_text(file.read_text(encoding="utf-8"), str(rel)))
    return errors


def validate_zips(path: Path) -> list[str]:
    errors: list[str] = []
    index = path / "index.json"
    if not index.is_file():
        return [f"missing index.json in {path}"]
    errors.extend(validate_manifests(path))
    data = json.loads(index.read_text(encoding="utf-8"))
    if data.get("source_revision") is None:
        errors.append("index.json missing source_revision")
    for item in data.get("skills", []):
        zip_name = item.get("zip")
        if not zip_name:
            errors.append(f"{item.get('name')}: missing zip name")
            continue
        zp = path / zip_name
        if not zp.is_file():
            errors.append(f"missing ZIP {zip_name}")
            continue
        with zipfile.ZipFile(zp) as zf:
            infos = zf.infolist()
            names = [x.filename for x in infos]
            if names != sorted(names):
                errors.append(f"{zip_name}: ZIP entries are not sorted")
            top = {Path(name).parts[0] for name in names if Path(name).parts}
            if top != {item.get("name")}:
                errors.append(f"{zip_name}: ZIP must have exactly one matching top-level folder")
            for info in infos:
                name = info.filename
                parts = Path(name).parts
                if any(p in FORBIDDEN_PARTS for p in parts):
                    errors.append(f"{zip_name}: forbidden path {name}")
                if name.endswith(".rubric.yaml"):
                    errors.append(f"{zip_name}: rubric leaked: {name}")
                if info.date_time != ZIP_TIMESTAMP:
                    errors.append(f"{zip_name}: non-deterministic timestamp on {name}")
                if name.endswith("/SKILL.md"):
                    text = zf.read(name).decode("utf-8")
                    errors.extend(validate_skill_text(text, f"{zip_name}:{name}"))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--zips", action="store_true")
    args = parser.parse_args()
    errors = validate_zips(args.path) if args.zips else validate_tree(args.path)
    for error in errors:
        print(f"[BLOCKER] {error}")
    if not errors:
        print(f"Artifact validation: OK ({args.path})")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
