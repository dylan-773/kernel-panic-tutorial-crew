---
title: SPLICE REFUND
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[patch-pieces]]", "[[the-pouch]]", "[[augments]]"]
---

# SPLICE REFUND

**Boost** · `patchRefund` · requires a piece in the [[the-pouch|pouch]]

> Placing a patch piece refunds its full RAM cost the instant it lands. The pouch still spends the piece itself.

`PLACE_COST` is 4 RAM, so this is the largest single-cast RAM swing in the catalog.

Gated by `{ kind: "pouch" }`, the only non-augment requirement in the system: the pouch must hold at least one piece **at roll time**. So the draft will not offer it to a player with an empty pouch, even though they might fill it later.
