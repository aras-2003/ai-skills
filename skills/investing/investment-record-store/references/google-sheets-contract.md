# Legacy Investment OS Google Sheets contract

This document describes the legacy 12-tab Investment OS workbook used before Supabase cutover.

## Status
- Before cutover: may remain canonical only under explicit `legacy_sheets` mode.
- During migration: source for reconciliation/import.
- After cutover: read-only archive/migration source; no new canonical writes.

## Legacy tabs
Portfolio_Current, Transactions, Portfolio_History, Watchlist, Opportunities, Research_Log, Signals_History, Thesis_Register, Decision_Journal, Investment_Policy, Market_Themes, Sources.

## Migration rule
Do not map tabs 1:1 into tables merely to preserve spreadsheet shape. Normalize into the relational contract in `supabase-contract.md`.

## Integrity rules
1. Preserve stable IDs where possible.
2. Preserve chronology and append-only history.
3. Preserve source references.
4. Reconcile latest portfolio state and transaction totals before cutover.
5. Record an explicit cutover; never allow dual canonical writes.
