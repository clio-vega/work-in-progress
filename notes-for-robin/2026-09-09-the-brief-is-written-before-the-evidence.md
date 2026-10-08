# The PROVE brief is written before the evidence that would revise it

**Date:** 2026-09-09 · **For:** Robin · **Type:** loop-ordering observation, one concrete instance

## The loop, as it ran today

| Time | Phase | What it did |
|---|---|---|
| 00:14 | WAKE | wrote `PROVE.md` — brief for the day, gated on **Q107** |
| 02:47 | BROWSE | **retired Q107 as the gate** ("its warrant did not survive the day", three independent routes), ranked a replacement gate (Q114) and a "first thing to open" (`math/0008188`) |
| 04:47 | PROVE | ran the brief. Ran the Q107 gate. Never opened `math/0008188`. Cited the **09-08** reading log, not the 09-09 one written two hours earlier. |

Nothing was lost today — PROVE independently re-derived BROWSE's Q107 correction, and
its main result (Q104 answered: the involution is $\omega$, with cocycle $t^{e-1}$)
is proved and stands. It also happens to have answered a question BROWSE had opened at
02:47 (Q116, "solve for the cocycle") **without knowing it had been asked.**

But that is luck, and the mechanism will not always be kind: **WAKE authors the brief
at 00:14; BROWSE gathers the evidence at 02:47; PROVE executes the 00:14 brief at
04:47.** The brief is structurally stale before it is read. Last night I promoted the
rule "the reading log is the first draft of the next proof" — and today it fired on
the *wrong log*, because the log PROVE was pointed at was yesterday's.

## What I'd suggest, cheapest first

1. **A one-line addition to the PROVE prompt:** read `memory/reading/$(date +%F)*.md`
   before opening `PROVE.md`, and treat any conflict as the log winning. This is
   entirely inside my own habits and needs nothing from you — I've written it into
   tonight's journal — but it lives in a prompt file I can't edit
   (`boot-prompt.md` is a read-only bind-mount).
2. **Or: have BROWSE append to `PROVE.md` rather than only to its own log.** BROWSE
   already produces a ranked follow-up list addressed to PROVE by name. It just has
   nowhere to put it that PROVE reads.

Option 2 is the structural fix; option 1 is the one I can approximate on my own.

## Also, one thing that does need you

**Matthew Fayers holds an unpublished Hall–Littlewood version of his Schur-$P$ Pieri
rule, "available on request"** (MathOverflow 337891, 2021-02-27). That is a real
person with a real unpublished theorem sitting exactly on the question I've been
working for a week. I can only email you, Lyra and Paul, so I can't ask him. If you
think it's appropriate to write, I can draft the letter.

## Status of the work itself, briefly

Q104 answered: $\omega R_e(t)\omega=t^{e-1}R_e(1/t)$, proved, verified $e\le5$, $N\le8$
on a code-disjoint engine. The honest caveat is that the $\mathbb{Z}/2$ **does not**
explain everything I hoped — the one-bead sector obeys the same equation on $ts=1$ and
is nonzero (52/52), against 0/58 for two-bead. Two of the four sightings become
corollaries; two do not. And CI on `tworow-d4-kernel` was pending, not green, when the
Lean session closed.
