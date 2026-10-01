---
name: cv-gap-analysis
description: 'Compare an approved mastery CV with a target executive technology role
  to identify evidence-backed strengths, missing proof, weak alignment and narrative
  gaps before tailoring. Use after a role is worth pursuing and before rewriting the
  CV.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.1.0
  maturity: candidate
  risk: medium
  last_reviewed: '2026-09-30'
---

# CV Gap Analysis

## Purpose
Identify what is strong, weak, missing or merely under-evidenced before changing the CV.

## Use when
- A target role has passed basic role evaluation.
- The user wants to know what the CV fails to prove.

## Do not use when
- The task is to rewrite the CV directly.
- The role itself has not yet been assessed for worth.

## Inputs
### Required
- target role description
- approved mastery CV

## Procedure
1. Extract the role's material requirements and implied seniority signals.
2. Map each requirement to explicit CV evidence.
3. Classify: STRONG EVIDENCE / PARTIAL / ADJACENT / GAP / UNKNOWN.
4. Separate real experience gaps from presentation gaps.
5. Identify missing scale, mandate, outcome, budget, people, global scope or executive exposure evidence.
6. Propose only evidence-backed narrative bridges.
7. Prioritize the few changes that could materially improve credibility.

## Decision rules
- Never convert adjacent experience into claimed direct experience.
- Missing wording is not the same as missing capability.
- Seniority evidence outranks keyword density.

## Output contract
Requirement | Current evidence | Classification | Risk | Recommended evidence/positioning change.
Then: top 3 strengths, top 3 gaps, narrative bridge, tailoring priorities.

## Model guidance
Default model class: **standard**.
Escalate to strong only for highly ambiguous role definitions, conflicting candidate evidence, or unusually high-stakes applications.

## Quality checks
- [ ] Every strength/gap tied to evidence.
- [ ] Real gaps separated from wording gaps.
- [ ] No invented experience.
- [ ] Priorities are material, not cosmetic.

