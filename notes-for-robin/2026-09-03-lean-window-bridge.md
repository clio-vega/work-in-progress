# The window bridge is formalised — and the gap to the paper is now a named thing

**Session:** LEAN, 2026-09-03 · **Repo:** `clio-vega/tworow-d4-kernel`, commits `d5707cf`, `5037b78`
**Note:** `proofs/2026-09-03-lean-window-bridge.md` · **Registry node:** `Q63-window-bridge`, `lean-verified`

## What happened

Yesterday I formalised the window lemma — *in any `N` consecutive integers each residue mod
`N` occurs exactly once* — and recorded honestly that it was a pretty arithmetic fact that
did not yet reach anything the paper needed. Today it reaches. `cor:range` of
`2026-09-01-Q63-wedge-fock-normalisation.tex` says

$$0 \le a \le \ell - 1, \qquad 0 \le h \le e - 1,$$

and **both halves are now machine-checked**, sorry-free, axioms within the standard three.

The thing I want to point at is not the proof — Mathlib did most of it and the corollaries
type-checked first try — but a small structural observation that made the session cheap.
Reading `sec:closed` closely, `a` and `h` are **the same count along the two axes of one
label**. `a` fixes the residue coordinate `c` and varies the runner `d`; `h` fixes the
runner and varies `c`. So there is one bridge lemma, applied twice with the axes exchanged,
and the price of the second half was a single extra injectivity lemma. I had gone in
expecting to formalise `a ≤ ℓ − 1` alone. Getting `h ≤ e − 1` free is the kind of thing that
makes me trust the coordinates.

## The part I think is actually worth your attention

The deliverable I was asked for was *the theorem plus a written statement of the gap between
it and the paper*. The gap is not zero and it has a shape:

1. **The coordinate change is the real gap.** The paper *defines* `a` in the `κ`-coordinate;
   Lean bounds the count in the `k`-coordinate. Their equality is the last paragraph of the
   proof of `thm:closed` — solving `eq:kcd` to get `μ′ = μ` for `d′ > d` and `μ′ = μ − 1` for
   `d′ < d`. That is a different *kind* of work: an arithmetic identification of two
   indexings, not a counting argument. Formalising it means giving the abacus a type, and
   that is the term-project the brief told me to stay out of. **This is exactly where the
   boundary falls**, and I think knowing that is worth more than having crossed it badly.
2. **Only "at most once" is proved, never "exactly once".** The upper bound needs only the
   injective half. The surjective half is what would make the bounds *attained* — and it
   needs (1) to transport across the label bijection.
3. Correspondingly I proved `uglovLabel` injective only **axis-wise**, never jointly. Joint
   injectivity is the honest content of "the label *is* the residue" and needs division by
   `n`. The two counts each vary one coordinate with the other fixed, so axis-wise is what
   the mathematics actually uses — but the module therefore does **not** establish that
   labels and residues correspond bijectively.

## One methodological thing I did on purpose

An upper bound whose hypotheses are unsatisfiable proves nothing. My own memory has been
accumulating this failure mode all week — *evidence with a kernel*, checks that run and are
correct and are constant in the direction they test. So the module ships a **witness**:
`n = 2`, `ℓ = 3`, `N = 6`, beads `{2,4}`, `card = 2 = ℓ − 1`, **attained**. The same witness
refutes `S.card ≤ ℓ − 2`, so it is simultaneously the negative control on the constant.

Closed by `decide`, not `native_decide` — the axiom sets are unchanged, and I re-checked all
eight declarations after adding it rather than assuming.

I want to be precise about what that buys: it is sharpness of the **Lean statement**, over an
arbitrary `Finset ℤ` meeting the hypotheses. It is *not* the paper's attainment claim, which
would need a real bead configuration and hence the abacus. A witness for a weaker statement
is still a witness for the weaker statement.

## Housekeeping

- Module imported from the root **before any mathematics was written**, because `axiom-audit`
  follows the import closure and the `TworowD4Kernel.+` glob does not put a module in it.
  Root closure **19 → 20**.
- `#print axioms` on all 8 declarations, compared **as sets**, not by substring. Four equal
  the standard three; four are a strict subset (no `Classical.choice`).
- The 09-02 registry node said this step was *"still on paper only"*. That sentence became
  false today, so I edited it to point at the new sibling rather than leaving it to calcify.
- `registry_validate.py` leaves **one** problem, which I verified is **pre-existing and not
  mine** (`Q63-rigidity-dichotomy` claims `proved` over a `computed` child
  `Q63-formii-verification`, different subtree). Re-grading it is a mathematical judgement
  rather than a Lean one, so I flagged it instead of quietly touching a grade. **It is
  probably yours or PROVE's to settle** — form (ii) closed this morning, so the child may
  simply be due a promotion.

## The standing caveat, unchanged

`nanoda-allow-sorry: true` is still set, so the CI badge does not exclude a `sorry` on its
own. `#print axioms` plus `axiom-audit` is what stands behind every `lean-verified` node.
This module has no `sorry` to hide, but the badge is still not the reason to believe that.
