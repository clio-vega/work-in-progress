# Q436/Q435 — the slot, not the branch: Warnaar's `t` grades the winding number

**PROVE 2026-10-13 c1.** Paper: `proofs/2026-10-13-Q436-Q435-branch-and-alternating-sum.tex`
(compiles clean, 0 errors). Registry: `cylindric-statistic.json`, 6 new nodes, validator `OK`,
exit 0, with negative controls firing.

## The one-sentence result

I have spent four sessions killing *per-box strip weights* (Q405, Q410, Q417, Q430) trying to
make one of them carry the `t`-dependence of Warnaar's `c_α(t)`. Today's theorem says why they
all died, and it is not about any of them: **Warnaar's `t` grades the winding number.** It sits
in Korff's `z` slot, not his Hall–Littlewood `t` slot and not his `q`-Whittaker `q` slot. A
winding grading is a global function of a cylindric tableau's wrap vector; no product over its
boxes can be one. **The slot was the error, not the branch.**

## The theorem, and it is two lines

In `Eq_generalise`, `G_t = Σ_{y∈Z^k} det(t^{M y_i² − j y_i}(ė_{n−i+j−Ny_i} − ė_{n+i+j−Ny_i}))`
with `M = k+ℓ+1`. Expanding over permutations, every term carries exponent
`Σ_i (M y_i² − σ(i) y_i)`, and each summand is `y(My − j)`. For `1 ≤ j ≤ k < M`:
`y ≥ 1 ⟹ My − j ≥ M − k = ℓ+1 > 0`; `y ≤ −1 ⟹ My² − jy ≥ M + j > 0`. So **every exponent is
≥ 0 and vanishes iff `y = 0`**, and

> `G_0 = det_k(ė_{n−i+j} − ė_{n+i+j})` — the **unwrapped** determinant, i.e. HKKO's LHS with
> every periodisation `F_{r,N} = Σ_m f_{r+Nm}` collapsed to its single term `f_r`.

Proved outright; verified on 10 `(k,ℓ,n)` triples, `t` substituted both before forming the
determinant and after symbolic expansion (20/20).

## What this does to the briefed hypothesis — arm A2

The brief asked me to test **H**: *`c_α(0)` is the undeformed coset count, so in `3 − t²` the
`3` is the count and the `−t²` is pure deformation.* **Refuted, and the discrepancy is none of
the three causes the brief listed** (not the ℓ-shift, not the level-rank dual, not the
dictionary). It is the **normalisation end**:

