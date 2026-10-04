from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def split_markdown_row(line: str) -> list[str]:
    """Split a pipe table row while keeping escaped pipes inside cells."""
    cells = re.split(r"(?<!\\)\|", line.strip())
    if cells and not cells[0].strip():
        cells = cells[1:]
    if cells and not cells[-1].strip():
        cells = cells[:-1]
    return [cell.replace(r"\|", "|").strip() for cell in cells]


def build_catalog(markdown: str) -> dict[str, object]:
    skills: list[dict[str, str]] = []
    for line in markdown.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = split_markdown_row(line)
        if len(cells) != 6 or cells[0] == "Skill" or set("".join(cells)) <= {"-", ":", " "}:
            continue
        name, domain, maturity, version, description, source = cells
        if not all((name, domain, maturity, description, source)):
            raise ValueError(f"Invalid catalog row for {name or '(unnamed skill)'}")
        if source.startswith("/") or ".." in Path(source).parts:
            raise ValueError(f"Unsafe source path for {name}: {source}")
        skills.append({
            "name": name,
            "domain": domain,
            "maturity": maturity,
            "version": version,
            "description": description,
            "source": source,
        })
    if not skills:
        raise ValueError("CATALOG.md did not contain any skill rows")
    return {"skills": skills}


def main() -> int:
    source = ROOT / "CATALOG.md"
    output = ROOT / "docs" / "catalog.json"
    catalog = build_catalog(source.read_text(encoding="utf-8"))
    output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated site catalog with {len(catalog['skills'])} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
