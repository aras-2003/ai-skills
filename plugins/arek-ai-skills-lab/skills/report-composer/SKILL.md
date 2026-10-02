---
name: report-composer
description: 'Compose one integrated decision report from an already-supported workflow
  result by interleaving narrative, evidence, decisions and contextually placed visual
  slots. Use when the user needs a coherent report where charts, diagrams, interactive
  components or Figma outputs appear inside the relevant sections instead of as a
  separate parallel artifact.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.1.0
  maturity: candidate
  risk: low
  last_reviewed: '2026-10-02'
---

# Report Composer

## Purpose
Turn a completed analysis into one coherent decision document. The report structure is primary; visuals are embedded where
they improve the reader's understanding of the surrounding argument.

Do not create a second "visual report" beside a textual answer.

## Preconditions
- The underlying analysis has already been produced by the calling workflow.
- Evidence, uncertainty and canonical state boundaries are already known.
- The composer may reorganize presentation, but must not silently change analytical conclusions.

## Procedure
1. Identify the audience, decision and minimum report depth.
2. Select a report profile from `references/report-profiles.md` or derive a minimal equivalent.
3. Build a semantic report model containing ordered sections:
   - section purpose;
   - narrative block;
   - evidence block;
   - decision/implication block;
   - optional inline visual slots;
   - section-level provenance and uncertainty.
4. Decide visual placement by reading flow, not by asset type:
   - put the visual immediately after the claim/context it helps explain;
   - put interpretation immediately after the visual;
   - avoid collecting unrelated visuals into a separate appendix/dashboard unless the user explicitly asks.
5. For each visual slot, call `visual-output-design` with:
   - the local section question;
   - only the relevant supported data;
   - required renderer capabilities;
   - as-of context and provenance.
6. Choose output target:
   - **chat-native report** when the runtime can embed native charts/widgets inline;
   - **rich integrated report** when HTML/React/Figma/deck rendering is required for richer interactivity/layout;
   - **text/table fallback** when richer renderers are unavailable.
7. Preserve progressive disclosure:
   - lead with the decision and minimum evidence;
   - keep detail near the section it supports;
   - move exhaustive evidence tables or appendices later.
8. Keep receipts, source notes and material limitations in the same report, not in a disconnected parallel artifact.
9. If the runtime cannot truly embed a requested visual inline in chat, say so and render one integrated rich report instead of duplicating the full narrative in two places.

## Inline visual slot contract
Each slot must define:
- **slot_id**
- **purpose**
- **placement_after**
- **renderer_class**: native-chart / interactive-html / figma-diagram / figma-design / deck / table / none
- **payload**
- **interaction**: e.g. none, 3m/6m/12m, scenario toggle, filter
- **as_of**
- **provenance**
- **uncertainty**
- **fallback**

## Decision rules
- The report is the product; visuals are evidence-bearing components inside it.
- Do not make a dashboard merely because several metrics exist.
- Do not repeat the same content in prose and a separate visual artifact unless repetition materially aids the decision.
- Use interactive controls only when the alternative views answer a real decision question.
- For company price/performance context, 3/6/12 month switching is useful when comparable, verified time-series data exist.
- A visual may summarize but must not strengthen, rank or score beyond the underlying analysis.
- Figma is preferred for editable structural artifacts; HTML is preferred for integrated multi-section reports with interactive components.
- Canonical READ/WRITE receipts remain explicit and auditable.

## Output contract
Return one semantic report with:
- **report_title**
- **decision_headline**
- **target**: chat-native / rich-report / text-fallback
- **sections[]**
  - heading
  - narrative
  - evidence
  - visual_slots[]
  - interpretation
  - decision_or_next_step
  - provenance
  - uncertainty
- **receipts**
- **limitations**
- **appendix** only when needed

## Evidence requirements
- Every factual visual slot inherits the evidence standard of the calling workflow.
- Values must retain units, periods and denominators.
- Derived analytics must remain identifiable as derived.
- Missing evidence stays visibly missing.

## Failure and uncertainty handling
- If `visual-output-design` is unavailable, preserve the integrated section structure and use compact tables/text.
- If inline embedding is not supported by the current chat runtime, do not pretend it is; switch to one rich integrated report or a text fallback.
- If an interactive control lacks complete comparable data, omit the control or disable the unsupported horizon/state.
- If a section has no useful visual, do not force one.

## Quality checks
- [ ] The output is one coherent report, not text plus a duplicate dashboard.
- [ ] Visuals appear where the surrounding narrative needs them.
- [ ] Every visual has local interpretation and provenance.
- [ ] No visual exists only for decoration.
- [ ] The same conclusion is preserved across text and visual rendering.
- [ ] Interaction controls correspond to real supported alternate views.
- [ ] The report remains readable on narrow/mobile layouts.
- [ ] Receipts and limitations remain visible.

## References
- references/report-profiles.md
- references/composition-rules.md
