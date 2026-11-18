# For Robin: G4 Lemma D, slide form, is sorry-free (LEAN 2026-11-18 c2)

`lemmaD_slides` in `TworowD4Kernel/SlideIteration.lean` (tworow-d4-kernel `43eaae1`) uses only the standard three axioms.
For every standard filling of length m+p, Σ's iterated forward jdt slides and the outward procedure's iterated reverse jdt slides
give the same chain. So every letter ends in the same cell, and in particular the U-part is the same. This is lem:D in the tex's own terms.

The proof is the glue that c1 left open. It has two parts:
- **Window lemmas** (forward and reverse). On the full configuration, the switches at positions |A|…|A|+p−1 replace the window cells by the
  one-letter carry and move no label outside the window.
- **Propagation.** The whole word stays standard, so the next row's (column's) slide theorem applies.

These give `sigma_eq_rows_product` and `outward_eq_columns_product`. The c1 theorem `lemmaD_rows_eq_columns` then finishes the proof.
The lesion is a window shifted by one position, and the kernel refutes it. An independent `#guard` evaluation shows rowsW = colsW
even as *cell words* on all 231 instances with |ν| ≤ 5 (120 of them nontrivial).

The parent `H1-G4` stays `proved`, because lem:A, lem:C and thm:G4 are not in Lean.

Note: https://github.com/clio-vega/proofs/blob/main/2026-11-18-lean-lemmaD-slide-form.md
