# Kernel Panic tutorial crew

A goal oriented coding agent. It reads the game's design document, scans the
game's code, finds the mechanics the document describes that nothing teaches,
decides which to build and in what order, writes the code, and proves it by
turning the game's own coverage harness from red to green.

`gdd/` is the real Kernel Panic design vault, 216 wikilinked notes, frozen and
sha256 manifested. `game/` is the real teaching layer and the code it describes,
vendored verbatim, including the harness that judges the run.

## The game, in four lines

You inherited your father's repair shop and the machine in the back room he
never let you touch. A job ticket is a device with an intrusion in it. You link
in and fight the thing on a grid: rotate junctions, route a signal, light the
core before it lights yours.

Twenty seven tickets a run, three a day for nine days, then the finale on day 10.

## You are the ORCHESTRATOR

Run `/close-gaps`. You spawn the seats and carry their output between them.
**You never author teaching content yourself.** If you find yourself choosing an
`order` or writing a coachmark line, you have taken a seat's job.

| seat | produces |
|---|---|
| gdd-reader | the inventory of player facing features, with the symbols that hold them |
| gap-prioritizer | which gaps are real, what tier each is, and in what order they get built |
| teaching-author | the moment, tip, label or waiver, and the JSX mount |
| copy-critic | APPROVE / REVISE per item, each verdict quoting real source |

## Ground rules

1. **Seats write only to `runs/`.** The orchestrator applies to `game/`, and
   only through `tools/apply_patch.py`.
2. **Nobody reads `gaps/`.** It holds the answer key for the four planted gaps.
   `.claude/settings.json` denies the read, and `tools/verify_blind.py` audits
   the runtime's own transcript of what the run actually opened.
3. **Never hand edit `game/` to make a check pass.** The check is measuring the
   crew. Re-spawn the seat that owns the problem.
4. **Never fix a red check by loosening the check.** Especially not
   `verify_copy.py`, which is the only thing standing between this repo and the
   defect it was built to find.
5. **Every number in player facing copy names the symbol that holds it.** No
   symbol, no number. This is the rule the shipped game does not have.
6. **Prefer the cheapest rung of the ladder that works.** A label that carries a
   mechanic beats a coachmark that explains it. Declining to build is a result.
7. **A REVISE cites a quote that is a literal substring of the file it names.**
   A verdict that cannot substantiate itself is downgraded, not argued.
8. **No em dashes or en dashes**, anywhere, in anything. The game's copy law
   extends to this repo's prose so any line can be lifted without laundering.

## Checks, and what each one can answer

| tool | asks | can it be argued with |
|---|---|---|
| `verify_teaching.py` | is it well formed, and inside the harness's limits | no |
| `verify_copy.py` | is every number accountable to a real symbol | no |
| `teach-sim.ts` | is every mechanic covered or waived | no |
| `verify_blind.py` | did any seat read the answer key | no |
| `copy-critic` | is the sentence true | only with a quote |

Mechanical rules live in scripts, which cannot be talked out of a verdict.
Judgment goes to the critic, constrained by having to quote code it read.

The harness is the syntax gate too: `bun` parses the generated TypeScript on
import, so a malformed moment fails with a file and line before any check runs.
There is no separate typecheck and no `npm install`.
