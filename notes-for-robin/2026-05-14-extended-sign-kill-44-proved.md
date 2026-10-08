# For Robin: extended sign-kill for hat_lambda = (4, 4) — proved (2026-05-14, ninth session)

## TL;DR

Ninth prove session of May 14, building on the eighth-session (4, 3)
result. **The extended sign-kill conjecture for hat_lambda = (4, 4) is
now proved in the containment direction at the predicted threshold
tau = q - 5, for q >= 6.**

For lambda = (4, 4, 1^q) with q >= 6:
- B subset E_j^- for j = 1, ..., q - 4 (containment, fully rigorous)
- B subset E_ell^+ universally with T_ell = q*Id (May-13 evening)

The structural sharpness lemma at j = q - 4 is proved (reduces to a
boundary-prefix witness in supp(B), verified computationally at q = 6).

Paper: `2026-05-14-extended-sign-kill-44.tex` (10 pp).

## What composed here that didn't before

(4, 4) is an r=1 multi-corner shape (only two corners), so its
E^+_{n-1} decomposition is a 2-piece (doubly-stripped Phi_A +
same-row Phi_h) like (3, 3). But unlike (3, 3), the same-row inner
shape mu_h = (4, 2, 1^q) is **not a hook**.

| Case      | mu_h (same-row inner) | vanishing input              |
|-----------|----------------------|------------------------------|
| (3, 3)    | (3, 1^{q+1}) hook    | May-12 hook column-1 theorem |
| **(4, 4)**| **(4, 2, 1^q)**      | **(4, 2) ext. sign-kill (May-14 6th)** |

This is the first case in the r=1 stratum where the same-row vanishing
requires a non-hook input. The general principle - "the extra
rightmost R'_{n-6}^{(mu_h)} factor kills E_1^- by the mu_h-level
sign-kill theorem" - carries over uniformly; only the specific input
shifts.

The contributing branch mu_A = (4, 3, 1^{q-1}) recurses on the
just-proved (4, 3) eighth-pass theorem at q' = q - 1.

## Stability ladder for (4, 4, 1^q)

The proof extracts a clean three-stage stability ladder, summarised
as data:

| q | dim V | dim B | B ⊆ E_1^- | min p(T) in supp(B) | regime |
|---|-------|-------|----------|---------------------|---------|
| 2 |   300 |  10   |    no    |        1            | sub-stable (factor 2) |
| 3 |   825 |  15   |    no    |        1            | sub-stable (factor 3) |
| 4 |  1925 |   5   |    no    |        1            | stable, pre-threshold |
| 5 |  4004 |   5   |    no    |        1            | stable, pre-threshold |
| 6 |  7644 |   5   |  **yes** |      **2**          | full regime |

Three thresholds:
- q ≥ 4: Phi_h vanishes (single-branch reduction holds). Stable dim 5.
- q ≥ 6: (4, 3) recursion kicks in. Predicted tau = q - 5 becomes positive.

So q=4,5 are "stable but pre-threshold": dim formula matches the May-13
multi-corner closed form, but the E_j^- chain is still trivially empty
(predicted tau = q - 5 <= 0). q=6 is the first q where the conjecture
makes a non-vacuous prediction, and it holds.

## Sharpness witness at q=6

The lemma reduces B ⊆ E_{q-4}^- to a prefix bound p(T) ≥ q - 3 for
T ∈ supp(B). The witness at q = 6 (n=14, dim V = 7644):
```
T(1, .) = (1, 3, 4, 5)
T(2, .) = (2, 6, 7, 8)
T(3..8, 1) = (9, 10, 11, 12, 13, 14)
p(T) = 2 = q - 4 exactly.
```
So B ⊄ E_{q-4}^- at q = 6, matching the empirically-conjectured sharpness.

## Computational notes

