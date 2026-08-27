---
name: md-dashboard-diagnostic
description: Diagnose an existing dashboard (from an uploaded screenshot, image, or description) against a Dashboard Type × Decision Depth framework — classifying it as Analytical (Microscope), Operational (Cockpit), or Executive (Radar), and placing it on the Decision Depth Ladder (Snapshot, Insight-Driven, Decision-Driven, Data Storytelling), then reporting strengths, gaps against a requested or default target, and pitfalls, with a visual scorecard. Closes with a proposed action (retain / revamp / split), and can compare multiple already-diagnosed dashboards to propose merges or retirements. Built for financial-services dashboards (risk, trade finance, liquidity, capital, board/committee reporting) with worked examples drawn from CIB & Treasury, and the rubric applies to any BI screenshot. Use whenever the user uploads or references a dashboard screenshot and asks to audit, diagnose, evaluate, review, or "sanity check" it — including phrasing like "is this Insight-Driven yet", "is this a Cockpit or a Radar", "what depth is this dashboard at", "check this against the framework/ladder", "should we split/merge these dashboards", or when a user shares a dashboard screenshot (Tableau, Power BI, Looker, an internal risk/treasury system, etc.) with a question about its depth, audience-fit, or maturity. Trigger even without the framework named explicitly, as long as the ask is "grade/assess/where does this sit" for a dashboard.
---

# Dashboard Diagnostic

This skill audits a *real, already-built* dashboard against a Dashboard Type × Decision Depth framework: which of the three Dashboard Types it actually behaves like, and — for Operational and Executive — which rung of the Decision Depth Ladder it currently occupies versus the rung it should occupy. It closes with a visual scorecard so the gap is legible at a glance, not just described in prose.

Read `references/Analytics_Design_Framework.md` in full before classifying anything. It contains the complete rubric — the type comparison table, the depth ladder, the type × depth ceiling rules, the pitfalls, and a feature library of concrete, non-overlapping signals for every type and every rung — and several of its rules are load-bearing exceptions (e.g. an Operational dashboard can only reach Decision-Driven with delegated authority; an unrequested Executive dashboard sitting at Snapshot is a finding, not a delivery). Skimming a summary instead of the source risks misapplying these.

Also read `references/visual-design-pitfalls.md` before Step 6. It covers a separate axis from `Analytics_Design_Framework.md` — visual and perceptual **craft** (precision, chart-type choice, color, clutter, layout) rather than strategic fit (audience/depth) — and Step 6 checks both.

## Scaffolding a new dashboard

When invoked with `/md-dashboard-diagnostic new <name>`, create the dashboard folder structure
directly under `dashboards/<name>/`:

```text
dashboards/<name>/
	inputs/
		screenshots/
		requirements/
		sample_data/
	outputs/
```

Do not create or depend on a shared `dashboards/_template/` folder. Do not overwrite an existing
`dashboards/<name>/` folder unless explicitly requested. After scaffolding, the user can add the
dashboard screenshots, requirements, and optional sample data, then invoke
`/md-dashboard-diagnostic <name>` to run the diagnosis. The skill produces
`outputs/<name>_diagnostic.md` and `outputs/<name>_scorecard.html`.

## Usage

```text
/md-dashboard-diagnostic new <name>                    # scaffold a new dashboard folder
/md-dashboard-diagnostic <name>                        # diagnose the dashboard
/md-dashboard-diagnostic compare <name1> <name2> ...   # compare 2+ already-diagnosed dashboards
```

For `new <name>`, confirm that these subfolders exist before returning:

- `dashboards/<name>/inputs/screenshots/`
- `dashboards/<name>/inputs/requirements/`
- `dashboards/<name>/inputs/sample_data/`
- `dashboards/<name>/outputs/`

## Why this is a diagnosis, not a rebuild

The framework describes what a *finished, well-built* dashboard of each type and depth looks like. This skill runs in reverse: it looks at something that already exists and infers, from the evidence on screen, where it actually landed — which is often not where it was supposed to land. Keep that distinction alive in the language you use: you are reporting what the dashboard *is*, not proposing what to build from scratch.

## Step 1 — Establish the target

Before classifying anything, pin down what the dashboard is being measured against:

