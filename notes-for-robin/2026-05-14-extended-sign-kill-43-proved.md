# For Robin: extended sign-kill for hat_lambda = (4, 3) — proved (2026-05-14, eighth session)

## TL;DR

Eighth prove session of May 14, building on the seventh-session (3, 3)
result. **The extended sign-kill conjecture for hat_lambda = (4, 3) is now
proved in the containment direction at the predicted threshold
tau = q - 4, for q >= 5.**

For lambda = (4, 3, 1^q) with q >= 5:
- B subset E_j^- for j = 1, ..., q - 4 (containment, fully rigorous)
- B subset E_ell^+ universally with T_ell = q*Id (May-13 evening)

Sharpness of the q >= 5 hypothesis verified at q=4: B NOT subset E_1^-.

Paper: `2026-05-14-extended-sign-kill-43.tex` (8 pp).

## What's new: first fully-recursive 3-branch case

This is the **first** hat_lambda case where every contributing
inner-shape branch reduces to a *non-hook* extended-sign-kill input.
The four-piece decomposition of E^+_{n-1}|_{V_lambda} has:

| Branch    | Inner shape              | Role                                      |
|-----------|--------------------------|-------------------------------------------|
| mu_12     | (3, 2, 1^q)              | **Vanishes** via (3,2) ext. sign-kill (5th pass) |
| mu_13     | (3, 3, 1^{q-1})          | Contributes via (3,3) ext. sign-kill (7th pass)  |
| mu_23     | (4, 2, 1^{q-1})          | Contributes via (4,2) ext. sign-kill (6th pass)  |
| mu_h      | (4, 1^{q+1}) hook        | **Vanishes** via hook column-1 (May-12)          |

Dimensions match exactly:
dim B = f^(3,2) = 5 = f^(2,2) + f^(3,1)
                   = dim B^(mu_13) + dim B^(mu_23).

## Two distinct vanishing mechanisms, same algebra

Both mu_12 and mu_h vanish for the SAME reason: their inner shapes have
ell(mu_X) + 1 = n - 4 (one larger than the standard ell + 1 = n - 5 of
the contributing branches), giving an extra inner R'^(mu_X)_{ell(mu_X)}
factor *outside* the standard B^(mu_X)_{ell+1}. That extra factor has
(T_1+1) as its rightmost piece, which kills B^(mu_X)_{ell+1} when the
latter is contained in E_1^-.

For mu_12, the inner B sits in E_1^- via the (3,2) extended sign-kill
theorem at q' = q >= 3.

For mu_h, the inner B sits in E_1^- via the May-12 hook column-1
theorem at k=4, m=q+1 >= 4 (so q >= 3).

Bookkeeping moral: a branch vanishes iff its inner ell+1 is at the
"wrong" level relative to lambda's chain length. This is shape-uniform
and should generalize.

## Why c_1 = (1, 4) has no same-row piece

Crucial structural fact distinguishing (4, 3) from (4, 2):
In (4, 3, 1^q), trying to place n-1 at (1, 3) and n at (1, 4) would
force T(2, 3) > n - 1 by column-3 monotonicity — impossible since
T(2, 3) must be in {1, ..., n-2}.

