# Meta skills — creating and governing skills

These skills are used to design, write, test, validate and promote other skills.

They are intentionally separated from domain skills because they govern the capability library itself.

## Meta-skill chain

```
skill-specification
  -> skill-authoring
     -> skill-validation
        -> skill-test-design
           -> skill-evaluation
              -> skill-release-review
```

Not every change requires every stage:
- typo/docs-only change: validation may be sufficient;
- description/routing change: add routing tests and evaluation;
- behavior change: full behavioral regression;
- new production skill: full chain required.

## Meta skills

| Skill | Purpose |
|---|---|
| `skill-specification` | Decide whether a task should become a skill and define its behavioral contract. |
| `skill-authoring` | Create or refactor a skill according to repository and Agent Skills conventions. |
| `skill-validation` | Check structure, standards, boundaries, safety, portability and static quality. |
| `skill-test-design` | Design representative routing, behavior, edge and regression tests. |
| `skill-evaluation` | Evaluate behavior against baseline/previous version and diagnose regressions. |
| `skill-release-review` | Decide whether a candidate is ready for production promotion. |

The workflow orchestration is defined in `workflows/skill-development/WORKFLOW.md`.
