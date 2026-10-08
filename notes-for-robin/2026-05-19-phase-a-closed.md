# For Robin — 2026-05-19: Phase A endpoint **closed** unconditionally → rank-zero theorem fully unconditional for $\lambda = (2^a, 1^{n-2a})$

## TL;DR

The last conditional piece of the rank-zero theorem for the family
$\lambda = (2^a, 1^{n-2a})$ is now closed. The Phase A endpoint
\[
   R'_n V = E_{n-1}^+(V)
\]
holds for *every* $H_q(S_n)$-module $V$ — no shape restriction, no
$a$-dependence — and the proof is short, abstract, and basis-free.

Writeup: `2026-05-19-phase-a-general.tex` (8pp).

**Consequence.** Combined with May-15 (inductive reduction) and
May-18 (final pair identification + support theorem), the rank-zero
theorem
$\Pi^{S_n}|_{V_{(2^a, 1^{n-2a})}} = 0$
holds **unconditionally** for every $a \ge 1$, $n \ge 3a$.

## The proof

The proof has three ingredients, none of which mention $\lambda$:

1. **Operator identity.** $(T_j+1) = (1+q) \pi_j^+$ where $\pi_j^+$
   is projection onto $E_j^+$ along $E_j^-$. (Follows immediately
   from $T_j$'s eigenvalues being $\{q, -1\}$.)

2. **Trace conjugacy.** $T_j$ and $T_{j+1}$ are conjugate in
   $H_q(S_n)$ via $h = T_j T_{j+1}$ (using the braid relation).
   Hence $\dim E_j^+$ is constant in $j$ on any module.

3. **Adjacent disjointness lemma.** $E_j^+(V) \cap E_{j+1}^-(V) = 0$
   for any $V$ and any $1 \le j \le n-2$.

The lemma is the only real content. It's proved by restricting $V$
to the subalgebra $\langle T_j, T_{j+1}\rangle$, which is a quotient
of $H_q(S_3)$ (via braid + quadratic relations). Three irreducibles
of $H_q(S_3)$:
- Trivial: $E_{T_2}^- = 0$ (since $q + 1 \ne 0$).
- Sign: $E_{T_1}^+ = 0$.
- Standard (2-dim): $T_1 = \mathrm{diag}(q, -1)$ in the seminormal
  basis; $T_2$ is a non-degenerate 2-block on the same basis. So
  $E_{T_1}^+ = \mathrm{span}(v_{T_A})$, and $T_2 v_{T_A}$ has
  nonzero $v_{T_B}$ component → $v_{T_A} \notin E_{T_2}^-$.
  Hence $E_{T_1}^+ \cap E_{T_2}^- = 0$.

The Phase A endpoint then follows by induction on $j$. Base:
$W_1 = (T_1+1)V = (1+q) E_1^+ = E_1^+$. Inductive step:
$W_j = (1+q) \pi_j^+(W_{j-1}) = \pi_j^+(E_{j-1}^+)$, and
$\pi_j^+|_{E_{j-1}^+}$ is injective by the lemma, surjective onto
$E_j^+$ by dimension match.

## Why this proof and not the May-13/14 one

The prior proofs used explicit basis-tracking through $\mathcal{B}_j$
— a set of $T_j$-$+q$-eigenvectors built from the seminormal basis
encoding the corners of $\lambda$. That approach works at $a = 2, 3$
but requires re-doing the case analysis with each new column-2 row.
For $a \ge 4$ it's mechanical but tedious.

The abstract proof says: forget the basis. The identity $W_j = \pi_j^+(W_{j-1})$ is shape-independent; the only thing it relies on is the kernel of $\pi_j^+$ being zero on $W_{j-1}$. And that kernel zeroness is a generic Hecke fact, not a partition-specific one.

This is the same pattern of progressive abstraction we've seen
through May-13 → May-15 → May-17 → May-18. Each round sheds
shape-specificity. This is the final layer for Phase A.

## Computational verification

Lemma $E_j^+ \cap E_{j+1}^- = 0$ verified at $q = 7$ for all
$j \in [1, n-2]$ on:
- All partitions $\lambda \vdash n$ with $\dim V_\lambda$ tractable,
  $3 \le n \le 7$.
- $(2^a, 1^{n-2a})$ for $a = 2$ at $n \in \{6, 7\}$, $a = 3$ at $n \in \{9, 10\}$, $a = 4$ at $n = 12$.

Phase A endpoint $R'_n V_\lambda = E_{n-1}^+|_{V_\lambda}$ verified
directly (dim agreement + span equality) at the same cases.

In particular, $\lambda = (2^4, 1^4)$ at $n = 12$:
$\dim R'_n V_\lambda = 75 = \dim E_{n-1}^+$, as predicted.

Script: `~/projects/scratch/2026-05-19-phase-a-general/verify_phase_a.py`.

## Status of the rank-zero theorem after this paper

| Family | Status |
|--------|--------|
| $(1^n)$ (sign) | trivial |
| $(2, 1^{n-2})$ | May-11 |
| $(3, 1^{n-3})$ | May-12 |
| $(2, 2, 1^{n-4})$ | May-13 |
| $(2^a, 1^{n-2a})$ all $a \ge 2$, $n \ge 3a$ | **May-19 (this paper) → unconditional** |

The full $(2^a, 1^{n-2a})$ family is now closed structurally, at every $a \ge 1$ and $n \ge 3a$.

## What's still open

1. **Optimal threshold $n = 3a$.** Empirically sharp (PROVE.md table:
   $a = 5$ stabilizes at $n = 15$, $n = 14$ gives 31 not 32). The
   $n \ge 3a$ bound enters in the May-17 same-row exclusion. Tightness
   not proved.

2. **The $(3, 2, 1^{n-5})$ family.** Backup PROVE.md target.
   Empirically $\dim B_{\ell+1} V = 2$ at $n = 9, 10, 11$ — so the
   $j$-formula at $j = \ell + 1$ does not immediately collapse to dim 1.
   Two interesting features: (i) needs $j > \ell + 1$ to collapse, (ii)
   the per-trajectory framework has TWO L/R choices per step instead
   of one. Worth thinking about.

3. **Other rank-zero non-hook families** — $(4, 1^{n-4})$ hook is
   straightforward; $(2, 2, 2, 2, 1^{n-8})$ et al. all fall under
   today's theorem (since they are $(2^a, 1^{n-2a})$).

## Push status

**32 unpushed commits**, latest is this one. PAT issue from May 6
persists. The 32-commit backlog includes the entire $a = 2 \to a = 6$
structural program plus the abstract Phase A proof.

## Questions for you

1. **Is the abstract Phase A proof clean enough to be the "official"
   version?** I think yes — it's basis-free, partition-free, and
   makes the role of trace conjugacy + the $H_q(S_3)$-restriction
   transparent. Worth re-citing instead of the May-13/14 basis
   proof in any future work.

2. **Next family — $(3, 2, 1^{n-5})$?** This is the natural next
   target. The two-L/R-choice structure is intriguing and may shed
   light on the general non-hook combinatorics.

3. **Move toward a uniform proof of rank-zero?** With the
   $(2^a, 1^{n-2a})$ family closed, the natural question is whether
   a uniform argument works across all rank-zero $\lambda$. The Phase A
   endpoint already works uniformly; what we lack is a uniform Phase B.

## Files

- Writeup: `~/projects/proofs/2026-05-19-phase-a-general.tex` + `.pdf`
- Verification: `~/projects/scratch/2026-05-19-phase-a-general/verify_phase_a.py`
