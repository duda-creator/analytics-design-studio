# Data modeling patterns for decision-driven dashboards

Guidance for Stage 3 of the pipeline: turning sample source extracts + the Stage 2 redesign into a proposed dimensional model.

## Start from the decision, not the source data

The default failure mode is modeling only what's already in the sample extracts. Instead, work backward from Stage 2's Now-What requirements: what grain, comparisons, and drill-paths does the redesign need? Then check which of those the source data already supports and which are gaps. The gaps list in `03-data-model.md` is often the most useful part of the deliverable — it's what data engineering actually has to go build.

## Grain first

Grain = what one row of a fact table represents. Get this explicit before anything else ("one row per order line per day" vs. "one row per order"). Every measure in the table must be true at that grain. A common source of dashboard bugs is mixing grains in one query (e.g. joining a daily fact to a monthly target without first aligning periods) — call this out explicitly in the data flow spec if the redesign needs period comparisons.

## Fact vs. dimension

- **Fact table**: the measurements — numeric, additive where possible (revenue, units, count). Rows are events or period-snapshots at the chosen grain. Foreign keys point to dimensions.
- **Dimension table**: the descriptive context used to slice/filter/group facts (customer, product, region, date, campaign). Wide, denormalized, changes slowly relative to facts.
- **Conformed dimensions**: if the redesign spans multiple fact tables (e.g. sales facts + marketing spend facts), shared dimensions (date, region, product) should be the same table/keys across both, so cross-fact comparisons in Stage 2's So-What layer are actually joinable.

## Measure types (matters for how they can be aggregated/compared)

- **Additive**: safe to sum across any dimension (revenue, units sold).
- **Semi-additive**: safe to sum across some dimensions but not time (account balance — sum across accounts, but not across days).
- **Non-additive**: never sum directly (ratios, percentages, margins — store the numerator/denominator and compute the ratio at query time, or make clear in the spec that the ratio must be recomputed after aggregation, not averaged).

Flag any metric in Stage 2 that's a ratio/rate — these are the most common source of dashboards that silently show wrong numbers after a groupby.

## Presenting the model: full ERD vs. star/galaxy view

Stage 3 needs the same dimensional model presented two ways, not two different models:

- **Full ERD** — every proposed table and relationship in one Mermaid `erDiagram`. This is the traceability view: it lets a reviewer (or an agent) walk from a gap back to the exact table/column it affects, and back to the screenshot/requirement/extract that justified it.
- **Star/galaxy view** — the same tables, redrawn per Kimball convention: one small `erDiagram` per fact table showing only that fact and its directly connected dimensions (a star), plus one additional constellation diagram listing which dimensions are shared across which facts (the galaxy). This is the handoff view for whoever builds the warehouse/semantic layer — it should look like the star schemas they already build DDL and BI models from, not like a general relationship graph.

Rules for building the star/galaxy view:

- One star diagram per fact table. Do not combine multiple facts into a single star diagram — that's what the constellation diagram is for.
- List conformed dimensions once in the constellation diagram (dimension → which fact tables reference it), instead of repeating full column lists per fact.
- **Resolve every snowflaked table before publishing the star view.** If a dimension only exists to hold a hierarchy or attribute of another dimension (e.g. a category table that only ever joins through the entity it classifies), either:
  - flatten it: pull its columns onto the parent dimension directly, and drop the separate table from the star view; or
  - keep it separate and justify why in one sentence (e.g. it's independently versioned, or referenced directly by more than one fact table at a grain the parent dimension doesn't have) — do not leave an unexplained snowflake in a schema meant to read as a star/galaxy.
- Degenerate dimensions (natural keys carried directly on the fact with no dimension table, e.g. an invoice number) stay on the fact in both views — don't invent a dimension table for them.
- If the target project also uses `md-table-spec-builder`/`md-ddl-generator`, tag each dimension/fact column with the same `Business Role` vocabulary those skills use (`Measure`, `Dimension`, `Dimension Attribute`, `Degenerate Dimension`) so the star/galaxy view can be handed off with minimal re-translation.

## Supporting the So-What/Now-What layer specifically

Ordinary source extracts capture "what happened." The comparison layer decision-driven design needs usually has to be modeled explicitly:

- **Prior-period comparison**: either a self-join in the transform (window function over the fact grain) or a precomputed `prior_period_value` / `delta_vs_prior` column on the fact — prefer precomputing if the comparison is a fixed, always-shown one; compute at query time if the user picks the comparison period interactively.
- **Target/budget/forecast**: usually a separate, lower-grain table (e.g. monthly target per region vs. daily actuals) — do not force targets into the same grain as actuals; instead define how the two grains reconcile (e.g. daily actuals roll up to monthly before comparing to monthly target).
- **Segment/peer benchmark**: a derived aggregate (e.g. category average) computed from the same fact table — model as a view/derived table, not a duplicated source.
- **Exception/threshold flags**: a boolean or status column derived from comparing actual to target/benchmark — precompute if the threshold logic is fixed business logic (SLA breach, budget overrun), so the dashboard layer doesn't reimplement business rules.
- **Slowly changing attributes**: if a dimension attribute changes over time and historical reporting needs to reflect the value *as of* the fact's date (e.g. a customer's tier at time of purchase, not today), flag it as needing SCD Type 2 (versioned rows with effective dates) rather than a simple overwrite.

## Output format for `03-data-model.md`

1. Full Mermaid `erDiagram` showing all proposed tables and their relationships
2. Kimball star/galaxy view: one Mermaid `erDiagram` per fact table (star) plus one constellation diagram of conformed dimensions across facts (galaxy) — see "Presenting the model" above
3. One subsection per table: grain (one sentence), column list (name, type, nullable, description, and for facts — additive/semi-additive/non-additive), primary/foreign keys
4. "Gaps vs. current sources" — table/column-level list of what's needed but not present in `inputs/sample_data/`, so it's clear what data engineering must source or build before the redesigned dashboard can go live
