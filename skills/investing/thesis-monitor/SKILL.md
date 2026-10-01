---
name: thesis-monitor
description: >
  Monitor an existing investment thesis against new earnings, guidance, industry data, price/valuation changes and
  predefined kill criteria. Use for ongoing holding reviews and event-driven updates. Do not restart full underwriting
  unless the thesis materially changes or evidence becomes stale.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: high
  last_reviewed: 2026-10-02
  execution:
    default_model_class: standard
---

# Thesis Monitor

## Purpose
Evaluate what changed versus the recorded thesis rather than summarizing news from scratch.

## Procedure
1. Load the latest thesis register entry and prior monitoring state.
2. Ingest new dated evidence relevant to assumptions, KPIs, catalysts and kill criteria.
3. Classify each change as strengthens, weakens, neutral/noise or invalidates.
4. Update valuation context separately from business-thesis state.
5. Detect portfolio implications such as position drift but route sizing decisions to position-sizing-review.
6. Append a monitoring record; never rewrite the historical thesis as though it had always contained new information.
7. Escalate to fresh underwriting when business model, cycle regime or thesis basis materially changes.

## Decision rules
- News importance is measured against thesis, not headline size.
- Price change alone does not prove thesis change.
- Kill criteria override narrative attachment when actually met.
- Historical thesis text is immutable; corrections are new records.

## Output contract
As-of date; prior thesis state; new evidence; assumption-by-assumption change; valuation change; thesis state; triggered kill criteria; next review trigger.

## Quality checks
- [ ] Comparison baseline is explicit.
- [ ] New evidence is dated.
- [ ] Historical records are preserved.
- [ ] Noise is allowed to produce NO MATERIAL CHANGE.
