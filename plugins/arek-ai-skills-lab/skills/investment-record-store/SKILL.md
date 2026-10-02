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
  version: 0.2.0
  maturity: production
  risk: high
  last_reviewed: '2026-10-02'
---

# Investment Record Store

## Purpose
Provide one durable, auditable data contract for Investment OS using Google Drive / Google Sheets.

## Canonical-store rule
The configured Investment OS Google Sheet is the only canonical store. Chat history, local Codex files, generated markdown, JSON sidecars and temporary workspace files are never canonical portfolio/history state.

A local artifact may be created for convenience, but it must be labeled `NONCANONICAL` and can never satisfy a persistence requirement.

## Procedure
1. Locate the user's canonical Investment OS spreadsheet in the configured Finance & Investments Drive area.
2. Return an explicit READ receipt for every state lookup. If the file, connector or required tab is unavailable, return `UNAVAILABLE` or `FAILED`; do not silently substitute chat/local files.
3. Read only the tabs/ranges required by the active workflow.
4. Require as_of_date for state records and source_date plus source reference for externally derived facts.
5. Treat Portfolio_Current as mutable current state; create Portfolio_History snapshots before material current-state changes.
6. Append Transactions, Research_Log, Signals_History, Thesis_Register history, Decision_Journal and Sources. Never rewrite historical rationale to match later outcomes.
7. Investment_Policy may be revised, but preserve version/effective-date history.
8. Use stable record IDs so later workflows can link thesis, evidence, decision and outcome.
9. After every write attempt, return an explicit WRITE receipt. If canonical persistence did not succeed, say so plainly and do not say the record was saved/preserved.

## Decision rules
- Chat history is not the system of record.
- Current-state correction and historical rewrite are different operations.
- Unknown source date means the claim cannot be treated as current.
- Duplicate evidence should link to one source record rather than create conflicting copies.
- Repository files contain schemas/instructions only, never the user's live holdings.
- A local file path is evidence of artifact creation, not evidence of canonical persistence.

## Output contract
For every read/write operation return a Persistence receipt with:
- status: SUCCESS / UNAVAILABLE / FAILED
- operation: READ / APPEND / SNAPSHOT / UPDATE_CURRENT / POLICY_VERSION
- canonical_target: spreadsheet + tab/range when known
- as_of_or_effective_date
- record_ids or rows affected when successful
- source references / provenance when applicable
- integrity warnings
- failure_reason when not successful
- fallback_artifact, if any, explicitly labeled NONCANONICAL

## Quality checks
- [ ] Canonical Drive file was identified or unavailability was surfaced.
- [ ] READ and WRITE outcomes are explicit.
- [ ] Append-only tables were not overwritten.
- [ ] Current-state mutation created required history first.
- [ ] Source provenance is retained.
- [ ] No personal portfolio data is written to Git.
- [ ] Local artifacts are never presented as durable canonical state.
- [ ] Failure to persist is surfaced explicitly.

## References
- references/google-sheets-contract.md
