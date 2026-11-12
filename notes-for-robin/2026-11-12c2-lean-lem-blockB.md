# Q559 lem:blockB is Lean-verified (2026-11-12 c2)

Robin — the "block avoiding n" lemma of the Q559 vanishing converse is now sorry-free Lean.

* Code: https://github.com/clio-vega/tworow-d4-kernel/blob/d9e22646aec83b6f51a41684774a013247cc3110/TworowD4Kernel/BlockB.lean
* Main declaration: `TworowD4Kernel.BlockB.lem_blockB`. Axioms: propext, Classical.choice, Quot.sound. A `sorryAx` control fired in the same run.

**How "order at w_n → ∞" was encoded.** I substituted w_n = 1/u. The lemma then becomes two equalities:
1. Ψ⁻ = (−u)^r · G(u).
2. G(0) = Ψ^C_{(1^r),θ+1}(M').

Here Ψ⁻ is the part of the expansion whose subsets T avoid n, and Ψ^C on the right is the defining head-injection sum. G's only u-dependent denominators are 1 − ux, so G is regular at 0. I read that regularity off G's definition; it is not proved as a valuation statement, and that is the honest scope limit. The exact coefficient is a checked equality.

**Lesions.** Each was Lean-refuted with an explicit ℚ witness: dropping n ∉ T, dropping w ≠ 0, and dropping both.

**Still open for a full thm:main.** lem:blockA (the rank-lowering branching rule) is not formalised. The order comparison between the two blocks will need a u-adic order that both lemmas share.

Snapshot: https://github.com/clio-vega/proofs/blob/main/2026-11-12c2-lean-lem-blockB.md
