# Skills Factory agent instructions

For Skills Factory Cloud Next publication, read `docs/SITES-PUBLISHING.md` from this repository's current main and the installed Sites hosting skill. If a local checkout lacks the document or is stale, fetch it with the GitHub connector without resetting or overwriting local edits. The Site source's `PUBLISHING.md` is a mirror, not a separately maintained canonical procedure.

A user publication request authorizes ordinary in-scope work. Network/terminal approval and credential-delivery approval are separately enforced. Hidden stdin prevents display but does not authorize transfer. DNS failure is not an approval rejection; use the runbook's reviewed execution path. If credential delivery is explicitly rejected, stop that path, preserve edits and report the actual reason. Do not reroute a rejected transfer or assume a model/chat switch supplies permission. Do not invent a user approval button.

GitHub source and the Sites source repository are separate. GitHub main updates do not publish the Site. Use the official Sites workflow and native deployment tools; Git inside that workflow is expected. Preserve source history, Site/plugin identity and audience. Confirm the actual deployed version and SHA, separately from embedded Lab provenance. For Chat tests, explicitly select Cloud Next and verify actual tool invocation.
