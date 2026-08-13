---
title: FIRST FAULT
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[neural-strain]]", "[[traps-and-telegraphs]]", "[[augments]]"]
---

# FIRST FAULT

**Boost** · `firstFault`

> The first trap that fires on you each dive bills zero Neural Strain. Every trap after that costs full.

In `finishDuel`:

```
chip += 4 * max(0, trapsFired - (firstFault ? 1 : 0))
```

> [!warning] It forgives the strain, never the tempo
> A halt trap still forfeits your turn and a siphon still drains your RAM. This only touches the bill at the end. The distinction is deliberate and is stated in the source comment.

Worth 4 strain per dive, which across a nine-day run is worth more than three night patches.
