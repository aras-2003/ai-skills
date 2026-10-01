# Career / Executive Job Market

Repeatable skills for job discovery, role evaluation, application tailoring and interview preparation.

| Skill | Purpose |
|---|---|
| `job-discovery` | Find relevant executive / senior technology roles from approved sources. |
| `job-validity-check` | Confirm that an offer is active, current and not a duplicate. |
| `executive-role-evaluator` | Decision engine for executive technology opportunities: role substance, mandate, candidate fit, career value, risk and unknowns. |
| `company-context-research` | Research factual company scale, ownership, leadership and technology context without silently extending into role evaluation. |
| `cv-gap-analysis` | Identify missing evidence or weak alignment between CV and role. |
| `cv-tailoring` | Tailor a mastery CV to one role without inventing experience. |
| `interview-brief` | Prepare role/company brief, likely questions, risks and candidate questions. |
| `process-update` | Convert new recruitment information into a structured tracker update. |

There is currently no implemented `career-trajectory-check` skill in this repository; it remains a possible future specialization.

Suggested workflow:
`job-discovery -> job-validity-check -> executive-role-evaluator -> company-context-research (when needed) -> cv-gap-analysis -> cv-tailoring -> interview-brief -> process-update`

Use progressive depth: expensive research should start only after basic validity and fit checks pass.


## Model-class defaults

- **fast:** job-discovery, job-validity-check, process-update
- **standard:** company-context-research, executive-role-evaluator, cv-gap-analysis, cv-tailoring, interview-brief
- **strong:** escalation only when ambiguity, novelty, conflicting evidence or decision impact justify it

See `docs/MODEL-ROUTING.md`.
