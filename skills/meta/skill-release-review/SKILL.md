---
name: skill-release-review
description: >
  Perform the final production-readiness review for an Agent Skill. Use after validation and evals are complete, before promoting a candidate from development/main to the production skill catalog.
metadata:
  owner: arkadiusz-kamrowski
  version: "0.1.0"
  maturity: draft
  risk: medium
  last_reviewed: 2026-09-29
---

# Skill Release Review

## Purpose

Make promotion a controlled decision based on evidence, not enthusiasm.

## Required evidence

Confirm:
- approved behavioral contract;
- standards/static validation passed;
- routing tests passed;
- behavioral tests passed;
- known regressions resolved or explicitly accepted;
- high-risk failure modes addressed;
- owner/version/review date current;
- real use case or workflow exists;
- optional dependencies documented;
- user-visible/external actions have explicit approval boundaries.

## Release decision

### APPROVE
Use when:
- no blocker/high issue remains;
- intended routing is stable;
- behavioral value is demonstrated;
- production maintenance burden is acceptable.

### APPROVE WITH FOLLOW-UP
Use only for non-critical low/medium issues with explicit owner and next review.

### REJECT / ITERATE
Use when:
- severe routing collision exists;
- key evals fail;
- skill adds no clear value over baseline;
- behavior is surprising/unsafe;
- scope remains unstable;
- the procedure is better represented as a script/project instruction/workflow.

## Promotion checklist

- [ ] Name and description final
- [ ] Package valid
- [ ] Tests committed
- [ ] Evals reviewed
- [ ] No unresolved blocker/high issue
- [ ] Version updated for behavioral change
- [ ] Catalog metadata ready
- [ ] Human approval recorded

## Output

Return:
- decision;
- evidence reviewed;
- unresolved issues;
- release notes;
- rollback/deprecation note if replacing an older skill;
- next review trigger/date.

Do not merge/promote automatically unless the user has explicitly authorized that action.
