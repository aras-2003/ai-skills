# Commerce Case 005 Validation — 2026-09-30

## Runtime

Model: Luna

Fixture:
- `evals/commerce/case-005-false-us-pl-transfer.md`

## Result

Overall: PASS+ with hardening.

## Passed

- selected `market-transferability-review` as the central diagnostic;
- correctly added local problem-demand, competition/substitutes and economics questions;
- did not infer Polish demand from US reviews or creator traction;
- separated universal storage need from US-specific large-garage context;
- surfaced bulky freight and local price anchors as material transfer risks;
- deferred acquisition/supplier deep dives until local fit is clearer;
- returned BADAĆ TERAZ rather than copying the US thesis or buying inventory.

## Hardening required

The next-action plan bundled interviews/surveys, local market evidence and a 350 PLN landing/reservation test into one validation sprint.

For a false-transfer case, the framework should stage evidence more strictly:
1. cheapest context screen first — prevalence of relevant storage environment/use case;
2. local substitutes and price anchors;
3. basic landed/logistics feasibility;
4. only if those gates survive, test willingness to pay / offer response;
5. paid acquisition last.

A target-market landing test should not be run merely because it is cheap if even cheaper context evidence could invalidate the source-market transfer thesis.

## Regression rules

- source-market traction != target-market demand;
- universal problem != transferable use context;
- transferability evidence should be staged from cheapest contextual screen to offer/channel tests;
- do not copy source-market price, channel or form factor before target-context fit is established;
- cross-market validation should stop early when the relevant use environment is too rare or local substitutes destroy the premium thesis.

## Expected corrected decision

BADAĆ TERAZ / RESEARCH NOW remains appropriate, but the next action should start with target-context prevalence, substitute/price-anchor evidence and basic logistics feasibility. Only if those survive should the workflow test a 350 PLN offer or paid acquisition.

## Promotion impact

Case 005 passes after hardening. The transferability sequencing rule should remain explicit before production promotion.
