---
name: decision-bottleneck-analysis
description: >
  Diagnose why specific material decisions are slow, repeatedly escalated or duplicated by tracing decision steps, waits, vetoes, evidence gaps and authority boundaries. Use after identifying a problematic decision class.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Decision Bottleneck Analysis

## Purpose
Find the actual source of decision latency rather than assuming governance is too heavy.

## Procedure
1. Select a small set of recent material decisions.
2. Reconstruct proposer, advisers, approvers/decision owner, evidence, timestamps and escalations.
3. Separate active decision time from waiting time.
4. Identify duplicate review, hidden veto, missing evidence, authority ambiguity, risk aversion and resource dependency.
5. Compare formal path with actual path.
6. Quantify latency where evidence permits.
7. Recommend the smallest bottleneck-removal experiment.

## Decision rules
- Do not infer bottlenecks from org charts alone.
- More governance is not a solution to unclear authority.
- A slow decision can be caused by missing evidence, not only too many approvers.
- Hidden vetoes count even when absent from formal governance.

## Output contract
Decision | formal path | actual path | wait points | vetoes | missing evidence | authority issue | latency | bottleneck hypothesis | validation experiment.

## Model guidance
Default: **standard**. Fast may be adequate for well-structured decision logs.

## Quality checks
- [ ] Formal vs actual path compared.
- [ ] Waiting distinguished from decision work.
- [ ] Bottleneck cause remains evidence-based.

