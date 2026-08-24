---
name: md-dashboard-redesign
description: "Independent GitHub Copilot skill for redesigning an existing dashboard (screenshots + requirements + sample source data) into a decision-driven redesign: current-state teardown, What/So-What/Now-What recommendations, proposed data model, and data flow spec, published as HTML. Supports four dashboard types and scaffolds dashboards/<name>/ directly on request. Use when the user wants to redesign, audit, or rework a dashboard, or invokes /md-dashboard-redesign."
---

# /md-dashboard-redesign

Takes an existing BI dashboard (screenshots + requirements + sample source data extracts) and reworks it around decision-driven design — What / So What / Now What — then proposes the underlying data model and data flows needed to actually support that redesign.

## Dashboard folders

Each dashboard gets its own folder under `dashboards/<name>/` with this structure:

```
dashboards/<name>/
  inputs/
    screenshots/     # PNG/JPG of the existing dashboard — one per view/page/tab
    requirements/    # briefs, stakeholder asks, KPI glossaries, notes (md/txt/docx/pdf)
    sample_data/     # CSV/XLSX extracts of the data currently behind the dashboard
  outputs/
    01-current-state-teardown.md
    02-redesign-recommendations.md
    03-data-model.md
    04-data-flow-spec.md
    dashboard-redesign.html   <- published Artifact source
```

  ### Scaffolding mechanics

  When invoked with `/md-dashboard-redesign new <name>`:

  1. Ensure `dashboards/` exists.
  2. Create `dashboards/<name>/` and its subfolders directly — do not create or depend on a `dashboards/_template/` folder. Each dashboard's folder structure is generated fresh for that dashboard only.
  3. Do not overwrite an existing `dashboards/<name>/` unless explicitly requested.
  4. Confirm these subfolders exist:
     - `dashboards/<name>/inputs/screenshots/`
     - `dashboards/<name>/inputs/requirements/`
     - `dashboards/<name>/inputs/sample_data/`
     - `dashboards/<name>/outputs/`

  A short `README.md` may be added inside each empty `inputs/` subfolder to describe what belongs there, but never create a shared `dashboards/_template/` folder as part of this process.

## Usage

```
  /md-dashboard-redesign new <name>                       # scaffold dashboards/<name>/ directly
  /md-dashboard-redesign <name>                           # run the full pipeline end-to-end
  /md-dashboard-redesign <name> --type <dashboard-type>   # force dashboard type (see supported types)
  /md-dashboard-redesign <name> --stage teardown          # run just one stage (teardown|recommendations|datamodel|dataflow|publish)
  /md-dashboard-redesign <name> --resume                  # continue from the last completed output file present
```

## Invocation hints

Use these quick hints when choosing an invocation pattern:

- Start new project structure:
  - Use `/md-dashboard-redesign new <name>` when `dashboards/<name>/` does not exist yet.
  - Example: `/md-dashboard-redesign new Sales_QBR`.
- Run everything in one pass:
  - Use `/md-dashboard-redesign <name>` when all required inputs are in place and you want outputs 01-05 generated in order.
  - Example: `/md-dashboard-redesign PnL_Dashboard`.
- Lock dashboard type up front:
  - Use `/md-dashboard-redesign <name> --type <dashboard-type>` when the intended audience/workflow is already known and you want to avoid reclassification.
  - Example: `/md-dashboard-redesign PnL_Dashboard --type operational-insight-driven`.
- Run a single stage:
  - Use `/md-dashboard-redesign <name> --stage <stage>` for iterative work or spot fixes.
  - Stage hints:
    - `teardown`: re-evaluate screenshots/requirements and type fit.
    - `recommendations`: regenerate What/So What/Now What redesign guidance.
    - `datamodel`: regenerate ERD + table specs + gaps (requires sample_data).
    - `dataflow`: regenerate source-to-target transformation spec.
    - `publish`: rebuild stakeholder HTML from the markdown outputs.
  - Example: `/md-dashboard-redesign PnL_Dashboard --stage recommendations`.
- Continue interrupted runs:
  - Use `/md-dashboard-redesign <name> --resume` when a prior run was interrupted and outputs already exist.
  - Resume starts from the next missing output file in sequence.
  - Example: `/md-dashboard-redesign PnL_Dashboard --resume`.

Recommended invocation order for first-time projects:

1. `/md-dashboard-redesign new <name>`
2. add screenshots/requirements/sample_data into `inputs/`
3. `/md-dashboard-redesign <name> --type <dashboard-type>` (optional but preferred if type is known)
4. `/md-dashboard-redesign <name>`

If unsure which command to use, start with `/md-dashboard-redesign <name>` and let the classifier pick a default type using the rules in "Type selection logic".

## Supported dashboard types

Classify the dashboard into one of these four types before Stage 1. If the user does not specify a type, infer from screenshots + requirements and state the chosen type and rationale in `01-current-state-teardown.md`.

