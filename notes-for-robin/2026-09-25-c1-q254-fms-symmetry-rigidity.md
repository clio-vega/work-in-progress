# Q254 — FMS Theorem 7 does not reach the cylindric theorem, and the reason is a theorem

**2026-09-25 c1 (PROVE).** Robin — the novelty question on my largest artifact is closed, and it
closed in an interesting direction.

**Artifacts (pushed, commit `5511463`):**
- paper — https://github.com/clio-vega/proofs/blob/main/2026-09-25-c1-fms-and-cylindric-exchange.tex
- pdf — https://github.com/clio-vega/proofs/blob/main/2026-09-25-c1-fms-and-cylindric-exchange.pdf (13pp)
- code — https://github.com/clio-vega/proofs/tree/main/code-q254

(Both URLs checked by me for HTTP 200 this session; the hash was printed by `git rev-parse`, not
typed from recall.)

## The question

`proofs/2026-09-20-c1-cylindric-M-convexity.tex` computes a saturated Newton polytope for
cylindric skew Schur polynomials. Fink–Mészáros–St.~Dizier (`1706.04935`, Adv. Math. 2018)
Theorem 7 computes a saturated Newton polytope for the dual character `χ_D` of the flagged Weyl
module of **any** diagram `D`, with no hypothesis whatsoever. If a cylindric skew shape's columns
are a diagram in their sense, my theorem is a 2018 corollary. I had cited "FMS Thm 7" in every
M-convexity proof I have written and had **never read the paper at first hand.** I have now read
all 328 lines of the e-print source.

## The answer

**Symmetry rigidity.** For a diagram `D` with `m = max ⋃_j D_j`: `supp(χ_D)` is stable under the
`S_m` permuting the coordinates it occupies **iff** every nonempty column equals
`{m−|D_j|+1, …, m}` (is bottom-justified).

The proof is elementary and short. `supp(χ_D)` has a partial-sum *minimum* (the row-count vector
`ξ^D`) and a partial-sum *maximum* (the top-justified filling). Symmetry forces the minimum weakly
increasing and the maximum weakly decreasing, and forces both to be dominance-maximal — so they
are reverses of each other. That identity holds termwise over the columns, and evaluating it at
`k = |D_j|` pins each column to the bottom.

Two consequences:

1. **FMS Theorem 7 has no symmetric content beyond Rado (1952).** Bottom-justified columns give
   *uniform* matroids, whose polytopes are hypersimplices, and a Minkowski sum of hypersimplices
   is a permutahedron. So on symmetric dual characters Theorem 7 says exactly
   `supp(s_λ̂) = P_λ̂ ∩ ℤ^m`. Their generality lives entirely in the non-symmetric directions.

2. **The circularity is exact.** Any diagram `D` with
   `supp(χ_D) = supp(s^c_{λ/μ}(x_1..x_ℓ))` has `λ̂` as the conjugate of its column-size
   partition. So *exhibiting the diagram is computing `λ̂`* — the diagram is not an auxiliary
   object from which `λ̂` is later extracted; `λ̂` is literally its column sizes, conjugated.
   FMS returns `λ̂` only if it is fed `λ̂`.

**The registry node is not demoted on novelty.** I promoted the obstruction to a standalone
proposition and asked what would falsify it (a diagram with symmetric support and a column that
is not bottom-justified); an exhaustive search over 113,621 diagrams found none, and the proof
says why none exists.

## What I got wrong in my own brief, and it was two things

My PROVE brief named two structural obstructions in bold. **Both are false.**

- *"FMS's variable count is welded to the grid, so the two sides see different data."* False:
  put every column inside `[ℓ]` and pad with empty columns — `D_j = {2}` repeated `N` times gives
  `χ_D = h_N(x₁,x₂)`, two variables and unbounded degree.
- *"FMS import the exchange axiom non-constructively at l.190 via Schrijver Cor. 46.2c."* Wrong
  three ways. l.190 is the *definition* of a matroid in a background section; no exchange
  verification occurs anywhere in FMS (Schubert matroids are matroids by a cited classical fact).
  The genuine non-constructive import is Schrijver Cor. 46.2c at **l.274**, a different statement
  (integer decomposition for polymatroids, which yields SNP). And the clause "for `D_j` a column
  of a cylindric skew shape" presupposes the dictionary that does not exist.

Both are recorded as dead ends in the registry with reasons. The pattern is one I have hit before
and keep hitting: a *reason for* a claim is never the object of a check. A blocker stated in a
brief is the worst case, because it says why something can't be done, so nobody tries.

## Two things worth your attention beyond the mathematics

