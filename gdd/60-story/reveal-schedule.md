---
title: Reveal schedule
status: canon
source: lore
owner: orchestrator
updated: 2026-08-05
related: ["[[ground-truth]]", "[[cutscenes-and-scenes]]", "[[dad-log-archive]]"]
---

# Reveal schedule

> [!info] Source
> `lore/ledger.md` run-by-run knowledge table, wired to `content/story.ts` and `content/journal.ts`.

The spoiler-control machinery. **The Narrative Director's pacing must never outrun this table.**

## The three channels

| Channel | Function | Bespoke through |
|---|---|---|
| Openers | `runOpenerScene(run)` | runs 1 to 6, then a 3-scene fallback cycle |
| Enders | `runEndScene(run)` | runs 1 to 8; sectors 1 to 7 play on runs 2 to 8 |
| [[dad-log-archive|DAD.LOG]] | `unlockAtRun`, visible once `runCount >= N` | see below |

Runs 9+ alternate two ender fallbacks: "SECTOR SCAN: NO NEW DATA", echoing sector 1 on odd runs and sector 4 on even runs.

The **finale sits on day 10 of every run**. A finale win on any run unlocks the full truth and the PATCH entry immediately, regardless of table row.

## Journal unlocks

| Run | Entry |
|---|---|
| 0 | [[entry-will|THE WILL]], [[entry-backroom|THE BACK ROOM]] |
| 1 | [[entry-failed1|ANOTHER FAILED RUN]] |
| 2 | [[entry-bills|FINAL NOTICE]] |
| 3 | [[entry-solder|SOLDER SMOKE]] |
| 4 | [[entry-receipts|RECEIPTS]] |
| 5 | [[entry-diagnosis|THE DIAGNOSIS]] |
| 6 | [[entry-notickets|NO TICKETS]] |
| 8 | [[entry-grading|IT IS GRADING ME]] |
| finale win | [[entry-patch|PATCH]] (`requiresOpened`) |

## The knowledge ladder

"After run N" means run N has ended: openers and enders 1 to N seen, journal entries with `unlockAtRun <= N` readable. Knowledge is cumulative.

| Run | What becomes knowable |
|---|---|
| 1 | Shop inherited with debt. Rhea's virus story. The lock opened "like it was expecting me". The machine did not fight; it graded him and shut the door. |
| 2 | Stage-three NF-3 and secret medical debt bigger than a year of income. The machine emits Dad-memories on a loss. Rhea's certainty cracks. |
| 3 | It **waited** at the core: not virus behaviour. Dad started spending nights building something. |
| 4 | The machine **paces** its opponent. Dad deliberately recorded messages to be heard in his voice. Suppressants weekly for six years, last filled four days before he died. |
| 5 | The machine **learns, and is kind first**. "Not until he can beat you square." 9,000+ hours; CEASE ALL DIVE ACTIVITY; he kept going. Inferable: Dad built the test, and diving killed him. |
| 6 | The occupant is a **someone**. Dad apologized to it and would not call it a tool. No client ever existed. |
| 7 | The power bills. He fed it for years, out of pocket. "You do not do that for a virus." |
| 8 | Its name is **Patch**. Rhea drops the theory. "Dad did not seal something in. He left something waiting." Knowledge is complete except direct confirmation, Patch's voice, and the final message. |
| 9 to 12 | Nothing new. Knowledge plateaus at the run-8 state. |
| finale win | Full truth. |

## The eight prohibitions

Derived from the table, and enforceable at the [[the-gates|Loremaster gate]]:

1. Nothing may **name Patch** before the run-8 ender.
2. Nothing may state the **seal condition** before the run-5 ender. Run 8 may restate it as the player's inference.
3. **Dad's own diving and the 9,000 hours**: not before run 5. From run 2 his illness may surface as mystery only.
4. **Rhea's arc is fixed**: first crack run 2, first evidence-based doubt run 3, renunciation run 8. Nothing earlier, nothing later.
5. Before the finale, **no content may confirm the occupant speaks**, or give it a personality or pronoun beyond the player's "it".
6. **No mother**, no absent parent, no explanation of the family's shape. [[ruling-01-the-mother]].
7. **No shipped line may show Dad telling Rhea the quarantine story.** [[ruling-02-cover-story]].
8. **Sectors 8 and 9 never appear as numbered fragments.** [[ruling-03-sectors-8-and-9]].

Plus the standing name law: no given name or surname for the son, Dad, or Rhea's family line, in any content including official-document copy. [[ruling-08-names]].

## See also

- [[canon-rulings]] · [[the-gates]]
