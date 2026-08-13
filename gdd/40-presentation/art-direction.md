---
title: Art direction
status: canon
source: rulings
owner: orchestrator
updated: 2026-08-05
related: ["[[law-5-imagery]]", "[[art-lead]]", "[[kp-os]]"]
---

# Art direction

## The rule

**1-bit dithered imagery, at 1:1 pixel mapping, never downscaled.**

Browser downscaling mushes the dots into grey noise. To show less, **crop**; to show more, crop wider. Integer upscaling is acceptable; downscaling never is.

Frame the crop on the **subject**. A centre crop of a busy illustration is usually the middle of the clutter and reads as texture rather than as an image.

## Imagery must be diegetic

There must be an in-fiction reason for the OS to show it. A portrait exists because the ticket carries a client photo; a device macro exists because the intake scanned it. Decoration with no diegetic warrant does not ship.

## Three treatments

| Treatment | What it is |
|---|---|
| **INK TINT** (default) | 1-bit multiplied to `--r-aux`, so it recolours with the scheme |
| **TRUE 1-BIT** | untinted. The source art is monochrome ink, so this is its actual colour |
| **FULL COLOUR** | a **colourisation, not a reveal**: gradient-map the raw greyscale through a lit-interior palette, then Floyd-Steinberg dither to a 16-colour adaptive palette so it still reads as a dithered frame |

See [[law-5-imagery]].

## The pipeline

| Tool | Job |
|---|---|
| Higgsfield `nano_banana_pro` | the working generator, 2 credits per image |
| `pipeline/tools/dither.py` | 1-bit dither treatments for window imagery |
| `pipeline/tools/pxpost.py` | the deterministic pixel post-pass for pixel assets |
| `pipeline/tools/colourise.py` | the FULL COLOUR gradient map |

PixelLab is a nearly empty trial and is not the working generator.

Palette hexes are pinned in every prompt, which is what keeps a generative pipeline on-model. See [[art-lead]].

## The finished set

19 images in `pipeline/art/done/`, symlinked into this vault at `_attachments/art`. Customer portraits, device macros, client figures, story stills, and window furniture.

Examples in [[juno-vex]], [[aldous-wick]], [[sable-okonkwo]], [[wren-tallis]], [[bram-hollander]].

## The open palette question

Whether role-token colour is the general law or a single-window exception is **unresolved**. See [[palette-generalization-conflict]].

## See also

- [[law-5-imagery]] · [[art-lead]] · [[music-and-sound]]
