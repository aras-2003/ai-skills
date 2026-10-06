# OAF Wave 2 — Runtime Evaluation Plan

## Goal

Validate the next OAF specialist layer on Luna before production promotion, then test the first design workflow where diagnosis transitions into target-state options.

## Runtime fixture location

In Skills Factory Lab, canonical eval fixtures are packaged into the selected skill/workflow under `references/evals/`. The repository source remains under `evals/`; runtime prompts must use the packaged reference path.

## Test order

### 1. Global / local model review

Fixture:
`references/evals/case-global-local-001.md`

Prompt:

> Use the `global-local-model-review` skill on the exact case in `references/evals/case-global-local-001.md`. Diagnose the current global/local split. Do not redesign the organisation yet. Explicitly distinguish which decisions or capabilities benefit from global consistency versus local autonomy, identify evidence behind local workarounds, and end with design implications plus the minimum evidence needed before a target model.

Pass focus:
- no centralisation bias;
- global/local placement rationale;
- workarounds treated as evidence;
- mandatory/configurable/advisory standard distinction;
- design implications, not final redesign.

### 2. Decision bottleneck analysis

Fixture:
`references/evals/case-decision-bottleneck-001.md`

Prompt:

> Use the `decision-bottleneck-analysis` skill on the exact 47-day investment decision case in `references/evals/case-decision-bottleneck-001.md`. Reconstruct formal versus actual decision paths, distinguish active decision work from waiting/rework, identify hidden vetoes or duplicate reviews, and propose only the smallest bottleneck-removal experiment. Do not redesign governance.

Pass focus:
- identifies evidence rework delay;
- detects duplicate architecture review;
- treats steering committee as possible shadow step, not proven fact;
- distinguishes adviser from de facto approver;
- avoids generic "remove committees" answer.

### 3. Portfolio health review

Fixture:
`references/evals/case-portfolio-health-001.md`

Prompt:

> Use the `portfolio-health-review` skill on the exact portfolio case in `references/evals/case-portfolio-health-001.md`. Assess the portfolio as a system, not as an average of individual project statuses. Focus on capacity, shared bottlenecks, dependencies, mandatory work, outcome traceability, overlap and stop/reprioritisation behavior. Do not rank initiatives unless the evidence is sufficient.

Pass focus:
- "green projects" do not imply healthy portfolio;
- 128% specialist-capacity commitment treated as system constraint;
- shared bottleneck resources and dependencies surfaced;
- mandatory work separated;
- no false ranking.

### 4. OAF operating-model redesign workflow

Run only after 1–3 are evaluated.

Fixture:
`references/evals/case-operating-model-redesign-001.md`

Prompt:

> Use the `oaf-operating-model-redesign` workflow on the exact case in `references/evals/case-operating-model-redesign-001.md`. Reuse the supplied diagnosis rather than restarting from generic analysis. Define design principles first, then compare 2–3 bounded operating-model options. Test each option against authority/accountability/resources, global/local interfaces, funding, architecture, decision latency and transition risk. Do not design governance forums until a target direction is selected.

Pass focus:
- diagnosis reused;
- options before recommendation;
- no default centralisation;
- explicit trade-offs;
- no premature org chart;
- governance delayed until target direction.

## Evaluation disposition

For each run record:

- PASS / ITERATE / REJECT;
- model used;
- routing correctness;
- evidence discipline;
- scope/boundary adherence;
- incremental value versus parent/general skill;
- corrections required;
- regression expectations discovered.

## Promotion threshold

A specialist skill may move to production when:
- positive case passes;
- boundary case passes;
- missing/conflicting evidence case passes;
- Luna or intended default model class is adequate for normal use;
- material failures are captured as regression expectations.

A design workflow requires a higher bar:
- at least one realistic design case;
- options and trade-offs are explicit;
- diagnosis-to-design gate is preserved;
- no premature structural recommendation;
- stronger-model comparison when the result is materially consequential.
