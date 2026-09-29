---
name: skill-test-design
description: >
  Design routing, behavioral, edge-case and regression evals for an Agent Skill. Use after a skill draft exists, when changing its description/procedure, or when converting real failures into permanent regression tests.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: draft
  risk: low
  last_reviewed: 2026-09-29
---

# Skill Test Design

## Purpose

Create tests that reveal whether a skill routes and behaves correctly, rather than tests that merely confirm happy-path prose.

## Test dimensions

Design two separate layers.

### Routing tests
Include:
1. direct should-trigger;
2. indirect should-trigger;
3. near-miss should-not-trigger;
4. competing-skill should-not-trigger;
5. uncommon but valid phrasing.

Description changes require routing tests.

### Behavioral tests
Include as relevant:
1. happy path;
2. missing required input;
3. ambiguity;
4. unsupported fact/action;
5. stale/conflicting evidence;
6. tool failure/partial result;
7. edge/adversarial input;
8. previous real regression.

## Assertion design

Prefer assertions such as:
- must perform X;
- must identify Y as unknown;
- must not invoke Z;
- must stop before external action;
- output must contain required fields.

Avoid:
- exact wording;
- stylistic trivia;
- assertions that encode one preferred chain of thought;
- tests that are too easy to fail only if the model is completely off-topic.

## Near-miss rule

Negative routing cases should share vocabulary/context with the skill but require a different capability.

Good negative:
- skill = `cv-tailoring`
- prompt = "Compare these two job descriptions and tell me which has broader scope."

Bad negative:
- "Write a Fibonacci function."

## Test output

Create/update `tests/cases.yaml` with:
- id;
- case;
- input;
- expected.should_trigger;
- expected.must;
- expected.must_not;
- optional output properties;
- optional fixtures/files.

Also identify which cases are:
- smoke;
- routing;
- behavioral;
- regression;
- high-risk.

## Minimum new-skill suite

A production candidate should have at least:
- 2 positive routing cases;
- 2 realistic negative/competing cases;
- 1 incomplete-input case;
- 1 edge/adversarial case;
- evidence/tool failure case when relevant.

Do not optimize tests to the current implementation. Tests represent the intended contract.
