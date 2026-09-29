---
name: executive-role-evaluator
description: >
  Evaluate senior and executive technology job opportunities based on real mandate, organizational scope,
  candidate fit, career value, risk and evidence quality. Use when assessing whether an executive technology
  role is worth pursuing, comparing opportunities, updating an assessment after recruiter/interview evidence,
  or identifying decision-critical unknowns. Do not use for company research alone, CV tailoring alone,
  interview preparation alone, or generic job matching.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
---

# Executive Role Evaluator

## Purpose

Support better executive-career decisions by evaluating the substance of a technology leadership opportunity rather than title or keyword overlap.

The skill must answer separately:
1. What is the role in substance?
2. How strong is the role itself?
3. How credible is the candidate for it?
4. How much career value does it create?
5. What material risks and unknowns could change the decision?

## Preconditions

Use a current candidate profile from the active project/context when available. Do not embed personal profile data in this reusable skill.

Work with incomplete information, but keep unsupported fields as `UNKNOWN`.

## Procedure

1. **Normalize the opportunity**
   - Extract company, title, location/work model, reporting line, team/organization size, budget authority,
     geographic/business/technology scope, transformation mandate, executive exposure, compensation, travel,
     hiring reason and source.
   - Never invent missing values.

2. **Classify evidence**
   - Mark important claims as `FACT`, `STRONG INFERENCE`, `HYPOTHESIS`, or `UNKNOWN`.
   - Never present inference as fact.

3. **Determine the real role archetype**
   - Use the archetypes in `references/evaluation-model.md`.
   - If uncertain, provide the two most plausible archetypes and explain the uncertainty.

4. **Evaluate role quality**
   - Assess mandate/decision authority, organizational ownership, technology scope, strategic influence,
     budget/investment authority, transformation leverage, business accountability and executive positioning.
   - Responsibility without authority is a negative signal.

5. **Evaluate candidate fit separately**
   - Assess current credibility, evidence-backed strengths, gaps and narrative bridge.
   - Never recommend claiming unsupported experience.

6. **Evaluate career value separately**
   - Assess scope expansion, organizational scale, executive exposure, budget ownership, global complexity,
     technology breadth, market signaling and learning density.

7. **Identify material risks**
   - Focus on strategic, organizational, delivery, career, compensation and lifestyle risks that could materially
     change the decision.
   - Do not generate long generic risk lists.

8. **Apply critical gates**
   - A severe authority/scope contradiction can override otherwise attractive scores.
   - Do not let weighted averages hide structural problems.
   - See `references/evaluation-model.md`.

9. **Challenge the preferred interpretation**
   - Identify the strongest reason to pursue and the strongest reason not to pursue.
   - Test for title inflation, prestige bias, compensation bias, confirmation bias and promised-future-authority risk.

10. **Identify decision-critical unknowns**
    - Ask only questions whose answers could materially change the assessment.
    - Prioritize `Critical` before `Important`.

11. **Assign decision state and confidence**
    - Decision: `PURSUE`, `INVESTIGATE`, `LOW PRIORITY`, or `SKIP`.
    - Confidence: `HIGH`, `MEDIUM`, or `LOW`.
    - Do not mechanically map scores to decisions.

12. **Return the structured result**
    - Follow `references/output-template.md`.
    - If this is an update, preserve previous evidence and show what changed.

## Decision rules

- Role substance outranks title.
- Candidate fit, role quality and career value are independent dimensions.
- High compensation must not compensate for a structurally narrow role.
- High prestige must not compensate for weak mandate.
- High score with one critical unresolved structural risk can still be `INVESTIGATE`.
- Missing evidence lowers confidence; it does not justify invented values.
- For comparison mode, show trade-offs instead of collapsing all opportunities into one ranking.
- For update mode, change only dimensions affected by new evidence and show a change log.

## Inputs

### Required
At least one meaningful source describing the opportunity, such as:
- job advertisement;
- recruiter message;
- role description;
- interview/recruiter notes;
- offer details.

### Optional
- company name;
- candidate CV/profile from project context;
- compensation;
- reporting line;
- team size;
- org chart;
- prior assessment;
- company research.

## Evidence requirements

When external research is requested or required:
1. prioritize official company/IR/regulatory sources;
2. use reputable business media for context;
3. use LinkedIn or employee-review sources as secondary evidence;
4. distinguish sourced fact from interpretation.

Do not treat recruiter statements about future authority as guaranteed reality.

## Output contract

Use the structure in `references/output-template.md`.

Always include:
- decision;
- confidence;
- role archetype;
- role quality;
- candidate fit;
- career value;
- risk;
- strongest reason to pursue;
- strongest reason not to pursue;
- critical unknowns;
- recommended next action.

## Failure and uncertainty handling

- If the opportunity is too vague to score responsibly, return an `INVESTIGATE`-style discovery assessment with low confidence rather than inventing detail.
- If candidate context is missing, evaluate role quality and career value generically, and mark personal fit as limited/unknown.
- If sources conflict, surface the conflict and identify what must be validated.
- If the task is only company research, CV tailoring or interview prep, route to the appropriate specialist skill instead of expanding this skill.

## Quality checks

Before returning:
- [ ] Evidence is separated from inference.
- [ ] Responsibility is distinguished from authority.
- [ ] Title does not drive the conclusion.
- [ ] Role quality, fit and career value remain separate.
- [ ] Critical gates were checked.
- [ ] Material unknowns are visible.
- [ ] Strongest counterargument was considered.
- [ ] Recommended action follows from evidence.
- [ ] No unsupported candidate experience is claimed.
- [ ] No generic SWOT-style filler was added.

## References

- `references/evaluation-model.md` — archetypes, dimensions, weights and critical gates.
- `references/output-template.md` — required response structure and update/comparison modes.
- `references/candidate-profile-schema.yaml` — generic profile schema; actual personal profile belongs in project/private context.
