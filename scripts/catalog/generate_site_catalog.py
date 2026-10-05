from __future__ import annotations

import json
import os
import re
import subprocess
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


def parse_package_manifest(text: str) -> dict[str, dict[str, str]]:
    """Read package identities without adding a YAML dependency."""
    packages: dict[str, dict[str, str]] = {}
    for key, label in (("package", "production"), ("lab", "lab")):
        match = re.search(
            rf"(?ms)^{re.escape(key)}:\s*\n(.*?)(?=^[^ \t]|\Z)",
            text,
        )
        if not match:
            raise ValueError(f"Missing {key} package metadata")
        section = match.group(1)
        name = re.search(r"(?m)^  name:\s*([^\n#]+)", section)
        version = re.search(r"(?m)^  version:\s*['\"]?([^'\"\s#]+)", section)
        if not name or not version:
            raise ValueError(f"Missing name or version for {key} package")
        packages[label] = {"name": name.group(1).strip(), "version": version.group(1).strip()}
    return packages


def build_catalog(
    markdown: str,
    package_manifest: str,
    source_revision: str,
) -> dict[str, object]:
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
    revision = source_revision.strip()
    if not revision:
        raise ValueError("Source revision is required for version provenance")
    return {
        "metadata": {
            "packages": parse_package_manifest(package_manifest),
            "source_revision": revision[:12],
        },
        "skills": skills,
    }


def current_revision() -> str:
    revision = os.environ.get("GITHUB_SHA") or os.environ.get("SOURCE_REVISION")
    if revision:
        return revision[:12]
    try:
        return subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", "--short=12", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def main() -> int:
    source = ROOT / "CATALOG.md"
    package_source = ROOT / "release" / "package.yaml"
    output = ROOT / "docs" / "catalog.json"
    catalog = build_catalog(
        source.read_text(encoding="utf-8"),
        package_source.read_text(encoding="utf-8"),
        current_revision(),
    )
    output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated site catalog with {len(catalog['skills'])} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
