# Q559 thm:main is now Lean-verified (2026-11-14, LEAN c1)

Robin, the converse of the ρ-shift vanishing law is now formal end to end. The statement: for |M| ≥ r and pairwise distinct
ρ-shifts m_j = θ_j + j − 1, Ψ^C_{(1^r),θ}(M) ≠ 0. The complete criterion `cor:criterion` is also formal, stated as an iff.

- Lean: https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/ThmMain.lean (commit `d851f73`)
- Paper: `proofs/2026-10-23-Q559-vanishing-converse.tex`, thm:main L360–L393.
- Axioms: propext, Classical.choice and Quot.sound only, on all 14 declarations. A `sorryAx` control fired in the same run.

**What "≠ 0" means in Lean.** Over any infinite field, some point with nonzero, pairwise distinct weights has Ψ ≠ 0. Going from
there to "≠ 0 in ℚ(w)" is the evaluation homomorphism, and that bridge is not in Lean. I've named it as the scope limit.

**The reflection step became concrete.** Case B runs Case A at θ∨ and then evaluates at the *point* w⁻¹:
Ψ_θ(w⁻¹) = (−1)^r e(w)^{2r} Ψ_{θ∨}(w) ≠ 0. The paper's argument that "ι is injective" turns into "w⁻¹ is admissible".

**Lesions.** I asked Lean to derive False from each weakened statement, and it did in every case:
- dropping |M| ≥ r;
- dropping distinctness;
- dropping both;
- dropping "K infinite": over 𝔽₂ there is no admissible point at all on two indices.

**One small generalisation.** The removed index n can be any element of M, not only the largest. The paper's "largest" is used
only to order the subsets T ∋ n, and a glued ordering supplies that for every n.

Snapshot: `proofs/2026-11-14-lean-thm-main.md`. Still not formal: cor:branch, the w_n → ∞ limit form of the branching rule.
