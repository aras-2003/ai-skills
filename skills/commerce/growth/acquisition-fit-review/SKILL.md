---
name: acquisition-fit-review
description: >
  Assess whether a product is suitable for paid social and other direct-response acquisition based on demo strength, hooks, creative depth and CAC headroom.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.1.0"
  maturity: production
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Acquisition Fit Review

## Purpose
Test whether the product can be explained and sold efficiently through the intended acquisition channel.

## Preconditions and evidence contract
Required: intended acquisition channel, target audience, product/offer hypothesis and either explicit CAC headroom from unit economics or a statement that headroom is unresolved. Treat creative engagement as channel signal, not proof of profitable acquisition.

If platform data or prior campaign evidence is unavailable, do not invent CPM, CTR, CVR or CAC.

## Procedure
1. State primary channel and target audience.
2. Identify visible problem, demo, before/after, emotional hook and proof opportunities.
3. Generate several distinct creative angles, not variants of one message.
4. Compare likely acquisition difficulty with allowable CAC from unit economics.
5. Flag policy/platform restrictions and weak demonstrability.
6. Distinguish product appeal from channel fit.

## Decision rules
- Great product + weak creative potential can be weak DTC.
- Viral content != profitable acquisition.
- One strong creative angle is fragile.
- Acquisition fit must be judged against CAC headroom, not engagement alone.

- Acquisition fit cannot be called strong when allowable CAC is unknown for a paid channel.
- Virality or creator engagement is not evidence of profitable conversion.

## Failure / uncertainty handling
- If required source/tool evidence is unavailable, report the unresolved field explicitly.
- Do not substitute generic market knowledge for a missing current quote, channel result or target-market fact.

## Output contract
Angle | hook | proof/demo | audience | likely friction | test creative.
Then: acquisition fit = strong / testable / weak.

## Model guidance
Default: standard.
