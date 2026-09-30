from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

from common import ValidationIssue, repo_root_from, split_frontmatter


def production_skills(root: Path) -> set[str]:
    names: set[str] = set()
    for path in (root / 'skills').rglob('SKILL.md'):
        fm, _ = split_frontmatter(path.read_text(encoding='utf-8'))
        metadata = fm.get('metadata') or {}
        if metadata.get('maturity') == 'production' and isinstance(fm.get('name'), str):
            names.add(fm['name'])
    return names


def production_workflows(root: Path) -> set[str]:
    data = yaml.safe_load((root / 'workflows/runtime-registry.yaml').read_text(encoding='utf-8')) or {}
    result: set[str] = set()
    for item in data.get('workflows') or []:
        metadata = item.get('metadata') or {}
        if metadata.get('maturity') == 'production' and isinstance(item.get('name'), str):
            result.add(item['name'])
    return result


def validate_readiness(root: Path) -> list[ValidationIssue]:
    path = root / 'release/readiness.yaml'
    issues: list[ValidationIssue] = []
    if not path.is_file():
        return [ValidationIssue('blocker', str(path), 'Missing production readiness record')]
    data = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    rows = data.get('components')
    if not isinstance(rows, list):
        return [ValidationIssue('blocker', str(path), 'components must be a list')]

    expected = {('skill', x) for x in production_skills(root)} | {('workflow', x) for x in production_workflows(root)}
    actual: set[tuple[str, str]] = set()
    for row in rows:
        if not isinstance(row, dict):
            issues.append(ValidationIssue('blocker', str(path), 'component record must be a mapping'))
            continue
        name = row.get('name')
        kind = row.get('kind')
        key = (kind, name)
        if not isinstance(name, str) or kind not in {'skill', 'workflow'}:
            issues.append(ValidationIssue('blocker', str(path), f'invalid readiness record: {row!r}'))
            continue
        if key in actual:
            issues.append(ValidationIssue('blocker', str(path), f'duplicate readiness record: {kind}/{name}'))
        actual.add(key)
        if row.get('maturity') != 'production':
            issues.append(ValidationIssue('blocker', str(path), f'{kind}/{name}: readiness record maturity must be production'))
        receipt = row.get('current_runtime_receipt')
        if receipt in {None, 'pending'}:
            exc = row.get('exception') or {}
            for field in ('status', 'owner', 'review_due', 'limitation'):
                if not isinstance(exc.get(field), str) or not exc.get(field).strip():
                    issues.append(ValidationIssue('blocker', str(path), f'{kind}/{name}: pending receipt requires exception.{field}'))
        hist = row.get('historical_evidence') or []
        if not isinstance(hist, list):
            issues.append(ValidationIssue('blocker', str(path), f'{kind}/{name}: historical_evidence must be a list'))
        else:
            for rel in hist:
                p = root / str(rel)
                if not p.is_file():
                    issues.append(ValidationIssue('blocker', str(path), f'{kind}/{name}: missing historical evidence path {rel}'))

    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    for kind, name in missing:
        issues.append(ValidationIssue('blocker', str(path), f'missing production readiness record: {kind}/{name}'))
    for kind, name in extra:
        issues.append(ValidationIssue('blocker', str(path), f'stale readiness record for non-production component: {kind}/{name}'))
    return issues


def main() -> int:
    root = repo_root_from(__file__)
    issues = validate_readiness(root)
    for issue in issues:
        print(issue)
    return 1 if any(i.severity in {'blocker', 'high'} for i in issues) else 0


if __name__ == '__main__':
    sys.exit(main())
