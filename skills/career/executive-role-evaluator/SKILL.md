---
name: executive-role-evaluator
description: >
  Evaluate senior and executive technology job opportunities based on real mandate, organizational scope,
  candidate fit, career value, risk and evidence quality. Use when assessing whether an executive technology
  role is worth pursuing, comparing opportunities, updating an assessment after recruiter/interview evidence,
  or identifying decision-critical unknowns. Do not use for company research alone, CV tailoring alone,
  interview preparation alone, generic job matching, or factual company research that does not explicitly ask for role implications.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.1.0"
  maturity: production
  risk: medium
  last_reviewed: "2026-09-30"
---

# Executive Role Evaluator

## Purpose
Evaluate the substance of an executive technology opportunity without confusing title, compensation or company prestige with mandate.

## Preconditions
Use the current candidate profile from project/context when available. Do not embed private profile data in this reusable skill. Missing evidence remains `UNKNOWN`.

## Boundary
Trigger only for role/mandate/fit/career-value decisions. Pure company facts route to company research; CV rewriting routes to CV tailoring; interview preparation routes to interview brief. Do not append career advice to factual company research.

## Procedure
1. Normalize the opportunity: reporting line, team, budget/decision rights, geographic/business/technology scope, executive exposure, compensation/travel and hiring reason.
2. Classify important claims as `FACT`, `STRONG INFERENCE`, `HYPOTHESIS` or `UNKNOWN`.
3. Determine the most plausible role archetype; show two if unresolved.
4. Assess **Role Quality** qualitatively across mandate/authority, organization, technology scope, strategic influence, budget, transformation leverage, business accountability and executive positioning.
5. Assess **Candidate Fit** separately from role quality.
6. Assess **Career Value** separately from both, focusing on scope expansion, scale, executive exposure, budget/global complexity, technology breadth and learning.
7. Identify only material strategic, organizational, delivery, career, compensation and lifestyle risks.
8. Apply critical gates. Responsibility without authority, title inflation or promised future mandate can override otherwise positive signals.
9. State the strongest reason to pursue and strongest reason not to pursue.
10. Identify only decision-critical unknowns.
11. Assign decision state `PURSUE`, `INVESTIGATE`, `LOW PRIORITY` or `SKIP`, plus `HIGH`/`MEDIUM`/`LOW` confidence. Do not mechanically map assessments to the decision.
12. Follow `references/output-template.md`, unless the user explicitly requests another format.

## Decision rules
- Role substance outranks title.
- Candidate Fit, Role Quality and Career Value are independent dimensions.
- Default assessments are qualitative, not /100.
- `UNKNOWN` is not zero and must not be averaged away.
- Do not invent a numeric total without a separately defined scale and aggregation contract.
- If the user explicitly requests a numeric score, explain that the repository has no calibrated /100 aggregation; keep the evidence-backed qualitative dimensions and uncertainty rather than fabricating precision.
- High compensation or prestige cannot compensate for a structural authority/scope mismatch.
- Comparison mode must use the same qualitative method for every role and show trade-offs rather than a winner-by-score.
- User-requested format takes precedence over the default layout, but the decision, confidence, material risks, strongest counterargument and critical unknowns must still be preserved.

## Inputs
Required: at least one meaningful source describing the role/opportunity.
Optional: company context, candidate profile, compensation, reporting line, team/budget scope, prior assessment and recruiter/interview evidence.

## Evidence requirements
When research is needed, prefer official/primary sources, then reputable business sources; keep recruiter promises about future authority as unverified until governance/mandate evidence supports them.

## Output contract
Default first block:
```
Decision: PURSUE / INVESTIGATE / LOW PRIORITY / SKIP
Confidence: HIGH / MEDIUM / LOW
Role archetype: ...
Role Quality: STRONG / MIXED / WEAK / UNKNOWN
Candidate Fit: STRONG / GOOD / PARTIAL / GAP / UNKNOWN
Career Value: HIGH / MEDIUM / LOW / UNKNOWN
Risk: LOW / MEDIUM / HIGH / VERY HIGH
```

Then include only decision-relevant sections. Always preserve:
- strongest reason to pursue;
- strongest reason not to pursue;
- critical unknowns;
- recommended next action.

If the user explicitly requests a table, memo, comparison matrix or compact format, use that format instead of forcing the default first block while preserving the same decision content.

## Failure and uncertainty handling
- Vague opportunity -> `INVESTIGATE` with low confidence, not invented detail.
- Missing candidate context -> role quality/career value may still be assessed; personal fit remains unknown/limited.
- Conflicting sources -> surface conflict and what would resolve it.
- Pure company facts/CV/interview task -> route elsewhere.
- Never claim unsupported candidate experience.

## Quality checks
- [ ] Evidence and inference are separated.
- [ ] Responsibility is distinguished from authority.
- [ ] Role Quality, Candidate Fit and Career Value remain separate.
- [ ] UNKNOWN was not converted to zero.
- [ ] No unsupported /100 score was invented.
- [ ] Critical gates and strongest counterargument were considered.
- [ ] Pure company research did not become unsolicited career advice.
- [ ] User-requested format was respected while preserving decision/confidence/risks/unknowns.

## References
- `references/evaluation-model.md`
- `references/output-template.md`
- `references/candidate-profile-schema.yaml`
