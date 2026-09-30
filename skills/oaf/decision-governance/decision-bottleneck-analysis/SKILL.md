---
name: decision-bottleneck-analysis
description: >
  Diagnose why specific material decisions are slow, repeatedly escalated or duplicated by tracing decision steps, waits, vetoes, evidence gaps and authority boundaries. Use after identifying a problematic decision class.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.0.0"
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
          - decision-path diagnosis
          - latency analysis
---

# Decision Bottleneck Analysis

## Purpose
Find the actual source of decision latency rather than assuming governance is too heavy.

## Procedure
1. Select a small set of recent material decisions.
2. Reconstruct proposer, advisers, approvers/decision owner, evidence, timestamps and escalations.
3. Compare the formal path with the actual path.
4. Separate active decision work, queue time, handoffs, waiting and rework where evidence permits.
5. Identify duplicate review, hidden veto, missing evidence, authority ambiguity, risk aversion and resource dependency.
6. Quantify latency only where timestamps or working-time evidence support it.
7. Recommend the smallest bottleneck-removal experiment.

## Decision rules
- Do not infer bottlenecks from org charts alone.
- A slow decision does not automatically mean too many approvers.
- Missing evidence, sequential review, duplicate review, shadow vetoes, queue time and authority ambiguity are distinct failure modes.
- A formal adviser can act as a de facto gate; verify this from actual progression behavior.
- Hidden vetoes count even when absent from formal governance.
- Do not call a review duplicate unless scope/evidence shows no material reason for repetition.
- More governance is not a solution to unclear authority.

## Output contract
Decision | formal path | actual path | wait points | vetoes/gates | missing evidence | authority issue | latency | bottleneck hypothesis | validation experiment.

Then:
- active work vs waiting/rework;
- hidden vetoes and duplicate reviews;
- authority diagnosis;
- smallest bottleneck-removal experiment;
- remaining evidence needed.

## Model guidance
Default: **standard**.
Validated on Luna for decision-path diagnosis and latency analysis.
Fast may be adequate for clean, structured decision logs. Escalate where executive authority or actual decision behavior is highly contested.

## Quality checks
- [ ] Formal vs actual path compared.
- [ ] Waiting/rework distinguished from decision work where evidence allows.
- [ ] Adviser vs de facto gate distinction tested.
- [ ] Duplicate review remains evidence-based.
- [ ] Smallest experiment targets the strongest confirmed bottleneck.
