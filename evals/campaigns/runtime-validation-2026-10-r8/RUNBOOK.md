# Runtime Validation Campaign R8 — Investment OS E2E hardening

## Identity

- campaign: `runtime-validation-2026-10-r8`
- behavior source: `6a598a036133284852c1dcb9f295aaefbb69686d`
- production package source version: `arek-ai-skills 1.10.0`
- Lab package source version: `arek-ai-skills-lab 0.4.0`

R1–R7 receipts remain historical evidence with their original source revisions and statuses.

## Purpose

R8 re-pins behavior after the first Investment OS E2E campaign exposed three runtime failure classes: noncanonical local persistence, missing canonical portfolio-history retrieval, and unsafe use of unverified decision-critical financial metrics. It also hardens the valuation/priced-in gate before sizing.

Primary retest focus:
- case-001-opportunity-hunter
- case-002-security-sizing
- case-003-portfolio-review

The executor still receives only packaged `.input.md`; evaluator rubrics remain isolated.

## Prepare

~~~bash
python scripts/eval/campaign.py validate
python scripts/eval/campaign.py prepare --output .tmp/runtime-campaign-r8
python scripts/eval/campaign.py validate-lock --lock .tmp/runtime-campaign-r8/lock.json
python scripts/eval/campaign.py validate-evidence
~~~

Static/offline checks are not runtime PASS.

## Promotion rule

First rerun the three investing regression cases on the fresh candidate artifact. Promote to production only after static/package gates are green and no high-severity investing regression remains open.
