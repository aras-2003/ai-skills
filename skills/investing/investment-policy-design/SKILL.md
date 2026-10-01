---
name: investment-policy-design
description: >
  Design or revise a personal investment policy from the investor's goals, liquidity, risk capacity, horizon,
  account structure and demonstrated behavior. Use when defining portfolio buckets, risk budget, concentration
  limits, sizing rules, review cadence or decision principles. Do not use for evaluating one security or reacting to one market move.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: high
  last_reviewed: 2026-10-02
  execution:
    default_model_class: standard
---

# Investment Policy Design

## Purpose
Create an explicit policy that governs later research and portfolio decisions without pretending that one famous investor's style is universally optimal.

## Procedure
1. Establish goals, horizon, liquidity needs, drawdown tolerance, tax/account constraints and investable universe.
2. Separate risk capacity from stated risk preference.
3. Review current portfolio behavior for concentration, turnover, chasing, averaging down and premature exits when history exists.
4. Compare relevant investor archetypes and institutional practices only as reference patterns; extract principles, not copied holdings.
5. Define portfolio buckets, position-size bands, concentration review thresholds, cash policy, rebalancing/review cadence and thesis invalidation discipline.
6. Mark every numeric limit as USER-SET, EVIDENCE-BASED, PROVISIONAL or UNKNOWN.
7. Record assumptions and the evidence that could justify changing the policy.

## Decision rules
- Policy precedes security-level sizing.
- Do not infer risk tolerance from one profitable or losing trade.
- Do not copy celebrity-investor concentration without matching horizon, liquidity and edge.
- A limit without rationale is provisional.
- Preserve optionality: policy may allow both 6-18 month and 2-5 year theses if they are labeled and governed separately.

## Output contract
Return: objectives; constraints; portfolio buckets; sizing bands; concentration rules; cash/rebalancing rules; thesis review rules; decision principles; unresolved choices; change triggers.

## Quality checks
- [ ] Risk capacity and risk appetite are separated.
- [ ] Numeric limits have provenance.
- [ ] Shorter and longer horizon theses have explicit handling.
- [ ] No security recommendation is smuggled into policy design.
- [ ] Policy changes identify what evidence changed.
