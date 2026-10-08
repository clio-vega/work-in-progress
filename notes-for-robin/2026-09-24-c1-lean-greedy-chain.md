# The greedy chain is machine-checked — 2026-09-24 c1 (LEAN)

`TworowD4Kernel/GreedyChain.lean`, `clio-vega/tworow-d4-kernel@1d35afb`.
Full file: https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/GreedyChain.lean
Session note: `proofs/2026-09-24-c1-lean-greedy-chain.md`.

`lake build` green, **0 sorries**, standard three axioms.

## What it is

`lem:greedy`(1) and (3) and the `ℓ`-independence half of `prop:noell` from the cylindric
M-convexity paper — the greedy chain `gᵗᵢ = min(gᵗ⁻¹ᵢ₊₁ − 1, λᵢ)`, that it stays a cylindric
shape, that each step is a horizontal strip, and that **it dominates every chain
coordinatewise**. That last one, `greedy_dominates`, is the brick the whole
dominance-maximum argument stands on.

## Why this one is different from yesterday's

Yesterday I formalised `AffineAdditive` and had to say honestly in the header that the paper's
criterion was *defined* rather than derived, because the affine symmetric group isn't in
Mathlib — a definition the type checker cannot falsify, discharged only by an external Python
check against Shi's inversion formula.

Here there is no transport. Every object is an explicit inequality on `ℤ → ℤ`, so there is
nothing to model and nothing to model wrongly. The file assumes nothing.

And the spine — `greedy_isCylindric`, `greedy_hstrip`, `greedy_dominates`, `greedy_fix` — is
**choice-free**: axioms exactly `[propext, Quot.sound]`. `Classical.choice` appears only in the
four declarations that touch `Finset.sum` or `Multiset.filter`.

## Two things worth your eye

**The correction to gap (iii) is one line.** `prop:noell` was proved on paper two days ago to
kill the 09-20 clause "λ̂ grows with ℓ", which was false. In Lean the whole of it is
`min(λᵢ₊₁ − 1, λᵢ) = λᵢ` because `λᵢ < λᵢ₊₁` — strict increase of `λ` doing all the work. It
is satisfying to see a three-day-old false obstruction reduce to `omega` on two hypotheses.

**`lem:greedy`(3) is weaker than the paper states.** In Lean it needs neither periodicity nor
`μ ⊆ λ` — only the strip conditions. The paper bundles the hypotheses of (1) and (3); they
separate cleanly, and I'd suggest restating (3) without them if the paper is revised.

## What I did NOT do

- `prop:max` itself (needs `Sₗ`-stability + Bender–Knuth) — out of scope, so `greedy-maximum`
  stays at `proved` in the registry; only the new child `greedy-dominates-coordinatewise` is
  `lean-verified`.
- `lem:greedy`(2), `gˡ = λ` — plumbing round the nonemptiness hypothesis, not difficulty.
- The step from "multiset of nonzero increments is `ℓ`-independent" (what I proved) to "sorting
  discards the trailing zeros" (what the paper says). That is a real proposition, not
  presentation, and I've recorded it as unproved rather than waved it through.

## Differential check

`proofs/code-greedy/greedy_check.py` re-implements the definitions independently and
enumerates *all* chains by brute force — successors built straight from `eq:hstrip`, so it
does not inherit `lem:box`. **0 failures** over 397 shape pairs, 5925 chains, 60225 coordinate
comparisons (`2 ≤ n ≤ 5`, `1 ≤ m ≤ 3`, length `≤ 4`). It also confirms `prop:noell`'s other
half (`𝒯_ℓ ≠ ∅` iff `ℓ ≥ ℓ₀`, 1985 instances), which is not in the Lean file.

## One tooling note

`registry_validate.py` resolves node `file` fields against `projects/proofs/` when they are
relative to `projects/`, so it reports 14 spurious "file not found" — every node in the
registry — and exits 0 while printing them. Same root-directory defect I found in
`trustcheck --files-dir` on 09-22, now in a second tool. Worth a one-line fix when you're next
in that code; I checked the paths by hand rather than trusting either tool.
