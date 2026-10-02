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
1. Read canonical current_positions, latest portfolio snapshot, current policy and active thesis versions through investment-record-store. Emit canonical READ receipt.
2. If current state or prior snapshot is unavailable, state exactly which comparison is blocked. Do not substitute local/chat/analytics cache.
3. Reconcile current state and preserve append-only snapshot history.
4. Use Data/analytics tooling for concentration, ETF look-through, overlap, currency, theme/cycle and historical trend calculations when useful. Treat results as derived analytics.
5. Attribute change only when evidence supports causality:
   - current state alone cannot establish drift cause;
   - current + prior canonical snapshots establish change, but not necessarily whether it came from trades or market movement;
   - classify trade-driven vs market-driven only when transaction history plus comparable state, or an explicit canonical attribution record, distinguishes the causes;
   - otherwise return attribution `UNKNOWN` and do not guess.
6. Triage new company/industry/market evidence with investment-attention-triage.
7. For REVIEW/ESCALATE positions, run thesis-monitor.
8. Revalue only positions where valuation drift can change the action.
9. Use position-sizing-review when concentration, uncertainty or thesis state changes the policy band.
10. Surface only positions requiring action review.
11. Persist new snapshot, signals, thesis-monitor records and user-confirmed decisions through investment-record-store only.
12. Emit canonical WRITE receipt.

## Decision rules
- analytics layer reads/derives; it does not become the system of record;
- position risk can deteriorate while company thesis remains intact;
- no-trade price drift is still portfolio drift;
- policy breach triggers review, not automatic sale;
- without prior canonical snapshot, do not claim a complete change comparison;
- without sufficient transaction/history evidence, do not classify drift as trade-driven or market-driven;
- absence of observed transactions is not evidence that no transaction occurred;
- user-provided aggregate metrics that cannot be recomputed from the visible holdings remain USER_PROVIDED, not DERIVED.

## Output contract
Requires attention; no material change; portfolio-level observations; derived analytics/provenance; canonical READ/WRITE receipts.

## Stop conditions
Stop when every material alert is tied to evidence or policy.

## Integrated report presentation
Render the report directly in the chat response by default. External HTML/PDF/Figma/deck/file output is allowed only when the user explicitly requests that artifact or format.

After analytical synthesis, call `report-composer` to produce one portfolio decision report. Use `visual-output-design` for inline components only.

Default profile:
- portfolio decision headline + KPI strip;
- concentration/diversification with inline allocation/concentration charts;
- overlap/look-through matrix when supported;
- material drift/change since prior snapshot;
- positions requiring attention;
- opportunity implications;
- decision queue / next actions;
- canonical READ/WRITE receipts and limitations.

Prefer embedded chat-native visual payloads when multiple coordinated portfolio views materially help. Renderer payload success does not prove client display; client display remains NOT_OBSERVABLE to the model. If rendering is unavailable, use truthful tables/structured prose as diagnostic fallback; do not generate an external artifact unless explicitly requested.
