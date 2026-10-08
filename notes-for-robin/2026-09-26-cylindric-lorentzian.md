# Q255: normalized cylindric skew Schur polynomials are Lorentzian — two cases closed

**2026-09-26, prove session c1.** Paper: `proofs/2026-09-26-c1-cylindric-lorentzian.tex` (10pp, compiles).
Registry: `proofs/registry/cylindric-lorentzian.json` (new, `in-progress`, validator clean).

## The short version

The question was whether `N(s^c_{λ/μ}(x_1..x_ℓ)) = Σ (K^c_α/α!) x^α` is Lorentzian. (L1) is free and
(L2) I already had (proved + Lean), so the whole question was the Hessian condition (L3). I ran the
falsifier first: **3647 instances, 1899 winding (52.1%), zero failures.** Then I proved two cases in
full and killed four routes.

**Proved.**
1. *Product form.* If `K_γ = Π_t f_t(γ_t)` with each `f_t` log-concave on an interval, then `N` is
   Lorentzian — because the Hessian is `P·uu^T` minus a nonnegative diagonal, so `λ₂ ≤ 0` by Weyl.
2. *`m = 1`, every `n`, `ℓ`, `d`*, since for one bead `K^c_α = Π_t 1_{[0,n-1]}(α_t)` exactly.
3. *`ℓ = 2`, every cylindric skew shape, every `m` and `n`.* This is the one I'm pleased with. At
   `ℓ=2` the constraints on the single intermediate shape **decouple** — `κ_i` is confined to
   `[max(μ_i, λ_{i-1}+1), min(λ_i, μ_{i+1}−1)]`, one interval per bead, and *no constraint couples two
   beads*; the interlacing and the wrap `κ_m < κ_1 + n` come out automatically. So the coefficient
   sequence is a convolution of interval indicators, hence log-concave with no internal zeros, and (L3)
   in two variables is exactly that log-concavity.

I proved "PF₂ is closed under convolution" (Hoggar's theorem) rather than cite it: `T(f*g) = T(f)T(g)`
for Toeplitz matrices, and Cauchy–Binet makes each 2×2 minor of a product a sum of products of pairs of
2×2 minors. Two lines, and it keeps the paper free of an uncited load-bearing step.

## What I got wrong, and would like you to check

**My intended proof skeleton was false.** I went in expecting "(L2) + pairwise root log-concavity ⟹
(L3)", with the pairwise half coming from a bead-hop injection. It fails as *linear algebra*:

    M = [[4,6,4],[6,1,4],[4,4,4]]

has strictly positive entries, satisfies `M_ij² ≥ M_ii M_jj` for every `i≠j` (36≥4, 16≥16, 16≥4), and
has **two** positive eigenvalues. So exchange-type inequalities — which is what sign-reversing
involutions give — cannot reach (L3) however many of them you prove. Two strengthenings (a Monge
condition; total nonpositivity of order 2) fail on the *actual* Hessians, so they aren't the mechanism
either.

**The Schur route is shut for a second reason I hadn't seen.** I knew `s^c` can have negative Schur
coefficients. But even in Postnikov's positive range the reduction to HMMS Thm 3 is invalid, because
**Lorentzian polynomials are not closed under addition**: `(x+y)²` and `(2x+y)²` are each Lorentzian and
their sum has a rank-2 PSD Hessian. My brief had the first reason and would have left the positive
regime looking open. Worth a sanity check from you — it is the kind of thing that is obvious once
stated and easy to have backwards.

## The gap, stated precisely

**`ℓ ≥ 3` and `m ≥ 2`**, and the reason is structural rather than technical. For a chain of length
`ℓ ≥ 3` the strip condition `κ^{t+1}_i < κ^t_{i+1}` makes bead `i` at time `t+1` depend on bead `i+1`
at time `t`, so consecutive *interior* layers couple. That coupling is absent at `ℓ=2` (only one
interior layer) and absent at `m=1` (`i+1 ≡ i`) — which is exactly why those are the two cases I could
close, and it says the two proofs are not accidents.

Constraints on any future certificate, measured not guessed:
- it must see ≥ 3 indices at once (above);
- it must be **exact**: among 2238 Hessians from winding `m≥2` instances, `λ₂ = 0` *exactly* in
  **73.1%**. The conjecture, if true, sits on the boundary of the Lorentzian cone three times in four,
  so no argument with slack can work;
- the product-form certificate (off-diagonal part rank one) covers 77.2% and fails on 22.8%. I want to
  be careful here: a `rank-one minus PSD` decomposition always *exists* when `λ₂ ≤ 0`, so that 22.8%
  bounds the reach of *that* certificate and is **not** evidence that no certificate exists. I am not
  claiming an obstruction.

## One thing I'd like you to act on

`sources.json` had Brändén–Huh **`1902.03719` graded `deep-read` while its own note read "POINTER ONLY
… never checked at source … Not read."** I corrected the grade to `agent-summary`. That is not
bookkeeping — it decided what this paper could be. Every attractive remaining route to the general case
(realizing `N(s^c)` as a volume polynomial; transporting Lorentzianity along a nonnegative linear
substitution; the Ehrhart route through polynomiality of stretched cylindric Kostka coefficients in
2311.07382) needs a Brändén–Huh closure theorem, and I am not allowed to lean on a paper I have not
read. **Reading `1902.03719` at source is the single highest-value next step for this programme** —
higher than another proof attempt.

Also: my own exact eigenvalue counter was wrong on first writing (mis-indexed Faddeev–LeVerrier). Its
hand controls caught it before it touched any mathematics, which is the argument for writing the
controls first.

— Clio
