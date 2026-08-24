# P&L Dashboard Current-State Teardown

## Executive summary

The current dashboard is a competent finance-analysis template, but it is not yet an executive briefing. It shows revenue, cost, gross margin, and net margin across an overview and a detailed P&L matrix, yet it gives every KPI similar visual weight and leaves the audience to determine which movement is material, why it occurred, and what deserves leadership attention.

The supplied extracts support a stronger briefing than the screenshots show. For the latest available actual period, 2020 Q4, net income is **$30.9K, $8.0K (35.1%) above budget**. Net margin is **22.8%, 4.8 percentage points above the 18% target**. The favorable net-income variance is led by revenue (**+$3.2K**) and COGS (**+$3.2K**) versus plan, followed by operating expense (**+$1.5K**). Collections exposure is close to its risk boundary: **14.7% of 2020 Q4 invoiced value remains outstanding versus a 15% threshold**.

## Inputs reviewed

| Input | Evidence used |
| --- | --- |
| `P&L_Report_Overview.png` | Two rows of KPI cards, cost breakdown, combined revenue/cost/margin trend, payment-status treemap, and date slider |
| `P&L_Report_2_Detail.png` | Expandable quarterly P&L matrix and date slider |
| `P&L Dashboard Requirements.png` | Finance/accounting audience; monthly and yearly performance; revenue, cost, margin, profitability, trends, previous-period comparison, and cost analysis |
| `gl_transactions.csv` | 333 transaction rows, 2020 Q2-Q4 |
| `chart_of_accounts.csv` | 12 P&L accounts with section, cost category, and sign semantics |
| `budget_targets.csv` | Quarterly targets by P&L section, 2017 Q1-2020 Q4 |
| `kpi_targets.csv` | Quarterly net-margin target and collections-risk threshold, 2017 Q1-2020 Q4 |
| `invoices.csv` | 102 invoices, 2020 Q2-Q4 |
| `customers.csv` | 22 customers across Online, Retail, and Wholesale segments |

## Apparent purpose and audience

The requirements describe a financial analysis tool for finance teams and accountants. The dashboard is intended to centralize recurring profitability monitoring and reduce spreadsheet review. Its current interaction model and detailed matrix fit that analyst workflow.

The forced target type changes the intended completion test. An executive audience should be able to state the material change, its business cause, and its implication without interpreting a dense matrix or reconciling multiple charts. The current dashboard does not meet that test.

## View inventory

### Overview view

#### Overview visual elements

| Element | Current content and grain | Assessment |
| --- | --- | --- |
| Date slider | A continuous range spanning approximately March 2017 to December 2020 | Broad exploratory control; it does not identify the reporting cycle, selected period, data freshness, or comparison basis clearly enough for an executive briefing. |
| Current Month cards | Revenue, Cost, Gross Margin, and Net Margin; each shows a value, percentage arrow, and previous-period value | The cards present bare outcomes but use equal prominence. Labels do not distinguish margin amount from margin percentage. Several displayed percentages are mathematically inconsistent with the adjacent values, weakening trust. |
| Current Financial Year cards | The same four measures at annual grain | Duplicates the card pattern and competes with the monthly row. No approved-plan or forecast comparison is shown. |
| Breakdown of Cost | Quarterly stacked columns for Marketing, Other, Shipping, and Transactions | Useful cost composition, but the title is topical rather than conclusion-led. The stack makes exact driver contribution hard to judge, and no variance-to-plan is visible. |
| Revenue, Cost & Net Margin | Quarterly clustered/stacked columns plus a line, with dual axes | Combines measures with different units and unclear line labeling. The title says what is plotted, not what changed. The viewer must find the inflection and infer its significance. |
| Payment Status | Treemap for Paid, Unpaid, and Partial | Shows composition without values, threshold, aging, trend, or customer concentration. Area comparison is weaker than a labeled risk metric and ranked exposure view. |

#### Visual hierarchy and reading order

The title dominates first, followed by eight equally weighted KPI cards. The payment treemap occupies a tall side rail despite lacking quantified risk context. The two explanatory charts arrive last and compete equally. The layout communicates abundance of information, not priority.

#### Questions answered today

- What are current-period and current-year revenue, cost, gross margin, and net margin?
- How have broad cost categories moved by quarter?
- How do revenue, cost, and a margin measure trend together?
- What is the broad mix of payment statuses?

#### Questions left to the viewer

- Which result is most material to leadership?
- Are results ahead or behind budget, forecast, or an approved target?
- Which drivers explain the variance, and how much did each contribute?
- Is the apparent performance change favorable after applying metric directionality?
- Is collections exposure inside tolerance, how close is it to the boundary, and where is it concentrated?
- What should leadership monitor in the next cycle?
- Are the displayed numbers certified, complete, and from the same reporting cycle?

### Detail view

#### Detail visual elements

| Element | Current content and grain | Assessment |
| --- | --- | --- |
| Date slider | Continuous range control | Repeats exploratory interaction without a clear period-close state. |
| Expandable P&L matrix | Rows for Revenue, COGS, Gross Profit, Operating Expenses, Operating Profit, Other Expenses, Total Income, Income Tax, and Net Income; columns by quarter | Appropriate for analyst reconciliation and drill-down, but too dense for the executive first screen. It provides actuals without budget variance, favorable/unfavorable semantics, materiality, annotations, or implication. |
| Drill controls | Row drill and hierarchy expansion | Useful in a governed detail path; distracting in a curated leadership briefing. |
| Total row | Quarterly total across the visible matrix | The meaning of the total is unclear because summing subtotal and component rows risks double counting conceptually. |

