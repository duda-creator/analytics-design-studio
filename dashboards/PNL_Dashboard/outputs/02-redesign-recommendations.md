# P&L Dashboard Redesign Recommendations

## Design contract

**Target type:** `executive-insight-driven`

**Primary executive question:** Are we delivering profitable growth against plan, what explains the result, and what could weaken the outlook?

**Proposed cadence:** Quarterly close briefing, published after Finance certification and preserved as a reproducible reporting-cycle snapshot.

**Completion test:** A leader can state the material performance result, the two largest drivers, and the principal attention item in under one minute without manipulating filters.

The redesign uses the Executive + Insight-Driven contract as primary guidance and the What / So What / Now What framework from the Executive + Decision-Driven reference as its baseline. It does not add approval buttons, formal triggers, or sign-off controls because those are not supported by the requirements.

## Executive narrative for the supplied data

> **2020 Q4 net income reached $30.9K, $8.0K (35.1%) above budget, as revenue outperformance and lower-than-planned COGS each contributed about $3.2K; collections exposure is 14.7%, only 0.3 percentage points inside the risk threshold.**

This is the first-read message. It combines outcome, commitment, quantified drivers, and implication. It replaces the generic `Profit & Loss Report` title as the visual focal point.

## What / So What / Now What by metric

| Metric or section | What | So What | Now What |
| --- | --- | --- | --- |
| Net income | 2020 Q4 net income is **$30.9K**, **$8.0K (35.1%) above budget** and **$3.3K (11.9%) above Q3**. | The result materially exceeds the approved plan and improved sequentially. Revenue, COGS, and operating expense all contributed favorably versus budget. | Keep the result as the primary headline; direct attention to whether favorable COGS can persist and whether collections risk could weaken cash conversion next quarter. |
| Net margin | Net margin is **22.8%**, **4.8 percentage points above the 18% target** and **1.6 points above Q3**. | Margin performance is stronger than both commitment and recent trajectory. The dashboard must compute this from revenue and signed expenses, never sum or average stored percentages. | Show target headroom beside the outcome and monitor the margin outlook once forecast data becomes available. |
| Revenue | Revenue is **$135.6K**, **$3.2K (2.4%) above budget** and **$5.6K (4.3%) above Q3**. | Revenue is a material positive contributor, but the current extracts do not identify product, channel, or customer revenue drivers because GL revenue is not linked to invoices or customers. | Show revenue contribution in the bridge; label causal attribution as unavailable until a governed revenue-to-customer/product mapping exists. |
| COGS / gross profit | COGS is **$55.0K**, **$3.2K favorable to budget**; gross profit is **$80.6K**, **$6.4K (8.6%) above budget**. | Revenue growth did not require above-plan COGS, producing stronger gross profit. However, sustainability cannot be inferred from one quarter or free-text transaction descriptions. | Rank COGS account contributions and flag the evidence as actual variance, not a forecast of structural savings. |
| Operating expense | Operating expense is **$41.9K**, **$1.5K favorable to budget**, but **$1.7K higher than Q3**. | The plan comparison is favorable while the sequential direction is unfavorable. Showing only one comparison would overstate certainty. Salaries and Wages is the largest account at **$29.6K**. | Present budget as primary and Q3 as secondary context; allow a curated link to the account detail matrix. |
| Collections | **$23.8K**, or **14.7%** of 2020 Q4 invoiced value, remains outstanding versus a **15% risk threshold**. | The position is technically inside tolerance but has only **0.3 percentage points** of headroom. Four customers hold the positive outstanding exposure; River Goods alone accounts for **$8.4K**. | Place collections in the attention agenda with a ranked customer view. Do not claim overdue aging until the six paid-before-invoice anomalies are corrected and an explicit as-of date is governed. |
| Detailed P&L | The matrix provides quarterly account-line actuals and hierarchy drill. | It supports reconciliation but overwhelms the executive first screen and omits plan variance and materiality. | Retain as a separate `Finance detail` view with Actual, Budget, Variance, and Variance % columns plus expandable accounts. |

