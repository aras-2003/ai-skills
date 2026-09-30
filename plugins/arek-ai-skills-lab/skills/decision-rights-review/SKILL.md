---
name: decision-rights-review
description: >
  Map and review critical organisational decision rights, including who proposes, decides, executes, advises and escalates. Use when decisions are slow, duplicated, political or unclear; do not use merely to create a generic RACI.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Decision Rights Review

## Purpose
Clarify how important decisions actually move through the organisation.

## Procedure
1. Select the critical decision set relevant to the problem.
2. For each decision, identify proposer, decision owner, mandatory advisers, execution owner and escalation path.
3. Compare formal governance with observed practice.
4. Detect duplicate vetoes, missing owners, shadow decisions, escalation loops and authority/accountability mismatch.
5. Classify each issue by impact on speed, quality and accountability.
6. Recommend the smallest decision-rights changes that remove the bottleneck.

## Decision rules
- Do not map every operational decision; focus on material decisions.
- One clear decision owner is preferred where feasible.
- Consultation is not decision authority.

## Output contract
Decision | current owner | actual owner | advisers | executor | escalation | issue | proposed change.

## Model guidance
Default: **standard**.

## Quality checks
- [ ] Formal vs actual practice distinguished.
- [ ] Decision owner explicit.
- [ ] Bottlenecks linked to consequences.

