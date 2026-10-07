# Publishing Skills Factory Cloud Next — agent runbook

This procedure is for Luna as well as Sol. The model does not determine network availability. Verified on local Codex/macOS for Site versions 8 and 9; the same workflow successfully opened the source again on 2026-10-07 after a sandbox DNS failure.

## Identity and authorization

- Reuse `.openai/hosting.json` project ID: `appgprj_6ac56f2116588191a4a1ebc682c97865`.
- Site: Skills Factory Cloud Next, `https://skills-factory-cloud-next.arek2003.chatgpt.site/`.
- Source checkout in this machine: `/private/tmp/codex-skills-site`; verify it instead of assuming that a temporary directory still exists.
- GitHub `aras-2003/skills-factory` and the Sites source repository are separate repositories. Merging GitHub main does not publish the Site or automatically refresh its embedded Lab artifact.
- A request to publish is authorization for publishing the agreed changes. No additional conversational confirmation is needed. Platform approval review still applies.

## Required capabilities

Read the installed `sites-hosting` skill and discover native Sites tools: `get_site`, `create_source_repository_write_credential`, `update_environment_variables`, `save_version_and_deploy_private`, `get_deployment_status`, `list_site_versions` / `get_site_version`.

Use the current installed Sites plugin path from the skill catalog. In this verified session it is `/Users/arkadiuszkamrowski/.codex/plugins/cache/openai-curated-remote/sites/0.1.75`. Do not hard-code that version for future installations.

The native plugin provisions credentials, configures runtime and publishes versions. Its official local `scripts/site-workflow.mjs` synchronizes the source using Git internally. There is no discovered native tool that uploads arbitrary source files directly; do not invent one. Do not use an ad-hoc authenticated `git push`.

## Execution steps

1. Call `get_site`. Verify the existing identity, current version, authenticated owner role and owner-only access. Preserve Site/plugin identity and access.
2. Test HTTPS without credentials: `curl --connect-timeout 10 --max-time 20 --silent --show-error --output /dev/null --write-out 'HTTP_STATUS=%{http_code}\nTLS_VERIFY=%{ssl_verify_result}\n' https://git.chatgpt-team.site/`. HTTP 400 with TLS verification 0 is sufficient transport evidence for this root URL; it is not a Git permission test.
3. If the local sandbox returns `Could not resolve host`, retry that credential-free check with `sandbox_permissions: require_escalated`. This is the normal approval mechanism, not a change to security settings. A failed sandbox request alone does not establish a platform rejection. If automatic approval review actually rejects the action, report its stated reason and stop that rejected path.
4. Launch the official workflow from the selected checkout with `exec_command`, `tty: true`, `yield_time_ms: 1000`: `node <plugin-root>/scripts/site-workflow.mjs --project-id <project_id>`. When local sandbox networking is unavailable, use `require_escalated`. The justification must state the full operation: local network access plus a fresh short-lived repo-scoped Sites credential delivered only through hidden stdin, opening/checking/building/normal source push and private publishing. Do not request networking approval while hiding that the process will receive a credential.
5. Wait for `Ready for Site workflow JSON on stdin (input is hidden).` Then obtain a fresh credential through the native plugin. Keep it only in orchestration memory. Send a newline-terminated JSON object through `write_stdin` with `{credential}` and `yield_time_ms: 30000`. Never put the token in shell arguments, files, environment configuration, logs or user messages. Do not copy a credential from previous attempts.
6. Wait for successful exit and retain the returned `source` object (`project_id`, `checkout_path`, `commit_sha`). If local edits already exist, preserve them; the workflow rejects incompatible remote history safely. Inspect relevant source and make scoped changes.
7. Prepare dependencies only when needed. Existing working `node_modules` may be reused while dependency inputs are unchanged. The Linux installer requires `flock` and GNU `timeout`; do not repeatedly reinstall or change the lockfile to solve this on macOS. Use the Sites execution-profile guidance for a new dependency installation. Run TypeScript with `--incremental false` so validation does not alter tracked `tsconfig.tsbuildinfo`.
8. Launch the same official workflow in the same approved execution context. Send `{credential, source, commands, archivePath}` through hidden stdin. If the credential expired, obtain a fresh one through the plugin. Use absolute archive path and literal argument arrays. Remaining checks/build:
   - `["node", "node_modules/typescript/bin/tsc", "--noEmit", "--incremental", "false"]`
   - `["node", "scripts/check-contracts.mjs"]`
   - `["node", "<plugin-root>/scripts/build-site.mjs"]`
   The workflow checks, builds, commits source, pushes normally, verifies remote HEAD and packages the archive. Never bypass a failed push by saving an archive against an older SHA.
9. Only after successful workflow, use its exact returned SHA and archive. Update the non-secret runtime keys `SKILLS_FACTORY_RELEASE_ID` and `SKILLS_FACTORY_SOURCE_REVISION` to that SHA, and `SKILLS_FACTORY_DEPLOYED_AT` to current UTC time using the native plugin.
10. Call native `save_version_and_deploy_private` with exact returned project ID, SHA and archive. If a save succeeded but deploy failed, retain the saved version ID and retry deployment rather than creating duplicate versions. Poll a non-terminal deployment to `succeeded` or `failed`.
11. Confirm the actual saved version number and source SHA with native Sites tools. Confirm Cloud MCP `runtime_info` reports `verified` and the same Site SHA; check catalog and change-specific regression. For a chart change, inspect the SVG payload; claim inline Chat rendering only after visibly observing it in Chat.
12. Report deployed version, source SHA, deployment result, tests and remaining failures. A local build, GitHub merge or saved version alone is not proof of a live publication. Normal source updates reuse the existing plugin; installation refresh is only investigated if discovery actually changes or becomes stale.

## Automatic private publication exception

If credentials are requested with `publish_on_push: private`, only skip native save/deploy when the returned `publish_on_push_accepted` is true. Reconcile the matching deployment rather than publishing twice. This runbook defaults to ordinary credentials and explicit private save/deploy so Site environment attestation can be set to the pushed SHA before deployment.

## Failure decisions

- Sandbox DNS failure: use the approved local execution path above.
- Cloud `proxy:8080` connection failure: domain allowlists cannot repair an unreachable proxy. Use the already authorized local Codex procedure if available; do not send the user through repeated Cloud setup.
- Missing Sites tools: report the precise missing capability; changing internet settings does not install tools.
- Platform approval rejection: quote the actual rejected action and reason. Do not describe a DNS failure as an approval rejection.
- Failed tests, divergent source or rejected backend authorization: retain source and report the actual error. Do not force-push, substitute another Site or weaken access.

## Chat regression

Open a fresh ordinary Chat and explicitly select `@Skills Factory Cloud Next` from the plugin menu. Verify that an actual tool invocation is visible. Test prompts and model statements alone do not prove that MCP ran. Site source revision and embedded Lab source revision identify different layers; compare each against its corresponding source.
