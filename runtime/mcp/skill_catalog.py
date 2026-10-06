"""Load the packaged Skills Factory catalog shared by Lab and remote MCP."""

from __future__ import annotations

import hashlib
import os
import re
from pathlib import Path
from typing import Any

import yaml


_SAFE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")


def _plugin_root() -> Path:
    configured = os.environ.get("PLUGIN_ROOT", "").strip()
    if configured:
        return Path(configured).resolve()
    current = Path(__file__).resolve()
    for candidate in (current.parent, *current.parents):
        if (candidate / "skills").is_dir():
            return candidate
    return current.parents[2]


def skills_root() -> Path:
    configured = os.environ.get("SKILLS_FACTORY_SKILLS_ROOT", "").strip()
    root = Path(configured).resolve() if configured else _plugin_root() / "skills"
    if not root.is_dir():
        raise RuntimeError(f"Skills catalog is unavailable: {root}")
    return root


def _frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    marker = text.find("\n---", 4)
    if marker < 0:
        return {}, text
    metadata = yaml.safe_load(text[4:marker]) or {}
    return metadata if isinstance(metadata, dict) else {}, text


def _tree_digest(path: Path) -> str:
    digest = hashlib.sha256()
    for item in sorted(p for p in path.rglob("*") if p.is_file()):
        relative = item.relative_to(path).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(item.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _entry(skill_dir: Path) -> dict[str, Any]:
    metadata, _ = _frontmatter(skill_dir / "SKILL.md")
    nested = metadata.get("metadata") or {}
    name = str(metadata.get("name") or skill_dir.name)
    return {
        "name": name,
        "directory": skill_dir.name,
        "domain": skill_dir.parent.name,
        "kind": "skill",
        "description": str(metadata.get("description") or ""),
        "version": str(nested.get("version") or "unknown"),
        "maturity": str(nested.get("maturity") or "unknown"),
        "content_sha256": _tree_digest(skill_dir),
    }


def entries() -> list[dict[str, Any]]:
    result = []
    for skill_dir in sorted(p.parent for p in skills_root().rglob("SKILL.md")):
        result.append(_entry(skill_dir))
    return result


def catalog_digest(items: list[dict[str, Any]] | None = None) -> str:
    items = items if items is not None else entries()
    payload = "\n".join(
        f"{item['name']}:{item['content_sha256']}" for item in sorted(items, key=lambda x: x["name"])
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def list_skills() -> dict[str, Any]:
    items = entries()
    return {
        "catalog_name": "Skills Factory Lab parity catalog",
        "catalog_digest": catalog_digest(items),
        "source_revision": os.environ.get("SKILLS_FACTORY_SOURCE_REVISION", "unattested"),
        "channel": os.environ.get("SKILLS_FACTORY_CHANNEL", "unknown"),
        "skills": [
            {key: value for key, value in item.items() if key != "directory"}
            for item in sorted(items, key=lambda x: x["name"])
        ],
    }


def load_skill(skill_name: str) -> dict[str, Any]:
    if not isinstance(skill_name, str) or not _SAFE_NAME.fullmatch(skill_name):
        raise ValueError("skill_name must be a simple packaged skill name")
    matches = [item for item in entries() if item["name"] == skill_name]
    if not matches:
        raise ValueError(f"skill is not present in the packaged Lab catalog: {skill_name}")
    item = matches[0]
    skill_dir = skills_root() / item["directory"]
    _, instructions = _frontmatter(skill_dir / "SKILL.md")
    return {
        **{key: value for key, value in item.items() if key != "directory"},
        "execution_mode": "host_model_executes_loaded_instructions",
        "instructions": instructions,
        "source_revision": os.environ.get("SKILLS_FACTORY_SOURCE_REVISION", "unattested"),
    }
