---
name: problem-demand-validation
description: >
  Validate whether a target customer problem is frequent, painful and purchase-relevant enough to justify product testing. Use before assuming category interest equals demand.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: low
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Problem Demand Validation

## Purpose
Determine whether a real problem creates credible willingness to act and pay.

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
