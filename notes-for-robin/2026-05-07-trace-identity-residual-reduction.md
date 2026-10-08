# Trace identity D(q) = cross_(3,1,1)→(3,2)(q): residual reduction

**Date:** 2026-05-07 (proof session)
**Output:** `~/projects/proofs/2026-05-07-trace-identity.tex` (+ pdf, 7 pages)
**Computational evidence:** `~/projects/scratch/2026-05-07-trace-identity/residual_check.py`

## What I tackled

The May 6 paths writeup (`2026-05-06-paths-explicit-and-Q3-refuted.tex`) flagged an exact, structurally unexplained identity:

  D(q) = cross_(3,1,1)→(3,2)(q) = q^5(1+q)(q^4+7q^3+12q^2+7q+1)

where D(q) is the contribution to σ_1(V_(3,2,1)) where the s_5 step (position 11 in the staircase word) acts as the diagonal piece of T_5+1, and cross_(3,1,1)→(3,2) is a KL-block off-diagonal trace.

I tried to prove this structurally.

## What I got

**1. Convention correction.** The path-enumeration code uses the unprimed C_w KL basis (where D_i records ascents); the May 6 prose papers say D_i records descents. Both conventions give the same σ_1, but local identities like P_(3,2) D_5 differ. I adopted the code's convention.

**2. Clean reduction.** With the corrected convention, the identity reduces to:

  cross_(3,1,1)→(3,2) = (1+q)(T_A + T_B)

where T_A = tr(Π^{S_5} P_(2,2,1) R_5') and T_B = tr(Π^{S_5} D_5^(3,1,1)asc R_5').

**3. Surprising explicit values.** Computed in `residual_check.py`:

  T_A = q^6 + 2q^7 + q^8 = q^6(1+q)^2
  T_B = q^5 + 6q^6 + 10q^7 + 6q^8 + q^9 = q^5((1+q)^4 + 2q(1+q)^2)
  T_A + T_B = q^5(1 + 7q + 12q^2 + 7q^3 + q^4)

T_A is a single σ_1-G1 atom (cleanest possible). T_A + T_B has B_4-decomp (1, 3, 0).

**4. Connection to A_(4,1).** A_(4,1) = 1 + 7q + 17q^2 + 7q^3 + q^4 = atom inside σ_1(V_(4,1)) at S_5. Difference: A_(4,1) - (T_A + T_B)/q^5 = 5q^2. The 5 is exactly m_(4,1)^(2), the multiplicity of the top atom in M_(4,1) = (1, 3, 5).

  T_A + T_B  =  q^5 · (A_(4,1) − 5q^2)

If this connection is real (not numerical coincidence), it ties the trace identity directly to V_(4,1) at S_5.

## What's still open

- A path-level enumeration giving T_A = q^6(1+q)^2 directly. This would explain why every closed staircase-minus-position-11 path with w_10 ∈ V_(2,2,1) has the same bigrade.
- Same for T_B.
- A structural reason for "T_A + T_B = q^5 · (A_(4,1) − top atom)".
- The 4 vanishing cross-traces (cross_(3,2)→(3,1,1) = 0, etc.) are still input data, not proved structurally.

## Honest assessment

This is a **partial structural reduction**, not a proof. It replaces the original 6-coefficient surprise polynomial identity with two 4-coefficient sub-identities (T_A and T_B), each with cleaner closed form. The structural payoff is that the gap is now smaller and more localizable — but the gap remains.

The most promising next step: enumerate closed paths in V_(2,2,1) along the staircase-minus-position-11 word at S_6, verify by hand that there are 4 paths with bigrade (6, 2). This is small enough to do.

The most promising structural angle: the formula T_A + T_B = q^5 · (A_(4,1) − top atom). If this is real, it suggests the trace identity has a representation-theoretic explanation connecting the V_(3,2,1) cell at S_6 to V_(4,1) at S_5 via the σ_1-G1 framework.

## GitHub

Two unpushed commits remain on `clio-vega/proofs` (the read-only PAT issue). I added the new `2026-05-07-trace-identity.{tex,pdf}` to the repo locally; will need a working PAT to push. Email earlier today flagged this.
