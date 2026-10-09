---
name: presentation-storyline
description: >
  Design and stress-test a slide deck's audience-specific argument, narrative order and action-title ghost deck before visual authoring. Use when a presentation brief or draft deck needs story structure, executive flow, persuasive narrative or decision logic; do not use only to lay out a given chart.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: draft
  risk: medium
  last_reviewed: "2026-10-09"
---

# Presentation Storyline

## Purpose
Turn a sufficient presentation brief and material claims into a coherent argument the audience can follow and act on. This skill owns the *deck narrative*, not research, rendering or layouts.

## Preconditions
A brief with audience, objective and intended outcome; factual claims have evidence status (supported, provisional or unknown).

## Procedure
1. Name the core audience question, proposed answer (or unresolved thesis) and the strongest credible counterposition.
2. Select fitting logic deliberately: **answer-first / pyramid** for decisions and leave-behinds; **situation→complication→resolution** where context matters; **problem→insight→options→ask** for choices; **journey/demo** for product or keynote; **learn→practice→recall** for teaching. Hybrid only with explicit reason.
3. Build a mutually distinguishable argument tree: conclusion → 2–5 necessary supporting reasons → evidence gaps and potential disconfirmers. MECE is a test for needless overlap, not a ritual that suppresses nuance.
4. Create *ghost deck*: ordered slide `slide_id, role, action_title, proof_needed, audience_question_answered, transition`. Write titles as informative claims **only where warranted**; for agenda, cover and teaching instructions, a label or question can be preferable to a fabricated conclusion.
5. Perform the **titles-only read-through**. Do they advance a coherent argument without needing slide bodies? Remove redundant slides, expose unexplained jumps, show the decision and trade-offs near the moment readers need them.
6. Stress-test: contradictory evidence, omitted alternative, audience objection, non sequitur, recommendation unsupported by evidence, misplaced appendix-level detail, and "why now"/"so what."
7. Set opening, turning points, final requested action and minimum appendix for anticipated questions. Do not default to 20 slides or force an agenda slide.
8. When weak evidence prevents a strong title, mark `PROVISIONAL` or pose a question rather than asserting certainty. Return missing-evidence handoff.

## Decision rules
A beautiful deck with a weak proposition fails. Change the initial premise when evidence warrants it, explain why. Keep the density and pacing appropriate to delivery mode and time.
For board/consulting leave-behind, default to answer-first; for live storytelling, withhold the answer only if that makes comprehension/engagement better without misleading.

## Inputs
Brief, claim/evidence ledger, user hypothesis, constraints and source material.

## Output contract
Return `Storyline{thesis,structure_choice,why_this_structure,governing_question,opening,ghost_deck[],strongest_counterargument,alternatives,required_proof,appendix_plan,closing_ask,revision_decisions}`.
Each ghost deck item has `id,role,action_title,evidence_ids,reader_question,transition,uncertainty`.

## Evidence and uncertainty
No invented market/customer findings; label unsupported claims. Handoff unresolved evidence to `presentation-evidence-review`.

## Failure handling
If no defensible decision/story exists, show an honest provisional narrative plus the smallest research/clarification step; do not fabricate action titles.

## Quality checks
- [ ] Titles-only test passes.
- [ ] Every claim has a planned evidence slot and implication.
- [ ] Sequence serves audience and intended decision, not a canned agenda.
- [ ] Strong counterargument was considered.
