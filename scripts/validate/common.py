from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class ValidationIssue:
    def __init__(self, severity: str, path: str, message: str) -> None:
        self.severity = severity
        self.path = path
        self.message = message

    def __str__(self) -> str:
        return f"[{self.severity.upper()}] {self.path}: {self.message}"


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter delimited by ---")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter closing delimiter not found")
    raw = text[4:end]
    body = text[end + 5:]
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        raise ValueError("SKILL.md frontmatter must be a YAML mapping")
    return data, body


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_waivers(root: Path) -> list[dict[str, Any]]:
    path = root / "scripts" / "validate" / "waivers.yaml"
    if not path.exists():
        return []
    data = load_yaml(path) or {}
    waivers = data.get("waivers") or []
    if not isinstance(waivers, list):
        raise ValueError(f"{path}: waivers must be a list")
    return [w for w in waivers if isinstance(w, dict)]


def waiver_for(root: Path, rule: str, skill_name: str) -> dict[str, Any] | None:
    for waiver in load_waivers(root):
        if waiver.get("rule") == rule and skill_name in (waiver.get("skills") or []):
            return waiver
    return None


def repo_root_from(script_file: str) -> Path:
    return Path(script_file).resolve().parents[2]
