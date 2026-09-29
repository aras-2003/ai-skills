# AI Skills Architecture

## 1. Objective

Build a portable, testable library of reusable AI procedures that can be used by agents across projects without duplicating project context.

The repository is a **capability library**, not a prompt dump.

A good skill:
- solves one repeatable class of task;
- has explicit trigger conditions;
- defines inputs and outputs;
- contains a stable procedure;
- separates judgment from deterministic logic;
- can be tested independently;
- composes cleanly into workflows.

## 2. Conceptual model

```
USER GOAL
   |
   v
PROJECT / AGENT CONTEXT
   |
   v
ROUTER
   |
   +--> SKILL A -----+
   |                 |
   +--> SKILL B -----+--> WORKFLOW --> QUALITY GATE --> OUTPUT / ACTION
   |                 |
   +--> SKILL C -----+
          |
          +--> tools/connectors
          +--> scripts
          +--> references
          +--> templates/assets
```

### Responsibility boundaries

| Layer | Owns | Must not own |
|---|---|---|
| Project | long-lived context, goals, files, project-specific constraints | generic reusable procedure |
| Agent / bot | role, responsibilities, routing, tool authority | detailed domain procedure duplicated across agents |
| Skill | reusable method for one task | global personal context or orchestration of unrelated tasks |
| Workflow | sequence, gates, branching, human checkpoints | deep instructions that belong in individual skills |
| Connector / tool | external data and actions | reasoning policy |
| Script | deterministic calculation, parsing, validation, transformation | judgment-heavy reasoning |
| Automation | trigger and recurrence | business logic duplicated from workflows |
| Quality gate | acceptance criteria and release decision | producing the substantive work itself |

## 3. Repository architecture

```
ai-skills/
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── LIFECYCLE.md
│   ├── TESTING.md
│   └── CATALOG-BENCHMARKS.md
├── templates/
│   └── skill-template/
│       ├── SKILL.md
│       ├── tests/
│       │   └── cases.yaml
│       ├── references/
│       ├── scripts/
│       └── assets/
├── skills/
│   ├── core/
│   ├── career/
│   ├── product-research/
│   ├── strategy-ea/
│   ├── web-design/
│   ├── ecommerce/
│   ├── tender/
│   └── learning/
├── workflows/
│   ├── README.md
│   └── <workflow-name>/
│       └── WORKFLOW.md
└── scripts/
    ├── validate_catalog.py
    ├── validate_skills.py
    └── generate_catalog.py
```

### Skill package

Each production skill should be self-contained:

```
skills/<domain>/<skill-name>/
├── SKILL.md          # required
├── tests/            # expected behavior and edge cases
├── references/       # only material needed while executing the skill
├── scripts/          # deterministic helpers
└── assets/           # templates or output artifacts
```

Do not create empty folders. Add optional directories only when they contain useful material.

## 4. SKILL.md contract

Use the open Agent Skills convention so the same library can be reused across compatible runtimes.

Minimum frontmatter:

```yaml
---
name: role-fit-analysis
description: >
  Evaluate a senior or executive job opportunity against the target role profile,
  mandate, scope, career trajectory and constraints. Use after offer validity has
  been confirmed and before expensive company research or CV tailoring.
---
```

Recommended body:

```markdown
# Role Fit Analysis

## Purpose
## Use when
## Do not use when
## Inputs
## Preconditions
## Procedure
## Decision rules
## Output contract
## Evidence requirements
## Failure / uncertainty handling
## Quality checks
## Examples
## References
```

### Design rule: description is routing metadata

The description must answer:
1. What task does this skill perform?
2. When should an agent invoke it?
3. What nearby tasks should route elsewhere?

A vague description such as "helps with careers" is a routing bug.

## 5. Skill granularity

Prefer a skill when all are true:
- the task repeats;
- the method is stable enough to describe;
- quality improves when the same procedure is reused;
- the task has a meaningful independent output;
- it can be tested separately.

Keep logic in the project/agent when:
- it is unique to one project;
- it changes constantly;
- it is mostly personal context;
- it is a one-off instruction.

Use a workflow rather than one giant skill when:
- there are multiple independent stages;
- stages have stop conditions;
- only some cases need deeper analysis;
- stages can be reused elsewhere.

## 6. Three classes of skills

### A. Reasoning skills
Examples: `red-team-review`, `architecture-review`, `role-fit-analysis`.

Primary content: decision process, evidence rules, trade-offs, output schema.

### B. Execution skills
Examples: `cv-tailoring`, `rfp-extraction`, `implementation-brief`.

Primary content: procedural steps, tools, templates, transformations.

### C. Control skills
Examples: `evidence-validator`, `quality-gate`, `change-review`.

Primary content: acceptance criteria, verification, regression and uncertainty handling.

A mature workflow usually combines all three.

## 7. Routing architecture

Routing should happen in this order:

1. Identify user intent.
2. Identify domain.
3. Check preconditions.
4. Select the smallest skill that fully addresses the task.
5. Load only the supporting references needed by that skill.
6. Execute.
7. Run an appropriate control skill if risk/impact warrants it.
8. Escalate to a workflow only if multiple stages are actually needed.

Avoid loading the whole library into context.

## 8. Progressive-depth architecture

Expensive work should happen only after cheap gates pass.

Example:

```
job-discovery
  -> job-validity-check
     -> role-fit-analysis
        -> [STOP if weak]
        -> company-context-research
           -> cv-gap-analysis
              -> cv-tailoring
```

This principle applies across domains:
- product validation before sourcing;
- eligibility before tender deep dive;
- concept approval before implementation;
- evidence validation before executive recommendation.

## 9. Deterministic vs model logic

Use code/scripts for:
- scoring arithmetic;
- thresholds;
- schema validation;
- duplicate detection;
- deterministic parsing;
- file checks;
- regression tests;
- formatting where exactness matters.

Use model reasoning for:
- interpretation;
- prioritization;
- ambiguity;
- qualitative trade-offs;
- counterarguments;
- executive synthesis;
- semantic matching.

Rule: **LLM interprets; code calculates and validates.**

## 10. Context economy

Use progressive disclosure:
- the agent first sees only skill metadata;
- it loads `SKILL.md` when relevant;
- it loads references/scripts only when the procedure calls for them.

Do not embed large research packs or project files directly in SKILL.md.

## 11. Portability

Keep skill content independent from one model whenever possible.

Runtime-specific instructions should live in a small adapter section or runtime-specific helper, not in the core procedure.

Target portability:
- ChatGPT / OpenAI agent environments
- Codex
- Claude / Claude Code
- other Agent Skills-compatible runtimes

## 12. Versioning model

Recommended metadata:

```yaml
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: draft
  risk: medium
  last_reviewed: 2026-09-29
```

Maturity:
- `draft` — usable for experiments;
- `candidate` — tested on representative cases;
- `production` — accepted and stable;
- `deprecated` — retained only for migration/history.

Version the skill when its behavior contract changes, not for typo-only edits.

## 13. Human decision points

Human approval is required when a workflow:
- commits money;
- publishes externally;
- sends messages on behalf of the user;
- changes production systems;
- makes irreversible repository changes;
- relies on materially uncertain evidence for a high-impact decision.

The workflow may prepare the action, but the approval boundary should be explicit.
