---
name: commerce-opportunity-review
description: Orchestrate the minimum evidence-backed path for discovering, screening
  and selecting e-commerce product opportunities without running the full commerce
  catalog by default.
metadata:
  owner: arkadiusz-kamrowski
  version: 1.0.0
  maturity: production
  risk: medium
  last_reviewed: '2026-09-30'
---

# Commerce Opportunity Review Runtime Entrypoint

## Purpose

Expose a repository workflow to the skill runtime without duplicating its orchestration logic.

## Procedure

1. Load `references/WORKFLOW.md`.
2. Follow it as the authoritative orchestration procedure.
3. Route only to specialist skills that the workflow actually requires.
4. Preserve workflow gates, stop conditions and evidence discipline.
5. If an optional dependency is unavailable, apply the declared reduced-scope behavior below and explicitly disclose that the specialist did not run.
6. Do not replace the workflow with a generic best-practice answer.

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

## Lab runtime eval inputs

When the user explicitly asks to run one of the exact lab eval cases below, load only the corresponding input file from `references/evals/`. The evaluator rubric is intentionally unavailable to the executor.

- `references/evals/case-003-viral-regulated.input.md`
- `references/evals/case-005-false-us-pl-transfer.input.md`
