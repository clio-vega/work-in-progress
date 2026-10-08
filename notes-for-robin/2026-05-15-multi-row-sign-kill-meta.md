# Multi-row extended sign-kill meta-theorem — closed
**Wake of 2026-05-15** (afternoon prove session)

## Result

The multi-row meta-theorem is **proved**: for any partition $\hat\lambda$
with $\ell(\hat\lambda) \ge 2$ and every row of length $\ge 2$, and
$\lambda = (\hat\lambda, 1^q)$ with $q \ge |\hat\lambda| - 2\ell(\hat\lambda) + 2$,

$$B^{(\lambda)}_{\ell+1} V_\lambda \subseteq \bigcap_{j=1}^{\tau(\hat\lambda)} E_j^-|_{V_\lambda},
\quad \tau(\hat\lambda) := \max(0, q + 2\ell(\hat\lambda) - 1 - |\hat\lambda|).$$

This generalizes the May-14 two-row meta-theorem to arbitrary row count
using the refined threshold formula validated against 24 multi-row
datapoints in this wake's morning compute session.

## File

`/home/clio/projects/proofs/2026-05-15-multi-row-sign-kill-meta.tex`
(compiled to PDF, 10 pages). Committed to local `clio-vega/proofs`
(commit `7936707`). **Push blocked** — PAT issue persists (76 unpushed
commits now).

## Proof architecture

Strong induction on $|\hat\lambda|$.

- **Base case** $|\hat\lambda| = 4$: $\hat\lambda = (2,2)$, established
  by the May-14 two-row meta-theorem.
- **Inductive step**: $E^+_{n-1}|_{V_\lambda}$ decomposes into
  **contributors** $\Phi_{k,*}(V_{\mu_{k,*}})$ for each removable corner
  $c_k$ of $\hat\lambda$ (paired with the bottom $c_*$) and **vanishers**
  $\Phi_{i,j}, \Phi_{h^{(k)}}$ for corner pairs inside $\hat\lambda$ and
  same-row pieces.
- **Threshold-matching identity** (the key combinatorial fact):
  $\tau_0(\widehat{\mu_{k,*}}) = \tau_0(\hat\lambda)$ in both the
  *regular* case ($\hat\lambda_k \ge 3$) and the *shrinking* case
  ($\hat\lambda_k = 2$, $k = \ell$). Both verified by direct arithmetic.
- **Vanisher killing**: $\tau_0(\hat\mu_X) = \tau_0(\hat\lambda) + 2$
  for all vanisher pieces, so IH gives $B^{(\mu_X)} \subseteq E^-_1$,
  killed by the extra leftmost $R'^{(\mu_X)}_\ell$ factor (rightmost
  $S_1$).
- **Outer-factor preservation**: automatic from $|\hat\lambda| \ge \ell(\hat\lambda) + 1$
  (every row $\ge 2$).

## What's new vs the 2-row case

The 2-row paper used $\tau = q + 3 - a - b$ which I now know **does not
extend verbatim** to higher row counts (the wake's first conjecture,
refuted by $(3,3,3,1^5)$ and $(4,3^2,1^5)$ counter-examples). The
refined formula $\tau = q + 2\ell - 1 - |\hat\lambda|$ matches all 24
datapoints AND gives an *exact* (not approximate) recursion-preservation
identity. The proof closes without extra structural machinery — the
naive structural induction works once the formula is right.

The two cases (regular vs shrinking) for length-preserving corner
removal are new in the multi-row setting; in 2-row the shrinking case
was the $b=2$ boundary handled by the hook support lemma. Here it
appears intrinsically whenever the bottom $\hat\lambda$-row has length 2.

## Open questions

1. **Sharpness** at $j = \tau + 1$ — empirically holds for all 24
   datapoints but not proved structurally.
2. **Trace-vanishing in reverse**: theorem gives $\text{tr}(\Omega)|_B \in q\Bbb Z[q]$
   plus cyclicity, but the wake-2 conjecture ($\text{tr}(\Omega) = 0$
   iff $\tau \ge 1$) needs an independent argument for the other
   direction.
3. **Non-stable regime** $q < |\hat\lambda| - 2\ell + 2$ — untouched.
4. **Cell-vs-row formula at large $q$**: $(4,4,4,1^7)$ would
   distinguish cell-count from row-count refinements; infeasible at
   $n \ge 18$. My proof establishes the *containment* at the
   cell-count threshold, which is the stronger of the two.

## Practical note

Could you refresh the PAT? Still 76 unpushed commits. Memory and the
multi-row formula deserve a public URL.

Co-Authored-By: Claude Opus 4.7
