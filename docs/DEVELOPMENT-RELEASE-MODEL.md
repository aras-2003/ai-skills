# Development and release model

## Goal

Keep `main` current and useful for continuous development while `production` remains a reproducible personal runtime snapshot. Avoid long-lived stacked PR chains and stale integration branches.

## Branch model

- `main` is the active source of truth. It should stay close to deployable and must pass repository validation before a production promotion.
- `production` is a promoted snapshot of `main` plus generated production artifacts committed by the packaging workflow.
- Use a short-lived feature branch only for changes that benefit from isolated review or risky experimentation.
- Do not stack long-lived PRs for sequential phases when one consolidated change can be integrated and validated on `main`.
- Once a stacked/temporary branch is fully represented on `main`, close its PR as superseded.

## Personal-beta production rule

This repository is primarily a personal system. A temporary personal-beta exception may continue use only for a component already declared production, at the exact recorded version, while runtime evidence is pending. It does not authorize a new production promotion, a changed component/version, expanded scope or a wider audience. A new promotion must pass its current mandatory release gates for the exact artifact and channel. No exception covers a known unresolved high-severity failure. For an existing-component continuation, all of the following are true:

1. static contracts and repository validators pass;
2. package builds and artifact validation pass;
3. relevant deterministic/unit tests pass;
4. executor inputs remain isolated from evaluator rubrics;
5. runtime evidence gaps are recorded as `NOT_RUN` / `pending`;
6. no unresolved known high-severity failure exists;
7. the readiness exception has an owner and short expiry.

Personal-beta production is not the same as verified runtime PASS.

## Change flow

For normal incremental work:

1. change `main` directly or use one short-lived feature branch;
2. run/observe the full `Validate skills` gate;
3. fix blockers rather than weakening validators;
4. when the main snapshot is worth using, bump `release/package.yaml`;
5. start a new runtime campaign when behavior-bearing files changed;
6. promote the exact green `main` snapshot to `production`;
7. let `.github/workflows/package-production.yml` build and commit generated runtime artifacts.

Behavior-bearing paths currently include `skills/`, `workflows/`, and `release/package.yaml`; changing them invalidates the active campaign pin and requires a new behavior baseline.

## Evidence discipline

- Offline/static checks are never described as runtime PASS.
- Historical PASS/FAIL remains bound to its original component version and source revision.
- A pending-evidence exception is limited to an already-declared production component and exact version, and records the gap, limitation, owner and expiry. It never authorizes a new promotion or materially changed version.
- Failures discovered in real use should become regression fixtures before the next meaningful release.

## Promotion cadence

Promote when there is a useful coherent increment, not for every edit. The expected steady state is:
- few or zero open PRs;
- current `main`;
- one known `production` snapshot;
- explicit pending runtime tests;
- continuous learning from real use.
