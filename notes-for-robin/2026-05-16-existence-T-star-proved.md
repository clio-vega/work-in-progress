# Conjecture 4.6 proved — column-descent-free SYT existence

**Robin** — closing the trace-vanishing converse direction.

## Result

For every $\lambda = (\hat\lambda, 1^q)$ with $\ell(\hat\lambda) \ge 2$, all
$\hat\lambda_r \ge 2$, $q \ge 1$, and $\tau(\hat\lambda) = 0$
(equivalently $q \le M+1$ where $M = |\hat\lambda| - 2L$), there
exists a standard Young tableau $T^*$ of shape $\lambda$ with
$T^*(0,0) = 1$, $T^*(0,1) = 2$, and no column descent.

Combined with the per-SYT positivity lemma (already proved in
`2026-05-17-converse-per-syt-positivity.tex`) and the forward
direction (`2026-05-16-trace-vanishing-from-pillar1.tex`), this
closes the trace-vanishing equivalence:

$$\mathrm{tr}_{V^\lambda}(\Omega^{(\lambda)}) \equiv 0 \iff \tau(\hat\lambda) \ge 1.$$

## Paper

https://github.com/clio-vega/proofs/blob/main/2026-05-16-existence-T-uniform-proof.tex

PDF: https://github.com/clio-vega/proofs/blob/main/2026-05-16-existence-T-uniform-proof.pdf

## The construction in one paragraph

Let $k$ = number of rows of $\hat\lambda$ of length $\ge 3$.  Place
column-$0$ values: $T^*(r, 0) = 2r+1$ for $r < k$ (the "low odds"),
then $T^*(r, 0) = n - 2(L+q-1-r)$ for $r \ge k$ (high values spaced
by 2 ending at $n$).  Fill the remaining cells in row-superstandard
order with the leftover values.  That's it.

## Why it works — three observations

1. **Column-$0$ gaps $\ge 2$.**  Within each band the gap is $2$ by
   construction.  At the boundary $r = k-1 \to k$ the gap is
   $M - q + 3 \ge 2$, using $\tau = 0$.

2. **Row condition $T^*(r, 0) < T^*(r, 1)$.**  For long rows
   ($r < k$): the "first non-col-$0$ value in row $r$" is the
   $(a_r+1)$-th smallest non-col-$0$ value, and $a_r \ge 2r$ because
   long rows contribute $\ge 2$ to the increment.  Both bounds give
   $> 2r+1$.  For short rows ($r \ge k$, $\hat\lambda_r = 2$):
   direct computation gives the gap is $2q-1 \ge 1$.

3. **No column descent.**  Consecutive integers in the non-col-$0$
   sequence exist only in one "Section S2" of indices $[k, k+M-q+1]$
   (values $2k, 2k+1, \ldots$).  A column-descent in the
   non-col-$0$ region would require both consecutive-integer indices
   to land at a row-boundary $r \to r+1$ with $\hat\lambda_r = 2$.
   For such $r$ (necessarily $r \ge k$), the boundary index is
   $M + r + 1 > k + M - q + 1$, past the end of S2.  So no such
   pair exists.  The slack is exactly $q$, which is exactly what
   $\tau = 0$ buys us.

## Comparison with Algorithm N (yesterday's paper)

Algorithm N from `2026-05-16-existence-T-star.tex` is a different
construction (greedy with column-balance priority).  Conjecture 4.18
(Algorithm N non-stuckness) remains open as a combinatorial question
of independent interest, but it is **no longer load-bearing** for
the converse trace-vanishing direction.  Today's $T^*$ is fully
explicit and the proof is three lemmas of elementary inequalities.

## Computational verification

5957 / 5957 $\tau = 0$ shapes with $|\lambda| \le 25$ produce valid
column-descent-free SYTs.  Code:
`~/projects/scratch/2026-05-16-prove-non-stuck/final_verify.py`.

## Next questions

- **Multi-row sharpness** ($\tau \ge 1$ implies $\Omega V^\lambda
  \not\subseteq E^-_{\tau+1}$ generically): the natural next target
  now that the equivalence is closed.
- **Hoefsmit positivity for general bases** ($b' \ne 1$): is there
  a categorical lift that makes the positivity automatic?
- The proof's "exactly $q$ slack" structure looks like a shadow of
  some larger combinatorial fact about partition packing — worth
  noticing.
