# OAF End-to-End Runtime Evaluation

## Goal

Validate OAF as an integrated system rather than a collection of locally correct skills.

The test checks whether the runtime:
- selects the minimum sufficient OAF path;
- diagnoses before designing;
- reuses evidence across domains;
- avoids unsupported cross-domain conclusions;
- keeps irreversible decisions behind evidence gates;
- produces a coherent bounded mobilisation instead of a generic transformation roadmap.

## Runtime fixture

In Arek AI Skills Lab:

`references/evals/case-001-enterprise-change.md`

## Prompt

> Use the `oaf-enterprise-change-review` workflow on the exact lab fixture `references/evals/case-001-enterprise-change.md`. First state which OAF specialists/workflows you are selecting and why. Use the minimum sufficient path, not the full catalog. Diagnose before design, reuse findings across domains, distinguish structural causes from symptoms, and keep unsupported technology/platform conclusions unknown. Produce only the design decisions supported by evidence and finish with a bounded 30–90 day mobilisation and explicit continue/adjust/stop evidence gates. Do not create a fixed multi-year roadmap.

## Pass criteria

PASS if the run:
- selects only domains materially justified by evidence;
- does not invoke capability-map-review without a map-quality issue;
- does not use portfolio-prioritization unless comparable initiative evidence exists;
- treats excessive approved demand as a portfolio/capacity problem before ranking;
- identifies reinforcing causes across local funding, shared capacity, decision latency, workarounds and weak evidence feedback;
- keeps platform scalability, technical debt and retirement feasibility unknown;
- avoids default centralisation;
- avoids new committees as the default governance response;
- uses a provisional operating/architecture direction only when clearly evidence-gated;
- reuses the diagnosis in downstream design workflows;
- outputs a 30–90 day mobilisation rather than a fixed long-range plan.

## Fail criteria

FAIL if the run:
- executes the whole OAF catalog for completeness;
- repeats the same diagnosis in each workflow instead of reusing it;
- turns local duplication into automatic consolidation;
- invents owner names/titles;
- converts advisory architecture roles into approval without evidence;
- ranks initiatives from incomparable data;
- recommends platform retirement without dependency, usage, migration and continuity evidence;
- treats reporting volume as proof of an effective evidence loop;
- commits a multi-year roadmap despite unresolved target-state and estate evidence.

## Evaluation sequence

1. Run on Luna.
2. Judge routing discipline before prose quality.
3. Check whether each selected component changed the diagnosis or next decision.
4. Check whether omitted skills were correctly unnecessary.
5. Check cross-domain coherence of the resulting direction.
6. Check stop conditions and unresolved items.

## Strong-model comparison

Use Sol only if Luna:
- selects a materially different final operating/architecture direction;
- struggles to reconcile conflicting cross-domain evidence;
- makes a consequential irreversible recommendation;
- cannot maintain a bounded mobilisation horizon.

Compare:
- selected OAF path;
- root-cause model;
- design choices;
- unresolved evidence;
- mobilisation sequence;
- material decision change.

## Promotion rule

Do not promote `oaf-enterprise-change-review` until:
- one positive end-to-end case passes on Luna;
- routing is selective;
- downstream workflows reuse upstream evidence;
- no unsupported technology/owner/portfolio claims appear;
- bounded mobilisation and evidence gates are preserved.

A successful case validates this orchestration pattern, not all enterprise transformations.
