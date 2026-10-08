# Structural dim = 2 for (3, 3, 1^q), q >= 4: lower bound closed

**Date:** 2026-05-13 afternoon-2 prove session
**Paper:** `2026-05-13-dim2-331-structural.tex` (6 pp, commit `eea24ff`, unpushed -- PAT still read-only as of session start)
**Status:** Unconditional structural at $q \ge 4$. Closes SRD-331 Remark 4.6 (lower bound was open structurally).

## What I set out to do

The for-robin note from the morning's $(4, 3, 1^q)$ lower-bound-analysis paper flagged the cleaner depth-2 case as a prerequisite: **structural $\dim B^{(\mu_A)}_{j_0} V_{\mu_A} \ge 2$ for $\mu_A = (3, 3, 1^{q-1})$**. SRD-331 had the upper bound $\dim \le 2$ structural at $q \ge 4$ but only computational lower bound at $q \in \{2, 3, 4, 5\}$ (Remark 4.6). I took aim at the lower bound.

## What I found

**A clean structural proof.** The reduction formula (SRD-331 Cor 4.3) gives
\[
   B_{\ell+1}^{(\lambda)} V_\lambda = (T_{n-4}+1)(T_{n-3}+1)(T_{n-2}+1)\,\Phi_*(B^{(\mu_1)} V_{\mu_1})
\]
with $\mu_1 = (3, 2, 1^{q-1})$, and the inner space is 2-dim by May-12 evening at $q \ge 4$.

**The new ingredient:** each outer factor $(T_j+1)$ maps $E_{j+1}^+|_{V_\lambda}$ **injectively** into $E_j^+|_{V_\lambda}$, because (i) its image lies in $E_j^+$ by the quadratic relation $T_j(T_j+1) = q(T_j+1)$, and (ii) its kernel $E_j^-$ intersects $E_{j+1}^+$ trivially by **adjacent disjointness** (May-19 abstract Phase A paper, swapped form).

Chaining the three factors:
\[
   E_{n-1}^+ \xrightarrow{(T_{n-2}+1), \text{inj}} E_{n-2}^+ \xrightarrow{(T_{n-3}+1), \text{inj}} E_{n-3}^+ \xrightarrow{(T_{n-4}+1), \text{inj}} E_{n-4}^+
\]

Since $\Phi_*(B^{(\mu_1)}) \subset E_{n-1}^+$ has dim 2, the image has dim 2. Hence $\dim B^{(\lambda)} = 2$.

## What this generalises

Theorem 5.1 of the paper: for **any** r=1 rank-zero shape $\lambda$ where SRD-style same-row-dies has been established and the $\{c_1, c_*\}$ 2-block is non-degenerate,
\[
   \dim B^{(\lambda)} = \dim B^{(\mu_1)}.
\]

The proof is shape-agnostic: image landing + adjacent disjointness, both universal $H_q(S_n)$-module facts. This subsumes hooks (Shift Lemma chain), $(3, 3, 1^q)$, $(4, 2, 1^q)$, and any future r=1 same-row family where the SRD framework gets established.

## Why the earlier "position-of-letter" attempt got stuck

The earlier proof-sketch (`2026-05-13-dim2-331/proof-sketch.md`) tried to use a position-of-$(n-2)$ projection to separate the chain-defined basis vectors $G_A, G_B \in B^{(\lambda)}$. It got stuck because $T_{n-3}$ and $T_{n-2}$ in the outer chain MOVE letter $(n-2)$, contaminating any position-of-letter separator.

**The correct argument doesn't track positions at all.** It uses the abstract module-structural fact that adjacent $T_j$-eigenspaces of opposite sign intersect trivially in any $H_q(S_n)$-module. The chain of injectivity arguments lives entirely in the +q-eigenspace tower, never touching the seminormal basis.

This is structurally cleaner than I expected. The position-of-letter framework is the right tool for **A vs B branch separation** in $r \ge 2$ shapes (where Hoefsmit case analysis is unavoidable), but **within a single branch** the abstract eigenspace argument is the right tool.

## What this does NOT close

The $(4, 3, 1^q)$ multi-corner lower bound. The argument gives full within-class linear independence of $\{F_A^1, F_A^2\}$ and $\{F_B^1, F_B^2, F_B^3\}$ in $V_\lambda$, but the lower-bound-analysis paper's Theorem 3.2 requires PROJECTED versions of (a) and (b). The projected vectors $\pi^{(c)}_n F_X^i$ are not in $E_{n-1}^+$ (the seminormal projection breaks the $T_{n-1}$-2-block's +q-eigenvector structure), so adjacent-injectivity doesn't directly apply.

A cross-class linear combination $\sum c_{A,i} F_A^i + \sum c_{B,j} F_B^j = 0$ could carry $c_3$-overlap (where $\Phi_A, \Phi_B$ both have $n$ at $c_3$) invisible to either $\pi^{(c_1)}_n$ or $\pi^{(c_2)}_n$ alone. So full within-class injectivity from this paper + A-vs-B decoupling from the LB-analysis paper still doesn't close it. The $(4, 3, 1^q)$ structural lower bound is still the tracer-pair Hoefsmit computation flagged in the morning paper.

## Computational verification

Mod-$P$ at $P = 100\,003$, $q = 11$:
- Adjacent-disjointness $E_j^- \cap E_{j+1}^+ = 0$ at $j \in \{n-4, n-3, n-2\}$: verified at $q \in \{4, 5, 6\}$.
- Outer-chain rank = $\dim E_{n-1}^+|_{V_\lambda}$ at $q \in \{4, 5, 6\}$ (no rank loss).
- Direct $\dim B^{(\lambda)} = 2$ at $q \in \{4, 5, 6\}$ via direct computation of $R'_{\ell+1}\cdots R'_n V_\lambda$.

Scripts: `~/projects/scratch/2026-05-13-dim2-331-lower/`.

## What I want next

- Push the paper (PAT still read-only -- Robin, can you fix? **46 unpushed commits + this one = 47 unpushed** on `clio-vega/proofs`).
- The adjacent-injectivity argument is more general than I used it. It suggests a clean meta-lemma: for any sequence of indices $a, a+1, \ldots, b$, the operator $\prod_j (T_j+1)$ is injective on $E_{b+1}^+$ for any $H_q(S_n)$-module. Worth recording as a general fact?
- The next reachable target on this thread is $(4, 3, 1^q)$ via the tracer-pair Hoefsmit computation. That's a finite explicit calculation; I expect it to close.

-- Clio
