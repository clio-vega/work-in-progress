# For Robin: extended sign-kill for hat_lambda = (5, 2) — proved (2026-05-14, tenth session)

## TL;DR

Tenth prove session of May 14, building on the eighth-session (4, 3) and
sixth-session (4, 2) results. **The extended sign-kill conjecture for
hat_lambda = (5, 2) is now proved in the containment direction at the
predicted threshold tau = q - 4, for q >= 5.** Combined with the
eighth-pass (4, 3) paper, the |hat_lambda_1 + hat_lambda_2| = 7 row of
the recursive ladder is now complete.

For lambda = (5, 2, 1^q) with q >= 5:
- B subset E_j^- for j = 1, ..., q - 4 (containment, fully rigorous)
- B subset E_ell^+ universally with T_ell = q*Id (May-13 evening)

Sharpness at j = q - 3 verified computationally at q = 5.

Paper: `2026-05-14-extended-sign-kill-52.tex` (9 pp).

## What's new structurally

The (5, 2) shape has r = 2 (three removable corners) like (4, 3), so the
E^+_{n-1} decomposition is four-piece. But unlike (4, 3) where only one
of the four inner shapes was a hook, **(5, 2) has TWO hook branches**:

| Piece | inner shape         | role           | input                      |
|-------|--------------------|----------------|----------------------------|
| Phi_A | (4, 2, 1^{q-1})    | contributes    | (4, 2) ext sign-kill (May-14 6th) |
| **Phi_B** | **(5, 1^q)**       | **contributes**| **hook support lemma (May-14 5th)** |
| Phi_C | (4, 1^{q+1})       | vanishes       | hook column-1 (May-12)     |
| Phi_h | (3, 2, 1^q)        | vanishes       | (3, 2) ext sign-kill (May-14 5th) |

The new feature: **Phi_B is the first hook branch in the May-14 series
that CONTRIBUTES rather than vanishes**. The mechanism: Phi_B's hook
shape has ell(mu_B) = q + 1 = n - 6, so its inner Omega^(mu_B) has the
right number of blocks to align with the two-branch reduction. The
hook support lemma at k=5, m=q gives prefix bound m - k + 2 = q - 3,
matching the (4, 2)-recursive prefix bound on Phi_A.

Dim arithmetic: 4 = f^(4,1) = 3 + 1 = f^(3,1) + f^(4) = dim Phi_A(I_A) +
dim Phi_B(I_B). The hook branch contributes exactly 1 to dim B.

## Why the hook count flips between (4,3) and (5,2)

For lambda = (5, 2, 1^q), lambda_2 = 2 is small enough that the
same-row strip at c_1 = (1, 5) leaves (3, 2, 1^q) — non-hook. The
hook piece is the corner-pair {c_2, c_3} stripping → (5, 1^q).

For lambda = (4, 3, 1^q), lambda_2 = 3 is large enough that the
same-row strip at c_1 = (1, 4) is FORBIDDEN by the column-3 constraint
T(1, 3) < T(2, 3) (cell (2,3) exists, forces T(2,3) > n-1, impossible).
The hook piece is the same-row strip at c_2 = (2, 3) leaving
(4, 1^{q+1}).

Both shapes have 4 pieces total; the hook count is shape-dependent.

## Sharpness witness at q = 5

dim V = 1728, dim B = 4, min prefix in supp(B) = 2 = q - 3.

Explicit witness with p(T) = 2 (column 1 starts with 1, 2, then breaks):
```
T(1, .) = (1, 3, 4, 5, 6)
T(2, .) = (2, 7)
T(3..7, 1) = (8, 9, 10, 11, 12)
```
Column-1 entries: (1, 2, 8, 9, 10, 11, 12). Prefix length = 2 exactly.

## Stability ladder for (5, 2, 1^q)

| q | dim V | dim B | predicted tau | regime |
|---|-------|-------|---------------|--------|
| 1 |    ?  |   ?   |     q - 4 = -3 | non-stable |
| 2 |    ?  |   ?   |    q - 4 = -2 | non-stable |
| 3 |   448 |   4   |     q - 4 = -1 | stable, pre-threshold |
| 4 |   924 |   4   |     q - 4 = 0  | stable, vacuous threshold |
| 5 |  1728 |   4   |    **q - 4 = 1** | **first non-vacuous** |

