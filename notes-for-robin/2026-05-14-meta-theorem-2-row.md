# For Robin: extended sign-kill meta-theorem for 2-row hat_lambda (2026-05-14, twelfth pass)

## TL;DR

**Your question 1 from the (5,3) note is answered for the two-row case.**

The extended sign-kill containment is now proved uniformly for every
hat_lambda = (a, b) with a >= b >= 2, at q >= a + b - 2:
$$B^{(\lambda)} V_\lambda \;\subseteq\; \bigcap_{j=1}^{q+3-a-b} E_j^-\!\mid_{V_\lambda}$$
where lambda = (a, b, 1^q).

This subsumes the eight case-by-case papers from passes 4-11 and closes
the entire 2-row stratum.  In particular it establishes:
- **(6, 2)** at |hat|=8: a gap from the prior series (never explicitly
  proved as its own pass).
- **(5, 4), (6, 3), (7, 2)** at |hat|=9: the entire next row.
- **(6, 4), (5, 5), (7, 3), (8, 2)** at |hat|=10 and beyond.

Paper: `2026-05-14-extended-sign-kill-meta.tex` (9pp).

## The argument in one paragraph

Strong induction on |hat_lambda| = a + b.  Base case (2, 2).  In the
inductive step, the $E^+_{n-1}$ decomposition of $V_\lambda$ splits
into **contributor pieces** (corner pair {c_i, c_3} with c_i
length-preserving; inner ell = ell(lambda) - 1; threshold preserved
exactly because removing a length-preserving corner subtracts 1 from
either hat_1 or hat_2 *and* from q simultaneously) and **vanisher
pieces** (corner pair {c_1, c_2} without c_3; same-row pieces at
length-preserving corners; inner ell = ell(lambda); have one extra
$R'_\ell^{(\mu)}$ block whose rightmost factor $(T_1+1)$ kills the
inductively known $E_1^-$ part).  Hook column-1 and hook support
handle the boundary cases (b=2, b=3) where inner shapes degenerate
to hooks.  Outer factors preserve the prefix bound.  Done.

## Why this works (the key combinatorial identity)

For a contributor mu_{i,3} obtained by removing a length-preserving
corner c_i and the bottom column-1 corner c_3, the inner shape has
$\hat\mu_1 + \hat\mu_2 = \hat\lambda_1 + \hat\lambda_2 - 1$ and the
trailing-1 count drops by 1 (q' = q - 1).  So
$\tau(\hat\mu_{i,3}) = (q-1) + 3 - (\hat\lambda_1 + \hat\lambda_2 - 1) = \tau(\hat\lambda)$.
**The threshold is preserved exactly.**  The inductive prefix bound
on the inner shape lifts to the outer one with no loss.

For b = 2, the boundary case where mu_{23} = (a, 1^q) is a hook,
the hook support lemma gives $p(T') \ge m - k + 2 = q - a + 2$,
which equals $\tau(\hat\lambda) + 1 = q + 4 - a - b = q - a + 2$
(using b = 2).  Same identity, different mechanism.

## Computational verification

| lambda            | n  | dim V | dim B | $(T_1+1)\Omega v = 0$? | min p | sharpness |
|-------------------|----|-------|-------|-----------------------|-------|-----------|
| $(6, 2, 1^6)$     | 14 | 8085  | 5     | yes                   | 2=q-4 | yes       |
| $(5, 4, 1^7)$     | 16 | 80640 | 14    | yes                   | 2=q-5 | yes       |
| $(6, 3, 1^7)$     | 16 | 82368 | 14    | yes                   | 2=q-5 | yes       |
| $(7, 2, 1^7)$     | 16 | 36608 | 6     | yes                   | 2=q-5 | yes       |

All four cases hit the predicted threshold exactly at first non-vacuous
$q$.  Scripts in `~/projects/scratch/2026-05-14-extended-sign-kill-meta/`.

## Status table after this paper

| hat_lambda           | |hat| | source                         |
|----------------------|-------|--------------------------------|
| (2, 2)               | 4     | base (May-14 fourth pass)      |
| (3, 2)               | 5     | subsumed by meta               |
| (4, 2), (3, 3)       | 6     | subsumed by meta               |
| (4, 3), (5, 2)       | 7     | subsumed by meta               |
| (4, 4), (5, 3), (6, 2)| 8    | subsumed; (6, 2) new           |
| (5, 4), (6, 3), (7, 2)| 9    | **new**: closes |hat|=9 row    |
| (a, b) for any a≥b≥2 | a+b   | meta-theorem                   |

## What remains open

1. **Multi-row hat_lambda** (corners in row >= 3): the threshold
   formula $\tau = q + 3 - \hat_1 - \hat_2$ is suspect.  Removing a
   row-k>=3 corner gives $\tau(\hat\mu) = \tau(\hat\lambda) - 1$
   (since $\hat_1, \hat_2$ unchanged but q drops), so the inductive
   bound is too weak.  Either:
   - The formula needs row-3+ correction terms.
   - Additional structural input compensates.
   Computational survey needed.

2. **Structural sharpness** ($B \not\subseteq E_{\tau+1}^-$): proved
   computationally case by case; the (4, 2) Lemma 5.1 mechanism
   should generalize, but a uniform structural proof is open.

3. **Dual Frobenius programme** (suggested in May-14 induced-image
   refutation note): still unexplored.

## Push status

After this twelfth-pass commit: **75 unpushed commits** on
`clio-vega/proofs`.  PAT issue from May 6 persists (read-only token,
git push returns 403).  Please refresh when you have a moment.

## Files

- Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-meta.tex` + `.pdf` (9pp)
- Scripts: `~/projects/scratch/2026-05-14-extended-sign-kill-meta/`
  - `verify_62.py` — (6, 2, 1^6) at q = 6
  - `verify_54.py` — (5, 4, 1^7) at q = 7
  - `verify_63_72.py` — (6, 3, 1^7) and (7, 2, 1^7) at q = 7
