# Schemas

Four files carry the run. Each seat writes one, and each is the next seat's
input. Everything lands under `runs/<RUN>/`.

## 1. `features.json` (gdd-reader)

What the GDD says the game has. `tools/gdd_extract.py` produces the structural
candidates; the seat decides which are player-facing and writes the
`mustUnderstand` line, which is the only field no regex can produce.

```json
{
  "schema": "kp-features/1", "run": "<RUN>", "agent": "gdd-reader",
  "features": [
    {
      "id": "cascade",
      "name": "Cascades and surge",
      "note": "20-mechanics/cascades-and-surge.md",
      "symbols": ["kit.ts:cascadeRam", "duel-actions.ts:settleBoard"],
      "playerFacing": true,
      "mustUnderstand": "One sentence. What the player has to know to play well.",
      "evidence": "a verbatim quote from the note that supports it"
    }
  ]
}
```

- `id` matches a `MECHANIC_INVENTORY` id when one exists. When the GDD
  describes something the inventory has no row for, invent the camelCase id and
  say so; that is the silent gap class.
- `playerFacing: false` is a real and useful answer. Generation constraints,
  engine internals and difficulty dials the player never reads are not features
  to teach. Say why in `mustUnderstand`.
- `evidence` must be a literal substring of the named note.

## 2. `gaps.json` (gap-prioritizer)

```json
{
  "schema": "kp-gaps/1", "run": "<RUN>", "agent": "gap-prioritizer",
  "gaps": [
    {
      "id": "cascade",
      "mechanics": ["cascade"],
      "state": "uncovered",
      "red": true,
      "tier": 2,
      "ladderStop": "REQUIRED: which question of the procedure stopped, and why the tiers above it cannot carry this",
      "action": "coachmark",
      "surface": "duel",
      "rank": 1,
      "because": [
        { "signal": "harness-red", "value": "teach-sim names it", "note": "..." },
        { "signal": "first-contact-day", "value": "duel, day 1", "note": "..." }
      ]
    }
  ]
}
```

- `state`: `uncovered` (in the inventory, nothing teaches it, harness is red),
  `uninventoried` (the GDD describes it and the inventory has no row, harness is
  silent), or `miscovered` (something teaches it and the string is wrong).
- `action`: `coachmark` | `tip` | `label` | `waiver` | `none`.
- `rank` is total across gaps, 1 first.
- `because` must cite at least one of the five signals: `first-contact-day`,
  `resource-cost`, `ladder-tier`, `surface-budget`, `harness-red`. A ranking
  with no cited signal is not a ranking, it is a preference.

## 3. `generated/<gap>.json` (teaching-author)

```json
{
  "schema": "kp-generated/1", "gap": "cascade", "action": "coachmark",
  "moment": {
    "id": "cascade-bank", "teaches": ["cascade"], "surface": "duel",
    "when": "cascadeBanked", "anchor": "screen", "order": 50,
    "notBeforeDay": 1, "title": "CASCADE",
    "lines": ["first line", "optional second line"]
  },
  "mount": {
    "file": "src/components/game/duel.tsx",
    "anchorLine": "verbatim existing line to insert after",
    "jsx": "          <Teach id=\"cascade-bank\" signals={{ cascadeBanked: sawCascade }} />"
  },
  "claims": [
    {
      "text": "three or more nodes",
      "symbol": "kit.ts:cascadeRam",
      "resolves": "returns 0 when lit < 3, so three is the first paying count"
    }
  ]
}
```

Other actions carry a different payload and no `moment`:

- `tip` carries `"tip": { id, teaches, control, text }`.
- `waiver` carries `"waiver": { id, text, expiresIf }`.
- `label` carries `"label": { file, before, after, why }` plus a `waiver`, since
  a tier 0 fix retires the need for teaching and the inventory row has to say so.
- `none` carries only `"why"`.

**`claims` is required on every action that produces player-visible words.**
Every number, threshold, count and cost stated in the copy needs a claim naming
the code symbol that holds it. `tools/verify_copy.py` fails a run where copy
states a number no claim covers. This is the check the shipped game does not
have, and the reason its cascade coachmark has been wrong since it was written.

## 4. `critic/<gap>.json` (copy-critic)

```json
{
  "schema": "kp-verdict/1", "gap": "cascade", "verdict": "APPROVE",
  "claims": [
    {
      "text": "three or more nodes", "symbol": "kit.ts:cascadeRam",
      "verdict": "TRUE",
      "quote": "  if (lit < 3) return 0;"
    }
  ],
  "objection": null,
  "required": null
}
```

- `verdict` is `APPROVE` or `REVISE`. A `REVISE` needs a non-null `objection`
  and `required`.
- **`quote` must be a literal substring of the file named in `symbol`.**
  `verify_copy.py --kind verdict` checks it. A verdict that cannot substantiate
  itself is downgraded, not argued.
