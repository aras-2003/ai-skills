---
name: oaf-health-check
description: >
  Run the OAF Health Check workflow as a selective cross-domain organisational architecture diagnostic.
  Use when the user asks for a broad diagnosis spanning strategy execution, operating model, decision rights,
  governance, enterprise architecture, portfolio/execution or evidence loops. Do not use for a narrow issue
  that should route directly to one specialist OAF skill.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# OAF Health Check Runtime Entrypoint

## Purpose

Expose the repository workflow to the skill runtime without duplicating the workflow logic.

## Procedure

1. Load `references/WORKFLOW.md`.
2. Follow it as the authoritative orchestration procedure.
3. Route only to OAF specialist skills that are actually needed.
4. Diagnose before using design skills such as `governance-design` or `transformation-blueprint`.
5. Stop when adding another OAF domain would not improve the decision.

## Output contract

Use the workflow's output contract exactly:
- Executive diagnosis
- OAF heatmap
- Cross-domain causes
- Critical unknowns
- Recommended next action

## Quality checks

- [ ] Specialist skills were selected selectively.
- [ ] Diagnosis preceded design.
- [ ] Evidence and uncertainty are explicit.
- [ ] No domain was added merely for completeness.
