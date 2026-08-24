# Executive + Insight-Driven dashboard design

An Executive + Insight-Driven dashboard is a curated briefing surface for senior leaders. It answers what changed, compared with what, why it matters, and where leadership attention is needed. It does not ask the viewer to discover the story through filters, nor does it claim that a formal decision workflow exists when the purpose is situational understanding.

## Design contract

| Dimension | Requirement |
| --- | --- |
| Primary audience | Senior leaders, executive committees, and boards |
| Core question | "What changed, why does it matter, and what deserves our attention?" |
| Cadence | Aligned to a leadership meeting or governance cycle |
| Detail level | A small number of enterprise-level outcomes and drivers |
| Interaction | Look-first; at most a period or scenario toggle and curated detail links |
| Decision depth | Comparison plus an explicit executive implication |
| Completion test | The audience can state the material change and its consequence without interpreting the charts themselves |

The dashboard is not a compressed operational report. Every metric must earn its place by changing leadership's understanding of performance, risk, resilience, or strategic trajectory.

## Executive insight anatomy: Outcome / Context / Driver / Implication

Every headline should provide four layers:

**Outcome** — the current enterprise result or exposure, expressed in a unit leadership recognizes.

**Context** — the most decision-relevant comparison: plan, forecast, prior governance cycle, risk appetite, regulatory floor, or external benchmark.

**Driver** — the one or two factors that materially explain the variance. Quantify contribution and concentration where possible.

**Implication** — a concise statement of what the movement means for the organization, outlook, risk posture, or agenda. This points attention toward a topic; it does not invent an approval request.

Example:

> **Liquidity headroom: $4.6B, $0.8B below plan**  
> Corporate deposit outflows account for 70% of the gap; the current trajectory reduces the downside buffer entering quarter-end.

## Curation rules

Include a metric only when it satisfies at least one test:

- it measures a stated strategic outcome;
- it shows proximity to a risk appetite, regulatory, capital, or liquidity boundary;
- it materially changes the approved outlook;
- it exposes a concentration that could alter an executive priority;
- it is required to frame an item already on the meeting agenda.

Demote metrics that are stable, duplicative, controllable entirely below executive level, or present only because the data exists. A useful rule is that every item should have a named executive question; "might be interesting" is not enough.

## Information hierarchy

### 1. Briefing header

State the reporting date, governance cycle, scope, units, scenario, data status, and the central takeaway in one compact band. The takeaway should be a conclusion, not a label such as "Executive Summary."

### 2. Material change

Give the largest or most consequential change the strongest first-read position. Pair the outcome with its comparison and implication. Avoid a row of equally weighted KPI cards that forces leaders to determine priority themselves.

### 3. Enterprise outcomes

Show a limited set of headline measures grouped by strategic objective or risk domain. Use restrained status treatment; highlight only genuine exceptions or meaningful changes since the last cycle.

### 4. Drivers and outlook

Use one or two compact views to explain the headline: a variance bridge, short annotated trend, ranked contribution view, or scenario range. The view should answer a known executive question, not invite open-ended exploration.

### 5. Attention agenda

Close with the issues to monitor, challenge, or place on a future decision agenda. Phrase each item as an implication with a time horizon, evidence state, and accountable executive area. Do not add formal triggers or sign-off unless the dashboard is intentionally Decision-Driven.

## Layout rules

- Fit the core briefing in one screen or one meeting page at the intended display size.
- Use an inverted pyramid: conclusion first, evidence second, supporting detail last.
- Favor a few strong alignments and generous whitespace over a dense card grid.
- Keep titles declarative: "Deposit outflows reduced headroom by $0.8B" is stronger than "Liquidity trend."
- Use large type for the primary conclusion, not for every value.
- Label charts directly and remove legends, axes, and decoration that do not aid judgment.
- Annotate the inflection, breach, or driver rather than expecting leaders to find it.
- Keep color semantic and sparse. Pair it with labels or symbols.
- Preserve comparable scales and periods for views intended to be compared.
- Avoid scrolling, dense tables, filter panels, and operational exception queues.

## Selecting comparisons

Executive comparisons should reflect commitments and exposure, not merely convenient time shifts:

| Executive question | Preferred context |
| --- | --- |
| Are we delivering the approved plan? | Budget, plan, or latest approved forecast |
| Has the outlook changed? | Previous forecast and scenario range |
| Are we within appetite? | Limit, appetite, regulatory floor, and headroom |
| Is the issue strategically material? | Enterprise contribution and concentration |
| Are we moving structurally? | Multi-period trajectory or external benchmark |

Use one primary comparison beside the headline. Secondary comparisons belong in supporting evidence only when they change the interpretation.

## Writing executive insights

Use a conclusion-led sentence:

> **[Outcome] is [variance] versus [commitment], driven by [material cause], which means [enterprise implication over a stated horizon].**

Good insight copy is:

- material: it connects to enterprise outcomes or risk;
- quantified: it states size, contribution, or headroom;
- time-bound: it identifies when the implication becomes relevant;
- evidence-aware: it distinguishes actuals, forecast, scenario, and judgment;
- brief: one conclusion, with supporting detail available elsewhere.

Avoid vague commentary such as "continued focus is required," unsupported causal language, and recommendations that exceed the evidence shown.

## Data and semantic requirements

The model should provide:

- governed enterprise metrics reconciled to operational sources;
- approved plan, budget, forecast, prior-cycle, appetite, and benchmark values;
- absolute and relative variance with favorable/unfavorable directionality;
- materiality thresholds and concentration measures;
- contribution analysis from outcome to the few executive-level drivers;
- outlook, scenario range, assumptions, and confidence status where relevant;
- reporting-cycle snapshotting so prior briefings remain reproducible;
- metric definition, executive owner, source, refresh time, and certification status;
- commentary provenance and review status.

The executive layer must use the same underlying metric definitions as operational and analytical views. It is a curated semantic layer, not a separately maintained spreadsheet truth.

## Boundaries and failure modes

- **Vanity Metric Radar:** large numbers have no comparison, implication, or link to a strategic question.
- **Executive dress-up:** an operational dashboard is squeezed into small tiles and relabeled for leadership.
- **Chart-led interpretation:** the audience must find the anomaly and construct the explanation themselves.
- **False precision:** detailed forecasts imply certainty that the assumptions do not support.
- **Commentary drift:** narrative and numbers come from different cycles or definitions.
- **Interaction leakage:** filters and drill controls transfer curation work to the executive.
- **Premature prescription:** an implication is presented as a mandated action without owner, trigger, authority, or sign-off design.

## Acceptance checklist

- [ ] The primary executive audience, governance cycle, and executive questions are named.
- [ ] Every headline metric has a commitment or benchmark comparison and an executive implication.
- [ ] The most material change has clear visual priority.
- [ ] The core briefing fits on one intended screen or meeting page.
- [ ] Drivers are quantified, concentrated, and limited to those that change interpretation.
- [ ] Actuals, forecasts, scenarios, and judgments are visibly distinguished.
- [ ] Titles and annotations state conclusions rather than chart topics.
- [ ] Interaction is limited to choices leadership genuinely needs.
- [ ] Data status, scope, units, timing, and commentary provenance are visible.
- [ ] The view informs attention without implying an ungoverned approval workflow.

The design is complete when leadership can absorb the state, change, cause, and implication quickly enough to spend the meeting testing assumptions and discussing consequences rather than decoding the report.
