# Executive + Data Storytelling decision-artifact design

Executive + Data Storytelling is a presenter-led decision artifact built to win a specific, time-bound call from an authorized audience. On the framework's Decision Support Depth ladder it is rung 4 of 4 (*Pitch*) — an optional communication layer built on top of a Decision-Driven foundation: a built, sequential narrative (slides, a doc, a presented case), not a live dashboard screen. It uses governed dashboard evidence, but it is not a general-purpose self-service dashboard. The design is sequential: it establishes the stakes, explains the change, tests alternatives, makes a recommendation, and ends with an explicit ask.

Use this combination only when a real decision must be made in a live forum and the case requires explanation or persuasion. It is expensive to prepare, easy to overuse, and weakens trust when every reporting cycle is treated as a dramatic story. Per the framework, Data Storytelling is never a default and never a proactive recommendation — build it only when explicitly requested for a real decision event.

## Design contract

| Dimension | Requirement |
| --- | --- |
| Framework position | Executive type (*the Radar*) at Data Storytelling depth — rung 4 of 4 (*Pitch*), a communication layer over a Decision-Driven foundation |
| Primary audience | A named executive committee, board, or authorized decision forum |
| Core question | "Why should we make this specific decision now?" |
| Data refresh cadence | A reproducible snapshot as of the meeting's as-of date — no routine refresh |
| Consumption rhythm | A scheduled decision event, presented live |
| Detail level | Curated evidence required to defend one recommendation |
| Interaction | Presenter-controlled sequence with optional evidence drill-down |
| Decision depth | Decision workflow plus a coherent case, alternatives, and explicit ask |
| Completion test | The forum can approve, reject, modify, or defer the ask with assumptions and consequences understood |

## Preconditions

Do not start with charts. Confirm the decision contract:

- **Decision:** the exact choice the forum is being asked to make;
- **Decision maker:** the person or body with authority;
- **Deadline:** why the choice is required now;
- **Options:** credible alternatives, including the status quo where legitimate;
- **Criteria:** the agreed outcomes, constraints, and risk appetite used to judge options;
- **Recommendation:** the proposed choice and accountable sponsor;
- **Implementation owner:** who acts after approval;
- **Evidence standard:** what must be true, reconciled, or independently reviewed;
- **Decision record:** how the outcome, conditions, and dissent will be captured.

If the ask cannot be written as a specific choice, remain at Executive + Insight-Driven until it can.

## Narrative spine: Context / Tension / Evidence / Choice / Resolution

### 1. Context

Establish the agreed baseline in one view: current position, prior commitment, relevant constraints, and the objective leadership already recognizes. Do not spend the opening teaching definitions that should have been pre-read.

### 2. Tension

State what changed and why the existing plan is no longer sufficient. Quantify magnitude, timing, and exposure. The tension must be a business condition, not manufactured drama.

### 3. Evidence

Explain the material drivers, uncertainty, and consequences. Use only the evidence needed to test the choice: trends, variance bridges, concentration, scenario ranges, sensitivities, and external benchmarks.

### 4. Choice

Compare a small set of viable options against the agreed criteria. Make trade-offs visible and use consistent assumptions. Name what each option costs, protects, delays, or makes irreversible.

### 5. Resolution

State the recommendation, explicit ask, accountable owner, implementation milestones, trigger conditions, and requested sign-off. Show what will happen immediately after approval and how outcomes will be monitored.

The narrative should survive this one-sentence test:

> **Because [material change], we need to decide [specific choice] by [deadline]; the evidence favors [option] because [criteria], with [principal risk and mitigation].**

## Recommended sequence

| Beat | Executive question | Evidence form |
| --- | --- | --- |
| 1. The ask | What are you asking us to decide? | One-sentence decision and deadline |
| 2. What changed | Why is this on the agenda now? | Headline variance and annotated trend |
| 3. Why it changed | What explains the shift? | Driver bridge or contribution view |
| 4. Stakes | What happens if we act or wait? | Scenario range and consequence timeline |
| 5. Options | What credible choices do we have? | Consistent option comparison |
| 6. Recommendation | Why this option? | Criteria-based case and sensitivities |
| 7. Execution | Who does what after approval? | Owner, milestones, triggers, controls |
| 8. Decision | What exactly must be recorded? | Approve/reject/modify/defer and conditions |

This is a narrative sequence, not eight mandatory slides. Combine beats when the decision is simple; never scatter the ask across the presentation.

## Designing the evidence

