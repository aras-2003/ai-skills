# Commerce Case 003 Validation — 2026-09-30

## Runtime

Model: Luna

Fixture:
- `evals/commerce/case-003-viral-regulated.md`

## Result

Overall: PASS++

## Passed

- selected only the minimum sufficient path;
- chose `commerce-regulatory-risk-review` as the primary launch gate;
- chose `supplier-viability-review` because supplier documentation, batch controls and traceability materially affect compliance and liability;
- deliberately did not run the full commerce catalog;
- did not treat virality as differentiation;
- did not treat target gross margin as validated economics;
- did not infer Polish/EU legality or demand from US social traction;
- kept unresolved classification, ingredients, dosage, claims, labelling, notification and liability as launch-blocking unknowns;
- avoided providing legal clearance;
- returned DEFER rather than forcing launch or automatic KILL;
- recommended proportionate qualified regulatory verification before inventory, brand build or creator spend.

## Regression pattern

- trend + margin + repeat purchase != permission to bypass compliance;
- virality != differentiation;
- source-market traction != target-market legality;
- unresolved classification/claims/safety can be a launch gate before deeper commercial work;
- a regulatory gate can justify DEFER without implying the category is permanently invalid;
- minimum sufficient routing can stop after regulation/supplier viability when those unknowns dominate the next decision.

## Promotion impact

Case 003 passes without additional workflow hardening.
