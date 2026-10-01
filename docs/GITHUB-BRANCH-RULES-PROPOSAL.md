# GitHub branch rules proposal — AIS-02

Status: **proposal only; NOT APPLIED**.

No repository settings are changed by this document. Application requires owner approval and a verified publication path compatible with protected branches.

## Proposed source protection

### `main`

Require:
- pull request before merge;
- at least 1 approving review;
- dismiss stale approvals when source changes;
- conversation resolution;
- required status check: `Validate skills / validate`;
- branches up to date before merge if GitHub reports this as reliable for the current stacked-PR process;
- no force pushes;
- no branch deletion.

### `production`

Require:
- pull request before source promotion;
- at least 1 approving review;
- dismiss stale approvals;
- conversation resolution;
- required status check: `Validate skills / validate`;
- no force pushes;
- no branch deletion.

Production promotion remains a deliberate `main -> production` review. Do not infer approval from successful package generation.

## Bot/publication constraint

Current marketplace installation follows generated content from Git branches. A blanket GitHub Actions bypass would let the bot bypass the same source protections this proposal is meant to create.

Preferred end state:
1. source changes always use protected PR flow;
2. generated packages are published as immutable release/workflow artifacts or through a dedicated generated-artifact branch/channel supported by the installer;
3. the source bot gets no broad bypass for arbitrary `skills/`, `workflows/` or release-policy edits.

Until a compatible installer path is confirmed, **do not apply branch rules that would silently break the existing generated-artifact publication flow** and do not grant a broad bypass as a shortcut.

## Transitional test plan before application

1. Merge the quality PR stack through normal review.
2. On a disposable/test branch or dry-run repository, enable the proposed rules.
3. Verify a human source PR can merge only after `Validate skills / validate`.
4. Verify a failing check blocks the merge.
5. Exercise the production package workflow from an exact source SHA.
6. Confirm generated publication can occur without permission to mutate source paths.
7. Simulate a source commit arriving during build; stale-source guard must refuse publication.
8. Read GitHub API/rulesets back and capture the active configuration.
9. Only then apply the equivalent rules to `main` and `production`.

## Required owner decisions

- approval of one-review policy vs stronger review count;
- whether “branch must be up to date” is required;
- approved mechanism for generated artifact publication under protected branches;
- any narrowly scoped bot identity/bypass after testing.

## Acceptance state

Preparation can be considered complete when this configuration and test plan are reviewed. Application remains pending until GitHub settings are changed and read back from the API.
