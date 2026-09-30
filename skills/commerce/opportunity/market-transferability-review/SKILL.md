---
name: market-transferability-review
description: >
  Review whether a product or business model proven in one market is plausibly transferable to another market, especially US-to-Poland, without assuming foreign traction will repeat locally.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.1.0"
  maturity: production
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Market Transferability Review

## Purpose
Test whether the reasons a product works in the source market exist in the target market.


## Preconditions
Require a source market, target market and explicit source-market success evidence. If target-market use context is unknown, transferability cannot be treated as established.

## Inputs and evidence
Test local prevalence of the use environment, substitutes, price anchors, logistics, regulation and channel behavior in stages. Source-market reviews remain source-market evidence only.

## Uncertainty and tool failure
If target-market evidence cannot be retrieved, keep transferability unresolved and specify the cheapest context screen needed next. Do not copy source-market price/channel assumptions.

## Procedure
1. State source-market success hypothesis.
2. Separate universal problem drivers from market-specific drivers.
3. Compare customer behaviour, willingness to pay, household/lifestyle context, climate, regulation, distribution, fulfilment and category maturity.
4. Identify target-market substitutes and local price anchors.
5. Separate transferable product value from non-transferable channel or cultural advantages.
6. Sequence local validation from cheapest context evidence to more expensive offer/channel tests.
7. State what must be tested locally before launch.

## Decision rules
- Source-market traction is evidence about the source market, not the target market.
- Similar demographics do not prove similar willingness to pay.
- A transferable problem may still require a different offer, price, channel or form factor.
- Do not use TAM alone as transfer evidence.
- Validate whether the source-market use environment is sufficiently prevalent in the target market before testing the copied offer.
- A landing page or paid test should not precede cheaper validation of target context, substitutes and basic logistics when those can invalidate transferability.

## Output contract
Source success driver | target-market match | mismatch | confidence | local test required.
Then: transferability = strong / plausible / weak / unresolved.
Then: staged local validation path = cheapest context screen -> next evidence gate -> only then offer/channel test if earned.

## Model guidance
Default: standard.
