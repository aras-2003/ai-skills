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


def repo_root_from(script_file: str) -> Path:
    return Path(script_file).resolve().parents[2]
