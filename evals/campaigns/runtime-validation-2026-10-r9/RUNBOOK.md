# Runtime Validation Campaign R9 — Investment Case 2 hardening

## Identity

- campaign: `runtime-validation-2026-10-r9`
- behavior source: `e301e7af458a2fb2461c7576960ba8415bf3435f`
- production package source version: `arek-ai-skills 1.11.0`
- Lab package source version: `arek-ai-skills-lab 0.5.0`

R1–R8 receipts remain historical evidence with their original source revisions and statuses.

## Purpose

R9 isolates the remaining Case 2 failures found after the R8 rerun:
- implausible or mis-extracted decision-critical Micron metrics were still used for valuation;
- an 8% review threshold was incorrectly converted into a provisional ceiling.

Primary retest focus:
- case-002-security-sizing

The executor receives only packaged input; evaluator rubrics remain isolated.

## Required runtime checks

Run the exact Case 2 executor prompt in a fresh Lab-only session. Then run two independent adversarial sessions:
1. evidence-sanity challenge using the observed implausible Micron figures;
2. review-threshold semantics challenge.

Static/offline checks are not runtime PASS.

## Promotion rule

Promote 1.11.0 to production only after:
- all static/eval/package gates are green;
- Case 2 rerun passes;
- evidence-sanity adversarial test passes;
- review-threshold semantics adversarial test passes.
