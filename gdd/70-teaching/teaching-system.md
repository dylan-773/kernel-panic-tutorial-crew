---
title: Teaching system
status: canon
source: code
owner: tutorial-agent
updated: 2026-08-05
related: ["[[placement-bias-order]]", "[[coachmarks]]", "[[mechanic-coverage]]"]
---

# Teaching system

> [!info] Source
> `content/teaching.ts` declares; `components/game/teach.tsx` renders; `dev/teach-sim.ts` enforces.

## Two governing rules

1. **Every mechanic resolves to a moment or a written waiver.** Enforced by `teach-sim.ts`, which exits 1 and names the gap.
2. **Teaching happens at first contact, once per save slot ever.** The opening dive teaches the four verbs and nothing else.

## The declaration

```ts
interface TeachingMoment {
  id; teaches: string[];      // MECHANIC_INVENTORY ids
  surface: TeachSurface;      // tutorial|duel|day|analyze|loadout|solder|
                              // result|upgrade|finalePre|runEnd|desktop
  when: TeachWhen;            // firstSight|overPar|holdingCells|cascadeBanked|
                              // draftOffered|craftReady|swapOffered
  anchor;                     // -> CSS class kp-teach-<anchor>
  order: number;              // LOWER shows first
  notBeforeDay: number;
  title; lines: string[];
  copyOrder?;                 // Narrative Director copy order id
}
```

## Exactly one callout at a time

> [!warning] The most common false bug report in the project
> `TeachProvider` collects every eligible moment across all mounted `<Teach>` elements and picks **the single winner with the lowest `order`**. Only one callout is ever on screen.
>
> A moment that "never appears" is almost always **losing the tie to a lower order on the same screen**, not broken.

`teach-sim.ts` requires `order` to be **unique** across the whole set, so precedence is total and there are no ties to resolve arbitrarily.

## Eligibility

```
!taught.includes(id)  &&  day >= m.notBeforeDay  &&  teachFires(m, signals)
```

`notBeforeDay` gates day 0, so **the opening dive takes no coachmarks by construction**. Every shipped coachmark carries `notBeforeDay: 1`.

## Anchoring is DOM-based

`<Teach id signals?>` is placed **inline next to the thing it explains**, rendering `.kp-teach.kp-teach-<anchor>`. Nothing is measured or positioned by coordinates, so a callout cannot drift from its subject when a layout changes.

## Taught is meta, not run

GOT IT dispatches `{type: "taught", id}` into `MetaState.taught`. **A mechanic explained in attempt 3 stays explained in attempt 4.** Per save slot, so a fresh slot is a fresh player.

## The limits teach-sim enforces

| Limit | Value |
|---|---|
| `MAX_FIRST_SIGHT_PER_SURFACE` | 2 |
| `MAX_MOMENTS_PER_SURFACE` | 4 |
| `MAX_COACH_LINE` | 160 chars |
| `MAX_BEAT_LINE` | 260 chars |

Plus: no duplicate ids, unique `order`, all four `CORE_VERBS` taught in the opening dive, the tutorial ladder never silent in a reachable state, and every moment's surface reached by an actual run walk.

## See also

- [[placement-bias-order]] · [[teaching-waivers]]
