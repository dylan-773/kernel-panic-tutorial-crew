---
title: Traps and telegraphs
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[arm-halt]]", "[[arm-siphon]]", "[[opponent-ai]]"]
---

# Traps and telegraphs

> [!info] Source
> `duel-types.ts:DuelCell.trap`, `oppTurn.aim`; `duel-power.ts:settlePower`; `duel-actions.ts:settleBoard`.

Interference comes in two forms: a mine you walk into later, and a move you can see coming one beat early.

## Traps

```ts
trap: { by: Side; revealed: boolean; kind: "halt" | "siphon"; drain: number } | null
```

A trap is armed on an **unbuilt** junction on the victim's board by an [[attack]] cast in [[arm-halt]] or [[arm-siphon]] mode.

### Firing

`settlePower` fires a trap the first time signal reaches its node, and consumes it. Three properties follow:

1. **It never blocks.** The cascade keeps running straight past it exactly as it would have. You take the hit and keep the chain.
2. **It fires on first light only.** A repaired chain re-lighting the same node does not re-fire, because the trap was consumed and the node is already `built`.
3. **It is hidden until revealed.** [[scan]] is the only way to see one before you step on it, which is why the [[purge]] description says you cannot defuse what you cannot see.

### The two kinds

| Kind | Effect on the victim |
|---|---|
| `halt` | Forfeits a turn. Plus `drain` RAM off the next active turn (this is [[tripwire]]'s 3). |
| `siphon` | Moves `drain` RAM from the victim's next turn into the caster's. |

A halt forfeits the **current** turn if the victim is the acting side, otherwise it sets `loseNextTurn`. The cascade lands first, then the turn ends. The player-facing line is explicit about that order:

> HALT TRAP. Your signal hit an armed node. The cascade lands, then your turn is forfeit.

### Counters

- [[scan]] reveals. [[purge]] disarms what is revealed.
- [[ward]] prevents new traps landing in a radius.
- A BREAK-tier cascade (10+ nodes) cooks one armed trap on your board dead. See [[cascades-and-surge]].
- [[first-fault]] forgives the strain of the first trap each dive, never the tempo.

## Telegraphs

`oppTurn.aim` holds the move the machine has locked in but not yet made. The UI highlights it for one tick before it lands.

```ts
aim:
  | { kind: "rotate"; idx: number }
  | { kind: "cast"; prog: "attack" | "defend"; mode: OppMode; targets: number[] }
  | null
```

> [!warning] Every telegraph must be answerable
> A telegraphed action the player cannot respond to during the wind-up is not a telegraph, it is an animation. The one-beat tell exists so the player can spend the intervening decision on a counter: lock the junction it is aiming at, ward the area, or accept the hit and push.

## The honest Analyze tell

Before the dive, the diagnostic reports the customer's `dominant` mode, and it does not lie. `MODE_TELL` in `kit.ts` carries the six lines, for example:

> Diagnostic flags halt traps. One wrong claim and you lose a whole turn. Scan early.

`oppDominantUsed` tracks whether the machine has actually used it yet. The dominant mode is prioritized and guaranteed early, so the tell is information the player can act on rather than a statistical hint. See [[customers]].

## See also

- [[opponent-ai]] - how targets are chosen
- [[the-kit]] - the programs on both sides of this
