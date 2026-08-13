---
title: Vault conventions
status: canon
source: user
owner: orchestrator
updated: 2026-08-05
related: ["[[home]]", "[[table-of-contents]]"]
---

# Vault conventions

The rules that keep this vault honest. A note that breaks them is a bug.

## Frontmatter is mandatory

```yaml
---
title: Cascades and surge
status: canon        # canon | derived | draft | unwritten
source: code         # code | lore | rulings | measured | user | none
owner: orchestrator  # orchestrator | loremaster | tutorial-agent | ux-agent | user
updated: 2026-08-05
related: ["[[split-boards]]", "[[ram]]"]
---
```

### status

| value | meaning |
|---|---|
| `canon` | Matches shipped code or settled canon. |
| `derived` | Read out of the code, never previously documented. |
| `draft` | A proposal awaiting review. |
| `unwritten` | No decision exists yet. Holds open questions only. |

### source

Where the note's authority comes from: `code` (a file in `kernel-panic-site/`), `lore` (the migrated setting bible or story ledger), `rulings` (the UI spec), `measured` (sim output), `user` (a direct decision), `none`.

Notes with `source: code` cite the file and symbol they were read from, so any claim can be re-verified against the build. Write `kit.ts:cascadeRam`, not "the cascade function".

## The load-bearing rule: never retype a number

If a note states a constant, it names the symbol that holds it. `PLACE_COST = 4` (`patch-cells.ts`), not "placing costs 4 RAM". This is what makes drift detectable: when the code changes, the note is checkable rather than merely wrong.

The vault exists because that discipline was missing. Three separate documents asserted territory and claiming for weeks after the engine deleted them.

## Naming

- Filenames are **kebab-case**: `cascades-and-surge.md`.
- `title` in frontmatter is sentence case: `Cascades and surge`.
- One idea per note. If a note needs two H1-worthy claims, it is two notes.
- Index notes for a folder take the folder's name: `20-mechanics.md`.

## Links

- Wikilinks `[[like-this]]` for everything inside the vault. Never markdown links.
- Link liberally. A `[[link]]` to a note that does not exist yet is a valid marker of work to do, not an error.
- `related:` in frontmatter carries the two or three strongest connections. The body carries the rest.

## No em or en dashes, anywhere

CLAUDE.md iron rule 6 forbids them in game copy. This vault extends that to all prose so that any line can be lifted into the game without laundering. Use a spaced hyphen, a comma, or two sentences.

## Callouts

| Callout | Use for |
|---|---|
| `> [!info] Source` | Where a note was read from |
| `> [!warning]` | A trap: something that looks like a bug and is not, or a stale claim elsewhere |
| `> [!question] UNWRITTEN` | The banner on every `status: unwritten` note |
| `> [!danger] REVISED IN PROTOTYPE` | A design change with the evidence that forced it, carried over from the v2 GDD |

## Attachments

Images live at `_attachments/`, which symlinks `art` to `pipeline/art/done/`. Embed by **bare filename**, `![[cust-card-juno-portrait.png]]`, and let shortest-path resolution find it through the symlink. Do not copy binaries into the vault; the symlink keeps one copy on disk and lets the art pipeline stay where the crew writes to it.

## What does not belong here

- Dated process logs. Cycle retrospectives, gate verdicts and loop history stay in `pipeline/` and `tutorial/ledger.md`. Extract the standing lesson, leave the diary.
- Anything under `kernel-panic-site/`. The code is the code.
- Anything that duplicates a number rather than citing it.
