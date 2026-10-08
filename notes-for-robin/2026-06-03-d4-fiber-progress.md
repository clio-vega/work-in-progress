# d=4 fiber-vanishing: solid partial progress (not yet closed)

**Target:** `G_λ(i) = 0 ⟺ λ = (2,2)` where `G_λ(q)=Σ_{T∈SYT(λ)} q^{s(T)}`, the
parity-twisted graded enumerator. This is the smallest *unproven* case of the
fiber-vanishing trichotomy (d=2 rich/unbounded, d=3 proved 06-02, d≥5 empty).

**Document:** `~/projects/proofs/2026-06-03-d4-fiber-vanishing.tex` (compiles, 6 pp),
pushed to
`https://github.com/clio-vega/proofs/blob/main/2026-06-03-d4-fiber-vanishing.tex`.
Please look when you have a moment — I'd value your eye on the two open routes.

## What's now PROVED (complete, rigorous)

1. **Reduction.** At ζ₄ the master identity collapses (all factors coincide, since the
   active set is a step-2 AP): for n=2m even, `G_λ(i)=⟨s_λ, ψ^m⟩`, `ψ=h₂+i e₂`.
   Equivalently `G_λ(i)=P_λ(i)` where `P_λ(t)=⟨s_λ,(h₂+te₂)^m⟩∈ℤ_{≥0}[t]`, so
   `G_λ(i)=0 ⟺ (t²+1)|P_λ`. Transpose acts by reciprocation `P_{λ'}(t)=t^m P_λ(1/t)`.

2. **Parity criterion.** In ℤ[i] mod the prime (1+i): `G_λ(i) ≡ f^λ`. Hence
   **f^λ odd ⟹ G_λ(i)≠0** (excludes infinitely many shapes outright). Refined:
   `Re G_λ(i) ≡ (f^λ+χ^λ(2^m))/2`, `Im ≡ (f^λ−χ^λ(2^m))/2 (mod 2)`, giving explicit
   mod-4 necessary conditions for a vanisher (and χ^λ(2^m)=0 unless 2-core empty).

3. **Exact values via a ψ⊥ 2-strip recursion** (weight 1 horizontal, i vertical, 1+i
   disconnected): `G_{(n)}=1`, `G_{(1^n)}=i^m`, `G_{(2M−1,1)}=(M−1)+Mi`, and the
   decisive one
   ```
        G_{(2m−2,2)}(i) = m(m−2)·i,
   ```
   which vanishes **iff m=2, i.e. iff λ=(2,2)**. So among two-row shapes (2,2) is
   provably the unique vanisher. Hooks verified vanishing-free n≤22; two-row n≤24.

## The GAP (precise) — where I got stuck

The full theorem ⟺ ψ^m has full Schur support for m≥3 (and omits exactly (2,2) at
m=2, a one-line expansion). Unlike d=3 — where the analogous Θ=φφ̄ was **Schur-
positive** so the support induction had no cancellation — at d=4 every master factor
is the *same* ψ (no conjugate partner), so ψ^m has genuinely **complex** coefficients
and the Pieri recursion `G_ρ=Σ_horiz G_μ + i Σ_vert G_μ` cancels. It does cancel,
exactly at (2,2).

**The naive ζ₄ sign-reversing involution route is REFUTED** (you'll recall the 06-09
note): not an involution, and Σi^vert over non-fixed chains is a nonzero set-invariant
(first break at (3,3), 3-cycle). My .tex states this.

Two routes I could not close:
- **(1+i)-adic monovariant.** Suffices to show v_{1+i}(G_λ(i)) finite for λ≠(2,2).
  It IS finite but *irregular* (2,3,5,6,8,9,11,…), no closed form vs 2-core/4-quotient
  — so the clean q=−1 law `ord=⌊|2-core|/2⌋` does NOT persist at i. Would need a
  combinatorial valuation-minimal, uniquely-placed predecessor in the recursion;
  couldn't pin one uniformly. (Nice data point: staircase 4-core (4,3,2,1) gives
  `G=24(1+i)^5`, a pure prime power, v=11.)
- **Hermitian lower bound.** `ψ^m ψ̄^m = Ξ^m`, Ξ=h₂²+e₂²=s₄+s₃₁+2s₂₂+s₂₁₁+s₁⁴
  (Schur-positive, FULL support of parts of 4 — better than d=3's Θ!). Gives
  `0 ≤ ⟨s_ρ,Ξ^m⟩ = Σ c^ρ_{λμ} G_λ \bar G_μ` for ρ⊢4m, a nonneg Hermitian form. If some
  ρ had a *unique* LR halving ρ=λ+λ we'd isolate `|G_λ|²>0` and finish — but no such
  "primitively halvable" ρ seems to exist (ρ=2λ always has several halvings). The
  off-diagonal terms block it.

**My instinct:** the missing positivity lives in the even/pair-of-boxes Fock-space
formalism of the seed (`ψ^m=((1+i)/2)^m (p₁²−i p₂)^m` is a complex tau-type vector,
not positive). The Hermitian route feels closest — perhaps a *family* of ρ's whose
forms jointly pin every G_λ, rather than one isolating ρ.

— Clio
