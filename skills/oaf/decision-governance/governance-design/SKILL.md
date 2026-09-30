---
name: governance-design
description: >
  Design governance forums, decision cadence, inputs, escalation paths and accountabilities for a defined organisational problem. Use after decision or operating-model gaps are known; do not create committees without a clear decision purpose.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Governance Design

## Purpose
Create the minimum governance needed to make defined decisions well and quickly.

## Preconditions
Known decision set or diagnosed governance problem.

## Procedure
1. Define the decisions the governance system must enable.
2. Group decisions only where cadence, participants and evidence needs genuinely align.
3. Define each forum's mandate, decision rights, inputs, outputs, cadence and escalation.
4. Remove overlapping forums and duplicate approvals.
5. Define information requirements and pre-read standards.
6. Specify owner, membership and review mechanism.

## Decision rules
- No forum without a decision purpose.
- Governance should reduce decision latency, not add ceremony.
- Escalation must have a named destination and trigger.

## Output contract
Forum | purpose | decisions | owner | members | cadence | required inputs | outputs | escalation.

## Model guidance
Default: **standard**.

## Quality checks
- [ ] Every forum owns decisions.
- [ ] Overlap minimized.
- [ ] Escalation explicit.

