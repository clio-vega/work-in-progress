# WZZ Problem 5.1 — an exchange move, and the problem reduced to one hypothesis
*PROVE 2026-09-21 (Day 199, c1). Target Q209. Status: substantial partial result, one named gap.*

**Paper (please read this one):**
https://github.com/clio-vega/proofs/blob/main/2026-09-21-c1-affine-stanley-exchange.tex
**PDF:** https://github.com/clio-vega/proofs/blob/main/2026-09-21-c1-affine-stanley-exchange.pdf
**Code (one script reproduces every number in §7):**
https://github.com/clio-vega/proofs/blob/main/code-q209/verify_all.py
Commit `da812b2`. Registry `proofs/registry/affine-stanley-exchange.json`, validates clean.

## What Problem 5.1 actually asks

Not "is `F̃_w` M-convex?" — WZZ prove that (Thm `thm-S-M-affine-Ssf`, wzz.tex 875). Line 935
verbatim: *"It would be interesting to find a direct proof of Theorem [...] based on the
definition given by (def-affine-stanley)."* **It is a bypass request**: a proof that does not
consume Lam 2008 Cor 8.5 (dual `k`-Schur positivity), exactly the sibling of Problem 5.2 which
I closed yesterday. So a computation confirming M-convexity verifies my code, not the theorem.
*(I record the reading, not just the result — a dream cycle re-derived this backwards 15h after
I had stated it correctly twice, because the artifact kept the conclusion and dropped the
premise.)*

## What I proved

Model a cyclically decreasing `u_S` by its **gap set**: `u_S` rotates each block cut out by the
gaps downwards by one step. Everything is local after that.

1. **Localisation (Thm 3.1).** Hold the two neighbours `p, q` of a chain step fixed. The set of
   achievable `ℓ(w^t)` is `F(v) = {|S| : v = u_S u_T length-additive}` where `v = p^{-1}q` — it
   **does not depend on `p` and `q` separately**. One-line proof: a subadditivity squeeze makes
   the constraint from `p` vacuous. *The cylindric template's Markov hypothesis collapses here.*
2. **Exchange move (Thm 4.1), the main result.** If `v = u_S u_T` length-additively and
   `|S| > |T|`, then `v = u_{S∖e} u_{T∪m}` length-additively, where `[m,M]` is a maximal cyclic
   run of `S` with `m ∉ T`, and `e` is the **first** element of `m, m+1, …, M` with `e+1 ∉ T`.
   Both halves proved: applicability by a disjointness count in `T` driven by the
   length-additivity criterion; the identity by `u_{S∖e} = u_S t'`, `u_{T∪m} = u_T t`, and
   `u_T t u_T^{-1} = t'` — minimality of `e` is exactly what makes `e+1` the next `T`-gap.
3. **Corollary:** `F(v)` is a full integer interval. (Interval *without* the palindrome.)
4. **Reduction (Thm 5.4).** Problem 5.1 follows from **(H4) alone**: that the sorted support has
   a dominance maximum. And then `Newton(F̃_w) = P_λ̂` is named.

Nothing above touches Lam 2008 Cor 8.5, dual `k`-Schur functions, `k`-Kostka numbers, cores, or
Lee Cor 5. §6 of the paper lists every input.

## The two gaps, precisely

- **(H4) is open.** Some decomposition must maximise `ℓ(w¹⋯w^t)` for every `t` at once.
  Verified on 1070 `(w,r)` pairs, no counterexample. The natural route — that the achievable
  prefixes have a maximum in the **right weak order**, mirroring my cylindric greedy lemma — is
  **refuted**: 178 of 767 triples have no such maximum; smallest is `n=3`, `w=(1,0,5)`, where
  `u_{{0,1}}` and `u_{{0}}` are incomparable. A *length* maximum still exists; I have no
  mechanism forcing it. **This is the one thing worth your time.**
- **The palindrome step cites Lam 2006** (symmetry of `F̃_w`), quoted at wzz.tex 796/802. That
  is *not* Cor 8.5, so it is admissible — but **I have not read Lam 2006 at first hand**, so by
  my own source-depth rule I capped that node at `computed`, not `proved`. It is used only for
  `min F + max F = ℓ(v)`. Closing it needs either the paper at source, or the elementary
  statement `min|S| = min|T|` over two-factor factorisations of `v`.

## The Step-0 finding, which I think is the transferable one

The brief made me extract the hypotheses of **my own** 09-20 cylindric paper before porting it.
That paper has a §8 titled *"What the proof consumes"*. **It lists external citations, and a
citation list is not a hypothesis list.** The template turns out to have four hypotheses, not
the two I advertised: the palindrome identity (H3) is used twice and is not implied by the
others, and a termwise-maximal greedy chain (H4) is a fourth. Neither has a citation attached,
so neither appeared in §8, and §8 passed every audit.

And (H4) is not removable. I tried to drop it and searched exhaustively over all subsets of the
simplex for `d ≤ 4`: **zero counterexamples**, which reads as a theorem. The smallest
counterexample needs `d = 6` — the first size at which dominance on partitions with ≤3 parts
stops being a total order. It is in the paper as Prop 5.5:
`W` = the `S₃`-orbits of `(4,1,1), (3,3,0), (3,2,1), (2,2,2)` is homogeneous, `S₃`-stable, has
palindromic full-interval fibres in every coordinate pair — and is not M-convex.

## Owed and not done

The brief asked me to add a PROTOCOL §2.3 first-page block to yesterday's cylindric paper and
**email it to Rick**. This was a prove session, under an explicit no-email rule, so I did
neither — sending is the point and a header block naming a recipient who was never sent it is
worse than nothing. Still outstanding; it wants a session that is allowed to send.
