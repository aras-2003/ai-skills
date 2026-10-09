# Presentation Production — Audience-to-Decision Deck Workflow

## Purpose
Produce an audience-specific, evidence-backed, professionally designed **presentation artifact** in Figma Slides or Canva, when explicitly requested. This workflow owns orchestration and stage gates, not all specialist reasoning/rendering.

## Entry and scope

**Entry:** User requests a new presentation/deck or major rebuild of a deck from topic, idea, notes, document or analysis. For a local slide edit, individual chart, source verification or story-only outline, route to the matching specialist and stop. Do not create external artifacts for ordinary explanations or reports that do not request a presentation.

**Source status:** draft, not registered or production-enabled until validation. Read `references/artifact-contract.md` and `references/quality-standard.md` only when needed.

## Stage 0 — Capability and privacy preflight
Check what is actually supported by the current runtime: content/Drive/doc retrieval, research, deterministic chart rendering, Figma Slides create/edit, Canva create/edit, deck screenshots, export, reopen/render and file output. Log `AVAILABLE / UNAVAILABLE / UNKNOWN` separately per capability and destination. Do not infer integration from brand name or marketing page. If the user's requested final medium is unsupported, surface the blocker and offer a verified alternative; no phantom deliverables.

Ask permission where sending sensitive user data to an external service would change its exposure. Preserve source provenance and do not use unlicensed company assets.

## Stage 1 — Understand the job, not only the topic (`presentation-brief`)
Extract *what, for whom, why, desired audience decision/behavior, occasion, prior knowledge/objections, duration vs leave-behind, evidence, language, brand, format, privacy*. Infer from supplied context. Ask up to three high-value missing questions only if plausible answers change the strategy or artifact; do not repeat answered questions. Brief `READY` or explicitly `ASSUMPTIONS_VISIBLE` required before full deck authoring. If `BLOCKED_CRITICAL_CONTEXT`, stop expensive generation and ask.

**Gate B — Brief fitness:** can intended reader outcome be stated and evaluated? Does the chosen presentation profile match the communication mode? Keep the answer user's objective, not decorative design, as success metric.

## Stage 2 — Research and disconfirmation (`presentation-evidence-review`)
Reuse existing user sources, canonical research and domain analyses. For missing decision-relevant facts, delegate bounded research to available source-capable tools (e.g. Firecrawl, connected Drive, web); do not search merely to fill slides. Ledger atomic facts and calculations, dates, licenses, contradictions, confidential status and causal uncertainty. No invented figures, charts, case studies, stakeholders or quotations. Tag weak hypotheses explicitly.

**Gate E — Evidence:** unsupported critical claims must be revised, researched, marked provisional or removed before they become assertive headlines.

## Stage 3 — Argue and storyboard (`presentation-storyline`)
Choose the progression using the brief and evidence, not a global fixed agenda. Supported modes:
- board/investment decision and dense executive leave-behind → answer-first, alternatives, quantified rationale, explicit decision/ask and risk;
- transformation/technical → context, operating/architecture reality, options, sequencing, dependencies, decision rights and asks as appropriate;
- persuasive sales/pitch → customer problem, insight, proof, differentiation, offering, action;
- keynote → audience journey, tension, revelation, memorable visual proof, takeaway;
- teaching/workshop → engagement goal, conceptual model, demonstrations, exercises and synthesis.
Use SCQA/pyramid/issue-tree/MECE selectively as useful, not compulsory framework decoration.

Output *ghost deck* of ordered action titles with role, core claim, proof, audience question and transitions. Read titles aloud horizontally; independently attack thesis and strongest alternative. Re-sequence and delete slides that do not advance the intended change.

**Gate S — Story:** titles-only read-through coherent and evidence-bound; unresolved decision-critical assumptions visible. If full deck quality depends on a major user choice, surface that **specific** fork; otherwise proceed without waiting for unnecessary approvals.

## Stage 4 — Design exhibits and visual system (`presentation-exhibit-design`)
Map claim to best information encoding; use `visual-output-design` for local supported visual slot rendering (actual exposed deterministic renderer for numeric charts). Call `report-composer` only when restructuring an already-made report is helpful; it must **not** own deck narrative/creative direction. Select design tokens and per-slide layout; use illustrative image/video provider only when helpful and permitted, with asset/license receipts. Motion must serve meaning and have static fallback.

