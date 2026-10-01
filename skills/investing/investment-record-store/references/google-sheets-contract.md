# Investment OS Google Sheets contract

Canonical workbook: **Investment OS** in the user's Google Drive finance area.

## Tabs

### Portfolio_Current
One row per current position.
Required logical fields: position_id, as_of_date, account, instrument_id, ticker, name, asset_type, currency, quantity, cost_basis, market_price, market_value, portfolio_weight, source_ref, updated_at.

### Transactions
Append-only.
transaction_id, trade_date, account, instrument_id, action, quantity, price, currency, fees, source_ref, recorded_at.

### Portfolio_History
Append-only snapshots.
snapshot_id, as_of_date, position_id, instrument_id, quantity, market_price, market_value, portfolio_weight, snapshot_reason, recorded_at.

### Watchlist
Current workflow state may be updated; removals should retain last status/date.
instrument_id, status, added_at, last_reviewed_at, setup, next_trigger, thesis_ref.

### Opportunities
Append research candidates and disposition changes.
opportunity_id, as_of_date, instrument_id, setup, changed_signal, valuation_context, main_risk, xtb_status, next_step, status.

### Research_Log
Append-only research events.
research_id, as_of_date, instrument_id, research_type, summary, confidence, thesis_ref, source_refs, recorded_at.

### Signals_History
Append-only time series.
signal_id, as_of_date, instrument_id, signal_type, value_or_state, interpretation, source_ref, source_date, confidence.

### Thesis_Register
Versioned, never hindsight-rewritten.
thesis_id, version, effective_date, instrument_id, horizon, thesis, assumptions, catalysts, risks, kill_criteria, state, evidence_refs, supersedes.

### Decision_Journal
Append-only.
decision_id, decision_time, instrument_id, lifecycle_action, price_context, position_weight, horizon, thesis_id, rationale, sizing_rationale, confidence, invalidation, evidence_refs.
Ex-post reviews are new linked rows/records, not edits to original rationale.

### Investment_Policy
Versioned.
policy_id, version, effective_date, objectives, constraints, bucket_rules, sizing_rules, concentration_rules, cash_rules, review_rules, rationale, supersedes.

### Market_Themes
Versioned observations.
theme_id, as_of_date, theme, mechanism, indicators, beneficiaries, losers, invalidation, evidence_refs.

### Sources
Evidence registry.
source_ref, source_type, title, publisher, url_or_drive_ref, published_date, accessed_at, primary_or_secondary, notes.

## Integrity rules
1. Historical tables are append-only.
2. Every material external claim links to Sources.
3. as_of_date describes the market/portfolio state; source_date describes evidence timing.
4. Stale data is not silently promoted to current.
5. Record IDs are stable across workflows.
6. Personal data remains in Drive, never the Git repository.
7. A failed persistence operation must be visible to the caller.
