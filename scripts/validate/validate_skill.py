from __future__ import annotations

import argparse
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from common import NAME_RE, ValidationIssue, load_json, repo_root_from, split_frontmatter

RECOMMENDED_HEADINGS = ("## Purpose", "## Procedure", "## Output contract", "## Quality checks")


def validate_skill(skill_dir: Path, schema: dict) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        return [ValidationIssue("blocker", str(skill_dir), "Missing SKILL.md")]

    try:
        frontmatter, body = split_frontmatter(skill_file.read_text(encoding="utf-8"))
    except Exception as exc:
        return [ValidationIssue("blocker", str(skill_file), str(exc))]

    validator = Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(frontmatter), key=lambda e: list(e.path)):
        where = ".".join(str(x) for x in error.path)
        suffix = f" at {where}" if where else ""
        issues.append(ValidationIssue("blocker", str(skill_file), f"Frontmatter schema violation{suffix}: {error.message}"))

    name = frontmatter.get("name")
    if isinstance(name, str):
        if not NAME_RE.match(name):
            issues.append(ValidationIssue("blocker", str(skill_file), "name must be kebab-case"))
        if skill_dir.name != name:
            issues.append(ValidationIssue("blocker", str(skill_file), f"Folder name '{skill_dir.name}' must equal skill name '{name}'"))

    description = frontmatter.get("description")
    if isinstance(description, str):
        normalized = " ".join(description.split()).lower()
        if len(normalized) < 40:
            issues.append(ValidationIssue("high", str(skill_file), "description is too short for reliable routing"))
        if not any(token in normalized for token in ("use when", "when ", "use after", "before ", "after ")):
            issues.append(ValidationIssue("medium", str(skill_file), "description should state when the skill should be used, not only what it does"))

    if not body.strip():
        issues.append(ValidationIssue("blocker", str(skill_file), "SKILL.md body must not be empty"))

    for heading in RECOMMENDED_HEADINGS:
        if heading not in body:
            issues.append(ValidationIssue("low", str(skill_file), f"Recommended heading missing: {heading}"))

    for optional_dir in ("scripts", "references", "assets", "tests"):
        path = skill_dir / optional_dir
        if path.exists() and path.is_dir() and not any(path.iterdir()):
            issues.append(ValidationIssue("medium", str(path), "Empty optional directory should be removed"))

    for path in skill_dir.rglob("*"):
        if path.is_file() and path.name != "SKILL.md":
            rel = path.relative_to(skill_dir)
            if rel.parts[0] not in {"scripts", "references", "assets", "tests"}:
                issues.append(ValidationIssue("medium", str(path), "Supporting files should live under scripts/, references/, assets/ or tests/"))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Skill directories to validate; defaults to all skills/**/SKILL.md")
    args = parser.parse_args()

    root = repo_root_from(__file__)
    schema = load_json(root / "scripts/validate/schemas/skill.schema.json")
    skill_dirs = [Path(p).resolve() for p in args.paths] if args.paths else sorted({p.parent for p in (root / "skills").rglob("SKILL.md")})

    issues: list[ValidationIssue] = []
    for skill_dir in skill_dirs:
        issues.extend(validate_skill(skill_dir, schema))

    for issue in issues:
        print(issue)

    return 1 if any(i.severity in {"blocker", "high"} for i in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
