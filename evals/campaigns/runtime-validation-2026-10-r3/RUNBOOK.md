# Runtime Validation Campaign R3 — post-R2 retest

## Identity

- campaign: `runtime-validation-2026-10-r3`
- behavior source: `cde46f59c20a0d4313528185e5df079335633b10`
- core case count: **38**
- supplemental routing cases: mixed interface diagnosis plus adjacent decision-bottleneck and decision-rights intents.

Historical R1/R2 receipts remain bound to their original behavior source and status. Do not reinterpret them against R3.

## Prepare

~~~bash
python scripts/eval/campaign.py validate
python scripts/eval/campaign.py prepare --output .tmp/runtime-campaign-r3
python scripts/eval/campaign.py queue --include-supplemental --output .tmp/runtime-campaign-r3/QUEUE.md
python scripts/eval/campaign.py validate-lock --lock .tmp/runtime-campaign-r3/lock.json
~~~

Always use the lock produced by this exact checkout. R2 locks are not valid for R3.

## Independent executor

Use a fresh session that has not seen evaluator rubrics or prior findings. Enable only the channel assigned in the lock. Capture independently observed smoke before the business input. Do not copy identity fields from the lock.

Offline test definitions and CI checks are not runtime PASS.

## Retest focus

Primary changed behavior:
- `fallback-strategy-production-002` — bounded evidence sample and consequence discipline;
- `oaf-interface-natural-pl` — mixed interface/accountability/capacity routing should lead with operating-model-review.

Control / neighboring intents:
- `fallback-interface-explicit-production-002` — preserve the previously correct explicit fallback behavior;
- `oaf-decision-bottleneck-natural-pl` — identified decision-latency class;
- `oaf-decision-rights-natural-pl` — identified decision ownership/authority question.

Use only executor input files from the generated retest pack. Rubrics are evaluator-only.

## Evidence status

No R3 runtime PASS exists when this file is authored. R1 and R2 results remain historical evidence with their original statuses.
