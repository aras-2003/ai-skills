# Runtime evaluation protocol

Runtime evaluation uses two isolated contexts:

1. **Executor context** receives only the case input and the runtime catalog/dependencies available to the tested component.
2. **Evaluator context** receives the actual output, the rubric, and the relevant execution/tool trace.

Files ending in `.input.md` are executor inputs. Files ending in `.rubric.yaml` are repository-only evaluator material and MUST NOT be packaged into executor references.

`evals/runtime-fixtures.yaml` is the registry. Each case declares its mode:
- `explicit` — behavior test where the component is deliberately invoked;
- `natural-routing` — routing test where the prompt must not name the target component.

Historical `case-*.md` files and `validation-*.md` reports are retained for audit history. They may contain assisted instructions or summary judgments and are **not current-version receipts**.

## Evidence receipts

A runtime run should record:
- case/input/rubric digests;
- tested component version/content digest;
- source revision;
- exact runtime/model/reasoning configuration;
- available catalog;
- actual output;
- relevant tool/resource trace;
- assertions/reviewer;
- assisted/unassisted status;
- timestamp.

If the required runtime is unavailable, record `NOT_RUN`/pending. Never infer PASS from a historical summary.

Static integrity is checked by:

`python scripts/eval/validate_eval_protocol.py`

The protocol validator rejects executor inputs that expose expected-routing/PASS/failure sections.
