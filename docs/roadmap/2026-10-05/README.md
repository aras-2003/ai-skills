# AI Skills expansion roadmap — 2026-10-05

This directory preserves the expansion analysis and 55 proposed development tasks. It is a planning artifact, not a release or runtime-readiness declaration.

## Start here

1. Read [the proposal and full backlog](PROPOSAL-AND-BACKLOG.md) for architecture boundaries, rationale, flows and rollout order.
2. Use [BACKLOG.json](BACKLOG.json) as the source of truth for task status, ownership, dependencies and acceptance criteria.
3. [BACKLOG.csv](BACKLOG.csv) is a derived import/export view. Regenerate it from JSON after changes; do not maintain a second independent task state.

The proposal is a dated analytical snapshot. Its source revision and installed runtime identity are recorded inside it. The main baseline when saving these documents was `007f659995945084ce18e4ca62b38c92523e414a`; some documentation findings were already corrected after the analysis. Recheck current source and evidence before implementing any task. Do not reopen resolved AIS/RT findings from historical descriptions alone.

## Development handoff

- Start with reconciliation and the existing Skill Engineering chain, then pilot Consumer purchases and article development.
- Select a task by its stable ID; confirm its dependencies and current need before implementation.
- Record owner and status in JSON: `PROPOSED`, `DISCOVERY`, `IN_PROGRESS`, `BLOCKED`, `DONE` or `DEFERRED`. Record blockers explicitly; never mark completion from a plan or static validation alone.
- Keep acceptance criteria intact. Add implementation PR/commit and evidence references when a task progresses; retain historical findings.
- Update task state in the implementation PR so future development starts from the current backlog.
- Use project context for private profiles and state, skills for methods, workflows for orchestration, scripts for deterministic work, and existing connectors for actions.
- New IDs supplement AIS/RT and do not replace those backlogs.
- Preserve the original analysis when decisions change; append a dated decision note or link an architecture decision rather than silently rewriting history.

Saving and merging this roadmap does not authorize execution of all proposed tasks, production promotion, purchases, external messages or publication.
