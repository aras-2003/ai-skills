# Visual quality and integrity system

## Executive design principles
- Lead with one clear message.
- Use a restrained information hierarchy: headline -> key metrics -> visual -> implications -> sources.
- Prefer whitespace and grouping over borders everywhere.
- Keep labels concise and direct.
- Make the first screen useful without scrolling through a long preamble.
- Use consistent component patterns across related workflows.

## Quantitative integrity
- Use the correct chart type for the relationship.
- Preserve chronological order in time-series.
- Do not truncate axes to exaggerate differences unless the context explicitly requires it and the scale is obvious.
- For normalized performance charts, state the normalization baseline and whether FX/dividends are excluded.
- Show units and denominators.
- Label scenarios/estimates separately from observed values.
- Do not hide missing observations by smoothing or interpolation without disclosure.

## Color
- Do not rely on color alone for meaning.
- Keep semantic color roles stable within one artifact.
- Reserve strong emphasis for exceptions, risk or action.
- Avoid rainbow palettes for categorical data unless category identity genuinely requires it.
- Use sufficient contrast in light and dark themes.

## Tables and cards
Use cards for:
- a few key metrics or states.

Use tables for:
- precise multi-column comparisons;
- evidence/provenance;
- detailed action lists.

Do not turn every field into a card.

## Diagrams
- Prefer left-to-right or top-to-bottom reading flow.
- Minimize crossing connectors.
- Make ownership/decision nodes visually distinct from information or execution nodes.
- Label inferred relationships as hypotheses where necessary.
- Keep current state and target state visually distinct.
- Do not imply reporting lines, authority or causal links that the evidence does not establish.

## Domain patterns

### Investing
Preferred:
- normalized price/performance line chart;
- allocation/concentration bars;
- overlap/exposure matrix;
- scenario valuation range;
- catalyst/risk timeline;
- candidate comparison cards;
- materiality x direction matrix.

Avoid:
- one composite stock score;
- decorative gauges;
- price charts without date/source context.

### OAF / organisational architecture
Preferred:
- operating-model map;
- decision-rights flow;
- governance/decision path;
- capability heatmap;
- interface/dependency map;
- transformation roadmap/gantt;
- architecture option comparison.

Avoid:
- generic org chart when the problem is decision rights or interfaces;
- boxes-and-lines with unsupported authority assumptions.

### Commerce
Preferred:
- unit-economics waterfall/bridge;
- competitor positioning matrix;
- demand/evidence heatmap;
- acquisition funnel;
- supplier/risk comparison;
- opportunity shortlist cards.

### Career
Preferred:
- mandate vs authority matrix;
- role-scope comparison;
- recruitment funnel/timeline;
- evidence-gap matrix.

## Provenance footer
For decision-useful visuals, include as applicable:
- as-of date;
- canonical source or dataset;
- external source names/links;
- notes on derived metrics;
- important omissions/limitations.
