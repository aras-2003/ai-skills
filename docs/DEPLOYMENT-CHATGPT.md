# Deploying production skills to ChatGPT / Codex

## Goal

Keep GitHub as the source of truth and expose only production-ready skills through one installable plugin.

## Why one plugin

Bundling related skills into one plugin gives:
- one installation surface instead of one install per skill;
- simpler routing and lifecycle management;
- a stable plugin identity while individual skills evolve;
- cleaner separation between development skills and production skills.

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

The Skills UI can still be used for individually created/uploaded skills. For this repository, prefer the plugin bundle for production distribution because it keeps lifecycle/versioning centralized.

## Release rule

Never package from `main`.
The installable plugin always tracks `production`.
