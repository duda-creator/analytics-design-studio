# Analytics Design Studio

Tech-agnostic workflow for taking a dashboard request from raw requirements to a signed-off design
and a working prototype. It deliberately stops before any platform commitment.

Pairs with **analytics-delivery-kit**, which builds the signed-off design on a chosen platform. The
two repos are independent: this one delivers value on its own as a design engagement, and the
delivery kit can be entered directly when the platform is already agreed.

## Requirements

Python 3.12. Nothing else — every script in this repo is standard library only. No database, no
Docker, no `pip install`.

## Workflow

| Step | Skill | Output |
| --- | --- | --- |
| 0 | `md-dashboard-diagnostic` | `{name}_diagnostic.md`, `{name}_scorecard.html` |
| 1 | `md-dashboard-redesign` | `01-current-state-teardown.md` … `04-data-flow-spec.md`, `dashboard-redesign.html` |
| 2 | `md-metric-spec` *(pending)* | `06-metric-spec.md` |
| 3 | `md-dashboard-mockup` *(pending)* | `05-mockup.html`, `05-mockup-notes.md` |
| 4 | `md-dashboard-datamap` *(pending)* | `07-datamap.md`, `08-target-spec/*.spec.csv` |
| 5 | `scripts/generate_fixture_data.py` *(pending)* | `fixtures/*.csv`, `fixtures/_provenance.md` |
| 6 | POC build | prototype dashboard |
| 7 | Sign-off + Architecture Decision Record (ADR) | `references/adr/0001-technology-selection.md` |

Steps 2-5 are not yet implemented. Steps 0-1 are.

## Layout

```
dashboards/<name>/inputs/{screenshots,requirements,sample_data}/
dashboards/<name>/outputs/          design artifacts
handoff/                            exported bundles for the delivery kit
references/                         design references read by the redesign skill
.github/skills/                     the workflow itself
```

`dashboards/PNL_Dashboard/` is a worked example of steps 0-1.

## Handoff

At sign-off, export a bundle to `handoff/`. Only two artifacts are contract:

- `08-target-spec/*.spec.csv`
- `06-metric-spec.md`

Everything else in the bundle — mockup, teardown, recommendations, data model, ADR — is context for
a human reader and is never machine-validated. The delivery kit owns the handoff schema and
validates on ingest; this repo only has to emit a shape it accepts.

## Rules

- Stay tech-agnostic. Canonical SQL types only (`DECIMAL(18,2)`, `VARCHAR`), never dialect types.
  Metric formulas in business terms, never SQL or DAX.
- If the platform is already decided, that is the signal to start in the delivery kit instead.
- The mockup is where stakeholder churn belongs. Iterate freely there; freeze the spec afterwards.
