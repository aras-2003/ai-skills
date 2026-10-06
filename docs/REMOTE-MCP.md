# Remote MCP deployment contract

`runtime/mcp/server.py` is the single MCP entrypoint for local and remote
profiles. The compatibility path `runtime/mcp/cloud_server.py` delegates to it.
It exposes these headless tools:

- `route_investment_request`
- `render_bar_chart`
- `render_line_chart`

The bundled skills remain the source of workflow instructions. The remote
server only provides deterministic routing/rendering capabilities; it is not a
replacement for the skill layer. Routing does not execute the selected
workflow. For investment requests, the server returns
`execution_state: routed_only` and `workflow_executed: false`. The host must
stop without substantive investment output until it actually executes the
selected workflow. These instructions are model-facing guidance rather than a
technical enforcement boundary, so each supported host still needs a runtime
evaluation that proves routing and stop behavior in a fresh chat.

## Required deployment properties

The chosen host must:

1. expose the ASGI `app` from `runtime/mcp/server.py`;
2. serve streamable HTTP MCP at a stable HTTPS `/mcp` endpoint;
3. enforce authentication at the edge when the endpoint is not strictly
   private to the owner;
4. keep secrets and user credentials outside the repository and runtime
   source tree;
5. provide health checks, request logs without sensitive prompt contents, and a
   rollback path for incompatible tool schemas.

The repository intentionally does not choose a cloud vendor or commit a
deployment credential. A concrete host and endpoint are release inputs, not
source defaults.

## Package after deployment

```bash
python scripts/package/build_plugin.py \
  --runtime-mode remote \
  --remote-mcp-url https://<your-host>/mcp \
  --output .tmp/chat-web
python scripts/package/artifact_validation.py .tmp/chat-web
```

The resulting profile contains the production skills and an HTTPS MCP mapping,
but no bundled local MCP executable. For mobile Chat, build and distribute the
`skills-only` profile instead:

```bash
python scripts/package/build_plugin.py \
  --runtime-mode skills-only --output .tmp/chat-mobile
python scripts/package/artifact_validation.py .tmp/chat-mobile
```

Do not mark the remote profile as mobile-compatible merely because the package
build succeeds. Mobile MCP support is a host capability and must be validated
separately from repository/package validation.