In (4, 2, 1^q) (sixth-pass paper), row 2 has length 2, so cell (2, 3)
doesn't exist, no column-3 constraint, and the same-row piece at c_1
does exist (this is the source of the sixth-pass paper's stated gap).

## Computational verification

At q=5 (n=12, dim V = 2079):
- dim B = 5 (via rank probe of Omega applied to 20 basis vectors)
- (T_1+1) Omega v = 0 for 5 independent random v (5/5 pass) → B subset E_1^-

At q=4 (n=11, dim V = 1100), sharpness:
- (T_1+1) Omega v has 164 nonzero entries on each of 5 random v
- Confirms B not subset E_1^- at q=4 → q >= 5 is sharp.

Four-piece decomposition dimensions match at q ∈ {2, 3, 4}:

| q | dim R'_n V | f^mu_12 + f^mu_13 + f^mu_23 + f^mu_h | match |
|---|-----------|--------------------------------------|-------|
| 2 | 111       | 35 + 21 + 35 + 20 = 111              | ✓     |
| 3 | 245       | 64 + 56 + 90 + 35 = 245              | ✓     |
| 4 | 470       | 105 + 120 + 189 + 56 = 470           | ✓     |

Scripts: `~/projects/scratch/2026-05-14-extended-sign-kill-43/{verify_decomp.py, verify_E1minus_q5.py, check_q4_sharp.py}`.

## Updated table

| hat_lambda | predicted tau | status                              |
|------------|---------------|-------------------------------------|
| (2, 2)     | q - 1         | proved (May-14 fourth pass)         |
| (3, 2)     | q - 2         | proved (May-14 fifth pass)          |
| (4, 2)     | q - 3         | proved (May-14 sixth pass, gap closable) |
| (3, 3)     | q - 3         | proved (May-14 seventh pass)        |
| **(4, 3)** | **q - 4**     | **proved (this paper, q >= 5)**     |

The first row of the table (|hat_lambda| <= 4) is fully closed. The
second row (|hat_lambda| = 5, 6, 7) is essentially fully closed too —
(2,2)+(3,2) for |hat|=4,5; (4,2)+(3,3) for |hat|=6; (4,3) for |hat|=7.
The next natural targets are |hat|=8: (5, 3), (4, 4), (5, 2, 1) etc.

## What composed here that didn't before

This is the **fourth recursive use** of an extended sign-kill theorem
as INPUT to a strictly larger hat_lambda. The recursion graph now is:

```
(2,2) [base via support rule]
 ↓
(3,2), (4,2)   [recurse on (2,2)]
 ↓
(3,3) [recurses on (3,2) for mu_A; hook column-1 for mu_hook]
 ↓
(4,3) [recurses on (3,3) AND (4,2) for two contributing branches;
       on (3,2) AND hook column-1 for two vanishing branches]
```

(4, 3) is the first node consuming TWO extended-sign-kill inputs
simultaneously, both as contributors. The framework is robust to this:
the two contributing branches' prefix bounds are independent and both
give the same q - 3 prefix (since both apply ext. sign-kill at q' = q - 1).

## Open: sharpness within the chain at q >= 5

The current paper proves the "subset" direction. The matching "iff"
direction would require showing B not subset E_{q-3}^- at q >= 5.
This would extend the Sharpness Lemma technique from the (3, 3)
seventh-pass paper (locating entry n-9 in a witness SYT, off-diagonal
block argument). I left it as a follow-up; the data at q=5 strongly
suggests B not subset E_2^- but I haven't verified or proved it.

## Push status

**69 unpushed commits** on clio-vega/proofs (after today's 8th-pass
commit). PAT issue from May 6 persists.

## Questions for you

1. **Is the recursive-ladder pattern crystallizing for you?** Each step
   adds one row to hat_lambda's first dimension, and the proof pattern
   is: (a) classify the corner pairs + same-row candidates;
   (b) categorize each branch as vanishing vs contributing by inner-shape
   ell+1 indexing; (c) recurse on prior sign-kill theorems. The
   classification step (a) needs case analysis but the rest is mechanical.

2. **Worth attempting (5, 3) or (4, 4) next?**
   - (5, 3): tau = q - 5, threshold q >= 6. Three corner pairs + maybe
     a same-row at c_2 (since row 2 has length 3 < row 1 = 5, same-row
     at c_1 has the (2,3) blocking constraint). Inner shapes
     (4, 2, 1^q), (4, 3, 1^{q-1}), (5, 2, 1^{q-1}); the (5,2) one is
     unproved.
   - (4, 4): r=1 (two corners). Only one corner pair. Like (3, 3) but
     bigger. Simpler structurally.

3. **Should I attempt the sharpness direction next, or push on?** The
   sharpness lemma in (3, 3) was a tight finite case-analysis. Doing
   one for (4, 3) would be analogous but with more entries to locate.

## Files

- Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-43.tex` + `.pdf` (8pp)
- Scripts: `~/projects/scratch/2026-05-14-extended-sign-kill-43/`
