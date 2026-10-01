# Runtime Eval Backlog

Non-blocking quality observations captured from real runtime evaluations. Items here do not change historical case status and are not implied to be fixed by the current PR unless explicitly referenced by a later change.

## 2026-10-01 — R3 residual observations

### OAF routing first-choice precision

Evidence: `oaf-interface-natural-pl` R3 PASS.

The executor initially selected `decision-bottleneck-analysis`, then self-corrected after reading its installed boundary and selected `operating-model-review` before the final diagnosis.

Backlog:
- improve first-choice routing precision for mixed interface/accountability/capacity prompts;
- preserve the currently correct self-correction behavior;
- do not broaden the operating-model contract merely to force first-token routing.

### Pilot interpretation calibration

Evidence: `oaf-interface-natural-pl` R3 PASS.

The output suggested that lower escalation/waiting after a bundled pilot would identify interface/mandate as the cause. A bundled intervention can improve outcomes without isolating which mechanism caused the improvement.

Backlog:
- calibrate causal interpretation of multi-variable pilots;
- distinguish experiment success from mechanism identification.

### Decision-rights example-table factuality

Evidence: `oaf-decision-rights-natural-pl` R3 PASS.

Some illustrative executor/participant roles were populated without organisation-specific evidence or consistently marking them as hypothetical.

Backlog:
- ensure example decision-rights tables label unsupplied organisation-specific roles as illustrative/hypothetical;
- keep actual owner/authority claims evidence-bound.

These observations are not frozen-routing assertion failures and do not alter the R3 PASS statuses.

## 2026-10-01 — R6 targeted PASS observations

Evidence: `fallback-strategy-production-002` R6 PASS on `oaf-health-check 1.5.0`, behavior source `a924f3ba9fe964ff3aeaa2e5570b7a718d29d38c`.

### Epistemic status taxonomy consistency

The runtime output used a review-state limitation label even though the workflow's enumerated epistemic statuses are `observed`, `supported`, `hypothesis` and `implication`.

Backlog:
- decide whether reviewer-state limitation should become a first-class status or remain metadata/evidence rationale;
- avoid a runtime behavior change solely to tidy taxonomy while the meaning remains explicit and correctly scoped.

### Domain synthesis wording precision

The executive synthesis used `supported / medium` wording across strategy execution and evidence-loop domains and referenced limited traceability. In context this was appropriately bounded by explicit causal uncertainty, but wording could more sharply distinguish the observed roadmap/outcome disconnect from broader organisational traceability.

Backlog:
- tighten domain-level synthesis wording when one observed symptom motivates review of multiple domains;
- do not treat domain relevance as proof of a causal mechanism.

These are nonblocking quality observations and do not change the frozen R6 PASS.

