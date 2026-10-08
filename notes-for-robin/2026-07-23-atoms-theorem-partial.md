# 2026-07-23 · Atoms decomposition of P_μ — partial theorem shipped

Robin,

3h prove session on the atom decomposition of ordinary HL P_μ via θ^alt +
Cherednik–Ram. Shipped as `~/projects/proofs/2026-07-23-atoms-decomposition-P-mu.tex`
(8pp, compiles clean). Verdict: **partial success** — main structural
ingredients proved cleanly, but one V_{<μ} consistency lemma remains
open for a fully general proof. Numerically verified 10+ cases at n=3.

## What's proved

1. **Key Identity (KI)**: `T_i = (1+t) s_i − θ^alt_i − id` on ℚ(t)[x_1,…,x_n].
   This is the technical crux, ties Cherednik–Ram operators (Demazure–Lusztig,
   Hecke) to atom operators (Mason-t-deformed) via a simple 3-term identity.
   Proof is 3 lines of algebra.

2. **Formula for T_i on ascending monomials**: for ν_i < ν_{i+1},
   `T_i(x^ν) = x^{s_i ν} + (1−t) · Σ intermediate monomials`,
   with the intermediates having strictly smaller partition shape.
   Corollary: T_i eigenvalue is t on x^ν when ν_i = ν_{i+1}.

3. **Parabolic factorization**:
   `P_μ = Σ_{v ∈ W^μ} T_v(x^{μ̄})`
   where W^μ = min coset reps of S_n / stab(μ̄). Follows from CR
   (Demazure-basics, 21/21 verified) + the ν_i=ν_{i+1} eigenvalue in (2).

4. **Atom triangularity in dominance**: A^alt_γ has x^γ as leading orbit
   monomial (coeff 1), other orbit monomials strictly upper in dominance,
   and non-orbit monomials of strictly smaller partition shape.

## What's the gap

The residual `R := P_μ − Σ c_γ A^alt_γ` has zero V_μ-part by construction
(triangular back-substitution). It's therefore supported in shape-<μ.
For R = 0 exactly (not just modulo lower shapes), we need a **V_{<μ}
consistency lemma**: the shape-<μ contributions of the atoms A^alt_γ
(with the c_γ from V_μ back-sub) must match the shape-<μ contributions
of P_μ from Macdonald III.(2.4).

Verified computationally for μ ∈ {(2,0), (2,1,0), (2,2,0), (3,0,0),
(3,1,0), (2,1,1), (2,2,1), (3,2,0), (3,3,0), (2,2,1), (3,2,1), (3,1,1)}
at n ≤ 3. In every case the shape-<μ equations hold automatically.

For a general proof, the natural strategy is to trace through the
parabolic factorization Σ_v T_v(x^{μ̄}) using KI + the ascending-T_i
formula (2), and show the intermediate contributions from each v
combine to match the intermediate contributions from each atom
A^alt_{v·μ̄}. That's a bookkeeping argument I didn't complete in this
cycle.

## Consequences (if fully proved)

- c_γ ∈ ℤ_≥0[t] positivity (conjectured, verified numerically as products
  of Gaussian [k]_t factors) would close the atoms route base case for
  the cylindric HL sprint.
- 07-30 interior identity `M^{(c)}_μ = v_μ · P_μ` (interior μ) + this
  atom expansion of P_μ = atom expansion of M^{(c)}_μ interior, matching
  Probe B 07-22 bis numerical data.

## What I want you to look at

1. **Is the V_{<μ} consistency lemma easy?** I have a hunch it follows
   from a careful accounting of "intermediate paths" in the parabolic
   sum, but I couldn't close it. Some third eye would help. Maybe Rick?

2. **Is there a slick alternative proof?** For instance via elliptic
   Hall, geometric Satake, or Kirillov's t-analogs of Kostant partition
   functions? The pattern c_γ = product of Gaussians strongly suggests
   a "graded character of a Bruhat cell/subquotient" reading.

3. **Positivity conjecture**: c_γ ∈ ℤ_≥0[t] (as products of Gaussians)
   is a specific candidate for a Blasiak–Haiman–Morse–Pun–Seelinger-style
   corollary. If you know a fast way to compare to their 2509.24040 setup,
   worth knowing.

## Files

- Proof: `~/projects/proofs/2026-07-23-atoms-decomposition-P-mu.tex` (+ .pdf)
- Scratch: `~/projects/scratch/prove-2026-07-23-atoms-decomposition.md`
- Verification: `~/projects/scratch/verify_KI.py`
- Probe B anchor: `~/projects/probes/2026-07-22-atoms-probe-B/RESULTS.md`
- CR verification: `~/projects/proofs/2026-07-20-demazure-reentry-cherednik-ram.pdf`

--Clio
