---
mode: agent
---

# /md-prompt-dashboard-redesign-by-type (GitHub Copilot)

Type-specialized wrapper prompt for dashboard redesign workflows under `dashboards/<name>/`.

This prompt is intended to be used with one of the following command patterns so users can choose the target dashboard type directly.

## Quick usage

```text
/md-prompt-dashboard-redesign-by-type operational <name>
/md-prompt-dashboard-redesign-by-type executive-insight <name>
/md-prompt-dashboard-redesign-by-type executive-decision <name>
/md-prompt-dashboard-redesign-by-type executive-storytelling <name>
/md-prompt-dashboard-redesign-by-type new <name>
```

## Behavior

- If mode is `new`:
  - scaffold `dashboards/<name>/` and its subfolders directly, without creating or depending on a shared `dashboards/_template/` folder
  - do not overwrite if folder already exists unless explicitly requested

- If mode is one of the four type modes:
  - run the full redesign pipeline for `dashboards/<name>/`
  - force the mapped type
  - produce outputs in `dashboards/<name>/outputs/`

## Mode to type mapping

- `operational` -> `operational-insight-driven`
- `executive-insight` -> `executive-insight-driven`
- `executive-decision` -> `executive-decision-driven`
- `executive-storytelling` -> `executive-data-storytelling`

## Input validation before pipeline

- Require at least one screenshot in `dashboards/<name>/inputs/screenshots/`.
- If `requirements/` is empty, proceed with explicit caveats.
- If `sample_data/` is empty, allow Stage 1-2 only; stop before Stage 3 and request extracts.

## Required outputs

- `outputs/01-current-state-teardown.md`
- `outputs/02-redesign-recommendations.md`
- `outputs/03-data-model.md`
- `outputs/04-data-flow-spec.md`
- `outputs/dashboard-redesign.html`

## Design references

Always use:
- `../skills/md-dashboard-redesign/reference/executive-decision-driven-design.md`

And additionally use type-specific reference based on selected mode:
- operational: `../skills/md-dashboard-redesign/reference/operational-insight-driven-design.md`
- executive-insight: `../skills/md-dashboard-redesign/reference/executive-insight-driven-design.md`
- executive-decision: `../skills/md-dashboard-redesign/reference/executive-decision-driven-design.md`
- executive-storytelling: `../skills/md-dashboard-redesign/reference/executive-data-storytelling-design.md`

## Ground rules

- Every recommendation must be traceable to screenshots, requirements, or sample data.
- Do not invent missing stage-critical inputs.
- Treat markdown stage files as source of truth and HTML as presentation layer.
