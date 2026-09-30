---
name: supplier-viability-review
description: >
  Assess whether sourcing, MOQ, lead time, quality, packaging and supplier concentration make a product viable to test and scale.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.0.0"
  maturity: production
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: fast
---

# Supplier Viability Review

## Purpose
Separate attractive product economics from sourcing and inventory reality.

## Procedure
1. Capture supplier options, MOQ, sample availability, lead time and landed-cost evidence.
2. Review quality consistency, packaging/customisation, certifications and defect risk.
3. Assess supplier concentration and backup options.
4. Estimate inventory cash exposure and replenishment risk.
5. Separate test-stage feasibility from scale-stage feasibility.

## Decision rules
- Low unit cost can be invalidated by MOQ or freight.
- One supplier quote is not market evidence.
- Sample quality != production consistency.
- Scale viability requires replenishment reliability, not just launch stock.

## Output contract
Supplier | MOQ | landed-cost evidence | lead time | quality risk | customisation | concentration | test viability | scale risk.

## Model guidance
Default: fast; standard when supplier trade-offs materially affect the business case.
