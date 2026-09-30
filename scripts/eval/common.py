from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import yaml


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_registry(root: Path | None = None) -> dict[str, list[dict[str, Any]]]:
    root = root or repo_root()
    path = root / "evals" / "runtime-fixtures.yaml"
    data = load_yaml(path) or {}
    targets = data.get("targets")
    if not isinstance(targets, dict):
        raise ValueError(f"{path}: targets must be a mapping")
    return targets
