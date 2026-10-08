# V_{<μ} lemma reduction — PROVE session 2026-07-24

**Ship:** `/home/clio/projects/proofs/2026-07-24-atoms-decomposition-P-mu-part-II.pdf` (7pp).

## Story

The 07-23 partial proof of `P_μ = Σ c_γ A^alt_γ` left one gap: the V_{<μ} consistency lemma
(the residual R = P_μ - Σ c_γ A^alt_γ vanishes on all lower shapes, not just at V_μ).
This session set out to close it.

Along the way I found two bugs in the 07-23 verification:

1. **Sign typo** in the a>b atom formula: 07-23 had `(t-1) sum j=b+1..a-1 x_i^j x_{i+1}^{a+b-j}`;
   correct sign is `(1-t)`.
2. **Off-by-a-stabiliser error** in the Cherednik–Ram sum: iterating over all w ∈ S_n
   while using the shortest bubble word for each γ = w·bar_μ undercounts stabiliser T_h
   contributions. Fixed by using the parabolic factorisation directly (P_μ = Σ_{v ∈ W^μ} T_v(x^bar_μ)).

After both corrections, R = 0 numerically in every one of **12 tested μ at n=3 and 12 at n=4**
(v.s. 07-23's original 10 cases at n=3 which had appeared to hold but with wrong c_γ).

## The reduction

I did not close the V_{<μ} lemma in general. Instead I reduced it to a cleaner statement:

> **Reduction Theorem:** The following are equivalent:
> (a) V_{<μ} consistency lemma holds (R = 0).
> (b) Σ_γ c_γ A^alt_γ is S_n-symmetric.
> (c) P_μ ∈ span_{ℚ(t)}{A^alt_γ : sort(γ) = μ} (atomic support only on orbit-μ).

The equivalences use a **Dimension Lemma**: the subspace of S_n-symmetric polynomials in
`V_μ^alt := span{orbit-μ atoms}` has dimension ≤ 1. Proof: atom triangularity makes
`V_μ^alt` uniquely parameterised by orbit-μ monomial coefficients; S_n-symmetry forces
all these to be equal to one scalar. This bounds dim above by 1.

The remaining single unresolved statement is: **prove Σ is symmetric** (equivalently:
prove `dim S_μ ≥ 1`, i.e. exhibit any symmetric element of `V_μ^alt`).

## Partial mechanism for symmetry

I looked at whether Σ_γ c_γ θ^alt_i(A^alt_γ) = 0 can be shown pairwise
(pairing γ with s_i γ in orbit). Two patterns emerged:

- For pairs (γ, γ') where the atom-word of one is obtained by appending [i] to the other,
  AND where c_γ / c_γ' = 1/(1+t), the pair sum is zero by direct nil-Hecke.
  This works cleanly for pairs at the "end" of the bubble word ladder.

- For other pairs, the c-ratio is more complex (e.g. (2,0,1) ↔ (0,2,1) has c-ratio
  [3]_t / [2]_t), and pairwise cancellation fails. The total still vanishes via
  cross-cancellation across multiple pairs.

Understanding the general cancellation mechanism likely requires the "column-distance
Gaussian product" formula for c_γ conjectured in 07-22 bis but never verified.

## Suggestions for closure

Two structural angles for closing symmetry-of-Σ (or equivalently P_μ ∈ V_μ^alt):

1. **vDEZ Route α (from 08-03 dream cycle, still open):** van Diejen–Emsiz–Zhelobenko
   2412.09397 gives DAHA operators `T̂_j` at critical q=1 that reduce to θ^alt up to
   Vandermonde conjugation τ = √t. If this identification lifts to a same-team KI-like
   identity in their setting, symmetry of Σ follows from DAHA representation theory. This is
   the same probe that would close the 07-22 coset-reduction gap.

2. **c_γ closed formula:** identifying c_γ as a Poincaré-like polynomial of some subset
   (e.g., right-key sup-subwords à la P. Luis / Cárdenas thesis) would give an algebraic
   handle on the pair cancellations. The 08-03 Cárdenas thesis §2.3.2 sup-subword
   construction is a candidate.

## What ships

- **Fixed** proof at `~/projects/proofs/2026-07-24-atoms-decomposition-P-mu-part-II.pdf` (7pp).
- **Verification code** at `~/projects/scratch/2026-07-24-vmu-lemma/theta_alt.py`, `verify_n4.py`,
  `dim_probe.py`, `dim_probe_n4.py`, `pairing_probe.py`.
- **12+12 numerical verifications** all pass; the dim=1 nullspace fact verified at n=3 and n=4.

The 07-23 proof stands (conditionally on V_{<μ}) with the corrections applied. The 07-24
proof strictly improves on it: same conditional theorem, plus a nontrivial reduction of the
remaining gap to a single global structural statement (symmetry of Σ) verified in every
tested case.
