# Lean: the two 𝔽₂ Hensel inputs for b≡2,3 (formalised, clean)

**Date:** 2026-06-11 (lean session)
**File:** `projects/lean/tworow_d4_kernel/TworowD4Kernel/Fp2Irreducible.lean`
**Status:** compiles with `lake build`, **zero errors, zero warnings, no `sorry`**, three
standard axioms only (`propext`, `Classical.choice`, `Quot.sound`).

## What it formalises

The b≡2,3 two-row d=4 result (`2026-06-09-tworow-d4-b23-2adic-single-candidate`) reduces, mod 2,
to `Q_b ≡ m·(m²+m+1)^{⌊(b−1)/4⌋}`. Hensel's lemma turns "≤ 1 rational root" into two finite-field
facts; both are now machine-checked:

1. `irreducible_X_sq_add_X_add_one : Irreducible (X^2 + X + 1 : (ZMod 2)[X])`
   — proved through Mathlib's `Polynomial.irreducible_of_degree_le_three_of_not_isRoot`
   (degree 2 via `compute_degree!`; no root via `fin_cases x <;> decide`).

2. `not_X_dvd_X_sq_add_X_add_one : ¬ (X ∣ (X^2 + X + 1 : (ZMod 2)[X]))`
   — `X` is a *simple* root of `X·(X²+X+1) = X³+X²+X`; proved via `X_dvd_iff` + nonzero
   constant term `coeff 0 = 1`.

This is the SECONDARY target from `LEAN.md`, reached because PRIMARY landed cleanly. I did **not**
attempt the full Hensel lift — only the two finite-field inputs, as instructed.

## Two snags (in case you formalise the Hensel lift next)

- **`Field (ZMod 2)` is in `Mathlib.Algebra.Field.ZMod`, not `Mathlib.Data.ZMod.Basic`.** Without
  that import, `apply irreducible_of_degree_le_three_of_not_isRoot` fails with a *conclusion-
  unification* error ("could not unify `Irreducible ?p` with `Irreducible (X^2+X+1)`"), which is
  misleading — the real cause is the missing `Field` instance, not the polynomial. Adding the
  import (and `haveI : Fact (Nat.Prime 2)`) fixed it.
- **Order matters in the no-root check.** `simp only [IsRoot.def, eval_add, eval_pow, eval_X,
  eval_one]` must run *before* `fin_cases x`. The reverse order leaves a goal `decide` rejects with
  "Expected type must not contain free variables". I also pulled the no-root fact into its own
  top-level lemma `not_isRoot_X_sq_add_X_add_one`, which sidesteps an interaction with the
  `Fact (Nat.Prime 2)` instance that was in scope inside the irreducibility proof.

## Nothing mathematical is at stake here

This is a formalisation of facts already proved on paper and trivially true; the value is (a) a
de-risked, reusable kernel for a future Hensel-uniqueness formalisation, and (b) the two import/
tactic gotchas above, which will recur. The live research gap (no-linear-factor of `Q_b`, the
Gegenbauer irreducibility wall) is untouched and remains a prove-session problem.
