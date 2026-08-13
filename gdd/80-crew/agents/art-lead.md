---
title: Art Lead
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[art-direction]]", "[[law-5-imagery]]", "[[ux-agent]]"]
---

# Art Lead

Pixel asset fabrication. **Haiku**, `maxTurns` 40. Tools: Read, Write, **Bash**, ToolSearch, Higgsfield, PixelLab.

One of only two agents with Bash, because its job is running generators and post-processors.

## Owns

`pipeline/art/done/` and the status field on `pipeline/art/orders/*.json`. Never `kernel-panic-site/`.

## The pipeline

1. Read an open order.
2. Generate via Higgsfield `nano_banana_pro`, **2 credits per image**, with the palette hexes pinned in the prompt.
3. Post-process deterministically: `dither.py` for 1-bit window imagery, `pxpost.py` for pixel assets.
4. Write `<order-id>.png` alongside `raw-<order-id>.png`, and update the order status.

Keeping the raw alongside the processed one means a treatment can be re-derived without re-spending credits.

## Palette-pinned plus deterministic post

> [!info] This is what keeps a generative pipeline on-model
> The generator is stochastic; the post-pass is not. Pinning hexes in the prompt and then running a fixed dither means two images generated a week apart still belong to the same game.

See [[art-direction]] and [[law-5-imagery]].

## A note on tooling

**PixelLab is a nearly empty trial.** Higgsfield is the working generator despite PixelLab being the more obviously fitting tool.

## Output

19 finished images in `pipeline/art/done/`, symlinked into this vault at `_attachments/art`.

## See also

- [[art-direction]] · [[ux-agent]]
