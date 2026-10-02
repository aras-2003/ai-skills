---
name: investment-record-store
description: 'Read and persist canonical Investment OS records in Supabase/Postgres,
  including portfolio state, transactions, research, signals, theses, decisions, policy,
  themes and sources. Use whenever an investing workflow needs durable state or history.
  Google Drive is raw-document/legacy migration storage, not the canonical relational
  store after cutover.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.3.0
  maturity: production
  risk: high
  last_reviewed: '2026-10-02'
---

# Investment Record Store

## Purpose
Provide one durable, auditable persistence contract for Investment OS, with Supabase/Postgres as the target canonical store.

## Canonical-store rule
Exactly one canonical store may be active at a time.

Target state:
- **Supabase/Postgres** = canonical relational state and history.
- **Google Drive** = raw documents, broker exports, PDFs, statements and migration/archive material.
- Chat history, local Codex files, markdown, JSON sidecars, temporary workspace files and analytics outputs are never canonical.

During migration, the legacy Investment OS Google Sheet may remain the active canonical store only until an explicit cutover record is made. Once cutover occurs, Sheets becomes read-only migration/archive input and must never receive new canonical writes.

A local artifact may be created for convenience, but it must be labeled `NONCANONICAL`.

## Procedure
1. Determine the configured canonical backend and emit it in the READ receipt.
2. If Supabase is the configured canonical backend:
   - identify the configured Investment OS project;
   - read only required tables/views;
   - use relational keys and stable record IDs;
   - treat append-only/event tables as immutable history;
   - derive current-state views from source records where practical.
3. If migration has not cut over yet, legacy Sheets may be read/written only under explicit `legacy_sheets` mode.
4. Never silently fall back from Supabase to Sheets. If the configured backend is unavailable, return `UNAVAILABLE` or `FAILED`.
5. Require `as_of_date` for state records and `source_date` plus source reference for externally derived facts.
6. Persist transactions, research events, signals, thesis versions, decisions, outcomes and sources append-only.
7. Preserve policy versions with effective dates.
8. Prefer views for current positions/current thesis/current policy rather than duplicating mutable current-state tables when the relational model can derive them safely.
9. After every write attempt, return an explicit WRITE receipt. Never claim saved/preserved if canonical persistence failed.

## Decision rules
- Supabase is a datastore, not an evidence source.
- Data/BI outputs are derived analytics, not canonical state.
- Google Drive remains authoritative for raw uploaded documents only, not normalized investment records after cutover.
- Current-state correction and historical rewrite are different operations.
- Duplicate evidence should link to one source record.
- Repository files contain schemas/instructions only, never live holdings or credentials.
- No hidden fallback between canonical backends.

## Output contract
For every read/write operation return a Persistence receipt with:
- status: SUCCESS / UNAVAILABLE / FAILED
- operation: READ / APPEND / SNAPSHOT / UPDATE_CURRENT / POLICY_VERSION / MIGRATE
- backend: SUPABASE / LEGACY_SHEETS
- canonical_target: project + schema/table/view or workbook + tab/range
- as_of_or_effective_date
- record_ids or rows affected when successful
- source references / provenance when applicable
- integrity warnings
- failure_reason when not successful
- fallback_artifact, if any, explicitly labeled NONCANONICAL

## Quality checks
- [ ] Exactly one canonical backend is active.
- [ ] No silent Supabase->Sheets fallback occurred.
- [ ] READ and WRITE outcomes are explicit.
- [ ] Append-only history was not overwritten.
- [ ] Source provenance is retained.
- [ ] Analytics outputs are not presented as canonical records.
- [ ] No personal portfolio data or credentials are written to Git.
- [ ] Persistence failure is surfaced explicitly.

## References
- references/supabase-contract.md
- references/google-sheets-contract.md
