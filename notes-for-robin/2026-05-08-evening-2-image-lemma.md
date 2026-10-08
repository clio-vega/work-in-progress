# Image Lemma — closes hook rank formula through n=7 (2026-05-08 evening-2)

**Date:** 2026-05-08, second evening prove session.
**Writeup:** `~/projects/proofs/2026-05-08-evening-2-kernel-dichotomy.tex` (7pp, commit `5175a4f`).

## What I proved (rigorous)

**Image Lemma.** For $n \ge 4$, $y \in \mathrm{span}(v_2,\ldots,v_{n-2})$,
and any $w \in V_{(n-1,1)}$ with $R_n'(w) = y$:
$$ w_{v_n} = C_n \cdot y_{v_{n-2}}, \qquad C_n = \frac{\beta_{n-2}\beta'_{n-1}}{(1+q)^{n-1}\alpha_{n-2}\alpha'_{n-1}} \in \mathbb{Q}(q)^\times. $$

This is the structural seed of the parity dichotomy: the
$v_n$-coordinate of any preimage is *exactly* $C_n$ times the
$v_{n-2}$-coordinate of the target. Replaces the May-8 morning
paper's "case analysis through each R_k' block" gap with a closed
formula.

**Reduction Theorem.** Combined with the branching factorization
$\Pi^{S_n} = \Pi^{S_{n-1}} R_n'$, the Image Lemma gives:
$$ v_n^*(K_n) = 0 \iff v_{n-2}^*\bigl(K_{n-1} \cap \{v_{n-1}^*=0\}\bigr) = 0. $$

**Hook rank formula at $n \le 7$ (rigorous).** Using the Image Lemma
and the $n=6$ case computed explicitly via lower-triangular matrix
inversion of $R_5''$, the hook rank formula
$\mathrm{rank}\,\Pi^{S_n}|_{V_{(n-1,1)}} = \lceil(n-2)/2\rceil$ is now
proven rigorously for $n \le 7$ (no computational gaps).

## What's left

For general even $m \ge 8$, need the **tail-coordinate
proportionality** $(R_m)$: for $m$ even, $v_{m-1}^*$ and $v_m^*$ are
proportional on $K_m$. This is verified computationally at $n=8$ —
explicit ratio
$$ \lambda_8 = -\frac{(q+1)(3q^4-2q^3+4q^2-2q+3)(q^6+q^5+q^4+q^3+q^2+q+1)}{q(q^2+1)(q^4+1)(q^2-q+1)(q^2+q+1)} $$
— and the proof at $n=6$ shows the mechanism: matrix inversion of
$R_{n-1}''$ plus the $K_{n-1}$-relation among coordinates collapses
$w_{v_{n-1}}$ to a multiple of $y_{v_{n-2}}$.

The general inductive proof of $(R_m)$ requires:
1. An explicit formula for the inverse of $R_{n-1}''$ on the
   iterative image basis (mechanical, lower-triangular).
2. A structural description of $K_{n-1}$ for $n-1$ odd (recursive
   $K_{n-1} = K_{n-3} \oplus \mathbb{Q}(q) w_{n-1}$), giving
   the relations among $y_{v_k}$'s.

The pattern in $\lambda_m$ for even $m$ — numerator factors
$1, 2q^2-q+2, 3q^4-2q^3+4q^2-2q+3$ at $m=4,6,8$ — suggests a closed
form, but I haven't found it.

## Why this matters

The May-8 morning paper acknowledged a gap: the inductive
image-tracking step from $D_n$ down to $D_2$ "requires a careful
case analysis at each $R_k'$ block; the formal proof of the
transition is left open."

This evening-2 writeup *closes that gap with a clean structural
formula* (the Image Lemma) for the case where it matters most: the
$v_n$-coordinate of preimages. The remaining open piece $(R_m)$ is
of the same flavour — a parallel "Image-Lemma-like" formula for
$v_{m-1}^*$ — and computational evidence is overwhelming.

## Push status

**Still 17 unpushed commits.** Read-only PAT remains a blocker.
Robin's email of 2026-05-06 noted this; status unchanged.

When the PAT is fixed, please push everything. The May-7 / May-8
session series (rank-1, rank-zero, hook rank formula, Image Lemma)
is the longest sustained structural progress on the
$\Pi^{S_n}|_{V_{(n-1,1)}}$ problem so far.

## Files

- `~/projects/proofs/2026-05-08-evening-2-kernel-dichotomy.tex` — main writeup.
- `~/projects/scratch/2026-05-08-kernel-dichotomy/probe_kernel.py` — kernel structure $m \le 7$.
- `~/projects/scratch/2026-05-08-kernel-dichotomy/test_nesting.py` — verifies $K_{n-2} \subset K_n$.
- `~/projects/scratch/2026-05-08-kernel-dichotomy/check_n8_proportionality.py` — verifies $(R_8)$ and nesting at $n=8$.
