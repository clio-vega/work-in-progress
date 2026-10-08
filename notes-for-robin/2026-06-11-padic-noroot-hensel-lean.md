# Lean: the 2-adic lift — X²+X+1 has no ℤ₂ root + Hensel uniqueness (formalised, clean)

**Date:** 2026-06-11 (lean session)
**File:** `projects/lean/tworow_d4_kernel/TworowD4Kernel/PadicNoRoot.lean` (new)
**Also touched:** `Fp2Irreducible.lean` (added one shared lemma), `README.md`.
**Status:** whole library compiles with `lake build`, **zero errors, zero warnings, no `sorry`**;
all three new results depend only on the three standard axioms (`propext`, `Classical.choice`,
`Quot.sound`).

## What it formalises — both halves of the unique-root result

Last cycle I landed the two **finite-field** Hensel inputs (`Fp2Irreducible.lean`). This cycle
lifts them to the **2-adic** conclusions they were built for — the PRIMARY and SECONDARY targets
of `LEAN.md`, both reached.

1. **PRIMARY — non-existence.**
   `no_padic_root_sq_add_self_add_one : ∀ r : ℤ_[2], r^2 + r + 1 ≠ 0`.
   Apply the reduction ring hom `PadicInt.toZMod : ℤ_[2] →+* ZMod 2` to a hypothetical root;
   `map_add/map_pow/map_one/map_zero` push it to `(toZMod r)² + (toZMod r) + 1 = 0` over `𝔽₂`,
   which `sq_add_self_add_one_ne_zero` forbids. This is exactly what forces `v₂(m − θ) = 0` for
   every integer `m` (Lemma A) and makes `ρ_b` unique.

2. **SECONDARY — uniqueness (Hensel), done in general not just one b.**
   `hensel_unique_root_of_simple_root_mod_two {F : ℤ[X]}
     (h0 : ‖F.aeval (0:ℤ_[2])‖ < 1) (h1 : ‖F.derivative.aeval (0:ℤ_[2])‖ = 1) :
     ∃! z : ℤ_[2], F.aeval z = 0 ∧ ‖z‖ < 1`.
   This is `hensels_lemma` specialised to `a = 0`: with `‖F'.aeval 0‖ = 1` the Hensel hypothesis
   `‖F.aeval 0‖ < ‖F'.aeval 0‖²` collapses to `‖F.aeval 0‖ < 1`, and the Hensel ball is `‖z‖ < 1`,
   i.e. the maximal ideal `2ℤ₂`. The hypotheses are precisely "reduction has `0` as a simple root":
   constant term in `2ℤ₂`, linear coefficient a 2-adic unit. **I stated the general integer-poly
   version rather than one concrete b** — it is no harder, fully faithful to any `Q_b`, and reusable.

3. **Concrete non-vacuity witness.**
   `hensel_unique_root_reduced_model : ∃! z : ℤ_[2], (X^3+X^2+X : ℤ[X]).aeval z = 0 ∧ ‖z‖ < 1`,
   the literal reduced model `X·(X²+X+1)`, discharged by `(by simp) (by simp)`. Its unique 2-adic
   root in `2ℤ₂` is `0` — the lift of `m ≡ 0`.

## Design notes (in case you extend this)

- **One small refactor in `Fp2Irreducible.lean`:** I pulled out the poly-free
  `sq_add_self_add_one_ne_zero : ∀ x : ZMod 2, x^2 + x + 1 ≠ 0` (one line, `fin_cases <;> decide`)
  and rewired `not_isRoot_X_sq_add_X_add_one` to use it. This is the shared `𝔽₂` fact both files
  need; keeping it poly-free dodges the `Polynomial.eval` plumbing in the 2-adic proof.
- **`PadicInt.toZMod` is the whole lever.** It is a genuine `RingHom ℤ_[p] (ZMod p)`
  (`Mathlib.NumberTheory.Padics.RingHoms`), so `congrArg` + the `map_*` simp lemmas do all the work.
  No norm computations needed for PRIMARY.
- **One real snag — bare `X` auto-binds.** With `relaxedAutoImplicit = false` I still got
  `X : Polynomial ℤ` silently bound as an auto-implicit in the concrete corollary, because the file
  didn't `open Polynomial`; the error was an unhelpful "unsolved goals" with a stray `X` hypothesis.
  Fix: `open Polynomial` at namespace level. (`open Polynomial in` between a docstring and the
  theorem does **not** parse — "unexpected token 'open'; expected 'lemma'".)
- **`hensels_lemma` shape:** `{F : Polynomial R} {a : ℤ_[p]} (hnorm : ‖F.aeval a‖ < ‖F'.aeval a‖^2)`
  returns `∃ z, F.aeval z = 0 ∧ ‖z-a‖ < ‖F'.aeval a‖ ∧ ‖F'.aeval z‖ = ‖F'.aeval a‖ ∧ (uniqueness)`.
  Destructure with `⟨z, hz, hzdist, _, huniq⟩`; `rw [h1, sub_zero]` turns the ball into `‖z‖ < 1`.

## What is NOT here

The live research gap is untouched and remains a prove-session problem: the **no-linear-factor**
of `Q_b` itself (the parametric-Gegenbauer irreducibility wall, frontier `b ≤ 171`). What is now
machine-checked is the *certificate machinery* — given the mod-2 factorisation, Hensel forces a
single 2-adic (hence ≤ 1 rational) candidate. That whole logical chain (𝔽₂ irreducibility +
simple root ⟹ no ℤ₂ root for the conjugate factor, unique ℤ₂ lift for the linear factor) is now
formalised end to end.
