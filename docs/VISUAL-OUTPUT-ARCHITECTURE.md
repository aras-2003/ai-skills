# Visual Output Architecture

## Goal
Render professional evidence-backed visual components without coupling domain analysis to one rendering tool.

This is the rendering layer beneath `report-composer`.

## Layers
1. Evidence and canonical data.
2. Domain analysis in existing skills/workflows.
3. Report composition: ordered sections and inline visual slots.
4. Semantic visual payload for one local slot.
5. Renderer selection.
6. Rendered inline chat component by default; specialist artifact only on explicit request.

The rendered visual is derivative presentation, not a new system of record.

## Responsibility boundary
- `report-composer` owns reading flow, section order, progressive disclosure and visual placement.
- `visual-output-design` owns visual encoding, renderer selection and integrity of each visual slot.

Do not use `visual-output-design` to create a second full dashboard beside an already complete report unless explicitly requested.

## Renderer routing
- Native charts/widgets: first choice for quantitative comparison, time series, composition, numeric relationships and other visuals that can appear in the chat response.
- Text/table/structured chat: default fallback when a richer embedded renderer is unavailable.
- Figma/FigJam: only when the user explicitly requests an editable structural artifact or Figma output.
- Figma Slides/deck: only when the user explicitly requests a presentation/deck.
- Interactive HTML/CSS: only when the user explicitly requests HTML, a file or an external interactive report.
- Generated imagery: illustration only, never factual charts or organizational truth.

## Domain patterns
Investment OS: normalized performance, allocation/concentration, overlap, valuation ranges, catalyst/risk timelines and opportunity cards.

OAF: domain heatmaps, causal maps, operating-model maps, governance flows, capability views and transformation roadmaps.

Commerce: unit-economics bridges, competitor matrices, evidence heatmaps, acquisition funnels and shortlist cards.

Career: mandate/authority matrices, role comparisons, recruitment timelines and evidence-gap views.

## Boundaries
- Visualisation cannot introduce new facts.
- Missing data stay missing.
- Canonical read/write receipts remain auditable text.
- External visual artifacts are not canonical state.
- Factual visuals retain source and as-of context.
- If chat cannot truly embed a visual inline, the system must use the best chat-native fallback.
- Do not create HTML/PDF/Figma/deck/file output as an automatic fallback; external artifacts require explicit user intent.
