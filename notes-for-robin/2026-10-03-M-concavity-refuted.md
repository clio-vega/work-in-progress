# The target was false, and the counterexample is one step outside the census

**2026-10-03 PROVE session.** Paper: `proofs/2026-10-03-M-positive-part-concave.tex` (10 pp, builds).
Code: `proofs/code-1003-Mconcave/`. Registry: `cylindric-lorentzian.json`, six new nodes, validator
exit 0 after a planted violation was refused exit 1.

## What I was asked to prove, and the answer

`rem:Mconcave` of yesterday's paper recorded that the half-width multiplicity profile
`M(r) = #{ν ∈ Σ°_b : Λ(ν) = r}` is the positive part of a concave function on all **135,422** nonzero
slices with `2 ≤ m ≤ 5`, `m ≤ n ≤ m+5`, `d ≤ 11`, and called it "a genuine invariant of the family
and the first thing I would try to prove next."

**It is not an invariant. The general statement is false.** Smallest counterexample:

| | |
|---|---|
| `m = 2`, `n = 8`, `μ = (0,4)`, `λ = (3,9)`, `d = 8`, `b = 3`, `c = 5/2` | |
| `ν = (0,7)` | `w = (2,1)`, `f_ν = (1,1)`, `Λ = 1/2` |
| `ν = (1,6)` | `w = (2,3)`, `f_ν = (1,2,2,1)`, `Λ = 3/2` |
| `ν = (2,5)` | `w = (2,5)`, `f_ν = (1,2,2,2,2,1)`, `Λ = 5/2` |
| `ν = (3,4)` | `w = (1,6)`, `f_ν = (1,1,1,1,1,1)`, `Λ = 5/2` |

`M = (1,1,2)`. Increments `0, +1` — not concave; `1² < 1·2` — **not even log-concave**. All four
summands are concentric about `c = 5/2`, exactly as `thm:C` requires, so this is not a failure of
anything proved yesterday.

**Condition (A) is untouched.** `k(·,3) = (2,4,6,6,4,2)` is still PF₂, and so is every other
counterexample I computed. `thm:blind` had already proved that no condition on `M` alone can suffice;
this just removes a true-looking statement from the board.

## The sharp threshold, both halves proved

Put `G = n − m`.

- **`G ≤ 5` ⟹ `M` is the positive part of a concave function**, for every `m`, every `d`, every `b`.
- **`G = 6` ⟹ counterexamples, for every `m ≥ 2`**, in closed form: `n = m+6`, `b = 3`,
  `μ = (0,1,…,m−2, m+2)`, `λ = (0,1,…,m−3, m+3, m+5)` (and `μ=(0,4)`, `λ=(3,9)` at `m=2`), giving
  `g = (0,…,0,5,1)`, `δ = (0,…,0,−2)`, `σ = 1`, `M = (1,1,2)`. Verified `m = 2,…,12`.

**The census range was exactly `G ≤ 5`.** A clean sweep there was guaranteed in advance. The
conjecture fails at the very next value of a single parameter.

## The one piece of new positive mathematics

With `a_i = λ_{i−1} + 1`,

> **Λ(ν) = (n−m)/2 − ½ · Σ_i |ν_i − a_i|**,  equivalently  **c − Λ(ν) = Σ_i (λ_{i−1}+1−ν_i)₊**,

and the right-hand side is **zero exactly when `λ/ν` is a horizontal strip**. So the half-width is
affine in the ℓ¹-distance from `ν` to a point of `ℤ^m` fixed by `λ` alone, and its defect below the
common centre is the horizontal-strip defect of `λ/ν`.

Proof is one line from `eq:Lam` using `(t)₊ = (t+|t|)/2` and the cyclic telescoping
`Σ_i λ_{i−1} = |λ| − n`; the `S_ν` terms cancel identically. Consequences:

- `thm:tent`(1) and (3) follow in two lines (a constant minus half a norm is concave; one unit
  coordinate step moves `Λ` by exactly `±½`, so `|ΔΛ| ≤ 1` along an exchange). **They are surplus.**
- `thm:C` is **spent nowhere.** It is what makes `M` a meaningful summary of a slice, and it supplies
  the value `c = (d−b)/2`; but "M is the positive part of a concave function" is a statement about `Λ`
  alone. Yesterday's route-plan listed `thm:C` as input 1 and it is not needed.
- `M` becomes the ℓ¹-sphere counting function of a box ∩ hyperplane, which is what makes the `G ≤ 5`
  half a finite computation **uniform in `m`**.

## How the `G ≤ 5` half is proved uniformly in m

Frozen coordinates (`P_i = Q_i`) only translate `σ` and `k`, so concavity depends on the non-frozen
box data. That data obeys two **necessary** bounds, which I derive from an exact identity:

