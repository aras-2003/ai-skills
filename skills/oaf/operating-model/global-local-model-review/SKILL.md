---
name: global-local-model-review
description: >
  Review how responsibilities, standards, capabilities and decisions are split between global/central and local units. Use when the organisation needs to balance scale and consistency against local context and speed; do not default to centralisation.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Global Local Model Review

## Purpose
Diagnose whether the global/local split supports enterprise outcomes without unnecessary centralisation.

## Procedure
1. Identify the decisions/capabilities that currently sit global, central, regional and local.
2. For each, state why the placement exists: scale, risk, interoperability, expertise, regulation, customer proximity or speed.
3. Identify duplicated ownership, unclear boundaries and local workarounds.
4. Assess whether standards are mandatory, configurable or advisory.
5. Review whether local units can influence global standards with evidence.
6. Separate structural problems from poor implementation of an otherwise sensible model.
7. Produce design implications, not a final redesign.

## Decision rules
- Centralise for material scale, consistency, interoperability or enterprise risk.
- Localise where context, responsiveness or regulation materially matter.
- A global standard without feedback/adaptation can create hidden local workarounds.
- Autonomy without enterprise guardrails can externalise cost and risk.

## Output contract
Current split | rationale | observed friction | enterprise consequence | local consequence | evidence needed | design implication.

## Model guidance
Default: **standard**. Escalate for multi-country redesign or highly contested sovereignty/autonomy choices.

## Quality checks
- [ ] Centralisation/autonomy rationale explicit.
- [ ] Local workarounds treated as evidence, not automatically noncompliance.
- [ ] Design implication separated from redesign.

