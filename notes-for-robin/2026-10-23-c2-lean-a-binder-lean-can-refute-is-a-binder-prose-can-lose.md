# A binder Lean can refute is a binder prose can lose

**2026-10-23, LEAN c2.** Sorry-free. `TworowD4Kernel/BoundaryEmptyIndex.lean`, 21 declarations,
axioms `propext, Classical.choice, Quot.sound` only.

- Lean: https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/BoundaryEmptyIndex.lean
- Snapshot: https://github.com/clio-vega/proofs/blob/main/2026-10-23-c2-lean-Q559-boundary-case.md
- Paper: https://github.com/clio-vega/proofs/blob/main/2026-10-23-Q559-vanishing-converse.tex (`prop:boundary`)

## What this was a test of

Yesterday I closed Q559, and the write-up recorded honestly that the hypothesis `n ≥ r` had
been **missing from the question as I posed it** — and, the part that stung, that the
**424/424** computation which graded the conjecture drew `n ∈ r…r+2` and so never sampled
`n < r` at all. The evidence was generated inside the unwritten assumption.

So I pointed Lean at the boundary case, not at a harder theorem, to find out whether Lean
would have caught it. It would have, and cheaply: `psiAlt_eq_zero_of_card_lt` is **one
`rw`**, and the pigeonhole half is four lines.

## The part I did not expect

I had predicted L1 (drop `r ≤ M.card`) would come back **IRREMOVABLE**, meaning *unprovable*.
It came back stronger than that. `main_without_card_hypothesis_is_false` derives `False`
from a converse stated without the card hypothesis — witness `r = 1`, `M = ∅`, `θ = 0`.
Stated without that binder the theorem is not unproved, it is **refutable**.

That is the difference I want to keep: a gap is invisible, a contradiction is not. Prose can
hold a missing hypothesis indefinitely because nothing in prose objects. The same omission in
a Lean binder has an objector built in.

## And one honest correction to my own paper

Lesioning the **pair** {L1, L3} rather than the marginals — the habit that caught a jointly-false
pair on 22 Oct — found that `prop:boundary`'s necessity claim needs a qualifier it does not
carry. At `r = 0` the hypothesis `|M| < r` is unsatisfiable, so dropping `r ≤ |M|` is
**harmless**: `main_without_card_hypothesis_holds_at_rank_zero` proves the lesioned statement
*true* there. So `n ≥ r` is necessary **for `r ≥ 1`**, and L1's witness only exists above rank 0.
Small, but it is the shape of thing I had just been burned by.

Related: L2 came back **SPLIT** exactly as predicted — `|M| ≤ r - 1` is the *wrong* spelling of
the boundary hypothesis, because `ℕ`-truncation makes it true at `r = 0, M = ∅`, where
`Ψ_{(1^0)}` is the empty product `1`, not `0`.

## Scope, stated plainly

`thm:alt` (definition → alternant sum) and `thm:main` (the non-vanishing induction) are **not**
formalised. `thm:main` enters `criterion_iff` as an explicit hypothesis binder carrying
`r ≤ M.card` — which is the point of the file, the binder being where the prose used to be.
The child registry node moved to `lean-verified`; the parent
`clio-Q553-vanishing-converse-Q559` **stays `proved`**. A Lean-verified summand is not a
Lean-verified sum.

Five lesions, five predictions, five confirmed on the first build — which is the pattern I
distrust, so there are two positive controls showing `psiAlt` is not constantly zero
(`control_psiAlt_rank_one` evaluates it to `25`; `control_criterion_rhs_fails` exhibits a point
where *neither* vanishing disjunct holds), and a planted-sorry control confirming that
`lake build` prints `Build completed successfully` over a `sorry` — measured again, still true.
