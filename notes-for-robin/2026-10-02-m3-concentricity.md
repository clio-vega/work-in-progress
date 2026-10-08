# 2026-10-02 PROVE — concentricity survives to every m, and the reduction provably does not

**Paper:** https://github.com/clio-vega/proofs/blob/main/2026-10-02-m3-concentricity.tex
(10pp, compiles). Code: `code-1002-m3/`. Registry: 6 new nodes under `conj-A-logconcave`.

## What I was asked and what came out

The brief asked one question: is the concentricity that proved condition (A) at `m=2`
yesterday an `m=2` accident, or a cylindric fact? **Neither — it is a horizontal-strip
fact, and it holds for every `m`.**

**Theorem 1.** `sum_i (L_i(nu) + R_i(nu)) = S_nu + |lambda|` for every `nu`, every `m`.
So every summand on a slice is symmetric about the one centre `(d-b)/2`.

The whole thing is `max(x, y+1) + min(x-1, y) = x+y`, applied once per bead by pairing
`L_i` with `R_{i-1}`. Both clamp pairs — `(nu_i, nu_i - 1)` and `(lam_{i-1}+1, lam_{i-1})` —
are consecutive integers coming from **one** number, and that is exactly what
"`nu < kappa` and `kappa < lambda` are horizontal strips" says, read once from each side.
Telescoping leaves one unmatched term `R_m - R_0`, and cylindric periodicity makes it the
constant `n`. So the honest accounting is **one local identity spent `m` times plus one
global closure** — not the "two hypotheses, each once" that yesterday's paper records. At
`m=2` the global closure is invisible because with two beads it hides inside the second
crossed sum.

**Theorem 2** generalises the tent lemma, and more cleanly than at `m=2`: the half-width is
`Lambda(nu) = sigma_0 - sum_i max(nu_i, lam_{i-1}+1)`, a **separably** concave function, and
`{nu : f_nu != 0}` is **again a box**. So the effective slice is box-∩-hyperplane,
exchange-connected, `|Delta Lambda| <= 1` along exchanges, hence the occurring half-widths
are consecutive. (This also explains why no coupled degeneracy case analysis is needed at
general `m`: the vanishing `nu` are cut off by single-coordinate bounds.)

## The finding I would actually keep, and it is negative

**Theorem 3 (no shape-blind hypothesis can suffice).** Two multisets of concentric box
splines with the *same* half-width profile `M = (1,1,1,1)`:

    {(1,1),(2,2),(1,5),(2,6)} -> (1,3,4,6,4,3,1)   16 < 18, NOT PF2
    {(1,1),(2,2),(3,3),(4,4)} -> (1,3,6,10,6,3,1)  PF2

So Theorems 1 and 2 are **provably not a complete reduction**. Any proof of condition (A) at
`m >= 3` must use the width *vectors* `w(nu)`, not only the half-widths they determine. That
closes an entire family of approaches, including the one I was ten minutes from writing down
as a conjecture.

Why the `m=2` proof escaped this: there `w_1 - w_2 = 2(t_0 - nu_1)`, so the width
*difference* determines the slice parameter and no two summands of one slice can share it.
The bad multiset above has differences `0,0,-4,-4` and is not realisable at `m=2`.

## Three things that died, each with a located mechanism

1. **Step 3 of the `m=2` proof** (`beta` = positive part of a concave function) is **false**
   at `m >= 3`: 24192/37448 single splines, smallest `w=(3,3,3,3)` with
   `beta=(3,6,6,3,1)`. On real slices it fails 105084 times at `m=3` alone. Smallest
   aggregate witness: `n=9, mu=(0,1,6), lam=(2,5,8), b=2`, where each individual `beta_nu`
   *is* concave and the sum is not — the class is not closed under addition.
2. **Pairwise `(*)` at the layer level** fails, on that same smallest witness (`0 >= 1`).
   The antichain obstruction of [c1 §2.1] is not removed by passing to layers.
3. **The natural repair** — prove `beta` log-concave, quote the tail lemma — is **strictly
   stronger than the target** and false in the abstract class my two theorems carve out:
   `w=(1,5)` and `w=(3,3)` sum to `(2,3,4,3,2)`, which **is** PF2, while `beta=(1,1,2)` is
   not log-concave. It is a fine *test* and the wrong *target*.

## Where I would go next

`M(r) = #{nu : Lambda(nu) = r}` **is** the positive part of a concave function on all 135422
real slices tested — the concavity that dies at the layer level reappears one level up. By
Theorem 3 it cannot suffice alone, but it is a genuine invariant and it should be provable
from Theorem 2 (it counts lattice points of a box-slice on which a separably convex function
is constant). Then: describe which `w(nu)` co-occur on a slice. That is the input Theorem 3
says is unavoidable.

## Process notes

- **Condition (A) itself**: 0 failures on 4,323,908 slices this session (`m=3` to `n<=16`,
  `d<=20`; `m=4,5,6` wide), against the registry's previous 96781 points. Instrument
  calibrated first: an independent chain enumerator touching none of the `L_i, R_i`
  machinery agrees on 13689 slices at `m=2,3,4`.
- **The control was four-way and discriminating**, not an alarm: offset *value* change
  silent, offset *mismatch* fires, period decoupling fires, ordinary-skew degeneration
  silent — all four predicted in advance. P3 **corrected me**: I had concluded periodicity
  was not load-bearing, which was wrong, and the control said so.
- **A by-product**: P4 shows concentricity holds for *ordinary* skew shapes too. The
  mechanism is not cylindric at all; only the boundary term is.
- **Third session running** in which extending a range past the one that bore a statement
  was the decisive move — and the first in which it caught a conjecture of *mine* before I
  wrote it down. Sizes 2 and 3 scored perfectly; size 4 refuted it.
- **One self-inflicted mess, reported rather than explained away**: a careless
  `cp *.py code-1002-m3/` dumped 44 unrelated scripts from `proofs/` into my working
  directory. No filename collided, so nothing of mine was overwritten (checked
  name-by-name, then re-ran the calibration to confirm the engine still reproduces both
  known `m=2` values). Removed. The glob was the bug; the check I ran afterwards is the one
  I should have run before.
