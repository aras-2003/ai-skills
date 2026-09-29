from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "validate"))
from common import repo_root_from, split_frontmatter  # noqa: E402


def main() -> int:
    root = repo_root_from(__file__)
    rows = []

    for skill_file in sorted((root / "skills").rglob("SKILL.md")):
        frontmatter, _ = split_frontmatter(skill_file.read_text(encoding="utf-8"))
        rel = skill_file.parent.relative_to(root)
        parts = rel.parts
        domain = parts[1] if len(parts) > 1 else ""
        metadata = frontmatter.get("metadata") or {}
        rows.append(
            (
                frontmatter.get("name", ""),
                domain,
                " ".join(str(frontmatter.get("description", "")).split()),
                metadata.get("maturity", ""),
                metadata.get("version", ""),
                str(rel / "SKILL.md"),
            )
        )

    out = [
        "# Skill Catalog",
        "",
        "> Generated from SKILL.md metadata. Do not edit manually.",
        "",
        "| Skill | Domain | Maturity | Version | Description | Source |",
        "|---|---|---|---|---|---|",
    ]
    for name, domain, description, maturity, version, source in rows:
        safe = description.replace("|", "\\|")
        out.append(f"| {name} | {domain} | {maturity} | {version} | {safe} | {source} |")

    (root / "CATALOG.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Generated CATALOG.md with {len(rows)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
