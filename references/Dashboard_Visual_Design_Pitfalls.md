# Dashboard Visual Design Pitfalls (Stephen Few)

### A craft-level checklist, complementary to the Dashboard Type × Decision Depth framework

The Type × Depth framework (`Analytics_Design_Framework.md` / `Analytics_Design_Framework_v1.0.md`) and its "Pitfalls to Watch For" section diagnose **strategic fit** — whether a dashboard is built for the right audience, at the right decision depth. The checklist below diagnoses a different axis entirely: **visual and perceptual craft** — whether an already-well-targeted dashboard is actually well-built, readable, and honest about what it shows.

A dashboard can be perfectly targeted (right type, right depth) and still fail this checklist — cluttered, imprecise, or visually misleading. Conversely, a beautifully-crafted dashboard can still be aimed at the wrong audience. Run both checks; don't let one substitute for the other.

**Overlap note:** Pitfall 2 below ("inadequate context") echoes the Snapshot → Insight-Driven distinction on the Decision Depth Ladder. When both checklists are in use, treat a hit on Pitfall 2 as reinforcing a Depth finding rather than a separate, new one.

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

- Score each pitfall against concrete, on-screen evidence (a specific tile, chart, or number) — "the settlement-fails bar chart uses 3D bars with a non-zero baseline" is checkable; "the charts look off" is not.
- Not every pitfall will apply to every dashboard — state "not observed" for a clean pass rather than manufacturing a finding.
- Pitfalls found here should translate into concrete craft fixes (e.g. "drop the 3D effect and start the axis at zero"), not a re-diagnosis of type or depth — that's a separate axis, covered elsewhere.
