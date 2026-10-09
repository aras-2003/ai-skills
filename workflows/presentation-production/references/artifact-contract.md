# Presentation OS — Semantic and Evidence Contract (draft)

All IDs are stable within a run. This is a **semantic model**, not a vendor API contract. Provider adapter translation occurs only after capability preflight.

## PresentationBrief
`brief_id, topic, context, audience, audience_prior_knowledge, audience_objections, communication_job, desired_outcome, desired_decision_or_behavior, occasion, delivery_mode{live|leave_behind|workshop|hybrid}, duration_minutes?, slide_budget?, language, source_constraints, brand_constraints, editable_target?, exports_requested[], privacy_level, external_tool_permissions, assumptions[], unanswered_material_questions[], readiness{READY|ASSUMPTIONS_VISIBLE|BLOCKED_CRITICAL_CONTEXT}`.

## Claim / Evidence
`claim_id, statement, epistemic_status{USER_PROVIDED|EXTERNAL_VERIFIED|CANONICAL|DERIVED|HYPOTHESIS|UNKNOWN|CONTRADICTED}, source_locator?, source_as_of?, retrieval_at?, data_fields?, units?, currency?, denominator?, derivation?, comparison_basis?, causal_qualification?, conflicts[], materiality, license_rights?, confidentiality?`.
A user-supplied claim is not automatically externally verified; a contradiction must survive normalization. A numeric transformation is reproducible from a stored input.

## Storyline / Slide
`deck_id, thesis, governing_question, structure_choice, why_choice, alternative_theses[], strongest_counterargument, slides:[{id,section,role,action_title,claim_ids[],reader_question,transition,proof_required[],exhibit_specs[],speaker_notes?,source_line?,layout_id?,alternative_text?,output_state}]`.
`action_title` is an evidence-anchored assertion on analytic slides; title/agenda/teaching slides may legitimately use labels/questions.

## Exhibit
`exhibit_id, slide_id, visual_job, visual_type, supported_data, provenance, units, as_of, uncertainty, annotations, deterministic_renderer, asset_id?, alt_text, editability{EDITABLE_NATIVE|EDITABLE_PARTIAL|RASTER_ASSET|FLATTENED|UNKNOWN}, capability_status{AVAILABLE|UNAVAILABLE|UNKNOWN}, execution_status{NOT_ATTEMPTED|BLOCKED_NO_RENDERER|PAYLOAD_RENDERED|FAIL_RENDERER_INVOCATION}`.

## Artifact / QA receipt
`run_id, source_revision, workflow_version, authoring_tool, connected_tool_capabilities[], native_file_url?, native_file_id?, slide_ids[], asset_manifest[], tool_receipts[], render_receipts[], export_receipts[], roundtrip_checks[], review_findings[], revision_history[], privacy_decisions[], unverified_features[], overall_status`.
Track the following **independently**: `BRIEF_READY`, `EVIDENCE_SUPPORTED`, `STORY_APPROVED`, `EXHIBITS_READY`, `NATIVE_CREATED`, `RENDER_CHECKED`, `QA_APPROVED`, `EXPORT_CREATED`, `PPTX_ROUNDTRIP_CHECKED`, `CLIENT_DISPLAY_OBSERVED`.
States per gate: `NOT_RUN|PASS|FAIL|BLOCKED|UNVERIFIED`; runtime PASS only from observed run receipts. `UNVERIFIED` describes missing evidence after execution, not an unavailable tool.
Use artifact URLs only when returned by actual creation; user-supplied URLs and mock URLs do not count. `client_display` is `NOT_OBSERVABLE` unless a separate client observation actually occurred.

## Responsibility rules
- Brief owns audience and purpose.
- Storyline owns argumentative flow and ghost deck.
- Evidence owns provenance and uncertainty.
- Exhibit owns semantic mapping and calls existing visual-output-design.
- Authoring owns vendor actions and editability implementation.
- Review owns editorial/visual red-team and per-slide corrections.
- Export verification owns media round-trip and delivery receipts.
No stage may silently overrule source truth from an earlier stage. Material conclusion changes must propagate upstream and be documented.
