# Lab 0.33.7 — R17 remediation and Cloud migration

## Scope

Addresses the nine R17 transcript FAIL verdicts: CV factual scope/source authority; company research contaminated by earlier recruitment context; OAF final decision authority vs known-owner bottlenecks; Investment OS routing, exact child load and execution evidence; portfolio renderer receipt. Historical R17 verdicts remain 36 PASS / 9 FAIL. Source changes and offline checks are not a fresh Chat E2E result.

The source fixes affect Lab and the shared skills it packages. Production-specific fallback cases remain excluded from this Lab campaign. No data/schema migration, credential change, new Site or new plugin is required.

## Two separate source layers

1. Merge this repository change only after required `Validate skills` and `Domain integrity` CI pass.
2. Obtain the successful `Package main Lab plugin` artifact for that exact merged main SHA. Validate its release manifest: Lab 0.33.7, source_revision equal to main SHA. Retain ZIP hash and artifact/run IDs.
3. In the existing Site checkout, apply `site-runtime.patch` against Site source `bc94902ba6e500a99030253c50bfa2345605daf2` if those changes are not already present. Do not apply twice or overwrite divergent work.
4. Run the existing `scripts/sync-lab-catalog.py` and `scripts/sync-lab-references.mjs` against the exact extracted CI artifact. Update the contract test's Lab version, source SHA, artifact hash and Investment OS workflow blob hash to the observed new artifact values.
5. Run Site contract tests, TypeScript and official Site build. Publish the matching source and archive only through the current `docs/SITES-PUBLISHING.md` procedure.

GitHub main alone does not update the deployed MCP. The Site source SHA and embedded Lab source SHA represent different layers and must both be checked.

## Current publication constraint

During preparation, platform auto-review rejected live Sites repository-write credential delivery to an elevated terminal. The waiting official workflow was cancelled. No changed Site source was pushed or deployed. Do not retry token delivery through another process, file, environment variable, wrapper or newly minted credential. Resume only with a supported protected credential channel and platform approval, or genuinely new evidence permitting normal re-evaluation. Earlier successful runs and model changes do not override this rejection.

## Runtime acceptance after approved publication

Check owner-only access, exact deployed Site SHA and `runtime_info` verified attestation. Confirm catalog Lab 0.33.7 with exact main artifact SHA. Run all 45 active Lab cases in ordinary Chat, at most four tabs, independent evaluation in a separate Chat. Retest the nine historical failures first, then the remaining passing cases to detect regressions. Record actual router calls, exact child loads and renderer receipts; never substitute declared execution for observed execution. Preserve missing evidence as unresolved, not PASS.

## Rollback

Retain live version 16 and its source `bc94902ba6e500a99030253c50bfa2345605daf2`. If the new publication fails runtime acceptance, restore the saved previous version through native Sites operations and align runtime attestation with its source. Do not pair a new archive with the old SHA.
