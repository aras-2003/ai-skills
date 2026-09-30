---
name: competition-landscape-review
description: >
  Review competition around an e-commerce opportunity across product, price, brand, distribution and acquisition. Use before calling a market empty or saturated.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.0.0"
  maturity: production
  risk: low
  last_reviewed: 2026-09-30
  execution:
    default_model_class: fast
---

# Competition Landscape Review

## Purpose
Understand how customers currently solve the problem and where competitive pressure actually sits.

## Procedure
1. Identify direct products, substitutes and do-nothing/workaround alternatives.
2. Compare price bands, offer structure, positioning and reviews.
3. Separate product competition, brand competition, distribution competition and acquisition competition.
4. Identify credible gaps, not merely absent local brands.
5. Flag commodity pressure and easy-copy risk.

## Decision rules
- Few local brands != low competition.
- Many cheap generics can cap premium willingness to pay.
- A category can be product-light but acquisition-heavy.
- Do not call a gap defensible unless there is a reason competitors cannot easily copy it.

## Output contract
Competitor/alternative | type | price | positioning | strength | weakness | implication.
Then: gap hypothesis, commodity risk, evidence gaps.

## Model guidance
Default: fast; escalate to standard when positioning or substitution boundaries are ambiguous.
