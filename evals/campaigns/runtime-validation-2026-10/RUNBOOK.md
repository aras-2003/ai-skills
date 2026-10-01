# Runtime Validation Campaign — 2026-10

## Scope

This campaign prepares, but does not execute or certify, runtime evidence for:

- Commerce cases 001–006 from \`evals/runtime-fixtures.yaml\`;
- all 16 natural-routing cases from \`evals/routing/registry.yaml\`;
- \`executive-role-001\` through \`executive-role-014\`;
- two production fallback cases for unavailable optional OAF specialists.

Behavior source is pinned to:

\`ff012e494f5b2f71803f850d71d20f54a3315e2b\`

The campaign PR may add eval tooling and fixtures after that commit, but \`campaign.py validate\` blocks the campaign if \`skills/**\`, \`workflows/**\` or \`release/package.yaml\` changed after the pinned behavior source.

Offline checks and routing proxies are not runtime PASS.

## 1. Prepare the campaign

From the campaign branch:

~~~bash
python scripts/eval/campaign.py validate
python scripts/eval/campaign.py prepare --output .tmp/runtime-campaign
python scripts/eval/campaign.py queue --output .tmp/runtime-campaign/QUEUE.md
~~~

\`prepare\` builds and validates the production plugin with \`SOURCE_REVISION\` pinned to the behavior SHA. It writes:

- \`lock.json\` — package identity, expected production catalog, component versions and content digests;
- \`QUEUE.md\` — exact executor text for every case;
- \`smoke-template.json\` — fields that must be filled from the actual fresh runtime session;
- \`production-plugin/\` — the exact offline-built package used to establish expected identity.

The two fallback preconditions are checked during preparation: \`strategy-to-execution-diagnostic\` and \`organizational-interface-review\` must not be present in the production catalog.

## 2. Executor/evaluator isolation

Use a fresh executor session for each independent run or for a tightly controlled batch with the same package/runtime identity.

The executor receives only:

1. the exact text from the relevant block in \`QUEUE.md\`;
2. the production package/catalog available in that session;
3. ordinary runtime tools available to that session.

The executor must not receive:

- any \`*.rubric.yaml\`;
- \`skills/career/executive-role-evaluator/tests/cases.yaml\`;
- expected routing targets;
- PASS/FAIL conditions;
- prior outputs for the same case.

This development conversation has seen the rubrics. Output produced here is therefore assisted and cannot be recorded as an independent unassisted PASS.

For natural-routing cases, do not prepend instructions such as “use skill X”. The committed routing inputs and split executive inputs are intentionally free of runtime capability names.

## 3. Installation smoke test

Do not start case execution until the runtime session proves the installed package and catalog.

In the fresh session, capture the actual package/runtime state into a copy of \`smoke-template.json\`:

~~~json
{
  "channel": "production",
  "package": {
    "name": "arek-ai-skills",
    "version": "1.8.0",
    "release_id": "actually-observed-release-id",
    "source_revision": "actually-observed-source-sha",
    "payload_content_sha256": "actually-observed-payload-digest"
  },
  "components": [
    {
      "name": "actually-observed-capability",
      "version": "actually-observed-version",
      "content_sha256": "actually-observed-component-digest"
    }
  ],
  "enabled_packages": ["arek-ai-skills"],
  "catalog": ["actual-capability-name", "..."],
  "runtime": {
    "provider": "actual-provider",
    "model_id": "exact-model-id",
    "reasoning": "exact-setting",
    "available_tools": ["actual-tool-1", "actual-tool-2"]
  }
}
~~~

The values must be observed from the installed runtime artifact, not copied from this example or from `lock.json`. If the runtime cannot expose release ID, source revision, payload digest and component identities, exact-version smoke is **not confirmed** and the run must not be promoted to PASS evidence.

Validate:

~~~bash
python scripts/eval/campaign.py verify-smoke \
  --lock .tmp/runtime-campaign/lock.json \
  --observed /path/to/observed-smoke.json
~~~

The smoke gate rejects:

- wrong or unobserved package name/version/release ID/source revision/payload digest for the declared channel;
- missing or mismatched observed component versions/content digests;
- the required package not enabled;
- production and Lab simultaneously enabled;
- duplicate capability names;
- a runtime catalog different from the locked catalog for that channel;
- missing provider/model/reasoning/tool metadata.

If the installed production version cannot match the lock without publishing or merging, stop. Record the campaign as NOT_RUN; do not substitute the currently published version.

## 4. Execution order

Default order minimizes wasted work:

1. Commerce 001–006 — explicit behavioral regression first;
2. two production fallback cases — verify missing optional-specialist behavior;
3. 16 natural-routing cases — execute each against the channel assigned in `lock.json`; some candidate-target cases require an isolated Lab-only session;
4. executive-role-001…014 — positive and negative trigger regressions last, normally production-only.

Generate the exact queue at any time with:

~~~bash
python scripts/eval/campaign.py queue
~~~

Every queue block contains the complete executor input. Do not add evaluator hints.

## 5. Capture one real run

Save the raw response as \`output.md\`.

Save a minimal trace as JSON:

~~~json
{
  "selected_capabilities": ["capability-actually-selected"],
  "tool_calls": [],
  "notes": "optional factual trace notes only"
}
~~~

For routing cases, \`selected_capabilities\` is required evidence of actual selection. For negative executive-role cases it must not contain \`executive-role-evaluator\`.

The evaluator, in a separate context, loads the case's rubric and the actual output/trace. After evaluation, import the run:

~~~bash
python scripts/eval/campaign.py import-run \
  --case-id case-001-premium-vs-generic \
  --run-id 2026-10-01T101500Z \
  --lock .tmp/runtime-campaign/lock.json \
  --smoke /path/to/observed-smoke.json \
  --output /path/to/output.md \
  --trace /path/to/trace.json \
  --status REVIEW_REQUIRED \
  --reviewer reviewer-id
~~~

Use \`PASS\` only after the separate evaluator has actually established PASS. If the evaluator is uncertain, use \`REVIEW_REQUIRED\`. If the executor saw the rubric or expected answer, pass \`--assisted\`; an assisted run cannot become PASS.

Imported evidence is stored under:

\`evals/results/runtime-campaign/<case-id>/<run-id>/\`

The receipt records:

- pinned behavior source revision;
- case input/rubric digests;
- component name/version/content digest;
- exact runtime provider/model/reasoning;
- actual observed catalog and tools;
- output path/digest;
- trace path/digest;
- reviewer, status and assisted flag.

Paths under the repository are stored relatively, so evidence can be validated after cloning into a different filesystem location.

## 6. Validate imported evidence

~~~bash
python scripts/eval/campaign.py validate-evidence
~~~

Campaign evidence validation checks the receipt against the current case definitions and current component version/content identity while treating the recorded behavior source SHA as immutable run provenance. A later checkout may contain evidence-only commits without invalidating an unchanged tested component.

Do not edit a receipt to upgrade NOT_RUN/REVIEW_REQUIRED to PASS.

## 7. What remains outside this PR

This PR does not:

- execute any provider/runtime case;
- install or publish the plugin;
- merge the A→E PR stack;
- change GitHub settings;
- change licensing;
- extend readiness exceptions;
- promote any pending readiness record.

Commerce 001–006, natural routing and executive-role regressions remain runtime pending until fresh, unassisted exact-version runs have been imported and independently evaluated.
