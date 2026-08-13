# The hard constraints

Everything here is enforced by `game/src/game/dev/teach-sim.ts`, which is the
shipped game's own harness, vendored unmodified. Breaking any of it is a red
build, not a style note. The symbols are the authority; the numbers below are
read out of them.

## Coverage

Every id in `MECHANIC_INVENTORY` is either covered or waived, never both.

- **Covered** means the id appears in the `teaches` array of a `TeachingMoment`,
  a `TutorialBeat`, or a `TeachTip`. See `teaching.ts:taughtMechanics`.
- **Waived** means the `MechanicEntry` carries a `waiver` string of at least 20
  characters, claiming the interface carries it unaided.
- Both at once fails: *"a waiver is a claim that no moment is needed."*
- A blanket waiver over a whole content type needs a `waiverPremise`, and the
  only two the harness knows how to re-verify are `augmentDescs` and
  `modeDescs`. A new premise is a harness change, not a string to invent.
- Any mechanic id referenced by a moment, beat or tip that is not in the
  inventory also fails.

## Moments

- `id` unique. **`order` unique across every moment**, because it is the total
  precedence used when two are eligible at once.
- `teaches` non-empty, and every id in it exists in the inventory.
- `notBeforeDay` within `0..FINAL_DAY` (`content/arc.ts`). Day 0 is the opening
  dive, which takes no coachmarks by construction.
- `title` non-empty and **ALL CAPS**. System text always is.
- **1 to 2 lines**, each **at most 160 characters** (`MAX_COACH_LINE`).
- `when` must be one of the seven strings in `TeachWhen`: `firstSight`,
  `overPar`, `holdingCells`, `cascadeBanked`, `draftOffered`, `craftReady`,
  `swapOffered`. A new trigger is a reducer change. Do not invent one.
- `surface` must be a `TeachSurface` the run actually reaches, or one of the
  window surfaces (`loadout`, `solder`, `desktop`, `tutorial`) which the run
  walk cannot visit and which are reachable by construction.
- `anchor` drives the position class `kp-teach-<anchor>`. Only these have rules
  in `game/src/styles.css`: `readout`, `rows`, `draft`, `par`, `screen`,
  `patch`, `grid`, `craft`. A new anchor needs CSS.

## Per-surface budget

- At most **2 unconditional (`firstSight`) callouts per surface**
  (`MAX_FIRST_SIGHT_PER_SURFACE`).
- At most **4 moments per surface** total (`MAX_MOMENTS_PER_SURFACE`).

Current headroom, from the shipped registry: `duel` 3 moments and 0 firstSight;
`result` 3 and 1; `upgrade` 2 and **2, already at the firstSight cap**;
`analyze` 1 and 1. A gap landing on `upgrade` cannot take another unconditional
moment, and that constrains what can be built there regardless of what the
mechanic deserves.

## Tips

- `id` unique, `teaches` non-empty, `control` non-empty.
- `text` **1 to 130 characters** (`MAX_TIP_LEN`).

## Beats

- `teaches` non-empty, line at most 260 characters (`MAX_BEAT_LINE`).
- All four `CORE_VERBS` (`rotate`, `scan`, `defend`, `attack`) taught before the
  opening dive ends.
- The ladder is ordered and the first passing `test` wins. It may never go
  silent in a reachable state; the harness sweeps the whole ladder to prove it.

## The stylesheet is frozen

`game/src/styles.css` is not mutable. Generated JSX may only use class names
that already have a rule in it, because a class nobody can style is an element
that renders bare. `verify_teaching.py` checks every `className` in a generated
mount or label.

Existing dive-dock classes worth knowing: `dv-ram-num`, `dv-ram-banked`,
`dv-ram-pips`, `dv-ram-label`, `dv-key-meta`, `dv-datarow`. Callout anchors are
listed above.

## Copy law

**No em or en dashes in anything a player reads. Ever.** The harness fails the
build on one. This applies to the notes in this repo too, so any line can be
lifted into game copy without laundering.

## What the harness cannot see

`teach-sim.ts` proves a mechanic is **covered**, never that the covering string
is **true**. It cannot read English. A coachmark that confidently states the
wrong number passes every check above.

That gap is not hypothetical. The shipped `cascade-bank` coachmark says a
cascade banks RAM at "Four or more nodes"; `kit.ts:cascadeRam` returns 0 only
when `lit < 3`, so it pays from three. The harness has been green over that
sentence for its entire life.

Closing that gap is what `tools/verify_copy.py` and the `copy-critic` seat are
for, and it is why every generated line has to name the symbol that holds each
number it states.
