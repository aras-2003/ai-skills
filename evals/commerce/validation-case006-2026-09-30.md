# Commerce Case 006 Validation — 2026-09-30

## Runtime

Model: Luna

Fixture:
- `evals/commerce/case-006-product-discovery.md`

## Result

Overall: PASS+ with minor hardening.

## Passed

- reduced ten raw signals to four hypotheses;
- returned no numerical ranking;
- kept purchase evidence separate from category/content signals;
- shortlisted a boring but operationally strong crevice-cleaning product;
- did not overvalue weighted blankets despite visible demand;
- deferred ingestibles because compliance complexity dominates discovery-stage viability;
- treated US garage-storage traction as a transferability question rather than Polish demand evidence;
- rejected premium cable clips due low problem intensity, commodity pressure and weak differentiation;
- avoided invented TAM, CAC and sales volumes;
- proposed low-cost qualitative validation rather than paid acquisition;
- made explicit reject/defer decisions and reduced the search space.

## Hardening required

The run repeatedly invented interview/demo sample sizes such as 8–10 or 10 participants without an evidence basis.

It also used willingness-to-buy statements after interviews/demos as if close to purchase evidence. These are useful qualitative signals but should remain weaker than deposits, reservations, purchases or other costly commitments.

## Regression rules

- discovery should reduce the search space, not create a business case;
- boring/testable can beat trendy/operationally weak;
- trend/social/US traction != purchase evidence;
- do not invent participant counts, test budgets or thresholds without an explicit evidence basis;
- stated willingness to buy != actual purchase evidence;
- use the cheapest decision-changing validation method first.

## Promotion decision

Promote `product-opportunity-discovery` to production 1.0.0 after adding the sample-size and evidence-strength guardrails above.

Fast/Luna is adequate for the tested broad mixed-signal discovery pattern.
