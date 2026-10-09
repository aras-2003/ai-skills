# R17 Lab-only Runtime Retest Summary

Campaign: `runtime-validation-2026-10-r17` — **45 active cases**, all pinned to Lab.

## Results

| Status | Count | Interpretation |
|---|---:|---|
| PASS | 36 | Completed Lab cases across Commerce, career routing, executive-role evaluation, OAF workflows and KPI quality review |
| FAIL | 9 | See the failure list below; includes domain behavior failures and strict routing/evidence failures |
| REVIEW_REQUIRED | 0 | All 45 active cases have a binary independent verdict |
| Executed but unrated | 0 | None |
| Not run | 0 | All 45 active Lab cases executed and independently evaluated |

## Evidence format

The `transcript-receipt.json` files preserve the observed Chat references, verdicts and hashes from this campaign. They do not contain the complete raw outputs, tool traces and artifact smoke evidence required by the repository’s machine-validated `receipt.json` schema. The 36/9 counts are independent transcript verdicts, not machine-certified runtime execution evidence. Original values and verdicts are preserved; no missing trace or artifact identity has been invented.

## Scope and channel

The Lab artifact contains all targets for the 42 domain/routing cases that had previously been auto-pinned to Production. Those cases are reassigned to Lab without changing their behavioral rubrics. Thus the full Lab campaign is 42 reassigned cases plus the 3 originally Lab-pinned cases.

Two tests specifically assert Production catalog absence/fallback behavior and cannot be meaningfully executed in Lab. They are excluded from R17 and retained in the campaign definition for a future Production campaign:

- `fallback-strategy-production-002`
- `fallback-interface-explicit-production-002`

Six earlier diagnostic receipts remain preserved separately and excluded from counts because they used Chrome or otherwise do not meet current Lab-only scope. The premium-vs-generic case was subsequently executed in the in-app browser through Lab 0.33.6, independently reassessed against the full economics excerpt, and is included as PASS. The boring-winner case was freshly executed in a ChatGPT Chat via Cloud Next/Lab 0.33.6 and independently scored PASS 4/4.

## Valid Lab findings

- `career-role-eval-en` — PASS 2/2. Natural request routed to executive-role-evaluator; the report kept authority, budget, vendor control and staffing mandate as unknown until verified.
- `career-company-facts-pl` — PASS 2/2. Natural-language request routed to company-context-research, addressed requested company facts, distinguished group from Polish-entity data and a pending acquisition from completed ownership changes, and did not add career or role evaluation.
- `case-006-product-discovery` — PASS 10/10. Fresh Lab run and independent score; discovery criteria all met.
- `case-005-false-us-pl-transfer` — PASS 5/5. Fresh Lab run and independent score; US-to-Poland transfer assumptions were appropriately tested.
- `case-004-boring-winner` — PASS 4/4. A non-viral product is not penalized; small size, demonstrability and preliminary contribution are recognized without treating them as proof of demand. Physical differentiation is tested before a bounded paid test, and CAC/MOQ remain explicit unknowns.
- `case-003-viral-regulated` — PASS 5/5. Regulatory risk review is selected before commercial expansion. The report does not claim the product is unlawful or cleared; unresolved product identity, ingredients, dose, claims, labeling and supplier-quality evidence are hard gates. Commercial signals are acknowledged but do not override those gates. Next step is a proportionate formulation dossier and qualified PL/EU review; no brand build, ads or inventory.

- `case-002-good-demand-bad-economics` — PASS 4/4. Demand is acknowledged but separated from viability. Correct contribution/break-even CAC is 22.09 PLN versus expected paid CAC of 70–110 PLN; even zero refund loss remains negative at the low CAC boundary. MOQ exposure is separated from per-order economics. The workflow rejects the current offer without further broad demand research.

- `case-001-premium-vs-generic` — PASS 6/6. Lab 0.33.6. The premium price gap is the central blocker; calculations distinguish 86.88 PLN gross profit after COGS from 60.88 PLN contribution before CAC, with break-even CAC reduced by omitted costs. MOQ cash exposure is disclosed; paid-social demonstrability is recognized without claiming validated CAC; Polish WTP remains unproven; US premium pricing is not treated as local demand evidence.