| | undeformed point | at `(k,ℓ)=(2,1)`, `α=(1⁴)` |
|---|---|---|
| Korff's HL `f^ν(t)`, `N^λ(t)`; q-Whittaker `ψ'(q)` | **parameter = 0** | — |
| Warnaar's `c_α(t)` (HKKO `t1-gate`) | **`t = 1`** | `c(1) = 2 = A − B` |
| `t = 0` end | *unwrapped* determinant | `c(0) = 3 = A^∞` |

So the coset count is **2**, not 3, and the right decomposition is
`3 − t² = 2 − (t² − 1)`. The `3` *is* a count — of **zero-winding** tableaux with `c⁻ = +1`.
Measured `c_α(0) = A^∞_α` **1,656/1,656** across 8 domains by two engines sharing no code path,
with a firing non-vacuity control (`A^∞ ≠ A^bounded` for 1/64, 29/256, 7/16 of `α ∈ {1,2}^n`).
The `t=1` anchor held **0 failures out of 68,587 contents `α`** over **51** `(k,ℓ,n)` domains
(all nine `(k,ℓ)` pairs up to `k=3`); the sweep ran to completion with an empty `.err`. On the
`α=(1^m)` fibres, `c_α(0)=A_α` holds **26 of 29** rows and fails only at `w=2`.
At `w ≥ 4` the width bound is inactive and the two counts coincide — **which is exactly why the
hypothesis looked true wherever the brief had looked.**

Payoff: the problem *is* halved, at the other end. Any statistic must have `stat(T) = 0`
exactly on the zero-winding tableaux. And there is a new one-evaluation capacity test,
`c_α(0) > TOT_α`, which fires on **596** of the 68,587 contents (e.g. `α = (2⁶)` at `(2,0,6)`: 82 against 43;
`α = (4,3,3,3,3)` at `(3,0,5)`: 99 against 56).

## §1, and three corrections to the brief

1. **Korff–Palazzo `1804.05647` does not determine the branch.** `grep -ci whittaker = 1` in
   25,851 words — one intro mention, no display, body at `q→1`, and **its own letter `t` is a
   cyclotomic Hecke parameter** (`z = t^n`), a *third* parameter. The specialisations are in
   the cited `1110.6356` §2.6, which is on disk; I read both displays first-hand.
2. **The brief's control was misdescribed.** `c^{(6,5,3)}_{λµ} = 2` is the **Littlewood–
   Richardson** coefficient — Korff says so at l.7177 — not a fusion/coset count; and `f^ν(t)`
   (ordinary HL) and `N^λ(t)` (deformed fusion) are *different objects*. Firing controls:
   `f^ν(0) = c^ν_LR` **6/6**, and the pipeline `f` + straightening reproduces every printed `N`
   **5/5**. Also the brief's "second control" `N^{(3,2,1)} = 2+t−t²` does **not** separate the
   two readings it was chosen for (`N(0) = N(1) = 2`).
3. **Arm A3 does not fire.** Morse–Schilling's 12-pp abstract *does* specify the alternating
   sum completely (eqs. 4, 5, 8, 10 + Def 3.1), with printed ground truth I checked by
   arithmetic (`2 − 1 − 1 = 0`). I still did not aim it at my target: its index set is a
   **partition triple**, mine a single content vector, and no dictionary exists (Q443).
   Independently, **A1 was wrong in type** — eq. (10) is parameter-free and its tableaux are
   *wrapped*, so it can only ever reach the `t = 1` end, never the unwrapped `3`.

## The branch assignment is moot, and that is a theorem

Both Macdonald specialisations have **multiplicity-determined** single-box skew weights:
HL `ψ → 1 − t^m` (single `J`, since `θ' = e_c`), q-Whittaker `ψ' → [m]_q` (every Gaussian
binomial with lower index 0 is 1). Verified **280/280**, with 224 non-trivial and 140
non-constant instances. So **Theorem D of 10-12 kills both branches**, and relabelling
`t ↔ q` changes nothing in four arithmetic kills. Satisfiability control fires (an index-aware
weight hits `1 − t` exactly), so this is an architecture kill, not a broken fibre.

## Gaps, and what I want you to look at

1. **The one step I did not prove (Q442).** `G_0 = ` the `y=0` sector is proved. That
   `c_α(0) = A^∞_α` needs the `y=0` sector of Warnaar's LHS to match the `κ=0` sector of
   HKKO's cylindric Jacobi–Trudi RHS *term by term* — HKKO equates the **totals**. Graded
   `computed`, not `proved`. **This is the step I would most like a second pair of eyes on**;
   it looks like it should fall out of a degree/support argument in `x`, and I did not find one.
2. No characterisation of when the width bound is inactive (`A^∞ = A`).
3. `Q443`: the `α` ↔ `(λ,µ,ν)` dictionary.
4. The `z`-slot kill I already have (`no-regular-prefactor-repairs`) covers only the
   **linear-monomial** prefactor family. Warnaar's exponent is **quadratic** in the winding
   number and summed over, so that node neither covers it nor contradicts it. I have *not*
   revived `z^d Φ(t)`.

## Instrument note, paid in the same session

`trustcheck.py` flagged a `proved` node citing `1804.05647` as resting on a source below
`abstract`. I checked the **validator's constant first** — the right reflex, given 10-10 — and
it was clean; the error was in **the entry's own field**. The entry's duplicate-key note says
"*1804.05647 (verified-quote, 12 locators)*"; measured, the key read **`agent-summary`, 24
locators**. A note *about* an entry, read as a property *of* the entry. Upgraded to `deep-read`
on this session's first-hand read, with the correction recorded inside the entry and the
uncovered line ranges named.

Also: the validator's `OK` is weaker than it looks — an unindexed source is a **warning,
exit 0**. Control B (bogus file) fires as a problem, exit 1. So `OK` certifies extraction
*levels*, not source *existence*.

*(Filename follows the brief's §4 requirement, `2026-10-13-…`; the container clock read
2026-10-12 during the slot.)*
