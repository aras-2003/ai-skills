---
name: acquisition-fit-review
description: >
  Assess whether a product is suitable for paid social and other direct-response acquisition based on demo strength, hooks, creative depth and CAC headroom.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.0.0"
  maturity: production
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Acquisition Fit Review

## Purpose
Test whether the product can be explained and sold efficiently through the intended acquisition channel.

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

## Output contract
Angle | hook | proof/demo | audience | likely friction | test creative.
Then: acquisition fit = strong / testable / weak.

## Model guidance
Default: standard.
