---
title: Placement bias order
status: canon
source: lore
owner: tutorial-agent
updated: 2026-08-05
related: ["[[teaching-system]]", "[[coachmarks]]", "[[hud-and-ui-design]]"]
---

# Placement bias order

The most reusable thing the teaching ledger contains. **Five tiers, and you take the lowest one that works.**

| Tier | Method | Owner |
|---|---|---|
| **0** | **Make the UI say it** | [[ux-agent]] |
| 1 | A persistent tip or hover explainer | [[tutorial-agent]] |
| 2 | A one-time coachmark | [[tutorial-agent]] |
| 3 | Reference in [[manual-txt]] | [[tutorial-agent]] |
| 4 | A scripted scene or beat | [[narrative-director]] |

## Tier 0 always wins

> [!info] Prefer a clearer interface over a coachmark
> This is CLAUDE.md iron rule 3's closing clause, and it is the reason the teaching system is small. A rule the interface expresses does not need explaining, and an explanation is a tax paid on every new player forever.

[[solder-bay]] is the worked example. Illegal weld partners are rendered **physically dead** rather than accepting a drag and rejecting it, so the outgrow rule is visible before the attempt. The `patch-craft` coachmark was **retired on 2026-07-29** because the interface had made it redundant.

That is the intended lifecycle: a coachmark is a debt against the interface, and paying it off deletes the coachmark.

## Tip or coachmark

> **A tip is reference you want again. A coachmark is a rule you need once.**

[[route-cost-and-par|Par]] gets both: a coachmark when you first exceed it, and a persistent tip because you will want the number again. See [[teaching-tips]].

## Any new visual footprint is a ui-spec

If a teaching decision needs pixels, the tutorial agent does not design them. It files a `ui-spec` to the [[ux-agent]]. Ten are logged, including `strain-chip-breakdown`, `night-shop-credit-adjacency` and `touch-safe-tooltips`.

That handoff is what keeps teaching from quietly becoming a second, worse design system layered over the first.

## See also

- [[teaching-system]] · [[hud-and-ui-design]]
