---
name: capability-gap-analysis
description: >
  Identify material gaps between required business capabilities and current organisational, process, information or technology enablement. Use after strategic outcomes are sufficiently clear; do not turn capability gaps directly into technology projects.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Capability Gap Analysis

## Purpose
Identify which capabilities are insufficient for the target outcome and what dimension of the capability is weak.

## Procedure
1. Start from strategic/business outcomes, not an application inventory.
2. Identify the small set of capabilities materially required.
3. Assess each capability across ownership, people/skills, process, information/data, technology and governance where relevant.
4. Separate capability absence from low maturity, capacity constraint or poor integration.
5. Identify dependencies between capabilities.
6. Distinguish evidence from assumptions.
7. State intervention hypotheses without prematurely selecting projects.

## Decision rules
- A capability is what the organisation must be able to do, not an org unit or system.
- Do not translate every gap into a new platform.
- Capability ownership and operating model may be the primary gap even when technology symptoms exist.

## Output contract
Capability | required outcome | current evidence | gap type | affected dimension | dependency | consequence | confidence | intervention hypothesis.

## Model guidance
Default: **standard**.

## Quality checks
- [ ] Outcome-to-capability traceability.
- [ ] Capability vs process/org/system distinction preserved.
- [ ] No automatic technology solution.

