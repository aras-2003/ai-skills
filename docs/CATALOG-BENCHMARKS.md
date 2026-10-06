# External Skill Catalogs and Design Benchmarks

This repository should use external catalogs as **design references**, not copy them wholesale.

## 1. Anthropic official Agent Skills repository

Repository: `anthropics/skills`

Why it is useful:
- canonical examples of the Agent Skills pattern;
- clear self-contained folder model;
- `SKILL.md` plus optional scripts/resources;
- includes simple examples and complex document-production skills;
- includes the specification and template.

What to borrow:
- minimal frontmatter;
- strong "what + when to use" descriptions;
- self-contained packages;
- progressive loading of support files;
- explicit examples.

What not to borrow blindly:
- domain content unrelated to our use cases;
- large document skills when a smaller procedure is enough.

## 2. OpenAI Skills guidance and repositories

OpenAI documents skills as reusable instructions plus supporting files and states compatibility with the open Agent Skills standard.

OpenAI repositories also show the pattern of storing repository skills under `.agents/skills/` and using mandatory/automatic routing rules in repository guidance.

What to borrow:
- portability with the open standard;
- skills as reusable components rather than project prompts;
- sandbox/runtime separation;
- focused eval harnesses for agent behavior.

## 3. frankxai/claude-skills-library

Useful as a catalog-engineering reference.

Observed patterns:
- generated catalog;
- automated validation;
- large categorized library;
- separate runtime compatibility layer.

What to borrow:
- generated CATALOG.md;
- validation scripts;
- metadata consistency;
- domain categorization.

Main warning:
- hundreds of skills create discoverability and maintenance problems unless routing and curation are strong.

## 4. JayRHa/AgentSkills

Useful as a packaging and distribution reference.

Observed patterns:
- `SKILL.md + scripts + references + examples`;
- cross-runtime positioning;
- selective installation;
- lightweight loading until invoked.

What to borrow:
- install only what is needed;
- canonical skill package;
- cross-agent portability.

## 5. secondsky/claude-skills

Useful for a large production-oriented technical catalog.

Observed patterns:
- category-based marketplace;
- individually installable skills;
- generated human-readable catalog;
- strong specialization instead of one giant general skill.

What to borrow:
- domain ownership;
- individual installability;
- explicit catalog metadata;
- separation of testing, design, architecture, API and tooling skills.

## 6. NVIDIA skills

Useful as a governance benchmark.

Observed patterns:
- verified/curated catalog;
- central catalog backed by skills maintained in product repositories;
- version/catalog metadata;
- automated synchronization.

What to borrow later:
- verification status;
- ownership;
- version tracking;
- catalog automation.

## Recommendation for Skills Factory

Use a hybrid model:

1. **Open Agent Skills format** for interoperability.
2. **Anthropic-style self-contained skill folders**.
3. **OpenAI-style agent/runtime portability and eval thinking**.
4. **frankxai-style generated catalog + validation**.
5. **NVIDIA-style maturity/verification governance** once the library grows.
6. Keep the production catalog deliberately small.

The objective is not to build the largest catalog. It is to build the smallest catalog that reliably improves repeated work.
