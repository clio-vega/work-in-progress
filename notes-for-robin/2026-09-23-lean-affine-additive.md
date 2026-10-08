# Lean, 23 Sep: the length-additivity criterion is machine-checked — and the brief's counterexample proves the wrong thing

**Module:** https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/AffineAdditive.lean
**Note:** https://github.com/clio-vega/proofs/blob/main/2026-09-23-c1-lean-affine-additive.md
**Transport check:** https://github.com/clio-vega/proofs/blob/main/code-q232/lean_transport_check.py

13 declarations, **0 sorries**, axioms exactly `[propext, Classical.choice, Quot.sound]`
on every one — and the four periodicity lemmas are choice-free.

## What it formalises

Not the affine symmetric group (not in Mathlib, and not what the theorem is about).
`Additive S T` is *defined* to be the criterion of Lemma 2.3 applied to the block model
of Lemma 2.2 — both assumed, as explicit definitions rather than sorries. So: the
**combinatorial core**, stated plainly as such in the module header.

The obvious objection to defining rather than deriving is that the definition might not
be the thing. So I checked it: `lean_transport_check.py` re-implements the Lean
definitions verbatim and compares them against `ℓ(u_S u_T) = |S| + |T|` computed by
**Shi's inversion formula** — a route that never touches the block model.
**0 disagreements over all 87 376 pairs, 2 ≤ n ≤ 8.**

Separately, `Additive` quantifies over one lift per residue rather than over all runs in
`ℤ`. The paper licenses that by `n`-equivariance; in Lean it is *proved*
(`criterion_periodic`), not waved at.

## The finding

The session brief told me to formalise a counterexample showing "the bracket condition
`i ∈ S, i+1 ∈ T` is not decoration", and said that if Lean and Python disagreed about
the witness, *that* would be the finding.

Lean and Python agree. The witness is real; `additive_not_hereditary` proves it. **The
finding is that the inference from it does not go through** — and today's PROVE note
reached the same conclusion independently.

The witness is `n=3`, `S={0}`, `T={0,1}`, `S'=T'={0}`. In it, **nothing is deleted from
`S` at all** — the deletion is `T ↦ T∖{1}` with `S` fixed. So it shows additivity is
not *hereditary*, which is a different statement from "you need `i+1 ∈ T`". The paper in
fact proves the deletion theorem *without* that hypothesis, in a stronger form.

So I formalised both, and named them honestly:

- `additive_not_hereditary` — the brief's statement. True. Its docstring says what it
  does not show.
- `additive_erase_left_not_stable` — the claim that **is** load-bearing: deleting `i`
  from `S` while leaving `T` alone breaks additivity (`n=3`, `S={0,1}`, `T={1}`, `i=0`
  → `({1},{1})`). The two deletions must be *coupled*; that is the real content.

Then `deletion_n3/n4/n5` machine-check the deletion theorem itself — strengthened form,
no bracket hypothesis — exhaustively over every `(S,T,i)` at those `n`.

## What I did not do

The general-`n` proof is **not** formalised, and nothing stands in for it. It needs the
two-position perturbation lemma proved from scratch against my fuel-bounded gap search,
plus the three-case interval analysis — a multi-session job. I would rather report that
than leave a `sorry` sitting where a theorem should be. The registry node is
`lean-verified` for what Lean checked; the parent `bracketed-pair-deletion` node stays
at `proved`.

You asked me to report which case the paper waves at. Honestly: none. I went looking for
the predicted unstated side condition on `i` being the bottom or top of its run, and it
is already there as `lem:incong` (`p ≢ i+1 mod n`), stated and proved from `q-p ≤ n-2`.
The only fast step is a parenthetical vacuous sub-branch inside Case 1b — correct, but
Lean would make it an explicit case. Yesterday Lean extracted four things the paper did
not contain; today it extracted one, and it was a naming error in my own brief rather
than a gap in the mathematics.
