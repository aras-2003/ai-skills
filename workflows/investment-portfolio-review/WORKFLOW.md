# Investment Portfolio Review Workflow

## Purpose
Review the current XTB portfolio as a system, detect material drift or thesis deterioration and surface only positions that require attention.

## Required skills
- portfolio-state-review
- thesis-monitor
- investment-record-store

## Optional skills
- investment-attention-triage
- position-sizing-review
- valuation-scenario-review
- thesis-challenge
- decision-journal-update

## Sequence
1. Read canonical current_positions, latest portfolio snapshot, current policy and active thesis versions through investment-record-store. Emit canonical READ receipt.
2. If current state or prior snapshot is unavailable, state exactly which comparison is blocked. Do not substitute local/chat/analytics cache.
3. Reconcile current state and preserve append-only snapshot history.
4. Use Data/analytics tooling for concentration, ETF look-through, overlap, currency, theme/cycle and historical trend calculations when useful. Treat results as derived analytics.
5. Separate trade-driven changes from market-driven drift.
6. Triage new company/industry/market evidence with investment-attention-triage.
7. For REVIEW/ESCALATE positions, run thesis-monitor.
8. Revalue only positions where valuation drift can change the action.
9. Use position-sizing-review when concentration, uncertainty or thesis state changes the policy band.
10. Surface only positions requiring action review.
11. Persist new snapshot, signals, thesis-monitor records and user-confirmed decisions through investment-record-store only.
12. Emit canonical WRITE receipt.

## Decision rules
- analytics layer reads/derives; it does not become the system of record;
- position risk can deteriorate while company thesis remains intact;
- no-trade price drift is still portfolio drift;
- policy breach triggers review, not automatic sale;
- without prior canonical snapshot, do not claim a complete change comparison.

## Output contract
Requires attention; no material change; portfolio-level observations; derived analytics/provenance; canonical READ/WRITE receipts.

## Stop conditions
Stop when every material alert is tied to evidence or policy.
