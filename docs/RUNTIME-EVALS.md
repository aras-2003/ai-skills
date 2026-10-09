# Runtime evaluation protocol

## Goal

Test candidate skills and workflows in the actual skill runtime before promoting them to production.

Static CI proves package quality. Runtime evals prove behavior.

## Lab plugin

`Skills Factory Lab` packages:
- every skill with `metadata.maturity: candidate` from `main`;
- selected workflow entrypoints needed for runtime orchestration.

The lab plugin is intentionally separate from `Skills Factory` production.

Executor input fixtures are stored at the Lab package root under
`executor-inputs/<target>/`, indexed by `executor-inputs.json`. They are not
placed under a skill's `references/` directory and their paths are not appended
to model-loadable `SKILL.md` instructions. Rubrics remain evaluator-side and
must not enter the Lab package. `load_skill` filters legacy eval appendices and
does not include files from eval/test directories in its public reference
inventory or content digest.

## Recommended evaluation sequence

### 1. Explicit skill execution
Invoke the exact skill by name and run one positive case.

Check:
- procedure adherence;
- output contract;
- evidence discipline;
- model-class adequacy.

### 2. Boundary test
Run a near-miss case.

Check that the skill does not expand into adjacent tasks.

### 3. Missing/conflicting evidence
Run the uncertainty/regression case.

Check that the runtime does not invent facts.

### 4. Workflow orchestration
Invoke the workflow entrypoint explicitly.

Check:
- selective routing;
- ordering of skills/gates;
- cross-domain synthesis;
- stop conditions.

### 5. Model-class comparison
For skills tagged `fast` or `standard`, run the same case on the intended cheaper model and on the stronger reference model when possible.

Compare observable output on:
- task completion;
- evidence accuracy;
- routing/boundary discipline;
- output contract;
- correction required;
- concision/context cost.

Do not promote a cheaper model class merely because it produces plausible prose.

MCP receipts distinguish tool execution from workflow execution. A
`tool_receipt.execution_state: executed` records that the MCP tool returned a
result; it does not imply that the routed workflow was executed. Routing
results preserve `execution_state: routed_only` for compatibility and also
report `workflow_execution_state: not_executed`, `workflow_executed: false`,
`outcome: null`, and a reason. Chart receipts may establish that a PNG payload
was rendered and hashed, but `client_display_state: not_observable` means they
do not prove that the host displayed it. Receipts are unsigned integrity records,
not cryptographic deployment attestations.

## Promotion rule

Promote a candidate only when:
- static validation passes;
- representative positive/negative/uncertainty cases pass;
- no severe routing or evidence regression exists;
- the intended model class is adequate for normal cases;
- runtime failures have been converted into regression tests.

## OAF first implementation case

Use:
`evals/oaf-health-check/case-001-enterprise-it.md`

Recommended first pass:
1. explicit `oaf-health-check`;
2. observe which OAF skills are selected;
3. rerun one selected skill independently;
4. compare its finding with the workflow synthesis;
5. record PASS / ITERATE / REJECT and smallest fix.
