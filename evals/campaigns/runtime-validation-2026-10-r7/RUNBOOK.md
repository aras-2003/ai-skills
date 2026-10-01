# Runtime Validation Campaign R7 — consolidated personal-beta baseline

## Identity

- campaign: `runtime-validation-2026-10-r7`
- behavior source: `008c9944cf3a8bc3e2d7231a4862aaf00e722889`
- production package: `arek-ai-skills 1.9.0`

R1–R6 receipts remain historical evidence with their original source revisions and statuses.

## Purpose

R7 re-pins the runtime campaign after consolidating AIS audit hardening and adding Investing OS to the personal production package. Existing 38 regression cases remain the core cross-domain regression pack. Investing-specific cases are registered separately in `evals/runtime-fixtures.yaml` and start as `NOT_RUN`.

## Prepare

~~~bash
python scripts/eval/campaign.py validate
python scripts/eval/campaign.py prepare --output .tmp/runtime-campaign-r7
python scripts/eval/campaign.py validate-lock --lock .tmp/runtime-campaign-r7/lock.json
python scripts/eval/campaign.py validate-evidence
~~~

Static/offline checks are not runtime PASS.

## Operating rule

This is a personal-beta production baseline: green static/package gates allow normal use. Missing exact-version runtime receipts remain explicit pending evidence unless a known high-severity failure is open.
