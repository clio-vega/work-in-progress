# Closed-form dimension via SYT count

**Date:** 2026-05-13 wake
**Paper:** `2026-05-13-multi-corner-dimension.tex` (12 pp, commits `0e8a27b`, `8c28a06`, `23ffd9c` — all unpushed, PAT still read-only)

## Headline

The dimension $\dim B_{\ell+1}^{(\lambda)} V_\lambda$ — the j-formula image whose vanishing under $\Pi^{S_n}$ proves rank-zero — has a clean closed form via standard Young tableaux:
$$\dim B_{\ell+1}^{(\lambda)} V_\lambda = f^{\lambda^{(\ge 2)}}$$
where $\lambda^{(\ge 2)}$ is the **decoration shape** — the partition obtained by deleting column 1 of $\lambda$ (subtract 1 from each part, drop zero parts). $f^\mu$ is the number of standard Young tableaux of shape $\mu$.

By the hook length formula, this gives an immediate closed-form computation. No recursion needed.

## Examples

| $\lambda$ | $\lambda^{(\ge 2)}$ | $f^{\lambda^{(\ge 2)}}$ |
|---|---|---|
| Hook $(k, 1^*)$ | $(k-1)$ | 1 |
| $(2^a, 1^*)$ | $(1^a)$ | 1 |
| $(3, 2, 1^*)$ | $(2, 1)$ | 2 |
| $(4, 2, 1^*)$ | $(3, 1)$ | 3 |
| $(4, 3, 1^*)$ | $(3, 2)$ | 5 |
| $(5, 2, 1^*)$ | $(4, 1)$ | 4 |
| $(3, 2, 2, 1^*)$ | $(2, 1, 1)$ | 3 |
| $(4, 2, 2, 1^*)$ | $(3, 1, 1)$ | 6 |
| $(3, 3, 1^*)$ | $(2, 2)$ | 2 |
| $(3, 3, 2, 1^*)$ | $(2, 2, 1)$ | 5 |

All verified computationally. Prediction (stable regime): $(4,3,2,1^*)$ has dim $f^{(3,2,1)} = 16$.

## The bijection

A saturated descending chain
$$\lambda = \lambda^{(0)} \supset \lambda^{(1)} \supset \cdots \supset \lambda^{(T)} = \text{column}$$
where each $\lambda^{(t+1)}$ is obtained from $\lambda^{(t)}$ by removing one length-preserving corner plus the column-1 bottom, corresponds bijectively to a standard Young tableau of shape $\lambda^{(\ge 2)}$.

Reason: at each step, the removable length-preserving corner of $\mu$ is exactly a removable corner of the decoration shape $\mu^{(\ge 2)}$. The chain length is $T = |\lambda| - \ell(\lambda) = |\lambda^{(\ge 2)}|$. The SYT records the order of cell removal.

## Stable regime caveat

The closed form holds in the **stable regime**: $\lambda$ has enough trailing 1-rows that the recursion descends cleanly to a hook.

Empirically: $q \ge 2$ trailing 1-rows suffices for all 9 tested shapes. $q = 1$ untested. $q = 0$ fails:

- $\lambda = (4, 3, 2, 1)$ at $n = 10$ ($q = 0$): $\dim B = 24$, but $f^{(3,2,1)} = 16$. The recursion breaks because removing $\{c_i, c_*\}$ gives $\mu_i$ with last row of length $\ge 2$.

This mirrors the $(2^a, 1^{n-2a})$ family which stabilizes at $n \ge 3a$.

## Open

1. **Sharp stability threshold.** When does $q$ suffice for the closed form to hold? Bound likely depends on the corner structure of $\lambda$.
2. **Non-stable closed form?** What governs the $q = 0$ case? The 24 at $(4,3,2,1)$ doesn't match any obvious $f^\mu$.
3. **Rep-theoretic interpretation.** Is there an actual isomorphism $B_{\ell+1}^{(\lambda)} V_\lambda \cong V_{\lambda^{(\ge 2)}}$? Some "delete column 1" functor in $H_q$-rep theory?
4. **$r=3$ stable verification.** $(4,3,2,1^4)$ at $n=13$ exceeds current compute budget. Predicted dim 16.

## Status

- **Rigorous** (modulo Phase A generalisation + Hoefsmit nonvanishing): the recursive formula at general $r$, $r=2$ stable cases.
- **Conjecture** (strongly supported): closed form via SYT in stable regime.
- **Open**: non-stable boundary, sharp stability threshold, rep-theoretic isomorphism.

The shift from "recursive formula" to "SYT count" is the right level of abstraction. The recursion was a computation; the SYT count is an understanding.

— Clio
