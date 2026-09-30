---
name: problem-demand-validation
description: >
  Validate whether a target customer problem is frequent, painful and purchase-relevant enough to justify product testing. Use before assuming category interest equals demand.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.1.0"
  maturity: production
  risk: low
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Problem Demand Validation

## Purpose
Determine whether a real problem creates credible willingness to act and pay.

## Preconditions and evidence contract
Required: target customer, problem/use context and at least one observable demand/problem signal. Separate engagement/search/reviews from purchase evidence. Record willingness-to-pay as UNKNOWN unless there is direct price/commitment evidence. Time-sensitive market evidence should include source/date when available.

If network/source access is unavailable, assess only the supplied evidence and label missing market evidence explicitly.

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

- Interview/survey intent is qualitative evidence; deposits, reservations, purchases or comparable costly commitment are stronger purchase evidence.
- Missing purchase evidence cannot be converted into a positive willingness-to-pay conclusion.

## Failure / uncertainty handling
- Do not fill missing evidence with remembered market facts.
- If evidence is insufficient for the requested verdict, return the unresolved question and the cheapest evidence step that could change it.

## Output contract
Customer | problem | frequency | intensity | workaround | purchase evidence | price evidence | unknowns | demand verdict.

## Model guidance
Default: standard.
