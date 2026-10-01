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

## Current source domains

- `skills/career/` — executive role/company/CV/interview workflows
- `skills/commerce/` — product discovery, demand, competition, economics, sourcing, acquisition and regulatory screening
- `skills/oaf/` — Organisational Architecture Framework specialists
- `skills/meta/` — skill engineering/control skills
- `skills/investing/` — personal Investment OS: market attention, research, portfolio, sizing, monitoring and learning
- `skills/core/`, `skills/ecommerce/`, `skills/learning/`, `skills/product-research/`, `skills/strategy-ea/`, `skills/tender/`, `skills/web-design/` — additional source domains at mixed maturity

The source tree is not the runtime allow-list.

Current implemented source skills: **52**. Only `career`, `commerce`, `meta` and `oaf` currently contain `SKILL.md` implementations. The other domain README files describe design/backlog intent unless stated otherwise.

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
2. **Lab channel** — isolated evaluation package containing candidate targets plus required production dependencies and executor-only eval inputs.
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

Current runtime follow-up campaign on this branch: `runtime-validation-2026-10-r7`, behavior source `008c9944cf3a8bc3e2d7231a4862aaf00e722889`, core count 38. Historical R1 and R2 runtime receipts remain bound to their original behavior sources and statuses. R3 is frozen historical evidence. R4 remains historical FAIL evidence for the strategy fallback. R5 remains historical FAIL evidence for the strategy fallback. R6 remains historical evidence. R7 is the consolidated personal-beta baseline after AIS hardening and Investing OS promotion. Investing runtime fixtures begin as NOT_RUN; green static/package gates permit personal use but do not imply runtime PASS.

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
- Active R6 runbook: `evals/campaigns/runtime-validation-2026-10-r6/RUNBOOK.md`
- Channel usage: `docs/GPT-USAGE.md`
- Branch-rules proposal: `docs/GITHUB-BRANCH-RULES-PROPOSAL.md`
- Distribution/license decision: `docs/DISTRIBUTION-LICENSE-DECISION.md`
- Generated catalog: `CATALOG.md`
