---
name: differentiation-review
description: >
  Test whether an e-commerce offer has a credible reason to win versus cheap generics and established brands. Use when premium pricing, brand positioning or commodity risk matters.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.1.0"
  maturity: production
  risk: low
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Differentiation Review

## Purpose
Determine why a customer should choose this offer rather than a cheaper or better-known alternative.

## Preconditions and evidence contract
Require a target customer, competing alternative and a claimed advantage. Separate product/offer proof from brand language. State whether the advantage is observed, demonstrated, inferred or unproven.

If no sample/comparison proof exists, the differentiation verdict cannot exceed a hypothesis-level conclusion.

## Procedure
1. State the target customer and competing alternatives.
2. Identify functional, emotional, convenience, trust, bundle, guarantee, design and education advantages.
3. Separate real product differentiation from branding claims.
4. Test whether the differentiation is visible before purchase and demonstrable in ads/product page.
5. Assess copyability and durability.
6. Test whether the premium price has a concrete justification.

## Decision rules
- Premium branding alone != premium differentiation.
- Better packaging does not justify a 4x price unless it changes perceived or delivered value.
- A difference that cannot be communicated cheaply may not help paid acquisition.
- Commodity products require offer-level or audience-level differentiation.

- A premium story without observable customer value is not differentiation.
- Claims about superiority require proof against a relevant alternative, not only attractive creative.

## Failure / uncertainty handling
- Do not fill missing evidence with remembered market facts.
- If evidence is insufficient for the requested verdict, return the unresolved question and the cheapest evidence step that could change it.

## Output contract
Differentiator | customer value | proof | visibility | copyability | price-support effect.
Then: differentiated / weakly differentiated / commodity-risk.

## Model guidance
Default: standard.
