---
name: skill-release-review
description: 'Make an evidence-gated production-readiness decision for an Agent Skill
  after validation and evaluation are complete. Use before promotion or publication,
  including when reviewing a changed production skill.

  '
metadata:
  owner: arkadiusz-kamrowski
  version: 0.2.0
  maturity: draft
  risk: medium
  last_reviewed: '2026-10-05'
---

# Skill Release Review

## Purpose

Decide whether a specific, identified skill version is ready for a named release channel. Separate the readiness recommendation from human authorization to merge, publish or deploy.

## Entry gate

Require:
- exact candidate identity (repository revision, skill version and target channel);
- approved scope/behavior contract;
- current validation and package/build results;
- routing, behavioral and regression evaluation evidence appropriate to the change;
- release criteria and known risk acceptances.

If evidence is missing, stale, belongs to another revision, or cannot be reproduced, record the gap and do not infer readiness. A local pass does not prove that the packaged artifact contains that revision.

## Review procedure

1. **Bind the candidate.** Record skill name, metadata version, source commit, package/channel, and the artifact or manifest digest when available. Check that all evidence targets this exact content.
2. **Check scope and value.** Confirm a real use case, stable boundary, distinct role versus neighboring skills, and acceptable maintenance cost. Prefer a workflow, reference, project instruction or script when that better fits the need.
3. **Review quality evidence.** Inspect validation, positive/negative routing, behavioral, edge/failure and regression cases. Verify that failures are resolved or explicitly dispositioned with an authorized owner; averages cannot erase a severe failure.
4. **Review safety and operations.** Check claims/evidence rules, privacy and security, tool permissions, external actions and approval boundaries, failure/rollback path, dependencies, observability and support ownership as relevant.
5. **Review packaging and catalog.** Confirm maturity is correct for the target channel, source files are included, generated catalog and manifests are current, dependencies are available, package/build succeeds, and no draft/test rubrics leak into production.
6. **Review version and compatibility.** Require an appropriate version change for behavioral changes, release notes for user-visible changes, and an explicit compatibility/deprecation plan where replacing behavior or identifiers.
7. **Apply the release gate.** Use the decision criteria below. Record blockers separately from follow-ups and name the evidence for every material conclusion.
8. **Request authorization.** State the exact merge/promotion/publication action, target and expected effect. Do not perform it unless the user has explicitly authorized that action in the current applicable context.

## Decision criteria

- **APPROVE** — all mandatory evidence is current and bound to the candidate; no unresolved blocking/high issue; behavior adds value; packaging, channel and ownership are ready.
- **APPROVE WITH FOLLOW-UP** — no blocker/high issue; only bounded low/medium follow-ups remain, each with owner, due/trigger and accepted risk.
- **ITERATE** — fixable required evidence, validation, test, packaging or readiness gaps remain.
- **REJECT** — unsafe/surprising behavior, severe unresolved regression, no demonstrated value, unstable scope, or a better non-skill solution is established.

A missing fact is a blocker only when it is required by the declared release policy; otherwise record it as a limitation. Never relabel missing evidence as a pass.

## Promotion checklist

- [ ] Candidate revision, skill version and destination channel match the reviewed artifacts
- [ ] Scope, distinct value and owner are current
- [ ] Validation and appropriate routing/behavior/regression evidence pass
- [ ] No unresolved blocker/high issue; risk acceptance is explicit and authorized
- [ ] Security, privacy, tools and external-action boundaries are sound
- [ ] Dependencies, support, monitoring and rollback/deprecation path are understood
- [ ] Package, manifest and generated catalog match source; production excludes non-production material
- [ ] Version and release notes reflect the change
- [ ] Human authorization for the exact promotion action is recorded

## Result

Return:
- decision: APPROVE / APPROVE WITH FOLLOW-UP / ITERATE / REJECT;
- candidate identity, target channel and evidence revision;
- evidence reviewed with pass/gap/blocker status;
- unresolved risks and authorized acceptances;
- package/catalog/version findings;
- release notes and rollback/deprecation note;
- exact next action and whether separate human authorization is required.

A recommendation is not a merge, promotion or deployment. Never promote automatically.
