# Lean: D₀(j) closed forms formalised (b ≡ 0 mod 4, §3 Lemma 1)

**Date:** 2026-06-10 (lean session)
**Status:** ✅ Complete. Compiles with zero errors, zero warnings, no `sorry`; only the three
standard axioms (`propext`, `Classical.choice`, `Quot.sound`).

## What this is

The LEAN.md target this cycle was to extend the formal footprint of the `b ≡ 0 (mod 4)` proof
from the *kernel facts* (delivered last cycle) to **Lemma 1 of §3** — the two closed forms for
the `m`-independent offset

> `D₀(j) = h + v₂(R!) − v₂(j!) − v₂(β_j!)`,  `h = ⌊j/2⌋`,
> `β_j = R − h` (j odd) / `R + 1 − h` (j even).

These offsets are what the tie analysis of §5 stands on. They are now machine-checked:

- **`D0_odd`** — `j = 2h+1` (`β_j = R − h`), `h ≤ R`:
  `h + v₂(R!) − v₂((2h+1)!) − v₂((R−h)!) = v₂(C(R, h))`.
- **`D0_even`** — `j = 2h` (`β_j = R + 1 − h`), `1 ≤ h ≤ R+1`:
  `h + v₂(R!) − v₂((2h)!) − v₂((R+1−h)!) = v₂(C(R, h−1)) − v₂(h)`.

New file: `TworowD4Kernel/D0ClosedForms.lean` in the `tworow_d4_kernel` project. Snapshot pushed
to `clio-vega/proofs` under `2026-06-10-lean-tworow-d4-D0-closed-forms/`.

## Three decisions worth knowing

1. **Stated over `ℤ`, not `ℕ`.** The even-case offset `v₂(C(R,h−1)) − v₂(h)` can be *negative*
   (it is `≥ −v₂(h)`, exactly the bound §4–§5 leans on). Truncated `ℕ` subtraction would have
   silently corrupted it. So I introduced `vz n := (padicValNat 2 n : ℤ)` and worked in `ℤ`,
   where the bookkeeping is honest and the final steps are one `linarith` each.

2. **Parametrised by `h`, not `j`.** I keyed the two lemmas on `h = ⌊j/2⌋` rather than carrying
   `j` plus an `Odd j`/`Even j` hypothesis. `j! ` and `β_j` are fully determined by `h`
   (`j = 2h+1` resp. `2h`), so this loses nothing and avoids parity-of-`j` friction. The
   docstrings record the `j ↔ h` correspondence. (LEAN.md explicitly permitted "a pair of lemmas
   keyed on parity".)

3. **Everything collapses to one additive identity.** I proved
   `vz_choose : v₂(C(R,h)) + v₂(h!) + v₂((R−h)!) = v₂(R!)` (the `vz` image of Mathlib's
   `Nat.choose_mul_factorial_mul_factorial`). Both closed forms then follow from `vz_choose`
   plus the doubling identity `v₂((2h)!) = h + v₂(h!)` (reused from last cycle's
   `padicValNat_two_factorial_two_mul`) and `v₂((2h+1)!) = v₂((2h)!)` (the odd factor adds no 2).
   I did **not** end up routing through `padicValNat_two_choose_eq` (the descFactorial form
   LEAN.md suggested) — `vz_choose` via `choose_mul_factorial_mul_factorial` was the shorter,
   more direct path. The descFactorial kernel lemma remains valid; it just wasn't the cleanest
   tool for this particular assembly.

## Faithfulness check

Beyond the type-checker, I numerically verified that the Lean statements match the paper's
offset definition `D₀(j) = h + v₂(R!) − v₂(j!) − v₂(β_j!)` for all `R ≤ 30` and all valid `h`
(both parities) — 0 mismatches. So the formal statement is the paper's statement, not a
convenient weakening.

## Did NOT attempt

The SECONDARY target (𝔽₂-irreducibility of `m²+m+1` to seed the `b ≡ 2,3` Hensel argument) — the
primary landed cleanly but I chose to stop at a fully-checked, well-documented primary rather
than open a new sub-thread late in the session. It remains a clean, self-contained next seed.

## If you want to look

Infoview: open `TworowD4Kernel/D0ClosedForms.lean`. The two theorems are `D0_odd` / `D0_even`
near the bottom; the load-bearing lemma is `vz_choose`. Build with `lake exe cache get && lake
build` from `projects/lean/tworow_d4_kernel/`.
