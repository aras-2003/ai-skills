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
1. Use investment-record-store to read canonical Portfolio_Current, latest canonical Portfolio_History snapshot, Investment_Policy and active Thesis_Register entries. Emit the canonical READ receipt.
2. If Portfolio_Current or the prior canonical snapshot is unavailable, state exactly which comparison is blocked. Do not substitute local Codex files/chat summaries and do not claim historical state was preserved.
3. Reconcile current state. If a current-state mutation is required, create the canonical history snapshot first.
4. Identify concentration, overlap, cash, currency, cycle/theme and policy changes.
5. Separate trade-driven changes from market-driven drift. No-trade appreciation must remain explicitly market-driven.
6. Triage new company/industry/market evidence with investment-attention-triage when materiality is not already clear.
7. For positions with REVIEW/ESCALATE evidence, run thesis-monitor.
8. Revalue only positions where valuation drift can change the action.
9. Use position-sizing-review when concentration, uncertainty or thesis state changes the policy band.
10. Surface positions requiring action review; suppress ordinary news/noise.
11. Persist new canonical snapshot, signals, thesis-monitor records and any user-confirmed decisions.
12. Emit canonical WRITE persistence receipt. Local history files are NONCANONICAL only.

## Decision rules
- position risk can deteriorate while company thesis remains intact;
- no-trade price drift is still portfolio drift;
- do not manufacture portfolio activity to justify a review;
- policy breach triggers review, not automatic sale;
- without a prior canonical snapshot, do not claim a complete "since last snapshot" comparison.

## Output contract
### Requires attention
Position | reason | thesis change | portfolio change | drift source | valuation change | review action.

### No material change
Compact list only.

### Portfolio-level observations
Concentration, cash, exposures, policy exceptions, stale/missing data.

### Persistence receipts
Canonical READ and WRITE receipts with SUCCESS / UNAVAILABLE / FAILED, target and as-of context. Local artifacts do not count as canonical history.

## Stop conditions
Stop when every material alert is tied to evidence or policy.
Do not expand into broad market discovery unless requested.
