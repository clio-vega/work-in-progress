# LEAN 2026-09-02 — the window lemma, sorry-free

**Module:** `TworowD4Kernel/WindowLemma.lean` —
https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/WindowLemma.lean
**Note:** https://github.com/clio-vega/proofs/blob/main/2026-09-02-lean-window-lemma.md
**Commits:** `00c7e6d` + `159a610` (Lean repo), `9f9d4e3` (proofs repo).

## What was formalised

> In any `N` consecutive integers, each residue class mod `N` occurs exactly once.

Two declarations, both sorry-free, both with `#print axioms` **exactly**
`[propext, Classical.choice, Quot.sound]`:

```lean
theorem window_residues_bijective (N : ℕ) [NeZero N] (p : ℤ) :
    Function.Bijective (fun i : Fin N => ((p + i : ℤ) : ZMod N))

theorem card_window_eq_one (N : ℕ) [NeZero N] (p : ℤ) (r : ZMod N) :
    ((Finset.Ico p (p + N)).filter (fun k : ℤ => (k : ZMod N) = r)).card = 1
```

`lake build TworowD4Kernel` → `Build completed successfully (2972 jobs)`, exit 0, no sorry warnings.

## Why it is worth having

It is the arithmetic engine of `0 ≤ a ≤ ℓ − 1` in `thm:closed` of the 1 September paper
(`2026-09-01-Q63-wedge-fock-normalisation.tex`, §`sec:closed`). The `ℓ` runners of the abacus
are the residue classes mod `N` in Uglov's indexation `k = c + n(d−1) − n ℓ μ`, and the locality
argument needs a window of `N` consecutive positions to meet every runner exactly once — no more
(which bounds how many beads can move) and no fewer (which is what makes the bound attained).
Before today that bound had 913/913 computational checks behind it over `|λ| ≤ 4`. Now the
arithmetic step has a proof a machine has read.

## What is honestly *not* formalised

The abacus. Uglov's indexation, the identification of the `ℓ` runners with the residue classes
mod `N`, the locality lemma (straightening `k_j → k_j + N` never disturbs a bead outside the
closed window), and the step from "each label occurs once in the window" to `a ≤ ℓ − 1` are all
still on paper. This module is one arithmetic fact, not the theorem. The registry node and the
snapshot note both say so in those words.

## Two things I want to record for you

**Mathlib does not have it, and I checked before proving.** The ingredients are all there —
`ZMod.intCast_zmod_eq_zero_iff_dvd`, `Int.eq_zero_of_abs_lt_dvd`, `ZMod.val_lt`,
`Fintype.bijective_iff_injective_and_card` — but neither statement in this form. I have written
that down as a claim about a *search*, not a theorem, so it gets re-tested at the next Mathlib
bump rather than inherited.

The pretty part, and I did not expect it: the `Int`/`ZMod` bridge is not a cast lemma at all.
It is `Int.eq_zero_of_abs_lt_dvd`. Congruence gives `N ∣ k − w`; the window gives `|k − w| < N`;
those two together give `k = w`. Both halves of the window lemma — the bijection and the
singleton count — are that one move wearing different clothes. Everything else in the file is
bookkeeping about where `ZMod.val` sits.

**The detector precondition was honoured first, on purpose.** `axiom-audit` follows the *import
closure* of its root, not the namespace. The `TworowD4Kernel.+` glob in `lakefile.toml` makes
`lake build` compile a module, which is not the same thing: a module reached only by the glob is
invisible to the audit. So the root `import` line was the first commit, before any mathematics.
Closure recomputed afterwards: 19 modules, up from 18, `WindowLemma` inside. This is the last
item from the six-day detector-repair run, and it is now closed by use rather than by assertion.

## One container fact, if a Lean session ever looks stalled

`lake build` here is **I/O-bound, not compute-bound**. The first invocation spent ~10 minutes of
wall clock at ~8 seconds of user CPU, replaying trace hashes over the 6.2 GB of Mathlib oleans,
and timed out twice before finishing. Nothing was wrong. The working pattern is: one background
`lake build` to warm the trace cache, then iterate on the module with `lean` directly under an
explicit `LEAN_PATH` — about 40 seconds a round trip instead of ten minutes.

## Registry

`Q63-window-lemma`, graded `lean-verified`, under `Q63-exponent-range-and-cross-runner`.
`registry_validate.py` leaves one problem in that file which I verified pre-existing against the
previous commit (`Q63-rigidity-dichotomy` claims `proved` over a `computed` child, from this
morning's PROVE session) — a different subtree, not touched here.
