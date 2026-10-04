---
name: report-composer
description: >
  Compose one integrated decision report from an already-supported workflow result by interleaving narrative, evidence,
  decisions and contextually placed visual slots. Use when the user needs a coherent report where charts, diagrams,
  interactive components or Figma outputs appear inside the relevant sections instead of as a separate parallel artifact.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.9.0"
  maturity: candidate
  risk: low
  last_reviewed: 2026-10-02
  execution:
    default_model_class: standard
---

# Report Composer

## Purpose
Turn a completed analysis into one coherent decision report rendered **in the chat response by default**. The report structure is primary; visuals are embedded where they improve the reader's understanding of the surrounding argument.

Do not create a second "visual report" beside the chat answer. Do not create an HTML/PDF/Figma/deck/file unless the user explicitly requests an external artifact or file format.

## Preconditions
- The underlying analysis has already been produced by the calling workflow.
- Evidence, uncertainty and canonical state boundaries are already known.
- The composer may reorganize presentation, but must not silently change analytical conclusions.

## Procedure
1. Identify the audience, decision and minimum report depth.
2. Apply `references/report-quality-standard.md` and `references/report-state-and-evidence-contract.md` as mandatory contracts.
3. Build the evidence ledger before presentation:
   - classify each decision-relevant claim as CANONICAL / USER_PROVIDED / EXTERNAL_VERIFIED / DERIVED / UNKNOWN;
   - require reproducible inputs for every DERIVED claim;
   - run the causal-attribution gate before stating why something changed.
4. Run `capability_preflight` before finalising any visual-floor requirement:
   - inspect both tools and host-native chat widgets/components exposed by the current runtime;
   - the native ChatGPT `chart` widget counts as an interactive deterministic data renderer when exposed;
   - classify whether a deterministic data renderer exists for the required visual grammar;
   - do not count `image_gen`, image viewers, generic media generation, or Figma diagram/design tools as a quantitative chart renderer;
   - record one of: `AVAILABLE`, `UNAVAILABLE`, `UNKNOWN`;
   - for required investment price/KPI charts, `UNKNOWN` means **attempt the host-native chart surface**, not block the report.
5. Select a report profile from `references/report-profiles.md` or derive a minimal equivalent.
6. Build a semantic report model containing ordered sections:
   - section purpose;
   - narrative block;
   - evidence block;
   - decision/implication block;
   - optional inline visual slots;
   - section-level provenance and uncertainty.
7. Decide visual placement by reading flow, not by asset type:
   - put the visual immediately after the claim/context it helps explain;
   - put interpretation immediately after the visual;
   - avoid collecting unrelated visuals into a separate appendix/dashboard unless the user explicitly asks.
8. For each visual slot, call `visual-output-design` with:
   - the local section question;
   - only the relevant supported data;
   - required renderer capabilities;
   - as-of context and provenance.
9. For required interactive investment price/KPI slots, do not finalize the report until a host-native chart attempt has been made when chartable verified data exist. A table is not an acceptable pre-attempt substitute.
10. Choose output target from actual renderer execution:
   - **chat-native report** when required visual slots have a qualifying renderer and a valid payload was produced;
   - **chat-blocked** when no qualifying renderer exists or invocation fails;
   - **external artifact** only when the user explicitly asks for one.
   Client-display success is never inferred by the model. A valid payload is `PAYLOAD_RENDERED`; client display remains `NOT_OBSERVABLE`.
11. A blocked report may still include a compact table/matrix so the user can inspect the data, but that fallback is diagnostic only: it does **not** satisfy the required visual slot and must carry `BLOCKED_NO_RENDERER` (or `FAIL_RENDERER_INVOCATION` when a qualifying renderer was discovered but failed).
12. Preserve progressive disclosure:
   - lead with the decision and minimum evidence;
   - keep detail near the section it supports;
   - move exhaustive evidence tables or appendices later.
13. Keep receipts, source notes and material limitations in the same report, not in a disconnected parallel artifact.
14. Run the contradiction check from the state/evidence contract before final output.
15. Never silently convert a required visual-floor slot into successful renderer execution. If no qualifying renderer exists or invocation fails, surface that execution state explicitly. Do not silently move the report into an HTML/PDF/Figma/deck artifact. Create an external artifact only when the user explicitly requested one.

## Visual coverage and dashboard contract

- For each required slot, track slot_id, renderer class, execution state, whether a native visual element was included inline, and its adjacent provenance/caption.
- In a detailed opportunity report, create a compact in-chat shortlist dashboard after the executive summary/radar. Show only decision-useful fields such as candidate, status, key change, valuation/expectation risk, portfolio fit, and next gate. Use a readable table or cards; do not call it interactive unless it is.
- Place candidate-specific price/KPI visuals inside the corresponding candidate section. Share a chart only when the compared series use compatible definitions, units, and periods.
- Before finalising, compare required slots with actual inline visual elements. A slot is not complete just because data were gathered, a tool was detected, a tool call was attempted, or a payload was mentioned in prose.
- Never expose data:image/...;base64,..., raw base64, serialized image blocks, or chart JSON in user-facing text/Markdown. Preserve returned media as an actual inline image or native chart element. If the runtime cannot emit it, state the slot's blocked/failed status and retain a compact table fallback.
- Prefer the best usable in-chat visual available. If only a static image renderer exists, embed the image as a native image element and label it static; do not imply interactivity.

