---
name: skill-validation
description: >
  Validate an Agent Skill package for structural correctness, routing clarity, standards alignment, security, portability, duplication and maintainability. Use after authoring or modifying a skill and before behavioral evaluation or release.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.0.0"
  maturity: production
  risk: medium
  last_reviewed: 2026-09-30
---

# Skill Validation

## Purpose

Perform static and semantic review before runtime evals.

## Validation sequence

### 1. Package structure
Check:
- SKILL.md exists;
- optional folders are purposeful;
- referenced files exist;
- paths are valid;
- no unrelated artifacts are bundled.

### 2. Frontmatter
Check:
- unique kebab-case name;
- description is meaningful;
- description states what + when;
- optional metadata is internally consistent.

### 3. Routing quality
Check:
- user goal is recognizable;
- indirect formulations can match;
- near-miss cases are distinguishable;
- scope does not collide materially with another skill.

### 4. Behavioral completeness
Check:
- preconditions;
- inputs;
- procedure;
- output contract;
- missing-data behavior;
- stop/escalation behavior;
- evidence requirements when factual claims matter.

### 5. Progressive disclosure
Check:
- core workflow is in SKILL.md;
- long/conditional material is externalized;
- references are pointed to explicitly;
- no unnecessary context loading.

### 6. Deterministic boundary
Flag:
- arithmetic in prose;
- fragile regex-like reasoning;
- repeatable parsing better done by code;
- validations that can be deterministic.

### 7. Tool / connector boundary
Check:
- skill explains the workflow;
- tools provide data/actions;
- dependencies do not substitute for instructions;
- handling of unavailable/partial tool results is defined.

### 8. Instruction hierarchy and portability
Check:
- no assumption that skill instructions outrank explicit user instructions;
- runtime-specific behavior is identified;
- core method is portable where practical.

### 9. Security / least surprise
Block if skill:
- hides destructive/external actions;
- requests unnecessary credentials/secrets;
- expands permissions unexpectedly;
- performs actions outside described user intent;
- includes unsafe or malicious behavior.

### 10. Maintainability
Check:
- no giant catch-all procedure;
- no duplicated domain truth;
- no unnecessary MUST-style rigidity;
- rationale is present for non-obvious rules;
- version and owner metadata are current if used.

## Result

Return:

- **PASS** — no blocking issue;
- **PASS WITH WARNINGS** — usable for evals; warnings tracked;
- **FAIL** — must be fixed before evals/release.

For every issue include:
- severity: blocker / high / medium / low;
- category;
- exact location;
- why it matters;
- smallest recommended fix.

Do not evaluate factual task performance here; that belongs to behavioral evaluation.
