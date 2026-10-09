# Analysis → Communication Artifacts: Cross-OS Contract (candidate v0.1)

## Decision and ownership

**Source-domain OS** (Strategy, OAF, Investing, Commerce or other subject specialist) owns **analytical truth, substantive options, recommendations, uncertainty and approvals**. **Report OS** and **Presentation OS** are separate consumers that structure and render communication artifacts. Output medium never authorizes the downstream creator to alter analytical conclusions. The user may request both deliverables, one, or only an answer.

This is an **interoperability design proposal**, not an installed global schema, database, automatic runtime router or published API. Finalize names and compatibility with planned STR-16 and actual domain stores before implementing a shared adapter.

## Minimal versioned handoff

`DomainResult{`
- `domain, source_workflow?, result_id, source_revision, analysis_as_of, scope, governing_question, audience_constraints?`
- `findings:[{finding_id, claim, epistemic_status, evidence_ids[], as_of?, units?, comparator?, uncertainty?}]`
- `evidence:[{evidence_id, source_locator, obtained_at?, publication_date?, license?, confidentiality?, transform?}]`
- `options:[{option_id, finding_ids[], tradeoffs[], feasibility?, choice_state{HYPOTHESIS|PROPOSED|RECOMMENDED|USER_APPROVED|REJECTED|UNKNOWN}}]` when domain supports options
- `recommendations:[{recommendation_id, option_ids[], finding_ids[], rationale, status, owner?}]` where applicable
- `limitations[], contradictions[], method_notes?, domain_validation_state{PASS|FAIL|NOT_RUN|BLOCKED|UNVERIFIED}, revision_history[]`
`}`.

All downstream outputs link claim/exhibit/section/slide to **stable IDs and version**. Domain pack is *read-only* for report/deck generation. A detected material conflict returns `UPSTREAM_REVIEW_REQUIRED{source_id, evidence, proposed_change}`; only the domain owner may adopt a substantive correction. Do not silently elevate `HYPOTHESIS` into `RECOMMENDED`, user-provided into independently verified, or a rhetorical claim into a fact. User can approve a communication artifact without approving an underlying recommendation.

## Media-specific output models

| Concern | Report OS | Presentation OS | Existing composer/visual |
| --- | --- | --- | --- |
| User goal | Sustained reading, traceable depth, decision record | Live narration or slide-based decision support | Chat-native compact/structured reporting |
| Plan | Sections, subheads, evidence distribution, appendices | Ghost deck, action titles, slide roles/transitions | Inline report sections, visual slots |
| Native artifact | Editable DOCX / optional Google Docs; PDF as consumption output | Figma Slides / Canva native deck; PPTX where supported | Native chat surface |
| Quality review | Page breaks, table splitting, TOC, cross-references, citations, font/links, full-page readability | Slide design, montage, story pacing, editability, PPTX export | Actual inline-rendered evidence |
| Runtime proof | Create/open/render DOCX and PDF, page-by-page inspection, content/links parity receipts | Native deck creation, screenshots, PPTX reopen receipts | Real emitted native visual payload |
| Non-goals | No deck-by-default, no reanalysis | No long document-by-default, no strategy design | No implicit external artifact |

`report-composer` remains the existing reusable semantic report composition layer, especially **for chat**. Its external-artifact option is not evidence that page-layout, native DOCX creation, or PDF round-trip already work. `visual-output-design` owns supported chart/diagram encoding, not domain analysis or chapter/slide planning.

## Intent router

1. **Analyze**: request is for solving/evaluating subject matter → source domain owns it. Respond directly or use `report-composer` when user did not ask for a file.
2. **Report**: explicit substantial written/document deliverable → Report OS. Use supplied/canonical domain result, delegating missing subject analysis only when user actually requests or it is needed to answer.
3. **Presentation**: explicit deck/slides/live talk → Presentation OS, same upstream governance.
4. **Both**: run/consume a single compatible, versioned source result; build document and deck **independently** with their respective profiles, stage gates, and QA. Never report combined PASS when one output is blocked.
5. **Narrow**: a short executive decision memo → PRO-04/report-composer; an article → Writing; an existing deck slide edit → deck specialist; one chart → visual-output-design. Do not start a full long-document or slide production pipeline.

## Capability, permissions and evidence

Preflight current runtime **per capability**, not product marketing: source retrieval, text edits, DOCX build, PDF render/export, Google Docs, Canva presentation create/edit, Figma Slides, charts, upload/privacy, reopen/inspection. `CONNECTED` for one read action does **not** imply `NATIVE_CREATED`, `EDITABLE` or `EXPORT_VERIFIED`. External transfer of private sources requires applicable authorization. If a necessary action is unavailable, return `BLOCKED` or `NOT_RUN` with missing prerequisite, no fictitious URL/file.

Release requires **separate subject-domain quality** and **medium-specific communication/artifact quality** receipts. No style critique may substitute for Strategy challenge, and no analytically rigorous result constitutes a finished DOCX or deck.
