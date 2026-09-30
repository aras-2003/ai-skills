from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

FORBIDDEN_PARTS = {"tests", "__pycache__"}


def validate_tree(path: Path, allow_lab_evals: bool = False) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing artifact: {path}"]
    for file in path.rglob("*"):
        if not file.is_file():
            continue
        rel = file.relative_to(path)
        if any(part in FORBIDDEN_PARTS for part in rel.parts):
            is_lab_eval = (
                allow_lab_evals
                and "evals" in rel.parts
                and "references" in rel.parts
                and (file.name.endswith(".input.md") or file.name == "INDEX.md")
            )
            if not is_lab_eval:
                errors.append(f"forbidden runtime content: {rel}")
        if file.name.endswith(".rubric.yaml"):
            errors.append(f"rubric leaked into runtime artifact: {rel}")
    return errors


def validate_zips(path: Path) -> list[str]:
    errors: list[str] = []
    index = path / "index.json"
    if not index.is_file():
        return [f"missing index.json in {path}"]
    data = json.loads(index.read_text(encoding="utf-8"))
    for item in data.get("capabilities", data.get("skills", [])):
        zip_name = item.get("zip")
        if not zip_name:
            continue
        zp = path / zip_name
        if not zp.is_file():
            errors.append(f"missing ZIP {zip_name}")
            continue
        with zipfile.ZipFile(zp) as zf:
            names = zf.namelist()
            if names != sorted(names):
                errors.append(f"{zip_name}: ZIP entries are not sorted")
            for name in names:
                parts = Path(name).parts
                if any(p in FORBIDDEN_PARTS for p in parts):
                    errors.append(f"{zip_name}: forbidden path {name}")
                if name.endswith(".rubric.yaml"):
                    errors.append(f"{zip_name}: rubric leaked: {name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--zips", action="store_true")
    parser.add_argument("--lab", action="store_true", help="allow executor-only references/evals/*.input.md in isolated Lab")
    args = parser.parse_args()
    errors = validate_zips(args.path) if args.zips else validate_tree(args.path, allow_lab_evals=args.lab)
    for error in errors:
        print(f"[BLOCKER] {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
