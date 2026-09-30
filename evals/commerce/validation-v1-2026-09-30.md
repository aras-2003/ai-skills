# Commerce Opportunity Framework V1 Validation — 2026-09-30

## Scope

Validated runtime patterns on Luna:
- Case 001 — premium vs cheap generic: PASS+ after hardening
- Case 002 — good demand, bad economics: PASS++
- Case 003 — viral but regulated: PASS++
- Case 004 — boring winner: PASS+ after hardening
- Case 005 — false US-to-PL transfer: PASS+ after hardening

## Production-validated capabilities

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

`product-opportunity-discovery` remains candidate 0.1.0 because broad discovery mode has not yet received a dedicated runtime behavioral eval.

`commerce-opportunity-review` is production-valid for screening/selection of known opportunities, regulation-first triage and cross-market transferability. Its broad discovery mode remains candidate-only.

## Model routing

Standard/Luna is adequate for the tested screening, deep-dive and evidence-gated decisions.

Fast remains appropriate for narrow extraction/competition/supplier tasks where interpretation is limited.

Strong is escalation-only for high-capital, highly regulated or strategically coupled decisions where conflicting evidence materially changes a consequential commitment.

## Promotion decision

Promote the validated Commerce V1 screening/selection stack to production 1.0.0.

Do not promote `product-opportunity-discovery` until a dedicated discovery eval passes.
