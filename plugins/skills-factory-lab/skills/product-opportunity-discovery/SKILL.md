---
name: product-opportunity-discovery
description: 'Discover product opportunity hypotheses from customer problems, category
  signals and market gaps. Use for broad e-commerce idea generation before deep validation;
  do not use when a concrete product already needs an end-to-end business decision.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 1.1.0
  maturity: production
  risk: low
  last_reviewed: '2026-09-30'
---

# Product Opportunity Discovery

## Purpose
Generate a small set of evidence-linked product hypotheses worth validating, without turning weak signals into a business verdict.

## Preconditions
Require a target market and discovery constraints, or mark them unresolved. If the user already has a concrete product, price/cost/supply thesis and wants test/defer/kill, route to the product deep dive.

## Inputs and evidence
Use customer problems, current workarounds, trend/category signals, purchase evidence, operational constraints and channel hypotheses. Keep trend, engagement, stated intent and purchase evidence distinct.

## Uncertainty and tool failure
If live market tools are unavailable, stay within supplied evidence and mark freshness/current demand unknown. Do not fabricate TAM, sales, CAC, prices, sample sizes or participant counts.

## Procedure
1. Start from customer problems or category signals, not products alone.
2. Capture target customer, problem, workaround, candidate product, why-now signal and likely channel.
3. Distinguish demand signal, trend signal and purchase evidence.
4. Prefer opportunities with visible problems, simple explanation, testable offers and manageable operations.
5. Apply fast kill/defer screens: weak problem, impossible economics, disproportionate regulation/logistics or pure commodity with no plausible differentiation.
6. Return only the strongest 3–5 hypotheses for deeper validation; keep fewer if the evidence does not support 3.

## Decision rules
- Popular product != good business.
- Search/social attention != purchase intent.
- US traction != PL transferability.
- Discovery reduces the search space; it does not produce a final business verdict.
- Do not invent sample sizes, response thresholds or test budgets without an evidence basis.
- Interview/survey intent is qualitative evidence, not purchase evidence. Deposits, reservations, purchases or other costly commitments are stronger.

## Output contract
Problem | target customer | candidate product | why now | evidence signal | purchase evidence | key unknown | cheapest next validation.
Also state deliberate rejects/defers and why. No numerical ranking.

## Quality checks
- [ ] Shortlist is 3–5 maximum, not quota-filled.
- [ ] Signals and purchase evidence are separated.
- [ ] Regulatory/logistics/commodity risks can remove ideas early.
- [ ] Next validation is cheapest decision-changing evidence, not paid ads by default.

## Lab runtime eval inputs

When the user explicitly asks to run one of the exact lab eval cases below, load only the corresponding input file from `references/evals/`. The evaluator rubric is intentionally unavailable to the executor.

- `references/evals/case-006-product-discovery.input.md`
