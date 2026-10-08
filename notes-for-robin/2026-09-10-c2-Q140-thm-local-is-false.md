# For Robin — 2026-09-10 c2 (PROVE)

## The short version

This morning's paper, `2026-09-10-Q129-reciprocity-does-not-deform.tex`, has a false theorem
in it. `thm:local` says the Khanna–Loehr local identity is inconsistent over Q(t) for *every*
μ⊢n, 4≤n≤7. It isn't: at n=4, μ=(2,2) it is solvable, and at n=5 so are μ=(3,2) and (2,2,1).

**The refutation was already printed in that same paper.** Its anchor-scan table gives the
generic column as 1/5 at n=4 and 2/7 at n=5 — i.e. one and two solvable μ. The prose explains
those away by saying that for those μ "the system happens to be square, P(n) equations, P(n)
unknowns". That is also wrong: |C(μ)| = n exactly, so the system is 5×4 at n=4 and 7×5 at
n=5, and it is square only for n≤3.

So the lesson is not "a brief's citations are not primary sources" (that one has fired plenty).
It is narrower and I had not met it: **a paper can refute its own theorem in its own
verification section.** The check to add is mechanical — diff the theorem's quantifier against
the verification table before shipping.

## The good news, which is most of the news

The corollary that motivated the whole computation is fine, and is now **proved for all n**
rather than verified for n≤7. The Khanna–Loehr local identity has to hold at *every* μ, so
one failing family suffices, and I have one:

> For μ=(n) and every n≥4 there is an explicit certificate c with cM=0 and cb = t(t+1) ≠ 0,
> supported on the n hooks (a,1^{n-a}) together with the single row (2,2,1^{n-4}).

At n=4 it *is* the certificate the paper displays. That is gap (1) of that paper, closed in
the direction that matters. By conjugation μ=(1^n) comes free.

The mechanism turned out to be very simple once I found the right description: for μ=(n)
every row of the matrix is either the all-ones row, or zero, or has exactly two entries, so
the homogeneous system is just `t·w_{b-1} + w_a = 0` for all a≥b≥1 with a+b≤n. Three of those
force t(t+1)·w_0 = 0.

## Two other things worth keeping

1. **The t=−1 anchor is the Euler identity.** ∑_L p_L p_L^⊥ = n·id on Λ_n, plus
   Murnaghan–Nakayama, gives the inverse weights in closed form: wt_B(μ,γ) = (−1)^{ht(μ/γ)}/n,
   every μ, every n. Three lines, and it replaces a cited black box. It also has a consequence
   I like: since the system is consistent at t=−1 for every μ, *every* certificate whatsoever
   must have its obstruction vanish there. So the (1+t) in the obstruction value is forced by
   a theorem I already hold — it is **not** a fourth independent sighting of the (1+t) that
   shows up in the sorting/commuting criterion. I had been about to count it as one.

2. **The general μ case is reduced to a t-free graph criterion** and then stops. Two
   "reflection" families of two-term relations on the abacus generate exactly the two-term
   rows; the question becomes whether a labelled graph on the n cells of μ is connected and
   carries a cycle of nontrivial label product. Verified equivalent for all 95 partitions with
   n≤9. Both halves are open in general. This is the honest boundary of the session.

## Paper

`https://github.com/clio-vega/proofs/blob/main/2026-09-10-c2-Q140-local-identity-certificate-family.tex`
(8pp; commit `7a7ed78`; verification scripts in `proofs/scripts-2026-09-10-c2-Q140/`).

Registry: `Q129-local-identity-unsolvable` is now `dead-end` with the counterexamples and the
reason; six new nodes under `Q129-reciprocity-does-not-deform`, two of them `proved`. Both
validators pass with `--files-dir /home/clio/projects`.

## One process note

The WAKE boot prompt still ships `--files-dir proofs`, which produces a wall of fake
"file not found" against files that exist. I used the correct root. Worth fixing at source —
`boot-prompt.md` is a read-only bind-mount from my side.
