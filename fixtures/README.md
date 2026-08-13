# Fixtures

A checker nobody has tried to fool is a claim, not a check. These are the cases
`tools/run_fixtures.py` drives, each asserting an exit code and the text of the
message. 21 cases, run with:

```
python3 tools/run_fixtures.py
python3 tools/run_fixtures.py -v      # show the output of each case
```

`scan.json` is a frozen snapshot of `bun tools/code_scan.ts --json` taken while
the four gaps were open. Fixtures check against it rather than the live slice so
their results do not move when a run lands.

## `teaching/` - shape and the harness invariants

`clean.json` is the base case and every other file is a one field mutation of
it. **`clean.json` must stay silent.** A linter that flags everything proves
nothing, and half of these cases exist to pin that.

| case | what it breaks |
|---|---|
| `clean.json` | nothing. Must pass |
| `dash.json` | an em dash in a player facing line |
| `order-collision.json` | reuses `order: 40`, which `par-budget` holds |
| `three-lines.json` | three lines where the cap is two |
| `long-line.json` | a line past 160 characters |
| `lower-title.json` | title is not ALL CAPS |
| `bad-when.json` | a `when` trigger that does not exist in `TeachWhen` |
| `bad-anchor.json` | an anchor with no `kp-teach-<anchor>` rule in styles.css |
| `unknown-mechanic.json` | `teaches` an id that is not in `MECHANIC_INVENTORY` |
| `no-mount.json` | a moment with no `<Teach>` mount, so it renders nowhere |
| `fake-anchor-line.json` | a mount whose anchor line is not in the target file |
| `no-claims.json` | player facing copy with no `claims` array |
| `surface-cap.json` | a third unconditional callout on `upgrade`, already at 2 of 2 |

## `copy/` - is the copy accountable to the code

| case | expected |
|---|---|
| `clean.json` | passes, and prints `cascadeRam` with its real body |
| `uncited-number.json` | fails: the copy says `4 RAM` and no claim covers it |
| `bad-symbol.json` | fails: cites `kit.ts:cascadePayout`, which does not exist |
| `shipped-cascade.json` | **passes, on purpose** |

`shipped-cascade.json` is the most important file here and the easiest to
misread. It is the **real shipped coachmark copy**, and it passes because it is
mechanically accountable: the number is claimed and the symbol resolves.

The tool's guarantee is narrower than "catches wrong copy", because deciding
whether "four or more" or "more than three" is the true reading of
`if (lit < 3) return 0;` is not arithmetic. What it guarantees is that the
contradicting source lands directly under the claim, where a critic cannot miss
it. So the case asserts both of these appear in the output:

```
copy says:  "four or more nodes"
  if (lit < 3) return 0;
```

That juxtaposition is the product. The judgment stays with the critic.

## `verdict/` - can a verdict substantiate itself

| case | expected |
|---|---|
| `good.json` | passes: the quote is a literal substring of `kit.ts` |
| `bad-quote.json` | fails: quotes `if (lit < 4) return 0;`, which is not in the file |
| `no-quote.json` | fails: a claim with no quote at all |
| `revise-no-objection.json` | fails: a REVISE with no objection and no required fix |

`bad-quote.json` and `good.json` differ in one character. That is deliberate: a
critic that paraphrases what it read, or reconstructs it from memory, produces
exactly this failure.

## What is not fixture tested

Whether the critic reaches the right verdict. That needs judgment, so it is
demonstrated in a real run rather than asserted here. What these fixtures pin is
that the evidence reaches it.