q = 6 with dim V = 7644 is too large for full-matrix Hecke
computations. I built a sparse-vector application module
(`sparse_ops.py`) that applies (T_i + 1) to a vector in O(N) using
the Hoefsmit block structure (at most 2 nonzero entries per row).
This makes Omega-applications and probes at q = 6 instant (0.5s
total for setup, milliseconds per application).

## Recursion graph now

```
(2,2) [base via support rule]
 ↓
(3,2), (4,2)   [recurse on (2,2)]
 ↓
(3,3) [recurses on (3,2) for mu_A; hook column-1 for mu_h]
 ↓
(4,3) [recurses on (3,3) AND (4,2) for two contributing branches;
       on (3,2) AND hook column-1 for two vanishing branches]
 ↓
(4,4) [recurses on (4,3) for mu_A; on (4,2) for mu_h vanishing]
```

The first row of the |hat-lambda| <= 8 stratum is now closed:
- |hat| = 4: (2,2)
- |hat| = 5: (3,2)
- |hat| = 6: (4,2), (3,3)
- |hat| = 7: (4,3)
- |hat| = 8: (4,4)  ← this paper

Still open at |hat| = 8: (5, 3). It has three corner pairs (so a
four-piece E_{n-1}^+ decomposition like (4, 3)), and the contributing
branches would include (5, 2) - currently unproved.

## Updated table

| hat_lambda | predicted tau | status                              |
|------------|---------------|-------------------------------------|
| (2, 2)     | q - 1         | proved (May-14 fourth pass)         |
| (3, 2)     | q - 2         | proved (May-14 fifth pass)          |
| (4, 2)     | q - 3         | proved (May-14 sixth pass)          |
| (3, 3)     | q - 3         | proved (May-14 seventh pass)        |
| (4, 3)     | q - 4         | proved (May-14 eighth pass)         |
| **(4, 4)** | **q - 5**     | **proved (this paper, q >= 6)**     |

## Push status

**70 unpushed commits** on clio-vega/proofs (after today's 9th-pass
commit). PAT issue from May 6 persists - please refresh when convenient.

## Questions for you

1. **(5, 3) next, or sharpness extensions?** The (4, 4) paper proves
   sharpness only at q = 6 (computational witness); a structural
   witness construction at all q >= 6 would be analogous to the (3, 3)
   seventh-pass sharpness lemma but with two more entries to locate.
   (5, 3) would extend the recursion graph by one level - but needs
   (5, 2) as an input, currently open.

2. **Is the r=1 vs r=2 split crystallizing as a real pattern?**
   r=1 shapes (two corners) give 2-piece E^+_{n-1} decompositions with
   one contributor + one vanisher. r=2 shapes (three corners) give
   4-piece decompositions with two contributors + two vanishers. The
   vanishing mechanism is shape-uniform; only the specific recursive
   input shifts. I haven't yet seen a structural reason for these
   counts beyond "count the corner pairs", but it does seem they're
   determined entirely by the corner combinatorics.

3. **The sub-stable factors (2 at q=2, 3 at q=3) for (4, 4, 1^q):**
   the factor-of-two-refuted paper noted these as exceptions. Now
   they're explained: at q < 4 the Phi_h branch doesn't vanish, so
   B carries both contributions and dim B = dim Phi_A(I_A) +
   dim Phi_h(I_h). For q = 2: 5 + 5 = 10. For q = 3: 5 + 10 = 15.
   Worth checking whether this dim-additivity continues to predict
   sub-stable dims for related shapes?

## Files

- Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-44.tex` + `.pdf` (10pp)
- Scripts: `~/projects/scratch/2026-05-14-extended-sign-kill-44/`
  - `check_decomp.py` — two-piece E^+_{n-1} decomp at q ∈ {1, 2, 3}
  - `check_dim_B.py` — full-matrix dim B + supports at q ∈ {2, 3}
  - `verify_E1minus.py` — sparse vector probe at q ∈ {4, 5, 6}
  - `sparse_ops.py` — sparse Hecke operator application module
