# Workflows

Workflows compose skills into repeatable end-to-end processes with entry criteria, dependency handling, gates, stop conditions and output contracts.

## Implemented workflow sources

Current `WORKFLOW.md` implementations:
- `commerce-opportunity-review`
- `commerce-product-deep-dive`
- `oaf-health-check`
- `oaf-operating-model-redesign`
- `oaf-governance-redesign`
- `oaf-enterprise-architecture-review`
- `oaf-transformation-design`
- `oaf-enterprise-change-review`
- `oaf-strategy-execution-reset`
- `skill-development`

Not every workflow is a production runtime entrypoint.

## Runtime workflow availability

`workflows/runtime-registry.yaml` is authoritative for plugin/Lab workflow entrypoints and dependency behavior.

Current production-maturity runtime workflows include:
- `commerce-opportunity-review`
- `commerce-product-deep-dive`
- `oaf-health-check`
- `oaf-operating-model-redesign`
- `oaf-governance-redesign`
- `oaf-enterprise-architecture-review`
- `oaf-transformation-design`
- `oaf-enterprise-change-review`

`oaf-strategy-execution-reset` is candidate maturity and belongs to controlled evaluation/Lab rather than the production plugin.

`skill-development` is a repository engineering workflow and is not implied to be a user-facing runtime entrypoint unless explicitly registered.

## Dependency behavior

Required and optional dependencies are declared in the runtime registry. Missing optional specialists must be handled explicitly according to `on_missing`; workflows must not silently simulate an unavailable dependency.

Examples:
- `oaf-health-check` may narrow a branch when a specialist is unavailable;
- `oaf-operating-model-redesign` must disclose a missing `organizational-interface-review` when interface analysis is material, keep interface-specific causes provisional and preserve a lower-disruption option;
- design workflows stop before unsupported downstream design when required evidence/capability is absent.

## Workflow design contract

Workflows should define:
- entry conditions;
- required inputs;
- dependency/skill sequence;
- evidence gates and stop conditions;
- outputs;
- quality checks;
- escalation/human decision points.

Runtime availability must be read from the generated channel manifest, not inferred from this README or source presence alone.
