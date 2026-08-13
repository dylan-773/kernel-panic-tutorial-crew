---
title: The pipeline
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-dev-crew]]", "[[the-gates]]", "[[the-plays]]"]
---

# The pipeline

`pipeline/` is the crew's shared workspace. **It is per-cycle scratch and is cleared between cycles.**

| Path | Holds |
|---|---|
| `BRIEF.md` | what this cycle is for. Every agent reads it first |
| `proposals/<agent>.json` | one file per agent, its only output |
| `gates/loremaster-review.md` | canon verdicts |
| `gates/tutorial-review.md` | teaching verdicts |
| `validation/report.md` | fresh sim numbers |
| `art/orders/<id>.json` then `art/done/<id>.png` | art work orders |
| `copy/orders/<id>.json` | copy orders, filled in place |
| `tools/` | `dither.py`, `pxpost.py`, `colourise.py`, `lint-proposal.sh` |

## Why it is not in this vault

It is process residue. Dated verdicts, per-cycle proposals and cleared briefs are not knowledge; they are the exhaust of producing knowledge.

What is durable **was** lifted out: the fourteen [[canon-rulings]], the [[standing-lessons]], and the waiver rationales in [[teaching-waivers]].

## The one durable exception

`ui-demos/manifest.json` is **never cleared**. It tracks every UI demo and its status (`awaiting`, `approved`, `complete`), which is what makes review-before-integration possible across cycles. See [[the-plays]].

## The lint hook

A `PostToolUse` hook on `Write` runs `pipeline/tools/lint-proposal.sh` against anything matching `pipeline/proposals/*.json` or `pipeline/copy/orders/*.json`.

So a malformed proposal is caught at write time, by the harness, rather than at integration time by a person. That is the same principle as `typecheck` being the schema enforcer: the machine checks shape, the human checks judgment.

## Integration

By hand, by the [[orchestrator]], always. Then [[verification-gate|the four harnesses]].

## See also

- [[the-gates]] · [[the-plays]]
