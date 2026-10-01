---
name: position-sizing-review
description: >
  Determine a decision-support position-size band from investment policy, thesis strength, uncertainty, valuation,
  downside, volatility, correlation and current portfolio concentration. Use after underwriting and challenge when
  deciding starter, build, hold or reduction sizing. Do not use without portfolio context and policy constraints.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: production
  risk: high
  last_reviewed: 2026-10-02
  execution:
    default_model_class: strong
---

# Position Sizing Review

## Purpose
Separate the decision to own an asset from the decision of how much risk to allocate.

## Procedure
1. Load current portfolio state and applicable investment policy.
2. Read surviving thesis, valuation state and key uncertainty.
3. Review downside, volatility/liquidity, correlation and existing thematic exposure.
4. Determine whether the state supports no position, starter, building, normal/full, hold or reduction review.
5. Express a policy-consistent size band rather than false point precision.
6. State what evidence would justify increasing or decreasing the band.

## Decision rules
- High conviction does not override portfolio concentration.
- High uncertainty can justify a small starter even when expected value looks attractive.
- A position that became oversized through appreciation may require review despite intact thesis.
- Without policy or portfolio state, return requirements instead of inventing a percentage.

## Output contract
Lifecycle state; policy band; current weight; constraints; rationale; add conditions; reduce conditions; missing data.

## Quality checks
- [ ] Policy and portfolio state were used.
- [ ] Conviction and sizing are not conflated.
- [ ] The output is a band or lifecycle state, not unsupported precision.
- [ ] Missing context blocks numeric sizing.
