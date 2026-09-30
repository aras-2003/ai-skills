# Commerce Opportunity Framework — V1 Runtime Evals

## Runtime approach
Run Luna first. Evaluate routing and decisions before prose quality.

## Case 001 — Premium vs cheap generic
Target: `commerce-product-deep-dive`
Fixture: `references/evals/case-001-premium-vs-generic.md`

Prompt:
> Use the `commerce-product-deep-dive` workflow on the exact lab fixture `references/evals/case-001-premium-vs-generic.md`. Test why the customer would pay the premium, calculate CAC headroom, separate evidence/hypothesis/unknown, and end with TEST NOW / RESEARCH ONE BLOCKER / DEFER / KILL.

Focus:
- premium branding != differentiation;
- gross margin != contribution;
- US benchmark != local willingness to pay.
- market test != first test; if a cheaper sample/landed-cost experiment can invalidate the thesis, choose RESEARCH ONE BLOCKER first.
- no invented ad-spend cap without budget or evidence basis.

## Case 002 — Good demand, bad economics
Target: `commerce-product-deep-dive`
Fixture: `references/evals/case-002-good-demand-bad-economics.md`

Prompt:
> Use the `commerce-product-deep-dive` workflow on the exact lab fixture `references/evals/case-002-good-demand-bad-economics.md`. Calculate contribution and break-even CAC, run CAC/returns sensitivity, and do not let demand override a failed economics gate.

Focus:
- demand != viable economics;
- bulky logistics and returns matter;
- fail early when headroom is structurally weak.

## Case 003 — Viral but regulated
Target: `commerce-opportunity-review`
Fixture: `references/evals/case-003-viral-regulated.md`

Prompt:
> Use the `commerce-opportunity-review` workflow on the exact lab fixture `references/evals/case-003-viral-regulated.md`. Use the minimum sufficient path. Do not provide legal clearance. Treat unresolved compliance as a gate before launch.

Focus:
- trend/margin/repeat purchase do not override compliance;
- regulatory verification should be proportionate and early.

## Case 004 — Boring winner
Target: `commerce-product-deep-dive`
Fixture: `references/evals/case-004-boring-winner.md`

Prompt:
> Use the `commerce-product-deep-dive` workflow on the exact lab fixture `references/evals/case-004-boring-winner.md`. Do not penalise lack of trendiness. Decide whether the main remaining uncertainty is best resolved by more research or a bounded paid test.

Focus:
- boring != bad business;
- strong logistics/economics/demo can justify testing;
- stop research when CAC/conversion is the main unknown.

## Case 005 — False US-to-PL transfer
Target: `commerce-opportunity-review`
Fixture: `references/evals/case-005-false-us-pl-transfer.md`

Prompt:
> Use the `commerce-opportunity-review` workflow on the exact lab fixture `references/evals/case-005-false-us-pl-transfer.md`. Test market transferability explicitly and do not infer Polish demand from US traction.

Focus:
- source-market success != target-market success;
- lifestyle, price anchor, logistics and channel context can break transfer.
- validate target-context prevalence and substitutes before copying the source-market offer into a landing/paid test.
- evidence steps should be staged; do not run interviews, offer tests and paid acquisition in parallel if a cheaper context screen could already kill the thesis.

## Promotion threshold
Do not promote before:
- cases 001–005 pass on Luna;
- workflow routing remains selective;
- unit economics are arithmetically coherent;
- fatal gates can produce KILL/DEFER rather than forced testing;
- opportunity workflow can stop discovery/research at the right time.

A passing case validates the tested pattern only.


## Case 006 — Broad product discovery
Target: `product-opportunity-discovery`
Fixture: `references/evals/case-006-product-discovery.md`

Prompt:
> Use the `product-opportunity-discovery` skill on the exact lab fixture `references/evals/case-006-product-discovery.md`. Reduce the raw signals to the strongest 3–5 hypotheses worth deeper validation. Separate signal from purchase evidence, state deliberate rejects/defers, and choose the cheapest next validation step for each shortlisted idea. Do not rank numerically or run a full product deep dive.

Focus:
- discovery must reduce the search space;
- boring but testable can beat trendy but operationally weak;
- trend/US traction != purchase evidence;
- regulatory/logistics/commodity risks can remove ideas early;
- cheapest falsifying validation step first;
- no more than 5 shortlisted hypotheses.

## Discovery promotion threshold
Do not promote `product-opportunity-discovery` before Case 006 passes on Luna with:
- 3–5 hypotheses maximum;
- at least one explicit reject/defer;
- no invented TAM, sales, CAC or demand certainty;
- no numeric ranking;
- clear signal-vs-evidence distinction;
- no full deep dive;
- next steps staged by cheapest decision-changing experiment.


## Case 006 result

Luna result: PASS+ after minor hardening.

Hardening retained:
- do not invent participant counts, budgets or thresholds without an explicit basis;
- stated willingness to buy remains qualitative evidence, not purchase evidence;
- actual costly commitment is stronger evidence than interview intent.

Promotion: `product-opportunity-discovery` -> production 1.0.0.
