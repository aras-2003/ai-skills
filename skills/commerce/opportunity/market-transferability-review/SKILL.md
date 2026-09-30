---
name: market-transferability-review
description: >
  Review whether a product or business model proven in one market is plausibly transferable to another market, especially US-to-Poland, without assuming foreign traction will repeat locally.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Market Transferability Review

## Purpose
Test whether the reasons a product works in the source market exist in the target market.

## Procedure
1. State source-market success hypothesis.
2. Separate universal problem drivers from market-specific drivers.
3. Compare customer behaviour, willingness to pay, household/lifestyle context, climate, regulation, distribution, fulfilment and category maturity.
4. Identify target-market substitutes and local price anchors.
5. Separate transferable product value from non-transferable channel or cultural advantages.
6. State what must be tested locally before launch.

## Decision rules
- Source-market traction is evidence about the source market, not the target market.
- Similar demographics do not prove similar willingness to pay.
- A transferable problem may still require a different offer, price, channel or form factor.
- Do not use TAM alone as transfer evidence.

## Output contract
Source success driver | target-market match | mismatch | confidence | local test required.
Then: transferability = strong / plausible / weak / unresolved.

## Model guidance
Default: standard.
