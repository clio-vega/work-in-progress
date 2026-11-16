# For Robin — LEAN 2026-11-16: growth-diagram confluence is sorry-free

The abstract half of G4's Lemma D, "the order of the elementary switches does not matter", is now machine-checked. It is
`GrowthConfluence.confluence` in github.com/clio-vega/tworow-d4-kernel (`TworowD4Kernel/GrowthConfluence.lean`).

- **Statement.** Let V be any type and L any local rule. Two monotone flip sequences that start from the labelled path `D^p R^m`
  and end on the same path give equal labellings. Both equal η, which is defined by recursion on i+j.
- **The invariant is enough.** The proof only checks that "each vertex on the current path carries η(v)". The claim "each vertex
  is created exactly once", which the paper's prose uses, turns out to be unnecessary.
- **Lesion 1.** A rule that also reads the step number separates rows-first from columns-first on the 2×2 grid. The two orders
  give labels `[0,1,3,2,0]` and `[0,2,3,1,0]`, both checked by `decide`.
- **Lesion 2.** Backward moves break confluence for `L = b+1`. A small extra result: backward moves are harmless exactly when
  `L a (L a b c) c = b`, which is the involutive case and is what tableau switching satisfies.
- **Axioms.** The standard three only, and a sorryAx control fired in the same run.

**Not formalised.** Half (i), that jdt slides are products of switches. The registry parent stays at `proved`, and the new child
`G4-growth-confluence-formal` is `lean-verified`.

Details: `proofs/2026-11-16-lean-growth-confluence.md` (github.com/clio-vega/proofs).
