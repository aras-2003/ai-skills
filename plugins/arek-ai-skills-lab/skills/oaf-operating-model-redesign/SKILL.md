---
name: oaf-operating-model-redesign
description: Run an evidence-gated OAF operating-model redesign workflow from diagnosis
  through options, decision architecture and bounded transition design.
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
        - bounded operating-model redesign
        - option generation
        - trade-off analysis
        - pilot design
      sol:
        status: comparative-pass
        validated_on: 2026-09-30
        incremental_value:
        - stronger option framing
        - stronger selection discipline
        material_decision_change: false
---

# Oaf Operating Model Redesign Runtime Entrypoint

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

## Lab runtime eval fixtures

When the user explicitly asks to run one of the exact lab eval cases below, load the corresponding file from `references/evals/` before executing the skill. Do not substitute another case or reconstruct missing details from memory.

- `references/evals/case-operating-model-redesign-001.md`