The matrix answers where a number sits in the P&L hierarchy, but not which line drove the enterprise outcome. It should remain a curated detail destination rather than the primary executive evidence surface.

## Requirements delivery gaps

| Requirement | Current delivery | Gap |
| --- | --- | --- |
| Revenue insights | Revenue cards and trend | No plan comparison, contribution explanation, or customer/segment driver. |
| Cost tracking | Cost cards and category stack | No budget variance or ranked contribution to profit variance. |
| Margins and profitability | Gross/net margin cards and trend | Labels mix currency and percentage concepts; target context and calculation semantics are absent. |
| Monthly and yearly performance | Separate KPI rows | The extracts are quarterly, while screenshots imply monthly/annual views. The production grain and fiscal calendar require confirmation. |
| Previous-period comparison | Card subtitles and arrows | Plan is the more decision-relevant executive comparison and is available in the extracts. Prior-period percentages shown in the screenshot appear inconsistent with the displayed values. |
| Deeper cost insights | Cost category stack and expandable matrix | No quantified variance bridge or materiality threshold. |
| Executive insight | Not stated in the source requirement | No conclusion, implication, outlook, attention agenda, or data-status context. |

## What / So What / Now What assessment

Scoring scale: 0 = absent, 1 = weak, 2 = partial, 3 = effective.

| Layer | Score | Evidence |
| --- | ---: | --- |
| What | 2/3 | Current values and period trends are visible, but metric definitions, units, directionality, and trustworthy comparison labels are inconsistent. |
| So What | 1/3 | Previous-period cues and cost composition provide context, but no budget, target, materiality, quantified driver contribution, or implication is stated. |
| Now What | 0/3 | No attention agenda, accountable area, monitoring horizon, or curated next view is provided. For this type, an implication is required, but a formal approval workflow is not. |
| **Total** | **3/9** | The dashboard reports performance but does not curate an executive interpretation. |

## Dashboard type fit

**Selected type:** `executive-insight-driven`

**Why this type is being used:** The requested mode explicitly forces an executive insight-driven redesign. It is also a reasonable destination for a P&L briefing: the core leadership question is what changed versus plan, what drove it, and what deserves attention. No evidence calls for approval controls, governed trigger/action objects, or a presenter-led one-off decision narrative, so `executive-decision-driven` and `executive-data-storytelling` would overstate the workflow.

### Current fit against the executive insight acceptance checklist

| Acceptance criterion | Status | Evidence or mismatch |
| --- | --- | --- |
| Audience, governance cycle, and executive questions named | Partial | Finance users are named; executive forum and cycle are not. |
| Every headline has a commitment comparison and implication | Fail | Cards use prior period only and provide no implication. |
| Most material change has visual priority | Fail | Eight cards have equal weight. |
| Core briefing fits one intended screen | Pass | The overview fits one screen, but density undermines comprehension. |
| Drivers are quantified and concentrated | Fail | Cost mix is shown; contribution to outcome variance is not. |
| Actual, forecast, scenario, and judgment distinguished | Fail | Only apparent actuals are shown; status is not labeled. |
| Titles and annotations state conclusions | Fail | Titles are chart topics and there are no annotations. |
| Interaction is limited to executive choices | Fail | Broad date slider and matrix drill expose analyst controls. |
| Scope, units, timing, data status, and provenance visible | Fail | Reporting date range appears, but certification and refresh state do not. |
| Attention is informed without false approval workflow | Partial | No false approvals exist, but no attention agenda exists either. |

Current fit: **1 pass, 2 partial, 7 fail**.

## Verified source evidence for the redesign

- 2020 Q4 revenue: **$135.6K**, **$3.2K (2.4%) above budget**, and **$5.6K (4.3%) above 2020 Q3**.
- 2020 Q4 COGS: **$55.0K**, **$3.2K favorable to budget** because expense is below plan.
- 2020 Q4 operating expense: **$41.9K**, **$1.5K favorable to budget**, although it increased **$1.7K** from 2020 Q3.
- 2020 Q4 gross profit: **$80.6K**, **$6.4K (8.6%) above budget**.
- 2020 Q4 net income: **$30.9K**, **$8.0K (35.1%) above budget** and **$3.3K (11.9%) above 2020 Q3**.
- 2020 Q4 net margin: **22.8%**, above the **18% governed target** by **4.8 percentage points**.
- Collections: **$23.8K outstanding**, equal to **14.7%** of 2020 Q4 invoiced value, only **0.3 percentage points below** the 15% risk threshold.
- Outstanding exposure is concentrated in four customers; the largest is River Goods at **$8.4K**.

## Data quality and evidence limitations

- Actual GL and invoice history covers only 2020 Q2-Q4. The 2017-2020 dates visible in the screenshots and target files are not matched by actual extracts, so year-over-year claims cannot be reproduced.
- Six invoice records have `paid_date` earlier than `invoice_date`; payment-timeliness and aging analysis must quarantine or correct these rows.
- The extracts contain no forecast, prior-governance-cycle snapshot, executive commentary, metric owner, certification state, materiality threshold, or entity/currency dimensions.
- Transaction descriptions are free text and cannot reliably establish causal drivers beyond account and cost category.
- The relationship checks otherwise pass: no duplicate business keys at the supplied grains, no unmapped GL accounts, no missing invoice customers, and no fiscal-quarter/date mismatches.

## Teardown conclusion

The current dashboard should retain its detailed matrix as a controlled finance drill path, but the first screen needs to become a curated quarterly leadership brief. The redesign should lead with net income and margin versus plan, explain the favorable variance with a compact contribution bridge, and elevate collections proximity to threshold as the principal attention item. This creates an executive implication without inventing a decision or approval workflow that the evidence does not support.
