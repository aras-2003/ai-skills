# Production readiness evidence — AIS-21

`release/production-readiness.yaml` is the machine-checkable record for every currently declared production skill/workflow.

## What the record means

This review does **not** mass-promote or mass-downgrade components. It distinguishes:
- declared maturity;
- static contract/test presence;
- exact-version runtime evidence;
- remaining evidence gaps and temporary disposition.

After evaluator-rubric isolation changes, historical narrative PASS/PASS++ summaries are not treated as exact-version unassisted receipts. Where no matching receipt exists, `current_runtime_receipt: pending` is explicit.

Existing production maturity is retained temporarily for review rather than silently re-certified. Each pending record has an owner and review date. No such record is an exception from a known unresolved high-severity failure.

## Promotion/readiness rule

A future new promotion or re-certification should require:
1. static/source/package checks for the exact component version;
2. representative behavior tests;
3. natural-routing evidence when automatic selection matters;
4. an exact runtime/model receipt where runtime behavior is claimed;
5. real-use/pilot evidence required by the lifecycle policy, or an explicit reviewed exception whose scope and expiry are documented;
6. no unresolved high-severity failure.

`NOT_RUN`/pending is a valid evidence state. It must never be translated to PASS.

Run:

```bash
python scripts/readiness/validate_readiness.py
```

to ensure the readiness registry still matches all production component names, versions and source paths.
