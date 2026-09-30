---
name: cv-tailoring
description: >
  Tailor an approved mastery CV to one specific executive technology role while preserving factual accuracy, seniority and evidence. Use after cv-gap-analysis; do not invent experience, inflate scope or optimize for keywords at the expense of credibility.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# CV Tailoring

## Purpose
Produce a role-specific CV variant that improves relevance without weakening factual integrity.

## Use when
- A role is worth pursuing.
- An approved mastery CV and gap analysis exist.

## Do not use when
- There is no authoritative base CV.
- The user asks for unsupported experience to be added.

## Inputs
### Required
- mastery CV
- target role description
### Recommended
- cv-gap-analysis output

## Procedure
1. Preserve identity, dates, employers, titles and factual achievements.
2. Reorder emphasis around the role's highest-value requirements.
3. Rewrite summary and selected bullets to surface relevant mandate, scale, outcomes and technology breadth.
4. Strengthen evidence density using existing facts.
5. Remove low-value detail only when it improves fit and does not distort history.
6. Run an accuracy pass against the mastery CV.
7. Flag claims that need user confirmation rather than guessing.

## Decision rules
- Factual truth outranks ATS optimization.
- Reframing is allowed; fabrication is not.
- Never inflate team size, budget, reporting line, ownership or business outcome.

## Output contract
Return: tailored summary, changed bullets/sections, retained critical evidence, removed/de-emphasized items, and a change log with rationale.

## Model guidance
Default model class: **standard**.
Escalate only for major restructuring across multiple CV versions or nuanced executive-positioning trade-offs.

## Quality checks
- [ ] Every material claim traceable to mastery CV/source.
- [ ] No scope inflation.
- [ ] Seniority and executive narrative improved.
- [ ] Change log included.

