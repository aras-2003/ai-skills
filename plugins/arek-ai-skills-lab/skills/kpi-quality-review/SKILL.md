---
name: kpi-quality-review
description: 'Review whether a defined KPI set is decision-useful, interpretable and
  linked to outcomes, owners, thresholds and actions. Use after the relevant decisions/outcomes
  are known; do not generate a generic KPI catalogue.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.1.0
  maturity: candidate
  risk: low
  last_reviewed: '2026-09-30'
---

# KPI Quality Review

## Purpose
Assess whether an existing KPI set supports real decisions and learning.

## Procedure
1. Identify the outcome and decision each KPI is intended to inform.
2. Check definition, formula, source, owner, frequency and data quality.
3. Classify leading/lagging and activity/outcome characteristics.
4. Check target/baseline/threshold and whether action is specified.
5. Detect duplicates, vanity metrics, conflicting measures and local optimisation incentives.
6. Identify missing measures only where a decision cannot be made without them.
7. Recommend removal, refinement or validation before adding new KPIs.

## Decision rules
- A KPI with no linked decision is suspect.
- More KPIs reduce signal when they compete for attention.
- Activity metrics can be useful but must not masquerade as outcomes.
- Do not invent a target value without evidence.

## Output contract
KPI | decision/outcome | definition quality | owner | cadence | threshold | action | issue | recommendation.

## Model guidance
Default: **fast** for structured KPI sets; escalate when business meaning or incentives are contested.

## Quality checks
- [ ] Every KPI linked to a decision/outcome.
- [ ] Activity vs outcome distinction explicit.
- [ ] No generic catalogue expansion.

