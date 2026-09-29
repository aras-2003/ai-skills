# ai-skills

Reusable AI skills library for repeatable work across projects.

## Principles

- A **Project** stores context and long-lived knowledge.
- A **Skill** stores a reusable method for performing one repeatable task.
- A **Workflow** composes several skills into an end-to-end process.
- An **Agent / bot** owns a role and decides when to invoke skills.
- **Connectors / plugins** provide access to external systems and data.
- **Automations** trigger workflows on a schedule or when a condition is met.
- Use deterministic code/tests for calculations, validation and checks that do not need model judgment.
- Promote a skill only after the procedure is repeatable and useful in real work.

## Repository structure

- `skills/meta/` — skills for designing, writing, validating, testing and releasing other skills
- `skills/core/` — cross-domain skills used everywhere
- `skills/career/` — executive job market and career management
- `skills/product-research/` — product discovery and validation
- `skills/strategy-ea/` — strategy, enterprise architecture and executive work
- `skills/web-design/` — website, visual concept and implementation review
- `skills/ecommerce/` — ecommerce, UX and conversion
- `skills/tender/` — tender / RFP analysis
- `skills/learning/` — Learning OS
- `workflows/` — compositions of skills into end-to-end processes

## Lifecycle

Suggested lifecycle:

`idea -> specification -> authoring -> validation -> test design -> evaluation -> release review -> production`

The detailed process is defined in `workflows/skill-development/WORKFLOW.md`.

Development happens on `main`. Accepted production-ready skills are promoted to `production`.

This branch contains the first catalog proposal only. Individual skills will be specified and polished in later iterations.


## Skill engineering

- Process: `workflows/skill-development/WORKFLOW.md`
- Architecture: `docs/ARCHITECTURE.md`
- Lifecycle: `docs/LIFECYCLE.md`
- Testing: `docs/TESTING.md`
- ChatGPT usage: `docs/GPT-USAGE.md`
- Generated catalog: `CATALOG.md`

Static validation is enforced in GitHub Actions by `.github/workflows/validate-skills.yml`.
