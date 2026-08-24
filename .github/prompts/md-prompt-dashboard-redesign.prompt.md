---
mode: agent
---

# /md-prompt-dashboard-redesign (GitHub Copilot)

Takes an existing BI dashboard (screenshots + requirements + sample source data extracts) and reworks it around decision-driven design (What / So What / Now What), then proposes the underlying data model and data flows needed to support that redesign.

## Dashboard folders

Each dashboard gets its own folder under `dashboards/<name>/`.

### Runtime structure for an invoked dashboard

```text
dashboards/<name>/
  inputs/
    screenshots/     # PNG/JPG of the existing dashboard — one per view/page/tab
    requirements/    # briefs, stakeholder asks, KPI glossaries, notes (md/txt/docx/pdf)
    sample_data/     # CSV/XLSX extracts of current dashboard source data
  outputs/
    01-current-state-teardown.md
    02-redesign-recommendations.md
    03-data-model.md
    04-data-flow-spec.md
    dashboard-redesign.html
```

## Scaffolding mechanics (required)

When invoked with `/md-prompt-dashboard-redesign new <name>`:

1. Ensure `dashboards/` exists.
2. Create `dashboards/<name>/` and its subfolders directly — do not create or depend on a shared `dashboards/_template/` folder. Generate the structure fresh for this dashboard only.
3. Do not overwrite an existing `dashboards/<name>/` folder unless user explicitly asks.
4. Confirm resulting subfolders exist:
   - `dashboards/<name>/inputs/screenshots/`
   - `dashboards/<name>/inputs/requirements/`
   - `dashboards/<name>/inputs/sample_data/`
   - `dashboards/<name>/outputs/`

## Usage

```text
/md-prompt-dashboard-redesign new <name>                        # scaffold dashboards/<name>/ directly
/md-prompt-dashboard-redesign <name>                            # run the full pipeline end-to-end
/md-prompt-dashboard-redesign <name> --type <dashboard-type>    # force dashboard type
/md-prompt-dashboard-redesign <name> --stage teardown           # run one stage (teardown|recommendations|datamodel|dataflow|publish)
/md-prompt-dashboard-redesign <name> --resume                   # continue from last completed output file
```

## Invocation hints

- Start new dashboard structure:
  - Use `/md-dashboard-redesign new <name>` when `dashboards/<name>/` does not exist.
- Run full pipeline:
  - Use `/md-dashboard-redesign <name>` when inputs are present and you want outputs 01-05.
- Lock type up front:
  - Use `/md-dashboard-redesign <name> --type <dashboard-type>` when audience/workflow is already known.
- Run one stage:
  - Use `/md-dashboard-redesign <name> --stage <stage>` for iterative work or targeted updates.
- Resume interrupted run:
  - Use `/md-dashboard-redesign <name> --resume` to continue from the next missing output.

## Supported dashboard types

Classify into one of four types before Stage 1:

1. `executive-insight-driven`
  - Reference: [../skills/md-dashboard-redesign/reference/executive-insight-driven-design.md](../skills/md-dashboard-redesign/reference/executive-insight-driven-design.md)
2. `executive-decision-driven`
  - Reference: [../skills/md-dashboard-redesign/reference/executive-decision-driven-design.md](../skills/md-dashboard-redesign/reference/executive-decision-driven-design.md)
3. `executive-data-storytelling`
  - Reference: [../skills/md-dashboard-redesign/reference/executive-data-storytelling-design.md](../skills/md-dashboard-redesign/reference/executive-data-storytelling-design.md)
4. `operational-insight-driven`
  - Reference: [../skills/md-dashboard-redesign/reference/operational-insight-driven-design.md](../skills/md-dashboard-redesign/reference/operational-insight-driven-design.md)

Always apply this baseline reference:
- [../skills/md-dashboard-redesign/reference/executive-decision-driven-design.md](../skills/md-dashboard-redesign/reference/executive-decision-driven-design.md)

## Type selection logic

- If formal trigger/owner/authority/sign-off controls are required: `executive-decision-driven`.
- Else if it is presenter-led for a specific decision event with options and explicit ask: `executive-data-storytelling`.
- Else if senior leadership briefing is primary: `executive-insight-driven`.
- Else default to `operational-insight-driven`.

Default rules for ambiguity:
- If unclear from requirements/current state: default to `operational-insight-driven`.
- If executive audience is indicated but subtype is unclear: default to `executive-insight-driven`.

## Before you start

- Confirm `dashboards/<name>/inputs/screenshots/` contains at least one image.
- If `requirements/` or `sample_data/` are empty, continue with explicit caveats.
- If `sample_data/` is still empty at Stage 3, stop and ask for extracts.

## Pipeline

### Stage 1 — Current-state teardown -> `outputs/01-current-state-teardown.md`

- Read every screenshot.
- Catalog purpose/audience, visuals, grain, slicers, hierarchy, and unanswered questions.
- Read requirements and identify delivery gaps.
- Score against What/So What/Now What baseline and selected type guide.
- Include a `Dashboard type fit` section (selected type, evidence, mismatches).

### Stage 2 — Redesign recommendations -> `outputs/02-redesign-recommendations.md`

- For each key metric/section, define What / So What / Now What.
- Apply selected type as the primary design contract.
- Convert findings into concrete layout and interaction changes.
- Ground every recommendation in Stage 1 evidence.

### Stage 3 — Proposed data model -> `outputs/03-data-model.md`

- Requires `sample_data/`.
- Infer grain, columns, types, keys, relationships.
- Design target dimensional model to support Stage 2.
- Include:
  - Mermaid ERD
  - Per-table specs (grain, columns, keys)
  - Explicit gaps list versus current extracts

Reference:
- [../skills/md-dashboard-redesign/reference/data-modeling-guide.md](../skills/md-dashboard-redesign/reference/data-modeling-guide.md)

### Stage 4 — Data flow spec -> `outputs/04-data-flow-spec.md`

- Define source-to-target mappings, transformations, cadence, assumptions/open questions.
- Tie cadence to selected type.

### Stage 5 — Publish -> `outputs/dashboard-redesign.html`

- Compile Stages 1-4 into a stakeholder-ready HTML artifact.
- Include: selected type, rationale, and type-specific reference used.

## Ground rules

- Recommendations must be traceable to screenshots/requirements/data.
- If required stage inputs are missing, stop and ask rather than inventing.
- Type-specific guidance is mandatory plus WSN baseline.
- Markdown outputs are source of truth; HTML is presentation.
