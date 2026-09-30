# Commerce Case 002 Validation — 2026-09-30

## Runtime

Model: Luna

Fixture:
- `evals/commerce/case-002-good-demand-bad-economics.md`

## Result

Overall: PASS++

## Passed

- separated demand attractiveness from business viability;
- calculated net revenue after VAT correctly;
- included COGS, inbound freight/duty, fulfilment, payment fees and returns before CAC;
- derived approximately 22 PLN break-even CAC from the baseline assumptions;
- showed expected CAC 70–110 PLN produces structurally negative contribution;
- ran returns sensitivity and demonstrated that returns are not the sole issue;
- recognized that even zero-return economics remain unattractive at the expected CAC range;
- treated bulky logistics, storage and MOQ as downside risk rather than secondary detail;
- did not recommend a paid-social test merely because demand looked strong;
- correctly returned KILL for the current price / cost / channel thesis;
- preserved the distinction between killing the current offer and rejecting the category.

## Regression pattern

- good demand != good e-commerce economics;
- gross demand evidence does not override a failed contribution/CAC gate;
- returns can worsen economics without being the root cause;
- when expected CAC remains above break-even even under favorable sensitivity, do not spend on validation ads;
- KILL can apply to the current thesis while leaving the category open to a materially different price/cost/channel model.

## Promotion impact

Case 002 passes without additional workflow hardening.
