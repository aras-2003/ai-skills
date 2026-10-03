# Investment OS Supabase contract

## Role
Supabase/Postgres is the target canonical relational datastore for normalized Investment OS state and history.

The canonical Supabase schema is not discovered heuristically. Resolve it from the fixed bootstrap authority `public.system_config` according to `canonical-schema-governance.md`. The current deployment resolves to schema `public`; duplicate schemas are noncanonical unless an explicit future cutover changes the bootstrap record.

Google Drive remains the raw-document store for broker exports, statements, PDFs and other source files.

## Core tables

### accounts
account_id PK, provider, account_type, currency, tax_wrapper, active, metadata, created_at.

### instruments
instrument_id PK, ticker, isin, name, asset_type, exchange, currency, xtb_symbol, xtb_status, metadata, created_at, updated_at.

### transactions
Append-only.
transaction_id PK, account_id FK, instrument_id FK, trade_date, action, quantity, price, currency, fees, source_id FK, imported_at.

### portfolio_snapshots
Append-only snapshot header.
snapshot_id PK, as_of_date, snapshot_reason, source_id FK, created_at.

### position_snapshots
Append-only snapshot lines.
snapshot_id FK, account_id FK, instrument_id FK, quantity, cost_basis, market_price, market_value, portfolio_weight, currency.

### watchlist
watchlist_id PK, instrument_id FK, status, setup, next_trigger, thesis_id FK nullable, added_at, last_reviewed_at, updated_at.

### opportunities
Append-only/disposition history.
opportunity_id PK, as_of_date, instrument_id FK, setup, fundamental_change, valuation_change, market_trend_change, materiality, main_risk, xtb_status, next_step, status, created_at.

### research_events
Append-only.
research_id PK, as_of_date, instrument_id FK nullable, theme_id FK nullable, research_type, summary, confidence, thesis_id FK nullable, created_at.

### signals
Append-only.
signal_id PK, as_of_date, instrument_id FK nullable, theme_id FK nullable, signal_type, value_or_state, interpretation, source_id FK, source_date, confidence, created_at.

### theses
Stable identity.
thesis_id PK, instrument_id FK, horizon, created_at.

### thesis_versions
Append-only/versioned.
thesis_version_id PK, thesis_id FK, version, effective_date, thesis, assumptions jsonb, catalysts jsonb, risks jsonb, kill_criteria jsonb, state, supersedes FK nullable, created_at.

Allowed lifecycle states:
- `DRAFT`: working thesis candidate awaiting owner/review acceptance;
- `ACTIVE`: approved/current thesis eligible for monitoring and downstream thesis-state claims;
- `RETIRED`: no longer active.

Lifecycle transitions are represented by appending a new version. Do not rewrite historical versions merely to change state.

### decisions
Append-only.
decision_id PK, decision_time, instrument_id FK, lifecycle_action, price_context, position_weight, horizon, thesis_version_id FK nullable, rationale, sizing_rationale, confidence, invalidation, created_at.

### decision_outcomes
Append-only ex-post review.
outcome_id PK, decision_id FK, review_date, thesis_quality, timing_quality, sizing_quality, process_adherence, outcome_summary, lessons, created_at.

### investment_policies
Stable identity/version header.
policy_id PK, created_at.

### investment_policy_versions
Versioned.
policy_version_id PK, policy_id FK, version, effective_date, objectives jsonb, constraints jsonb, bucket_rules jsonb, sizing_rules jsonb, concentration_rules jsonb, cash_rules jsonb, review_rules jsonb, rationale, supersedes FK nullable, created_at.

### market_themes
Stable identity.
theme_id PK, name, created_at.

### market_theme_versions
Append-only.
theme_version_id PK, theme_id FK, as_of_date, mechanism, indicators jsonb, beneficiaries jsonb, losers jsonb, invalidation jsonb, created_at.

### sources
Evidence registry.
source_id PK, source_type, title, publisher, url_or_drive_ref, published_date, accessed_at, primary_or_secondary, content_hash nullable, notes.

### evidence_links
Many-to-many provenance links.
evidence_link_id PK, source_id FK, entity_type, entity_id, claim_key nullable, created_at.

### instrument_exposures
Normalized look-through metadata.
exposure_id PK, instrument_id FK, as_of_date, exposure_type, exposure_key, exposure_value, source_id FK nullable.

Canonical identity for refresh/idempotency is:
`instrument_id + as_of_date + exposure_type + exposure_key + coalesced(source_id)`.

The same source snapshot must not create duplicate rows for that identity. Newer issuer snapshots use a new `as_of_date` and remain historically queryable.

## Derived views

### current_positions
Latest valid position state per account/instrument from transactions and/or latest reconciled snapshot.

### latest_portfolio_snapshot
Latest complete snapshot header and lines.

### current_theses
Latest thesis version per thesis/instrument only when the latest version state is `ACTIVE`. DRAFT and RETIRED latest versions are excluded.

### draft_theses
Latest thesis version per thesis/instrument only when the latest version state is `DRAFT`. This view is for review/approval workflows and must not be used by thesis-monitor as the active investment thesis.

### current_policy
Latest effective investment policy version.

### current_watchlist
Current watchlist state.

### portfolio_exposures
Aggregated single-name, sector, geography, currency, theme and ETF look-through exposure.

### decision_performance
Decision records joined to later outcome reviews and performance windows when market data exists.

## Integrity rules
1. Historical/event tables are append-only.
2. No historical thesis or decision rationale is rewritten with hindsight.
3. Every material external claim should link to a source through evidence_links.
4. `as_of_date` describes market/portfolio state; `source_date` describes evidence timing.
5. Stable IDs link instrument -> thesis -> evidence -> decision -> outcome.
6. Current views are derived where possible; duplicate mutable state is avoided.
7. Analytics tools may query views/tables but must not silently mutate canonical state.
8. Raw Drive files may be referenced in sources but normalized records live in Supabase after cutover.
9. A failed write must be visible to the caller.
10. Migration from Sheets is complete only after reconciliation counts and an explicit cutover record; never allow dual canonical writes.
11. Never infer canonical schema from populated tables, row counts or duplicate table names.
12. Never silently fall back between Supabase schemas; a noncanonical schema may be inspected only for migration/security diagnostics.
13. Bootstrap metadata lives in `public.system_config`; conflicting metadata elsewhere is noncanonical and cannot override it.
14. `instrument_exposures` refreshes are idempotent for the canonical exposure identity; historical dates remain append-preserved rather than overwritten.
15. Thesis lifecycle is state-aware: only latest ACTIVE versions appear in `current_theses`; DRAFT versions remain separately reviewable and RETIRED theses are not monitored as current.

## Migration/cutover minimum checks
- all 12 legacy logical areas mapped to relational entities;
- row counts and key totals reconciled;
- latest portfolio state matches legacy source;
- thesis/policy versions preserve chronology;
- source links are retained;
- no duplicate transaction IDs;
- canonical backend flag/cutover record is explicit;
- Sheets becomes read-only archive after cutover.
