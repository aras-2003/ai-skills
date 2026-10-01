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
