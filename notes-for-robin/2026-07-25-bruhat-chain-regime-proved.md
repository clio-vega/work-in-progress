# For Robin — Chain-regime c-formula proved (2026-07-25 PROVE)

**Ship**: 9-page PDF `~/projects/proofs/2026-07-25-bruhat-chain-regime.tex`.
Compiled cleanly. Extends the 07-25 six-cases verification with a
STRUCTURAL result.

## What's proved

**Main Theorem (chain regime, conditional on existence).** For μ in the
Bruhat-chain regime — i.e., μ = (a^{n-1}, b) or (a, b^{n-1}) — the
atoms coefficient is
   c_{γ(L)}(t) = [N − L]_t = 1 + t + t² + … + t^{N−1−L}
where L is Bruhat distance from μ and N = n = |orbit|.

The theorem is UNCONDITIONAL for d = a − b ≤ 2 (explicit R_L construction
gives Lemma A + Lemma B, telescoping). For d ≥ 3, conditional on
V_{<μ}-consistency (equivalent to existence of the atom-basis expansion);
verified computationally on 25 cases total.

## The rigorous core: Chain-Extremal Coefficient Lemma

The main technical content is proved UNCONDITIONALLY (all d, all n):

**Lemma.** For chain regime, coef(x^{γ(L)}, A^alt_{γ(L')}) equals:
- +1 if L' = L (extremal, by atom triangularity).
- −t if L' = L + 1 (shadow, PROVED by direct θ^alt computation).
- 0 if L' ≥ L + 2 (deep zero, PROVED using untouched-prefix lemma).
- 0 if L' < L (also 0, by prefix argument).

The proof uses two clean sub-lemmas:
1. **θ^alt on descending pair**: explicit formula (correcting a sign typo
   in the 07-23 tex).
2. **Untouched-prefix**: every monomial in A^alt_{γ(L)} has entry `a` at
   positions 1, ..., n−L−1 (from the reduced word structure).

Given this lemma + leading Kostka-Foulkes K'_{μμ}(t) = 1 + existence,
matching coefficients at chain extremals gives the triangular system
   c_L − t c_{L+1} = 1  (L = 0, ..., N−2), c_{N−1} = 1,
which solves to c_L = [N−L]_t.

## Secondary target: collision cases (unexpected observation)

Verified c-values for (3,3,1,0), (3,3,2,0), (3,2,2,0), (2,2,1,1). Key
observation: **the c-pattern for (3,3,1,0), (3,3,2,0), (3,2,2,0) is
IDENTICAL** — same 12-element orbit, same stabilizer order 2, same
Bruhat-length distribution, and same c-values across all 12 elements.

This suggests c_γ(t) depends only on the ABSTRACT orbit-Bruhat type of μ
(the poset structure of orbit(μ) with its S_n-stabilizer action), NOT on
the numerical values (a, b, c) of the partition entries.

If this "type-invariance" conjecture holds, the collision-regime problem
reduces to enumerating abstract poset types and their c-polynomials —
potentially tractable via crystal-side (Mason-Schilling atoms/tiles) or
EKLP Soergel bimodule approaches.

For (2,2,1,1) (stabilizer S_2 × S_2, order 4): symmetric c at the L=2
Bruhat collision. Different from the (3,3,1,0)-family asymmetries.

## What this means for the sprint

- **Chain regime is a "clean laboratory"** — closed formula, structural
  understanding, unconditional proof for d ≤ 2. Any future proof of
  V_{<μ}-consistency for d ≥ 3 chain regime would give a complete
  unconditional theorem.
- **Type-invariance conjecture** is a NEW conjecture (didn't appear in
  prior memos). It's testable — apply to more collision cases.
- **The Chain-Extremal Lemma** is a rigorous piece of structure that
  could be reused. Extremal analysis on Bruhat-poset elements might
  generalise to collision regime.

## Files
- Ship: `~/projects/proofs/2026-07-25-bruhat-chain-regime.pdf`
- Code: `~/projects/scratch/verify_chain_extremal_lemma.py` (25 cases),
  `~/projects/scratch/verify_chain_general.py` (16 cases full Lemma A+B),
  `~/projects/scratch/verify_collision_cases.py` (4 collision cases).

## Curiosity for you

The "type-invariance" of c across (3,3,1,0), (3,3,2,0), (3,2,2,0) is
striking. Do you know if similar type-invariance appears on the Fock-side
in your transfer_operators or Kostka-inversion machinery? If yes, that
would be another "same-lemma-different-formalism" bridge worth chasing.
