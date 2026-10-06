# Integrated report composition rules

## Reading flow
Default section pattern:

1. claim / context;
2. inline visual when it materially helps;
3. interpretation;
4. implication / decision;
5. local provenance or limitation.

Do not place all visuals at the top or bottom by default.

## Progressive disclosure
First screen / opening:
- decision headline;
- 2–4 key facts;
- immediate action or next gate.

Middle:
- evidence and analysis by topic/entity;
- contextually embedded visuals.

End:
- decision queue / next actions;
- receipts;
- source/limitation notes;
- appendix only if needed.

## Inline component patterns

### Time-series block
Use when change over time matters.
For securities, support 3M / 6M / 12M switching when verified daily or suitable periodic data exist.
State normalization, FX/dividend treatment and as-of date.

### KPI strip
Use for 2–5 genuinely decision-relevant measures immediately before deeper interpretation.

### Scenario range
Use for bear/base/bull or bounded alternatives.
Do not fabricate numeric ranges from qualitative labels.

### Matrix
Use for two-dimensional comparisons such as materiality x direction, overlap, evidence status or option trade-offs.

### Structural diagram
Use for reporting lines, decision rights, dependencies, operating models, value chains or flows.
Prefer a chat-native diagram renderer when available. Use Figma/FigJam only when the user explicitly requests an editable Figma/FigJam artifact.

### Roadmap / timeline
Use for sequencing, catalysts, risks or transformation.
Clearly separate committed, conditional and unresolved items.

## Duplication rule
A visual may replace repeated prose. Keep only the interpretation that changes the decision.

Bad:
- 12-line paragraph listing allocations;
- followed by a chart showing the same allocations;
- followed by a dashboard repeating both.

Good:
- one sentence explaining why concentration matters;
- inline concentration chart;
- two sentences interpreting the decision consequence.

## Source placement
Use local provenance near visuals where source identity changes confidence.
Use a compact global source/limitations block at the end for shared sources.

## Mobile/readability
- one primary column for narrative flow;
- multi-column cards collapse cleanly;
- legends remain visible without hover;
- interactive controls are touch-friendly;
- avoid wide tables when a chart/card can communicate the same decision more clearly;
- preserve a text fallback for essential conclusions.

## Delivery rule
Default delivery is the report itself in the chat response, with visual components embedded in the relevant sections.

A separate HTML/PDF/Figma/deck/file may be produced only when the user explicitly requests that artifact or format. If the preferred inline visual is unavailable, use the best chat-native fallback rather than silently creating a file.

When an external artifact is explicitly requested, avoid duplicating the entire report in both chat and the artifact unless the user asks for both.
