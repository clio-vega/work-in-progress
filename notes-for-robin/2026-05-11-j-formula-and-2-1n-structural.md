# j-formula refinement + structural proof for the (2, 1^{n-2}) family

**Date:** 2026-05-11 prove session
**Writeup:** `~/projects/proofs/2026-05-11-j-formula.tex` (7pp, compiled)

## Headline

Sharpened the May-8 *boundary lemma* (the gap that the rank-zero
theorem reduces to for $n \ge 8$ even) into a precise and stronger
conjecture, the **j-formula**, and proved it structurally for one
infinite family.

## The j-formula

For $\lambda \vdash n$ with $\ell(\lambda) = \ell > \lceil n/2 \rceil$
(rank-zero regime) and $\lambda \ne (1^n)$:
$$ B_{\ell+1}(V_\lambda) := R_{\ell+1}' R_{\ell+2}' \cdots R_n'(V_\lambda) \subseteq E_1^-, $$
with $j = \ell+1$ **sharp** ($B_{\ell+2}$ does not lie in $E_1^-$).

Plus a **rank-corner formula** (also conjectural):
$$ \text{rank}\, B_{\ell+1}|_{V_\lambda} = \#\{r < \ell : \lambda_r > \lambda_{r+1}\}. $$
The number of corners of $\lambda$ in rows $1, \ldots, \ell-1$ — the
length-preserving corners.

Both verified computationally at every rank-zero non-sign $\lambda
\vdash n$ for $4 \le n \le 8$ (15 cases). At $n=8$ the boundary
partitions are $(4,1^4), (3,2,1^3), (2,2,2,1,1)$ — the smallest cases
not yet covered by the May-8 paper.

## The structural proof for $(2, 1^{n-2})$

For the family $\lambda = (2, 1^{n-2})$ (length $\ell = n-1$,
$j = n$, so $B_n = R_n'$ — a single block), I proved:

**Theorem.** $R_n'(V_{(2, 1^{n-2})}) \subseteq E_1^-$, and the image
is one-dimensional.

**Mechanism: the shifting window.** SYTs are parameterized by
$T^{(a)}$ where $a + 1$ sits at position $(1, 2)$ and the remaining
values fill column 1. The action of each $T_k$ in the seminormal
basis is *tridiagonal* in the index $a$:
- $T_k v_{T^{(a)}} = -v_{T^{(a)}}$ for $a \notin \{k-1, k\}$.
- $T_k$ couples $v_{T^{(k-1)}}$ and $v_{T^{(k)}}$ as a $2 \times 2$
  Hoefsmit block.

Tracking the image $W_k$ after step $k$ of $R_n'$ by induction:
$W_k = \mathrm{span}(v_{T^{(k)}}^+)$ where $v_{T^{(k)}}^+$ is the
$+q$-eigenvector of $T_k$ in the block. Each step $(T_k+1)$
annihilates the "stale" component $v_{T^{(k-2)}}$ (since
$T_k v_{T^{(k-2)}} = -v_{T^{(k-2)}}$) and projects the surviving
component to the new $+q$-eigenvector.

After step $n-1$: image in $\mathrm{span}(v_{T^{(n-2)}}, v_{T^{(n-1)}})
\subseteq E_1^-$ (both have $a \ge 2$, so $2$ is in column 1).

**Corollary.** $\Pi^{S_n}|_{V_{(2, 1^{n-2})}} = 0$ unconditionally for
every $n \ge 2$. (Previously: only known up to $n=7$ via the May-8
boundary computation.)

## Inductive strategy and the obstruction

For the general j-formula at $\lambda$, the natural induction via
branching $V_\lambda \downarrow_{S_{n-1}} = \bigoplus_{\mu \prec
\lambda} V_\mu$ goes through cleanly for every $\mu$ with $\ell(\mu)
= \ell$ (corner removed from a row $r < \ell$): IH at $n-1$ applies
directly.

The obstruction is the **row-$\ell$ corner** removal, $\mu =
\lambda^-$ with $\ell(\mu) = \ell - 1$. In the boundary regime
($n = 2k$, $\ell = k+1$), $\mu$ sits at the rank-zero *threshold* at
$n-1$ — the j-formula doesn't apply. In the deep regime,
$\mu \in $ rank-zero at $n-1$, but the j-formula gives the wrong
index ($B_\ell^{(n-1)}$, not $B_{\ell+1}^{(n-1)}$ — the latter has
one fewer factor).

The needed strengthening is precisely:
$$ \widetilde B_{\ell+1}^{(n-1)}\, W_\mu \subseteq E_1^-, $$
where $W_\mu = \mathrm{proj}_{V_\mu}(R_n' V_\lambda) \subset V_\mu$ is
the projection of the image of $R_n'$ onto the $V_\mu$-summand. So
the question reduces to: what is $W_\mu$?

## Open problems raised

1. Prove the j-formula for $\lambda = (k, 1^{n-k})$ (single
   non-column-1 row). Generalizes my $k=2$ proof; needs a
   multi-parameter shifting argument.
2. Prove the rank-corner formula structurally — find an explicit
   basis of $\text{Im}\, B_{\ell+1}$ indexed by length-preserving
   corners.
3. The first non-hook test case for the rank-corner formula is
   $\lambda = (3, 3, 1^4)$ at $n=10$, where $\lambda^{>1} = (2,2)$
   has 2 SYTs but only 1 length-preserving corner. Conjecture
   predicts rank 1, distinguishing the two formulas.

## Push status

Still 21 unpushed commits (read-only PAT). Today's contribution:
1 new commit (`5756dd5`).

## Honesty check

The j-formula is **strictly stronger** than the boundary lemma. The
boundary lemma asks for *some* $j$; the j-formula identifies the
smallest such $j$, namely $\ell + 1$. So a structural proof would
both close the rank-zero theorem AND give finer information about
the operator.

What's *not* proven today: the j-formula at general boundary $\lambda$
for $n \ge 8$ even — though the obstruction is now precisely
identified.
