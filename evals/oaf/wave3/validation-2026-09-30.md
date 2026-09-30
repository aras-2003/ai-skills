# OAF Wave 3 Validation — 2026-09-30

## Runtime

Primary model: Luna. Comparison model: Sol for `oaf-transformation-design` only.

The lab eval-fixture discovery blocker was fixed before behavioral validation. Subsequent runs used the exact packaged fixtures under `references/evals/`.

## Results

| Component | Result | Disposition |
|---|---|---|
| governance-design | PASS+ on Luna | promote |
| transformation-blueprint positive | PASS+ on Luna | promote |
| transformation-blueprint stop condition | PASS++ on Luna | promote |
| oaf-governance-redesign | PASS++ on Luna | promote |
| oaf-transformation-design | PASS++ on Luna | promote |

## Governance design

Validated:
- decision-led, not committee-led;
- direct rights / standing rules / asynchronous mechanisms preferred where sufficient;
- remove/merge/narrow before adding;
- advice separated from approval;
- no invented owner identity;
- bounded architecture-exception mechanism;
- effectiveness measured through decision lead time, rework, escalation, exception quality and meeting load.

Regression:
- governance design is not meeting design;
- retain an existing forum only when the material decision need still requires it.

## Transformation blueprint

Positive case validated:
- diagnosis-to-workstream traceability;
- `owner-to-confirm` for unresolved ownership;
- capacity/dependencies on the critical path;
- bounded 30–90 day mobilisation;
- reversible pilots and coexistence;
- continue / adjust / stop gates;
- conditional longer horizon rather than a fixed multi-year roadmap.

Stop-condition case validated:
- stopped when target direction, decision rights, funding model and architecture direction were unresolved;
- did not invent workstreams, owners or dates;
- proposed only a bounded target-direction/evidence phase.

Regression:
- a request for a roadmap does not override blueprint preconditions;
- unresolved target state -> stop -> resolve design boundary -> blueprint later.

## Governance redesign

Validated:
- diagnosis reused;
- decision-rights fixes separated from governance mechanisms;
- overlapping portfolio mechanisms merged/removed;
- below-threshold funding escalation treated partly as accountability behavior;
- architecture/security hidden vetoes removed where policy is advisory;
- steering narrowed to material unresolved escalations;
- risk control preserved through evidence, ownership, thresholds, expiry/review and escalation;
- bounded pilot and effectiveness measures included.

## Transformation design

Luna validated:
- selected federated direction reused;
- 90-day boundary explicit;
- deferred enterprise rollout and permanent appointments;
- `owner-to-confirm` preserved;
- constrained global data-team capacity treated as primary critical-path resource;
- foundations -> reversible pilot -> evidence -> conditional scale;
- service continuity protected;
- no fixed multi-year roadmap.

A Sol run of the same case was executed before the intended Luna run and retained as a comparison. Sol had slightly stronger narrative framing, but no material change in sequence, risk posture or recommended plan. It also used a `mobilisation sponsor` label at a gate without explicit authority evidence; the Luna run stayed more conservative with unresolved ownership.

Material decision change between Luna and Sol: **No**.

## Promotion

Promote:
- `governance-design`
- `transformation-blueprint`
- `oaf-governance-redesign`
- `oaf-transformation-design`

Routing:
- standard/Luna for tested bounded design uses;
- strong/Sol only for final high-impact authority selection, enterprise-wide multi-year sequencing, material transition economics, highly coupled global programs or contested target-state assumptions.
