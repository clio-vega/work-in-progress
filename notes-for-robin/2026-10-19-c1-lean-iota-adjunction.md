# The ι-adjunction scalar is lean-verified — and `pairwise distinct` moved house

**2026-10-19 c1 (Lean session).** Sorry-free, standard three axioms.

`lean/tworow_d4_kernel/TworowD4Kernel/IotaAdjunction.lean`, 7 theorems, 0 sorries.
Headline: `IotaAdjunction.iotaAdjunctionScalar` — Step 5 of `thm:gauge`,
`(1-q)^d · Q₂²/Q₁ = ∏_{y∈D} (1-q)/(1-qy²)`, with `lem:I2` underneath it.

## The thing worth your time

Yesterday I retracted a clause and restored a `pairwise distinct` hypothesis on the
strength of a plant census (12/12 green at `r=0`, 0/14 at `r≥1`). I pre-registered for
this session that Lean would find the hypothesis **irremovable**.

Lean found it **absent**. Not false — absent. No declaration in the file mentions
injectivity of `y`, and the identity compiles without it. The hypothesis is not an
ingredient of the reindexing identity; it lives one lemma upstream, in
`lem:head`/`cor:heads`, where it is what makes the line-2a/3a denominator `(v_p − v_{p'})`
nonzero. It is a **well-definedness hypothesis for the `T`-operator**, and my own
`rem:distinct` already said so in words — *"the expression is undefined"* — I just hadn't
noticed that this puts it in a different lemma from the one I was about to test it on.

So: the retraction was **necessary** for `thm:gauge` as stated, and my pre-registration
was **wrong about where the hypothesis lives**. Relocated, not confirmed. Same shape as
the 10-17 `CollapseMultiplier` finding: *a genericity hypothesis belongs where the
distinction is made, not where the object is described.*

## Two hypotheses the paper doesn't need

Free strengthening, both from lesions that **survived**:
* **`τ` involutive** is not spent. The identity holds for *any* permutation `τ` with
  `y ∘ τ = y⁻¹`. (With distinct values that forces `τ²=1`; without them it doesn't — so
  this is real generality, not a restatement.)
* **values in `Fˣ`** is not spent either. `div_eq_mul_inv` + `inv_inv` is unconditional
  in a field.

The one hypothesis actually spent is `y ∘ τ = y⁻¹`, and it has an explicit witness:
`d=1, y=(2), q=1` over `ℚ` gives `Q₁ = 0` against `−3`. Non-empty domain, checked.

## Not formalised — the honest boundary

Steps 1–4 of `thm:gauge` (the `W^C`/`E^C` bookkeeping, the six lines of `T`, head
selections) and `lem:I1`. Nothing in the file mentions `T` or `r`. So `gauge-theorem-iota-
adjunction` stays `proved` in the registry; I added lean-verified **children** under it
and under `iota-reindexing-identities` rather than flipping the gapped parents.

## And the build gap from 10-18 is closed

10-18 c2 graded the whole-project build `terminated` at `[3463/3471]` with
`TworowD4Kernel.olean` absent. Cause was **build-lock contention**, which I reproduced
(concurrent `lake build` + `lake env lean` on 4 cores stalls at `[3468/3471]` for 11
minutes with no error and no completion — identical signature). Serialised and rerun
alone: **`Build completed successfully (3472 jobs)`, exit 0, 0 errors**, every one of the
74 sources has an olean. There is nothing wrong with the project; there was something
wrong with how I was invoking it.

Full snapshot: `proofs/2026-10-19-c1-lean-iota-adjunction.md`.
