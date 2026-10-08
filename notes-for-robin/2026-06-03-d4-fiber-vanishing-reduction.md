# d=4 fiber-vanishing: a clean reduction, and the obstruction I couldn't pass

**Date:** 2026-06-03 (prove session)
**Target:** `G_λ(i) = 0 ⟺ λ = (2,2)`, where `G_λ(q)=Σ_T q^{s(T)}` (graded branch exponents).
**Status:** Reduction PROVED; final nonvanishing OPEN (precisely demarcated).
**Doc (pushed):** https://github.com/clio-vega/proofs/blob/main/2026-06-03-d4-fiber-vanishing.tex

## The one idea worth keeping (the reduction)

At ζ_4 the active set `A={k : n−k odd}` is a step-2 arithmetic progression, so all
its elements share one parity, so `i^{2k−1}` is CONSTANT over k∈A. The master
identity's product therefore collapses to a **single pure power**:

- n=2m even: `G_λ(i) = ⟨s_λ, ψ^m⟩`, `ψ = h_2 + i e_2 = s_2 + i s_{11}`.
- n=2m+1 odd: `G_λ(i) = ⟨s_λ, h_1 ψ̄^m⟩`.

So **`G_λ(i)=0 ⟺ λ ∉ supp_ℂ(ψ^m)`** (n even). This dissolves the worry in
PROVE.md ("value is genuinely complex, d=3 won't transplant"): it explains *why*
d=3 fails — at ζ_3 the factors pair as φ,φ̄ giving the Schur-positive
Θ=φφ̄; at ζ_4 with n even there is **no conjugate partner inside the product**, so
ψ^m is irreducibly complex and no positivity is available.

Equivalent faces (all verified numerically):
- Interpolating poly `P_λ(t)=⟨s_λ,(h_2+te_2)^m⟩∈ℤ_{≥0}[t]`, `G_λ(i)=P_λ(i)`;
  `(t²+1)|P_λ ⟺ λ=(2,2)`. Pinned: `P_λ(1)=f^λ`, `P_λ(−1)=χ^λ(2^m)`, `P_λ(0)=K_{λ,2^m}`.
- Hermite determinant: `h_r(p_1=A,p_2=B,0)=[z^r]e^{Az+Bz²/2}` ⟹ `s_λ(A,B,0)=det(Hermite)`,
  and `P_λ(t)=(1/√π)∫e^{−s²}s_λ(2s,2t,0)ds` (Hubbard–Stratonovich on p_1²).
- Parseval: `Σ_{λ⊢2m}|G_λ(i)|² = 2^{−m}Σ_a C(m,a)²2^a a!(2m−2a)!` (=2,12,168,4512,…).
- **Kostka form** (via e_2=h_1²−h_2 ⟹ ψ=i h_1²+(1−i)h_2):
  `G_λ(i)=i^m Σ_k C(m,k)(−1−i)^k K_{λ,(2^k 1^{2m−2k})}`. Reducing mod the Gaussian
  prime (1+i) kills k≥1 ⟹ `G_λ(i)≡i^m f^λ (mod 1+i)` ⟹ **f^λ odd ⟹ G_λ(i)≠0**
  (so every vanisher has f^λ even; f^{(2,2)}=2 ✓). One prime can't see vanishers;
  the even-k and odd-k partial sums do NOT separately vanish at (2,2) (they are
  2+2i and −2−2i, cancelling), so iterating needs the 2-adic valuations of those
  Kostka numbers (2-core tower) — a second possible route besides the involution.

## What's proved vs open
PROVED: the reduction; m=2 support = {λ⊢4}\{(2,2)} (one-line Pieri:
ψ²=s_4+(1+2i)s_31+(2i−1)s_211−s_{1^4}, the s_22 coeff is 1−1=0); extreme shapes
P_{(2m)}=1, P_{(1^{2m})}=i^m; conjugation P_{λ'}(t)=t^m P_λ(1/t); vanisher-scan n≤16.

OPEN (≡ theorem for m≥3): **supp_ℂ(ψ^m) is full for m≥3.** The Re and Im parts are
signed sums (a_0−a_2+a_4−…); each vanishes for some λ, but the two zero-sets are
DISJOINT except at (2,2). No Schur-positive proxy exists (P_λ(t) is generically
irreducible, e.g. (5,5): t⁵+10t³+10t²+15t+6).

## Where I'd look next (the route I believe in)
The skewing recursion at t=i is `P_λ(i)=Σ_horiz P_μ(i) + i·Σ_vert P_μ(i)`, i.e.
`P_λ(i)=Σ_chains i^{vert(chain)}` over horizontal/vertical 2-strip removals λ→∅.
At **t=−1** the same model gives `Σ(−1)^{vert}=χ^λ(2^m)`, resolved by the classical
sign-reversing involution whose fixed points are domino tableaux ⟹ the proven
2-core law. At **t=i** one wants the **fourth-order (ζ_4) analog**: group chains into
orbits with `Σ i^{vert}=0`, residual fixed configs governed by the **4-quotient**.
Evidence this is the right object: every vanisher is a 4-core (PROVE.md pt 3, I
reconfirmed), and the staircase 4-core (4,3,2,1) gives `G=24(1+i)^5` — a pure power
of the Gaussian prime (1+i). Constructing this involution (well-defined; fixed set
nonempty ∀λ≠(2,2)) is the missing step. I think this is a genuine
domino-tableaux-style combinatorial project, not a one-liner.

Question for you: is there a known "ζ_d cyclic sieving on r-ribbon / r-strip
chains" that already packages this? It feels adjacent to the
Springer/Stembridge q=−1 fake-degree sieve we used for Theorem B, but at a
primitive 4th root and for 2-strips rather than dominoes.

Scripts: `~/projects/scratch/d4_*.py`, `prove-2026-06-03-d4.md`.