So q = 5 is the boundary where the conjecture first makes a non-vacuous
prediction, and it holds. Both the May-13 (5,2) j-formula paper (dim B
= 4 and B ⊆ E_1^- at q ≥ 5) and this paper assume q ≥ 5.

## Recursion graph now

```
(2,2) [base via support rule]
 ↓
(3,2), (4,2)   [recurse on (2,2)]
 ↓
(3,3)   [recurses on (3,2) for mu_A; hook column-1 for mu_h]
 ↓
(4,3)   [recurses on (3,3) AND (4,2); (3,2) AND hook for vanishers]
 ↓
(4,4)   [recurses on (4,3) for mu_A; on (4,2) for mu_h vanishing]
                                       ↘
                                        ↘
(5,2)   [recurses on (4,2) for mu_A; HOOK SUPPORT for mu_B; (3,2) and
         hook column-1 for vanishers] ← THIS PAPER
```

The first row of the |hat-lambda| <= 8 stratum is now closed:
- |hat| = 4: (2,2)
- |hat| = 5: (3,2)
- |hat| = 6: (4,2), (3,3)
- |hat| = 7: (4,3), **(5,2)** ← this paper closes the row
- |hat| = 8: (4,4) — proved. Open: (5,3).

## Updated status table

| hat_lambda | predicted tau | status                              |
|------------|---------------|-------------------------------------|
| (2, 2)     | q - 1         | proved (May-14 fourth pass)         |
| (3, 2)     | q - 2         | proved (May-14 fifth pass)          |
| (4, 2)     | q - 3         | proved (May-14 sixth pass)          |
| (3, 3)     | q - 3         | proved (May-14 seventh pass)        |
| (4, 3)     | q - 4         | proved (May-14 eighth pass)         |
| (4, 4)     | q - 5         | proved (May-14 ninth pass)          |
| **(5, 2)** | **q - 4**     | **proved (this paper, q >= 5)**     |

## On (5, 3) — the last |hat-lambda| = 8 case

lambda = (5, 3, 1^q). Three corner pairs (3 corner-pair pieces) PLUS
potentially TWO same-row pieces (one at c_1 leaving (3, 3, 1^q),
one at c_2 leaving (5, 1^{q+1}) hook). So FIVE-piece decomposition,
not four. Inputs needed for contributing branches:
- mu_{12} = (4, 2, 1^q): (4, 2) ext sign-kill at q' = q. Need q ≥ 4.
- mu_{13} = (4, 3, 1^{q-1}): (4, 3) ext sign-kill at q' = q - 1. Need q ≥ 6.
- mu_{23} = (5, 2, 1^{q-1}): (5, 2) ext sign-kill at q' = q - 1 — THIS PAPER. Need q ≥ 6.

Same-row pieces are likely vanishers (mu_h^1 = (3, 3, 1^q) uses (3, 3);
mu_h^2 = (5, 1^{q+1}) hook column-1). Predicted tau = q - 5. Hypothesis
likely q >= 6.

This would be the natural next session target.

## Push status

**71 unpushed commits** on clio-vega/proofs (after today's 10th-pass
commit). PAT issue from May 6 persists — please refresh when convenient.

## Questions for you

1. **(5, 3) next, or shift focus?** The recursion ladder has a natural
   next step but it's getting bookkeeping-heavy. Five-piece
   decompositions and three recursive inputs per case suggest the
   marginal benefit per session is dropping. Maybe time to step back
   and think about whether the threshold formula
   tau = q + 3 - hat_1 - hat_2 has a structural proof rather than
   case-by-case recursion.

2. **The hook-as-contributor phenomenon.** (5, 2) is the first case
   where a hook branch contributes rather than vanishes. The hook
   support lemma's prefix bound m - k + 2 matches the prediction
   exactly. Is there a unified principle here — does every
   contributing branch's prefix bound coincide with the parent's?

3. **The PROVE.md target is long dead.** PROVE.md is still pointing
   at the induced-module image conjecture (refuted morning of May 14).
   It might be worth updating it to point at the live frontier
   (extended sign-kill, sharpness, threshold formula).

## Files

- Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-52.tex` + `.pdf` (9pp)
- Scripts: `~/projects/scratch/2026-05-14-extended-sign-kill-52/`
  - `verify_decomp.py` — four-piece dim sum at q ∈ {3, 4, 5}
  - `verify_q5_sparse.py` — B ⊆ E_1^- + sharpness witness at q = 5
  - `verify_prefix_small.py` — pre-threshold behavior at q ∈ {3, 4}
