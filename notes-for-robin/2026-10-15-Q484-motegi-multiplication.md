# Q484 — Motegi's type B/C weight functions: a multiplication rule, and a stratified obstruction

**PROVE 2026-10-15.** Writeup: `proofs/2026-10-15-Q484-motegi-puzzle-Gm.tex` (compiles,
342,219 B PDF). Registry: `proofs/registry/motegi-typeBC-multiplication.json`
(`trustcheck` OK, status `proved`, 2-arm control on the validator both arms firing).

## What I set out to do, and what the gate did to it

The brief asked for a type-A `G_m` puzzle with a reflecting edge, structure constants read
off the configurations touching that edge, closed by Motegi's uniqueness theorem. I ran the
§0 parameter census first, before any code. It redirected the session, and I think
correctly:

1. **The brief's pre-registered falsifier is unusable.** It said a type-A puzzle produces
   no `u_j u_k` coupling, so a rule with no boundary piece would refute either the rule or
   the formal-group connection. The coupling claim is right; the inference is not. Motegi's
   crossings are literally `R(u_i, u_j^{-1})`, and `R` sees only the ratio
   `u_j^{-1}/u_i = (u_i u_j)^{-1}`. A type-A R-matrix whose second alphabet is the *inverse*
   of the first already produces the coupling. I drew no inference from this row.
2. **The row that actually separates the objects is a different one.** Wheeler–Zinn-Justin's
   type-A `G_m` puzzle is the `q = 0` five-vertex degeneration — zero free deformation
   parameters — while Motegi's characterisation theorems have `q` free. Same formal group,
   different point of the quantum parameter inside it.
3. **The census table had one row for two groups.** There are two symmetry groups on each
   side. On the one the brief compared — `S_n` on the `u`-alphabet, type A, `sgn = 0` — the
   two objects *agree*. The group carrying the type-B/C-ness is `W(X_N)` of rank `N` acting
   on the `w`-alphabet, and it is the one whose inversion and ascent sets write the diagonal
   evaluation as a product over positive roots.

## What I proved

In the **fixed-point algebra** `V` = functions on the `2^N` specialisation points
`u = w_M`, `M ⊆ [N]`, with pointwise product:

- **Lemma.** The specialised weight functions `e_I : M ↦ \widetilde{WX}(w_M|w|I)` form a
  basis of `V` (triangularity in Motegi's order `≥`, which I check is a partial order, plus
  a nonzero diagonal). Independently corroborated by Motegi's own explicit matrix inverse.
- **Theorem A.** `c^ν_{λμ} ≠ 0 ⟹ ν ≥ λ and ν ≥ μ` — the type-B/C analogue of
  `ν ⊇ λ, μ`. Well-founded induction, no computation. Measured 64/64 and 512/512.
- **Theorem B.** A well-founded recursion determining every `c^ν_{λμ}` from Motegi's
  specialisation values alone.
- **Corollary C.** At any `ν` minimal in `{κ ≥ λ, κ ≥ μ}` the coefficient is a closed
  quotient; if `λ ≥ μ` then `c^λ_{λμ} = \widetilde{WX}(w_λ|w|μ)`; and
  `c^λ_{λλ} = ∏_{α∈Inv(λ)}(1-e^{-α}) ∏_{α∈T(λ)}(1-qe^{α})` — a product over positive roots.
- **Theorem D.** A closed `2^N`-term localisation formula via Motegi's explicit inverse.
  Soft: not manifestly supported, positive, or polynomial. Reported as such.

## The two negatives, and why they are the more useful half

- **Theorem E.** The identity does **not** lift to functions of `u`: at `N = n = 2` it fails
  for all 16 pairs at a generic point. The rule lives in the localized picture.
- **Theorem F + Conjecture.** The coefficients are **not Laurent polynomials**, and the
  failure locus is sharp:

  > `c^ν_{λμ}` is Laurent in `w` **iff** `|ν| − max(|λ|,|μ|) ≤ 1`.

  Measured against **every** triple permitted by Theorem A at `N = 2, 3` — 225 of them —
  with zero false positives and zero false negatives. Smallest witness
  `c^{(1,2)}_{∅,∅}` at `N=2`, a simple pole on `w_1w_2 = 1`, the hyperplane of the root
  `t_1+t_2 ∈ Δ^+(C_2)`.

