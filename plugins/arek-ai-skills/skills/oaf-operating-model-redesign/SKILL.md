---
name: oaf-operating-model-redesign
description: Run an evidence-gated OAF operating-model redesign workflow from diagnosis
  through options, decision architecture and bounded transition design.
metadata:
  owner: arkadiusz-kamrowski
  version: 1.1.0
  maturity: production
  risk: medium
  last_reviewed: '2026-10-01'
---

# Oaf Operating Model Redesign Runtime Entrypoint

## Purpose

Expose a repository workflow to the skill runtime without duplicating its orchestration logic.

## Procedure

1. Load `references/WORKFLOW.md`.
2. Follow it as the authoritative orchestration procedure.
3. Route only to specialist skills that the workflow actually requires.
4. Preserve workflow gates, stop conditions and evidence discipline.
5. If an optional dependency is unavailable, apply the declared reduced-scope behavior below and explicitly disclose that the specialist did not run.
6. Do not replace the workflow with a generic best-practice answer.

## Dependency availability

The following optional branches are unavailable in this package. Do not simulate or claim execution of the missing specialist:

- `organizational-interface-review`: Interface-specialist analysis is unavailable; disclose the gap and do not pretend it ran.

## Output contract

Use the output contract defined in `references/WORKFLOW.md`.

## Quality checks

- [ ] The workflow source was loaded.
- [ ] Specialist skills were selected selectively.
- [ ] Required dependencies were available.
- [ ] Missing optional dependencies were disclosed and not simulated.
- [ ] Workflow stage order and gates were preserved.
- [ ] Evidence and uncertainty remain explicit.
- [ ] No extra domain was added merely for completeness.
