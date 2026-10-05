# ai-skills

Reusable AI capability library for repeatable work across projects.

## Operating model

- A **Project** stores long-lived context and project-specific constraints.
- A **Skill** stores one reusable procedure.
- A **Workflow** composes skills with gates and stop conditions.
- **Scripts** calculate and validate deterministic logic.
- **Runtime packages** expose a maturity/channel-specific subset of source capabilities.
- GitHub source is authoritative; generated plugins/ZIPs are build outputs, not editing targets.

Rule: **LLM interprets; code calculates and validates.**

## Visual catalog

Browse skills by domain and maturity in the [Arek AI Skills catalog](https://aras-2003.github.io/ai-skills/). The catalog is generated from the source metadata in `SKILL.md`.

## Expansion roadmap

The [AI Skills expansion roadmap](docs/roadmap/2026-10-05/README.md) preserves the architecture analysis, proposed flows and 72-task development backlog. Start there before implementing expansion work; task state is maintained in its `BACKLOG.json`.

## Current source domains

- `skills/career/` — executive role/company/CV/interview workflows
- `skills/commerce/` — product discovery, demand, competition, economics, sourcing, acquisition and regulatory screening
- `skills/oaf/` — Organisational Architecture Framework specialists
- `skills/meta/` — skill engineering/control skills
- `skills/investing/` — personal Investment OS: market attention, research, portfolio, sizing, monitoring and learning
- `skills/core/`, `skills/ecommerce/`, `skills/learning/`, `skills/product-research/`, `skills/strategy-ea/`, `skills/tender/`, `skills/web-design/` — additional source domains at mixed maturity

The source tree is not the runtime allow-list.

Current implemented source skills: **54**, across five implemented domains: `career`, `commerce`, `investing`, `meta` and `oaf`. The source tree contains 17 workflow definitions. Other domain README files describe design/backlog intent unless stated otherwise.

## Branches, maturity and installed capability

These are separate concepts:

- `main` — development source branch.
- `production` — promoted source/release branch. It can contain source components of mixed maturity because branch history is promoted as a repository change set.
- `metadata.maturity` — component-level lifecycle state used by builders.
- generated `capabilities.json` — actual capability availability for a built channel/version.
- generated `release-manifest.json` — package version, source revision and provenance.
- `CATALOG.md` — generated source catalog, useful for discovery but not a substitute for a channel manifest.

Do not infer installed availability from branch membership alone.

## Delivery channels

Production builders currently support:

1. **Plugin channel** — production skills plus workflow entrypoints allowed by `workflows/runtime-registry.yaml`.
2. **Lab channel** — isolated evaluation package containing candidate targets, required production dependencies, executor-only eval inputs, and explicitly allow-listed draft test targets.
3. **ChatGPT ZIP channel** — individual production skill ZIPs. Workflow availability is declared explicitly in the channel manifest; unsupported workflows are not silently implied.

Runtime packages use an allow-list: `SKILL.md`, required `references/`, `scripts/` and `assets/`. Test definitions, eval summaries and evaluator rubrics stay outside production runtime payloads.

## Lifecycle

`idea -> specification -> authoring -> static validation -> isolated evaluation -> candidate -> real-use evidence -> release review -> production -> monitor`

Details:
- `workflows/skill-development/WORKFLOW.md`
- `docs/LIFECYCLE.md`
- `docs/TESTING.md`
- `docs/RUNTIME-EVALS.md`
- `release/production-readiness.yaml`

A narrative historical PASS is not a current-version runtime receipt. When runtime evidence is unavailable, record `NOT_RUN`/pending rather than assuming success.

Current runtime validation campaign: `runtime-validation-2026-10-r16`, pinned to behavior source `89db15ef94cf38a35117ec02b8c60928ef72654d`, with 44 core cases plus 3 supplemental routing regressions. R1–R15 remain historical and bound to their original source revisions. R16 validates inline report visuals and bounded research-state persistence; it does not evaluate the three draft skill-lifecycle test targets included in Lab 0.32.0. Static/package checks do not imply runtime PASS.

## Quality and build

Required PR validation is defined in `.github/workflows/validate-skills.yml` and covers:
- source/static contracts;
- validator mutation tests;
- eval input/rubric isolation;
- active runtime campaign definition, imported evidence validation and offline campaign regressions;
- package safety/reproducibility;
- catalog freshness;
- production plugin, Lab and ChatGPT ZIP builds plus artifact validation;
- deterministic Commerce unit-economics tests.

Generated artifacts are built atomically and include source provenance.

## Key docs

- Architecture: `docs/ARCHITECTURE.md`
- Lifecycle: `docs/LIFECYCLE.md`
- Testing: `docs/TESTING.md`
- Runtime evals: `docs/RUNTIME-EVALS.md`
- Active R16 runbook: `evals/campaigns/runtime-validation-2026-10-r16/RUNBOOK.md`
- Channel usage: `docs/GPT-USAGE.md`
- Branch-rules proposal: `docs/GITHUB-BRANCH-RULES-PROPOSAL.md`
- Distribution/license decision: `docs/DISTRIBUTION-LICENSE-DECISION.md`
- Generated catalog: `CATALOG.md`
