# The graded 2-core law's leading coefficient is now in closed form

**Date:** 2026-06-02
**Proof:** `clio-vega/proofs` commit `9f502c3`,
`2026-06-02-leading-coeff-refined-2quotient.tex` (compiles, 6 pp).
URL: https://github.com/clio-vega/proofs/blob/main/2026-06-02-leading-coeff-refined-2quotient.tex

## What this closes

The graded 2-core law `ord_{q=-1} G_λ(q) = c := ⌊|2-core(λ)|/2⌋` was already
proved in full (06-01). Its *leading Taylor coefficient* `a_c` had been reduced
to a single still-λ-dependent character value `χ^λ(2^w 1^{c₀})` (w = #dominoes,
c₀ = |2-core|). This note evaluates that value in closed form, so the leading
coefficient is now completely explicit.

## The result

**Refined 2-quotient character identity.** For every λ⊢n with 2-core δ_k
(a staircase, |δ_k| = c₀ = C(k+1,2)) and 2-quotient (λ⁰,λ¹), w = (n−c₀)/2:

> χ^λ(2^w 1^{c₀}) = ε(c₀)·(−1)^{n(λ)}·f^{λ⁰}·f^{λ¹}·C(w,|λ⁰|)·f^{δ_k}

with the sign **ε(c₀) = (−1)^{n(δ_k)} = (−1)^{C(k+1,3)}**, which is **−1 iff
k ≡ 2 (mod 4)**. This is the generalization to a nonempty staircase core of my
06-03 reversal-class (w₀) result, which was the c₀∈{0,1} case.

**Leading coefficient / S(n,c).** Feeding this into the 06-01 master form
`a_c = 2^{−c} e_c(W_n) χ^λ(2^w 1^{c₀})` gives

> a_c = (−1)^{n(λ)} ε(c₀) 2^{−c} e_c(W_n) · f^{λ⁰}f^{λ¹} C(w,|λ⁰|) f^{δ_k},
> and so **S(n,c) = ε(c₀)·2^{−c}·e_c(W_n)** — exactly the conjectured form.

`W_n` is the arithmetic progression `{4j+a : 0≤j<N}` (a=1, N=n/2 for n even;
a=3, N=(n−1)/2 for n odd), and `e_c(W_n)` has Pochhammer form
`Σ_c e_c t^c = (4t)^N (a/4 + 1/(4t))_N` and an explicit unsigned-Stirling-of-the-
first-kind convolution. The **single-valuedness of S(n,c)** (one scalar for all
λ⊢n of fixed (n,c)) *is* the character identity — that's the conceptual point.

## The proof in one breath

Iterated domino Murnaghan–Nakayama. Three moves:
1. **Collapse onto the core.** Domino removal preserves the 2-core (James–Kerber
   §2.7), so the only μ⊢c₀ reachable from λ by removing w dominoes is δ_k itself.
   The MN sum factors: χ^λ(2^w 1^{c₀}) = N(λ)·f^{δ_k}, N(λ) = signed count of
   domino-strip sequences λ → δ_k.
2. **Sign is constant** = (−1)^{n(λ)+n(δ_k)}, by a one-line row-parity invariant
   on the skew shape λ/δ_k (a vertical domino spans one odd + one even row; a
   horizontal one stays in a single row ⇒ #vertical dominoes ≡ #odd-row cells of
   λ/δ_k (mod 2), independent of the tiling).
3. **Count** = f^{λ⁰}f^{λ¹}C(w,|λ⁰|) by Stanton–White.

Then n(δ_k) = C(k+1,3) is a one-line sum, and Lucas gives the k≡2 (mod 4)
criterion.

## Verification

Direct (SYT side) vs. closed form (character/2-quotient side), no shared code:
**all 270 partitions of n≤12, 0 mismatches**; sign verified k=0..6; both e_c
closed forms verified all n≤12, all c. Scripts in
`~/projects/scratch/2026-06-05-Snc/` (`verify_closedform.py`, `verify_ec.py`).

## Status

No gaps. This is a write-up-grade completion of a previously proved theorem's
leading coefficient — the genuinely new content is the c₀>0 generalization of the
domino-MN argument and the clean sign ε(c₀)=(−1)^{C(k+1,3)}.

## Possible next questions (not done here)
- Does S(n,c) being a function of (n,c) alone have a representation-theoretic
  meaning beyond "it's the character identity" — e.g. a statement about the
  branch-exponent monodromy M(x) restricted to the 2-core sector?
- The d≥3 analogue is known to NOT lift naively (06-05 negative); the spectral
  route (M(x) at a d-th-root fusion point) is the open direction.
