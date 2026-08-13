---
title: Turn structure
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[ram]]", "[[the-duel]]", "[[opponent-ai]]"]
---

# Turn structure

> [!info] Source
> `duel-commands.ts` (untracked, new), `duel-reducer.ts`, `duel-actions.ts:beginTurnEconomy`.

One round is one player turn then one opponent turn. `round` is 1-based.

## Turn economy

`beginTurnEconomy` at the start of a side's turn:

```
ram = ramPerTurn + carry - drainNext
drainNext = 0
```

`drainNext` is settled **first**, then zeroed, so a turn burned by a halt trap does not also owe the drain on the turn after. Negative `drainNext` is a gain, which is how [[cascades-and-surge|cascade RAM]] arrives.

`carryCap = 2` on both sides, flat. The v2 GDD listed a CARRY CACHE augment raising it to 4; that augment is not in the shipped `AUGMENTS` catalog. See [[augments]].

## What a turn can contain

- Any number of [[rotation|rotations]], 1 RAM each, each settling the board immediately.
- One [[patch-pieces|patch placement]], 4 RAM, once per turn (`placedThisTurn`).
- Each of the three programs once (`used: Record<Program, boolean>`), 1 RAM each.

Programs are once **per program**, not once total. A full turn can SCAN, ATTACK and DEFEND.

## The command layer

`duel-commands.ts` is now the **only** gate a move can be refused at. Previously that logic was duplicated across the reducer, `executeCast`, the kitted bot and `botPlayTurn`, which is exactly the shape defects hide in.

```ts
type DuelCommand =
  | { kind: "rotate"; idx: number }
  | { kind: "place"; idx: number; pouchIdx: number; mask: number }
  | { kind: "cast"; prog: Program; mode: OppMode | null; targets: number[] };
```

> [!info] Commands are records, not closures
> Because undo replays them. Pulling one entry out of a turn means re-running the rest from the turn's starting snapshot, which only works if a move is data.

`checkCommand` returns a `DenyReason`, and the reducer maps reason to prose via `denyCopy`:

`notYourTurn` · `noRam` · `welded` · `clamped` · `isGoal` · `outOfReach` · `pouchEmpty` · `alreadyPlaced` · `staleClick` · `notSlag` · `programOffline` · `badTargetCount` · `illegalTarget`

## The one undo

`UndoPoint { before, label, sprung }`, one per turn, tracked by `undoSpent`.

- A **rotation** or a **placement** arms it.
- A **cast clears it** rather than arming one. Casts are not reversible.
- It is re-armed at the start of the next turn.

### Undo does not un-spring a trap

`sprung` records traps the move fired, and they are **re-applied** after the state restore.

> [!warning] This is the anti-minesweeper rule
> Without it: twist into a hidden node, watch the trap fire, take the move back, and now you know where the mine is for free. You get your junction back, never your mine back.

A HALT is not in `sprung` in practice, because it forfeits the turn outright and there is no turn left to undo in. The rule takes care of itself.

### Why only one

Touch-move is the texture of the game. The undo is a fix for a misread, never a tool for exploring the board.

## `opts.arm === false`

The AI and both sims run with undo snapshotting disabled, so roughly 4000 simulated duels pay no clone cost. See [[simulation-harnesses]].

## Reducer actions

`rotate | place | cast | endTurn | oppStep | view | fxDrain | undo`

No action carries a board tag. `targetBoardOf` derives it from the verb. See [[split-boards]].

## The opponent's turn

Advanced one visible step at a time by `oppStep`, so the player watches it move rather than seeing a diff. The [[traps-and-telegraphs|telegraph]] beat highlights the aim for one tick before it lands.

## See also

- [[opponent-ai]] - what the machine does with its turn
- [[ram]] - the resource all of this spends
