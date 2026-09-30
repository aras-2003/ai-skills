---
name: supplier-viability-review
description: >
  Assess whether sourcing, MOQ, lead time, quality, packaging and supplier concentration make a product viable to test and scale.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.1.0"
  maturity: production
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: fast
---

# Supplier Viability Review

## Purpose
Separate attractive product economics from sourcing and inventory reality.


## Preconditions
Require a defined product specification and target market. Quote-based conclusions require quote scope, date/currency and what freight/duty/packaging are included.

## Inputs and evidence
Separate sample evidence from production reliability. Capture MOQ, lead time, landed-cost scope, certifications where relevant, defect/quality evidence, backup suppliers and inventory exposure.

## Uncertainty and tool failure
If current supplier/quote evidence is unavailable, keep cost, MOQ and lead time unresolved. Never convert a sample result or one marketplace listing into proven scale reliability.

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
