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
  version: 0.10.0
  maturity: candidate
  risk: low
  last_reviewed: '2026-10-02'
---

# Visual Output Design

## Purpose
Render one evidence-backed visual component or visual system for an already-defined local information need.
This skill is the renderer/router beneath `report-composer`; it does not own the structure of a full report.

Preserve the source analysis, evidence, uncertainty and canonical data contracts while choosing the best visual medium available in the runtime. Follow `../report-composer/references/report-state-and-evidence-contract.md` for renderer/client-state semantics.

## Preconditions
- The underlying analysis/result already exists or can be produced by the calling workflow.
- Visualisation must not become a second analytical engine.
- Decision-relevant data must retain source/provenance and as-of context.

## Procedure
1. Identify the local decision/comprehension job supplied by the calling workflow or `report-composer`.
2. Decide whether a visual materially improves the result and whether the caller marks it as required by the visual floor.
3. Run `capability_preflight` against the capabilities actually exposed by the host runtime:
   - inspect both callable tools and host-native chat widgets/components;
   - the native ChatGPT `chart` widget, when exposed, is a qualifying interactive quantitative renderer for bar/line/pie/scatter charts;
   - for investment price/KPI time series, prefer native `chart` line charts over static MCP/image renderers;
   - a quantitative chart renderer must deterministically encode supplied numeric series/categories;
   - `image_gen`, image viewing, generic media generation and Figma diagram/design capabilities do not qualify as quantitative data-chart renderers;
   - return `AVAILABLE`, `UNAVAILABLE`, or `UNKNOWN`.
4. If the visual is optional and no qualifying renderer exists, use the truthful text/table fallback.
5. For a **required interactive investment price/KPI chart**:
   - if preflight is `AVAILABLE`, render with the qualifying interactive chart capability;
   - if preflight is `UNKNOWN` because host-native widgets are not visible through tool enumeration, build the factual payload and **attempt the host-native chart component before blocking**;
   - only after an explicit unavailable/rejected host-native attempt may the slot become `BLOCKED_NO_RENDERER`;
   - if an available renderer invocation fails, use `FAIL_RENDERER_INVOCATION`.
6. For other required visuals with no qualifying renderer, return `BLOCKED_NO_RENDERER`; do not claim successful rendering and do not let a table/text fallback satisfy the slot.
7. Build a semantic visual model from the supported analysis only:
   - headline/message;
   - entities/categories;
   - measures/units;
   - relationships/order;
   - time/as-of context;
   - uncertainty/status;
   - source/provenance references.
8. Select the narrowest suitable renderer using `references/tool-routing.md`.
9. Apply the design and integrity rules in `references/design-system.md`.
10. Prefer a renderer that can appear directly inside the chat response. Use an external-artifact renderer (HTML file, Figma file, PDF, deck) only when the user explicitly requested that output form.
11. Keep the visual synchronized with its surrounding report section: it must not imply a stronger conclusion than the written analysis.
12. Provide a compact text/table fallback when useful, but label it diagnostic when a required renderer is unavailable; it does not change renderer execution from `BLOCKED_NO_RENDERER`.
13. For interactive HTML, keep analysis data and presentation logic separated so the report can be regenerated from the same payload.

## Inline visual delivery integrity

A visual slot is complete only when a valid chart, widget, or image is emitted as a native visual element in the chat response and placed beside the relevant analysis.

- Never print, quote, or expose a data:image/...;base64,... payload in prose, a Markdown image URL, a code block, or a table. Do not stringify binary/image content.
- When a renderer returns an image content block, preserve it as the renderer's native image output; add only a short caption, as-of date, and provenance in text.
- Use a native interactive chart only through a real host-supported response mechanism. Do not invent a chart tool, widget call, or response syntax that the runtime does not expose.
- A valid static image is a useful inline visual when interactivity is unavailable, but label it static; do not claim hover, filtering, or interaction.
- If no actual inline visual can be emitted, mark the slot blocked/failed and show a concise diagnostic table. A URL, base64 string, or JSON payload printed as text is not a rendered visual.

## Decision rules
- Prefer one strong visual over several decorative ones.
- When a required investment-history slot has supported data, **attempt the host-native chart** only through a documented, callable host mechanism; prefer the interactive chart before any text/table fallback. Tool-list uncertainty alone is not evidence that the renderer is unavailable.
- When another required visual has no suitable renderer, return `BLOCKED_NO_RENDERER`; text-only is not a successful substitute.
- Prefer the visual grammar in `references/design-system.md`: horizontal bars for ranked concentration, real time-series lines for performance, matrices for overlap/trade-offs, ranges for scenarios, KPI strips for a few metrics.
- Use a chart for quantitative comparison, trend, composition or relationship.
- Use a diagram for structure, flow, dependency, ownership or state.
- Use chat-native interactive components/widgets when available for linked views, filters, horizon switches or hover detail.
- Treat host-native `chart` as the default interactive quantitative renderer when available; do not ignore it merely because it is not packaged as an MCP tool.
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
- **fallback**: concise textual/table equivalent when rendering is unavailable.
- **capability_status**: AVAILABLE / UNAVAILABLE / UNKNOWN.
- **renderer_execution_status**: NOT_REQUIRED / NOT_ATTEMPTED / BLOCKED_NO_RENDERER / PAYLOAD_RENDERED / FAIL_RENDERER_INVOCATION.
- **client_display_status**: NOT_OBSERVABLE.

## Evidence requirements
- Every plotted factual value must come from user-provided data, canonical state, calculation or cited evidence.
- Derived values must be reproducible from the stated inputs.
- Scenario/estimate values must be labelled as such.
- Visual labels must preserve units, time period and denominator.

## Failure and uncertainty handling
- If the preferred chat-native renderer is unavailable, choose the next qualifying chat-native renderer.
- For required investment history, do not treat `UNKNOWN` capability discovery as unavailable: attempt the host-native chart surface first.
- If the attempted host surface explicitly cannot render the required visual, return `BLOCKED_NO_RENDERER`; a table/text fallback may accompany the status but cannot satisfy the requirement.
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
- [ ] Required quantitative visuals passed `capability_preflight` against an actual deterministic renderer.
- [ ] Media-generation or design tools were not misclassified as quantitative chart renderers.
- [ ] `BLOCKED_NO_RENDERER` cannot be reported as successful rendering.
- [ ] Tool success with a valid native image/chart payload is `PAYLOAD_RENDERED`, not proof of client display.
- [ ] No base64 image data or serialized visual payload leaked into user-facing text.
- [ ] Every required visual slot has an actual inline visual element, or an explicit blocked/failed state.
- [ ] Client display is always `NOT_OBSERVABLE` from the model unless explicit external evidence is supplied.
- [ ] Do not emit `UI_CONFIRMED`, `UI_RENDER_UNCONFIRMED`, `VISIBLE` or `BROKEN` as model-owned facts.
- [ ] Do not describe a visual as visible/rendered "above" merely because the tool returned an image payload.

## References
- references/tool-routing.md
- references/design-system.md
