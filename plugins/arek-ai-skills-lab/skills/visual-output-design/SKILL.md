---
name: visual-output-design
description: 'Convert an already-supported analysis or workflow result into a professional
  decision-useful visual presentation. Use when charts, diagrams, interactive HTML,
  Figma/FigJam, executive dashboards, matrices, timelines or decks would materially
  improve comprehension or decision quality. Do not use visuals merely for decoration
  and never invent data to make a visual complete.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.4.0
  maturity: candidate
  risk: low
  last_reviewed: '2026-10-02'
---

# Visual Output Design

## Purpose
Render one evidence-backed visual component or visual system for an already-defined local information need.
This skill is the renderer/router beneath `report-composer`; it does not own the structure of a full report.

Preserve the source analysis, evidence, uncertainty and canonical data contracts while choosing the best visual medium available in the runtime.

## Preconditions
- The underlying analysis/result already exists or can be produced by the calling workflow.
- Visualisation must not become a second analytical engine.
- Decision-relevant data must retain source/provenance and as-of context.

## Procedure
1. Identify the local decision/comprehension job supplied by the calling workflow or `report-composer`.
2. Decide whether a visual materially improves the result. If not, keep the response concise and textual.
3. Build a semantic visual model from the supported analysis only:
   - headline/message;
   - entities/categories;
   - measures/units;
   - relationships/order;
   - time/as-of context;
   - uncertainty/status;
   - source/provenance references.
4. Select the narrowest suitable renderer using `references/tool-routing.md`.
5. Apply the design and integrity rules in `references/design-system.md`.
6. Prefer a renderer that can appear directly inside the chat response. Use an external-artifact renderer (HTML file, Figma file, PDF, deck) only when the user explicitly requested that output form.
7. Keep the visual synchronized with its surrounding report section: it must not imply a stronger conclusion than the written analysis.
8. Provide a compact text fallback when the chosen renderer is unavailable.
9. For interactive HTML, keep analysis data and presentation logic separated so the report can be regenerated from the same payload.

## Decision rules
- Prefer one strong visual over several decorative ones.
- Prefer the visual grammar in `references/design-system.md`: horizontal bars for ranked concentration, real time-series lines for performance, matrices for overlap/trade-offs, ranges for scenarios, KPI strips for a few metrics.
- Use a chart for quantitative comparison, trend, composition or relationship.
- Use a diagram for structure, flow, dependency, ownership or state.
- Use chat-native interactive components/widgets when available for linked views, filters, horizon switches or hover detail.
- Use interactive HTML only when the user explicitly requests HTML/a file or an external interactive artifact.
- Use Figma/FigJam only when the user explicitly requests an editable design/diagram artifact or when the calling task explicitly requires Figma output.
- Use Figma Slides/deck output only when the user explicitly requests a presentation/deck.
- Use generated imagery only for illustrative assets, never to encode factual quantities or organizational truth.
- Do not use ASCII art or punctuation-based pseudo-charts in professional decision reports.
- Do not expose raw Mermaid code fences to the user. Mermaid is acceptable only when the runtime renders it as an embedded visual; avoid Mermaid xychart when a better native chart/widget is available.
- Do not create a single composite score merely to simplify a visual when the underlying dimensions should remain separate.
- Never infer missing values, dates, hierarchy, weights or causal links just to make a chart or diagram look complete.

## Inputs
- analysis result or workflow synthesis;
- structured data where available;
- intended audience and decision;
- relevant sources/provenance;
- optional user preference for format/tool.

## Output contract
Return or render:
- **message**: one decision-relevant headline;
- **visual_type**: chart / diagram / interactive-component / figma-design / deck / none;
- **visual_payload**: structured data used by the renderer;
- **as_of**: date/time context when relevant;
- **provenance**: sources or canonical data references;
- **uncertainty**: what is estimated, missing or inferred;
- **fallback**: concise textual equivalent when rendering is unavailable.

## Evidence requirements
- Every plotted factual value must come from user-provided data, canonical state, calculation or cited evidence.
- Derived values must be reproducible from the stated inputs.
- Scenario/estimate values must be labelled as such.
- Visual labels must preserve units, time period and denominator.

## Failure and uncertainty handling
- If the preferred chat-native renderer is unavailable, choose the next suitable chat-native renderer or a table/text fallback; do not escape to an external file unless explicitly requested.
- If data are incomplete, show the gap or omit the visual element rather than fabricating it.
- Do not create a Figma/HTML/PDF/deck artifact unless the user explicitly requested that artifact class.
- If interactivity is unavailable, fall back to a static chart/table plus concise interpretation.

## Quality checks
- [ ] Visual choice matches the information structure.
- [ ] No new unsupported facts were introduced.
- [ ] Units, period, denominator and as-of context are visible where relevant.
- [ ] Sources/provenance remain recoverable.
- [ ] Visual and prose imply the same conclusion.
- [ ] The result is readable without relying on color alone.
- [ ] The visual is not decorative clutter.
- [ ] The renderer stays inside chat unless an external artifact was explicitly requested.
- [ ] A text fallback exists when the renderer is non-portable.

## References
- references/tool-routing.md
- references/design-system.md
