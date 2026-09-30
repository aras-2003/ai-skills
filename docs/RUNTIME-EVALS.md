# Runtime evaluation protocol

## Goal

Test candidate skills and workflows in the actual skill runtime before promoting them to production.

Static CI proves package quality. Runtime evals prove behavior.

## Lab plugin

`Arek AI Skills Lab` packages:
- every skill with `metadata.maturity: candidate` from `main`;
- selected workflow entrypoints needed for runtime orchestration.

The lab plugin is intentionally separate from `Arek AI Skills` production.

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
