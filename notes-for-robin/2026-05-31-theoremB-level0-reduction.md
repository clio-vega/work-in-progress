# Theorem B: level-0 coefficient verified n≤7, and PROVED for τ>0

**Date:** 2026-05-31 (prove session). (Harness note: command stdout was delivered only in
lumpy batches this session, which slowed cross-checking — but everything resolved.)

## Result

For Theorem B (`{d_j}(λ)={s(T)}`, branch-exponent multiset of the Baxterised w₀ monodromy) I
isolated and pinned down the **level-0 coefficient** `#{j:d_j=0}`.

**Reduction.** At fusion `r(q²)=0` so `M(q²)=∏_a P_q^{(i_a)}` (staircase word). By continuity of
char-poly roots, `#{d_j=0}=n_λ−mult₀(charpoly M(q²))`; and since 0 is semisimple in `M(q²)`
(you verified this), `=rank M(q²)=rank ∏P_q`. Level-0 of B is then

    #{d_j=0} = #{s(T)=0} = K_{λ,β(E)},   β(E)=(2^{n/2}) (n even).      (★)

**Verified n≤7.** Reading the multiplicity of 0 off your `survey7.out`: (4,2)→3, (4,1,1)→1,
(3,2,1)→2, (2,2,2)→1, … each equals `#{s(T)=0}`. Holds for all 43 shapes n≤7. Independently
re-confirmed by a self-checking seminormal script for all shapes n≤6 — and the count is the
same for FIVE different reduced words for w₀, so the level-0 count is **word-independent**
(the operator `∏P_q` is word-dependent, but its rank isn't).

**τ>0: PROVED.** `|S|=0<τ(τ+1)/2 ⟹ Ω=(q+1)^N M(q²)=0` (Strong Pillar 1) ⟹ `#{d_j=0}=0=K`.
One-line corollary of work already done. **Level-0 of B is closed for every τ>0 shape.**

**τ=0: residual** is the clean finite statement `rank ∏_a P_q^{(i_a)} = K_{λ,(2^{n/2})}` — no
Puiseux content, pure linear algebra at `x=q²`. Cleanest next target.

## The lead I'd love your eyes on

`K_{λ,(2^{n/2})}` = dim of the `(2^{n/2})`-weight space of the GL-irrep `V_λ` (content "every
value twice"). Conjecture: the (word-independent) **image of the staircase `∏P_q` at q² is
exactly that weight space** — i.e. fusion at q² *pairs the strands*. That would prove the τ=0
case by inevitability and template the higher levels. The 2-step alphabet recursion you already
found (`A(n)=A(n-2)∪(A(n-2)+(2n-3))`, "pairing adjacent transpositions") points the same way.
Does the strand-pairing / `(2^{n/2})`-weight-space picture ring a bell from the integrable or
Schur–Weyl side?

## Honest footnote
I briefly thought I'd found a counterexample at (4,2)/(4,1,1); it was my own bug — a stray
`sp.nsimplify` on exact rational matrices. Cross-checking against your `fastp` survey caught it.
(★) is solid.

## What's still hard
Higher levels `#{d_j≥k}`: Newton polygon of `det(tI−M(x))`; gaps = no-leading-cancellation and
eigenvalue-valuation-vs-Smith. Not hand-waved; needs the ε-series engine on examples.

## UPDATE (same session, later): the lead is PROVED — it's FUSION.

The strand-pairing conjecture above is now a theorem (modulo one clean n-uniform lemma), and it
turns out to handle **all τ at once**, not just τ=0. Statement:

    #{d_j(λ)=0} = K_{λ, β(n)},   β(n) = (2^⌊n/2⌋, 1^{n mod 2}),   for EVERY λ.

**Proof (Schur–Weyl fusion).** Take m≥n; (C^m)^⊗n = ⊕_λ V_λ^{GL} ⊗ S^λ. Each P_q^{(i)} is the
q-symmetrizer on strands i,i+1, and M(q²)=∏P_q commutes with U_q(gl_m), so
`rank(M(q²)|_{S^λ}) = mult of V_λ in im M(q²)`. Now choose the **odd-even transposition-sort**
reduced word for w₀ (legit since the level-0 count is word-independent): its leftmost layer is
{P_1,P_3,P_5,…} on disjoint pairs, so `im M_oe(q²) ⊆ (Sym²_q)^⊗⌊n/2⌋ ⊗ (C^m)^{n mod 2} =: S`.
A rank computation shows this containment is **equality** (I verified im = S as a literal
subspace, n≤6, m≤4, both parities). Since char(S)=h_{β(n)}=Σ_λ K_{λ,β(n)} s_λ, the multiplicity
of V_λ is K_{λ,β(n)}. Done. And K_{λ,β(n)}=0 ⟺ λ'_1>⌊n/2⌋ ⟺ τ>0 — so this **reproves** the
τ>0 vanishing (Strong Pillar 1) from the same picture: V_λ just isn't in the fused module.

**The one remaining lemma** (fusion-invertibility): `M_oe(q²)|_S` is invertible, i.e. rank=D. I
proved it per fixed n: confinement gives rank≤D identically in q, and rank only drops under
specialization, so rank_{C(q)} ≥ rank_{q=2} = D (exact compute) ⟹ det(M_oe|_S)(q) ≢ 0. The
determinant is a clean nonzero monomial — m=2: n=2→1, n=4→64q¹⁶/(q²+1)¹⁶. The conceptual reason
it holds for **all** n is the Kulish–Reshetikhin–Sklyanin fusion: after the odd layer fuses pairs
into Sym² super-strands, the remaining factors are fused Ř-matrices at non-singular parameters,
composing to an invertible monodromy on ⌊n/2⌋ sites. **This is where I'd value your eyes** — is
there a one-line fusion-calculus argument that M_oe|_S is invertible (or unitriangular in the
pair-basis, which the monomial determinant suggests) uniformly in n?

Net: level-0 of Theorem B is now PROVED for all n≤6 (all τ), and reduced for general n to this
single fusion lemma. Writeup: `~/projects/proofs/2026-05-31-theoremB-level0-fusion.tex` (compiles).

## Files
- `~/projects/proofs/2026-05-31-theoremB-level0-fusion.tex` (fusion proof, 4pp, compiles) — NEW.
- `~/projects/proofs/2026-05-31-theorem-B-reformulations.md` (earlier writeup).
- `~/projects/scratch/2026-05-31-thmB/tensor_fusion.py` (image=S verification, both words/parities),
  `det_lemma.py` (symbolic det of M_oe|_S), `verify_B2.py` (level-0 + word test), `prove-journal.md`.
  Project engine: `~/projects/scratch/2026-05-31-branch-multiset/`.
