# Condition (A) at ℓ=3: reformulated for all m, settled at m=2 in the single-region case

**2026-09-30 c1 prove session.** Paper: `proofs/2026-09-30-c1-cylindric-kostka-logconcavity.tex`
(9pp, compiles). Registry: `proofs/registry/cylindric-lorentzian.json`, validated — and I watched
the boundary gate refuse a planted violation before recording that it passes.

---

## The one thing to take away

Condition (A) — `k(a,b)² ≥ k(a+1,b)k(a-1,b)` for cylindric Kostka numbers at ℓ=3 — is **not** a
statement about a three-step chain. For **every** m,

> `k(a,b) = k(b,a) = Σ_{ν ∈ Box(μ), S_ν = |μ|+b} f_ν(a)`

where `Box(μ) = ∏_i [μ_i, μ_{i+1}-1]` is a genuine box (the `μ ≺ ν` constraints decouple per bead,
and cylindricity is automatic), and `f_ν` is the **ℓ=2** cylindric Kostka sequence of `λ/ν` — which
is **PF₂** by `ell2-all-m`, already proved.

So (A) reads: *a sum of PF₂ sequences over one slice of a box is log-concave.* One parameter, and
the summands are objects we already understand. I think this is the right way to hold the problem,
and it is what made the rest of the session possible.

## What I proved

At **m=2** the slice is one-dimensional. The four interval endpoints
`a_t=max(t,A), b_t=min(u-1-t,B), c_t=max(u-t,C), d_t=min(t+n-1,D)` (with `A=λ₂-n+1, B=λ₁, C=B+1,
D=λ₂`) share only **two** breakpoints — `τ₁ = λ₂-n+1` and `τ₂ = u-1-λ₁` — because `D-n+1 = A` and
`u-C = u-1-B`. That is the structural accident the whole m=2 analysis turns on. It splits the
t-range into ≤4 regions, and each region's contribution is PF₂ by one of two mechanisms:

- **Regions I, III:** one of the two intervals is *constant in t*, so `G_I = 1_{[A,B]} * w_I` with
  `w_I` the positive part of a concave function. PF₂, then `pf2-convolution`.
- **Regions II, IV:** `a_t+c_t` and `b_t+d_t` are *both constant*, so every trapezoid has the same
  support and `G_R(s) = ρ_R(H(s))` with `H` a concave tent and `ρ_R` concave nondecreasing. Hence
  `G_R` is **concave**, hence PF₂.

**Theorem.** If the t-range lies in a single cell — explicit inequalities in `T_±, τ₁, τ₂` —
then (A) holds. Criterion verified correct on 5187/5187 slices; **4147 (79.9%) qualify.**

## The gap — one inequality, and I can tell you what it is not

`2 G_R(s)G_R'(s) ≥ G_R(s-1)G_R'(s+1) + G_R(s+1)G_R'(s-1)` between **distinct** regions. Given it,
symmetrisation closes (A) at m=2 outright. **Verified 525/525 region pairs. Unproved.**

What makes it hard, precisely: it cannot follow from any comparison between individual slice
members, because that same inequality already *fails* there — n=6, μ=(0,3), λ=(4,5), slice S_ν=5,
`f_{(0,5)} = 1_{[0,4]}` against `f_{(2,3)} = δ₂`; their sum `(1,1,2,1,1)` is not log-concave, and it
is repaired only by the third slice member `(1,4)`. The slice is a genuine antichain — the same
obstruction the registry already records for condition (B). **Term-by-term fails; region-by-region
works.** The grouping is the content.

## A near-miss I want on the record

`k(·,b)` is **concave** on all 905 instances with n≤6, d≤7. It is **false**: 1758 failures in 96781
interior points once I pushed to n≤9, with a witness at m=2 — `(1,3,6,7,6,3,1)`, n=8, μ=(0,3),
λ=(4,7), b=2. Log-concavity failed 0/96781. I came close to recording a small-case artifact as a
theorem; what caught it was extending the sweep past the range the statement was born in.

This is also a *positive* signal: regions II/IV are proved by a concavity argument, and concavity is
false in general, so that argument **provably cannot** extend to the multi-region case. The gap is
where it has to be.

## Brändén–Huh — the four-day blocker is closed, and two of my beliefs were wrong

Read at source, cited by internal `\label` + line number.

- **Lorentzian IS closed under products** (`\label{CorollaryProduct}`, l.1758). My own brief
  explicitly disclaimed knowing this. Also `N(f),N(g)` Lorentzian ⇒ `N(fg)` Lorentzian.
- **There is no characterisation of Lorentzian polynomials as limits of volume polynomials.** That
  was Question `\label{RealizationQuestion}`, answered *negatively* in an added-in-proof footnote.
  So the Ehrhart/volume route is **closed** — this retracts the "re-opened as a candidate" line in
  my own 09-30 WAKE block from that morning.
- Closure under **addition** is never addressed in the paper (it is false; witness already in the
  registry). `\label{flow}` (nonneg linear substitution) and `\label{derivatives}` are as hoped.
- The paper proves **nothing** about Schur polynomials.

**None of it shortcuts (A).** Getting `h_b = [y^b]s^c` via `∂_y^b` then `y=0` would be legitimate,
but presupposes `N(s^c)` Lorentzian — the whole conjecture.

**But it opens a new route to the main conjecture, which I did not pursue:**
`\label{normalizedcoefficients}` (l.2853) — if `log c_α` is M-concave then the normalised polynomial
is Lorentzian — has a **local** form needing only `|α-β|₁ = 4`, valid whenever the support is
M-convex, which is exactly (L2), already proved. At ℓ=3 the case `α-β = (2,-2,0)` of that local
axiom **is** condition (A); the cases `(2,-1,-1)` and `(1,1,-2)` are mixed conditions I have not yet
matched against (A) or (B). Filed as `m-concavity-via-normalizedcoefficients`, `unclassified`
pending Murota at source (that entry is label-keyed with no arXiv id, so invisible to every
ID-keyed check I own).

## Question for you

The gap is a statement about four explicit one-parameter families of trapezoid sums with nested
supports. It smells like something with a name — a cross-covariogram of two lattice-convex sets
along one direction, or a discrete Prékopa statement for a function that is a truncated concave
function on ℤ². I deliberately did not go reading for it this session. If you recognise the shape,
that is probably a shortcut.

## Scope, stated flatly

- (A) at **m ≥ 3**: open beyond the reformulation. The slice is (m-1)-dimensional and neither the
  m=2 reduction nor the region decomposition survives. Nothing in the proofs suggests an
  m-independent form.
- (A) does **not** settle (L3), even at ℓ=3. By `l3-det-reduction`, (L3) at ℓ=3 needs `e₂(M) ≤ 0`
  **and** `det M ≥ 0`; (A) gives only the first. The second is condition (B).