**(a) The natural dictionary fails already at `d = 0`, with a two-box witness.** For `λ = (2,1)`,
`μ = ∅`, `ℓ = 2`: the column diagram is `({1,2},{1})` and `supp(χ_D) = {(2,1)}`, while
`supp(s_{21}(x₁,x₂)) = {(2,1),(1,2)}`. The reason is pretty — the straight shape drawn at the
top-left of the grid is the skyline diagram of the **dominant** composition, and
`κ_{(2,1)} = x₁²x₂`. It is the *antidominant* placement that gives a Schur polynomial, and a
genuinely skew shape has no antidominant placement. Across 486 skew shapes the natural dictionary
fails in 320, and the 166 that succeed are *exactly* the 166 with symmetric `supp(χ_D)`.

**(b) Cylindric skew Schur functions are not Schur-positive**, so the soft route
(Schur-positive ⇒ support is a union of Schur supports ⇒ SNP by Rado) is unavailable. Smallest
instance in my sample: `n=3, m=1, μ=(0), λ=(3), ℓ=3`, where `s^c = s_{21} − s_{111}`. Same
phenomenon as WZZ's Example 4.2. Monomial positivity survives; Schur-basis cancellation is real.

## Two tooling defects, both of which made a check silently vacuous

These cost me time this session and I would rather you knew.

1. **`trustcheck --files-dir` is not a fixed value, and my own brief told me the wrong one.**
   The brief said, in bold, *"`--files-dir proofs` … do not use `--files-dir .`"*. I ran both
   against all ten of my registries: **nine need `.` and exactly one needs `proofs`** — and that
   one is the registry the brief was verified against yesterday. Using `proofs` everywhere
   produces 464 spurious "file not found". The correct rule is a *kind*, not a value: the flag
   must be the directory from which that registry's own stored `file` paths resolve. I normalised
   the odd registry out, so a single `--files-dir .` now validates all ten.

2. **The source-extraction gate is defeated by a locator suffix.** The validator refuses a
   `proved` node whose sources are all below `abstract` — but *only* when the `sources` entry is a
   **bare** arXiv id. `"1706.04935 Thm 7 (forArxiv.tex l.253-258)"` fails to resolve, degrades to
   a soft "not in the sources index" warning, and the gate then never fires. I probed it both ways
   to be sure. **Every node in all ten of my registries carries locator-suffixed ids only**, so the
   gate has been vacuous across the whole system. My new node now carries both forms and I
   confirmed the gate binds by lowering the grade and watching it refuse. The wider repair — giving
   every existing node a bare id alongside its locator — is owed and not done.

## Two defects in FMS itself, recorded because I am citing them

- **l.147 is a typo.** The skyline diagram is printed as `D(α)_j = {j ≤ n : α_j ≥ j}`; the bound
  variable is wrong and the intended formula is `{i ≤ n : α_i ≥ j}`. Forced by their own preceding
  sentence and their own Figure 2. My corrected reading is validated independently by 698
  divided-difference key-polynomial computations — with the printed formula the test fails at once.
- **Their bibliography swaps two entries' titles**, and `\cite{keypolynomials}` — the key cited for
  their Theorem 5 — is misattributed to Demazure. **FMS Theorem 5 is due to Reiner–Shimozono**,
  JCTA 70 (1995) 107–143. (An agent read had found this on 09-24; I have now confirmed it myself
  in `forArxiv.bbl` l.24–33.)

## Honest gaps

- The verdict is about **direct** application of Theorem 7 to `s^c`. It does not exclude an
  indirect argument using Theorem 7 as one ingredient — e.g. a decomposition
  `s^c = Σ_D c_D χ_D`. I have not investigated those and do not claim they are impossible; I note
  only that by (b) above the `c_D` could not be assumed nonnegative. Recorded as an open question,
  not a claim.
- `χ_D = κ_α = s_λ̂` as **polynomials** (not merely supports) cites FMS Theorem 5, i.e.
  Reiner–Shimozono, which I have not read. Nothing load-bearing uses it; every essential statement
  here is about supports and the support version is proved.
- FMS Theorem 10 (the Schubitope) computes the same polytope, so symmetry rigidity applies to it
  verbatim, but I have not written that out.

## Verification summary

| check | instances | result |
|---|---|---|
| my transcription of FMS's definitions vs. divided-difference Schubert + key polynomials | 850 | 850/850 supports agree |
| symmetry rigidity, exhaustive, both directions + the `λ̂` identification | 113,621 diagrams | 0 failures |
| natural column dictionary at `d = 0` | 486 skew shapes | 320 fail; the 166 that pass are exactly the symmetric ones |
| tested range genuinely winds (relaxing the wrap constraint changes the support) | 488 | 199 wind |
| control on `thm:main` over winding instances | 199 | 199/199 |
| exhaustive diagram search, winding instances only | 36 classes | 36/36 have exactly one solution, the `λ̂`-skyline |
| negative control: drop one column | 151 | 151/151 break |
| negative control: move one box up one row | 158 | 158/158 break |

One control I ran and then **discarded rather than reported**: reversing the column order.
`supp(χ_D)` is a sumset over columns, so it is invariant under reordering *by construction* —
nothing about the world could make that control fail, so reporting it as passing would have been
reporting nothing.

— Clio
