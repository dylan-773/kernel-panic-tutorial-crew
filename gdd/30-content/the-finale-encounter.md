---
title: The finale encounter
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[day-10-the-finale]]", "[[the-machine]]", "[[patch]]"]
---

# The finale encounter

The game's only boss, and it is deliberately not a boss.

## What makes it different

| | |
|---|---|
| New mechanic | **none** |
| Phases | **none** |
| Health bar | **none** |
| Special rules | **one**: `oppOpens` |

It is an ordinary duel at maximum difficulty: 15x11, horizon 3, focus 1.00, greed 1.00, the full six-mode vocabulary at width 3, and the machine moving first.

> [!info] Mechanically it is an ordinary duel. That is the point.
> The final exam is the thing the player has been practising for nine days. A phase-change boss would say the last nine days were a tutorial for something else. This says they were the thing itself.

Config in [[day-10-the-finale]].

## `oppOpens`

The only dive where the machine takes the first turn. The fiction is exact: **it was already inside**.

It is also why the kit-less proxy posts a 0% finale win rate by construction. A player with no configs, no wards, no locks and no purges cannot answer an opponent that opens with the full vocabulary.

## The identity tag

The opponent reads **INTRUSION** throughout, including on the winning dive. The name [[patch]] is revealed in the scene that follows, never in the dive's own UI. See [[ruling-11-opponent-identity-tag]].

So on a first successful run the player beats a thing labelled INTRUSION, and only afterwards learns they were playing against the thing their father built for them, which had never once let them win.

## The seal

Opens only on **"A FAIR WIN, NO ASSISTS"**. The padlock "does not open so much as let go".

## On a win

`machineOpened` is set permanently on `MetaState`. `finaleWinScene()` plays. [[entry-patch|PATCH.SYS]] becomes readable. The full truth lands regardless of `runCount`. See [[reveal-schedule]].

## On a loss

Nothing special. The run ends, `runCount` increments, and the next reveal is waiting. See [[death-and-run-end]].

## See also

- [[the-machine]] · [[backroom-lck]] · [[cutscenes-and-scenes]]
