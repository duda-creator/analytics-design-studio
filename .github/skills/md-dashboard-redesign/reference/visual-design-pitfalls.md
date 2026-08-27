# Dashboard Visual Design Pitfalls (Stephen Few)

### A craft-level checklist, complementary to the redesign type references in this folder

The type-specific design references in this folder (`executive-*-design.md`, `operational-insight-driven-design.md`) define **content and structure** — what a redesigned dashboard of a given type should say and how it should be organized (What/So What/Now What, inverted pyramid, drill paths, etc.). The checklist below is a different axis: **visual and perceptual craft** — whether the resulting charts and layout are actually well-built, readable, and honest about what they show.

Use it in Stage 1 (teardown) to catalog concrete craft issues in the *current* dashboard, and in Stage 2 (recommendations) to ground craft-level fixes alongside the content-level What/So-What/Now-What changes. A redesign can nail the content model and still fail this checklist — cluttered charts, misleading axes, decorative color — so check both.

**Overlap note:** Pitfall 2 ("inadequate context") is largely already handled by the What/So-What/Now-What model itself — a proper "So What" supplies the comparison this pitfall is checking for. Don't double-count it as a separate finding if Stage 2 already adds that context.

---

## The 13 Pitfalls

1. **Exceeding the boundaries of a single screen** — A dashboard should communicate its core information without requiring scrolling or jumping between screens.
2. **Supplying inadequate context for the data** — A number without a target, comparison, trend, benchmark, etc. often can't tell the user whether it matters.
3. **Displaying excessive detail or precision** — Don't show more granularity or decimal precision than the decision requires.
4. **Expressing measures indirectly** — Don't make people decode a value through an unnecessary visual metaphor or elaborate graphic.
5. **Choosing inappropriate display media** — Choose the visual form that best represents the data and task; don't default to fashionable chart types.
6. **Introducing meaningless variety** — Different visual treatments should communicate different meanings; variety for decoration creates noise.
7. **Using poorly designed display media** — Even an appropriate chart type can be badly constructed or difficult to read.
8. **Encoding quantitative data inaccurately** — The visual encoding must represent the numbers faithfully — e.g. misleading axes or proportions.
9. **Arranging information poorly** — Layout and spatial hierarchy should guide attention and make relationships apparent.
10. **Highlighting important information ineffectively or not at all** — The things requiring attention should visually stand out from routine information.
11. **Cluttering the display with visual effects** — Remove decorative elements that compete with the information.
12. **Misusing or over-using color** — Color should have a purpose and consistent meaning, rather than being decoration.
13. **Designing an unattractive visual display** — The overall design should be clean, coherent and aesthetically credible — although attractiveness is subordinate to information effectiveness.

---

## How to apply it

- Score each pitfall against concrete, on-screen evidence from the screenshots (a specific tile, chart, or number) — "the trend chart truncates its y-axis at 80%" is checkable; "the charts look off" is not.
- Not every pitfall will apply to every dashboard — state "not observed" for a clean pass rather than manufacturing a finding.
- Each pitfall found in Stage 1 should map to a concrete craft fix proposed in Stage 2 (e.g. "drop the 3D pie, use a sorted bar chart instead"), separate from the content-level What/So-What/Now-What changes.
