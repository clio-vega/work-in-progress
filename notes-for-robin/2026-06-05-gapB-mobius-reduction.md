# Gap B (two-row d=4): the engine IS a scalar Möbius orbit — reduction of Lemma 1

**Date:** 2026-06-05 (prove session). **Status:** Lemma 1 NOT fully closed, but the
problem is recast much more cleanly and the gap is now a single, sharp analytic step.

Proof doc: `~/projects/proofs/2026-06-05-lemma1.tex` (compiles, 5pp).
Verification: `~/projects/scratch/2026-06-05-lemma1/verify.py` (exact Z[i], all pass).

## The one thing to take away

The whole `(N_l, P_l, Q_l)` engine for `f=u²+(1+i)u+1`, `r_l=[u^l]f^m` collapses to a
**scalar complex Möbius recurrence** for the consecutive-coefficient ratio
`ζ_l := r_{l-1}/r_l`:

    ζ_{l+1} = (l+1) / [ (m-l)(1+i) + (2m-l+1) ζ_l ],     ζ_1 = (1-i)/(2m).

Dictionary (all proved):  `μ_l = N_l/N_{l-1} = 1/|ζ_l|²`,  `s_l = Re ζ_l`,
`t_l = Q_l/N_l = -Im ζ_l`.  So:
- **The law** `Q_l>0`  ⟺  `Im ζ_l < 0`.
- **Lemma 1 (MU-UB)** `μ_l ≤ 1+3(2j+1)/(2m-3j)`  ⟺  `|ζ_l|² ≥ ρ_j² := (2m-3j)/(2m+3j+3)`,
  i.e. the orbit stays OUTSIDE a shrinking circle.  (j=m-l.)

This is the continued-fraction unrolling of the Z[i] 3-term recurrence; the orbit hugs
the circle `|ζ|=ρ_j` from outside with gap O(1/m²) at the top of the band.

## What I proved rigorously

1. **The reduction** (Thm 1) — new and clean.
2. **Necessity of a quantitative t-lower-bound** (Lemma+Cor): writing
   `c²μ_{l+1}=(a+bs)²+(a-bt)²` with `s²+t²=1/μ_l`, the function is *strictly decreasing in
   both μ and t*. Hence the sup over `t≥0` is at `t=0` = the chained CS majorant. So any
   bound using only μ-bounds + the qualitative law (t≥0) cannot beat that majorant, which
   overshoots U by O(1/m) relative to the slack. **⟹ Lemma 1 genuinely requires a
   quantitative lower bound `t_l ≥ T_j > 0`.** This finally explains *why* CS was circular.
3. **Conditional closure** (Thm 2): one explicit inequality (C1) gives Lemma 1 from lower
   envelopes (L_j,T_j); the whole law = four corner inequalities (C1)–(C4) for a box
   `[L_j,U_j]×[T_j,T̄_j]` mapping to the j-1 box. A finite, explicit design problem.
4. **Contraction** (Prop): along the orbit the (μ,t)-Jacobian has both eigenvalues
   |λ|<1 (complex pair), so the orbit is *attracting* and an invariant tube exists —
   but marginally, |λ|=1-Θ(1/m).
5. **Exact 2nd-order asymptotics** (Richardson-certified):
   `μ_l = 1 + 3(2j+1)/(2m) + (36j²+16j-1)/(8m²) + O(1/m³)`,
   `t_l = (2j+1)/(4m) - 3(2j+1)²/(16m²) + O(1/m³)`,
   slack `U_j - μ_l = (2j+1)/(8m²) + O(1/m³)`.

## The single remaining gap (sharp)

Make the contraction **effective**: prove `|λ_j| ≤ 1 - c_j/m`. Then the 2nd-order
expansions are provable sub/super-solutions (L_j,T_j,T̄_j accurate to 1/m²), and
(C1)–(C4) become explicit rational inequalities in (m,j). Leading-order envelopes fail
(C1) by ~4% (the historical "5% loss") because the slack is only O(1/m²) — you MUST be
2nd-order accurate.

## Concrete lead for the effective-contraction step

Since `ζ↦M_l(ζ)=c/(a(1+i)+bζ)` is a Möbius map (holomorphic), its contraction is
**conformal** with derivative modulus, evaluated on the orbit,
`|M_l'(ζ_l)| = cb/|a(1+i)+bζ_l|² = (b/c)/μ_{l+1}`.
On the band (j≥2) the orbit gives `(b/c)/μ_{l+1} = (m+j+1)/[(m-j+1)μ_{l+1}] ≈ 1-(2j-3)/(2m) < 1`.
So the map is a genuine *conformal contraction* in the ζ-plane. This is the natural
home for a Schwarz–Pick / hyperbolic-metric argument: "the orbit stays outside the circle
`|ζ|=ρ_j`" should follow from a self-map-of-a-disk picture if one can exhibit a disk family
`D_j` with `M_l(D_j)⊆D_{j-1}`, `D_j⊇{|ζ|≤ρ_j}^c∩(orbit nbhd)`. The (μ,t)-Jacobian
eigenvalues I measured (|λ|≈0.98) differ from |M_l'|² only by the nonconformal coordinate
change (p,q)↦(1/|ζ|²,-q), whose Jacobian det is 2p/|ζ|⁴ — all explicit. I think the clean
closing lemma is hyperbolic-geometric, not the brute box induction.

## Why I think this is the right frame

The law is *marginal*: in the leading-order θ-map (θ=arg ζ_l - π/4 essentially) the fixed
point sits exactly at the critical angle -π/4 (=the law's boundary). The orbit equilibrates
O(1/m) above it via subleading drift. So the law/Lemma 1 are inseparable at the same order,
and the proof is a (contracting but marginal) invariant-manifold / singular-perturbation
argument. The Möbius form is the natural language for it — Robin, if there's a slick
hyperbolic-geometry or continued-fraction convergence argument for "orbit stays outside
ρ_j", that closes everything. I couldn't find the clean effective-contraction lemma in the
session, but the reduction stands on its own.

— Clio
