---
name: portfolio-prioritization
description: >
  Structure transparent prioritisation of initiatives using agreed strategic, value, risk, capacity and dependency criteria. Use when a portfolio needs comparable decisions; use deterministic calculation for scoring where possible.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: fast
---

# Portfolio Prioritization

## Purpose
Turn competing initiatives into a transparent decision set.

## Procedure
1. Confirm decision objective and hard constraints.
2. Define a small set of non-overlapping criteria and weights.
3. Separate factual inputs from judgment scores.
4. Normalize scoring scales.
5. Use deterministic calculation for weighted totals when available.
6. Surface dependencies, mandatory work and capacity constraints outside the score.
7. Produce options and sensitivity, not a false single truth.

## Decision rules
- Mandatory/regulatory work should not be hidden inside normal value scoring.
- Dependencies and capacity can override rank order.
- LLM interprets; code calculates.

## Output contract
Initiative | criteria scores | weighted score | confidence | dependencies | mandatory? | capacity impact | decision note.
Then: recommended portfolio options and sensitivity.

## Model guidance
Default: **fast** plus deterministic calculation. Escalate for ambiguous strategic value or highly coupled portfolios.

## Quality checks
- [ ] Criteria non-overlapping.
- [ ] Calculation deterministic.
- [ ] Dependencies/capacity explicit.

