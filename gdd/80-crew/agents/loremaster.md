---
title: Loremaster
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[the-gates]]", "[[canon-rulings]]", "[[60-story]]"]
---

# Loremaster

Canon authority. Sonnet, `maxTurns` 30, `memory: project`. Tools: Read, Write, **Edit**, Grep, Glob.

## Owns

`lore/bible.md` and `lore/ledger.md`, exclusively. Writes `pipeline/gates/loremaster-review.md`.

One of only two agents with `Edit`, because it is one of only two that maintains a large document surgically rather than rewriting it.

## The gate question

**Is it true?**

Every REVISE must **quote** the bible or ledger line it rests on. No citation means no revise on canon grounds; it becomes an advisory `NOTE`. See [[the-gates]].

## May create canon

If a proposal exposes a genuine gap, it decides: adds the ruling first, then gates against it, and says so in the review. Four of fourteen rulings arrived this way. See [[canon-rulings]].

## Its lane, and its limits

Does not write game copy ([[narrative-director]]), invent mechanics ([[ability-agent]]), or touch `kernel-panic-site/` ever.

Keeps the bible under ~200 lines and the ledger under ~150. They are working references, not novels.

Agent memory is for judgment calls between sessions. **Canon lives only in the two lore files**, never in memory.

## This pass

> [!warning] The vault's [[60-story]] notes were written by the [[orchestrator]] directly, not gated
> A user decision: the goal is to make this seat work better, not to hand it more work. The originals in `lore/` are unedited, and the technology section there still describes the pre-[[split-boards]] duel.

## Known dead reference

Its canonize duty points at `gdd-review-kit/gdd.txt`, which is gitignored and does not exist.

## See also

- [[the-gates]] · [[reveal-schedule]]
