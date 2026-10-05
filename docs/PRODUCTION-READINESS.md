# Production readiness evidence — AIS-21

`release/production-readiness.yaml` is the machine-checkable record for every currently declared production skill/workflow.

## What the record means

This review does **not** mass-promote or mass-downgrade components. It distinguishes:
- declared maturity;
- static contract/test presence;
- exact-version runtime evidence;
- remaining evidence gaps and temporary disposition.

After evaluator-rubric isolation changes, historical narrative PASS/PASS++ summaries are not treated as exact-version unassisted receipts. Where no matching receipt exists, `current_runtime_receipt: pending` is explicit.

Existing production maturity may be retained temporarily for review rather than silently re-certified. Each pending record must identify the exact component/version, evidence gap, limitation, owner, explicit exception scope and expiry. This R7 personal-beta disposition applies only to components already declared production; it does not authorize a new promotion, changed version, expanded scope or wider audience. No exception can cover a known unresolved high-severity failure.

## Promotion/readiness rule

A future new promotion or re-certification should require:
1. static/source/package checks for the exact component version;
2. representative behavior tests;
3. natural-routing evidence when automatic selection matters;
4. an exact runtime/model receipt where runtime behavior is claimed;
5. real-use/pilot evidence required by the lifecycle policy for new promotions; the temporary R7 continuation exception is limited to existing declared production components and does not waive new-promotion gates;
6. no unresolved high-severity failure.

`NOT_RUN`/pending is a valid evidence state. It must never be translated to PASS.

Run:

```bash
python scripts/readiness/validate_readiness.py
```

to ensure the readiness registry still matches all production component names, versions and source paths.
