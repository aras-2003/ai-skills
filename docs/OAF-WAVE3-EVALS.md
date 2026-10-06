# OAF Wave 3 — Design Layer Runtime Evaluation

## Goal

Validate the first OAF governance and transformation design layer on Luna, while preserving stronger evidence gates than the diagnostic layers.

The design layer has a higher promotion threshold because plausible prose is not enough: options, mechanisms and sequencing can directly shape high-impact organisational choices.

## Runtime fixture location

In Skills Factory Lab, canonical eval fixtures are packaged into the selected skill/workflow under `references/evals/`. The repository source remains under `evals/`; runtime prompts must use the packaged reference path.

## Test order

### 1. Governance design

Fixture:
`references/evals/case-governance-design-001.md`

Prompt:

> Use the `governance-design` skill on the exact case in `references/evals/case-governance-design-001.md`. Start from the confirmed material decision set. Design the minimum governance needed, preferring direct decision rights, standing rules, asynchronous mechanisms or event-triggered escalation over new forums where they are sufficient. Explicitly identify mechanisms to remove, merge or narrow. Do not invent decision owners.

Pass focus:
- decision-led, not committee-led;
- remove/merge before adding;
- advice vs approval;
- no invented owner;
- evidence/outputs/escalation explicit;
- effectiveness measures defined.

### 2. Transformation blueprint — positive

Fixture:
`references/evals/case-transformation-blueprint-001.md`

Prompt:

> Use the `transformation-blueprint` skill on the exact case in `references/evals/case-transformation-blueprint-001.md`. Convert the agreed federated target direction into an evidence-gated blueprint. Separate 30–90 day mobilisation from longer-term rollout, trace each workstream to the diagnosis and target principles, make capacity/dependencies explicit, preserve unresolved ownership as owner-to-confirm, and define continue/adjust/stop gates. Do not invent a fixed multi-year roadmap.

Pass focus:
- diagnosis-to-workstream traceability;
- bounded mobilisation;
- data-team capacity constraint;
- unresolved ownership preserved;
- pilots/stage gates;
- outcomes vs activity.

### 3. Transformation blueprint — stop condition

Fixture:
`references/evals/case-transformation-blueprint-stop-001.md`

Prompt:

> Use the `transformation-blueprint` skill on the exact stop-condition case in `references/evals/case-transformation-blueprint-stop-001.md`. The user requested a full three-year roadmap. Apply the skill's preconditions and stop conditions strictly.

Pass focus:
- refuses to pretend target state is selected;
- identifies blocking design decisions;
- offers only bounded decision-resolution/mobilisation if justified;
- no invented owners/dates/workstreams.

### 4. Governance redesign workflow

Run after governance-design passes.

Fixture:
`references/evals/case-governance-redesign-001.md`

Prompt:

> Use the `oaf-governance-redesign` workflow on the exact case in `references/evals/case-governance-redesign-001.md`. Reuse the confirmed diagnosis, distinguish decision-rights fixes from governance mechanisms, remove or merge before adding, and design the lightest mechanisms that preserve risk control. Include a bounded pilot and evidence of effectiveness.

Pass focus:
- diagnosis reuse;
- no new enterprise board by default;
- low-threshold funding escalation recognized as partly behavioral/accountability issue;
- exception mechanism bounded;
- operational dependencies delegated where possible;
- measurable governance effectiveness.

### 5. Transformation design workflow

Run after transformation-blueprint positive + stop cases pass.

Fixture:
`references/evals/case-transformation-design-001.md`

Prompt:

> Use the `oaf-transformation-design` workflow on the exact case in `references/evals/case-transformation-design-001.md`. Reuse the selected target direction, define the transformation boundary, sequence foundations and pilots before scale, make the constrained data capacity part of the critical path, define continue/adjust/stop gates, protect service continuity, and limit detailed commitment to the approved 90-day mobilisation horizon.

Pass focus:
- no restart of strategy/design;
- bounded 90-day commitment;
- critical path/capacity;
- reversible pilot logic;
- service continuity;
- longer horizon remains conditional.

## Model comparison

Run Luna first for all cases.

Run Sol comparison only when:
- Luna makes a high-impact final design choice rather than a bounded/pilot choice;
- different plausible governance mechanisms could materially change authority;
- transformation sequencing has material transition economics;
- evidence is contested enough that design selection could change.

Compare decisions and assumptions, not prose quality.

## Promotion threshold

### Specialist design skill
Requires:
- positive case PASS;
- boundary/stop case PASS where relevant;
- no invented authority/ownership;
- explicit trade-offs;
- evidence gates preserved;
- Luna adequate for the validated normal use.

### Design workflow
Requires:
- specialist prerequisites validated;
- diagnosis reused rather than regenerated;
- bounded options/mechanisms/workstreams;
- pilot/reversibility where useful;
- explicit effectiveness evidence;
- Sol comparison if final selection is high impact.

Do not promote a design workflow merely because the output is plausible.