- If the user names a target ("is this a good Radar", "does this clear Insight-Driven", "we wanted this as a Cockpit") — use that.
- If they don't name one, use the framework's own default: **Operational, Insight-Driven**. Say explicitly that you're using the default, so the user can correct you if the dashboard was actually commissioned as something else.
- If the user says what audience or purpose the dashboard was *built* for (e.g. "this goes to the leadership team" or "the ops team uses this every morning"), treat that as strong evidence for the target type even before looking at the image — a dashboard built for leadership is implicitly Executive regardless of how it currently looks, and that gap (built-for vs. looks-like) is often the finding itself.

## Step 2 — Read the evidence

Look directly at the screenshot(s) (you have vision — use it, don't ask the user to transcribe it). Pull out what's actually visible before you classify anything:

- **Granularity**: individual trade/transaction rows, vs. rolled-up metrics with drill paths, vs. headline numbers only.
- **Comparison points**: is any number shown against last period, budget, forecast, or a peer — or is it standalone?
- **Insight/narrative**: is there a plain-English "why" sentence anywhere, or is it numbers and colors only?
- **Decision machinery**: named owner, trigger threshold, pre-agreed action, sign-off — anything that reads as a live workflow rather than a report?
- **Interactivity cues**: visible filters, drill-down affordances, "explore" or slice/dice controls (even if you can't click them, the UI chrome tells you they exist) vs. a static, curated layout.
- **Cadence markers**: "as of [date]", "updated daily/weekly/monthly", live-refresh indicators.
- **Visual density and polish**: a dense grid of small multiples reads differently from three or four large, curated numbers — density is itself evidence of intended audience.
- **Craft signals**: chart types used, axis treatment (truncated/non-zero baselines), color usage, decimal precision, clutter/chart-junk, layout crowding — this is the evidence Step 6's visual craft pitfall check draws on, per `references/visual-design-pitfalls.md`.

Quote or describe the specific tile, label, or number that supports each classification call in your report — "the top-left card shows LCR at 128% with no comparison" is checkable evidence; "this looks operational" is not.

## Step 3 — Classify the Type

Using the comparison table in `references/Analytics_Design_Framework.md`, decide which of the three the dashboard *behaves like right now*, independent of what it was supposed to be:

- **🔬 Analytical (the Microscope)** — record-level detail, free-form slicing, built for someone actively investigating a question.
- **🎛️ Operational (the Cockpit)** — rolled-up metrics, filters on the well-worn questions, a fixed reporting cadence.
- **📡 Executive (the Radar)** — headline numbers only, curated and clean, nothing to poke at.

Cross-check against the Feature Library in `references/Analytics_Design_Framework.md` — each type's signature-features list is written so items don't overlap across types, so a feature you spot on screen should point at one type, not several.

Two things to actively check for, because they're named pitfalls, not just style differences:

- **Everything-to-Everyone Trap**: does the same screen mix record-level detail with headline-only framing? That's not "a bit of both" — call it out plainly rather than splitting the difference.
- **Executive Dress-Up**: is this a dense operational report with the font shrunk and an "Executive Summary" label slapped on it, rather than something curated from the ground up? Look for the tell: operational-density content (many small tiles, drill controls) wearing Executive labeling.

If the type is ambiguous or mixed, don't force a single label — report it as a mix and name which pitfall it matches, since that mix *is* the finding.

## Step 4 — Classify the Depth

**If the dashboard is Analytical**, skip the ladder entirely — investigation isn't leveled. Instead, audit the metrics for the flag test the framework uses: does each number carry a comparison and a "so what," or is it raw? Report this per metric or per section, not as a single score.

**If it's Operational or Executive**, place it on the ladder using the test in `references/Analytics_Design_Framework.md` — "Snapshot tells you if a number is good or bad. Insight-Driven tells you why, compared to what, and what that means":

- **Snapshot** *(Pulse Check)*: a target/status line with no comparison and no explanation — colors alone.
- **Insight-Driven** *(Diagnosis)*: a comparison point (vs. last period, budget, forecast, peer) plus a plain-English sentence saying what it means.
- **Decision-Driven** *(Prescription)*: everything in Insight-Driven, *plus* a named decision, named owner, a stated trigger point, a pre-agreed action, and sign-off — a workflow, not a report. Look for this explicitly; don't infer it from Insight-Driven content that merely looks important.
- **Data Storytelling** *(Pitch)*: a built, defended narrative aimed at winning a specific live decision — this is very rarely what a static screenshot shows, since it's presented, not screenshotted. Only call it Data Storytelling if there's clear evidence of an argument being built to move a room (e.g. slide-like framing, a call to action), not just because the stakes look high.

Apply the ceiling rules from the Type × Depth Matrix in `references/Analytics_Design_Framework.md` as you go: an Operational dashboard that reaches Decision-Driven needs evidence of *delegated authority*, not just a trigger threshold on the screen — if you can't tell whether the person using it holds that authority, say so as an open question rather than asserting Decision-Driven. An Executive dashboard sitting at Snapshot isn't a valid steady-state design — it's a diagnostic finding calling for revamp to Insight-Driven, and your report should say that explicitly rather than reporting Snapshot as merely "on target."

## Step 5 — Ask only what you can't infer

You now have a provisional Type and Depth from the visual evidence alone. Before finalizing, check whether anything material is still genuinely unknown — typically: who actually uses this day to day, whether that person holds sign-off authority (this decides whether an apparent Decision-Driven Cockpit is legitimate or an Authority Gap), or the real refresh cadence if nothing on screen shows it.

Only ask about items that would actually change the verdict — if the visual evidence already settles Type and Depth confidently, don't ask just to be thorough. Ask as a short, specific set of questions (not a generic "tell me more about this dashboard"), and say why each one matters — e.g. "Does whoever looks at this daily have authority to actually pause the campaign, or does that decision sit elsewhere? That's the difference between a legitimate Decision-Driven rung and an Authority Gap." If the user can't answer, proceed with the visual classification and flag the authority question as unresolved in the report rather than blocking on it.

## Step 6 — Compare to target, write the report

Now assemble the findings using this structure (adapt section content to what you actually found — e.g. an Analytical report replaces the ladder section with the per-metric flag audit):

```markdown
# Dashboard Diagnostic — [dashboard name / one-line description]

## Snapshot
- **Detected:** [Type] — [Depth, or "flag-based (Analytical)"]
- **Target:** [Type] — [Depth] ([stated by user] / [framework default])
- **Verdict:** [On target / Under-built / Over-built / Type mismatch / Mixed — pitfall]

## What the screenshot shows
[3-6 bullets of concrete visual evidence, each tied to a specific tile/label/number]

## Strengths
[What's already working, stated against the framework's own definition of "done" for this type/depth — not generic praise]

## Gaps vs. [target]
[Specific, named gaps — e.g. "no comparison point on any tile: currently Snapshot, target is Insight-Driven" — each gap should point to what closing it would require (the Feature Library's revamp moves are good source material), not just that it's missing]

## Strategic fit pitfall check
[Name any of the framework's five apply, with the specific evidence; state "none observed" if genuinely clean]

## Visual craft pitfall check
[Score against the 13 pitfalls in `references/visual-design-pitfalls.md`; name only the ones with concrete on-screen evidence (e.g. "truncated y-axis on the trend chart"), and state "none observed" for a clean pass. Don't double-count a Pitfall 2 (inadequate context) hit that's already captured above as a Depth gap.]

## Open questions
[Only if Step 5 left something unresolved — otherwise omit this section]

## Recommendation
[Follow the framework's own diagnostic-default rules: a Snapshot Operational/Executive dashboard → recommend revamp to Insight-Driven, not just "add more detail." An Insight-Driven dashboard with a real nameable decision behind it → make the case for Decision-Driven as a standing recommendation, not an instruction. Never recommend Data Storytelling proactively — it's opt-in only. If it's already on target, say so plainly instead of manufacturing a gap.]

## Proposed Action
[One of the following, chosen from evidence already gathered in Steps 2-4 — never introduce new evidence here:]
- **Retain** — one clear audience/purpose at an appropriate type/depth; only the gaps above apply, no structural change.
- **Revamp** — one audience/purpose, but under- or over-built for target; closing the gaps above is enough, no split needed.
- **Split into: [Name A — purpose], [Name B — purpose], ...** — use only when Step 3/4 evidence supports it: the Everything-to-Everyone Trap, different tabs/screenshots landing at different types or depths, or mixed audiences/grains/cadences/authority levels on the same screen. Name each proposed dashboard and its purpose in one line; do not design them here.
- **Flag for portfolio comparison** — if this dashboard's purpose/KPIs look like they overlap with another dashboard the user has mentioned or that also exists in `dashboards/`, say so here and recommend running `/md-dashboard-diagnostic compare <this-name> <other-name>` rather than guessing at overlap from one dashboard's evidence alone.
```

Keep the prose specific and evidence-grounded throughout — every claim about Type or Depth should trace back to something named in Step 2, not general impressions.

## Step 7 — Build the visual scorecard

Produce a single self-contained HTML file as a companion to the written report. Use `assets/scorecard_example.html` as the design reference — read it before building, since it establishes the visual language (the type-matrix strip, the depth gauge with current/target markers and the gap between them, the strength/gap chips) that every diagnostic should share for consistency across runs. Adapt its content, list lengths, and the Analytical-specific layout (flag audit instead of a gauge) to this diagnosis; don't reuse its placeholder copy.

If you're extending or restyling it, consult the `frontend-design` skill for the underlying design principles — but the instrument-panel/schematic visual direction already established in the example should carry through rather than being reinvented each time, so the scorecard reads as one consistent product across dashboards.

Save the files to `dashboards/<name>/outputs/` using the dashboard-specific names `<name>_diagnostic.md` and `<name>_scorecard.html`, then present both files to the user together. The scorecard is the at-a-glance version; the report is where the reasoning and evidence live.

## Comparing multiple dashboards (`compare`)

Use this mode only when the user has 2+ dashboards that already exist as separate `dashboards/<name>/` folders and wants to know whether any should be merged, retired, or retained as-is — this is the cross-dashboard counterpart to the single-dashboard `Split` call in Step 6, and it never mixes their `inputs/` folders together (each dashboard keeps its own screenshots/requirements/sample_data — merging those folders would corrupt Stage 3 data profiling if the sources are unrelated).

`/md-dashboard-diagnostic compare <name1> <name2> [<name3> ...]`

1. For each `<nameN>`, read `dashboards/<nameN>/outputs/<nameN>_diagnostic.md`. If it doesn't exist yet, run Steps 1-7 for that dashboard first to produce it — don't guess at a dashboard's type/depth/purpose from memory.
2. Compare the dashboards using only what's in their diagnostic reports (purpose, audience, type, depth, KPIs/decisions referenced, Proposed Action): look for shared audience, duplicate or near-duplicate KPIs, overlapping decisions, and redundant grain. Cite the specific diagnostic report each overlap claim comes from — "same audience" or "looks similar" is not evidence.
3. Write `dashboards/_comparisons/<name1>-<name2>[-<name3>...]_portfolio-synthesis.md`:

```markdown
# Portfolio Comparison — [name1] vs [name2] ...

## Dashboards compared
| Dashboard | Type | Depth | Audience | Purpose (one line) |
| --- | --- | --- | --- | --- |
| [name1] | ... | ... | ... | ... |

## Overlap evidence
[Specific KPI/decision/audience overlaps, each citing the source diagnostic report; state "no material overlap found" if genuinely distinct]

## Proposed Action
- **Retain:** [names] — distinct audience/purpose, no overlap found
- **Merge:** [Name A + Name B] → [proposed merged name] — [why, tied to the overlap evidence above]
- **Retire:** [name] — [why: fully superseded by another compared dashboard]

## Open questions
[Anything needed before detailed design can proceed on the retained/merged set — otherwise omit this section]
```

This synthesis file is markdown only — it does not need a companion scorecard. Each compared dashboard's own `<name>_diagnostic.md`/`<name>_scorecard.html` stay unchanged.

## Handling edge cases

- **No image, just a description**: work from the user's description as evidence instead, but be more conservative about confidence — say plainly which calls would firm up with an actual screenshot. Ask clarifying questions if the description is vague or incomplete, and note any assumptions you make in the report.
- **Multiple screenshots of one dashboard** (different tabs/states): treat them as one diagnosis, pooling evidence across all of them; note if different tabs land at different depths (common, and worth flagging — e.g. "the summary tab is Snapshot but the drill-down tab adds Insight-Driven context") — this is also the primary evidence for a Step 6 `Split` call.
- **Multiple genuinely different dashboards** in one request: diagnose each separately with its own report/scorecard pair rather than merging them — one dashboard, one type, one primary audience applies to the diagnosis too. If the user actually wants to know whether they overlap or should merge, use `compare` after each has its own diagnostic report.
- **The dashboard is fine**: it's a legitimate outcome for the verdict to be "on target, no material gaps" — don't manufacture findings to fill out every section.
