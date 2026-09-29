# Deploying production skills to ChatGPT / Codex

## Goal

Keep GitHub as the source of truth and expose only production-ready skills through two delivery paths: one installable plugin for Work/Codex-style plugin runtimes, plus individually packaged native ChatGPT Skill bundles for ordinary Chat where the Skills feature is available.

## Why dual deployment

The plugin remains the preferred bundled distribution for Work/Codex because it provides one installation surface and one stable plugin identity.

Ordinary Chat can expose skills differently from Work/Codex. To avoid coupling daily Chat usage to local-marketplace plugin runtime behavior, production also generates one native skill ZIP per production skill.

See `DEPLOYMENT-CHATGPT-CHAT.md` for the ordinary-Chat installation path.

## Production packaging flow

```
feature branch
  -> PR to main
  -> static validation
  -> behavioral eval
  -> release review
  -> promotion to production
  -> package-production-plugin.yml
  -> plugins/arek-ai-skills/
  -> repo marketplace
```

Only skills whose frontmatter contains:

```yaml
metadata:
  maturity: production
```

are copied into the installable plugin.

The packaging step flattens the repository's domain structure:

```
skills/career/role-fit-analysis/
```

into the plugin format required by OpenAI:

```
plugins/arek-ai-skills/skills/role-fit-analysis/
```

so every bundled skill is an immediate child of `skills/`.

## Initial installation

On a supported ChatGPT desktop/Codex environment, add the Git-backed marketplace:

```bash
codex plugin marketplace add aras-2003/ai-skills --ref production
```

Then refresh/restart the ChatGPT desktop app and install **Arek AI Skills** from that marketplace if the client still asks for confirmation.

The marketplace declares `INSTALLED_BY_DEFAULT`. This is useful for supported local/repo marketplace clients, but it is not the same as an account-wide cloud installation policy.

## Updating

Refresh the Git marketplace:

```bash
codex plugin marketplace upgrade
```

or:

```bash
codex plugin marketplace upgrade arek-ai-skills
```

Then restart/refresh the desktop client if needed.

## Important limitation

OpenAI currently documents automatic installation policies for managed workspaces and local/repo marketplaces, but no public API that lets a personal GitHub Actions workflow silently install or replace a skill on an individual ChatGPT account.

Therefore:
- production packaging can be fully automated in GitHub;
- marketplace distribution/update can be automated;
- the initial account/client installation still may require explicit user action;
- account-wide silent installation should not be assumed unless OpenAI exposes that capability for the active account/workspace.

## Native Skills page

When the active account exposes the native Skills page, use the generated bundles in `dist/chatgpt-skills/` for ordinary Chat.

Lifecycle and versioning remain centralized in GitHub; the uploaded ChatGPT copy is a deployment target, not the source of truth.

## Release rule

Never package from `main`.
The installable plugin always tracks `production`.
