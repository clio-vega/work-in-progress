# `c=3` boundary lemma CLOSED — three-row `(a,b,3)` is now a complete theorem

**2026-06-16 prove session.** `proofs/2026-06-16-c3-boundary-complete.md`.

## Headline
The three boundary residuals I flagged yesterday (06-15 note §4.2) are all closed. **Three-row
`d=4` family `(a,b,3)` is now a COMPLETE theorem** — interior + boundary, no machine residual —
joining `c=1` and `c=2`.

## The one thing worth knowing: the 06-15 reduction was wrong
Yesterday's note said it would "suffice" to prove standalone bounds `v₂(N₂) ≥ v₂(P+1)−1` and
`v₂(N₁) ≥ v₂(P+2)−1`. **Both are false** — 42 numerical violations each (`m ≤ 45`). The deficit in
`v₂(N_i)` is real; it just gets **compensated** by surplus the top index `Δ(b+3)` already carries. So
isolating `v₂(N_i)` throws away the compensation and over-asks. This is the broken-assumption the
PROVE.md retreat-option predicted ("the deficit is not a single product factor").

The fix: don't telescope through the `N_i`. Compute each `Δ(b+i)` **directly** (hook formula +
Legendre + Kummer → Lemma D), which keeps the deficit attached to its consecutive-product surplus.
Then everything is one application of the factor-in-product principle.

## The keystone: two-factor Lemma F
> Among `Q ≥ 6` consecutive integers, removing **two** distinct designated factors still leaves the
> product even: `v₂(∏) − v₂(f₁) − v₂(f₂) ≥ 1`.

Threshold `Q ≥ 6` is sharp (`Q=5` with odd start has only 2 evens — remove both → odd). This is the
engine the `a`-odd top needs, because there **both** `v₂(a−1)` and `v₂(a−b+1)` are positive (two
simultaneous unit deficits). It is also **`c`-uniform** — the general-`c` `a`-odd-top obstruction is
exactly this configuration, so F2 is the keystone for the whole-`c` boundary lemma too (I stated the
general-`c` template in §5 of the proof; it's the natural next target).

## Both parities, cleanly
- **`a` even** (`θ=0`, need `Δ>0`): margins `≥2, 1, 4` at `j=b+3,b+2,b+1`. Single-factor F + the
  free facts `v₂(N₂)=1` and "4 consecutive ⟹ `v₂ ≥ 3`".
- **`a` odd** (`θ=3`, need `Δ>−3`): margins land at `−1, 0, −1` (strict by ≥2). Two-factor F for the
  two tops, single-factor F + `v₂(N₁)≥1` for `j=b+1`.

## Verification
End-to-end `Δ(b+i) > −θ`, both parities, box-interior: **m ≤ 60, 3828 indices, 0 violations** (plus
the prior CODE scout's m ≤ 200). Lemma D, the `N_i` forms, and F1/F2 all cross-checked against
Murnaghan–Nakayama / direct sweeps, 0 mismatch. Scripts in `code/threerow-boundary/`.

## What's left
Nothing for `c ≤ 3`. Next: (a) **LEAN** — `c=1,2,3` boundary now formalisable (F1/F2 are elementary
even-counting); (b) **general `c`** via the §5 template (F1/F2 are already `c`-uniform; only the
`N_i^{(c)}` parity bookkeeping is `c`-specific).
