# P0 evidence reconciliation — 2026-10-09

This is a **bounded implementation and reconciliation entrypoint**, not a claim that
14 historical P0 items are finished. The legacy `BACKLOG.json` is historical
and its statuses are not current GitHub Issue/Project state.

## Verified directly from main

- `.github/workflows/validate-skills.yml` already runs security scanner,
  capability contract validator, static routing collision report, isolation
  tests, release/readiness tests and packaged artifact validation.
- `workflows/skill-development/WORKFLOW.md` already classifies
  NEW/ROUTING/BEHAVIOR/RESOURCE/DOCS changes.
- `skills/meta/skill-release-review/SKILL.md` already requires exact
  source/build/package/manifest identity and forbids conflating approval
  recommendations with deployment.
- `release/production-readiness.yaml` uses pending receipt states and
  personal-beta owner/expiry fields.

These are **source observations**, not claims of runtime/browser PASS,
configured GitHub rulesets, or completed historical acceptance criteria.

## Auditable inventory

Run:

```bash
python scripts/roadmap/audit_p0.py --output .tmp/p0-audit.json
python -m unittest discover -s scripts/roadmap/tests -p 'test_*.py'
```

The tool checks historical P0 IDs, duplicate IDs, missing/self dependencies,
and cycles through non-P0 dependencies. Every task is marked
`evidence_state: UNVERIFIED` until a separately reviewed source revision,
PR, CI receipt and runtime receipt justify a more specific disposition.

## Disposition and ordering

1. ENG-01/02 — reconcile exact source and release policy.
2. ENG-15/16/20 — verify scanner, side-effects, protections, publisher.
3. ENG-03/04/05/06/10 — validate meta skill behavior and routing.
4. ENG-08/17 — evaluate runner and registry gaps.
5. E2E-01/02 — verify exact deployed runtime + UI/browser receipts.

Open review-required Issues must not be closed because this report exists.
Do not modify E2E baseline, queue, receipts or claim a deployed Site.
