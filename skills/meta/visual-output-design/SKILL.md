---
name: visual-output-design
description: >
  Convert an already-supported analysis or workflow result into a professional decision-useful visual presentation.
  Use when charts, diagrams, interactive HTML, Figma/FigJam, executive dashboards, matrices, timelines or decks would
  materially improve comprehension or decision quality. Do not use visuals merely for decoration and never invent data
  to make a visual complete.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: low
  last_reviewed: 2026-10-02
  execution:
    default_model_class: fast
---

# Visual Output Design

## Purpose
Add a professional presentation layer after the analytical work is complete. Preserve the source analysis, evidence,
uncertainty and canonical data contracts while choosing the best visual medium available in the runtime.

## Preconditions
- The underlying analysis/result already exists or can be produced by the calling workflow.
- Visualisation must not become a second analytical engine.
- Decision-relevant data must retain source/provenance and as-of context.

## Procedure
1. Identify the decision or comprehension job of the output.
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
6. Render the visual using a connected native/plugin tool when one is appropriate and available.
7. Keep the visual and prose synchronized: the visual must not imply a stronger conclusion than the written analysis.
8. Provide a compact text fallback when the chosen renderer is unavailable.
9. For interactive HTML, keep analysis data and presentation logic separated so the report can be regenerated from the same payload.

## Decision rules
- Prefer one strong visual over several decorative ones.
- Use a chart for quantitative comparison, trend, composition or relationship.
- Use a diagram for structure, flow, dependency, ownership or state.
- Use interactive HTML for linked multi-view analysis where filters, tabs, hover detail or multiple coordinated visuals add value.
- Use Figma/FigJam for editable executive-grade diagrams, reusable visual systems or high-fidelity layouts.
- Use Figma Slides/deck output for narrative presentation rather than analysis exploration.
- Use generated imagery only for illustrative assets, never to encode factual quantities or organizational truth.
- Do not use ASCII art, pseudo-charts made from punctuation or decorative emoji when a real renderer is available.
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
- **visual_type**: chart / diagram / interactive-report / figma-design / deck / none;
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
- If the preferred renderer is unavailable, choose the next suitable renderer; do not pretend a tool ran.
- If data are incomplete, show the gap or omit the visual element rather than fabricating it.
- If a high-fidelity Figma/deck artifact would add little value, do not create one.
- If interactivity is unavailable, fall back to a static chart/table plus concise interpretation.

## Quality checks
- [ ] Visual choice matches the information structure.
- [ ] No new unsupported facts were introduced.
- [ ] Units, period, denominator and as-of context are visible where relevant.
- [ ] Sources/provenance remain recoverable.
- [ ] Visual and prose imply the same conclusion.
- [ ] The result is readable without relying on color alone.
- [ ] The visual is not decorative clutter.
- [ ] A text fallback exists when the renderer is non-portable.

## References
- references/tool-routing.md
- references/design-system.md
