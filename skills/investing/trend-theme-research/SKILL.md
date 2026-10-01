---
name: trend-theme-research
description: >
  Research an investment trend or market theme by mapping its economic value chain, demand drivers, bottlenecks,
  second-order beneficiaries and failure modes. Use when exploring themes such as AI infrastructure, power, memory,
  automation or other structural/cyclical trends. Do not use for one-company underwriting alone.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-10-02
  execution:
    default_model_class: standard
---

# Trend Theme Research

## Purpose
Turn a narrative into a falsifiable economic map and a research universe.

## Procedure
1. Define the theme, time horizon and claimed mechanism.
2. Map demand source -> bottlenecks -> suppliers -> enabling infrastructure -> second-order effects.
3. Identify measurable leading and lagging indicators.
4. Separate secular, cyclical and narrative components.
5. Identify where economics may accrue versus where headlines concentrate.
6. Map candidate beneficiaries and losers, then intersect with XTB availability.
7. Record what would weaken or invalidate the theme.

## Decision rules
- Theme popularity is not an investment thesis.
- Revenue exposure matters more than label association.
- Capacity expansion can destroy economics even when end demand grows.
- Second-order beneficiaries require evidence of economic capture, not storytelling.

## Output contract
Theme mechanism; value-chain map; indicators; beneficiaries/losers; crowded assumptions; invalidation conditions; XTB research queue.

## Quality checks
- [ ] Mechanism is explicit.
- [ ] Secular and cyclical components are separated.
- [ ] At least one disconfirming path is included.
- [ ] Candidate companies are not treated as validated investments.
