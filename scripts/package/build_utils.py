from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import yaml

RUNTIME_DIRS = ("references", "scripts", "assets")
EXCLUDED_NAMES = {"__pycache__", ".DS_Store"}
EXCLUDED_SUFFIXES = (".pyc", ".pyo", ".rubric.yaml")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def source_revision(root: Path) -> str:
    override = os.environ.get("SOURCE_REVISION")
    if override:
        return override
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True
        ).strip()
    except Exception:
        return "unknown"


def load_versions(root: Path) -> dict:
    data = yaml.safe_load((root / "release" / "package.yaml").read_text(encoding="utf-8")) or {}
    return data


def package_version(root: Path, key: str) -> str:
    data = load_versions(root)
    section = data.get(key) or {}
    version = section.get("version")
    if not isinstance(version, str) or not version:
        raise ValueError(f"release/package.yaml: missing {key}.version")
    return version


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def sha256_tree(path: Path) -> str:
    h = hashlib.sha256()
    for item in sorted(p for p in path.rglob("*") if p.is_file()):
        rel = item.relative_to(path).as_posix().encode()
        h.update(len(rel).to_bytes(4, "big"))
        h.update(rel)
        data = item.read_bytes()
        h.update(len(data).to_bytes(8, "big"))
        h.update(data)
    return h.hexdigest()


def _resolved(path: Path) -> Path:
    return path.resolve(strict=False)


def validate_output_path(root: Path, output: Path) -> Path:
    root = _resolved(root)
    output = _resolved(output)
    forbidden = {
        root,
        _resolved(root / ".git"),
        _resolved(root / "skills"),
        _resolved(root / "workflows"),
        _resolved(root / "scripts"),
        Path(output.anchor),
    }
    if output in forbidden:
        raise ValueError(f"unsafe output path: {output}")
    try:
        output.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"output must stay inside repository: {output}") from exc

    current = output
    while current != root:
        if current.exists() and current.is_symlink():
            raise ValueError(f"output path traverses symlink: {current}")
        current = current.parent
    return output


@contextmanager
def atomic_output(root: Path, output: Path) -> Iterator[Path]:
    output = validate_output_path(root, output)
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=f".{output.name}.stage-", dir=output.parent))
    backup = output.parent / f".{output.name}.backup"
    if backup.exists():
        shutil.rmtree(backup)
    try:
        yield stage
        if output.exists():
            output.rename(backup)
        try:
            stage.rename(output)
        except Exception:
            if backup.exists() and not output.exists():
                backup.rename(output)
            raise
        if backup.exists():
            shutil.rmtree(backup)
    except Exception:
        if stage.exists():
            shutil.rmtree(stage)
        raise


def include_runtime_file(rel: Path) -> bool:
    if any(part in EXCLUDED_NAMES for part in rel.parts):
        return False
    if rel.parts and rel.parts[0] == "tests":
        return False
    if rel.name.startswith(".") and rel.name != ".well-known":
        return False
    if any(rel.name.endswith(suffix) for suffix in EXCLUDED_SUFFIXES):
        return False
    return True


def copy_runtime_support(src_skill: Path, dst_skill: Path) -> list[str]:
    inventory: list[str] = []
    for dirname in RUNTIME_DIRS:
        source = src_skill / dirname
        if not source.exists():
            continue
        for path in sorted(p for p in source.rglob("*") if p.is_file()):
            rel = path.relative_to(src_skill)
            if not include_runtime_file(rel):
                continue
            target = dst_skill / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
            inventory.append(rel.as_posix())
    return inventory


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
