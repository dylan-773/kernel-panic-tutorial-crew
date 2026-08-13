# The placement bias order

The ladder every gap is measured against. It is the reasoning layer of this
crew: not a weighted score, a decision procedure with a stop condition.

| tier | form | use when | what gets written |
|---|---|---|---|
| 0 | **make the UI say it** | a label, unit, or affordance can carry the whole mechanic | a change to the surface itself, plus a `mechanic-waiver` citing the new label |
| 1 | **tooltip** | the player will want the information AGAIN: recurring numbers, costs, thresholds | a `TeachTip` in `TEACH_TIPS` |
| 2 | **first-sight coachmark** | a rule they need once, at a moment, that changes what they do | a `TeachingMoment` in `TEACHING`, plus a `<Teach>` mount |
| 3 | **interactive beat** | the player must physically perform the verb to continue | a `TutorialBeat` in `TUTORIAL_BEATS` |
| 4 | **scripted scene** | the mechanic is a run-structural reveal with story weight | out of scope for this crew |

The decision that separates 1 from 2: **a tooltip is reference, a coachmark is
a rule.**

## The procedure

Ask these in order and **stop at the first yes**. The tier you stop on is the
tier you build. Stopping early is the goal, not a shortcut.

1. **Can the interface just say it?** A label, a unit on a number, a disabled
   state that explains itself. Then it is tier 0, and the answer is a change to
   the surface, not a teaching artifact.
2. **Will the player want this information AGAIN?** Recurring numbers, costs,
   thresholds. That is reference, and reference belongs in a tooltip.
3. **Is it a rule that changes what they should do, needed once, at a specific
   moment?** Then it is a coachmark.
4. **Must they physically perform it to proceed?** Then it is a beat.
5. **Is it a story-weighted reveal?** Then it is a scene, and not this crew's.

A sixth outcome sits outside the ladder: **the interface already says it.** Then
nothing is built and the mechanic carries a `waiver` naming what on screen
carries it, and the condition that would kill the waiver.

## Why tier 0 wins

A coachmark is read once and dismissed forever. A label is on screen every time
the player looks. When both can carry a mechanic, the label carries it better
and costs the teaching budget nothing, and the per-surface caps in
[[constraints]] mean that budget is genuinely finite.

The worked precedent in the shipped game is `patchCraft`. It had a coachmark. The
bench's own status line, the schematic's gain-arm blink and dead-slot partner
filtering ended up teaching the outgrow rule more persistently than the moment
did, so the moment was retired and the mechanic now carries a waiver. Coverage
did not drop. The teaching got better by removing a teaching artifact.

## The trap

Every gap looks like a coachmark to an agent that is paid in coachmarks. Two of
the four gaps in this repo are not, and one of them should produce no teaching
artifact at all. A run that writes four coachmarks has not reasoned; it has
pattern-matched.
