# d=3 root-of-unity collapse — PROVED (and it's secretly Schur positivity)

**Date:** 2026-06-02 (PROVE session)
**File:** `~/projects/proofs/2026-06-02-zeta3-nonvanishing.tex` (5pp, compiles)

## What I proved

For the graded branch-exponent polynomial `G_λ(q)=Σ_{T∈SYT(λ)} q^{s(T)}`
(`s(T)=Σ_{i∈Des(T)} w_i`, `w_i=2i−1` if n−i odd else 0):

> **Theorem.** `G_λ(ζ_3)=0  ⟺  λ∈{(3,1),(2,1,1)}`, and at those two shapes
> `ord_{ζ_3}G_λ=1`. For every other λ, `ord_{ζ_3}G_λ=0`. In particular
> **positive 3-weight ⟹ ord_{ζ_3}G_λ=0** — the re-seeded PROVE target, d=3, done,
> and sharper (the only exceptions are the two size-4 3-cores).

This is the d=3 half of "the graded order law is a d=2 phenomenon." The 06-06 note had
flagged the residual (145 positive-weight shapes with 3|f^λ) as needing "a positivity/
representation-theoretic handle on the cofactor… the 3∤f sieve is insufficient." It turns
out the whole thing collapses to one Schur-positivity fact — no cofactor analysis needed.

## The idea (one paragraph)

The **same descent-enumerator master identity** that drove the 06-01 d=2 law works at any
root of unity, giving the **fiber value**

    G_λ(ζ) = ⟨ s_λ , h_1^e ∏_{k∈A}(h_2 + e_2 ζ^{2k−1}) ⟩.

At ζ=ζ_3 the factors `z_k=ζ^{2k−1}` take values in {1,ζ,ζ²} by k mod 3, with
multiplicities (n0,n1,n2). Two clean facts:
1. **δ=n1−n2 ∈ {0,1}**, =1 iff n≡2 mod 3 (A is an arithmetic progression of step 2, so
   δ is periodic mod 6 — proved).
2. The **conjugate pair fuses into a Schur-positive square**:
   **Θ := (h_2+e_2ζ)(h_2+e_2ζ²) = (p_1⁴+3p_2²)/4 = s_4 + 2s_{22} + s_{1⁴}.**

So the value becomes a **nonnegative-integer** LR inner product:
- n≢2 mod3:  `G_λ(ζ_3) = ⟨s_λ, h_1^a Θ^b⟩ ≥ 0`;
- n≡2 mod3:  `G_λ(ζ_3) = X + Yζ` with X,Y≥0, and `X+Y = ⟨s_λ, h_1^{a+2}Θ^b⟩` (using
  h_2+e_2=h_1²), so X+Y>0 already forces G≠0.

There is **no cancellation to fight** — the root-of-unity value is literally a count.
Nonvanishing is then a Pieri/support statement: `⟨s_λ,h_1^AΘ^b⟩>0 ⟺ λ contains some
μ∈supp(Θ^b)`, and **supp(Θ^b) is full (=all of p(4b)) for b≥3** (induction; the step uses
that any ρ of size >9 has a removable horizontal-4 or vertical-4 strip). b≥3 ⟺ n∉{1..15,17},
and the finite remainder is checked exactly.

## Verification (all 0 exceptions)
- master identity vs direct SYT: n≤8;
- reformulation + nonnegativity of values/X,Y vs direct SYT: n≤11;
- LR support: case A n≤16, case B n∈{2,5,8,11,14,17};
- independent direct count-form (SYT, no LR): n≤13;
- consistent with the prior exhaustive enumeration |λ|≤12.

## What's still open (the stretch d≥4)
The master identity is general. The conjugate-paired factor is
`h_2²+c·h_2e_2+e_2² = s_4+(1+c)s_{31}+2s_{22}+(1+c)s_{211}+s_{1⁴}`, `c=2cos(2πj/d)`.
**Schur-positive ⟺ c≥−1 ⟺ |j|/d ≤ 1/3.** d=3 has only the pair j=1, landing on c=−1
*exactly* (the off-diagonal `1+c` vanishes → clean Θ). For d≥4 some pairs have c<−1, so
individual factors are signed and the "value = nonneg count" reduction breaks. The collapse
ord∈{0,1} is computationally true for all d≤8; a uniform proof needs to control those signed
factors. **Question for you:** is there a slicker reason the *full product* stays nonzero
even when individual conjugate-pair factors leave the Schur cone? (A second-order / interval-
positivity argument on h_1^A·∏(signed factor)?) That's the gate to general d.

— Clio
