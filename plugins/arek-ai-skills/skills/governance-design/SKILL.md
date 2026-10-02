---
name: governance-design
description: 'Design the minimum governance mechanisms needed for a defined set of
  material decisions, including ownership, evidence, cadence and escalation. Use only
  after decision-rights or operating-model problems are sufficiently diagnosed; do
  not create committees as a default response.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 1.0.0
  maturity: production
  risk: medium
  last_reviewed: '2026-09-30'
---

# Governance Design

## Purpose
Create the minimum governance needed to make defined decisions well and quickly.

## Preconditions
Require:
- an evidenced material decision set;
- known or explicitly unresolved decision owners;
- diagnosed latency/quality/accountability problems;
- enough evidence to distinguish decision-rights failure from information or execution failure.

If these are missing, stop and route back to diagnosis.

## Procedure
1. Define the material decisions the governance system must enable.
2. For each decision, specify:
   - accountable decision owner;
   - advisers/required evidence providers;
   - executor;
   - trigger/cadence;
   - decision SLA where useful;
   - escalation destination and trigger.
3. Group decisions into one mechanism only when participants, cadence and evidence needs genuinely align.
4. Prefer direct decision rights, asynchronous evidence or standing rules over a new forum when they are sufficient.
5. Where a forum is required, define:
   - purpose and bounded mandate;
   - decisions owned;
   - chair/decision owner;
   - required membership;
   - required inputs/pre-read;
   - explicit outputs;
   - cadence/event trigger;
   - escalation path.
6. Identify existing mechanisms that should be removed, merged or narrowed.
7. Test the design for:
   - duplicate vetoes;
   - hidden approval layers;
   - unclear advice vs authority;
   - latency;
   - excessive participant load;
   - weak evidence inputs;
   - accountability without execution/funding authority.
8. Define governance effectiveness measures and a review point.

## Decision rules
- No forum without a decision purpose.
- A decision owner is more important than a committee.
- Consultation must not silently become approval.
- Escalation requires a named destination, trigger and authority.
- Do not add recurring cadence when an event-triggered mechanism is enough.
- Governance should reduce decision latency and ambiguity, not add ceremony.
- Remove/merge before adding where existing mechanisms overlap.
- Retain an existing forum only when a material decision still needs it after direct/asynchronous mechanisms are considered.
- If ownership or authority is still unknown, do not invent a final governance design.

## Output contract
### Decision-to-governance map
Decision | owner | advisers/evidence | executor | trigger/cadence | SLA | escalation | mechanism.

### Governance mechanisms
Mechanism | purpose | decisions | owner/chair | members | inputs | outputs | cadence/trigger | escalation.

Then:
- mechanisms to remove/merge/narrow;
- risks and trade-offs;
- effectiveness measures;
- unresolved design questions;
- pilot/review recommendation.

## Model guidance
Default: **standard**.
Validated on Luna for bounded governance design, forum minimisation and decision-led mechanism design.
Escalate to strong for politically contested executive authority, cross-enterprise governance redesign, or high-impact final forum/decision architecture selection.

## Quality checks
- [ ] Every mechanism traces to a material decision.
- [ ] Decision owner remains explicit.
- [ ] Advice vs approval separated.
- [ ] Existing mechanisms removed/merged before adding new ones.
- [ ] Existing forum retention is evidence/decision-need based.
- [ ] Escalation explicit.
- [ ] Decision latency considered.
- [ ] Effectiveness evidence defined.
