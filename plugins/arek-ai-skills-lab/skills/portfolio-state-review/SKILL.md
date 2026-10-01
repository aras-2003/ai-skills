---
name: portfolio-state-review
description: 'Reconstruct and review the current investment portfolio plus historical
  snapshots, exposures and material changes. Use when assessing portfolio concentration,
  diversification, overlap, cash deployment capacity, risk changes or what changed
  since a prior snapshot. Do not use for deep underwriting of a single security.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.1.0
  maturity: candidate
  risk: high
  last_reviewed: '2026-10-02'
---

# Portfolio State Review

## Purpose
Turn holdings and history into a decision-useful portfolio state while preserving history.

## Procedure
1. Read the latest portfolio state and prior snapshot when available.
2. Reconcile position, quantity, cost basis, market value, portfolio weight, account and currency.
3. Calculate or infer only metrics supported by data; mark unavailable metrics UNKNOWN.
4. Review single-name, sector/theme, geography, currency, factor/cyclicality and ETF/stock overlap where evidence supports it.
5. Compare with the previous snapshot and identify material changes caused by trades versus price movement.
6. Flag policy breaches or review thresholds; do not automatically translate a breach into a sell action.
7. Append a new snapshot rather than overwriting historical records.

## Decision rules
- A good company can become a poor portfolio position through concentration.
- Price appreciation that increases weight is a portfolio change even without a transaction.
- Missing holdings or stale prices lower confidence.
- Current state and historical snapshots are different records.

## Output contract
Return: as-of date; reconciled portfolio summary; material exposures; changes since prior snapshot; policy exceptions; stale/missing data; positions requiring review.

## Quality checks
- [ ] As-of date is explicit.
- [ ] Trade-driven and market-driven changes are separated.
- [ ] Historical state is not overwritten.
- [ ] Portfolio concern is not presented as company-thesis failure.
