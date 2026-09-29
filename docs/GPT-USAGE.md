# Efficient use of ai-skills in ChatGPT

## Current ChatGPT availability

As of 2026-09-29, OpenAI documents native ChatGPT Skills for eligible Business, Enterprise, Healthcare and Edu workspaces. Availability differs by plan and surface.

For ChatGPT Plus, treat this Git repository as the canonical skills source and use the **Project + router + on-demand GitHub loading** pattern below. If native Skills become available on the account later, production skills can be installed selectively without changing their core design.

## Recommended architecture for ChatGPT Plus

```
ChatGPT Project
   |
   +-- project context / files / instructions
   |
   +-- small skill router
          |
          +-- CATALOG.md metadata
          |
          +-- fetch one production SKILL.md from GitHub only when needed
                 |
                 +-- optional references/scripts only when required
```

Do not load the entire repository into every conversation.

## Source of truth

- `main` = development/candidate skills.
- `production` = accepted skills only.
- `CATALOG.md` = lightweight discovery metadata.
- Individual `SKILL.md` files = execution instructions.
- GitHub remains canonical; avoid manually diverging copies in ChatGPT.

## Project routing pattern

Each ChatGPT Project should contain a short router instruction, not full skill bodies.

Example:

```text
Use reusable procedures from aras-2003/ai-skills when they materially improve a repeatable task.

Source:
- production branch for normal work
- main only when explicitly testing a candidate skill

Routing:
1. Identify whether the request matches a listed production skill.
2. Prefer the smallest relevant skill; do not load unrelated skills.
3. Fetch that SKILL.md from GitHub only when needed.
4. Load references/scripts only if the skill procedure requires them.
5. Project instructions and current user intent provide context; the skill provides method.
6. For high-impact decisions, apply an appropriate control skill such as evidence-validator or red-team-review when justified.
7. Do not run meta-skills during normal domain work unless the task is creating or changing a skill.
```

## Recommended project-to-skill mapping

### Career project
Router allow-list:
- job-validity-check
- role-fit-analysis
- career-trajectory-check
- company-context-research
- cv-gap-analysis
- cv-tailoring
- interview-brief
- evidence-validator
- decision-brief

### Product Hunter
Router allow-list:
- signal-scout
- problem-validation
- poland-demand-check
- competition-landscape
- why-would-they-buy
- supplier-feasibility
- unit-economics
- regulatory-screen
- meta-ad-test-design
- investment-decision
- evidence-validator
- red-team-review

### Strategy / EA
Router allow-list:
- strategy-challenge
- architecture-review
- architecture-decision-record
- business-case-review
- operating-model-review
- portfolio-prioritization
- governance-design
- kpi-design
- vendor-evaluation
- executive-decision-brief
- evidence-validator
- red-team-review

### Web / design
Router allow-list:
- reference-analysis
- concept-to-metaphor
- motion-storyboard
- design-critique
- implementation-brief
- visual-regression-review
- quality-gate

### Skill development
Router allow-list:
- skill-specification
- skill-authoring
- skill-validation
- skill-test-design
- skill-evaluation
- skill-release-review

Meta-skills should remain isolated here so they do not compete with normal task routing.

## User interaction

The user should normally describe the goal rather than name implementation details.

Preferred:
> Evaluate this role against my target profile and highlight the material gaps.

Avoid requiring:
> Run role-fit-analysis, then evidence-validator, then decision-brief.

A well-configured router should select the procedure automatically.

Explicit skill names are useful for:
- testing;
- debugging;
- forcing a known workflow;
- comparing versions;
- developing a skill.

## Context-efficiency rules

1. Keep CATALOG metadata short.
2. Fetch only one or a few matching skills.
3. Avoid loading references before a branch needs them.
4. Keep project-specific facts in the Project, not in skills.
5. Do not repeat skill bodies in project instructions.
6. Do not use meta-skills outside skill engineering.
7. Prefer workflows with stop gates so expensive research happens only after cheap checks pass.

## Native Skills migration

When native ChatGPT Skills are available for the account/workspace:

1. Install only `production` skills.
2. Start with core skills and the active project's domain skills.
3. Do not globally install overlapping candidates.
4. Keep GitHub as source of truth and version/release through the repository.
5. Use ChatGPT's automatic selection for normal work; explicitly invoke only for tests/debugging.

## Recommended next automation

Later, add a publish/sync job that packages production skill folders for the target runtime. Keep this separate from validation and release approval so CI cannot silently publish behavioral changes.
