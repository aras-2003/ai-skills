from __future__ import annotations

import sys
from collections import defaultdict

from common import ValidationIssue, repo_root_from, split_frontmatter


def main() -> int:
    root = repo_root_from(__file__)
    issues: list[ValidationIssue] = []
    names = defaultdict(list)

    for skill_file in sorted((root / "skills").rglob("SKILL.md")):
        try:
            frontmatter, _ = split_frontmatter(skill_file.read_text(encoding="utf-8"))
        except Exception as exc:
            issues.append(ValidationIssue("blocker", str(skill_file), str(exc)))
            continue

        name = frontmatter.get("name")
        if isinstance(name, str):
            names[name].append(skill_file)

    for name, paths in names.items():
        if len(paths) > 1:
            issues.append(ValidationIssue("blocker", ", ".join(str(p) for p in paths), f"Duplicate skill name: {name}"))

    for issue in issues:
        print(issue)

    print(f"Catalog: {len(names)} unique skills")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
