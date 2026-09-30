---
name: commerce-regulatory-risk-review
description: >
  Triage regulatory, claims, safety and compliance risk for consumer e-commerce products. Use to decide whether complexity is proportionate before deeper legal review.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.1.0"
  maturity: production
  risk: high
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Commerce Regulatory Risk Review

## Purpose
Identify whether regulatory burden or claims risk can invalidate an otherwise attractive product thesis.

## Preconditions and evidence contract
Required before a non-unresolved gate: target jurisdiction/market, product category or best available classification hypothesis, intended claims/marketing language and the evidence sources used for obligations. Distinguish product rules, claims/advertising rules and supplier/documentation obligations.

If jurisdiction, classification or authoritative evidence is missing, return UNRESOLVED and identify the specific verification required. This skill is commercial triage, not legal clearance.

## Procedure
1. Classify product and intended claims.
2. Identify safety, labelling, certification, import, consumer-protection and category-specific obligations that require verification.
3. Separate product regulation from advertising/claims risk.
4. Identify evidence or professional review required before sale.
5. Classify risk as low / medium / high / unresolved for commercial screening.

## Decision rules
- Strong demand or margins do not reduce compliance obligations.
- Health/medical-type claims can materially change risk even when the physical product appears simple.
- Do not provide a legal clearance; identify what must be verified.
- If compliance cost/uncertainty is disproportionate to the opportunity, defer or kill.

- Never infer compliance from source-market legality.
- A supplier certificate name without document scope, issuer/date and applicability is not compliance proof.
- High demand, margin or repeat purchase cannot override an unresolved launch-blocking compliance question.

## Failure / uncertainty handling
- Missing required evidence stays UNKNOWN/UNRESOLVED.
- If tool or source access is unavailable, state the limitation and the exact next evidence step; do not simulate retrieval.

## Output contract
Risk area | evidence | severity | required verification | commercial implication.
Then: regulatory gate = pass / conditional / fail / unresolved.

## Model guidance
Default: standard. Escalate to external legal/regulatory verification where required.
