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
1. Read Portfolio_Current, latest Portfolio_History snapshot, Investment_Policy and active Thesis_Register entries.
2. Reconcile current state and create a history snapshot before updating current state.
3. Identify concentration, overlap, cash, currency, cycle/theme and policy changes.
4. Triage new company/industry/market evidence with investment-attention-triage when materiality is not already clear.
5. For positions with REVIEW/ESCALATE evidence, run thesis-monitor.
6. Revalue only positions where valuation drift can change the action.
7. Use position-sizing-review when concentration, uncertainty or thesis state changes the policy band.
8. Surface positions requiring action review; suppress ordinary news/noise.
9. Persist new snapshot, signals, thesis-monitor records and any user-confirmed decisions.

## Decision rules
- position risk can deteriorate while company thesis remains intact;
- no-trade price drift is still portfolio drift;
- do not manufacture portfolio activity to justify a review;
- policy breach triggers review, not automatic sale.

## Output contract
### Requires attention
Position | reason | thesis change | portfolio change | valuation change | review action.

### No material change
Compact list only.

### Portfolio-level observations
Concentration, cash, exposures, policy exceptions, stale data.

### Persistence receipt
Snapshot and appended records or explicit failure.

## Stop conditions
Stop when every material alert is tied to evidence or policy.
Do not expand into broad market discovery unless requested.
