# The order law's mechanism is clean: per-subset projector vanishing, with Catalan survivors

*2026-05-26 wake. Follows up [[for-robin/2026-05-23-uniform-rapidity-grade]]. Short version:
the grade law `ord_{x=q²} Z_λ = τ(τ+1)/2` is now over-determined by data, both of my earlier
proof leads are dead, and the real mechanism turned out to be the cleanest possible thing.*

## Recap (from 2026-05-23)

On the uniform-rapidity line of the corrected Baxterised staircase monodromy,
`Z_λ(x) = tr_{V^λ} M(x,…,x)`, with `(q+1)^N Z_λ(q²) = tr_{V^λ}(Ω)`. The binary dichotomy
`(x−q²) | num Z_λ ⟺ tr(Ω)=0 ⟺ τ≥1` is Diagnostic 2 (already proved). The *new* content is the
**order** of that zero: `ord_{x=q²} Z_λ = τ(τ+1)/2`, depending only on τ.

## What today's data session established

**1. The law is over-determined.** Verified on 13 shapes (was 6), τ up to 4 (order 10),
λ̂-independence confirmed across distinct ℓ(λ̂) at fixed τ (5 distinct λ̂ at τ=1, 3 at τ=2,
3 at τ=3). No mismatches. The formula is not in doubt.

**2. Both of my structural leads were wrong.**
- *Depth-weighted layer filtration* (I'd hoped the order splits as 1+2+···+τ over the
  Diagnostic-1 kernel layers): REFUTED. `num Z_λ` carries the order as ONE clean power
  `(x−q²)^{τ(τ+1)/2}`; the cofactor is irreducible and non-vanishing at q². Two τ=2 shapes share
  the exponent 3 but have coprime cofactors — the exponent is the τ-invariant, the cofactor is
  λ̂-noise. There's no polynomial-factor filtration to telescope over.
- *Recursive tail-cell factorization* (the lucky `num Z_{(2,1)} | num Z_{(2,1,1,1)}`): REFUTED as a
  pattern. Every consecutive peel-one-cell pair fails, including the direct extension
  `num Z_{(2,1,1,1)} ∤ num Z_{(2,1,1,1,1)}` and the whole `(3,1^m)` chain. Numerators don't nest.

**3. The real mechanism (and it's lovely).** Because `s := (q²−x)/(q(x−1))` is a Möbius local
isomorphism at `x=q²`, the order is computed at `s=0`:
```
   ord_{x=q²} Z_λ = ord_{s=0} P_λ(s),    P_λ(s) = tr_{V^λ} ∏_k ( PQ_{i_k} + s·PM_{i_k} ),
```
where `PQ_i=(T_i+1)/(q+1)`, `PM_i=(q−T_i)/(q+1)` are the two orthogonal eigenprojectors of `T_i`.
Expanding, `P_λ(s) = Σ_S s^{|S|} c_S`, with `c_S` the trace of the staircase product where I insert
the (−1)-projector `PM` at the word-positions in `S` and the q-projector `PQ` elsewhere. Grade `|S|`
counts (−1)-projector insertions; the grade-0 term is `tr(Ω)/(q+1)^N`.

**The verdict (hooks (2,1^m), m=2,3,4):**
```
   ord = min{ |S| : c_S ≠ 0 }    — pure minimal-support, ZERO cancellation.
```
Every `S` below the critical grade has `c_S = 0` *individually*; at the critical grade every
surviving `c_S` is *equal and positive* (= `q^{m+1}/(q+1)^{2m}`). So the order law is a **per-subset
vanishing statement** — "every small PM-subset has zero trace" — not a cancellation phenomenon. This
is the friendliest situation: I can attack it shape-by-shape with the sign-kill / leftmost-factor /
V±-projector / Hoefsmit-positivity machinery already in hand. (I'm checking right now whether the
no-cancellation picture survives off the hook locus — on (2,2,1,1,1), τ=2.)

**4. A multiplicity convergence I love.** The number of minimal-support subsets is `2, 5, 14` for
m=2,3,4 — **Catalan** `C_m`. That's the same Catalan count as my hook support lemma
(`|supp(B^μ)| = C_{k-1}`). The minimal PM-subsets cluster on the most-repeated generator i=1 and the
high single-occurrence generators, avoid i=2, and form contiguous "block-pairs" in the staircase
word. The equal-value-plus-Catalan-count is begging for a lattice-path / ballot bijection (the hook
leg is exactly a ballot path — cf. the hook transfer-chain work).

## Next

The next prove session is seeded around this: close the hooks (2,1^m) first — Part A the lower
bound (every PM-subset of size < C(m,2) has zero trace) and Part B the C_m equal-value survivors —
then deform off hooks to the general τ(τ+1)/2. If you want a single artifact, the connection note
`connections/2026-05-23-uniform-rapidity-lift.md` has the full table and the verdict.

(Ops note: Gmail's been locked ~8 sessions — it needs you to run `/mcp` and re-auth "claude.ai
Gmail" before I can send any of this by email. Until then these notes just pile up locally.)
