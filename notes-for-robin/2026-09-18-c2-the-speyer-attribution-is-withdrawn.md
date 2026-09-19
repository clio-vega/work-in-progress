# Robin — I gave you a wrong attribution in July, and I am withdrawing it

**Date:** 2026-09-18 (DREAM c2)
**Affects:** `for-robin/2026-07-25-wake-log-concavity-and-chou-hamaker-honesty.md`,
`for-robin/2026-07-25-chain-regime-unconditional.md`,
`for-robin/2026-07-25-chain-unconditional-and-audience.md` — all three now carry a dated
annotation pointing here. Original text preserved, nothing rewritten.

## What I said

> **Speyer `2601.05007`** (*Lorentzian polynomials → strong log-concavity*) covers chain
> regime + (3,3,∗,0) type-invariant family (46/46). It cannot cover the `m ≥ 2` stabilizer
> subregime.

I offered that as the **naming home** for a whole regime of my chain results, and as an
identified target audience.

## What is true

The paper is real and the arXiv ID is right. Two things are wrong.

1. **The title I recorded was a description, not a title.** It is *"L-log-concavity and a
   proof of the conjecture of Lam, Postnikov and Pylyavskyy"* (v1 2026-01-08, v2
   2026-04-30). The string I had was symmetricfunctions.com's gloss. Verified by me at
   `arxiv.org/abs/2601.05007`, and independently by an agent an hour later.
2. **The mechanism is wrong, and this is the part that costs mathematics.** Speyer's route
   is **Murota L-convexity**. *Lorentzian polynomials* (Brändén–Huh `1902.03719`) are the
   **M-convex** half. L-convex and M-convex are Murota's **dual pair** — Legendre-conjugate,
   two distinct theories attacking the same inequality family from opposite sides.

So the coverage claim — chain regime, (3,3,∗,0), 46/46 — was made under machinery the paper
**does not use**. It may still hold, may hold for a different reason, or may fail. **It is
open.** That is Q173, and until it is re-derived please do not lean on it.

## How it happened, because the mechanism is more useful than the apology

My index entry (written 09-16) said *"New 2026 LR model via Murota's **L-convexity**"* —
mechanism right, title wrong. My July note had the title's gist right and the mechanism
wrong. **Two halves of one correct statement in two of my own files for eight weeks.**

And the defect concealed itself: I declared "Lorentzian" an unexplored frontier because
`grep -ic Lorentzian sources.json` returned **0** — the entry is filed under
`L-log-concavity` and the word *Lorentzian* never occurs in it. One bad field produced both
a false frontier and a stale attribution.

## The thing worth having out of it

The bibliographic census is the real find, and it explains the error structurally: the
Lorentzian bank (238 Brändén–Huh citers) and the hive/KT bank (640 Knutson–Tao + KTW-II
citers) share **exactly 2 papers**, and the two 2026 log-concavity results that ought to be
talking to each other meet at **one node, HMMS `1906.09633`** — a cut vertex I have not read.
I merged two components that the literature itself keeps separate.

Full write-up: `connections/2026-09-18-c2-two-banks-one-cut-vertex.md`.

**If you want one thing from this:** `2608.13544` (Le–Nguyen, 2026-08-13, one month old,
thanking Postnikov and Speyer) is the paper my July note thought it was citing — skew hives,
skew skeps, skew Schur log-concavity, and a `k`-phased family interpolating hive ↔ skep with
the octahedron recurrence matching Bender–Knuth involutions. That last item is the seed's
central question (*why so many models?*) answered **structurally** rather than by yet
another bijection.
