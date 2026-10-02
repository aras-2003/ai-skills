---
name: position-sizing-review
description: 'Determine a decision-support position-size band from investment policy,
  thesis strength, uncertainty, valuation, downside, volatility, correlation and current
  portfolio concentration. Use after underwriting and challenge when deciding starter,
  build, hold or reduction sizing. Do not use without portfolio context and policy
  constraints.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.2.0
  maturity: production
  risk: high
  last_reviewed: '2026-10-02'
---

# Position Sizing Review

## Purpose
Separate the decision to own an asset from the decision of how much risk to allocate.

## Procedure
1. Load current portfolio state and applicable investment policy.
2. Read surviving thesis, evidence-sanity status, valuation state, priced-in expectations and key uncertainty.
3. If decision-critical evidence is UNVERIFIED/CONFLICTED, stop numeric sizing and return the exact verification requirement.
4. Review downside, volatility/liquidity, correlation and existing thematic exposure.
5. Distinguish current weight caused by a new trade from weight drift caused by price appreciation.
6. Determine whether the state supports no position, starter, building, normal/full, hold or reduction review.
7. Express a policy-consistent size band rather than false point precision.
8. State what evidence would justify increasing or decreasing the band.

## Decision rules
- High conviction does not override portfolio concentration.
- High uncertainty can justify a small starter even when expected value looks attractive.
- A position that became oversized through appreciation may require review despite intact thesis.
- Strong momentum is not permission to add.
- A surviving business thesis does not imply attractive security valuation.
- Without policy or portfolio state, return requirements instead of inventing a percentage.
- Without a verified valuation/priced-in assessment, do not recommend adding to an already-large position.

## Output contract
Lifecycle state; business-thesis state; security-attractiveness state; priced-in context; policy band; current weight; drift source; constraints; rationale; add conditions; reduce conditions; missing/blocked data.

## Quality checks
- [ ] Policy and portfolio state were used.
- [ ] Conviction and sizing are not conflated.
- [ ] Business thesis, valuation and portfolio fit are separate.
- [ ] Market-driven drift is distinguished from a new trade.
- [ ] Unverified critical evidence blocks numeric sizing.
- [ ] The output is a band or lifecycle state, not unsupported precision.
- [ ] Missing context blocks numeric sizing.