## Proposed first-screen layout

### 1. Briefing header

Use a compact full-width band containing:

- reporting cycle: `2020 Q4 close`;
- status: `Actual | Finance certification pending` until a certification source exists;
- scope and units: `Enterprise P&L | USD thousands`;
- refresh timestamp and source version;
- the declarative headline above.

Remove the oversized generic title and continuous date slider. Replace the slider with a restrained reporting-cycle selector whose default is the latest certified close. A scenario toggle should remain hidden until forecast or scenario data exists.

### 2. Material outcome

Give net income the strongest position and largest value treatment:

**Net income $30.9K | +$8.0K / +35.1% vs budget**  
`Margin 22.8%, 4.8pp above target; +$3.3K vs Q3.`

Use a single semantic favorable marker with text. Do not use green/red arrows without directionality metadata.

### 3. Supporting enterprise outcomes

Show three compact, aligned measures beneath the headline:

| Outcome | Primary comparison | Secondary context |
| --- | --- | --- |
| Revenue `$135.6K` | `+$3.2K / +2.4% vs budget` | `+$5.6K vs Q3` |
| Gross profit `$80.6K` | `+$6.4K / +8.6% vs budget` | `59.4% gross margin` |
| Operating expense `$41.9K` | `$1.5K favorable vs budget` | `$1.7K higher than Q3` |

These are not four equal hero cards. Net income is the conclusion; the other measures are evidence.

### 4. Driver evidence

Replace `Breakdown Of Cost` and the dual-axis `Revenue, Cost & Net Margin` chart with one **net-income variance bridge**:

`Budget net income $22.9K` → Revenue `+$3.2K` → COGS `+$3.2K` → Operating expense `+$1.5K` → Other expense and tax `+$0.1K` → `Actual net income $30.9K`.

Use directly labeled bars with favorable/unfavorable semantics. This answers why the result changed against the commitment. Add one annotation: `Revenue and COGS account for 80% of the favorable variance.`

### 5. Attention agenda

Replace the unlabeled payment-status treemap with a compact evidence panel:

#### Collections exposure is 14.7%, 0.3pp inside threshold

- Horizontal bullet or threshold bar from 0% to 20%, with the 15% threshold explicitly labeled.
- Ranked exposure list: River Goods `$8.4K`, Harbor Market `$6.1K`, Maple Wholesale `$5.7K`, Vista Trading `$3.6K`.
- Evidence status: `Aging unavailable pending correction of 6 paid-before-invoice records.`
- Accountable area: `Finance / Accounts Receivable`, pending confirmation of a named executive owner.
- Horizon: `Review at next certified quarter close; escalate earlier if governed monitoring is introduced.`

This is an attention item, not a formal trigger or approval workflow.

### 6. Curated detail link

Add one text link, `Open finance detail`, leading to the P&L matrix. Remove drill icons from the executive surface. Preserve the selected reporting cycle and scope when opening detail.

## Wireframe

```text
+--------------------------------------------------------------------------------+
| 2020 Q4 CLOSE | ACTUAL | USD $K | DATA STATUS | REFRESHED                      |
| Net income $30.9K, $8.0K above budget, led by revenue and COGS                 |
+--------------------------------------------------------------------------------+
| NET INCOME                     | REVENUE       | GROSS PROFIT | OPEX            |
| $30.9K  +$8.0K vs plan         | $135.6K       | $80.6K       | $41.9K          |
| Margin 22.8%, +4.8pp to target | +2.4% plan    | +8.6% plan   | $1.5K favorable |
+------------------------------------------------+-------------------------------+
| WHY PERFORMANCE BEAT PLAN                     | ATTENTION                      |
| Budget NI -> Revenue -> COGS -> Opex -> Actual | Collections 14.7% / 15% limit |
| $22.9K       +3.2     +3.2     +1.5    $30.9K | Top exposures + evidence note |
+------------------------------------------------+-------------------------------+
| Outlook / assumptions unavailable | Open finance detail                       |
+--------------------------------------------------------------------------------+
```

