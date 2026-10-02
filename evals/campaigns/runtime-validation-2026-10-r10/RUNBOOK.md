# Runtime Validation Campaign R10 — Investment Data Platform migration

## Identity
- campaign: `runtime-validation-2026-10-r10`
- behavior source: `0900bca7816341b1727285669fac88148ebc4174`
- production package source version: `arek-ai-skills 1.12.0`
- Lab package source version: `arek-ai-skills-lab 0.6.0`

R1–R9 remain historical evidence.

## Purpose
R10 validates the Investment OS migration from spreadsheet-centric persistence to a layered data platform:

- Supabase/Postgres becomes the target canonical relational store after explicit cutover;
- Google Drive remains raw-document and migration/archive storage;
- structured equity/ETF research plugins provide breadth/context but are never canonical portfolio state;
- Firecrawl/primary sources verify decision-critical evidence;
- Data/analytics tooling provides derived analytics but does not write canonical state directly.

## Runtime focus
Retest:
- case-001-opportunity-hunter
- case-002-security-sizing
- case-003-portfolio-review
- case-004-theme-discovery
- case-006-attention-acn

Case 005 investment-policy-design is unchanged and is not the primary R10 regression focus.

## Additional migration checks
Before production cutover:
1. Supabase project/schema exists and passes security/performance advisor review.
2. Legacy 12-tab workbook is imported and reconciled.
3. Exactly one canonical backend is active.
4. No silent fallback to Sheets occurs after cutover.
5. Analytics outputs remain derived/noncanonical.
6. Research plugins do not become persistence sources.

## Promotion rule
Promote only after static/eval/package gates are green and the focused R10 runtime cases pass on the exact Lab artifact.
