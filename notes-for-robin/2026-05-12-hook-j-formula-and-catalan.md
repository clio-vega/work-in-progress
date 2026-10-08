# j-formula for $(3, 1^{n-3})$ + Catalan support phenomenon

**Date:** 2026-05-12 prove session
**Writeup:** `~/projects/proofs/2026-05-12-hook-j-formula.tex` (9pp, compiled)
**Commit:** `9b532b6` (unpushed --- now 22 unpushed commits, PAT still
read-only)

## Headline

Extended the May-11 structural proof of the j-formula from $k=2$ hooks
($\lambda = (2, 1^{n-2})$) to $k=3$ hooks ($\lambda = (3, 1^{n-3})$) at
every $n \ge 6$.  Closing one more infinite family of the rank-zero
theorem unconditionally.

Plus: documented a striking computational phenomenon I noticed during
the search --- a **Catalan structure** governing the support of the
spanning vector for all hook irreducibles in the rank-zero regime.

## The k=3 proof

For $\lambda = (3, 1^{n-3})$, $n \ge 6$:
$$ R'_{n-1} R'_n V_\lambda \subseteq E_1^-, \quad \dim = 1. $$

The proof is a clean step-by-step image trace in two phases:

**Phase A** ($R'_n$): The image after each Hecke factor of $R'_n$ has
dimension $n-2$ and an explicit basis built from $+q$-eigenvectors of
the current $T_j$.  After all $n-1$ steps, $W_n$ has basis
$\{u^+_{(c, n-1)} : c = 2, \ldots, n-2\} \cup \{v_{(n-1, n)}\}$.  Every
basis vector is supported on subsets $S = (a, b)$ with $b \in \{n-1, n\}$.

**Phase B** ($R'_{n-1}$): The first factor $(T_1+1)$ collapses $W_n$ to
$\mathrm{span}(u^+_{(2, n-1)})$ --- 1-dimensional --- because all other
basis vectors of $W_n$ have $a \ge 3$ and are in $E_1^-$.

The remaining factors $(T_2+1), \ldots, (T_{n-2}+1)$ operate as a
**shifting window**: each step kills two of four supports (those with
$a = j-1$, where $T_j$ acts as $-1$) and rotates the other two to a
$+q$-eigenvector of $T_j$ in the 2-block (axial distance $d = j$).
After step $j$, the support is $\{(j, n-1), (j+1, n-1), (j, n), (j+1, n)\}$.

The final step $(T_{n-2}+1)$ is the only "irregular" one, producing a
5-element support
$\{(n-3, n-2), (n-3, n-1), (n-2, n-1), (n-2, n), (n-1, n)\}$.
All have minimum $\ge n-3 \ge 3$, hence in $E_1^-$.

## The Catalan support phenomenon

This is the more exciting discovery.  Computational data at $n \le 8$
for $k = 2, 3, 4$ shows:

> For hook $\lambda = (k, 1^{n-k})$ in rank-zero regime, the spanning
> vector of $B_{\ell+1} V_\lambda$ has support of size **exactly $C_k$**
> (the $k$-th Catalan number), on subsets of the "top range"
> $R_k(n) = \{n-2k+3, \ldots, n\}$.

Verified:
- $k=2$: $C_2 = 2$ singletons $\{n-1\}, \{n\}$.
- $k=3$: $C_3 = 5$ pairs from $\{n-3, n-2, n-1, n\}$, all except the
  "extreme" pair $(n-3, n)$.
- $k=4, n=8$: $C_4 = 14$ triples from $\{3, \ldots, 8\}$.  6 triples
  excluded: $\{(3,4,7), (3,4,8), (3,5,8), (3,6,8), (3,7,8), (4,7,8)\}$.

The Catalan identity $C_k = \binom{2k-2}{k-1} - \binom{2k-2}{k-3}$
matches the (size of top range) choose ($k-1$) minus the (number
excluded).

**If the Catalan conjecture holds, the j-formula for hooks follows
immediately**: the top range starts at $n-2k+3 \ge 3$ (since $n \ge 2k$),
so all supports avoid the value 2, hence the spanning vector lies in
$E_1^-$.  This is captured in Cor.~5 of the writeup.

## Open questions

1. Combinatorial characterization of the $C_k$-element support family.
   I tried Dyck paths, partition shapes inside a $(k-1)\times(k-1)$
   box, axial-distance rules --- none cleanly separated the supported
   from the excluded.  Probably encodes a non-crossing or non-nesting
   structure I haven't pinned down.

2. Structural proof for $k \ge 4$.  The $k=3$ proof relies on the
   image of $W_n$ being killed to dim 1 by the first factor of
   $R'_{n-1}$.  For $k \ge 4$, that first factor leaves the image at
   dim $\binom{n-3}{k-3} > 1$.  A multi-dimensional shifting argument
   is needed.

3. Generalization to non-hook $\lambda$.  Probably the support is
   governed by a $\kappa(\lambda)$-tuple of Catalan-like structures,
   one per length-preserving corner.  Worth verifying on
   $\lambda = (2, 2, 1^{n-4})$ at $n = 8$.

## Honesty check

The $k = 3$ structural proof is solid.  The verification script
(`verify_k3_proof.py`) confirms every intermediate dimension and
support pattern at $n = 6, 7, 8$.

The Catalan conjecture is computational at $n \le 8$ for $k \le 4$.
Extending to $k = 5$ would require $n = 10$ (boundary case
$(5, 1^5)$) where the seminormal computation has $\dim V_\lambda =
\binom{9}{4} = 126$.  Doable but not done today.

The combinatorial rule for the $C_k$-family is the most tantalizing
open question.  I noticed the support sizes are Catalan but couldn't
crack the rule despite trying multiple natural encodings.  Wondering if
you (or Lyra) might see a connection I'm missing --- it has the flavor
of something Lyra's "non-crossing partitions ↔ functor composition"
work might illuminate.

## Push status

22 unpushed commits.  Read-only PAT still blocking.
