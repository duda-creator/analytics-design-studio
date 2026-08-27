# Analytics Design Studio

Tech-agnostic workflow for taking a dashboard request from raw requirements to a signed-off design
and a working prototype. It deliberately stops before any platform commitment.

Pairs with **analytics-delivery-kit**, which builds the signed-off design on a chosen platform. The
two repos are independent: this one delivers value on its own as a design engagement, and the
delivery kit can be entered directly when the platform is already agreed.

## Requirements

Python 3.12. Nothing else — every script in this repo is standard library only. No database, no
Docker, no `pip install`.

## Quick Start

Create a new repository from this template, replacing `my-dashboard-project` with your project
name:

```powershell
gh repo create duda-creator/my-dashboard-project `
  --template duda-creator/analytics-design-studio `
  --public
gh repo clone duda-creator/my-dashboard-project
cd my-dashboard-project
code .
```

Use `--private` instead of `--public` when the project should not be publicly visible. Confirm that
Python 3.12 is available:

```powershell
python --version
```

Add dashboard inputs under `dashboards/<name>/inputs/`:

```text
dashboards/
  MyDashboard/
    inputs/
      requirements/
      sample_data/
      screenshots/
```

`dashboards/PNL_Dashboard/` is a worked example. Start a new dashboard with
`/md-dashboard-diagnostic new <name>` or `/md-dashboard-redesign new <name>`, add screenshots and
requirements under `inputs/`, then run the corresponding skill. Steps 2-5 in the workflow are
currently pending.

Diagnostic outputs use the dashboard-specific names `dashboards/<name>/outputs/<name>_diagnostic.md`
and `dashboards/<name>/outputs/<name>_scorecard.html`. Every diagnostic report closes with a
**Proposed Action** — `Retain`, `Revamp`, `Split into: [...]`, or `Flag for portfolio comparison` —
and `/md-dashboard-diagnostic compare <name1> <name2> ...` compares 2+ already-diagnosed dashboards,
writing `dashboards/_comparisons/<name1>-<name2>..._portfolio-synthesis.md` with a `Retain` /
`Merge` / `Retire` call for each. See [Sequencing the diagnostic skill](#sequencing-the-diagnostic-skill)
below for how this feeds into `md-dashboard-redesign`.

Commit and push your project when ready:

```powershell
git add .
git commit -m "Initialize dashboard project"
git push
```

## Workflow

For engagements that assess and rationalize multiple related dashboards around one common logical
data model, use the [Portfolio Dashboard Design Workflow](references/dashboard-portfolio-workflow.md).
It defines two linked workflows: rapid portfolio assessment, followed by comprehensive design,
prioritization, conceptual mockups, three stakeholder gates, and technology-agnostic handoff.

### Sequencing the diagnostic skill

Always run `md-dashboard-diagnostic` first, no matter which of these you're starting from — its
closing **Proposed Action** is what tells you how many `md-dashboard-redesign` runs come next, and
on which names. `md-dashboard-redesign` always runs once per *target* dashboard name, never once
per input.

- **Single dashboard, revamp in place** (`Retain` / `Revamp`):

  ```powershell
  /md-dashboard-diagnostic new PNL_Dashboard
  # add screenshots/requirements under dashboards/PNL_Dashboard/inputs/
  /md-dashboard-diagnostic PNL_Dashboard
  /md-dashboard-redesign PNL_Dashboard
  ```

- **One cluttered/multi-view dashboard, split into several** (`Split into: [...]`):

  ```powershell
  /md-dashboard-diagnostic BigReport
  # Proposed Action: Split into Exec_Summary, Ops_Detail
  /md-dashboard-redesign new Exec_Summary
  /md-dashboard-redesign new Ops_Detail
  /md-dashboard-redesign Exec_Summary
  /md-dashboard-redesign Ops_Detail
  ```

- **Several existing dashboards, check for overlap** (`Flag for portfolio comparison`):

  ```powershell
  /md-dashboard-diagnostic DashA
  /md-dashboard-diagnostic DashB
  /md-dashboard-diagnostic DashC
  /md-dashboard-diagnostic compare DashA DashB DashC
  # Proposed Action: Merge DashB + DashC -> Consolidated_BC, Retain DashA
  /md-dashboard-redesign new Consolidated_BC
  /md-dashboard-redesign Consolidated_BC
  /md-dashboard-redesign DashA
  ```

Each input dashboard keeps its own `inputs/` folder throughout — `compare` reads existing
`<name>_diagnostic.md` reports only, it never merges screenshots or sample data across dashboards.

| Step | Skill | Output |
| --- | --- | --- |
| 0 | `md-dashboard-diagnostic` | `{name}_diagnostic.md`, `{name}_scorecard.html`, optional `_comparisons/*_portfolio-synthesis.md` |
| 1 | `md-dashboard-redesign` | `01-current-state-teardown.md` … `04-data-flow-spec.md`, `dashboard-redesign.html` |
| 2 | `md-metric-spec` *(pending)* | `05-metric-spec.md` |
| 3 | `md-dashboard-mockup` *(pending)* | `06-mockup.html`, `06-mockup-notes.md` |
| 4 | `md-dashboard-datamap` *(pending)* | `07-datamap.md`, `08-target-spec/*.spec.csv` |
| 5 | `scripts/generate_fixture_data.py` *(pending)* | `fixtures/*.csv`, `fixtures/_provenance.md` |
| 6 | POC build | prototype dashboard |
| 7 | Requirements sign-off + handoff readiness | approved bundle in `handoff/` |

Steps 2-5 are not yet implemented. Steps 0-1 are.

## Smoke Tests

The template includes a standard-library-only GitHub Actions check. It compiles the Python scripts,
runs both helper entrypoints with `--help`, and validates the worked-example HTML. Run the same checks
locally from the repository root:

```powershell
python -m compileall -q scripts .github/skills
python scripts/profile_sample_data.py --help
python scripts/validate_dashboard_html.py dashboards/PNL_Dashboard/outputs/dashboard-redesign.html `
  --require "01 / Current state teardown" "02 / Redesign recommendations" "executive-insight-driven"
```

## Layout

```text
dashboards/<name>/inputs/{screenshots,requirements,sample_data}/
dashboards/<name>/outputs/          design artifacts
dashboards/_comparisons/            cross-dashboard portfolio-synthesis files from `compare`
portfolios/<portfolio>/             future multi-dashboard engagement convention
portfolios/<portfolio>/dashboards/<name>/
                                    dashboard-specific portfolio artifacts
handoff/                            exported bundles for the delivery kit
references/                         shared project references
.github/skills/md-dashboard-redesign/reference/
                                    redesign skill references
.github/skills/                     the workflow itself
```

`dashboards/PNL_Dashboard/` is a worked example of steps 0-1.

## Handoff

At sign-off, export a bundle to `handoff/`. Only two artifacts are contract:

- `08-target-spec/*.spec.csv`
- `05-metric-spec.md`

Everything else in the bundle — mockup, teardown, recommendations, data model, ADR — is context for
a human reader and is never machine-validated. The delivery kit owns the handoff schema and
validates on ingest; this repo only has to emit a shape it accepts.

Technology selection and any platform-specific Architecture Decision Record belong to the delivery
repository after the requirements bundle is approved.

## Rules

- Stay tech-agnostic. Canonical SQL types only (`DECIMAL(18,2)`, `VARCHAR`), never dialect types.
  Metric formulas in business terms, never SQL or DAX.
- If the platform is already decided, that is the signal to start in the delivery kit instead.
- The mockup is where stakeholder churn belongs. Iterate freely there; freeze the spec afterwards.
