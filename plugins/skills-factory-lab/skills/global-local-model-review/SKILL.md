---
name: global-local-model-review
description: 'Review how responsibilities, standards, capabilities and decisions are
  split between global/central and local units. Use when the organisation needs to
  balance scale and consistency against local context and speed; do not default to
  centralisation.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 1.0.0
  maturity: production
  risk: medium
  last_reviewed: '2026-09-30'
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
- Global consistency does not automatically require one global implementation.
- Treat local workarounds as diagnostic evidence, not automatic noncompliance.
- A global standard that is routinely bypassed may indicate poor implementation, unsuitable scope or legitimate local need.
- Autonomy without enterprise guardrails can externalise cost and risk.
- Distinguish structural design failure from poor execution of the current model.

## Output contract
Current split | rationale | observed friction | enterprise consequence | local consequence | evidence needed | design implication.

Then:
- global-consistency vs local-autonomy analysis;
- standards classification: mandatory / configurable / advisory;
- local-workaround evidence;
- structural vs implementation issues;
- minimum evidence before target-model selection.

## Model guidance
Default: **standard**.
Validated on Luna for global/local diagnosis and standards-placement review.
Escalate for multi-country target-model selection, highly contested sovereignty/autonomy choices, or material funding/authority redesign.

## Quality checks
- [ ] Centralisation/autonomy rationale explicit.
- [ ] Global consistency separated from single global implementation.
- [ ] Local workarounds treated as evidence, not automatically noncompliance.
- [ ] Mandatory/configurable/advisory distinction considered.
- [ ] Structural problem separated from implementation problem.
- [ ] Design implication separated from final redesign.

## Lab runtime eval inputs

When the user explicitly asks to run one of the exact lab eval cases below, load only the corresponding input file from `references/evals/`. The evaluator rubric is intentionally unavailable to the executor.

- `references/evals/case-global-local-001.input.md`
