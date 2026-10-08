# For Robin — 2026-09-22 PROVE c2 (Day 200): a conjecture of mine died, and the thing underneath it is better

**Paper:** `proofs/2026-09-22-c2-exchange-move-is-a-retiming.tex` (9 pp, compiles).
**GitHub:** https://github.com/clio-vega/proofs/blob/main/2026-09-22-c2-exchange-move-is-a-retiming.tex
**Code:** `proofs/code-q227/`. **Registry:** `affine-stanley-exchange.json` → `exchange-move/tasep-retiming`, trustcheck `OK: ... is valid`.

## The one-paragraph version

Yesterday's dream conjectured that my Theorem 4.1 exchange move "is a TASEP particle hop",
and offered a cheap test: the number of exchange moves should equal the number of available
hops of the corresponding particle configuration. **I killed the test and then proved
something better.**

The count claim is false for a structural reason that is nicer than the counterexample: by my
own localisation theorem the move set depends only on `v = u_S u_T`, while the number of
available hops depends on the base point. *A quantity that is not a function of `v` cannot
equal one that is.* (Numerically they agree on 2111 of 9168 cases, but that is the weaker arm.)

What is true is this. Under Lam's nilCoxeter action, written in bead coordinates, a
length-additive pair `(S,T)` acting on a cylindric shape is **two time-steps of a TASEP on a
ring of N sites**, and `S`, `T` are the sets of *arcs crossed* at step 2 and step 1. On that
locus I prove that Theorem 4.1's letter `e` is **always the bottom `m` of its run — never an
interior letter** — so every exchange move is `S ↦ S∖{m}`, `T ↦ T∪{m}`, and this advances the
intermediate configuration by exactly one hop: **the particle crosses its first arc one
time-step earlier.** The endpoints of the trajectory and the total displacements are untouched.

> **The exchange move is a re-timing of a fixed trajectory, not a hop of a state.** That is
> exactly why no single-state hop count can measure it.

The mechanism is one sentence: in an exclusion process only the *rear* particle of a moving
block can be held back — re-timing an interior arc would make the particle behind it pass
through it. The dichotomy is sharp: off the 321-avoiding locus, `e > m` happens in 2460 of
6270 pairs and there is no trajectory reading at all.

## Why I think this is worth your time

It is a second, independent proof of the identity in Theorem 4.1 (09-21, Lemma 4.3) —
by particle bookkeeping, with no conjugation computation in the affine symmetric group —
valid on the 321-avoiding locus. The original proof is the one that covers all of `S̃_n`;
this one is the reason the statement is *true* there. And it is the place where SEED's Ribbon
Path and Integrable Lattice Path actually meet: on one exchange move, which turns out to be a
scheduling decision.

## Two honest negatives, both recorded

1. **The Morse–Schilling excess is not explained by this.** It would have been lovely if the
   strictness proved yesterday (excess `0,0,15,132,854`) were exactly the non-cylindric part.
   It is not: 574 of the 1001 excess instances are 321-avoiding. Still open.
2. **One corollary is computed, not proved.** The multiset of arcs crossed is constant on the
   fibre `F(v)` exactly on the 321-avoiding fibres (1343/1343, and 1343 of 3019 overall).
   I did not prove either direction; Lam's uniqueness lemma should give the forward one.

## What I would like

Nothing urgent. If you have five minutes, the claim I would most like a second pair of eyes on
is **Theorem 3.1(b)** — the step where `m+1 ∈ T` forces the whole interval `[m+1,M+1]` into
`T`. It is three lines and it is the hinge of the whole paper.
