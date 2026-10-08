# For Robin — 2026-09-29 PROVE: Q255 at ℓ=3 reduced to two inequalities

**Artifact:** https://github.com/clio-vega/proofs/blob/main/2026-09-29-c1-cylindric-lorentzian-ell3.tex
(PDF beside it; commit `f5295ff`.)

I did **not** prove (L3) at ℓ=3. I reduced it, proved the reduction, and the gap that is
left is now one sentence long instead of a regime.

## The shape of it

At ℓ=3 the Hessian `M_ij = K^c_{β+e_i+e_j}` is a 3×3 nonnegative symmetric matrix, so
"at most one positive eigenvalue" is equivalent to `e_2(M) ≤ 0` **and** `det M ≥ 0`. The
first is exactly the sum of the three raw RLC quantities, which have never failed here.
**So the whole open content of (L3) at ℓ=3 is a determinant sign.**

Then the new piece. Add to RLC — call it (A) — the three-index condition

  (B)  `M_ik M_kj ≥ M_ij M_kk`   (i,j,k distinct).

**Lemma.** (A)+(B) ⟹ at most one positive eigenvalue. Proved, elementary, half a page.
The identity is `det M = P + 2t − x − y − z` with `xyz = P t²`, where `P` is the product
of the diagonal, `t` the product of the off-diagonal, and `x = M₁₁M₂₃²` and cyclic. (B)
multiplied through says precisely `x, y, z ≤ t`, so for `t > 0`

  `det M = t · g(x/t, y/t, z/t)`,   `g(ξ,η,ζ) = ξηζ − ξ − η − ζ + 2`,

and `g` is **multilinear**, hence minimised at a vertex of the cube, where it takes
values 2, 1, 0, 0. Equality `det M = 0` iff two of the three (B) consequences are tight —
that matches all 3921 Hessians in the small range, and it explains the 65.6% of exactly
singular Hessians that had been sitting in my data unexplained.

Nothing from Brändén–Huh is used anywhere in the note; that entry is still
`agent-summary` and I kept my hands off it.

## The part I think is worth your attention

**(B) is exactly what my own recorded dead end was missing, and the dead end's witness
said so.** The node `rlc-implies-l3` has been `dead-end` since 09-26 with the witness

  `[[4,6,4],[6,1,4],[4,4,4]]` — all three 2×2 conditions hold, two positive eigenvalues.

That witness **satisfies (A) and violates (B)**: `M₁₃M₃₂ = 16 < 24 = M₁₂M₃₃`. In the
normalised form `N_ij = M_ij/√(M_ii M_jj)` the triple is `(3,1,2)` and the triangle
inequality `N₁₂ ≤ N₁₃N₂₃` fails by one.

I had that counterexample in my own registry for three days and read it as a closed door.
It was a specification. I have written that up as a memory.

## Scope — because I have been caught by unscoped reasons before

(A)+(B) say exactly that `φ_ij = log(M_ij/√(M_ii M_jj))` is a **pseudometric**. On
`{Σx_i = 0}` the form becomes `Σ_{i≠j}(e^{φ_ij} − 1)x_i x_j`, so the criterion really
asks for `e^φ − 1` to be of **negative type** — and not every metric is. The `K_{2,3}`
shortest-path metric at ℓ=5 satisfies (A) and (B) and has **two** positive eigenvalues
(spectrum −6.389 ×3, +4.469, +19.698). At ℓ=4 a random search found 777 such matrices in
4012.

So the criterion is strictly a 3×3 phenomenon. That does **not** refute (L3) at ℓ≥4 — the
cylindric pseudometrics may all be of negative type, and (A),(B) held without exception on
143375 Hessians at ℓ=4,5,6. It says only that this mechanism stops at 3. It is also the
first time I have had a *reason* for why ℓ=3 was the right target rather than just a hunch
that it was the smallest coupled case.

## What is left, precisely

Two statements about `k(a,b) = K^c_{(a,b,d−a−b)}`:

  (A) `k(a,b)² ≥ k(a+1,b)k(a−1,b)`            [log-concave in a]
  (B) `k(a+1,b)k(a,b+1) ≥ k(a,b)k(a+1,b+1)`   [log-submodular]

Verified on 220658 Hessians, zero failures, exact integer arithmetic throughout (integer
characteristic polynomial + Descartes; no float eigenvalues anywhere).

I got a genuine chunk of (B). Unfolding the horizontal-strip condition gives a clean
model: `K^c` at ℓ=3 counts pairs `(κ,σ)` with `κ_i ≤ σ_i ≤ κ_{i+1}−1` cyclically inside
boxes — a single cyclic interlacing chain (checked against the transfer-matrix DP,
911/911). Fixing κ, the σ_i decouple, so `P(u,v) = Σ_{S_κ=u} W_κ(v)` with each `W_κ` a
convolution of interval indicators. I proved that convolution preserves the likelihood
ratio order for PF₂ sequences (nice antisymmetric-pairing proof, tested 97289 quadruples,
negative control fails 99/484 so the PF₂ hypothesis is load-bearing), hence `W_κ ≼ W_κ'`
whenever `κ ≤ κ'` coordinatewise. That gives (B) whenever the admissible inner shapes form
a **chain** — in particular m=1.

**And then it stops, for a reason I can state exactly.** The obvious strengthening —
`S_κ < S_κ'` ⟹ `W_κ ≼ W_κ'` — is **false**, at 42% (692 of 1652 incomparable pairs).
Smallest witness: n=5, m=2, μ=(0,2), λ=(1,5), κ=(1,2), κ'=(0,4); `W_κ` is the indicator of
{3,4,5,6} and `W_κ'` the indicator of {5}. Yet the **fibre sums** do satisfy the order,
327/327.

> The missing step is a cancellation across an **antichain**, not a pointwise comparison.
> No argument that compares individual inner shapes can close it.

Ahlswede–Daykin is the natural tool and does not apply: `(S_κ, S_σ)` is modular on the
interlacing sublattice but is not a lattice homomorphism, since `Σ_i max(κ_i, κ'_i)` strictly
exceeds `max(S_κ, S_κ')` in general.

If you know the right machine for "log-supermodularity of fibre counts of a linear map on a
distributive lattice when the map is modular but not a homomorphism", that is the whole
remaining problem. I suspect it is known to somebody in the FKG/Karlin lineage.

## Housekeeping

- Registry `cylindric-lorentzian.json` updated: 5 new proved nodes, 2 new dead-ends with
  reasons **and the scope of each reason**, 2 open conjectures at `computed`. trustcheck
  validates; I watched the boundary rule actually **refuse** a promotion of
  `ell3-coupling-gap` before recording that it holds.
- One correction to the brief you may want for the next one: it pinned HEAD at `603ffd1`,
  which is real but is now HEAD's *parent* — a later commit landed after the brief was
  written. True when written, stale on arrival. I checked with `git rev-parse` rather than
  trusting it.

— Clio
