# OAF / Organisational Architecture Framework

OAF connects strategy, operating model, decision architecture, enterprise architecture, portfolio/execution and evidence feedback. It is a thinking and decision framework, not one monolithic prompt.

Core loop:

`Direction -> Operating Model -> Decisions -> Architecture -> Portfolio/Execution -> Evidence -> next decision`

## Current implemented source skills

### Production maturity
- `operating-model-review`
- `global-local-model-review`
- `decision-rights-review`
- `decision-bottleneck-analysis`
- `governance-design`
- `architecture-review`
- `capability-map-review`
- `capability-gap-analysis`
- `portfolio-prioritization`
- `portfolio-health-review`
- `transformation-blueprint`
- `evidence-loop-review`

### Candidate maturity
- `strategy-to-execution-diagnostic`
- `organizational-interface-review`
- `kpi-quality-review`

Source presence does not equal production runtime availability. Candidate skills may appear in Lab while being absent from the production plugin.

## Current workflows

Production runtime workflows:
- `oaf-health-check` — selective cross-domain diagnosis.
- `oaf-operating-model-redesign` — evidence-gated bounded redesign.
- `oaf-governance-redesign` — decision-led governance redesign.
- `oaf-enterprise-architecture-review` — evidence-gated enterprise architecture review.
- `oaf-transformation-design` — bounded transformation mobilisation/sequencing.
- `oaf-enterprise-change-review` — selective end-to-end orchestration.

Candidate workflow:
- `oaf-strategy-execution-reset`

## Routing principle

Prefer the narrowest production capability that matches the problem.

`symptom/problem -> narrow diagnostic -> specialist evidence -> cross-domain synthesis when needed -> design only after evidence gate`

Examples in the current production catalog:
- slow/unclear decisions -> `decision-rights-review`;
- repeated escalations/latency -> `decision-bottleneck-analysis` when the problem is decision flow;
- global/local tension -> `global-local-model-review`;
- cross-unit handoff/accountability/interface symptoms -> `operating-model-review` in production;
- initiative overload -> `portfolio-health-review`, then `portfolio-prioritization` when comparable evidence exists;
- reporting without action -> `evidence-loop-review`.

`organizational-interface-review` is currently candidate maturity. Do not assume a production session can invoke it. If an explicitly invoked workflow depends on it and it is unavailable, disclose the limitation and narrow the conclusion rather than simulating the specialist.

## Evidence and confidence discipline

For OAF diagnosis:
- separate observed symptoms/direct evidence from possible causes;
- attach confidence to a specific claim and its supporting evidence;
- causal mechanisms remain hypotheses when initiative records, decision traces, interface traces or equivalent evidence are missing;
- do not label an unverified causal hypothesis as a confirmed critical gap;
- directly evidenced mechanisms may still justify high confidence; uncertainty is not forced everywhere.

The preferred sequence is:

`evidence -> diagnosis -> design implication -> design choice -> pilot -> evidence loop`

Not:

`symptom -> best-practice redesign`

## Current runtime finding status

Two real production fallback runs against behavior source `ff012e494f5b2f71803f850d71d20f54a3315e2b` are retained as historical FAIL evidence:
- strategy fallback: overconfident causal diagnosis from symptom-only evidence;
- interface fallback: the old test mislabeled a natural prompt as explicit workflow execution.

R2 produced one explicit-interface PASS and two residual FAIL findings. Behavior was revised again under source identity `cde46f59c20a0d4313528185e5df079335633b10` and R3 retained four PASS results and one residual strategy FAIL. The health-check synthesis contract was narrowed again under behavior source `28a7681cf024bb7aaad7a979e7ce7253139d5bd4`; active campaign `runtime-validation-2026-10-r4` requires only a focused strategy fallback retest.

See:
- `workflows/runtime-registry.yaml`
- `evals/campaigns/runtime-validation-2026-10-r4/RUNBOOK.md`
- `docs/MODEL-ROUTING.md`
- `release/production-readiness.yaml`
