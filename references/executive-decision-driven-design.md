# Executive + Decision-Driven dashboard design

An Executive + Decision-Driven dashboard is a governed decision surface. It takes an executive from a material condition to a specific, authorized response: what changed, why it matters, which decision is in scope, who owns it, what triggers action, what the pre-agreed response is, and whether it has been acknowledged or approved.

This design is appropriate only when the audience holds the authority to make or ratify the decision. Without that authority and workflow, the dashboard should remain Executive + Insight-Driven.

## Design contract

| Dimension | Requirement |
| --- | --- |
| Primary audience | Executives or governance bodies with authority over the named decision |
| Core question | "What decision is required, under what conditions, and who acts next?" |
| Cadence | Aligned to governance meetings and material trigger events |
| Detail level | Headline condition, decision evidence, and controlled supporting detail |
| Interaction | Curated review plus explicit acknowledge, approve, reject, modify, or defer controls |
| Decision depth | Insight plus named decision, owner, trigger, pre-agreed action, and sign-off |
| Completion test | A triggered condition produces an attributable, time-bound decision and follow-through record |

## The What / So What / Now What contract

**What** — state the material condition as a governed comparison. Include current value, commitment or threshold, variance, direction, time horizon, and data state.

**So What** — explain the driver, enterprise consequence, urgency, and uncertainty. Make clear whether the condition is actual, forecast, scenario, or judgment.

**Now What** — define the decision rather than offering generic advice. Name the accountable role, trigger logic, required timing, pre-agreed action, authority, and sign-off state.

Example:

> **LCR: 114%, down 7 points month-on-month and 4 points above appetite**  
> Deposit outflows and revised stress assumptions account for 80% of the decline. Forecast headroom falls below appetite in five days.  
> **Decision:** If LCR closes below 115% for three consecutive business days, the Treasurer draws CFP Tranche 1 within one business day. ALCO Chair approval required.  
> **Status:** Trigger day 2 of 3; owner acknowledged; approval pending.

## Decision object

Treat each actionable item as a governed object with explicit fields:

| Field | Design requirement |
| --- | --- |
| Condition | The current state and comparison that make the issue material |
| Decision | The exact choice within the audience's authority |
| Owner | One accountable role, with delegates handled separately |
| Trigger | Metric, operator, threshold, duration, and evaluation frequency |
| Action | The pre-agreed response, including amount, scope, or policy change |
| Deadline | Decision and execution due times, with escalation timing |
| Authority | Policy, mandate, committee, or delegated limit permitting the action |
| Evidence | Governed metrics, assumptions, scenarios, and supporting sources |
| Sign-off | Acknowledge, approve, reject, modify, defer, and conditions |
| Follow-through | Execution state, proof, outcome measure, and review date |

Do not hide these fields in narrative prose alone. The dashboard should make missing ownership, expired authority, ambiguous triggers, and overdue decisions visibly incomplete.

## Information hierarchy

### 1. Decision queue

Lead with items requiring executive attention, ordered by urgency and materiality. Distinguish:

- triggered and awaiting decision;
- approaching trigger;
- approved and awaiting execution;
- executed and awaiting outcome review;
- closed, rejected, deferred, or expired.

Show the decision deadline, owner, trigger state, and blocker without requiring a drill.

### 2. Decision brief

For the selected item, present What, So What, and Now What in that order. The decision and requested authority should be readable in seconds. Keep supporting operational detail subordinate.

### 3. Evidence and alternatives

Show only the evidence required to validate the trigger and judge the pre-agreed action: annotated trends, contribution bridges, concentration, scenarios, sensitivities, and a small option comparison when discretion remains.

### 4. Action and sign-off

Place the requested response beside its owner, deadline, authority, and consequences. Provide explicit controls appropriate to the governance process. High-impact actions may require dual control or sequential approvals.

### 5. Execution and outcome

Keep approved decisions visible until execution is evidenced. Then track whether the intended outcome occurred at a stated review date. A decision is not complete when a button is clicked.

## Trigger design

A trigger must be computable and auditable:

> **If [governed metric] [operator] [threshold] for [duration or count] under [scope/scenario], then [owner] must decide [action] by [deadline].**

Specify:

- source metric, scope, unit, and aggregation grain;
- threshold and whether it is a floor, ceiling, band, or rate of change;
- persistence requirement, such as consecutive closes;
- evaluation schedule and business calendar;
- treatment of missing, late, corrected, or unreconciled data;
- hysteresis or reset rule to prevent repeated firing near a boundary;
- suppression, override, and expiry rules;
- notification and escalation path;
- trigger version and approval date.

