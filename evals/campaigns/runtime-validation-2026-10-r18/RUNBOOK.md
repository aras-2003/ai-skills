# R18 — Lab 0.33.7 regression campaign

Behavior source: `e51df8120031726a59f6f2acabf1bf7c021c94a4`. This commit adds the investment-attention materiality fix; later commits may only change campaign/test/deployment documentation without changing this behavior pin.

Execute the same 45 Lab cases and unchanged rubrics as R17, using the exact merged-main Lab 0.33.7 CI artifact. Keep both Production-only fallback cases excluded. Execute in ordinary Chat, maximum four tabs, with independent evaluation in another Chat. Start with the nine historical failures listed in `evals/results/runtime-campaign-r17/SUMMARY.md`, then run remaining cases.

Use `campaign.py prepare` to create the lock for the new artifact. Verify the installed Lab identity and retain actual output, trace, routing/child-load/renderer receipts and independent assessment. Import full evidence through `campaign.py import-run`; do not turn transcript-only references into machine-valid receipts. Missing client display remains pending when required. Never reuse R17 PASS verdicts as R18 results.

Deployment preparation and platform constraint: `docs/releases/r18/MIGRATION.md`.
