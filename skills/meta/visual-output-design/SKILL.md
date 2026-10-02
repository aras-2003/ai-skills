---
name: visual-output-design
description: >
  Convert an already-supported analysis or workflow result into a professional decision-useful visual presentation.
  Use when charts, diagrams, interactive HTML, Figma/FigJam, executive dashboards, matrices, timelines or decks would
  materially improve comprehension or decision quality. Do not use visuals merely for decoration and never invent data
  to make a visual complete.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.5.0"
  maturity: candidate
  risk: low
  last_reviewed: 2026-10-02
  execution:
    default_model_class: fast
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
2. Decide whether a visual materially improves the result and whether the caller marks it as required by the visual floor.
3. Run `capability_preflight` against the tools actually available in the current runtime:
   - match the required visual grammar to a concrete renderer capability;
   - a quantitative chart renderer must deterministically encode supplied numeric series/categories;
   - `image_gen`, image viewing, generic media generation and Figma diagram/design capabilities do not qualify as quantitative data-chart renderers;
   - return `AVAILABLE`, `UNAVAILABLE`, or `UNKNOWN`.
4. If the visual is optional and no qualifying renderer exists, use the truthful text/table fallback.
5. If the visual is required and no qualifying renderer exists, return `BLOCKED_NO_RENDERER`; do not claim successful rendering and do not let a table/text fallback satisfy the slot.
6. Build a semantic visual model from the supported analysis only:
   - headline/message;
   - entities/categories;
   - measures/units;
   - relationships/order;
   - time/as-of context;
   - uncertainty/status;
   - source/provenance references.
7. Select the narrowest suitable renderer using `references/tool-routing.md`.
8. Apply the design and integrity rules in `references/design-system.md`.
9. Prefer a renderer that can appear directly inside the chat response. Use an external-artifact renderer (HTML file, Figma file, PDF, deck) only when the user explicitly requested that output form.
10. Keep the visual synchronized with its surrounding report section: it must not imply a stronger conclusion than the written analysis.
11. Provide a compact text/table fallback when useful, but label it diagnostic when a required renderer is unavailable; it does not change `BLOCKED_NO_RENDERER` to PASS.
12. For interactive HTML, keep analysis data and presentation logic separated so the report can be regenerated from the same payload.

## Decision rules
- Prefer one strong visual over several decorative ones.
- When the calling report marks a visual slot as required by the visual-floor rule and supported data are present, render a real chat-native visual if a suitable renderer exists. If none exists, return `BLOCKED_NO_RENDERER`; text-only is not a successful substitute.
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
- **fallback**: concise textual/table equivalent when rendering is unavailable.
- **capability_status**: AVAILABLE / UNAVAILABLE / UNKNOWN.
- **render_status**: PAYLOAD_RENDERED / UI_CONFIRMED / BLOCKED_NO_RENDERER / FAIL_RENDERER_INVOCATION / UI_RENDER_UNCONFIRMED / NOT_REQUIRED.

## Evidence requirements
- Every plotted factual value must come from user-provided data, canonical state, calculation or cited evidence.
- Derived values must be reproducible from the stated inputs.
- Scenario/estimate values must be labelled as such.
- Visual labels must preserve units, time period and denominator.

## Failure and uncertainty handling
- If the preferred chat-native renderer is unavailable, choose the next qualifying chat-native renderer. If a required visual has no qualifying renderer, return `BLOCKED_NO_RENDERER`; a table/text fallback may accompany the status but cannot satisfy the requirement.
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
- [ ] Tool success alone is not called UI-rendered. A valid image payload receipt proves `PAYLOAD_RENDERED`; visible client rendering is `UI_CONFIRMED`.
- [ ] For a required visual slot, `PAYLOAD_RENDERED` without `UI_CONFIRMED` resolves to `UI_RENDER_UNCONFIRMED`.
- [ ] Do not describe the visual as rendered/visible in the surrounding prose unless `UI_CONFIRMED`.
- [ ] If the client shows a broken/blank placeholder, report `UI_RENDER_UNCONFIRMED`, not PASS.

## References
- references/tool-routing.md
- references/design-system.md
