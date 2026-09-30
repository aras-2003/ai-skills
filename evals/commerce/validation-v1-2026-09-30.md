# Commerce Opportunity Framework V1 Validation — 2026-09-30

## Scope

Validated runtime patterns on Luna:
- Case 001 — premium vs cheap generic: PASS+ after hardening
- Case 002 — good demand, bad economics: PASS++
- Case 003 — viral but regulated: PASS++
- Case 004 — boring winner: PASS+ after hardening
- Case 005 — false US-to-PL transfer: PASS+ after hardening

## Production-validated capabilities

- broad mixed-signal product discovery and shortlist reduction
- problem-demand validation
- competition/substitute framing
- premium differentiation discipline
- unit-economics gating
- supplier/MOQ and logistics screening
- paid-acquisition fit
- regulatory-risk triage
- cross-market transferability
- end-to-end known-product deep dive
- selective opportunity screening/selection

## Regression guardrails

- popular product != good business
- search/social interest != purchase intent
- premium branding != differentiation
- gross margin != contribution margin
- break-even CAC != target CAC
- good demand != viable paid-acquisition economics
- trend/margin/repeat purchase do not bypass compliance
- market test != first test
- use the cheapest falsifying experiment first
- do not invent media spend caps
- source-market success != target-market demand
- universal problem != transferable use context
- stage cross-market evidence before offer/channel tests

## Production boundary

`product-opportunity-discovery` is production-valid for broad mixed-signal discovery and shortlist reduction after Case 006 PASS+ with minor hardening.

`commerce-opportunity-review` is production-valid for discovery, screening/selection of known opportunities, regulation-first triage and cross-market transferability.

## Model routing

Standard/Luna is adequate for the tested screening, deep-dive and evidence-gated decisions.

Fast remains appropriate for narrow extraction/competition/supplier tasks where interpretation is limited.

Strong is escalation-only for high-capital, highly regulated or strategically coupled decisions where conflicting evidence materially changes a consequential commitment.

## Promotion decision

Promote the validated Commerce V1 discovery + screening/selection stack to production 1.0.0.
