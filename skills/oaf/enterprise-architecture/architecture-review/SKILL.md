---
name: architecture-review
description: >
  Review alignment across business direction, capabilities, organisational design, information and technology architecture. Use for enterprise or organisational architecture decisions; do not use as a low-level software design review.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Architecture Review

## Purpose
Test whether organisational and technology architecture coherently supports strategic direction.

## Procedure
1. State the business outcomes and constraints.
2. Identify impacted capabilities, ownership and key dependencies.
3. Review organisation, process, information/data and technology implications.
4. Identify structural misalignments, duplicated capabilities, brittle dependencies and architecture debt.
5. Distinguish local optimisation from enterprise impact.
6. Recommend decision options with trade-offs and transition implications.

## Decision rules
- Architecture decisions must trace to business/capability needs.
- Avoid technology-only recommendations when the problem is organisational.
- Explicitly surface trade-offs and reversibility.

## Output contract
Context; affected capabilities; current-state issues; options; trade-offs; recommendation/decision needed; transition risks.

## Model guidance
Default: **standard**. Escalate to strong for novel cross-domain target architecture.

## Quality checks
- [ ] Business-to-architecture traceability.
- [ ] Organisational and technology dimensions both considered where relevant.
- [ ] Trade-offs explicit.