## Interaction changes

| Current interaction | Redesign |
| --- | --- |
| Continuous date slider | Certified reporting-cycle selector; latest close by default |
| Broad chart exploration | Look-first briefing with direct labels and annotations |
| Matrix drill controls on primary surface | One curated link to finance detail |
| Treemap hover dependency | Values, threshold, and concentration visible without hover |
| Equal emphasis across periods | One primary comparison: budget; Q3 used only when it changes interpretation |
| Implicit filters | Persistent scope, units, cycle, and data-status labels |

## Visual language

- Use a restrained neutral canvas with dark ink, one brand accent, and semantic favorable/adverse/attention colors.
- Reserve the largest type for the declarative conclusion, not the dashboard name or every metric.
- Direct-label the bridge and threshold view; remove legends where labels can sit on the evidence.
- Use color only after applying metric directionality: lower costs are favorable, higher revenue and profit are favorable, and collections proximity is attention rather than failure.
- Keep the first screen within a standard 16:9 meeting display. Do not scroll the core briefing.
- Avoid decorative cards and heavy borders. Use alignment, whitespace, and typography to establish hierarchy.

## Finance detail redesign

Retain a separate matrix because it answers a valid reconciliation question. Change it to:

- rows: P&L section, account, then transaction only on deliberate drill;
- columns for the selected quarter: Actual, Budget, Variance, Variance %, Q3 Actual, and optional YTD after fiscal logic is confirmed;
- subtotals computed once, avoiding any total that sums both detail and subtotal rows;
- favorable/unfavorable labels driven by account directionality;
- a materiality filter defaulted to the configured executive threshold;
- visible data-quality and reconciliation status;
- export restricted to the finance detail view, not the executive brief.

## Metric definitions

| Metric | Definition |
| --- | --- |
| Signed amount | `gl_transactions.amount × chart_of_accounts.normal_sign` |
| Revenue | Sum of signed amount where `pl_section = Revenue` |
| Gross profit | Revenue + signed COGS |
| Net income | Revenue + signed COGS + signed operating expense + signed other expense + signed tax |
| Gross margin % | Gross profit / Revenue; recomputed after aggregation |
| Net margin % | Net income / Revenue; recomputed after aggregation |
| Variance to budget | Actual signed amount − budget signed amount |
| Favorable variance | Variance interpreted using metric directionality; positive signed contribution improves net income |
| Outstanding amount | Invoice amount − amount paid |
| Outstanding % | Sum outstanding amount / sum invoice amount for the governed invoice cohort |
| Threshold headroom | Collections-risk threshold − outstanding % |

## Implementation priorities

1. **Reconcile and certify the semantic layer.** Confirm fiscal calendar, currency, scope, signs, margin definitions, and whether invoice collections belongs on a P&L executive brief.
2. **Build actual-versus-budget measures and the variance bridge.** This supplies the primary executive comparison and quantified drivers.
3. **Correct invoice date anomalies and define the collections cohort/as-of rule.** Do not add aging before this is resolved.
4. **Publish the one-screen executive brief and preserve the matrix as detail.** Validate it at the intended meeting resolution.
5. **Add governed commentary and provenance.** Capture author, review state, metric owner, data refresh, and snapshot version.
6. **Source forecast and longer actual history.** Only then add outlook or year-over-year claims.

## Traceability to Stage 1

- Equal-weight KPI cards drive the recommendation for one dominant net-income outcome.
- Missing plan context drives the use of `budget_targets.csv` as the primary comparison.
- The topical cost chart drives the variance bridge recommendation.
- The dual-axis trend's interpretation burden drives direct labels and a single explanatory view.
- The unlabeled payment treemap drives the threshold-and-concentration attention panel.
- The dense matrix drives a separate finance detail path.
- Inconsistent screenshot percentages and absent data status drive metric definitions, directionality, certification, and provenance requirements.
- Limited actual history and invoice anomalies constrain claims about year-over-year performance and aging.
