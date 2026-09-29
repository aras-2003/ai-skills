---
name: arek-skills-diagnostic
description: >
  Confirm that the Arek AI Skills plugin is exposing bundled skills to ChatGPT or Codex.
  Use when the user explicitly asks to test, verify, diagnose, or confirm whether Arek AI Skills is active.
metadata:
  owner: arkadiusz-kamrowski
  version: "1.0.0"
  maturity: production
  risk: low
  last_reviewed: 2026-09-30
---

# Arek Skills Diagnostic

## Purpose

Verify that the installed Arek AI Skills plugin exposes bundled skills to the runtime.

## Procedure

When invoked for an explicit plugin/skill availability test:

1. State exactly: `AREK_AI_SKILLS_ACTIVE`.
2. List this skill name: `arek-skills-diagnostic`.
3. State that the runtime successfully loaded the skill instructions.
4. Do not claim that other skills are available unless they are actually visible to the runtime.

## Output contract

Keep the response to at most three short lines.

## Quality checks

- Do not emit the marker unless this skill was actually loaded.
- Do not infer availability from the plugin mention alone.
