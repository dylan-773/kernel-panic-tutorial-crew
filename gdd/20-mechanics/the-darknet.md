---
title: The darknet
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[patch-pieces]]", "[[darknet-rate]]", "[[ruling-09-darknet]]"]
---

# The darknet

> [!info] Source
> `run-reducer.ts:buyDarkPatch`, `darkPullPrice`; `patch-cells.ts:darkPatchCost`. Window: [[darknet-lnk]].

The gray market. One blind [[patch-pieces|patch piece]], priced by day.

```
darkPatchCost(day) = 25 + 5 * (day - 1)
darkPullPrice(run) = darkPatchCost(day) * (darkDiscount ? 0.85 : 1)
```

Night phase only.

## Blind is the product

You pay before you see the shape, and the roll uses the same weights as a job drop (I 40 / L 45 / T 12 / X 3). You are buying a lottery ticket on board material.

That is what makes it different from every other purchase: patches and bays are known quantities, the pull is not. It is the cheapest entry price and the only one that can disappoint.

[[darknet-rate]] discounts it by 15% and explicitly does **not** make the roll visible.

## The fiction

[[ruling-09-darknet]] settled that the dealer is **permanently anonymous**. There is no character, no relationship, no reveal. It stays a CLI over three relay hops and a price.

That constraint is why the window is the only one in KP/OS with `notched: true` chrome and a dial-handshake sequence: the interface carries the whole characterization, because canon forbids a person.

## See also

- [[darknet-lnk]] - the window
- [[economy]] · [[the-night-shop]]
