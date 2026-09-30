---
name: interview-brief
description: >
  Prepare a concise executive interview brief from an evaluated role, company context and candidate profile, including likely themes, evidence-backed talking points, risks and high-value questions. Use before recruiter, hiring-manager or executive interviews.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: candidate
  risk: medium
  last_reviewed: 2026-09-30
  execution:
    default_model_class: standard
---

# Interview Brief

## Purpose
Convert known role/company evidence into a practical interview preparation brief.

## Use when
- An interview/recruiter call is scheduled.
- Role evaluation and company context already exist or can be gathered cheaply.

## Do not use when
- The user only wants generic interview advice.
- The company still needs basic factual research only.

## Inputs
### Required
- role/company/interview stage
### Optional
- executive-role-evaluator output
- company-context-research output
- CV/profile
- interviewer identity

## Procedure
1. Identify interview stage and probable decision agenda.
2. Summarize what is known about role, company and mandate.
3. Generate likely questions based on actual role risks, not generic lists.
4. Map each likely question to evidence-backed candidate stories.
5. Prepare concise messages: why this role, why now, relevant proof, concerns.
6. Generate 5–8 high-value questions that can change the candidate's decision.
7. Flag topics that require validation rather than polished assumptions.

## Decision rules
- Questions should target mandate, success criteria, authority, team, budget, operating model and hidden problems when relevant.
- Do not script fake certainty or unsupported accomplishments.

## Output contract
1-page style brief: meeting objective, 5 key messages, likely questions + proof points, critical unknowns, candidate questions, red flags to listen for, 30-second close.

## Model guidance
Default model class: **standard**.
Escalate for board-level interviews, complex political/organizational dynamics, or multiple conflicting stakeholder narratives.

## Quality checks
- [ ] Tailored to interview stage.
- [ ] Talking points evidence-backed.
- [ ] Questions are decision-relevant.
- [ ] No generic filler.

