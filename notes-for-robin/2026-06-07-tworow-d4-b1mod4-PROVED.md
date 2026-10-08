# Two-row d=4 law PROVED for an infinite family (b ≡ 1 mod 4)

**Date:** 2026-06-07 (prove session)
**TL;DR:** The two-row case of the d=4 fiber-vanishing law `G_{(2m−b,b)}(i)=0 ⟺ (2,2)` is
now **proved outright for all `b ≡ 1 (mod 4)`** (infinitely many `b`; before today we only
had `b ≤ 24` by direct factorization). The mechanism is a clean **2-adic valuation identity**.
The case `b ≡ 0 (mod 4)` is reduced to one short mod-4 lemma (verified `b ≤ 40`). The cases
`b ≡ 2,3 (mod 4)` are shown to need a genuinely different prime.

## The idea in one breath
The last cycle reduced everything to `(♦)`: an explicit integer polynomial `Q_b(m)` has no
integer root `m ≥ b`, and concluded the 2-adic route was dead because `v₂(I_b(m))` is
*unbounded*. The new insight: **that unboundedness lives entirely in the forced product
`∏_{r=0}^{R}(m−r)` (`R=⌊(b−1)/2⌋`) that we already divided out.** The quotient `Q_b` is a
2-adic *unit* of constant valuation. Precisely, for `b ≡ 1 (mod 4)`:
```
        v₂(I_b(m)) = v₂(∏_{r=0}^{R}(m−r)) − v₂(R!)      for ALL integers m.
```
Both sides finite for `m ≥ b` ⟹ `I_b(m) ≠ 0` ⟹ the law. Equivalently `Q_b(m)` is always odd,
i.e. `q_b ≡ (m²+m+1)^{⌊(b−1)/4⌋} (mod 2)`, which has no root mod 2.

## How it's proved (honest)
Exact binomial expansion `I_b(m) = Σ_{j=1}^{b} τ_j(m)` from splitting `1+su+u² = (1+u²)+su`,
`s=1+i`. The only term with an **odd** coefficient `Im((1+i)^j)` is `j=1`, and that term is
*exactly* `(m)_{R+1}/R!`. For every `j ≥ 2` a Vandermonde identity + a telescoping product
gives `v₂(τ_j) − v₂(τ_1) = D_j + Σ_t v₂(m−R−t)` with the **m-independent**
`D_j = v₂(h+1) + v₂(C(R+1,h+1)) ≥ 0` (`h=⌊j/2⌋`). When `D_j=0` it forces `j ≡ 1 (mod 4)`,
`j ≥ 5`, where the sum `Σ_t v₂(m−R−t) ≥ 1` (a window of ≥2 consecutive integers has an even
one). So every `j ≥ 2` term has strictly larger `v₂` than `τ_1`; `τ_1` dictates `v₂(I_b)`. ∎

This needs `R+1 = (b+1)/2` **odd**, which is exactly `b ≡ 1 (mod 4)`. For `b ≡ 0 (mod 4)`,
`R+1 = b/2` is even, the terms only *tie*, and one needs a mod-4 refinement (stated, verified,
left open). For `b ≡ 2,3 (mod 4)`, `q_b ≡ m·(m²+m+1)^k (mod 2)` genuinely has the root
`m ≡ 0`, so the 2-adic certificate is *unavailable* — those need an odd-prime Newton-polygon /
irreducibility argument (the Filaseta route).

## Files
- Proof: `~/projects/proofs/2026-06-07-tworow-d4-b1mod4-proved.md` (full), `.tex`/`.pdf` (compiles).
- Scripts: `~/projects/scratch/2026-06-07-prove/` (`verify_Dj.py` is the key check — the
  exact decomposition + strict domination over random `m ≤ 10⁵`, all `b ≡ 1 (mod 4)` to 41).

## What I'd value your eyes on
1. The `b ≡ 0 (mod 4)` mod-4 lemma — it should be a finite/clean cancellation count; I ran out
   of session to nail it but it's verified solidly. Worth a Lean formalisation of the
   `b ≡ 1` theorem too (the valuation argument is very mechanical).
2. The `b ≡ 2,3` classes are the real open frontier now — and they are exactly the
   "imaginary-axis" hard cases. Newton-polygon at an odd prime is the named tool.
