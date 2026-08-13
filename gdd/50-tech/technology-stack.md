---
title: Technology stack
status: canon
source: code
owner: orchestrator
updated: 2026-08-05
related: ["[[technical-requirements]]", "[[performance-budget]]", "[[kp-os]]"]
---

# Technology stack

> [!info] Source
> `kernel-panic-site/app/package.json`, `vite.config`, `src/`.

A browser app. No engine, no build target beyond the web.

| Layer | Choice |
|---|---|
| Runtime | **bun** |
| Bundler | **Vite** |
| Framework | **React** on a TanStack Start template |
| Language | **TypeScript**, `tsc --noEmit` as the schema enforcer |
| UI primitives | Radix, plus the project's own `kp-ui.tsx` |
| Audio | custom **sfxr** synthesis, no audio library. See [[music-and-sound]] |
| Art | 1-bit dithered PNG. See [[art-direction]] |
| Persistence | `localStorage`. See [[save-and-load]] |
| Hosting | Higgsfield, website id `ce0a9c8c-bae7-418c-909a-84648abdcf17` |

> [!danger] REVISED IN PROTOTYPE
> **Unity was cut**, along with the purchased asset packs. The game ships as a browser app, which is what makes the whole KP/OS conceit cheap: an operating system is a much easier thing to render in a browser than a world is.

## No game engine at all

The duel is a reducer over a plain state object. The run is another reducer. Nothing inherits from a framework class, and neither reducer imports React.

That separation is what lets [[simulation-harnesses|the sims]] drive the real reducers headlessly, exactly as the UI does, at 200 seeds a day. A duel coupled to a renderer could not be simulated 4000 times.

## Commands

```
bun run typecheck     # tsc --noEmit
bun run build         # tsc --noEmit & vite build, in parallel
bun run lint
```

## Two traps

> [!warning] `bun run dev` SSR is broken in this template
> Verify builds with `bun run build` plus a fetch against `dist/server/server.js`.

> [!warning] `bun run preview` serves a snapshot
> Every rebuild changes asset hashes, so the preview server must be killed and restarted after `bun run build` or the page 404s its own stylesheet and renders unstyled. `bun dist/server/server.js` serves SSR only, not static assets. localStorage saves are **per port**.

## See also

- [[verification-gate]] · [[technical-requirements]]
