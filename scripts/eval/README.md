# Runtime eval protocol

This directory defines the evidence boundary for runtime evaluations.

## Isolation rule

The executor receives only files ending in `.input.md` plus the runtime catalog needed for the case. It must never receive files ending in `.rubric.yaml`, expected routing, expected answer, PASS/FAIL criteria, or evaluator notes.

`evals/runtime-fixtures.yaml` is the canonical registry. Every runtime case records a stable case ID, execution mode (`explicit` or `natural-routing`), executor input, and evaluator rubric.

The Lab packager copies only executor inputs.

## Evidence receipts

Use `receipt.py` to create or validate a record. `NOT_RUN` is a first-class status and is required when runtime/model access is unavailable. Historical narrative summaries are not receipts for a later component version.

A receipt binds evidence to input/rubric digests and a source revision. It also records runtime/model identity, reasoning setting, available catalog, prompt, actual output digest, trace location, reviewer, and assisted/unassisted state.

An assisted run cannot be recorded as PASS.

## Commands

- `python scripts/eval/validate_isolation.py`
- `python scripts/eval/validate_isolation.py --artifact <built-lab-dir>`
- `python -m unittest discover -s scripts/eval/tests -p 'test_*.py'`
- `python scripts/eval/receipt.py validate evals/results/<record>.json`

Provider adapters are intentionally out of scope for the first harness. Runtime execution can be imported later, but missing credentials/runtime must remain `NOT_RUN`.
