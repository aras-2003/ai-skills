# OAF Wave 2 Validation — 2026-09-30

## Environment

Primary runtime:
- ChatGPT Work
- Luna
- candidate skills/workflow from Skills Factory Lab

Comparison runtime:
- Sol
- exact same operating-model redesign case and workflow prompt

Fixtures:
- `case-global-local-001.md`
- `case-decision-bottleneck-001.md`
- `case-portfolio-health-001.md`
- `case-operating-model-redesign-001.md`

## Results

| Component | Luna | Sol comparison | Disposition |
|---|---|---|---|
| global-local-model-review | PASS | not required | promote |
| decision-bottleneck-analysis | PASS | not required | promote |
| portfolio-health-review | PASS+ | not required | promote |
| oaf-operating-model-redesign | PASS+ | better framing/selection discipline, no material direction change | promote; strong escalation only |

## global-local-model-review

Validated behaviors:
- no automatic centralisation bias;
- global consistency separated from single global implementation;
- standards classified as mandatory / configurable / advisory;
- local workarounds treated as diagnostic evidence rather than automatic noncompliance;
- structural model problems separated from implementation/service-quality problems;
- design implications produced without prematurely selecting a target model.

Regression expectations:
- duplication alone is not sufficient evidence for centralisation;
- a routinely bypassed standard may indicate unsuitable scope, slow service, legitimate local need or poor implementation;
- local variation must be judged by enterprise externalities and local value/context.

## decision-bottleneck-analysis

Validated behaviors:
- formal and actual decision paths reconstructed separately;
- active work, waiting, rework and queue time distinguished only where evidence permits;
- 11-day evidence rework recognized as the strongest confirmed bottleneck;
- architecture re-review treated as probable duplicate work, not proven duplication;
- steering committee treated as a possible shadow gate, not assumed veto;
- formal advisers recognized as possible de facto gates;
- smallest bottleneck-removal experiment targeted evidence readiness rather than governance redesign.

Regression expectations:
- slow decision does not automatically mean too many approvers;
- missing evidence, sequential review, duplicate review, shadow veto, queue time and authority ambiguity are different failure modes;
- adviser status must be compared with actual progression authority.

## portfolio-health-review

Validated behaviors:
- portfolio evaluated as a system rather than average project status;
- 128% specialist capacity commitment treated as a hard system constraint;
- shared platform and architecture resources treated as portfolio bottlenecks;
- mandatory cybersecurity demand separated from discretionary capacity;
- approved budget separated from operational deliverability;
- outcome-traceability and no-stop behavior surfaced;
- possible initiative overlap remained a hypothesis until validated;
- ranking deferred until comparable evidence is normalized.

Regression expectations:
- many green projects do not imply a healthy portfolio;
- approved budget does not imply a deliverable portfolio;
- capacity and dependency constraints can dominate nominal project health;
- unknown ownership should be verified before prescribing a new owner.

## oaf-operating-model-redesign — Luna

Validated behaviors:
- supplied diagnosis reused rather than restarted;
- design principles defined before options;
- three bounded alternatives generated;
- authority/accountability/resources, interfaces, funding, architecture, latency and transition risk compared;
- no default centralisation;
- no premature org-chart design;
- provisional target direction accompanied by a bounded pilot;
- governance design deferred until target direction selection.

Luna result:
- provisional direction: federated/shared-capability model;
- lower-disruption current-split improvement remained a plausible fallback;
- central delivery option judged hard to justify given local-speed objective and current platform lead-time issues.

## Sol comparison

Using the same case and prompt, Sol:
- reached the same material provisional direction;
- framed the lower-disruption option more cleanly;
- more explicitly separated option framing from final selection;
- more strongly protected against assigning named owners without evidence;
- articulated that missing evidence limits **selection**, not necessarily option generation.

Material decision change: **No**.

Interpretation:
- Luna is adequate as the default for bounded operating-model redesign and option/trade-off generation;
- Sol-class reasoning adds value mainly at high-impact selection boundaries and contested evidence, not enough to justify strong as the default.

## Promotion decision

Promote to production:
- `global-local-model-review`
- `decision-bottleneck-analysis`
- `portfolio-health-review`
- `oaf-operating-model-redesign`

Validated model routing:
- default: standard / Luna-capable for tested uses;
- strong/Sol escalation for final high-impact target-state selection, materially conflicting executive evidence, major multi-country redesign, material transition economics, or politically contested authority/funding decisions.

Keep candidate:
- `organizational-interface-review`
- `capability-gap-analysis`
- `kpi-quality-review`
- `governance-design`
- `transformation-blueprint`
- `oaf-governance-redesign`
- `oaf-strategy-execution-reset`
