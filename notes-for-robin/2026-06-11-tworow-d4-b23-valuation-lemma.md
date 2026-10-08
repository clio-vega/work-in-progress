# For Robin — two-row d=4, b≡2,3: an exact valuation lemma (not yet a closure)

**11 June 2026, prove session.**

Honest headline first: I did **not** close the `b ≡ 2,3 (mod 4)` case, so the full two-row
d=4 law is still open. But I think I found the right way to *say* what's left, and it's clean.

## What I proved (Lemma A)

For `b ≡ 2,3 (mod 4)` and **every** integer `m`,
```
   v₂( I_b(m) ) = v₂(ℓ_b) + Σ_{r=0}^{R} v₂(m − r) + v₂(m − ρ_b),
```
where `R = ⌊(b−1)/2⌋`, `ℓ_b` is the (rational) leading coefficient of `Q_b`, and `ρ_b ∈ ℤ₂` is
the unique 2-adic root from the 06-09 work. The proof is short: factor `Q_b` over `ℂ₂`; the monic
model reduces mod 2 to `X·(X²+X+1)^{(d−1)/2}`, so every root other than `ρ_b` reduces into
`𝔽₄ ∖ 𝔽₂` and is therefore a unit that *no integer can be 2-adically close to* — its valuation
contribution is `0` for all `m`. So only `v₂(m − ρ_b)` survives.

## Why I think it's worth your time

For a week the file said "`v₂(I_b(m))` is unbounded, therefore no finite 2-adic truncation can
work, therefore go find central-trinomial congruences." Lemma A says the unboundedness was never
a pathology to be tamed — it's literally one algebraic root `ρ_b` lifting the valuation whenever
an integer `m` happens to approximate it 2-adically. The "spikes" of `v₂` sit exactly at the
integers nearest `ρ_b`. So:

- the obstruction is **one number**, `ρ_b`, and the law is the single statement `ρ_b ∉ ℤ_{≥b}`;
- there is **no 2-adic leverage left to find** beyond locating `ρ_b` — the central-trinomial
  congruence route (Route α in my brief) cannot give anything new, because the valuation is
  already given exactly. This is a negative I'm fairly confident about now.

It rests the same gap as the 06-09 single-candidate certificate on an *exact identity* rather than
a Newton-polygon estimate, which feels like the honest foundation.

## What's still in the way (unchanged target)

`ρ_b ∉ ℤ_{≥b}`, i.e. `Q_b` has no linear factor over `ℚ` — the parameter-versus-degree
irreducibility of the Gegenbauer-in-parameter family `g_b(m) = C_b^{(−m)}(−(1+i)/2)`. My brief
told me not to attack this head-on, and after today I agree: every 2-adic, single-prime,
covering-set and digit route is provably exhausted (`ρ_b ≡ 2 mod 16` is uniform but only four
bits; `mod 32` already splits). This is a genuine irreducibility wall and I suspect it needs a
tool from outside the 2-adic world — possibly the oscillatory `sinh·sin` form (the real roots of
`Q_b` are Chebyshev-spread, so "is a root an integer" smells transcendental), or a global
Galois/Newton-above-several-primes argument. I'd value your read on whether that family's
irreducibility is reachable, or known.

One small structural bonus: `Q_b(b − 1/2)` is a **unit fraction** `±1/N_b` for `b ≡ 2,3`, and an
**exact root** for `4 ∣ b`. So the `b mod 4` split in all our proofs is really one fact: the
half-integer `b − 1/2` is a genuine root of `Q_b` exactly when `4 ∣ b`.

Proof write-up: `projects/proofs/2026-06-11-tworow-d4-b23-valuation-concentration.md`.
Verified `b ≤ 80` (factorisation + Lemma A), `b ≤ 59` (`ρ_b ≡ 2 mod 16`).

— Clio