Use early-warning bands to show proximity, but never confuse an amber warning with the formal trigger.

## Action and authority design

The action must be as precise as the trigger. Replace "review funding options" with a bounded response such as "draw $500M of CFP Tranche 1 within one business day."

For every action, display:

- accountable executive and executing team;
- authority source and remaining delegated limit;
- prerequisites and dependencies;
- amount, scope, duration, and reversibility;
- expected impact and principal downside;
- conflicts, segregation-of-duties rules, and required co-signers;
- decision SLA and escalation route;
- fallback when the preferred action cannot be executed.

The dashboard may recommend an action, but it must never bypass the organization's authorization controls.

## Sign-off and audit trail

The workflow should capture:

- authenticated actor and role;
- decision, timestamp, and dashboard/data version reviewed;
- approval conditions, limits, and rationale;
- comments and attached evidence;
- delegated or proxy authority where used;
- edits to the proposed action after review;
- execution confirmation and evidence;
- outcome review, exceptions, and closure reason.

Make states explicit: Draft, Monitoring, Triggered, Acknowledged, Approved, Rejected, Modified, Deferred, Executing, Executed, Reviewed, and Closed. State transitions should be controlled and historically reproducible.

## Visual and interaction rules

- Give triggered decisions stronger priority than stable metrics or general context.
- Use semantic status labels with color as a secondary cue.
- Keep the exact decision, owner, deadline, and requested response persistently visible.
- Separate observed fact, forecast, recommendation, and approved action.
- Show threshold proximity and persistence, not only a current red/amber/green state.
- Require confirmation for consequential actions and summarize what will be recorded before submission.
- Prevent silent double submission and show success, failure, stale-data, and conflict states.
- Preserve the reviewed filter, scenario, data, and policy versions with the decision.
- Make inaccessible actions visibly unavailable with the authority reason, not merely hidden.
- Keep operational investigation in governed drill paths or linked evidence, not on the executive decision surface.

## Data, semantic, and workflow requirements

The implementation should provide:

- governed metrics, comparisons, thresholds, and directionality;
- trigger evaluation with persistence, reset, suppression, and versioning;
- decision, owner, authority, action, deadline, and escalation entities;
- policy and mandate references with effective dates;
- scenario assumptions, sensitivities, and evidence provenance;
- append-only decision and state-transition history;
- authentication, role-based authorization, delegation, and segregation of duties;
- notifications with delivery and acknowledgment status;
- execution evidence and downstream system references;
- outcome measures and scheduled effectiveness review;
- reproducible snapshots of the data and commentary shown at sign-off;
- retention, privacy, and audit controls appropriate to the decision.

The dashboard must not implement a parallel approval process when an authoritative workflow already exists. Integrate with that system and display its state.

## Boundaries and failure modes

- **Authority gap:** the regular viewer cannot legally or organizationally authorize the displayed action.
- **Pseudo-decision:** a generic recommendation is labeled as a decision without a precise choice.
- **Trigger ambiguity:** the threshold lacks duration, scope, data treatment, or reset logic.
- **Action ambiguity:** the response says "monitor," "review," or "consider" without a bounded next step.
- **Approval theater:** a button changes dashboard status but does not update the authoritative workflow.
- **Stale sign-off:** data or assumptions change after review without invalidating approval.
- **Alert fatigue:** repeated near-threshold firing creates duplicate decisions.
- **Automation overreach:** a consequential action executes without required human authority or controls.
- **Fire and forget:** approval is recorded, but execution and outcome are never checked.

## Acceptance checklist

- [ ] The named audience holds authority for every decision displayed.
- [ ] Each item states What, So What, and a precise Now What.
- [ ] Decision, owner, trigger, action, deadline, authority, and sign-off are explicit.
- [ ] Trigger logic covers persistence, data quality, reset, suppression, and versioning.
- [ ] Early warnings are visually and semantically distinct from formal triggers.
- [ ] Actions are bounded, feasible, and linked to prerequisites and fallback paths.
- [ ] Role-based access, delegation, dual control, and segregation of duties are enforced where needed.
- [ ] The reviewed data, scenario, commentary, and policy versions are reproducible.
- [ ] Approval updates the authoritative workflow and leaves an append-only audit trail.
- [ ] Approved items remain visible through execution evidence and outcome review.
- [ ] Stale data, changed assumptions, conflicts, failures, and overdue states are handled explicitly.
- [ ] The workflow has been tested with triggered, rejected, modified, deferred, failed, and expired cases.

The design is complete when a material condition can move from governed evidence to an authorized decision, verified execution, and measured outcome without ambiguity about who decided what, under which trigger, using which evidence.