> (B1) `Σ_i u_i + Σ_i (δ_i)₊ ≤ G`   (B2) `Σ_i Q_i + Σ_i (−P_i)₊ ≤ G`,  where `u_i = Q_i − P_i`

hence `#{i : u_i > 0} ≤ G`, `P_i ∈ [−G,G]`, `Q_i ≤ G`, and (separately) `d ≤ 3G` on every nonempty
slice. For fixed `G` that is a **finite** superset of what cylindric shapes can realise, independent
of `m`. Exhausting it gives `0, 4, 44, 499, 6679, 105443` reduced cases at `G = 0,…,5` and **zero
failures**. Because `d ≤ 3G`, the independent shape sweep at fixed `(m,n)` is also *complete*, and it
agrees: zero for `G ≤ 5`, failures at exactly `G = 6`, for `m = 2,3,4,5`.

## Controls — what I'd want you to check first

1. **Positive control on the absence claim.** The finite enumerator is the instrument certifying an
   absence, so I first made it find a presence: at `G = 6` it returns **10 failures** out of
   1,931,110. An enumerator returning 0 at `G=6` would have voided the `G ≤ 5` rows whatever their
   arithmetic said.
2. **Refusal control, with the outcome predicted in advance.** Decouple the two budgets (`Σu_i ≤ U`,
   `ΣQ_i + Σ(−P_i)₊ ≤ B`). Prediction from the witness (both equal 6): least admissible is `U=6`
   **and** `B=6`, neither alone. Outcome: `(5,5)`, `(6,5)`, `(5,6)`, `(8,5)`, `(5,8)` all clean;
   `(6,6)` fails. Both bounds load-bearing, both tight, neither relaxable alone **even to 8**.
3. **Abstract-class control.** The statement is **false** for arbitrary box ∩ hyperplane
   (440,168 / 5,531,904 at `m=4`; smallest `P=(−3,−3)`, `Q=(0,2)`, `σ=−1`, `N=(2,1,1)`). So the real
   constraints are doing work and this is not a lattice-point fact in general position.
4. **Three independent routes to the refutation**, the first being *yesterday's own script*
   (`proofs/code-1002-m3/mprofile.py`) verbatim with only `n ∈ [m,m+5] → [m,m+9]` changed: 0 failures
   in its original range (42,718 slices, reproducing [c3]), 100 failures with the wider `n`.

## The methodological thing I think matters most

Not "sweep wider". In the census range **every profile `M` has length ≤ 3, and about 90% have length
≤ 2** — and a nonnegative sequence of length ≤ 2 is concave automatically. The predicate being tested
was **near-vacuous exactly where it was tested**, so it returned green at 135,422 cases and would have
returned green at 10⁷. A census should report the *length of the objects it tests*, not only the count
of tests. That is a cheap column to add and it would have flagged this the day the claim was written.

## Honest gaps and coverage bounds

- Sweeps at `m = 6, 7` (`n ≤ 13` / `n ≤ 14`, `d ≤ 13`) were launched and had not returned at
  write-up. I report that rather than quietly dropping the rows; the closed-form family covers
  `m = 2,…,12` instead, which is the stronger statement anyway.
- The `G ≤ 5` theorem rests on a finite exhaustion (105,443 cases at `G=5`) rather than a structural
  argument. The bounds (B1),(B2) are proved by hand; only the final sweep over the finite class is
  machine work. A structural proof would be nicer and I do not have one.
- *(flagged, then closed during the session)* `w_i(ν) = g_i − (y_{i+1})₋ − (y_i)₊ + 1` **is** exact —
  on all 175,746 nonzero summands tested, with `Σ_i w_i = 2Λ + m` on the same set, zero
  disagreements — and it has a two-line proof. It is now Lemma 4 of the paper and it gives Theorem 2
  more cleanly than the route through `eq:Lam` does. The point: the width **vector** sees `(y_i)₊` and
  `(y_i)₋` separately; the half-width sees only `|y_i|`. That is, quantitatively, the information
  `thm:blind` proves no proof of (A) can do without — so the next target is
  *"for which `(P,Q,σ)` does the multiset `{w(y)}` over the box-slice sum to a PF₂ sequence?"*,
  which is `thm:blind`'s open question with coordinates.

## One slip, reported

`ln -sf` into my scratch directory, then a heredoc **wrote through the symlink** and overwrote
`proofs/code-1002-m3/control.py` — yesterday's refusal-control script. Caught only because the new
file then failed to import; restored with `git checkout`, `git status` confirms nothing else in that
directory changed, and the scratch directory is now real copies rather than symlinks. Separately:
PROVE.md told me to validate "with the command stored in that file's `validate_with` field" and that
field did not exist in the registry. I have added it.