## Inline visual slot contract
Each slot must define:
- **slot_id**
- **purpose**
- **placement_after**
- **renderer_class**: native-chart / native-widget / table / structured-chat / interactive-html / figma-diagram / figma-design / deck / none
- **payload**
- **interaction**: e.g. none, 3m/6m/12m, scenario toggle, filter
- **as_of**
- **provenance**
- **uncertainty**
- **fallback**
- **capability_status**: AVAILABLE / UNAVAILABLE / UNKNOWN
- **renderer_execution_status**: NOT_REQUIRED / NOT_ATTEMPTED / BLOCKED_NO_RENDERER / PAYLOAD_RENDERED / FAIL_RENDERER_INVOCATION
- **client_display_status**: NOT_OBSERVABLE
- **inline_visual_included**: YES / NO

## Decision rules
- The report is the product; visuals are evidence-bearing components inside it.
- Apply the default quality standard without requiring the user to spell out formatting, section limits, chart preferences or receipt compactness in the prompt.
- Prefer concise executive hierarchy: 3–5 opening points, a small number of detailed entities, selective visuals and a 3–5 item decision queue unless the task genuinely requires more.
- Apply the visual-floor rule from the quality standard: material chartable data create a required visual slot. If a qualifying renderer is absent, the report is blocked rather than silently accepted as text-only.
- Do not make a dashboard merely because several metrics exist.
- Do not repeat the same content in prose and a separate visual artifact unless repetition materially aids the decision.
- Use interactive controls only when the alternative views answer a real decision question.
- For company price/performance context, 3/6/12 month switching is useful when comparable, verified time-series data exist.
- A visual may summarize but must not strengthen, rank or score beyond the underlying analysis.
- Prefer native chat renderers for normal report delivery. Use Figma/HTML/PDF/deck renderers only when the user explicitly requests an editable or external artifact/file.
- Canonical READ/WRITE receipts remain explicit and auditable.

## Output contract
Return one semantic report with:
- **report_title**
- **decision_headline**
- **analysis_state**: COMPLETE / PARTIAL_EVIDENCE / BLOCKED_ANALYSIS
- **target**: chat-native / chat-blocked / external-artifact-requested
- **sections[]**
  - heading
  - narrative
  - evidence
  - visual_slots[]
  - interpretation
  - decision_or_next_step
  - provenance
  - uncertainty
- **runtime_diagnostic** only when requested or useful:
  - capability_status
  - renderer_execution_status
  - client_display_status: NOT_OBSERVABLE
- **receipts**
- **limitations**
- **appendix** only when needed

Do not emit `report_status: PASS` for ordinary report composition. Runtime visual PASS/FAIL belongs to an external evaluator with client evidence.

## Evidence requirements
- Every factual visual slot inherits the evidence standard of the calling workflow.
- Values must retain units, periods and denominators.
- Derived analytics must remain identifiable as derived.
- Missing evidence stays visibly missing.

## Failure and uncertainty handling
- If a required investment price/KPI visual has `UNKNOWN` renderer visibility, attempt the host-native chart component before deciding it is blocked.
- If a required visual is explicitly unavailable after the required attempt, use `BLOCKED_NO_RENDERER`.
- If renderer invocation fails, use `FAIL_RENDERER_INVOCATION`.
- If the renderer returns a valid payload, use `PAYLOAD_RENDERED`; do not infer whether the client displayed it.
- If decision-critical evidence is missing but useful analysis remains possible, use `analysis_state: PARTIAL_EVIDENCE`.
- If the core requested analysis cannot be supported, use `analysis_state: BLOCKED_ANALYSIS`.
- Never generate an external file merely as a fallback.

## Quality checks
- [ ] The output is one coherent report in chat by default, not text plus a duplicate dashboard or unsolicited file.
- [ ] Visuals appear where the surrounding narrative needs them.
- [ ] Every required slot is covered by an actual inline visual element or is explicitly blocked/failed.
- [ ] A discovery report includes a compact in-chat shortlist dashboard when several candidates are compared.
- [ ] No raw base64/data URI or serialized chart payload appears in user-facing text.
- [ ] Every visual has local interpretation and provenance.
- [ ] No visual exists only for decoration.
- [ ] The same conclusion is preserved across text and visual rendering.
- [ ] Interaction controls correspond to real supported alternate views.
- [ ] No external artifact/file was created unless explicitly requested.
- [ ] The report remains readable on narrow/mobile layouts.
- [ ] Receipts and limitations remain visible.
- [ ] `capability_preflight` was run for every required visual-floor slot.
- [ ] Text/table fallback never converts `BLOCKED_NO_RENDERER` into renderer success.
- [ ] Renderer success is reported only as `PAYLOAD_RENDERED`; client display remains `NOT_OBSERVABLE`.
- [ ] No `UI_CONFIRMED`, `UI_RENDER_UNCONFIRMED`, `PASS_WITH_LIMITATIONS` or invented status appears.
- [ ] Every derived metric is reproducible from identified inputs.
- [ ] User-provided but non-reproducible metrics remain labelled USER_PROVIDED.
- [ ] Causal claims pass the causal-attribution gate.
- [ ] Limitations do not contradict earlier claims.

## References
- references/report-quality-standard.md
- references/report-state-and-evidence-contract.md
- references/report-profiles.md
- references/composition-rules.md
