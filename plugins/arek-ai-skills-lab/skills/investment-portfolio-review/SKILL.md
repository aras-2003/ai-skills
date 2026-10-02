---
name: investment-portfolio-review
description: Review a user's investment portfolio end to end. Use when the user asks
  to review "my portfolio" or "this portfolio", asks what requires attention, or provides
  holdings/weights and wants concentration, diversification, ETF overlap, portfolio
  risk, policy fit, drift or next decisions. Trigger even when the user does not name
  Investment OS, XTB, canonical records or this workflow. Start from canonical portfolio
  state when available, reconcile user-supplied holdings as evidence rather than replacing
  canonical state, then run the integrated report and required visual-floor path.
metadata:
  owner: arkadiusz-kamrowski
  version: 0.2.0
  maturity: production
  risk: high
  last_reviewed: '2026-10-02'
---

# Investment Portfolio Review Runtime Entrypoint

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

- `references/evals/case-003-portfolio-review.input.md`