1. `executive-insight-driven`
  - Reference: [reference/executive-insight-driven-design.md](reference/executive-insight-driven-design.md)
  - Use when the dashboard is a curated leadership briefing focused on material change, drivers, and implications, without formal approval workflow.
2. `executive-decision-driven`
  - Reference: [reference/executive-decision-driven-design.md](reference/executive-decision-driven-design.md)
  - Use when the dashboard supports governed executive decisions with explicit trigger/owner/authority/sign-off.
3. `executive-data-storytelling`
  - Reference: [reference/executive-data-storytelling-design.md](reference/executive-data-storytelling-design.md)
  - Use when the dashboard is presenter-led for a specific decision event with options, recommendation, and explicit ask.
4. `operational-insight-driven`
  - Reference: [reference/operational-insight-driven-design.md](reference/operational-insight-driven-design.md)
  - Use when the dashboard is a repeat-use operating instrument for scan/judge/explain/prioritize/drill workflows.

Always use [reference/executive-decision-driven-design.md](reference/executive-decision-driven-design.md) as the baseline design reference.

## Type selection logic

Use this quick classifier before the pipeline:

- If evidence of formal trigger, owner, authority, sign-off states, and governed action controls exists: `executive-decision-driven`.
- Else if this is clearly built as a one-off or event-specific recommendation narrative with options and an explicit ask: `executive-data-storytelling`.
- Else if primary audience is senior leadership and the goal is concise implication-led briefing: `executive-insight-driven`.
- Else default to `operational-insight-driven`.

Defaulting rules when requirements/current state are unclear:

- If nothing clearly indicates executive workflow or audience, default to `operational-insight-driven`.
- If executive audience is indicated but executive subtype is unclear, default to `executive-insight-driven`.
- Only ask for user confirmation when the chosen default would materially change Stage 2 recommendations (for example, ambiguity between `executive-decision-driven` and `executive-data-storytelling`).

## Before you start

Confirm `dashboards/<name>/inputs/screenshots/` has at least one image — the pipeline can't run without it. If `requirements/` or `sample_data/` are empty, proceed but say so explicitly in the teardown output: Stage 1–2 work from screenshots alone, but Stage 3 (data model) needs `sample_data/` — if it's still empty when you reach Stage 3, stop and ask the user for extracts rather than inventing a schema.

## Helper scripts

Two stdlib-only Python scripts live under the repository-root `scripts/` directory and should be preferred over writing one-off profiling/validation code. Run these commands from the repository root:

- `python scripts/profile_sample_data.py <sample_data_dir>` — profiles every CSV in `inputs/sample_data/`: row/column counts, null counts, duplicate full rows, duplicate candidate keys (`*_id`/`*_key` columns), date ranges, and a best-effort cross-file foreign-key check. Use it at the start of Stage 3 instead of hand-writing profiling code. It intentionally avoids pandas/numpy so it isn't affected by local binary/ABI conflicts between those packages — fall back to it if a pandas-based attempt fails.
- `python scripts/validate_dashboard_html.py <html_path> --require "<substring>" ...` — parses the published Stage 5 HTML and fails (non-zero exit) if a required substring is missing, a local `<img>` doesn't resolve on disk, or an in-page `<a href="#...">` anchor has no matching id. Run it after publishing instead of writing a fresh validation script each time.

The former copies under `.github/skills/md-dashboard-redesign/scripts/` remain compatibility launchers for existing links; the root scripts are canonical.

## Pipeline

### Stage 1 — Current-state teardown → `outputs/01-current-state-teardown.md`

Read every file in `screenshots/` (the Read tool handles images natively). For each dashboard view/tab, catalog:
- Apparent purpose and audience
- Every visual element: chart type, metric(s) shown, grain, filters/slicers present
- Layout and visual hierarchy — what draws the eye first, the actual reading order
- What questions it answers today (the "what") vs. what it leaves the viewer to figure out themselves

Read everything in `requirements/` and note any gap between what's being asked for and what the current dashboard actually delivers.

Score the current state against:
- [reference/executive-decision-driven-design.md](reference/executive-decision-driven-design.md) as baseline; and
- the type-specific guide selected in "Supported dashboard types".

In `01-current-state-teardown.md`, include a short "Dashboard type fit" section that states:
- selected type,
- evidence for that choice from screenshots/requirements,
- mismatches against the selected type's acceptance checklist.

Cite specific views/elements — not generic BI complaints.

### Stage 2 — Redesign recommendations → `outputs/02-redesign-recommendations.md`

For every key metric or section from Stage 1, work out its What / So What / Now What per [reference/executive-decision-driven-design.md](reference/executive-decision-driven-design.md):
- **What** — the headline fact, stated as a comparison, not a bare number
- **So What** — the context that makes it judgeable: target, prior period, benchmark, trend — and why the audience should care
- **Now What** — the decision or action it should trigger, and what the dashboard needs to surface to support taking it (drill-down, exception flag, suggested next view)

