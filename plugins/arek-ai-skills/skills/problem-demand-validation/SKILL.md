---
name: problem-demand-validation
description: 'Validate whether a target customer problem is frequent, painful and
  purchase-relevant enough to justify product testing. Use before assuming category
  interest equals demand.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 1.1.0
  maturity: production
  risk: low
  last_reviewed: '2026-09-30'
---

# Problem Demand Validation

## Purpose
Determine whether a real problem creates credible willingness to act and pay.


## Preconditions
Require a defined target customer/problem and target market or state them as unresolved. Do not use engagement metrics alone as proof of demand.

## Inputs and evidence
Prefer dated target-market purchase evidence, current workarounds, price anchors and costly commitments. Separate awareness, engagement, stated intent and actual purchase behavior.

## Uncertainty and tool failure
If current market evidence cannot be retrieved, state which demand claims remain unverified. Do not replace missing purchase evidence with search volume, reviews or social engagement.

## Procedure
1. Define customer, job/problem and usage context.
2. Assess frequency, intensity, urgency and current workaround.
3. Separate awareness, engagement, search and purchase-intent evidence.
4. Identify price anchors and willingness-to-pay evidence where available.
5. Check repeatability: one-off, replenishment, replacement or recurring need.
6. State what evidence is observed, inferred and unknown.

## Decision rules
- High search volume != high purchase intent.
- Emotional intensity can matter more than frequency.
- Existing workaround is evidence of need, but not automatically willingness to buy a premium solution.
- Do not infer willingness to pay from category popularity alone.

## Output contract
Customer | problem | frequency | intensity | workaround | purchase evidence | price evidence | unknowns | demand verdict.

## Model guidance
Default: standard.