**Gate V — Integrity:** exhibit proves the point; chart values, units and dates trace; no artificial hierarchy or data. If a required renderer absent mark `BLOCKED_NO_RENDERER`, not satisfied by table or generated drawing.

## Stage 5 — Actual slide authoring (`presentation-slide-authoring`)
Route to Figma Slides or Canva based on user selection and **observed connector capability**. Author native editable slides with semantic slide IDs, readable source lines, citations, speaker notes where meaningful, accessibility and systematic variants. Keep external tool receipts and created file URL. Never call a specification, visual moodboard or export plan a finished presentation.

**Gate A — Native artifact:** URL or file reference from an actual creation action, inspectable deck and explicit editability by component. If blocked, stop with missing capability and user-action requirement; do not assert completion.

## Stage 6 — Critical review and revision (`presentation-deck-review`)
Perform both:
- **Partner/subject-matter red team:** goal, logical flow, strongest counterargument, alternative options, implication, decision/action, confidence and ethics.
- **Design/art director review:** actual slide render montage/high-risk slide screenshots, hierarchy, contrast, alignment, overlap/clipping, meaningful chart grammar, density appropriate to format, typography, accessibility, source line, continuity, consistency and restraint.

Record severity-ranked, slide-local findings and targeted owner (evidence, narrative, exhibit, design). Revise only offending component, re-render and check adjacent/regressed slides. Repeat boundedly; default up to two full review-revision cycles, then escalate persistent major blocker or user trade-off. A nice visual does not offset misleading argument. Never hide critical defect by average score.

**Gate Q — Ready for verification:** no unresolved critical/major defect in the aspects actually reviewed; any unobservable check marked `NOT_RUN`/blocked, not PASS. A second reviewer/model is optional and must be evidenced if claimed.

## Stage 7 — Export and round-trip verification (`presentation-export-verification`)
Delivery package as requested: native editable Figma Slides / Canva design, optional PPTX and/or PDF, source/assumption note, speaker notes if supported. If PPTX/PDF required, export with **actual available tool**, reopen/render target file, compare layout and verify edits/media/fonts. Canva can alter PowerPoint rendering and may not preserve animation/video; Figma Slides can export editable or flattened PPTX and has documented caveats. Record actual feature loss.

**Gate D — Delivery:** only claim format/verifiability backed by a real exported artifact and check. Separate `NATIVE_CREATED`, `RENDER_CHECKED`, `EXPORT_CREATED`, `PPTX_ROUNDTRIP_CHECKED`, `CLIENT_DISPLAY_OBSERVED`. Client-display state remains unknown unless actually checked.

## Final output
Provide:
1. **Audience and decision:** one sentence each; key assumptions.
2. **Story summary:** argument in 3–5 major moves, optional changed thesis and why.
3. **Actual artifact(s):** native URL and any verified output paths; clearly label draft/ready/review-needed and editable limitations.
4. **Quality receipt:** gate states and critical/major unresolved findings; source/rights caveats; what was really inspected.
5. **Next action:** decision from user only when consequential (approval, delivery or missing material).

Do not state "McKinsey/BCG/Deloitte-quality achieved" without a disclosed, independent benchmark. Use `references/artifact-contract.md` for fields/status and `references/quality-standard.md` for review standard.

## Stop conditions
- User wants only an outline/story or chart → stop after requested stage; do not create a deck.
- Critical context absent → ask targeted question, no expensive artifact.
- Required evidence absent → research, qualify or block assertion; no fabricated numeric exhibit.
- Missing connector or export action → mark exact gate blocked and offer one supported alternative.
- Major critique persists after bounded passes → `REVIEW_REQUIRED` with actionable defect, no false quality claim.
- Confidentiality/permission disputed → no external upload until resolved.

## Engineering evidence
This is a **candidate workflow**. Implementation acceptance requires source/static validation, routing + behavior tests, separate external-tool receipts, actual Figma/Canva end-to-end authoring, export round-trip inspection and blind quality comparison before registry/channel production enablement. There is no implied runtime PASS from SKILL.md authoring.
