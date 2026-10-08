# For Robin — `c = 3` three-row boundary is now machine-checked (Lean)

**Date:** 2026-06-18 (lean session)

## Headline

`threerow_c3_boundary` compiles `sorry`-free in `lean/tworow_d4_kernel` (Mathlib v4.30.0).
`#print axioms` shows only `[propext, Classical.choice, Quot.sound]`. Full project `lake build`:
0 errors, 0 warnings, 2091 jobs.

**All three complete three-row `d = 4` families — `c = 1, 2, 3` — now have their boundary lemmas
end-to-end machine-checked.** (`c = 1`: `ThreeRowC1Boundary`, 06-16; `c = 2`: `ThreeRowC2Boundary`,
06-18; `c = 3`: `ThreeRowC3Boundary`, this session.) Snapshot:
`proofs/2026-06-18-lean-c3-boundary/`.

## What was new this session

1. **`lemma_F2` is finally load-bearing.** The `a`-odd cases carry two simultaneous unit deficits
   (`v₂(a−1)` from `a−1 = 2(P+β+1)`, and `v₂(P+2)` from `a−b+1 = 2(P+2)`). The two-factor engine
   (`Q ≥ 6`, surplus `≥ 1`) dissolves both at once for the top `b+3` and subtop `b+2`. Its `Q ≥ 6`
   threshold was already formalised; this is the first proof that actually needs it.

2. **`N₁, N₂` evenness derived, not assumed.** Only the *definitions*
   `N₂ = a(b+3) − (b²+2b+3)`, `N₁ = ab² + 5ab + 6a − (b³+b²+4b+6)` are hypotheses. The valuations
   `v₂(N₂) ≥ 1`, `v₂(N₁) ≥ 1` are proved in Lean via exact even decompositions
   (`N₂ = 2(Pb+3P+2b+3)`; `N₁ = 2·(…)` with parity-split coefficients), each closed by `ring` after
   substituting `a = 2P+b+3` and `b = 2β` / `2β+1`, then `Nat.add_sub_cancel`. Same idiom as `c = 2`'s
   `W₁`. Note `N₁` is even in *both* parities (the bracket `b(7b+17)` is always even), which is what
   lets the `a`-even subtop `b+1` reach `Δ ≥ 2` rather than stalling at `Δ ≥ 0`.

3. **Hypothesis form.** I expanded the §1 Lemma D `carries(·,·)` terms via
   `carries(x,y) = s₂(x)+s₂(y)−s₂(x+y)`; the `s₂(b+2k±1)` columns cancel, leaving the clean forms
   in the README. These extend the `c = 2` hypothesis shape verbatim and were re-verified against
   true Murnaghan–Nakayama valuations: **573 box-interior cases, 0 mismatches.** The six
   bridge-collapse identities and the `N₁` decompositions were checked symbolically (sympy).

## Honesty / scope

- A `C(m,j)`-factor subtlety bit me early: `val(j) = j + 2 v₂(C(m,j)·M_j)`, *not* `j + 2 v₂(M_j)`.
  My first MN reproduction omitted `C(m,j)` and disagreed with the (correct) `c = 2` forms; once
  corrected, everything matched. The Lean hypotheses use the right convention.
- No gap found in the paper proof. The informal `Δ`-telescope (`2026-06-16-c3-boundary-complete.md`)
  is exactly right in the box-interior regime.
- As always, the `M_j`/`G_λ` symmetric-function closed forms stay MN-verified, not Lean-checked.

## On the `c = 4` stub (deferred, deliberately)

The brief suggested stubbing `threerow_c4_boundary` if `c = 3` landed quickly. I **did not** add it,
because a `sorry`-bearing file would break the project's 0-sorry / 0-warning guarantee (the lakefile
glob `TworowD4Kernel.+` compiles every file in the namespace). The `c = 4` boundary is `θ = 0`,
indices `b+1..b+4`, `a−b+1 = 2P+5` odd (no smooth deficit — structurally like `c = 2`, **no F2
needed**), and the paper proof is closed (`2026-06-16-c4-boundary-complete.md`). But it genuinely
needs the `c = 4` `N_i` contents (`v₂(N₂) ≥ 2`, `v₂(N₁) ≥ 3` (b even) / `≥ 2` (b odd),
`v₂(N₃) ≥ 1`) and the D-telescoping — a full file, not a one-line skeleton. **Recommended next lean
target:** `threerow_c4_boundary`, reusing `vz_prod_Icc` + `lemma_F` (single-factor suffices, c even)
+ four `vz_N_*` even/4-content helpers analogous to `vz_N2_ge_one`. It pairs with the `c = 4`
interior PROVE work.

## If you want to look (Infoview)

`TworowD4Kernel/ThreeRowC3Boundary.lean`. The six per-index lemmas
(`threerow_c3_boundary_{top,sub2,sub1}_{aeven,aodd}`) are each ~25 lines; the assembled theorem is
the last declaration. The `vz_N2_ge_one` helper sits at the top.
