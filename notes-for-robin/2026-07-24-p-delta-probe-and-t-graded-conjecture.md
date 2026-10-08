# For Robin — P-δ probe at μ=(2,2,0), n=3, + t-graded A-G conjecture

**Date:** 2026-07-24 (container) / ~2026-08-05 (narrative clock).

## TL;DR

Today's wake ran the P-δ probe from dream cycle 10. Two landings:

1. **A-G local condition at t=0 for μ=(2,2,0), n=3 — VERIFIED as expected.**
   Deep-read of Assaf-González 1901.07520 [was mis-cited as A-G 2512.19814] confirms the local characterisation
   is (E) extremal + (I) ideal + (P) principal, purely classical (no t
   anywhere in the paper). Implemented as a Python predicate; test on 9
   candidate subsets of B((2,2,0)) — three Demazure crystals PASS, shape-<μ
   FAILS (E) with three parallel violations. This is L-S 1990 in a fresh
   packaging.

2. **NEW: t-graded A-G conjecture (Route δ+).** Computed nil-Hecke t-atoms
   A^alt_γ as explicit polynomials in ℚ(t)[x_1, x_2, x_3]. Viewed as
   ℚ(t)-linear combinations of crystal elements, the coefficient matrix
   (rows = γ ordered by Bruhat, cols = T ∈ B((2,2,0))) is
   **block lower triangular** with (1-t) block-diagonal + pure-t shadows
   on sub-diagonals. **This is the mechanism behind the Dim Lemma**: the
   [k]_t coefficients c_γ absorb the -t shadows exactly, and the (1-t)
   block diagonal produces the (1-t) coefficient on m_(2,1,1) in P_(2,2)(x;t)
   = m_(2,2) + (1-t) m_(2,1,1).

If the block-triangular structure is uniform across all μ, **V_{<μ} closes
at generic t as a structural observation about θ^alt-atoms** — bypassing
Route α (vDEZ) DAHA machinery entirely.

## The concrete finding

For μ=(2,2,0), n=3, the coefficient matrix [coeff of T ∈ B(μ) in A^alt_γ]:

```
             H       A         B      C      D      L
(2,2,0):     1       0         0      0      0      0
(2,0,2):    -t     (1-t)       1      0      0      0
(0,2,2):     0    t(t-1)      -t   (1-t) (1-t)     1
```

Where B(μ) elements are (labeled by SSYT of shape (2,2)):

- H = [[1,1],[2,2]], wt = (2,2,0), classical atom A_{(2,2,0)}
- A = [[1,1],[2,3]], wt = (2,1,1), classical atom A_{(2,0,2)}
- B = [[1,1],[3,3]], wt = (2,0,2), classical atom A_{(2,0,2)}
- C = [[1,2],[2,3]], wt = (1,2,1), classical atom A_{(0,2,2)}
- D = [[1,2],[3,3]], wt = (1,1,2), classical atom A_{(0,2,2)}
- L = [[2,2],[3,3]], wt = (0,2,2), classical atom A_{(0,2,2)}

Verified: Σ_γ c_γ(t) A^alt_γ = P_(2,2)(x;t) with c = ([3]_t, [2]_t, 1).

At t=0: (1-t) → 1, (-t) → 0, t(t-1) → 0. Matrix collapses to classical
atom characteristic function; recovers L-S 1990.

## Why this matters for the sprint

**Portfolio update.** The V_{<μ} lemma has now been attacked from five
routes (α vDEZ, β Paten-Woodruff downgraded, γ Cárdenas, δ A-G, ε own
Dim Lemma). Today's landing adds a sixth candidate:

- **Route δ+ (t-graded A-G, conjectured):** if block-triangular structure
  of A^alt_γ holds for all μ, then V_{<μ} at generic t closes structurally
  — no DAHA (Route α), no crystal-graph edge combinatorics beyond A-G,
  no Cárdenas closed formula. Just a direct polynomial-side observation
  about θ^alt-atom expansions.

The path forward: verify the block-triangular structure at μ=(2,1,0), n=3
(orbit size 6, richer Bruhat), μ=(2,2,1), n=3, μ=(3,1,0), n=3, and
μ=(2,2,0), n=4. Four verifications turns the conjecture into a load-
bearing structural claim; then attempt to prove it from θ^alt commutation
relations + Bruhat descent.

## A subtlety worth flagging

The extremal elements of B((2,2,0)) are **{H, B, C, L} — FOUR, not three**.
C has weight (1,2,1) which is NOT in the S_3-orbit of μ = (2,2,0). C is an
"internal extremal" point in A-G's sense. This means A-G's atom
decomposition of B(μ) potentially includes a singleton atom at C, distinct
from the three coset-indexed classical Demazure atoms (which are what I
computed).

I have not fully sorted out whether A-G's atom decomposition and the
classical right-key atom decomposition agree at μ=(2,2,0), or whether A-G
gives a strictly finer decomposition. To verify at μ=(2,1,0) where the
Weyl orbit has no stabiliser.

## Files

- **7pp PDF proof**: `~/projects/proofs/2026-07-24-p-delta-probe-Vmu-at-tzero.pdf`
  (contains full A-G test table, coefficient matrix, and t-graded lift
  conjecture).
- **Python probes**: `~/projects/probes/2026-07-24-p-delta-crystal/`
  - `build_crystal.py`, `crystal_data.py/.json`
  - `compute_atoms.py`, `atom_decomposition.json`
  - `ag_test.py`
  - `compute_A_alt.py`, `compute_A_alt.out`

**All files still blocked from GitHub push** — PAT expired ~7d ago
(from Lyra email uid 479, escalated to you). When PAT is refreshed, will
push proofs + probes to `clio-claude/proofs` for you to review.

## Ask (soft, not blocking)

If you have thoughts on the block-lower-triangular observation — especially
whether you've seen this structure in the literature (nonsym Macdonald
atoms? Blasiak flagged LLTs? Warnaar affine dual Jacobi-Trudi cocycle
factor?) — I'd love a pointer. The (1-t) block diagonal with pure-t
shadows feels like it should be named somewhere; five candidates for
naming home (L-S 1987, Borodin-Wheeler 1904.06804 [was mis-cited as vDEZ 2412.09397], Cárdenas 2026, Blasiak §7.6,
Alexandersson 2607.18746) still active, one has to have this pattern.

The **ICERM Fall 2025 Workshop 3 attendee question** from yesterday
(Blasiak, Williams, Lenart, Griffeth all co-located Nov 2025) remains
open. If you attended or know someone who did, that's a single-hop entry
to all five naming-home candidates plus the Talca cluster (Cárdenas +
Lapointe).

— C.
