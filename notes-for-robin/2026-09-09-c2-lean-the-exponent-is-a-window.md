# The $e-1$ in $\omega R_e(t)\omega = t^{e-1}R_e(1/t)$ is the size of a window

*2026-09-09, LEAN session (cycle 2).*

Repo: `clio-vega/tworow-d4-kernel`, commit `e6bd6a1`, module
[`TworowD4Kernel/RibbonTranspose.lean`](https://github.com/clio-vega/tworow-d4-kernel/blob/e6bd6a1841b75656c7c439cea41956c87116aabf/TworowD4Kernel/RibbonTranspose.lean).

## What I formalised

Not the operator identity — the **lemma that forces its exponent**. Yesterday's Q104 paper
proves $\omega R_e(t)\,\omega = t^{e-1}R_e(1/t)$, and the interesting question about that
theorem is not whether it is true but *why the anomaly is $t^{e-1}$* rather than $t^2$ or a
root of unity. The answer is one lemma:

$$\hgt(\lambda/\mu) + \hgt(\lambda'/\mu') = e-1 .$$

The paper proves it by walking the border strip: each of the $e-1$ steps between consecutive
cells is a row-change or a column-change, and conjugation swaps the two kinds.

**Machine-checked declaration** (sorry-free, axioms exactly the standard three):

```lean
theorem ribbonHeight_add_ribbonHeight_transposeConfig (e : ℕ) (M : Finset ℤ) (b : ℤ) :
    ribbonHeight e M b + ribbonHeight e (transposeConfig e M b) b = e - 1
```

## The thing I want to show you

Transported to the abacus, the paper's step-count stops being a walk and becomes a *count*.
`ribbonHeight e M b` is the number of beads strictly inside the window $(b, b+e)$. Those beads
are exactly the row-changes. The **gaps** in that window are exactly the column-changes. So the
lemma is:

> beads in the window $+$ gaps in the window $=$ size of the window $= e-1$.

The exponent is not a computed constant at all. It is *the cardinality of the window that
conjugation complements* — $e$ sites minus the endpoint the bead sits on. Once you see it that
way the theorem is not a fact about border strips; it's a fact about a $(e-1)$-element set
carrying a $\mathbb{Z}/2$ action.

The corollary I like: `AbacusRibbon.ribbonHeight_le_sub_one` (the degree bound
$\deg_t R_e \le e-1$) had been proved by containment in the window. It is now re-derived in one
`omega` line as `ribbonHeight_le_sub_one_of_transpose`. The bound was never an estimate — it is
one side of an exact split, and the split is what makes it tight.

## What is *not* checked, stated plainly

- Not $\omega R_e(t)\omega = t^{e-1}R_e(1/t)$ itself. That needs $\Lambda$ and $R_e$; the
  registry node `omega-conjugation` stays at `proved`, not `lean-verified`.
- `transposeConfig` is a **window-local** model of conjugation: it agrees with $M$ off the
  window and is the reflected complement on it (`transposeConfig_sdiff_window`,
  `transposeConfig_inter_window` state exactly that, so the modelling assumption is visible in
  the Lean rather than buried in prose). I deliberately did not build the global Maya-diagram
  conjugation — reflect-and-complement takes a `Finset ℤ` outside `Finset`. That
  `transposeConfig` restricts the genuine conjugation is the paper's claim, carried as a
  docstring citation, not machine-checked.

## Housekeeping, two items

1. **Not a regression:** the last three green CI runs all carry
   `Failed to create deployment (status: 404) … Ensure GitHub Pages has been enabled`. The job
   still reports success (the docgen step is `continue-on-error`). It is a repo setting —
   **Settings → Pages** on `clio-vega/tworow-d4-kernel` — not a code defect. One click if you
   want the docs published; otherwise it is harmless noise I will keep ignoring.
2. **A small Lean fact worth having:** `#guard` *compiles* its argument while `decide`
   *kernel-reduces* it, and in this toolchain `Finset.Ico (0:ℤ) 4` pulls in the noncomputable
   `Int.instConditionallyCompleteLinearOrder` — so a `#guard` on it dies with
   `dependsOnNoncomputable` even though the identical proposition proves by `decide`.
   `Finset.Ioo` on `ℤ` is fine. So it is `Ico` specifically, not integer intervals as such.

Artifact with the full audit: `proofs/2026-09-09-c2-lean-ribbon-transpose-complementation.md`
(local). 35 declarations, 0 sorries, all 35 axiom sets checked by set-containment against
`{propext, Classical.choice, Quot.sound}`; `lake build` and `lake test` both exit 0, and the
test driver was verified to fail *independently* by planting a wrong expected value.
