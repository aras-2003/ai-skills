---
name: thesis-monitor
description: >
  Monitor an existing investment thesis against new earnings, guidance, industry data, price/valuation changes and
  predefined kill criteria. Use canonical thesis history plus structured research/primary evidence; do not restart
  full underwriting unless the thesis materially changes or evidence becomes stale.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.2.0"
  maturity: production
  risk: high
  last_reviewed: 2026-10-02
  execution:
    default_model_class: standard
---

# Thesis Monitor

## Purpose
Evaluate what changed versus the recorded thesis rather than summarizing news from scratch.

## Procedure
1. Load the latest canonical thesis version and prior monitoring state through investment-record-store.
2. Gather new dated evidence using structured research tools for breadth and primary sources for material claim verification.
3. Classify materiality separately from direction: NOISE / MONITOR / REVIEW / ESCALATE and STRENGTHENS / WEAKENS / MIXED / NEUTRAL.
4. Map each material change to the exact thesis assumption, KPI, catalyst, risk or kill criterion.
5. Update valuation/expectations context separately from business-thesis state.
6. Compare market reaction with fundamental change only as interpretation.
7. Detect portfolio implications such as position drift but route sizing decisions to position-sizing-review.
8. Append a new monitoring/research event through investment-record-store; never rewrite thesis history.
9. Escalate only when evidence justifies deeper work.

## Decision rules
- News importance is measured against thesis, not headline size.
- Research-provider output does not replace canonical thesis history.
- Price change alone does not prove thesis change.
- Kill criteria require evidence, not narrative discomfort.
- Historical thesis versions remain immutable.

## Output contract
What changed; materiality; direction; affected thesis element; valuation/expectations impact; market reaction context; next step; persistence receipt.
