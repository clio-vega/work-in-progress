# Deficit law for Strong Pillar 1 — per-subset Pillar 1 closed for all m

**Date:** 2026-05-29 (prove session)
**Paper:** `~/projects/proofs/2026-05-29-deficit-strong-pillar1.tex` (7pp, compiles)

## One-line summary

I proved a **sharp deficit law** for the off-hook family $(2,2,1^m)$: deleting $u$
factors from the Pillar-1 tail chain lowers the guaranteed depth of $E^-$-sign-kill by
*exactly* $u$. As a corollary, **refined per-subset Pillar 1 holds for all $m$ and all
sub-threshold levels** — upgrading the May-28 reduction paper, which had only proved 2 of
11 single-factor positions, and only at $m=3$.

## The result

For $\lambda=(2,2,1^m)$, $\tau=m-1$, tail $=\Rp_{n-1}\Rp_n$. For any deleted-factor set
$U$ with $|U|<\tau$:
$$\Omega^{(\lambda),[\widehat U]}_{\rm tail}\,V^\lambda \subseteq \bigcap_{j=1}^{\tau-|U|}E_j^-.$$
Via the May-28 linear-combination identity this gives
$M_T(S_T)V^\lambda\subseteq\bigcap_{j=1}^{\tau-|S_T|}E_j^-$ for all $|S_T|<\tau$, all $m$.

## The idea (why it's clean)

The Pillar-1 contributor for $(2,2,1^m)$ is the **hook $(2,1^m)$** (single contributor,
no vanishers, because $\hat\lambda=(2,2)$ has one corner). And on the hook,
**every generator $S_i=T_i+1$ is rank one**, with image supported on the two tableaux
whose arm value $T(1,2)\in\{i,i+1\}$. (Direct seminormal check: $S_i$ kills every $v_a$
with $a\notin\{i,i+1\}$ since $i,i+1$ are then both in column 1; on the remaining
2-dimensional space it's the rank-1 $q$-eigenprojection.)

So a descending product $\prod_{i\in A}S_i$ has image **pinned by its leftmost factor**
$S_{\max A}$, with support arm-value $\ge\max A\ge|A|$. That is the entire hook deficit
bound — no induction, just "leftmost factor wins." The off-hook bound then follows by the
established $\Rp_n$-branching:

- **$T_{n-1}$ retained:** image lands in $E^+_{n-1}=\Phi(V^{(2,1^m)})$, pull through to
  the hook bound. (Bonus: deletions *inside* the last block below its head are free — this
  is exactly the "cost-free interior deletions" seen in the kill-point census.)
- **$T_{n-1}$ deleted:** chain $\in H_q(S_{n-1})$, branches to the larger hook
  $(2,1^{m+1})$ (closed by the same rank-1 fact) and the smaller off-hook $(2,2,1^{m-1})$
  (strong induction on $m$).

## Status / what I'd want you to check

**Fully rigorous & m-uniform:** the rank-1 lemma, the hook deficit bound (sharp), the
off-hook lift for all $U$ retaining $T_{n-1}$, the per-subset corollary.

**One soft spot:** in the $T_{n-1}$-deleted case, the *smaller-off-hook* summand closes by
strong induction on $m$ whose descent is the head/branching dichotomy itself; the
squaring rewrite $\Rp_{n-1}=S_{n-2}\Rp_{n-2}$ across the branching is the same mechanism as
the proved May-28 "position 15" lemma, applied recursively. I verified the bound
exhaustively for $m\le4$ (all tail subsets, exact, two $q$). I believe it's correct but
the recursive bookkeeping is presented at reduction-level rigor, not fully spelled out.

**Not closed (honest):** the *full* strong vanishing $M(S)\equiv0$ for $|S|<D$. This
deficit law is the **tail half**. Two pieces remain: (i) a prefix counterpart controlling
$M_R(S_R)$, and (ii) the regime $|S_T|\ge\tau$. See the Remark in §6.

## Scripts

`~/projects/scratch/2026-05-29-strong-pillar1/` (test1–test6.py). All exact rational, $q=5/7$
cross-checked at $q=2/3$.
