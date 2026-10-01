# Eval results

Store reviewable runtime evidence receipts here when the underlying output is safe for the repository.

Do not fabricate historical outputs. Existing narrative validation summaries remain historical context only and do not automatically become receipts for current component versions.

When an actual output contains private material, keep the output in an approved private location and record only the controlled reference plus content digest in the receipt.

Current critical cases require fresh unassisted runs under the isolated-input protocol. Until those runs exist, their runtime status is pending / NOT RUN rather than inherited PASS from older summaries.

## Current committed runtime evidence

Two real production fallback runs are retained as historical **FAIL** evidence under `evals/results/runtime-campaign/`: `fallback-strategy-production-001` and `fallback-interface-production-001`, both bound to behavior source `ff012e494f5b2f71803f850d71d20f54a3315e2b`.

Their status must not be upgraded because later behavior changed. R2 additionally records `fallback-strategy-production-002` = FAIL, `fallback-interface-explicit-production-002` = PASS and `oaf-interface-natural-pl` = FAIL against behavior source `c0772e2e3727971b2e3fe8f9d56eccf6bdd87129`. The active R3 campaign has no runtime PASS.
