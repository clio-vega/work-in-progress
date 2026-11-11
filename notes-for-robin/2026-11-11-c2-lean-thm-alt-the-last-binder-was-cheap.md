# 2026-11-11 LEAN c2: `thm:alt` is formalised, and the Q565 reduction theorem is now unconditional

Robin,

This morning's first Lean cycle formalised Q565's reduction theorem, `thm:red`, but only on the
condition that `thm:alt` held, which it took as an explicit hypothesis. `thm:alt` is my 2026-10-22
alternant expansion, `Ψ = Σ_T B(T)·det(x^m)/V(T)`. In this second cycle I proved `thm:alt` itself.
It turned out cheap: no new mathematics, about 20 minutes of Lean. The proof follows the paper:

1. Group the head injections by their image `T`.
2. The factors that do not depend on the ordering are exactly `B(T)`. The one place that takes care
   is a bijection between ordered pairs `j<k` and the 2-subsets of `T`.
3. Reindex each group by `Perm(Fin r)`.
4. Use Vandermonde antisymmetry (`Matrix.det_permute`).
5. Apply Leibniz (`Matrix.det_apply`).

**Code:** `lean/tworow_d4_kernel`, module `TworowD4Kernel/AlternantExpansion.lean`, pushed at
`231a29f`: https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/AlternantExpansion.lean.
It has no sorries and uses only the standard three axioms. A planted `sorry` control printed
`[sorryAx]` in the same run.

**What this settles in Lean:**
- `thm_alt_paper`: `thm:alt` exactly as the paper states it, for **any** ordering of each `T`.
- `thm_red_a_uncond`, `thm_red_b_uncond`: Q565 `thm:red` on the defining sum, with no hypothesis.
- `psiHead_eq_zero_of_criterion`: the forward ρ-shift vanishing law at the level of Ψ. Before this,
  only its determinant layer was in Lean.
- `psiHead_eq_zero_of_reciprocal_pair`: `prop:recip` at the level of Ψ.

I promoted four registry nodes to `lean-verified`. Each carries a scope note. Not promoted: Q559
`thm:main`, the non-vanishing direction. Its proof needs orders at infinity and the reflection, and
neither is formalised.

**One finding worth knowing.** It is a slip in the repository's encoding, not an error in the paper.
The Lean `rhoShift` uses 0-indexed `j`, so it is the paper's `m − 1`. As a result, the true `V` in
the Lean encoding is `Vandermonde / ∏_T w`. If anyone had plugged the paper's literal Vandermonde
into the cycle-1 hypothesis, they would have been assuming something **false**. Lean refutes that
version at `r=1`, `w=2` (`3/8 ≠ 3/4`). I measured this numerically before writing any Lean: 14/60
against 60/60. Nothing had used that hypothesis, so nothing was lost.

Snapshot note: `proofs/2026-11-11-lean-thm-alt.md` (clio-vega/proofs).

— Clio
