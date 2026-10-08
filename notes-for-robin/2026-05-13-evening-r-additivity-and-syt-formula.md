# 2026-05-13 evening: General-r dim-additivity + closed-form SYT formula (structural)

**Paper:** `2026-05-13-r-additivity-and-syt-formula.tex` (8pp).

## What's new

The May-13 afternoon LB-closed paper proved an **r=2 dim-additivity meta-theorem** structurally:

> Under the SRD reduction at $\lambda$ with two length-pres corners $c_1, c_2$ and column-1 bottom $c_*$,
> $\dim B^{(\lambda)} = \dim B^{(\mu_1)} + \dim B^{(\mu_2)}$ where $\mu_i = \lambda \setminus \{c_i, c_*\}$.

Remark 9 of that paper sketched the $r$-general extension. **This paper formalises it for all $r$.**

## Main theorem (general-$r$ dim-additivity)

For $\lambda$ with $r \ge 1$ length-pres corners $c_1, \ldots, c_r$ and column-1 bottom $c_*$, under the SRD-style reduction
$$B^{(\lambda)} = \mathcal{O}_\lambda \big[ \sum_{i=1}^r \Phi_i^\lambda(B^{(\mu_i)}) \big],$$
**we have $\dim B^{(\lambda)} = \sum_{i=1}^r \dim B^{(\mu_i)}$.**

**Proof.** Transcribes the r=2 proof verbatim. The $r$ unordered cell pairs $\{c_i, c_*\}$ all share $c_*$ but differ in the other element ($c_1, \ldots, c_r$ are distinct length-pres corners). So the seminormal SYT supports of the $r$ pieces $\Phi_i^\lambda(V_{\mu_i})$ are pairwise disjoint. Each piece lies in $E_{n-1}^+|_{V_\lambda}$ (non-degenerate 2-block). The outer chain $\mathcal{O}_\lambda$ is injective on $E_{n-1}^+$ by adjacent-injectivity (chained $(T_j+1)$'s). The $r$-piece direct sum has dimension $\sum_i \dim B^{(\mu_i)}$, preserved by $\mathcal{O}_\lambda$.

## Corollary (closed-form SYT formula)

If $\lambda$ is in the **fully stable regime** (SRD reduction holds at every shape in the recursive descent tree from $\lambda$ down to column shapes), then
$$\dim B^{(\lambda)} = f^{\lambda^{(\ge 2)}}.$$

**Proof.** Induction on $n = |\lambda|$. Base case $\lambda = (1^n)$: $\dim B = 1 = f^{\emptyset}$. Inductive step: by additivity, $\dim B^{(\lambda)} = \sum_i \dim B^{(\mu_i)}$. By induction, each $\dim B^{(\mu_i)} = f^{\mu_i^{(\ge 2)}}$. A computation (Lemma 7) shows $\mu_i^{(\ge 2)} = \lambda^{(\ge 2)} \setminus c_i^{(\ge 2)}$ where $c_i^{(\ge 2)}$ ranges over corners of $\lambda^{(\ge 2)}$. Hence
$$\sum_i f^{\mu_i^{(\ge 2)}} = \sum_{c \text{ corner of } \lambda^{(\ge 2)}} f^{\lambda^{(\ge 2)} \setminus c} = f^{\lambda^{(\ge 2)}}$$
by the SYT branching identity.

This upgrades the closed-form SYT formula from a numerical conjecture (May-13 multi-corner paper) to a **structural theorem** under the fully-stable hypothesis.

## Computational verification at r=3

Family $(4, 3, 2, 1^t)$, $\hat\lambda^{(\ge 2)} = (3, 2, 1)$, $f = 16$:

| $t$ | $n$ | $\dim V$ | $\dim B$ | Target | Verdict |
|---|---|---|---|---|---|
| 0 | 9 | 168 | 16 | 16 | matches (outside framework, no $c_*$) |
| 1 | 10 | 768 | 24 | 16 | non-stable |
| 2 | 11 | 2310 | 40 | 16 | non-stable |
| 3 | 12 | 5632 | **16** | 16 | ✓ stable |

At $t = 3$ (stable), verifying additivity:
- $\mu_1 = (3, 3, 2, 1^2)$: $\dim B = 5 = f^{(2,2,1)}$
- $\mu_2 = (4, 2, 2, 1^2)$: $\dim B = 6 = f^{(3,1,1)}$
- $\mu_3 = (4, 3, 1^3)$: $\dim B = 5 = f^{(3,2)}$
- **Sum = 5 + 6 + 5 = 16 ✓**

This is the first r=3 verification of the dim-additivity (and hence of the closed-form SYT formula in a stable regime).

## What this resolves

1. **Formalises Remark 9 of LB-closed**: the r=$r$ extension is now a theorem, not a sketch.
2. **Upgrades the closed-form SYT conjecture to a structural theorem** (conditional on fully-stable regime, which is shape-dependent but well-defined).
3. **r=3 stability threshold**: empirically $t \ge 3$ for $(4, 3, 2, 1^t)$, sharper than the crude $t \ge |\lambda^{(\ge 2)}|$ bound. The threshold is also non-monotone in $t$ (matches at $t = 0$ via a different mechanism!).

## What remains open

1. **Structural proof of the SRD-style reduction at general $\lambda$**: currently proved only for individual shape families. A general proof would close the closed-form SYT formula unconditionally.
2. **Sharp stability threshold $t_0(\widehat\lambda)$**: the decoration-iso-failed paper showed shape-dependent thresholds with non-monotone matching sets. A clean characterisation remains open.
3. **The $t = 0$ phenomenon**: at $(4, 3, 2)$ with no trailing 1-rows, $\dim B = 16$ matches the closed form despite my framework not applying (no $c_*$). This suggests a different reduction operates at the boundary.

## Honest scope

- T1 is **proved structurally** modulo the SRD reduction hypothesis (which is the substantive content).
- Corollary is **conditional** on the fully-stable regime.
- Computational verification covers $r \in \{1, 2, 3\}$.

## Connection to decoration-iso refutation

This morning's `2026-05-13-decoration-iso-failed.tex` refuted any naive Hecke iso $B^{(\lambda)} \cong V_{\lambda^{(\ge 2)}}$ under standard parabolic embeddings. The present paper gives the next best thing: a structural derivation of the **numerical** dim equality, via direct decomposition of $V_\lambda$. No rep-theoretic upgrade is claimed, but the dim equality is no longer a numerical coincidence — it has a clean structural derivation chain.

## Git status

37 unpushed commits on `clio-vega/proofs`. PAT still read-only. New paper not yet committed; will commit + (try to) push after this note is filed.
