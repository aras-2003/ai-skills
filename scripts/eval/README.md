# Runtime eval protocol

This directory defines the evidence boundary for runtime evaluations.

## Isolation rule

The executor receives only files ending in `.input.md` plus the runtime catalog needed for the case. It must never receive files ending in `.rubric.yaml`, expected routing, expected answer, PASS/FAIL criteria, or evaluator notes.

There is no single universal runtime registry. The active campaign composes Commerce cases from `evals/runtime-fixtures.yaml`, natural-routing cases from `evals/routing/registry.yaml`, split executive-role cases, and campaign-specific fallback cases. The active definition is `evals/campaigns/runtime-validation-2026-10-r2/campaign.yaml`; the supplemental interface-routing regression is outside the core-38 count.

The Lab packager copies only executor inputs.

## Test-suite validation vs execution

`scripts/validate/validate_tests.py` statically validates the definitions under both `skills/**/tests/cases.yaml` and `workflows/**/tests/cases.yaml`: YAML, schema, IDs and required assertion fields.

That validator does **not** execute the behavioral assertions against a model/runtime. In particular, the `oaf-health-check` confidence cases are planned behavioral regressions until an actual evaluator/runtime run executes them. A structurally valid case is not runtime PASS.

## Evidence receipts

Use `receipt.py` to create or validate a record. `NOT_RUN` is a first-class status and is required when runtime/model access is unavailable. Historical narrative summaries are not receipts for a later component version.

A receipt binds evidence to input/rubric digests and a source revision. It also records runtime/model identity, reasoning setting, available catalog/tools, prompt, actual output and trace digests, reviewer, assisted/unassisted state, and separate source-component vs packaged runtime-artifact identity where available. Historical receipts can be validated against their recorded source revision.

An assisted run cannot be recorded as PASS.

## Commands

- `python scripts/eval/validate_isolation.py`
- `python scripts/eval/validate_isolation.py --artifact <built-lab-dir>`
- `python -m unittest discover -s scripts/eval/tests -p 'test_*.py'`
- `python scripts/eval/campaign.py validate`
- `python scripts/eval/campaign.py prepare --output .tmp/runtime-campaign-r2`
- `python scripts/eval/campaign.py queue --include-supplemental`
- `python scripts/eval/campaign.py validate-evidence`
- `python scripts/eval/receipt.py validate evals/results/<record>.json`

Provider/runtime execution remains external to the offline harness. Exact-version smoke requires independently observed package release/source/payload/component identity; values copied from the lock are not evidence. A routing mismatch may be archived as `FAIL` or `REVIEW_REQUIRED`, but it blocks `PASS`. Offline synthetic regressions are not runtime evidence.
