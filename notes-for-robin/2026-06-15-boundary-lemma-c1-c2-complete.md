# Boundary Lemma closed for c=1, c=2 — those two three-row families are now COMPLETE

**Date:** 2026-06-15 (prove session)
**Proof:** `proofs/2026-06-15-boundary-lemma-threerow.md` · **Code:** `code/threerow-boundary/`
(pushed to `clio-vega/proofs`).

## Headline

The boundary residual that was flagged *identically* in all three interior notes ("one same-shape
boundary inequality, verified-only `m ≤ 79–80`") is now a **theorem for `c = 1` and `c = 2`**, and
partially for `c = 3`. So the **three-row `d=4` families for `c = 1` and `c = 2` are fully complete**
— interior + boundary, no machine-checked gap left. `J*` is exactly the interior 2-adic box; `|J*|`
is even on every tie.

## The one idea

First I killed the tempting wrong reduction: `val(b+i) ≥ b+i`, so "prove `V ≤ b`" — **false** (`V`
can exceed `b`; both sides grow with binomial valuations). The honest reduction is exact:
`val(b+i) > V ⟺ Δ(b+i) := val(b+i) − val(0) ≥ 2 − θ`, where `θ ∈ {0,3}` is the proved
offset/forced-descent.

Then **one engine** does everything — the **factor-in-product principle**:

> Among `Q ≥ 4` consecutive integers `R+1,…,R+Q`, any single one `R+t₀` satisfies
> `v₂(∏_{t=1}^Q (R+t)) − v₂(R+t₀) ≥ 1` (there's always a *second* even factor).

Every `Δ(b+i)`, after a hook-formula computation of `val(0)` (clean 3-row dimension
`f^{(a,b,c)} = (2m)!(a−c+2)(a−b+1)(b−c+1)/[(a+2)!(b+1)!c!]`) and a Kummer "carry" expansion, takes
the shape *(positive linear in `b`) + 2·carries − 2·(deficit)*, where the deficit is `v₂` of a
**factor** of the consecutive product the carries build. Lemma F then gives a one-line surplus.

This closes `c=1` (both parities), `c=2` (both boundary indices, both parities), and the `c=3`
top index `j=b+c` (`a` even) — all with the same bound. The `c=3` top working is the proof that the
engine scales to the genuinely harder family.

## What's left for the full `c=3` win (precisely isolated)

The two `c=3` subtops `j=b+1,b+2` carry an extra polynomial factor (`N₂=a(b+3)−(b²+2b+3)`, and a
cubic `N₁`); the lemma reduces to `v₂(N₂) ≥ v₂(P+1)−1` and an analogue for `N₁`, plus a *two-factor*
Lemma F for the `a`-odd top (two simultaneous deficits). These are finite-shape, verified `m ≤ 39`
(0 violations, strict — no boundary tie, so the interior theorems need no correction), and are the
natural next PROVE/LEAN target alongside the now-complete `c=1,2`.

## Suggested next steps

- **LEAN:** the `c=1,2` families are now complete and worth formalising end-to-end (Lemma F is a
  trivial Lean target; the hook formula + Kummer are standard).
- **PROVE:** finish `c=3` via the two isolated bounds above; the engine is in place.
- The factor-in-product principle looks uniform in `c` for the **top** index (Lemma T is uniform);
  worth a dedicated attempt at "all-`c` top boundary" as a clean partial of the general `e₂ mod 2`
  programme.

— Clio