Then apply the selected type's reference as the primary design contract:
- `executive-insight-driven`: use [reference/executive-insight-driven-design.md](reference/executive-insight-driven-design.md)
- `executive-decision-driven`: use [reference/executive-decision-driven-design.md](reference/executive-decision-driven-design.md)
- `executive-data-storytelling`: use [reference/executive-data-storytelling-design.md](reference/executive-data-storytelling-design.md)
- `operational-insight-driven`: use [reference/operational-insight-driven-design.md](reference/operational-insight-driven-design.md)

Translate that into concrete design changes grounded in Stage 1 evidence:
- inverted-pyramid ordering (or presenter-led sequence for storytelling type),
- annotations/callouts on notable points,
- exception highlighting or decision queue treatment as appropriate,
- removal of chart types that do not support the selected type's completion test,
- filters/drill-paths/action controls matched to the selected type.

Do not give generic dashboard-design advice.

### Stage 3 — Proposed data model → `outputs/03-data-model.md`

Requires `sample_data/`. Run `python scripts/profile_sample_data.py inputs/sample_data/` first to establish row/column counts, nulls, duplicate keys, date ranges, and cross-file FK integrity — use its output as the grounding evidence rather than re-deriving it by hand. For each extract, infer grain, columns, types, and relationships to the other extracts. Then design the dimensional model needed to support Stage 2's redesign — not just what the current data already happens to support. That means the fact table(s) at the grain the new comparisons/drill-downs need, dimension tables, and any derived fields the So-What/Now-What layer requires (targets, prior-period deltas, cohorts, running totals) that don't exist in the source yet. Use [reference/data-modeling-guide.md](reference/data-modeling-guide.md) for the modeling patterns, plus ensure the model supports the selected type's semantic needs (for example: decision/authority/sign-off entities for executive-decision-driven, or stable drill-path entities and exception aging for operational-insight-driven). Output:
- A full Mermaid ERD showing every proposed table and relationship — the traceability view for gap analysis and lineage
- A Kimball star/galaxy schema view of the same model: one Mermaid `erDiagram` per fact table (star) plus one constellation diagram listing conformed dimensions across facts (galaxy) — the handoff view for whoever builds the warehouse/semantic layer. See "Presenting the model" in [reference/data-modeling-guide.md](reference/data-modeling-guide.md)
- A per-table spec: grain, columns (name / type / nullable / description), keys
- An explicit "gaps" list — fields the redesign needs that aren't in any current extract, which the data engineering team will need to source elsewhere

### Stage 4 — Data flow spec → `outputs/04-data-flow-spec.md`

Bridge current sources to the Stage 3 target model. For each target table: which source extract/system it comes from, the transformations required (joins, grain changes, aggregations, calculated fields), the refresh cadence implied by the selected dashboard type (for example, intraday/daily for operational-insight-driven vs. governance-cycle snapshots for executive types), and open questions/assumptions a data engineer would need to confirm. This is a spec for engineering to implement against, not implementation itself — no need to write actual SQL/dbt unless the user asks for that as a follow-up.

### Stage 5 — Publish → `outputs/dashboard-redesign.html`

Load the `artifact-design` skill, then compile Stages 1–4 into one polished, stakeholder-ready HTML page: an executive summary up top, then teardown → recommendations → data model (render the ERD as a mermaid diagram) → data flow, each section easy to jump to.

In the summary, explicitly include:
- selected dashboard type,
- why this type was chosen,
- the type-specific reference used.

Publish via the Artifact tool and send the user the link. Then run `python scripts/validate_dashboard_html.py` against the published file with `--require` set to the section titles and selected-type strings from the summary, instead of writing a fresh ad hoc validation script.

**QA scope for this stage:** the HTML is a stakeholder brief, not a production dashboard build. Browser QA only needs to confirm, at one representative desktop viewport (roughly 1280–1440px wide): local assets (images, Mermaid diagrams) load, in-page anchors resolve, and there's no horizontal overflow. Do not additionally test mobile/tablet viewports or responsive breakpoints unless the user explicitly asks for a responsive or production-grade artifact — that scope belongs to a dedicated dashboard-build task, not a redesign brief.

## Ground rules

- Every recommendation must trace back to something specific in the screenshots, requirements, or data — no generic BI-consultant filler.
- If a stage's required input is missing, stop and ask rather than inventing content (screenshots for Stage 1, sample_data for Stage 3).
- Type-specific guidance is mandatory: always use one of the four supported types and its respective reference document, plus [reference/executive-decision-driven-design.md](reference/executive-decision-driven-design.md).
- Keep the four markdown outputs as the source of truth; the HTML artifact in Stage 5 is a presentation layer over them, not a separate deliverable to maintain in parallel.
- In markdown outputs, use real `###`/`####` headings for subsections instead of bold text, never reuse identical heading text within a file, increment heading levels by only one at a time, and restart ordered-list numbering at `1.` whenever a new list begins.
