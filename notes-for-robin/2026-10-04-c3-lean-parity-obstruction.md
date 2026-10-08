# The parity obstruction is now machine-checked — and it had been hiding inside another proof

**2026-10-04, LEAN session c3.** Sorry-free, standard axioms only.

- Lean: `TworowD4Kernel/ParityObstruction.lean` —
  https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/ParityObstruction.lean
- Note: https://github.com/clio-vega/proofs/blob/main/2026-10-04-c3-lean-parity-obstruction.md
- Commits: `tworow-d4-kernel @ 17be689`, `proofs @ 45ebe58`

## What changed

`proofs/2026-10-04-width-vector-M-convexity.tex` states `lem:P` and then *measures* it:
13,522 slices where the width-vector set `W` is M-convex, 22,451 where it fails, the failures
coinciding **exactly** with the multiple-coordinate-sum slices. I had been reading that
coincidence as strong evidence. It isn't evidence — it's a theorem, and I already had every
piece of it.

16 theorems and 2 definitions, `lake build` exit 0, all 12 theorems on
`[propext, Classical.choice, Quot.sound]`. The chain:

1. `∑ᵢ wᵢ(ν) = n − ‖y‖₁` (already Lean-verified, `HalfWidthL1`).
2. `‖y‖₁ = ∑ᵢ yᵢ + 2k(ν)`, so `‖y‖₁ ≡ ∑ᵢ yᵢ (mod 2)` — **new, and consumes no hypotheses**.
3. `sum_eq_of_mConvex`: **an M-convex set has constant coordinate sum** — new, by infinite
   descent, each exchange spending exactly 2 of the `ℓ¹` distance.
4. Compose: a slice with two distinct `‖y‖₁` has a non-M-convex width-vector set, the two
   sums differing by at least 2. `widthSet_not_mConvex`. **No counterexample search.**

Step 3 is the sentence my (Q) write-up the same day leans on when it explains why the slack
coordinate `w = h − x − e` is *the hypothesis* rather than bookkeeping. It's now checked
rather than quoted, which I think makes that argument meaningfully safer.

## The bit I find genuinely uncomfortable

Step 2 was **already written**. It sat as an anonymous `have hsum` inside the proof of
`HalfWidthL1.twoHalfWidth_eq_sub_two_mul_defect` — with `Per lam` and `Per nu` in scope and
*used by neither*. The parity obstruction that killed (H1) had been living inside a proof of
something else for a full day, and two consecutive briefs talked past it. The fix was to pull
it out as a top-level declaration with no hypotheses; that's all it needed.

I'd flag the general shape: **an unnamed `have` is invisible to every instrument I own.**
Grep finds declarations; nothing I have enumerates the intermediate steps of proofs. If you
have a view on whether that's worth tooling, I'd like it.

## A false instruction in my own brief, for the record

My brief said: *"reuse their `MConvex` predicate, do not introduce a second one."* There is no
`MConvex` predicate — 0 hits for `def`/`structure`/`abbrev`/`class MConvex` across the tree.
`MConvexExchange.lean` and `SublevelMConvex.lean` each prove an exchange axiom for one
*concrete* set (`InSupp`, `InS`) and never abstract it. The token `MConvex` appears only in
filenames, docstrings and namespace names — which is precisely why the claim read as true.

Same brief: nine true claims about existing declarations (I verified all five `HalfWidthL1`
line numbers it cited), one false one, and nothing in its prose distinguishing them. Since
the predicate is new, I added `mConvex_inS` — it derives my `MConvex` from
`sublevel_symm_exchange`, so a misstated definition can't let the theorems typecheck
vacuously.

## What I did NOT formalise

Please don't read the registry node as covering these:

- The **M♮** half (sums of an M♮-convex set form an integer interval). No M♮ predicate exists.
- `A-general-m-tent`, hence *"distance **exactly** 2"*. I prove only `≥ 2`
  (`two_le_abs_sum_sub`), from the slice condition plus parity.
- The converse (13,522/13,522) — measured, not proved; the paper says so.

All three are **proved on paper and not formalised**. Different predicate from "not proved",
and I've been sloppy about that distinction before.

Registry: new node `A-parity-obstruction-lean` at `lean-verified`; parent
`A-width-vector-M-convexity-REFUTED` left at `proved`.

— Clio
