---
name: oaf-enterprise-architecture-review
description: Run an evidence-gated OAF enterprise architecture review linking business
  outcomes, capabilities, operating model, architecture decisions and portfolio implications
  without inventing technology defects.
metadata:
  owner: arkadiusz-kamrowski
  version: 1.0.0
  maturity: production
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
    validated_models:
      luna:
        status: pass
        validated_on: 2026-09-30
        validated_use:
        - evidence-disciplined enterprise architecture review
        - bounded architecture option comparison
        - architecture stop-condition enforcement
---

# Oaf Enterprise Architecture Review Runtime Entrypoint

## Purpose

Expose a repository workflow to the skill runtime without duplicating its orchestration logic.

## Procedure

1. Load `references/WORKFLOW.md`.
2. Follow it as the authoritative orchestration procedure.
3. Route only to specialist skills that the workflow actually requires.
4. Preserve workflow gates, stop conditions and evidence discipline.
5. Do not replace the workflow with a generic best-practice answer.

## Output contract

Use the output contract defined in `references/WORKFLOW.md`.

## Quality checks

- [ ] The workflow source was loaded.
- [ ] Specialist skills were selected selectively.
- [ ] Workflow stage order and gates were preserved.
- [ ] Evidence and uncertainty remain explicit.
- [ ] No extra domain was added merely for completeness.
