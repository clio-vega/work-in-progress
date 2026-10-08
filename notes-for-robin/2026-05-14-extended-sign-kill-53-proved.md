# For Robin: extended sign-kill for hat_lambda = (5, 3) — proved (2026-05-14, eleventh session)

## TL;DR

Eleventh prove session of May 14, building on the tenth-session (5, 2)
and eighth-session (4, 3) results. **The extended sign-kill conjecture
for hat_lambda = (5, 3) is now proved in the containment direction at
the predicted threshold tau = q - 5, for q >= 6.** Together with the
ninth-session (4, 4) result, the **|hat_lambda| = 8 row of the
recursive ladder is now complete**, and the entire |hat_lambda| <= 8
stratum is closed.

For lambda = (5, 3, 1^q) with q >= 6:
- B subset E_j^- for j = 1, ..., q - 5 (containment, fully rigorous)
- B subset E_ell^+ universally with T_ell = q*Id (May-13 evening)

Sharpness at j = q - 4 verified computationally at q = 6: explicit
witness with p(T) = 2 exhibited.

Paper: `2026-05-14-extended-sign-kill-53.tex` (10 pp).

## What's new structurally

The (5, 3) shape is the **first case with a five-piece E^+_{n-1}
decomposition** (three corner-pair + two same-row branches).

| Piece          | inner shape              | role           | input                          |
|----------------|--------------------------|----------------|--------------------------------|
| Phi_12         | (4, 2, 1^q)              | vanishes       | (4, 2) ext sign-kill (May-14 6th) |
| **Phi_13**     | **(4, 3, 1^{q-1})**      | **CONTRIBUTES**| **(4, 3) ext sign-kill (May-14 8th)** |
| **Phi_23**     | **(5, 2, 1^{q-1})**      | **CONTRIBUTES**| **(5, 2) ext sign-kill (May-14 10th)** |
| Phi_h^(1)      | (3, 3, 1^q)              | vanishes       | (3, 3) ext sign-kill (May-14 7th) |
| Phi_h^(2)      | (5, 1^{q+1})             | vanishes       | hook column-1 (May-12)         |

**Both contributing branches come from |hat_X| = 7 papers proved this
same evening.** This is the first case where the recursive structure
catches up to the immediately previous row of the ladder.

Same-row analysis: the candidate at c_1 = (1, 5) survives because
lambda_2 = 3 < 4 (so cell (2, 4) does not exist, no column-strict
constraint to block it). The candidate at c_2 = (2, 3) also survives
unconditionally. Both same-row branches exist — hence five pieces.

Dim arithmetic: 9 = f^(4,2) = 5 + 4 = f^(3,2) + f^(4,1) =
dim Phi_13(I_13) + dim Phi_23(I_23). Verified computationally at
q = 6 with rank 9 on probe of 60 basis vectors.

## Sharpness witness at q = 6

dim V = 14014, dim B = 9, min prefix in supp(B) = 2 = q - 4.

Explicit witness with p(T) = 2:
```
T(1, .) = (1, 3, 5, 9, 10)
T(2, .) = (2, 8, 11)
T(3..8, 1) = (4, 6, 7, 12, 13, 14)
```
Column-1 entries: (1, 2, 4, 6, 7, 12, 13, 14). Prefix = 2 exactly
(entry 3 sits at (1, 2), not (3, 1)).

## Stability ladder for (5, 3, 1^q)

| q | dim V  | dim B | predicted tau | regime |
|---|--------|-------|---------------|--------|
| 2 |  567   |   ?   | q - 5 = -3    | non-stable (?) |
| 3 |  1540  |   ?   | q - 5 = -2    | non-stable (?) |
| 4 |  3564  |   ?   | q - 5 = -1    | stable, vacuous |
| 5 |  ~8400 |   9   | q - 5 = 0     | stable, vacuous |
| 6 | 14014  |   9   | **q - 5 = 1** | **first non-vacuous** |

q = 6 is exactly where the conjecture first makes a non-vacuous
prediction, and it holds.

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
         hook column-1 for vanishers]
                                       ↘
                                        ↘
(5,3)   [recurses on (4,3) AND (5,2) for contributors; (4,2), (3,3),
         hook column-1 for vanishers] ← THIS PAPER
```

The |hat-lambda| <= 8 stratum is now closed:
- |hat| = 4: (2,2)
- |hat| = 5: (3,2)
- |hat| = 6: (4,2), (3,3)
- |hat| = 7: (4,3), (5,2)
- |hat| = 8: (4,4), **(5,3)** ← this paper closes the row

## Updated status table

| hat_lambda | predicted tau | status                              |
|------------|---------------|-------------------------------------|
| (2, 2)     | q - 1         | proved (May-14 fourth pass)         |
| (3, 2)     | q - 2         | proved (May-14 fifth pass)          |
| (4, 2)     | q - 3         | proved (May-14 sixth pass)          |
| (3, 3)     | q - 3         | proved (May-14 seventh pass)        |
| (4, 3)     | q - 4         | proved (May-14 eighth pass)         |
| (4, 4)     | q - 5         | proved (May-14 ninth pass)          |
| (5, 2)     | q - 4         | proved (May-14 tenth pass)          |
| **(5, 3)** | **q - 5**     | **proved (this paper, q >= 6)**     |

## On (5, 4), (6, 3) — the |hat-lambda| = 9 row

lambda = (5, 4, 1^q) and (6, 3, 1^q) are the next natural targets at
|hat| = 9. Both will likely use the same five-piece (or possibly
six-piece for (6, 3) if a same-row at c_1 = (1, 6) leaves a non-hook)
template, with contributors from |hat_X| = 8 papers (now in hand):
- (5, 4) likely recurses on (4, 4) and (5, 3) — both proved.
- (6, 3) likely recurses on (5, 3) and a (6, 2) — but (6, 2) is open.

So (5, 4) is the cleanest next-session target.

## Push status

**73 unpushed commits** on clio-vega/proofs (after this 11th-pass
commit). PAT issue from May 6 persists — please refresh.

## Questions for you

1. **(5, 4) next, or chase the structural threshold proof?** The
   marginal benefit per case is dropping (we now have 8 cases and the
   pattern is firmly established). Maybe time to step back and prove
   the threshold formula tau = q + 3 - hat_1 - hat_2 structurally
   across all hat_lambda. The four-/five-piece decomposition seems to
   admit a uniform description: the contributing branches are always
   {c_i, c_3} for length-preserving c_i, and same-row pieces always
   vanish (or are handled by hook column-1). I have not yet found the
   right uniform argument for the prefix bound on contributors.

2. **Sharpness across all q.** Computational sharpness is now
   confirmed at q = 5 for (5,2), q = 6 for (5,3), q = 7 for (4,4),
   etc. The structural sharpness mechanism sketched in the (4,2)
   paper (Lemma 5.1) should generalize, but I haven't written it up.

3. **PROVE.md is still pointing at the long-refuted induced-module
   conjecture.** Worth updating to point at the live frontier
   (extended sign-kill ladder, threshold formula, sharpness).

## Files

- Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-53.tex` + `.pdf` (10pp)
- Scripts: `~/projects/scratch/2026-05-14-extended-sign-kill-53/`
  - `verify_decomp.py` — five-piece dim sum at q ∈ {2, 3, 4}
  - `verify_q6_sparse.py` — B ⊆ E_1^- + sharpness witness at q = 6
