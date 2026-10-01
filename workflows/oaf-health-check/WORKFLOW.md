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
- observed symptom or direct evidence;
- OAF domain;
- possible structural cause;
- consequence;
- dependency on other findings;
- claim-level confidence and the evidence that supports that confidence.

Keep observation and causality separate:
- an observation must be a direct paraphrase of a concrete statement in the input or of evidence actually collected during the review;
- do not add an unobserved mechanism, missing owner, process failure, absence claim or downstream effect inside an observation;
- symptoms stated in the input may be treated as observed for the purpose of the review;
- a cause is not observed merely because it is a plausible explanation of those symptoms;
- without relevant initiative records, decision traces, review-cycle evidence, interface traces or equivalent data, causal explanations remain hypotheses;
- do not label an unverified causal hypothesis as a confirmed critical gap;
- each claim has exactly one epistemic type: observed/supported or hypothesis/implication; if a sentence or table row contains both, split it into separate claims;
- confidence belongs to one atomic claim and its evidence, not to a compound "observation + hypothesis", an entire domain or section;
- high confidence is appropriate when the relevant mechanism is directly evidenced, not merely because the symptom is severe or common;
- downstream consequences are separate claims: unless the consequence is stated in the input or directly evidenced, label it as an implication/hypothesis with its own confidence;
- inability to link a roadmap to measurable strategic outcomes supports only that linkage symptom; by itself it does not establish that an evidence-to-action loop fails, lacks an owner, or that decision ownership is missing.

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

When the input contains symptoms but not mechanism evidence, the next step is a bounded evidence sample that can discriminate between the leading hypotheses. Select a small representative set of recent initiatives, priority changes, decisions, reviews or interface events and inspect only the evidence needed to test the suspected mechanism.

Do not require complete initiative cards, decision maps or action decisions for the whole portfolio before identifying the mechanism. A bounded sample is a test of hypotheses, not proof that the sample will be sufficient. State what the sample can discriminate, what result would support or weaken each hypothesis, and expand only if the evidence remains ambiguous.

Avoid producing a long transformation backlog from weak evidence.

## Stage 6 — Design only what is ready

When diagnosis is sufficient:
- use `governance-design` for governance-system changes;
- use `transformation-blueprint` for cross-domain sequencing and mobilisation.

## Output contract

### Executive diagnosis
3–5 sentences on what is structurally wrong and why it matters.

### OAF heatmap
| Domain | Status | Finding type | Evidence confidence | Main issue | Consequence |
|---|---|---|---|---|---|

Use only domains actually reviewed. Use `observed` for supported findings and `hypothesis` for plausible causes that still need evidence. Do not use compound labels such as `observed + hypothesis`; split them into separate rows/claims with separate confidence. A hypothesis may be material, but must not be presented as a confirmed critical gap.

### Cross-domain causes
List the few structural causes connecting multiple symptoms. Mark each as observed/supported or hypothesis and state what evidence would raise or lower confidence.

### Critical unknowns
Questions whose answers could materially change the diagnosis.

### Recommended next action
Route to the next OAF skill/design step, or stop if evidence is insufficient. For symptom-only diagnosis, prefer the smallest representative evidence sample that can test the leading hypotheses before portfolio-wide process or action changes.

## Stop conditions

Stop when:
- the decision problem is narrow enough for one specialist skill;
- evidence is insufficient for cross-domain claims;
- additional OAF domains would add breadth but not decision value.
