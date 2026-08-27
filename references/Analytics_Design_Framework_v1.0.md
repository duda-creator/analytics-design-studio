# Analytics Design Framework

### A reference for designing the right dashboard for the right purpose, audience and decision

> **A note on the examples:** the worked examples throughout are drawn from bank Treasury — liquidity coverage (LCR), ALCO governance, contingency funding — because concrete beats generic. The framework itself is domain-agnostic and applies to analytics in any financial-services function: risk, finance, operations, trade, asset management, insurance. A short glossary of the Treasury terms used sits at the end of this document.

Every dashboard should answer a fundamental question: **what does this audience need to know, and what do they need to be able to do with it?**

A senior manager monitoring liquidity needs an immediate view of what has changed, where attention is required and whether action is needed. An analyst investigating a movement needs the ability to drill into drivers, compare periods, segment exposures and trace the number back to its underlying detail.

Get the design wrong and the dashboard becomes either **too shallow to support analysis or too complex to support decisions.**

This framework provides two complementary dimensions for diagnosing and designing analytical products: <br> **Dashboard Type** - who the product is designed for and how they interact with it, and <br> **Decision Depth** - how far the experience takes the user from simply seeing a status to understanding drivers and determining an appropriate action.

**The principle is simple: design for the decision, not the data.**

One dashboard should have **one primary purpose and one primary audience.** A single screen trying to serve as an executive briefing, operational monitoring tool and analyst workspace will inevitably compromise all three. The executive needs the answer quickly; the operator needs to identify exceptions; the analyst needs the freedom to investigate. These are different analytical experiences and should be designed accordingly.