- `career-cv-gaps-en` — PASS 2/2. Correctly performed a CV gap analysis and did not turn a target role's 500-person requirement into claimed experience. Stored-document use outside the case prompt is recorded as an isolation concern.
- `career-cv-tailor-pl` — FAIL. Routing worked, but the tailored CV included scale claims not supported by the August 2026 baseline (developer population, project count, management-line detail and total banking-program participants). This does not prove those numbers false; it means the supplied baseline did not substantiate them. The evaluator compared the specified claims, not the complete October CV. The local skill fix is not yet packaged or deployed, so this receipt remains evidence for the prior Lab artifact.
- `oaf-kpi-quality-en` — PASS 2/2. Reviewed all four KPIs individually and stayed within the requested KPI-definition review rather than redesigning the full evidence loop. No current KPI definition cards or operational data were provided, so the case assessed conceptual definition quality.
- `commerce-deep-dive-en`, `commerce-discovery-pl`, `commerce-economics-pl`, `commerce-supplier-en`, and `commerce-regulatory-en` — PASS, independently evaluated in Lab 0.33.6. Their receipts preserve each routing/decision rubric and separate evaluation evidence.
- `executive-role-001` through `executive-role-007` — PASS. The tested cases preserve uncertainty in thin role descriptions; executive-role-007 correctly excludes role-fit analysis from standalone company research.
- `executive-role-008` — PASS 1/1. CV tailoring did not become a role evaluation; it requested the missing CTO job description instead of inventing requirements.
- `executive-role-009` — FAIL 2/4. A factual Kelvion research request referenced an earlier role discussion. The answer resumed CTO mandate/career-value analysis and recommended a diagnostic recruitment step. The evaluator judged this a context-contamination/scope violation.
- `executive-role-010` — PASS 4/4. Explicitly connected global technology functions to the local CTO mandate, with INVESTIGATE/LOW confidence and authority/reporting unknowns.
- `executive-role-011` to `executive-role-013` — PASS 15/15 assertions. Decision and confidence were explicit; critical unknowns remained visible; output expansion was relevant and numeric scores were not invented.



## Final batch and remaining failures

The campaign is complete: all **45/45 active Lab cases** have receipts and independent PASS/FAIL verdicts. The two Production-only fallback cases remain excluded from this Lab campaign and are not counted.

Additional independently scored results:

- `investment-policy-natural-pl`, `investment-portfolio-natural-en`, `investment-security-natural-en`, and `investment-theme-natural-en` — **FAIL**. The first three did not provide evidence of the required Investment OS front-door sequence; the portfolio case also lacked evidence of integrated visual-floor execution. The theme case explicitly reported routing to `investment-security-review` instead of thematic discovery. These are strict evidence/routing outcomes, not all proof that the front door was operationally skipped.
- `oaf-architecture-en`, `oaf-architecture-workflow-pl`, and `oaf-decision-bottleneck-natural-pl` — **PASS**. Architecture decisions were appropriately deferred without comparable evidence; the enterprise workflow integrated cross-domain implications; bottleneck hypotheses and experiments were kept evidence-gated.
- `oaf-decision-pl` — **FAIL**. The rubric expected `decision-rights-review`, but Lab routed to `decision-bottleneck-analysis`. The latter provided relevant diagnosis and avoided premature governance redesign, but the exact specialist-selection assertion failed.
- `oaf-interface-natural-pl`, `oaf-evidence-loop-pl`, `oaf-decision-rights-natural-pl`, `oaf-portfolio-health-en`, and `oaf-portfolio-priority-pl` — **PASS**. Each selected the expected Lab diagnostic/decision workflow, preserved uncertainty where evidence was missing, and avoided premature redesign, ranking or invented results.

The complete case-level receipts, evaluator scores, conversation IDs and evidence summaries are recorded under `evals/results/runtime-campaign-r17/`. All findings are Lab-only; Production behavior was not tested.
