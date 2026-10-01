---
name: supplier-viability-review
description: >
  Assess whether sourcing, MOQ, lead time, quality, packaging and supplier concentration make a product viable to test and scale. Use when supplier or inventory risk can change the launch decision.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.1.0"
  maturity: production
  risk: medium
  last_reviewed: "2026-09-30"
---

# Supplier Viability Review

## Purpose
Separate attractive product economics from sourcing, quality and inventory reality.

## Preconditions
Require a defined product and target market. A supplier quote may be incomplete; do not convert an incomplete quote into landed cost.

## Inputs and evidence
Capture quote date/currency/scope, MOQ, incoterm or freight/duty inclusion where known, packaging/customisation, sample evidence, production-quality evidence, certifications/documents, lead time and backup suppliers.

## Uncertainty and tool failure
If current quotes or supplier documents are unavailable, keep landed cost, quality or compliance claims unresolved. One sample is evidence about that sample, not production consistency.

## Procedure
1. Capture supplier options, quote scope, MOQ, sample availability, lead time and landed-cost evidence.
2. Review quality consistency, packaging/customisation, certifications and defect risk.
3. Assess supplier concentration and backup options.
4. Estimate inventory cash exposure separately from per-order economics.
5. Separate test-stage feasibility from scale-stage feasibility.

## Decision rules
- Low unit cost can be invalidated by MOQ or freight.
- One quote is not supplier-market evidence.
- Sample quality != production consistency.
- Scale viability requires replenishment reliability, not just launch stock.
- Unknown freight/duty/packaging means landed cost is unresolved.

## Output contract
Supplier | quote scope/date | MOQ | landed-cost evidence | lead time | quality evidence | customisation | concentration | test viability | scale risk | unknowns.

## Quality checks
- [ ] Quote scope is explicit.
- [ ] MOQ cash exposure is visible.
- [ ] Sample and production reliability are separated.
- [ ] Missing quote/documents are not silently filled.
