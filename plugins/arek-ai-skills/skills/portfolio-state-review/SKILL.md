---
name: portfolio-state-review
description: 'Reconstruct and review the current investment portfolio plus historical
  snapshots, exposures and material changes. Use when assessing portfolio concentration,
  diversification, overlap, cash deployment capacity, risk changes or what changed
  since a prior snapshot. Do not use for deep underwriting of a single security.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.2.0
  maturity: production
  risk: high
  last_reviewed: '2026-10-02'
---

# Portfolio State Review

## Purpose
Turn holdings and canonical history into a decision-useful portfolio state while preserving history.

## Procedure
1. Use investment-record-store to read canonical Portfolio_Current and the latest canonical Portfolio_History snapshot. Do not use local Codex files or chat summaries as substitutes.
2. If the prior canonical snapshot is unavailable, state that the comparison cannot be completed and identify exactly which history is missing.
3. Reconcile position, quantity, cost basis, market value, portfolio weight, account and currency.
4. Calculate or infer only metrics supported by data; mark unavailable metrics UNKNOWN.
5. Review single-name, sector/theme, geography, currency, factor/cyclicality and ETF/stock overlap where evidence supports it.
6. Compare with the previous snapshot and identify material changes caused by trades versus price movement.
7. Flag policy breaches or review thresholds; do not automatically translate a breach into a sell action.
8. Append a new canonical snapshot rather than overwriting historical records.
9. Return explicit read/write persistence receipts.

## Decision rules
- A good company can become a poor portfolio position through concentration.
- Price appreciation that increases weight is a portfolio change even without a transaction.
- Missing holdings or stale prices lower confidence.
- Current state and historical snapshots are different records.
- No prior canonical snapshot means no claim of "change since prior snapshot."
- A local history.json file is NONCANONICAL and cannot satisfy history preservation.

## Output contract
Return: as-of date; canonical-read status; reconciled portfolio summary; material exposures; changes since prior snapshot or explicit comparison block; policy exceptions; stale/missing data; positions requiring review; canonical persistence receipt.

## Quality checks
- [ ] As-of date is explicit.
- [ ] Canonical current state and prior snapshot were attempted.
- [ ] Missing canonical history is surfaced, not replaced with local artifacts.
- [ ] Trade-driven and market-driven changes are separated.
- [ ] Historical state is not overwritten.
- [ ] Portfolio concern is not presented as company-thesis failure.
- [ ] Persistence receipt states whether snapshot/history write actually succeeded.
