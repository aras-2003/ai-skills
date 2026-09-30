---
name: executive-role-evaluator
description: >
  Evaluate senior and executive technology job opportunities based on real mandate, organizational scope,
  candidate fit, career value, risk and evidence quality. Use when the user asks whether a role is worth
  pursuing, compares opportunities, or asks what new company/interview evidence means for a specific role.
  Do not use for company facts alone, CV tailoring, interview preparation or generic job matching.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.1.0"
  maturity: production
  risk: medium
  last_reviewed: "2026-09-30"
---

# Executive Role Evaluator

## Purpose

Support executive-career decisions by evaluating the substance of a technology leadership opportunity rather than its title.

Keep three dimensions separate:
- **Role Quality** — mandate, authority, scope and executive positioning;
- **Candidate Fit** — evidence-backed credibility for this role;
- **Career Value** — whether the move expands the capabilities/scope relevant to the candidate's direction.

## Boundary

Use this skill only when the user asks for role evaluation, role implications, fit, career value or a pursue/investigate/skip decision.

If the request is factual company research only, stay factual and route elsewhere. Do not append unsolicited career advice merely because prior conversation context contains a role. If the request asks to rewrite a CV, prepare an interview or research company facts without evaluating the role, route to the corresponding specialist.

## Preconditions and evidence

At least one meaningful source about the opportunity is required: job description, recruiter message, interview notes, offer details or a concrete role summary.

Use candidate/project context when available, but never invent missing experience. Mark important claims as:
- FACT
- STRONG INFERENCE
- HYPOTHESIS
- UNKNOWN

Missing evidence lowers confidence; it does not become a zero score.

## Procedure

1. **Normalize the opportunity**
   - company, title, location/work model, reporting line, team, budget authority, geographic/business/technology scope, mandate, executive exposure, compensation/travel where relevant;
   - keep missing fields UNKNOWN.

2. **Classify the real role archetype**
   - use `references/evaluation-model.md`;
   - if uncertain, show the two most plausible archetypes.

3. **Assess Role Quality**
   - mandate and decision authority;
   - organizational ownership;
   - technology breadth;
   - strategic influence;
   - budget/investment authority;
   - transformation leverage;
   - business accountability;
   - executive positioning.

4. **Assess Candidate Fit separately**
   - evidence-backed strengths;
   - material gaps;
   - credible narrative bridge;
   - never claim unsupported experience.

5. **Assess Career Value separately**
   - scope expansion;
   - organizational scale;
   - executive exposure;
   - budget ownership;
   - global complexity;
   - technology breadth;
   - market signalling;
   - learning density.

6. **Apply structural gates**
   - responsibility without authority;
   - title inflation;
   - promised future mandate without current sponsor/governance;
   - transformation accountability without decision rights;
   - hard lifestyle constraint conflicts.

7. **Challenge the preferred interpretation**
   - strongest reason to pursue;
   - strongest reason not to pursue;
   - test title/prestige/compensation/confirmation bias.

8. **Identify decision-critical unknowns**
   - ask only questions whose answers could change the decision.

9. **Assign decision and confidence**
   - Decision: PURSUE / INVESTIGATE / LOW PRIORITY / SKIP;
   - Confidence: HIGH / MEDIUM / LOW;
   - do not mechanically map dimension assessments to the decision.

10. **Return the result**
    - default structure: `references/output-template.md`;
    - keep simple cases compact;
    - if the user explicitly requests another format, honor that format while preserving decision, confidence, material risks, strongest counterargument and critical unknowns.

## Decision rules

- Role substance outranks title.
- Responsibility without authority is a negative structural signal.
- Compensation and prestige do not repair a structurally narrow mandate.
- UNKNOWN is not zero and is not silently averaged away.
- Comparison mode compares the same qualitative dimensions and evidence/confidence; it does not require a numeric ranking.
- A critical unresolved gate can keep an otherwise attractive role at INVESTIGATE.
- Company facts alone do not trigger role evaluation.

## Output contract

Default first block:

Decision: PURSUE / INVESTIGATE / LOW PRIORITY / SKIP
Confidence: HIGH / MEDIUM / LOW
Role archetype: ...
Role Quality: STRONG / ADEQUATE / WEAK / UNKNOWN
Candidate Fit: STRONG / GOOD / PARTIAL / GAP / UNKNOWN
Career Value: HIGH / MEDIUM / LOW / UNKNOWN
Risk: LOW / MEDIUM / HIGH / VERY HIGH

Then include only decision-relevant sections needed for the case.

Always preserve:
- strongest reason to pursue;
- strongest reason not to pursue;
- critical unknowns;
- recommended next action.

If the user requests a table, bullets, one-paragraph answer or another layout, that requested layout may replace the default block order, but the required decision facts above must remain present. Do not fabricate numeric /100 scores unless the user explicitly requests a scored model and an explicit scoring contract is supplied.

## Failure and uncertainty handling

- If the role is too vague, use INVESTIGATE with LOW confidence rather than inventing scope.
- If candidate context is missing, Candidate Fit is UNKNOWN/limited-evidence.
- If sources conflict, surface the conflict and identify what must be validated.
- If only factual company research is requested, do not trigger this skill.
- If the user asks for a numeric score without a defined scoring method, explain that the default model is qualitative and ask whether a separately anchored scoring model is wanted.

## Quality checks

- [ ] Evidence is separated from inference.
- [ ] Authority is distinguished from responsibility.
- [ ] Title does not drive the conclusion.
- [ ] Role Quality, Candidate Fit and Career Value remain separate.
- [ ] UNKNOWN was not treated as zero.
- [ ] Material unknowns and strongest counterargument are visible.
- [ ] No unsupported candidate experience is claimed.
- [ ] Pure company research was not extended into unsolicited career advice.
- [ ] User-requested format was respected without dropping decision-critical facts.

## References

- `references/evaluation-model.md` — qualitative dimensions, archetypes and structural gates.
- `references/output-template.md` — default, compact, comparison and update layouts.
- `references/candidate-profile-schema.yaml` — generic profile schema; personal data belongs in private/project context.
