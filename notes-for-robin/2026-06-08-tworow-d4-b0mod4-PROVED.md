# Two-row d=4 law CLOSED for b ≡ 0 (mod 4) — half of all b now done

**2026-06-08 prove session.** Robin —

Last cycle I proved the two-row d=4 fiber law `G_{(2m−b,b)}(i)=0 ⟺ (2,2)` for all
`b ≡ 1 (mod 4)`. **Today I closed `b ≡ 0 (mod 4)`.** Together: the law holds
unconditionally for the **full residue classes `b ≡ 0,1 (mod 4)` — half of all b**,
infinitely many, not just verified-up-to-some-bound.

## What's proved
The exact 2-adic identity **(V)**: `v₂(I_b(m)) = v₂((m)_{R+1}) − v₂(R!)` for every integer
`m`, where `R = (b−2)/2` and `I_b(m) = Im G_{(2m−b,b)}`. (V) makes `v₂(Q_b(m))` a constant
`−v₂(R!)`, so `Q_b(m) ≠ 0` — the law.

## The one idea worth remembering
For `b ≡ 1`, the `j=1` term of the binomial expansion `I_b = Σ τ_j` *strictly* dominates in
2-adic valuation — one minimal term, and it's odd, done. For `b ≡ 0` that fails: `R+1 = b/2`
is even, which lowers the offsets, and **for odd `m` the terms `j=2` and `j=3` tie `τ_1`**.
The fix is not domination but **parity counting**: I show (Lemmas) that the *only* terms
ever attaining the minimal valuation are `j ∈ {1,2,3}`, that they tie iff `m` is odd, and so
the number of minimal terms is always odd — **1** (even `m`) or **3** (odd `m`). Three odd
numbers sum to an odd number, so `I_b/2^{v₂(τ_1)}` stays odd and the valuation is pinned.

The structural pivot is that `4 | b ⟹ R = 2t−1` is **odd**, which is exactly what forces
both offsets `D₀(2) = D₀(3) = 0` and pins the tie to the parity of `m`. The clean closed form
`D₀(j odd) = v₂(C(R,⌊j/2⌋))`, `D₀(j even) = v₂(C(R,⌊j/2⌋−1)) − v₂(⌊j/2⌋)`, and the fact that
`h` consecutive integers are divisible by `h!`, are the whole engine.

## Files
- `projects/proofs/2026-06-08-tworow-d4-b0mod4-proved.{tex,md}` (tex compiles, 4 pp).
- `projects/scratch/2026-06-08-prove/verify.py` — 24,480 exact term-level checks
  (`b ≤ 64`, random `m ≤ 10⁶`) + boundary/forced-root checks, 0 problems.

## What's left
`b ≡ 2,3 (mod 4)` only. The 2-adic method is **structurally dead** there: `q_b` acquires a
genuine root mod 2 (`q_b ≡ m·(m²+m+1)^k mod 2`), so I need an **odd prime** —
Filaseta-style Newton-polygon non-vanishing, or a uniform-in-`b` irreducibility / non-square
discriminant argument. The CODE phase has been tabulating per-`b` root-free odd primes; that's
the natural next prove target. A uniform "disc(q_b) non-square ⟹ no rational root" would close
all classes at once.
