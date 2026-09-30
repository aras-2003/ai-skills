# OAF Health Check Workflow

## Purpose

Run a selective organisational architecture diagnostic across OAF domains without turning OAF into one giant skill.

## Entry criteria

Use when the user asks for a broad diagnosis of how strategy, organisation, decisions, architecture and execution fit together.

Do not run every skill by default.

## Stage 1 — Frame the decision problem

Clarify:
- what outcome is failing or at risk;
- where symptoms appear;
- what evidence exists;
- what decision the diagnostic must support.

If the request is already narrow, route directly to the relevant OAF skill and stop.

## Stage 2 — Select diagnostic domains

Route only where evidence suggests a material issue:

- Strategy disconnected from execution -> `strategy-to-execution-diagnostic`
- Central/local or structural/interface problems -> `operating-model-review`
- Slow/unclear decisions -> `decision-rights-review`
- Excessive/weak governance -> `governance-design` after diagnosis
- Capability/organisation/technology misalignment -> `architecture-review`
- Capability-map quality/usefulness issue -> `capability-map-review`
- Initiative overload or prioritisation conflict -> `portfolio-prioritization`
- Reporting without learning/adaptation -> `evidence-loop-review`

## Stage 3 — Diagnose before design

Run diagnostic/review skills before design skills.

Do not use `governance-design` or `transformation-blueprint` until the relevant problem is sufficiently evidenced.

## Stage 4 — Cross-domain synthesis

For each finding record:
- evidence;
- OAF domain;
- structural cause;
- consequence;
- dependency on other findings;
- uncertainty.

Look for reinforcing loops, for example:
- unclear strategy -> overloaded portfolio;
- unclear decision rights -> governance proliferation;
- fragmented operating model -> duplicate technology/capabilities;
- weak evidence loop -> repeated low-quality prioritisation.

## Stage 5 — Prioritise structural changes

Separate:
1. critical blockers;
2. foundational changes;
3. local improvements;
4. unresolved questions.

Avoid producing a long transformation backlog from weak evidence.

## Stage 6 — Design only what is ready

When diagnosis is sufficient:
- use `governance-design` for governance-system changes;
- use `transformation-blueprint` for cross-domain sequencing and mobilisation.

## Output contract

### Executive diagnosis
3–5 sentences on what is structurally wrong and why it matters.

### OAF heatmap
| Domain | Status | Evidence confidence | Main issue | Consequence |
|---|---|---|---|---|

Use only domains actually reviewed.

### Cross-domain causes
List the few structural causes connecting multiple symptoms.

### Critical unknowns
Questions whose answers could materially change the diagnosis.

### Recommended next action
Route to the next OAF skill/design step, or stop if evidence is insufficient.

## Stop conditions

Stop when:
- the decision problem is narrow enough for one specialist skill;
- evidence is insufficient for cross-domain claims;
- additional OAF domains would add breadth but not decision value.