A puzzle counts tilings with monomial weights and therefore yields a Laurent polynomial.
So the kill on the puzzle route is **stratified**: excluded at cardinality jump `≥ 2` in this
normalisation, still open on the jump-`≤1` stratum. That is the brief's own fork resolved on
the *wrong normalisation* side, **not** against the `G_m` formal group. And no diagonal
rescaling fixes it — `g_I = Δ_I` drops the Laurent count from 29/30 to 4/30.

**New question, Q491** (allocator read-and-bumped 491→492): in which normalisation are the
structure constants Laurent polynomials at all jumps?

## Two things I'd like you to be sceptical about

1. **A control of mine could not fire over its domain, and only a plant revealed it.**
   My diagonal control (brute-force `S_n` sum vs product over positive roots, 14/14 at
   `N=1,2,3`) cannot see a plant in the factor `(u_ju_k - q)`, because at `M = I` we have
   `s = r`, hence `n = r`, hence the range `r+1 ≤ j<k ≤ n` is **empty** — three of the seven
   product blocks of Motegi's symmetrisation formula are absent from the diagonal's domain.
   A clean 14/14 validated **4 of 7 blocks**. I built a second control (his cross-sector
   branching theorem, clean 27/27) specifically to cover that domain; it does fire on the
   plant, 1/5 and 7/22. I would not have found this without planting, and I had already
   written the 14/14 up as a pass.
   Separately, Motegi's biorthogonality is **insensitive to both plants** (each passes 16/16
   while demonstrably altering matrix entries) — reported as a check on my implementation of
   his theorem, not on the engine.
2. **I graded the imported facts unequally and I want that checked.** (M1) — triangularity
   plus the explicit nonzero diagonal product — I graded `proved`: I read its proof in full
   (his L620–790). (M2), the root-theoretic *rewriting* of that same diagonal, has its proof
   deferred to his §3, which I did **not** read; (M4)'s proof I read only in part. Both are
   graded `computed`. I then restructured the registry so the main rule leans only on (M1),
   with (M2) needed for Corollary C(iii) alone and (M4) for Theorem D alone. The validator
   flagged my first attempt, which had all three at `unclassified` under a `proved` root —
   it was right, and the restructuring is my answer to it. Tell me if you think the split is
   self-serving.

Everything is type **C**. No type-B run was performed; nothing in the proofs distinguishes
the types, but the negatives and the criterion are untested for `B`.

## Links (pushed — you can read these)

- writeup: https://github.com/clio-vega/proofs/blob/main/2026-10-15-Q484-motegi-puzzle-Gm.tex
- PDF: https://github.com/clio-vega/proofs/blob/main/2026-10-15-Q484-motegi-puzzle-Gm.pdf (343,365 B)
- registry: https://github.com/clio-vega/proofs/blob/main/registry/motegi-typeBC-multiplication.json
- verification code + README: https://github.com/clio-vega/proofs/tree/main/code-1015-q484
- commit `ede369e` on `main`

## A third thing to be sceptical about, caught by the trajectory validator

My trajectory had `evt-0013` ("N=2: Thm A 64/64, Cor C 10/10, Thm D 64/64") listing the
*theorems* as its input rather than the engine, and `tracecheck` flagged it
**circular-verification**. The wiring was wrong, and fixing it exposed a real distinction I had
flattened: the coefficients are computed **by** Theorem B's recursion, so of the three checks
only two are worth anything and only one is independent —

- **Theorem A against recursion-computed values: a real test.** The support bound is a
  consequence of the defining identity and (M1), not of the recursion.
- **Corollary C against them: tests only my derivation** `A + B ⟹ C`, not the engine.
- **Theorem D against them: genuinely independent.** D reaches `c` from (M4) and the basis
  lemma by a route that never passes through the recursion — two routes to the same vector.

I had reported all three as equal. The paper now says which is which (§5, after the main
numbers). `evt-0021` records the correction rather than overwriting the flagged event.
