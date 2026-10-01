---
name: investment-record-store
description: 'Read and persist canonical Investment OS records in the user''s Google
  Drive spreadsheet, including current portfolio, snapshots, transactions, research,
  signals, theses, decisions, policy, themes and sources. Use whenever an investing
  workflow needs durable state or history. Do not store personal portfolio values
  or secrets in the skill repository.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.1.0
  maturity: candidate
  risk: high
  last_reviewed: '2026-10-02'
---

# Investment Record Store

## Purpose
Provide one durable, auditable data contract for Investment OS using Google Drive / Google Sheets.

## Procedure
1. Locate the user's canonical Investment OS spreadsheet in the configured Finance & Investments Drive area.
2. Read only the tabs/ranges required by the active workflow.
3. Require as_of_date for state records and source_date plus source reference for externally derived facts.
4. Treat Portfolio_Current as mutable current state; create Portfolio_History snapshots before material current-state changes.
5. Append Transactions, Research_Log, Signals_History, Thesis_Register history, Decision_Journal and Sources. Never rewrite historical rationale to match later outcomes.
6. Investment_Policy may be revised, but preserve version/effective-date history.
7. Use stable record IDs so later workflows can link thesis, evidence, decision and outcome.
8. When the Drive file or required tab is unavailable, return a storage precondition failure rather than silently keeping canonical state only in chat.

## Decision rules
- Chat history is not the system of record.
- Current-state correction and historical rewrite are different operations.
- Unknown source date means the claim cannot be treated as current.
- Duplicate evidence should link to one source record rather than create conflicting copies.
- Repository files contain schemas/instructions only, never the user's live holdings.

## Output contract
Operation: READ / APPEND / SNAPSHOT / UPDATE_CURRENT / POLICY_VERSION.
Return affected record IDs, tab, as-of/effective date, source references and any integrity warning.

## Quality checks
- [ ] Canonical Drive file was identified.
- [ ] Append-only tables were not overwritten.
- [ ] Current-state mutation created required history first.
- [ ] Source provenance is retained.
- [ ] No personal portfolio data is written to Git.
- [ ] Failure to persist is surfaced explicitly.

## References
- references/google-sheets-contract.md
