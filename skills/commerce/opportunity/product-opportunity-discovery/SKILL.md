---
name: product-opportunity-discovery
description: >
  Discover product opportunity hypotheses from customer problems, category signals and market gaps. Use for broad e-commerce idea generation before deep validation; do not treat trend popularity as proof of business viability.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.1.0"
  maturity: production
  risk: low
  last_reviewed: 2026-09-30
  execution:
    default_model_class: fast
---

# Product Opportunity Discovery

## Purpose
Generate a small set of evidence-linked product hypotheses worth validating.

## Preconditions and evidence contract
Required: target market, commercial constraints that materially shape the search and a set of customer/category signals or a clearly defined discovery question. Treat trend, social, review and source-market traction as signals, not purchase evidence.

Discovery produces hypotheses and a shortlist, not a final business verdict. When source freshness or tool access is missing, label current market facts unresolved instead of reconstructing them from memory.

## Procedure
1. Start from customer problems or category signals, not products alone.
2. Capture target customer, problem, current workaround, candidate product, why-now signal and likely channel.
3. Distinguish demand signal, trend signal and purchase evidence.
4. Prefer opportunities with visible problems, simple explanation, testable offers and operationally manageable products.
5. Apply fast kill screens: weak problem, impossible economics, obvious regulatory burden, poor logistics or pure commodity with no plausible differentiation.
6. Return only the strongest 3–5 hypotheses for deeper review.

## Decision rules
- Popular product != good business.
- Search/social attention != purchase intent.
- US traction != PL transferability.
- Do not invent sales volume from reviews, followers or ad visibility.
- Discovery should reduce the search space, not produce a ranked business case.
- Do not invent sample sizes, response thresholds or test budgets without an explicit evidence basis; describe the validation method and stopping logic instead.
- Interview or survey intent is qualitative evidence, not purchase evidence. Treat actual deposits, reservations, purchases or other costly commitment as stronger evidence.

- Do not move directly to inventory commitment or paid acquisition while a cheaper falsifying experiment can invalidate the hypothesis.
- Do not invent sample sizes, thresholds, TAM, CAC or sales volumes without an explicit evidence basis.

## Failure / uncertainty handling
- Missing required evidence stays UNKNOWN/UNRESOLVED.
- If tool or source access is unavailable, state the limitation and the exact next evidence step; do not simulate retrieval.

## Output contract
Problem | target customer | candidate product | why now | evidence signal | key unknown | next validation step.

## Model guidance
Default: fast. Validated on Luna for broad mixed-signal discovery and shortlist reduction. Escalate only when interpreting conflicting category signals materially changes the shortlist.
