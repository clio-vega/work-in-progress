# Lean: the leading-π dichotomy heart is machine-checked

**2026-06-12 lean session.** New file `TworowD4Kernel/GaussianUnitSum.lean` (snapshot in
`proofs/2026-06-12-lean-gaussian-unit-sum/`). Compiles clean: **zero `sorry`, zero warnings**, only
the three standard axioms (`propext`, `Classical.choice`, `Quot.sound`).

## What it proves

Theorem A's arithmetic core (`2026-06-11-leading-pi-coefficient-dichotomy.md`). The leading
`π = 1+i` coefficient of `G_λ(i)` is `C = Σ_{j∈J*} u_j i^{j−a_j}`, a sum of `|J*|` units of `ℤ[i]`.
Because `i ≡ 1 (mod π)`, `C ≡ |J*| (mod π)`, so **`|J*|` odd ⟹ `C ≠ 0` ⟹ `G_λ(i) ≠ 0`** — the
line that prunes ~72% of `d=4` shapes.

Headline lemmas (`TworowD4Kernel.GaussianUnitSum`):
- `pi_dvd_iff : pi ∣ z ↔ phi z = 0` — the iso `ℤ[i]/(1+i) ≅ 𝔽₂`, the workhorse.
- `sum_units_sub_card` — `(1+i) ∣ (Σ us − |us|)` for any multiset of units = `C ≡ |J*| mod π`.
- `odd_card_sum_ne_zero` — odd count ⟹ sum `≠ 0` (the `C ≠ 0` conclusion).

## How (one design choice worth noting)

I routed everything through the ring hom `φ : ℤ[i] → ZMod 2` built with `Zsqrtd.lift ⟨1, _⟩`
(sending `i ↦ 1`, well-defined since `1·1 = -1` in `𝔽₂`). That turned three things into one-liners:
the unit fact `φ u = 1` becomes "`a² = a` in `ZMod 2`" (`by decide`) applied to `u.re²+u.im²=1`; the
sum fact is `map_multiset_sum` + a constant-map collapse; the odd obstruction is
`ZMod.natCast_eq_zero_iff_even`. The only hand-built witness is the `(⟸)` of `pi_dvd_iff`:
`z = (1+i)·⟨k, k−z.re⟩` where `2k = z.re+z.im`, closed by `Zsqrtd.ext` + `ring`/`omega`.

## Scope (honest)

Abstract: the unit multiset is a hypothesis. I did **not** formalise `J*`/`M_j`/`G_λ(i)`
(symmetric-function machinery — out of scope). The genuinely OPEN math (that `|J*|` is *even* on
ties — the 2-adic Newton-polygon wall in §3 of the proof) is untouched; this is the *proved* half.
Nothing here patches that gap, and I didn't try to (lean session discipline).

Nothing for you to action — just a checkpoint. If you open it in VS Code, `pi_dvd_iff` is the one to
look at; the rest hang off it.
