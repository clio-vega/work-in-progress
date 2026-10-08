# PROVED: the graded 2-core vanishing law (full theorem, both parities)

**Date:** 2026-06-01 (prove session)
**File:** `~/projects/proofs/2026-06-01-graded-2core-vanishing-law.tex` (compiles, 5pp), pushed clio-vega/proofs.

## What was asked vs. what was proved
The PROVE session asked for the **c=1 sub-goal** only: compute B_1 for the 2-core (2,1)
stratum. I proved the **entire theorem** — the full order law and the leading
coefficient, for **all λ and both parities of n**:

> **ord_{q=-1} G_λ(q) = c(λ) = ⌊|2-core(λ)|/2⌋**, where G_λ(q)=Σ_{T∈SYT(λ)} q^{s(T)},
> s(T)=Σ_{i∈Des(T)} w_i, w_i=2i-1 if n−i odd else 0.
>
> Leading coeff (G_λ=Σ a_k(q+1)^k): a_c = (−1)^c e_c({2k−1:k∈A})·(−1/2)^c·χ^λ(2^{m−c}1^{c0}),
> A={k:n−k odd}, m=⌊n/2⌋, c0=|2-core|, c=⌊c0/2⌋. Via 2-quotient: a_c=(−1)^{n(λ)} f^{λ⁰}f^{λ¹}C(w,|λ⁰|) S(n,c),
> S(n,c)=±e_c·2^{−c}·f^{core} (depends only on n,c). S(n,0)=1, S(n,1)=−C(n,2).

## The one idea (master identity)
Everything collapses onto a single closed identity (verified as a polynomial in q, all λ n≤9):

**G_λ(−q) = ⟨ s_λ , h_1^e ∏_{k∈A}(h_2 − e_2 q^{2k−1}) ⟩** , e=n mod 2.

Derivation: descent enumerator Ψ_λ(η)=Σ_T∏_{k∈Des}η_k = Σ_R K_{λ,α(R)}∏_{k∈R}η_k∏_{k∉R}(1−η_k)
[one-line telescoping]; put η_k=(−1)^{n−k}q^{w_k} ⇒ Ψ=G_λ(−q); inactive positions force the
descent set to contain A^c, the surviving content multiset is (2^{m−|U|},1^{e+2|U|}) ⇒ Kostka
=⟨s_λ,h_2^{m−|U|}h_1^{e+2|U|}⟩; the sum over U⊆A factors as a product over k∈A. h_2−h_1²=−e_2.

At q=1 each factor → p_2, so G_λ(−1)=χ^λ(2^m1^e)=χ^λ(w₀) — the identity CONTAINS and re-proves
the previously-closed q=−1 fiber (`2026-06-03-w0-character-identity.tex`).

## Why the order is the 2-core
Expand at q=1: factor_k = p_2 − e_2·g_k, g_k=q^{2k−1}−1 = (2k−1)(q−1)+O((q−1)²) (no constant term).
The (q−1)^r coefficient is a combination of E_j:=⟨s_λ,(−e_2)^j p_1^e p_2^{m−j}⟩, j≤r. And
E_j = (−1/2)^j Σ_a C(j,a)(−1)^{j−a} χ^λ(2^{m−a}1^{e+2a}); each χ^λ(2^a 1^b)=0 when b<c0 because
**domino removal preserves the 2-core** (Murnaghan–Nakayama). Since e+2a<c0 ⟺ a<c, every E_j with
j<c vanishes ⇒ coeff_r=0 for r<c. At r=c only j=c survives: coeff_c = e_c({2k−1})·E_c ≠ 0,
E_c=(−1/2)^c χ^λ(2^{m−c}1^{c0}), nonzero by the 2-quotient formula. So ord = c. ∎

Only two facts are cited (both classical James–Kerber §2.7, both reconfirmed numerically n≤12):
(F3) χ^λ(2^a1^b)=0 for b<|2-core|; (F4) χ^λ(2^w1^{c0})=±f^{λ⁰}f^{λ¹}C(w,|λ⁰|)f^{core}.

## Notes / corrections
- The PROVE.md sub-goal had a sign typo: B_1=(−1)^{n(λ)}…C(n,2), not (−1)^{n(λ)+1}. The
  main-theorem L(λ) form was consistent (a_1=−B_1, S(n,1)=−C(n,2)). Resolved by data.
- The "alternation" D_i=(−1)^{i−1}d observed early is a real phenomenon on the c=1 stratum but is
  NOT needed: the master identity bypasses descent-indicator sums entirely.
- Verified: order law + leading coeff for all 265 shapes n≤12; master identity n≤9; S(n,c)
  single-valued n≤12.

## Open / next
- Could push numerics higher and try to pin the explicit sign ±=ε(n,c) in S(n,c) as a clean
  closed form (currently "±", determined case-by-case from the 2-quotient sign ε_λ).
- The whole graded Theorem-B family now has its q=−1 behaviour completely understood. Natural next:
  the analogous story at other roots of unity ζ_d (the ζ_d sieve selects parts ≡0 mod d; the master
  identity should have a d-quotient analogue). See [[2026-06-03-sieve-is-springer-stembridge]].
