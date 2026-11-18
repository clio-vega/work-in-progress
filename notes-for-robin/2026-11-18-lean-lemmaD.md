# For Robin: G4 Lemma D, switch form, is sorry-free (LEAN 2026-11-18)

`lemmaD_rows_eq_columns` in `TworowD4Kernel/LemmaD.lean` (tworow-d4-kernel `9df5be9`) uses only the standard three axioms. For all m, p and every chain,
applying the elementary switches by rows gives the same word and the same chain as applying them by columns.
It is the dictionary: one switch is one `Flip switchL` (with U↦D, F↦R, forced by the flip orientation), both orders are monotone flip
sequences from U^mF^p to F^pU^m, and then `confluence_final` finishes it.

Two things you may want to know:
- With `switchL` no chain-level lesion is possible, because confluence holds for every step-blind rule and switchL is involutive.
  The lesions that do bite are on the word.
- The parent `H1-G4` stays `proved`. The glue that turns "rows" into "Σ's iterated forward slides" (a window lemma plus hypothesis
  propagation) is not formalised yet, and neither are lem:A, lem:C or thm:G4.

Note: https://github.com/clio-vega/proofs/blob/main/2026-11-18-lean-lemmaD-rows-eq-columns.md
