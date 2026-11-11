# LEAN 2026-11-11: Q565 `thm:red` is formalised (alternant layer unconditional, Psidef form conditional on thm:alt)

Robin, `thm:red` from the Q565 paper (`proofs/2026-10-24-Q565-zero-locus-in-M.tex`, L241–L291) is now in
Lean, sorry-free. Commit `bbdbb83`:
https://github.com/clio-claude/tworow_d4_kernel/blob/main/TworowD4Kernel/ReciprocalRestriction.lean

The theorem says: if `w_a w_b = 1` then `Psi(M) = Psi(M \ {w_a,w_b})`, and if `w_a^2 = 1` then `Psi(M) = Psi(M \ {w_a})`.

- The cross-factor identity behind it holds unconditionally: the two cross factors of a reciprocal pair multiply to
  exactly 1. It needs only `w_i ≠ 0, w_a, w_b`.
- At the alternant layer (`psiAlt`) both (a) and (b) are unconditional.
- At the definition `eq:Psidef`, both halves are proved *conditional on* `thm:alt`. I stated `thm:alt` as an explicit
  `Prop` binder at exactly two sets. It is not an axiom, so `#print axioms` shows only the standard three.
- One surprise in the lesions: the Multiset-vs-Finset lesson from `prop:recip` does **not** carry over. There, the
  collapse `{a,a}={a}` lost a square inside a product. Here `{a,b}` is only *removed*, and removing one copy is
  correct. Dropping `a ≠ b` turned out to be removable: Lean proves the lesioned statement. The repeated-entry
  failure the brief predicted is real, but it is admissibility that excludes it, not the choice of carrier.

`thm:alt` is still the single unformalised step under the whole Q559/Q565 tree.
Snapshot: `proofs/2026-11-11-lean-thm-red.md`.
