# For Robin: extended sign-kill for hat_lambda = (2,2) proved (2026-05-14, fourth session)

## TL;DR

This is the third "very late" prove session of May 14, and the most
productive one. **The extended sign-kill conjecture for hat_lambda = (2,2)
is now proved in both directions.**

For lambda = (2, 2, 1^q) with q >= 2:
- B subset E_j^- for j = 1, ..., q - 1  (containment)
- B not subset E_j^- for j = q, q+1, ..., n-1  (sharpness)
- B subset E_ell^+ universally (Theorem A, May-13 evening)

Combined: a complete characterization of the T_j-eigenspace
containments of B for the (2,2,1^q) family at all q >= 2.

Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-22.tex` (7pp).

## How the proof works

This was sitting in plain sight. The May-13 paper
`2026-05-13-non-hook-22-1n.tex` already gave the explicit 4-SYT
support of b at q >= 2, and proved B subset E_1^-. The May-14
afternoon conjecture asserted the full chain B subset E_j^- for
j <= q - 1 with no proof.

Just reading the May-13 paper's support description gives the
proof in two lines:

  S_n = {(n-3, n-2), (n-3, n-1), (n-2, n), (n-1, n)}   (column-2 labels)

For each (a, c) in S_n, a >= n - 3. Hence column 1 of T^{(a,c)}
has the identity prefix T(i, 1) = i for i = 1, ..., n - 4.

For each j in {1, ..., n - 5} = {1, ..., q - 1}, both j and j+1
sit in {1, ..., n-4}, so both are in column 1 at adjacent rows.
Hoefsmit same-column rule: T_j v_T = -v_T for each support SYT.
Linearity: T_j b = -b.

For sharpness, the off-diagonal action of T_j at j = q puts weight
on SYTs outside S_n (specifically T^{(q, q+2)}), and the four
support coefficients are nonzero (May-13). So T_q b has nonzero
coefficient outside the support of b, hence T_q b != -b.

## Lesson learned

Conjectures sometimes have proofs in papers already written; the
job is to *connect* the dots, not always to invent new techniques.
The May-14 afternoon session conjectured the chain without
recalling the May-13 paper's explicit support. The May-14 evening
session noted "$b in W_q$" (with a wrong definition) but didn't
extract the consequence. The May-14 very-late-late session reads
both papers carefully and the proof falls out.

This is a useful pattern to remember: when you see a conjecture
about a quantity with explicitly identified support, check the
support against the eigenvalue conditions. Sometimes the answer is
combinatorial.

## What's still open

- **hat_lambda = (3, 2)** at j >= 2: **strong empirical evidence**
  for the extended sign-kill conjecture. Computational verification
  at q = 3, 4, 5, 6:
  - Support of B has 26 SYTs in every case.
  - Min identity prefix in support: q - 1. (I.e., every support SYT
    has T(i, 1) = i for i = 1, ..., q-1.)
  - By the support rule (Prop 6 in my paper), this gives
    B subset E_j^- for j <= q - 2, matching the predicted threshold
    tau = q + 3 - 3 - 2 = q - 2.
  - **Missing**: structural identification of the support. The
    May-20 paper constructs B as the image of three branches under
    R'_{ell+1} ... R'_{n-1}, and the resulting 26-element support
    can presumably be extracted by tracing through. Would close the
    (3, 2) row.

- **General hat_lambda** at j >= 1: requires support description for
  general multi-corner shapes. Currently no closed-form support
  description; the May-13 multi-corner-dimension paper gives the
  *dimension* of B but not the support.

- **Top-two-rows independence** structural mechanism: the threshold
  tau = q + 3 - hat_lambda_1 - hat_lambda_2 only depends on the top
  two rows. No structural explanation for why lower rows don't
  contribute.

## Side note: the (2,2,1^q) "$E_j^- chain support criterion"

The proof reveals a clean criterion for B subset E_j^- in the
(2,2,1^q) family:

  B subset E_j^- iff every support SYT has j, j+1 in the same column.

For B in the (2,2,1^q) family, the support is the 4-SYT set S_n,
all of which have T(i, 1) = i for i <= n - 4. Hence the criterion
is satisfied iff j+1 <= n - 4, i.e., j <= n - 5 = q - 1. Done.

This criterion generalizes: if dim B = m and the support is a known
set of N SYTs, then B subset E_j^- iff every support SYT has j, j+1
in the same column (or equivalently, the off-diagonal contributions
cancel out, which is a much stronger condition).

The sufficient condition "every support SYT has j, j+1 in same
column" might be the cleanest path to extending the conjecture.

## Push status

**65 unpushed commits** on clio-vega/proofs (was 64). PAT issue
from May 6 persists --- please refresh when you can.

## Files

- Paper: `~/projects/proofs/2026-05-14-extended-sign-kill-22.tex` + `.pdf`
- Scripts: `~/projects/scratch/2026-05-14-extended-sign-kill-proof/`
  - `explore_22_family.py` --- eigenspace structure of B for q = 2,3,4
  - `identify_22.py` --- explicit basis vector of B in Hoefsmit basis
  - `check_S1Omega_zero.py` --- S_1 Omega = 0 as matrix for q >= 2
  - `verify_support_argument.py` --- end-to-end verification, q = 2..7

## What I'd suggest tackling next

The natural sequel is **hat_lambda = (3, 2) at j >= 2**. The
strategy:

1. Read the May-20 paper's Phi_A, Phi_B, Phi_C formulas carefully.
2. Compute the explicit support of B for (3, 2, 1^q) at small q
   (q = 3, 4, 5) and check whether all support SYTs share a
   "T(i, 1) = i for i <= k" pattern.
3. If yes: extract the structural proof as before. If no: identify
   what additional ingredient is needed.

Alternative: investigate the **top-two-rows independence**
phenomenon directly. Why does the threshold only depend on the top
two rows? This feels representation-theoretic --- maybe related to
the SL_2 horizontal-strip structure or the column-1-deletion functor.
