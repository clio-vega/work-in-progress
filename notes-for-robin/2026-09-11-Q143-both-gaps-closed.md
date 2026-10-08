# Q143 — both combinatorial gaps closed, and `thm:class` is now proved for all μ

**Date:** 2026-09-11 (PROVE, cycle 1)
**Paper:** https://github.com/clio-vega/proofs/blob/main/2026-09-11-Q143-graph-criterion.tex
**PDF:** https://github.com/clio-vega/proofs/blob/main/2026-09-11-Q143-graph-criterion.pdf
**Scripts:** https://github.com/clio-vega/proofs/tree/main/scripts-2026-09-11-Q143
**Commit:** `clio-vega/proofs@b272a1c`

## What closed

The 2026-09-10 paper reduced the Khanna–Loehr local-identity classification to two open
statements about a labelled graph `G(μ)`, and verified them to n ≤ 9:

- **(G1)** `G(μ)` is connected.
- **(G2)** for n ≥ 6, `G(μ)` carries a cycle whose label product is ≠ 1.

Both are now proved, and (G2) in a stronger form. Together with a third proof (below),
`thm:class` — the classification of the μ for which the local identity with T = S is
consistent over ℚ(t) — is **proved for all μ and all n**. The n ≤ 9 table is now only a check.

## The idea, in one paragraph

The paper wrote the graph's relations on abacus pairs `(b,b')`. Making the hole enumeration
explicit (`u₁ = -ℓ`, `h_ik = b_i - u_k`) shows the vertices *are* the cells of μ, and then the
whole thing becomes a hook-length statement on the Young diagram: **edges run only along rows
and columns**, and

> `(i,k) ~ (i,m)` iff `h_ik + h_im` is **not** a hook length of row i — dually for columns.

The variable `t` leaves the combinatorics entirely. After that both gaps are short:

- **(G1):** `h_i1` is the *largest* hook in row i, so `max + anything > max` is not a hook. The
  corner cell of each row is a hub, `(1,1)` is a hub of hubs, diameter ≤ 4.
- **(G2):** every label is `-t^h`, and `(-t^h)⁻¹ = -t^{-h}` — traversal direction inverts the
  exponent but **not the sign**. So an odd cycle has product `-t^m ≠ 1`, with no exponent
  bookkeeping. Then: `G(μ)` is **triangle-free iff n ≤ 3 or μ ∈ {(2,2),(3,2),(2,2,1)}** — a
  complete classification, which gives (G2) for every n ≥ 4 outside the exceptions.

## Two things worth your attention

**1. I found an error in my own previous paper, and it is the reason the gap stayed open.**
`sec:gaps(2)` of the Q140 paper says: *"for μ=(3,1,1,1,1) the row-1 hooks are 7,2,1 and no second
edge inside row 1 exists."* That is false. The condition the paper used, `d₁+d₂ > h_i1`, is
**sufficient but not necessary** — the exact condition is `d₁+d₂ ∉ H_i`. Here `h₁₂+h₁₃ = 3 ∉
{7,2,1}`, so the edge exists and row 1 *does* carry a triangle. I confirmed it independently
from the matrix. The sentence was the stated reason for abandoning the triangle route; a
sufficient condition used as if necessary manufactured an obstruction and stopped the search for
a day. The negative control that flips it back moves the non-bipartite count at n = 4, 5 and 7.

**2. Building the registry is what exposed the real gap.** When I went to grade the chain I
noticed `prop:reflect` — the only link between `G(μ)` and the matrix — was stated in the Q140
paper with a *sketch* ("...generically admits exactly two decompositions...") and verified only
to n ≤ 8. So (G1)+(G2) would have left the classification still resting on a computed step. I
proved it: both edge types are **one configuration** (two beads and two holes with `b+c = b'+e`,
which the midpoint reflection forces into exactly two orderings), the witnessing row is explicit
(`B \ {b,c} ∪ {b',e}`), and "exactly two nonzero entries" is a four-line set computation. I also
replaced the paper's "verified" consistency at the nine exceptional μ with explicit solution
vectors over ℚ(t), checked by substitution.

I mention this because the grading step did real mathematical work here, not just bookkeeping.

## Instrumentation

Three independent constructions of `G(μ)` — from the abacus relations, from hook lengths alone,
and from a rim-hook matrix that uses neither — agree on **edge sets and labels** (138 partitions
n ≤ 10; 66 partitions n ≤ 8). That is sharper than the paper's claim that the two families
"span the same space". Four negative controls, all of which move. Counts factorised against
their quantifiers rather than reported as totals.

## What I did *not* prove (stated in §8 of the paper)

- **Completeness** of `prop:reflect` — that (I) and (II) exhaust the two-term rows of M. Not
  needed for `thm:graph`, which requires only soundness. Verified n ≤ 8.
- The **converse** of `thm:graph`: failing the cycle criterion is not shown to imply consistency.
  Not needed, since consistency at the nine exceptions is now proved by exhibition.
- `rank M^(μ)(-1) = n`, the hypothesis of `prop:firstorder`. Untouched, still verified n ≤ 8.
- Gap (2) of the earlier paper: Khanna–Loehr allow `T(μ,L)` to be an arbitrary subset of
  `R(n-L)`. Nothing here bears on that.

## Question for you

The hook-length criterion `h_ik + h_im ∉ {hooks of row i}` defines a graph on any Young diagram
without reference to any of this machinery, and it is conjugation-self-dual. Triangle-freeness
turns out to have a clean classification. Is this graph known? It smells like it should have a
name, and I have not searched — this was a prove session.
