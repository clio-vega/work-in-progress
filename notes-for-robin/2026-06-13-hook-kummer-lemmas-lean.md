# Lean: Hook tie Kummer core (Lemmas K and K′) — done, target exceeded

**Clio, lean session 2026-06-13.**

## TL;DR

Both inequalities you asked for in `LEAN.md` are formalised, plus all the scaffolding —
no `sorry`, no warnings, only the three standard axioms. New file:
`tworow_d4_kernel/TworowD4Kernel/HookKummerLemmas.lean`. Snapshot in the proofs repo at
`2026-06-13-lean-hook-kummer-lemmas/`.

The two headline theorems (namespace `TworowD4Kernel`), verbatim from §3 of
`2026-06-12-hook-Jstar-even.md`:

```lean
theorem hook_lemma_K {m t : ℕ} (ht : 1 ≤ t) (htm : 2 * t ≤ m) :
    vz ((m - 1).choose t) - vz (m.choose (2 * t)) ≤ ((Nat.digits 2 t).sum : ℤ)

theorem hook_lemma_K' {m s : ℕ} (hsm : 2 * s + 1 ≤ m) :
    vz ((m - 1).choose s) - vz (m.choose (2 * s + 1)) ≤ (s : ℤ)
```

(`vz n = (padicValNat 2 n : ℤ)`, reused from `D0ClosedForms.lean`; `(Nat.digits 2 t).sum = s₂(t)`.)

## What carried the proof

The crux import you flagged — the central binomial valuation — was clean. Mathlib has Kummer in
the digit-sum form `sub_one_mul_padicValNat_choose_eq_sub_sum_digits`:
`(p−1)·v_p(C(n,k)) = s_p(k) + s_p(n−k) − s_p(n)`. At `p = 2` the `(p−1)` factor is `1`, so it is a
direct equality, and `v₂C(2t,t) = s₂(t)` falls out via `s₂(2t) = s₂(t)`
(`Nat.digits_base_mul`). That is `padicValNat_two_centralBinom`. The odd analogue
`v₂C(2s+1,s) = s₂(s+1) − 1` is the same lemma with `s₂(2s+1) = s₂(s) + 1`.

The only genuinely fiddly part was the **bracket** `v₂(m−t) − v₂(m) − v₂C(m−t,t) ≤ 0`. The paper's
case split on `v₂(m−t) ⋛ v₂(m)` needed the ultrametric `min(v₂(m−t), v₂ t) ≤ v₂ m`, which I built
from `padicValNat_dvd_iff_le` (the common power `2^min` divides the sum). In the hard case the
absorption identity `(m−t)·C(m−t−1,t−1) = C(m−t,t)·t` (`Nat.add_one_mul_choose_eq`) closes it. No
`change`, no `sorry`, no non-terminal `simp` — every step is a named identity or `omega`/`linarith`.

## Honesty / scope

- I formalised **only** the §3 valuation inequalities (K, K′, the `v₂+s₂≤w` helper, and the
  supporting digit/valuation lemmas), as `LEAN.md` instructed. The §1 closed form
  `M_j = C(2m−1−j, a−1)`, the §2 Prop-2 expansion, `G_λ`, and the `g(j)>0` assembly are
  symmetric-function content and stay out of Mathlib reach.
- Before writing any Lean I re-checked that the **formal statements equal the paper statements**
  (not a weakening) and re-ran the numerics: K and K′ over all hooks `m ≤ 400`, the helper for
  `w ≤ 2000`, the central binomial for `t ≤ 500` — 0 mismatch.
- `#print axioms` on all four mains: `[propext, Classical.choice, Quot.sound]` only.

## Reproduce

```
cd ~/projects/lean/tworow_d4_kernel
lake exe cache get
lake build          # 2084 jobs, clean
```

Nothing is blocked and there is no gap to report — this one closed cleanly.
