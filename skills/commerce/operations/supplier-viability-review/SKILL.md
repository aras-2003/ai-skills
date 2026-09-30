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

## Preconditions and evidence contract
Required: product specification and at least the scope of supplier evidence available. For each quote record supplier/source, date, MOQ, Incoterm or freight scope, unit basis and what is excluded. Distinguish sample quality from production reliability.

If quotes, certifications or factory evidence are unavailable, label landed cost, quality consistency and scale viability unresolved rather than inferring them.

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

- A supplier quote without freight/duty/packaging scope is not a landed-cost estimate.
- One good sample does not establish batch consistency.

## Failure / uncertainty handling
- If required source/tool evidence is unavailable, report the unresolved field explicitly.
- Do not substitute generic market knowledge for a missing current quote, channel result or target-market fact.

## Output contract
Supplier | MOQ | landed-cost evidence | lead time | quality risk | customisation | concentration | test viability | scale risk.

## Model guidance
Default: fast; standard when supplier trade-offs materially affect the business case.
