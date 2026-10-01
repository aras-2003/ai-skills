from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml

PORTABLE_METADATA_KEYS = ("owner", "version", "maturity", "risk", "last_reviewed")


def read_frontmatter(skill_md: Path) -> tuple[dict[str, Any], str]:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{skill_md}: missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{skill_md}: unterminated frontmatter")
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{skill_md}: frontmatter must be a mapping")
    return data, text[end + 5:]


def scalar_string(value: Any) -> str:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, (str, int, float, bool)):
        return str(value)
    raise TypeError(f"portable metadata values must be scalar, got {type(value).__name__}")


def portable_metadata(metadata: Any) -> dict[str, str]:
    if not isinstance(metadata, dict):
        return {}
    result: dict[str, str] = {}
    for key in PORTABLE_METADATA_KEYS:
        value = metadata.get(key)
        if value is not None:
            result[key] = scalar_string(value)
    return result


def portable_frontmatter(frontmatter: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "name": frontmatter.get("name"),
        "description": frontmatter.get("description"),
    }
    if frontmatter.get("compatibility") is not None:
        result["compatibility"] = str(frontmatter["compatibility"])
    metadata = portable_metadata(frontmatter.get("metadata"))
    if metadata:
        result["metadata"] = metadata
    return result


def render_portable_skill(skill_md: Path) -> str:
    frontmatter, body = read_frontmatter(skill_md)
    portable = portable_frontmatter(frontmatter)
    fm = yaml.safe_dump(portable, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{fm}\n---\n{body}"