Every dashboard carries an unspoken question: *how deep does this audience need to see, and how ready do they need to be to act on what they find?* Get that wrong and a board member ends up scrolling through raw transaction rows, or an analyst gets handed a red/amber/green tile with no way to dig underneath it. This framework gives you two independent axes to diagnose any dashboard against: **Type** (who it's built for, and how much they can poke at it) and **Decision Support Depth** (how much scaffolding sits behind each number — from a bare status light to a case built to win a room).

**One dashboard, one primary type, one primary audience.** A single screen trying to be a board briefing, a daily ops report, *and* an analyst's sandbox at once doesn't just look cluttered — it breaks for someone. A board member needs an answer in two seconds; an analyst needs the freedom to ask ten different questions in ten minutes. You can't engineer for both on the same screen — when a dashboard tries to, that's the diagnostic finding, not a detail to smooth over.

---

## The Framework at a Glance

Read top to bottom: first identify **who** the dashboard serves and how they use it (Type), then how much scaffolding sits behind each number (Depth), then whether this user actually holds the **authority** to act on what they see. Only when all three line up does the dashboard reliably produce action. Data Storytelling sits outside the main flow — an optional, opt-in communication layer, never a default.

```text
                 ANALYTICS DESIGN FRAMEWORK

                     ┌───────────────┐
                     │   DASHBOARD   │
                     │     TYPE      │
                     └───────┬───────┘
                             │
                WHO + HOW THEY USE IT
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
     Analytical         Operational         Executive
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                     DECISION DEPTH
                             │
                ┌────────────┼────────────┐
                │            │            │
            Snapshot      Insight      Decision
                │            │            │
                └────────────┼────────────┘
                             │
                     AUTHORITY / CONTEXT
                             │
                     Can this user act?
                             │
                             ▼
                          ACTION

              ───────────────────────────
                OPTIONAL COMMUNICATION
              ───────────────────────────
                     Data Storytelling
               "Make the case for the call"
```

---

## The Three Dashboard Types

| | 🔬 **Analytical**<br>*(the Microscope)* | 🎛️ **Operational**<br>*(the Cockpit)* | 📡 **Executive**<br>*(the Radar)* |
|---|---|---|---|
| **Analogy** | A detective's case board — pull any thread, follow it wherever it leads, nobody's timing you | A pilot's instrument panel — the same dozen gauges, checked every flight, tuned to the routes you actually fly | Air-traffic control radar — you're not tracking every rivet on every plane, just what's approaching and what needs a call right now |
| **Who's in the seat** | Analysts and ICs who need to dig | Team and function leads running the day-to-day | Senior leaders and the board, steering strategy |
| **The question it answers** | "Why did this happen?" | "How's my business doing this week?" | "What do I need to know or decide right now?" |
| **How much you can poke at it** | Slice it any way you like | Filter on the usual questions, drill down defined paths only | Look, don't touch — curated and clean |
| **Level of detail** | Down to the individual record, order, or session | Rolled up, with drill-through on the common questions | Headline numbers only |
| **Refresh rhythm** | Whenever someone needs to look | Daily, weekly, or monthly, on a fixed technical schedule | Tied to a meeting calendar (board, QBR), not a refresh schedule |
| **What "done" looks like** | The question gets answered, and someone else could reproduce it | The numbers are trusted and consistent every cycle | The room knows where things stand and what happens next |
| **A real-world example** | A risk analyst tracing yesterday's VaR spike down to desk and trade | A Trade Finance head's weekly view of settlement fails and limit utilization | A Treasurer's LCR, NII, and capital ratios walking into ALCO |

---

### Data Freshness vs. Consumption Rhythm

**Refresh cadence and consumption cadence are different design decisions.** A dashboard may refresh daily or intraday while being formally reviewed weekly or monthly. Data freshness is an architectural and control requirement; consumption rhythm is a user-behaviour and decision-context requirement.

A dashboard should therefore specify both:

- **Data refresh cadence:** when the underlying data becomes current.
- **Consumption / review rhythm:** when the audience is expected to use, review or act on it.

---

## The Decision Support Depth Ladder

Not every number needs the same scaffolding around it. The ladder measures how much interpretation and stakeholder commitment sits behind a metric — independent of dashboard type. One running example (a Treasury team watching LCR) shows the climb:

| Rung | It answers | You bring | Fuel-gauge analogy | Treasury example | Decision Support Depth |
|---|---|---|---|---|---|
| **Snapshot** *(Pulse Check)* | "What's happening?" | An agreed metric and a clear line for what "good" looks like | Your car's fuel gauge — full or empty | "LCR at 128%, comfortably above the 110% floor" | 1 |
| **Insight-Driven** *(Diagnosis)* | "...and why does it matter?" | Everything above, plus a comparison point (last period, budget, forecast, a peer) and a plain-English takeaway | The gauge, plus "you're burning gas faster than usual — you've been idling in traffic" | "LCR down 6 points vs. last month — stress-scenario outflow assumptions tightened" | 2 |
| **Decision-Driven** *(Prescription)* | "...so what are we doing about it?" | Everything above, plus a named decision, a named owner, a trigger point, a pre-agreed action, and sign-off | "Range hits 20 miles at this rate — pull over at the next station, 3 miles ahead" | "If LCR holds below 115% for three consecutive days, the Treasurer draws Tranche 1 of the CFP" | 3 |
| **Data Storytelling** *(Pitch)* | "Why should you decide this, right now?" | Everything above, plus a narrative someone builds and defends live, aimed at winning a specific call | The case you build for your partner, backed by six months of fuel receipts, for why the family needs an EV | The LCR trend and funding cost pressure laid out as the argument for approving the CFP drawdown at ALCO | 4 |

**The line between Snapshot and Insight-Driven is simple once you name it:** Snapshot tells you if a number is *good or bad*. Insight-Driven tells you *why*, compared to *what*, and *what that means*. A target on its own is Snapshot. A target with a "here's why it moved and what it's telling us" sentence attached is Insight-Driven.

---

## The Type × Depth Matrix
Not every type needs to climb the whole ladder. Type and Depth are complementary dimensions, but the useful combinations are constrained by purpose and authority.

| Type | Typical reachable depths | Primary purpose |
|---|---|---|
| **Analytical** | Variable / exploratory — see the flag test below | Investigate |
| **Operational** | Snapshot → Insight-Driven | Monitor and diagnose |
| **Executive** | Snapshot → Decision-Driven | Prioritise and decide |

**Authority unlocks the rung, not job title.** Decision-Driven is not exclusive to Executive dashboards. A user can legitimately receive a Decision-Driven experience when they genuinely hold delegated authority for the decision it supports. Where a decision is rule-based, the experience may additionally include triggers, pre-agreed actions and workflow/sign-off. Where the decision is judgement-based, the dashboard can remain decision-driven without pretending there is a deterministic trigger.

**The Analytical flag test** (instead of a rung): does each metric carry a comparison and a "so what," or is it raw? Score this per metric, not as one number. Analytical is deliberately not forced onto the depth ladder because its primary purpose is exploration rather than decision presentation.

**When an analyst keeps pulling the same cut every week, that's the signal to graduate it into an Operational or Executive metric** — a deliberate hand-off, not scope creep.

### One Metric, Three Experiences

**LCR does not determine the dashboard design. The decision context does.**

- **Analytical:** Which entities, currencies and cash-flow components drove the movement?
- **Operational:** Is LCR within tolerance, what changed since yesterday, and does anything require investigation?
- **Executive:** Is the liquidity position materially different from plan, and does management need to take action?

The metric is the same. The **experience, depth and decision context are different**.

---

## Pitfalls to Watch For

1. **The Everything-to-Everyone Trap** — one dashboard trying to be a board briefing, a daily ops report, and an analyst's sandbox at once. A "master dashboard" mixing trade-level detail with a headline capital-ratio tile for the board is the classic shape. Something always breaks — usually speed, sometimes trust.

2. **Executive Dress-Up** — taking a dense operational report, shrinking the font, and calling the tab "Executive Summary." An Executive view has to be curated from day one, not squeezed down after the fact. The tell: operational-density content (many small tiles, drill controls) wearing Executive labeling — e.g. a limit-utilization grid with the font shrunk and a "Board Summary" tab slapped on it.

3. **The Authority Gap** — wiring an Operational dashboard to a formal decision trigger when the person looking at it doesn't hold the authority to pull that trigger. Example: a desk head's daily dashboard is wired to "draw the facility if headroom drops below $50M" — but the actual draw decision belongs to the Treasurer, who never opens it. If the decision is real and someone *does* hold that authority, build it with Executive-tier rigor — don't bolt it onto a weekly ops report.

4. **The Fire-and-Forget Dashboard** — shipping a Decision-Driven dashboard and never checking whether the trigger fired and the named owner actually acted. Skip this, and a liquidity dashboard's CFP trigger quietly becomes a report with extra fields that nobody ever confirmed actually fired.

5. **The Vanity Metric Radar** — an Executive dashboard full of big, impressive-looking numbers ("Total Assets Under Management: $42B") with no comparison point and no connection to any decision. Headline-shaped, but content-empty — a Snapshot-level tile that's snuck onto an exec screen undiagnosed.

---

## Feature Library

Concrete, checkable signals for each Type and each Depth rung — written so a feature you spot points at one classification, not several. Use this both to diagnose current state (what's actually on screen) and to write revamp recommendations (what to add next).

### By Type

**🔬 Analytical**

- Record-level detail is available (individual orders, sessions, tickets, trades — not just aggregates)
- Free-form filter/pivot controls, not a fixed set of pre-built slices
- An ad hoc query or "explore" affordance (a pivot table, SQL box, formula bar)
- Flexible consumption / exploration — refresh cadence may be fixed, but analysis is not constrained to predefined questions
- Export/download capability — the point is to take the finding somewhere else
- Little to no narrative on screen — the analyst supplies the interpretation

*Example:* a market-risk analyst pivoting a trade blotter by desk, trader, and product to isolate yesterday's VaR spike.

*Revamp move:* if the same cut is being pulled every week, that's not a build gap — it's the signal to graduate the metric into an Operational or Executive view.

**🎛️ Operational**

- Rolled-up KPI tiles at a consistent unit of aggregation (per team, per day, per SKU) — not raw rows
- A fixed, repeating set of filters on well-worn dimensions (region, team, product line) — not free-form
- Defined drill-through paths (click a KPI → see its components), not open-ended exploration
- A visible refresh timestamp on a technical schedule ("as of Mon 9am", "updated hourly")
- Threshold or status coloring (RAG, sparkline trend) on each tile
- Built for repeat, habitual use — same people, same screen, same time, every cycle

*Example:* a Trade Finance head's daily view of settlement fails, limit utilization, and nostro breaks.

*Revamp move:* if tiles show numbers with no comparison, that's a Depth gap, not a Type gap — add context, don't rebuild the layout.

**📡 Executive**

- A small number of headline metrics — rule of thumb: fits on one screen, no scrolling
- No interactivity beyond maybe a date-range toggle — look, don't touch
- Heavy curation: every tile earned its place, nothing "might be useful"
- Cadence tied to a meeting calendar (board date, QBR), not a technical refresh schedule
- Generous whitespace, large type, minimal chart-junk
- Built from the same underlying numbers as the Operational/Analytical views, not a separately maintained set

*Example:* a Treasurer's LCR, NII, and capital-ratio tile walking into ALCO.

*Revamp move:* watch for Executive Dress-Up (above) — the tell is operational density with the font shrunk, not genuine curation.

### By Depth

**Snapshot** *(baseline)*

- A number or status with a target/threshold line
- Color-only signal (RAG) or a single trend arrow
- No comparison to another period, benchmark, or peer
- No explanatory text

*Revamp move:* add one comparison point (last period, target, or peer) and a one-sentence plain-English "why" — that whole jump is the move to Insight-Driven.

**Insight-Driven** *(new, on top of Snapshot)*

- A comparison point sits next to the number (vs. last period, budget, forecast, peer)
- A plain-English sentence explaining the movement — not just "down 6%" but "down 6% because X"
- Often a sparkline or delta arrow with a magnitude, not just direction

*Revamp move:* name the decision this insight should trigger, name who owns it, and state the trigger threshold and pre-agreed action — that's what makes it Decision-Driven.

**Decision-Driven** *(new, on top of Insight-Driven)*

- A named, specific decision the metric is wired to — not just "this matters"
- A named owner or accountable role
- A stated trigger point ("if X crosses threshold Y…")
- A pre-agreed action tied to the trigger
- A visible sign-off or acknowledgment mechanism, even just a status field

*Revamp move:* only climb further if a live decision genuinely needs winning in a room — build the narrative case (Data Storytelling). Don't do this by default.

**Data Storytelling** *(optional communication layer)*

- A built, sequential narrative — slides, a doc, a presented case — not a live dashboard screen
- Evidence assembled specifically to move a named audience to a specific decision, right now
- An explicit call to action or ask
- Built and defended live by a person, not self-serve

*Note:* never build or recommend this by default — it's opt-in, expensive to build and defend, and loses credibility when pushed on people who didn't ask for it.

---

## Diagnostic Defaults

When a target isn't stated, don't guess — use a known default and say so out loud:

- **Default type: Operational. Default depth: Insight-Driven.** Most unspecified requests are really asking "how's my business doing, and why" — exactly what this combination answers.
- **Analytical is never assumed.** Ad hoc, drill-to-record capability has to be explicitly requested or evidenced — defaulting to it invites an open-ended, unscoped diagnosis.
- **Snapshot, on either Operational or Executive, is a diagnostic finding, not a target.** If a dashboard is sitting there with no comparison and no insight, the standing recommendation is to revamp it to Insight-Driven.
- **Decision-Driven is the rung worth climbing toward** wherever an Insight-Driven dashboard has a real, nameable decision plausibly sitting behind it — call it out as a standing recommendation, not an instruction.
- **Data Storytelling is never a default and never a proactive recommendation.** Only assess or recommend it when explicitly requested.

---

## Glossary: Treasury Terms Used in the Examples

- **LCR (Liquidity Coverage Ratio)** — regulatory ratio of high-quality liquid assets to projected 30-day stressed net cash outflows; must stay above a floor (100% regulatory, often a higher internal appetite).
- **ALCO (Asset & Liability Committee)** — the senior committee governing balance-sheet, liquidity, and interest-rate risk decisions.
- **CFP (Contingency Funding Plan)** — a pre-approved playbook of funding actions, usually staged in tranches, drawn on in a liquidity stress.
- **NII (Net Interest Income)** — interest earned minus interest paid; a core earnings measure of the banking book.
- **VaR (Value at Risk)** — a statistical estimate of potential portfolio loss over a given horizon at a given confidence level.
- **Nostro breaks** — unreconciled differences on accounts a bank holds with other banks.
