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


## Preconditions
Require target jurisdiction, product type/formulation where relevant, intended claims and sales/import route. Missing classification inputs make the gate unresolved.

## Inputs and evidence
Identify the source and jurisdiction of material obligations. Separate product classification, safety/labelling/import duties and advertising/claims requirements.

## Uncertainty and tool failure
If authoritative regulatory sources or qualified review are unavailable, return an unresolved gate and the verification needed. Never present commercial screening as legal clearance.

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

## Output contract
Risk area | evidence | severity | required verification | commercial implication.
Then: regulatory gate = pass / conditional / fail / unresolved.

## Model guidance
Default: standard. Escalate to external legal/regulatory verification where required.
