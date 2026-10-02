---
name: investment-os-review
description: Default Investment OS front door for natural investment requests. Use
  when the user asks in ordinary language to review their portfolio or holdings, assess
  a stock/security, find investment opportunities, research themes, evaluate whether
  new market/company information matters, or define portfolio policy/risk limits.
  Route first, then invoke the matching specialist workflow; use the MCP routing preflight
  when available and do not answer with generic investment commentary.
metadata:
  owner: arkadiusz-kamrowski
  version: 0.2.0
  maturity: production
  risk: high
  last_reviewed: '2026-10-03'
---

# Investment Os Review Runtime Entrypoint

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