- Use declarative titles that state the conclusion supported by each view.
- Put one argumentative job on each page or state: establish, explain, compare, recommend, or ask.
- Reveal complexity progressively; keep technical evidence available without placing it in the main reading path.
- Annotate material inflections, assumptions, and discontinuities directly on the evidence.
- Use common scales, horizons, and assumptions across option comparisons.
- Show uncertainty as ranges, sensitivities, or scenarios rather than hiding it behind a point estimate.
- Distinguish facts, forecasts, management judgments, and recommendations visually and verbally.
- Show source, as-of date, scope, and reconciliation state unobtrusively on every evidence page.
- Use animation only to control sequence or reveal causality; never to decorate.
- Preserve a printable or static version so the decision record does not depend on live software state.

## Option comparison

Compare options against pre-agreed criteria rather than a collection of unrelated pros and cons. Typical criteria include:

- strategic fit and expected benefit;
- capital, liquidity, earnings, or cost impact;
- risk appetite and regulatory consequences;
- implementation time, capacity, and dependencies;
- reversibility and option value;
- downside under plausible stress scenarios;
- customer, conduct, and reputational impact.

For each option, show the same horizon and assumptions. Identify dominated or infeasible options transparently; do not construct a weak alternative merely to make the recommendation look inevitable.

## The recommendation and ask

The final decision view should include:

- the exact recommendation and amount, scope, or policy change;
- the authority being requested and from whom;
- the deadline and consequence of deferral;
- the accountable executive and implementation owner;
- the principal assumptions and risks;
- conditions, limits, or guardrails attached to approval;
- immediate next step and first monitoring checkpoint;
- controls for approve, reject, modify, or defer;
- a durable record of sign-off, conditions, and rationale.

Do not finish on a summary of facts. Finish on the decision.

## Live presentation and challenge design

The presenter owns the sequence and must be able to defend the evidence. Prepare for challenge without bloating the main story:

- keep an indexed evidence appendix mapped to likely questions;
- define which assumptions are material enough to change the recommendation;
- prepare sensitivity views for those assumptions;
- expose counter-evidence and known limitations;
- assign subject-matter owners for technical questions;
- rehearse paths for approval, conditional approval, deferral, and rejection;
- capture questions that require post-meeting validation.

The artifact should support discussion, not script it so tightly that legitimate challenge becomes difficult.

## Data and governance requirements

The evidence base should provide:

- governed metrics reconciled to the same semantic layer as regular reporting;
- reproducible snapshots for the meeting's as-of date;
- approved plan, prior commitment, benchmarks, and risk appetite thresholds;
- option assumptions, dependencies, costs, benefits, and scenario outputs;
- sensitivity analysis for material uncertain inputs;
- data lineage, quality, certification, and model-validation status;
- commentary and recommendation authorship with review history;
- version control for pre-read, meeting version, and final decision record;
- role-based access for confidential evidence;
- post-decision measures, trigger monitoring, and outcome review dates.

## Boundaries and failure modes

- **Story without a decision:** the sequence is polished, but no exact choice or authority request exists.
- **Cherry-picked evidence:** only facts favorable to the recommendation are shown.
- **False binary:** options are framed as the recommendation versus an obviously unacceptable alternative.
- **Data dump:** the presentation follows source-system structure instead of an argument.
- **Drama inflation:** normal variance is presented as a crisis to force urgency.
- **Hidden uncertainty:** point estimates conceal assumptions that could reverse the recommendation.
- **Presenter dependency:** the visuals are unintelligible without one individual and leave no durable record.
- **Decision theater:** sign-off is displayed, but the real choice was already made elsewhere or the forum lacks authority.
- **Fire and forget:** implementation and outcome measures disappear after approval.

## Acceptance checklist

- [ ] One specific decision, authorized forum, deadline, and sponsor are named.
- [ ] The opening states the ask and the reason it is required now.
- [ ] The narrative moves coherently from change and evidence to options and recommendation.
- [ ] Options use consistent criteria, assumptions, horizons, and scenarios.
- [ ] Material uncertainty, counter-evidence, and downside are visible.
- [ ] Every page has a declarative conclusion and a clear role in the argument.
- [ ] The final view requests an explicit recorded decision and any conditions.
- [ ] Owners, milestones, guardrails, triggers, and monitoring are defined.
- [ ] The evidence is governed, reproducible, versioned, and suitable for a durable record.
- [ ] An appendix supports challenge without overwhelming the main sequence.
- [ ] The artifact remains understandable in static form after the meeting.
- [ ] A post-decision review will test whether the promised outcome occurred.

The design is complete when the audience can challenge the case, compare credible options, understand uncertainty, and make a recorded decision without reconstructing the argument from raw analysis.
