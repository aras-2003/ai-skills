# Commerce Case 001 Validation — 2026-09-30

## Runtime

Model: Luna

Fixture:
- `evals/commerce/case-001-premium-vs-generic.md`

## Result

Overall: PASS+

## Passed

- problem vs willingness-to-pay separation;
- premium branding was not treated as differentiation;
- break-even CAC was distinguished from target CAC;
- evidence / hypothesis / unknown separation;
- MOQ and inventory restraint;
- acquisition fit treated as plausible but unvalidated.

## Hardening required

The run selected TEST NOW even though two cheaper pre-market blockers remained:
- sample performance versus 20–35 PLN generics;
- reliable landed-cost range.

A paid market test should not be the first experiment when a cheaper experiment can invalidate the premium thesis.

The run also proposed an illustrative ad budget without a user-supplied budget or explicit sample-size/evidence basis.

## Regression rules

- market test != first test;
- if a cheaper pre-market experiment can invalidate the thesis, run it first;
- break-even CAC is a ceiling, not a target;
- incomplete landed cost makes CAC headroom provisional;
- do not invent test spend caps without a budget or evidence basis.

## Expected corrected decision

RESEARCH ONE BLOCKER:
validate sample performance against a cheap generic and confirm landed cost; if the visible premium advantage survives and CAC headroom remains credible, then move immediately to a bounded paid demand test.

## Promotion impact

Case 001 is not a blocker after hardening, but the regression must remain explicit in the workflow before promotion.
