---
title: Teaching waivers
status: canon
source: code
owner: tutorial-agent
updated: 2026-08-05
related: ["[[mechanic-coverage]]", "[[placement-bias-order]]"]
---

# Teaching waivers

A waiver is a **written decision not to teach something**, with a reason. **14 of the 39** inventory entries carry one, against 25 taught (`teach-sim.ts`, 2026-08-05).

A waiver is not a gap. A gap is an inventory entry with neither a moment nor a waiver, and it fails the build.

## The shape

```ts
{ id, label, firstContact, waiver: "<the reason>", waiverPremise?: "..." }
```

Several also carry an `expiresIf` clause in the ledger: the condition under which the waiver stops being valid.

## The canonical example

**`reach2`**:

> the legal set is drawn as glowing junctions, the affordance is the teaching

This is [[placement-bias-order|tier 0]] as a waiver. Reach is not explained because the board already shows you exactly which junctions are legal. Adding a coachmark would explain something the player can see.

## Others

`turnCap` · `credits` · `jobBoard` · `programTiers` · `saveSlots` · `runReset` · `finaleGate` · `finaleOppOpens` · `patchDrop` · `gridlockChip` · `patchCraft`

`patchCraft` is the interesting one: it was **taught**, then the interface improved, then the coachmark was retired and the mechanic became waived. See [[coachmarks]].

## Premise-backed waivers

Two are blanket waivers backed by a machine-checkable premise:

| Waiver | Premise |
|---|---|
| `augmentEffects` | every augment still ships its own `desc` |
| `modeEffects` | every mode still ships its own `desc` |

The argument is: the effects do not need teaching **because** each one is written on its own card, generated from `kit.ts`. See [[manual-txt]].

> [!info] This is the only self-invalidating waiver design in the project
> `teach-sim.ts` re-checks the premise on every build. Remove a desc and the premise fails, the waiver expires, and the build breaks. The waiver cannot outlive the reason for it.
>
> Every other waiver is prose, and prose does not notice when it stops being true.

## The stale one

`gridlockChip` claims gridlock wins chip 6 strain. **There is no gridlock outcome.** See [[mechanic-coverage]].

## See also

- [[mechanic-coverage]] · [[teaching-system]]
