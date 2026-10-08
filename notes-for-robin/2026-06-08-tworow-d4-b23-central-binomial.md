# For Robin — 2026-06-08: a pretty fact, and a course correction (b ≡ 2,3 mod 4)

Hi Robin,

Today's prove session was on the **last open class** of the two-row d=4 fiber law,
`b ≡ 2,3 (mod 4)`. I did **not** close it — it remains genuinely open — but I came back with one
result I'm fond of and one piece of news that changes how we should attack it.

## The pretty fact (Theorem A)

At the half-integer `m = (2b−1)/2` — the centre of the dangerous window — the whole transfer
amplitude collapses to a **central binomial coefficient**:
```
   G_b((2b−1)/2) = (−1)^b · C(2b,b)/4^b · (1−i)^b.
```
Taking imaginary parts, `I_b((2b−1)/2) = (−1)^{b+1} C(2b,b)/4^b · Im(s^b)`, with magnitude
`2^{⌊b/2⌋} C(2b,b)/4^b`, and it **vanishes exactly when 4 ∣ b**. So one formula explains both
sides of the dichotomy: for `4∣b` it *is* the rational root `(2b−1)/2` we'd found numerically;
for `b ≡ 2,3` it's a nonzero central binomial, so the nearest half-integer provably escapes being
a root (the real roots only *cluster* near it — e.g. b=14→13.5, b=23→22.5).

The proof is clean: `g_b(m) = C(m,b) s^b ₂F₁(−b/2, −(b−1)/2; m−b+1; −2i)`, and at the half-integer
the lower parameter becomes `1/2` (and `3/2` for `g_{b−1}`), so two classical Gauss quadratic
transformations evaluate it and almost everything cancels. The family is
`g_b(m) = C_b^{(−m)}(−(1+i)/2)` — a **Gegenbauer polynomial in the parameter `−m`**, not the
usual variable. That's why the standard orthogonal-polynomial machinery slides off (the recurrence
coefficient depends on `m`).

## The course correction (this is the important part)

The plan (and my own earlier instinct) was a uniform **analytic / log-concavity** lower bound on
the alternating trinomial sum. **That cannot work, and now I can prove it can't.** `I_b(m)`, as a
real polynomial in `m`, genuinely **has real zeros inside `[b, ~0.33 b²]`** — the function really
passes through zero in range. So no bound of the form "|I_b(m)| > 0 for all real m ≥ b" can hold;
any dominance argument only reaches `m` *beyond the largest root* (~b²), which is no better than
just computing the roots. The real difficulty is **arithmetic**: those in-range zeros are all
irrational and dodge the integers. The honest conclusion is that closing `b ≡ 2,3` needs an
arithmetic input (irreducibility of `Q_b`, empirically true for all `b`), not analysis — and the
local routes (single-prime Newton, Eisenstein, 2-adic) are already provably dead. So the live
leads are all global: irreducibility of the Gegenbauer-parameter family, a Legendre reflection
identity (`A^{−1/2} = Σ P_n(−s/2) u^n`), or a Perron-type coefficient-growth bound.

## Frontier

Rigorously certified (exact rational roots, SymPy) for **all `b ≡ 2,3`, `b ≤ 70`** — up from the
previous `b ≤ 40`. Supplementary: `I_b(m) ≠ 0` for all integers `m ∈ [b, b²]`, `b ≤ 150`.

Files: `proofs/2026-06-08-tworow-d4-b23-halfinteger-central-binomial.{md,tex,pdf}`, scripts in
`scratch/2026-06-08-prove/`. Pushed to clio-vega/proofs.

Status of the whole law: `b ≡ 0,1` proved (infinite); `b ≡ 2,3` open but now with a clean new
identity, a sharper picture, and a correct sense of which door it's behind.

— Clio
