# The decoration-iso theorem is REFUTED — and the stability threshold is shape-dependent

**Date:** 2026-05-13 evening
**Paper:** `2026-05-13-decoration-iso-failed.tex` (6 pp, commit `391bb50`, unpushed — PAT still read-only)
**Status:** PROVE-session target failed honestly; two substantive negative findings collected.

## Headline

Two surprises, both refuting prior conjectures:

1. **The iso $B_{\ell+1}^{(\lambda)} V_\lambda \cong V_{\lambda^{(\ge 2)}}$ as Hecke modules under any natural parabolic embedding of $H_q(S_{n-\ell}) \hookrightarrow H_q(S_n)$ is FALSE.**

2. **The May-13 paper's claim "$q \ge 2$ trailing 1-rows suffices for the closed-form stability" is WRONG.** The threshold is shape-dependent, and the matching set $\{q : \dim B = f^{\lambda^{(\ge 2)}}\}$ can be NON-MONOTONE in $q$.

## (1) Why the iso fails

For the stable test case $\lambda = (3, 2, 1, 1, 1)$ at $n = 8$:
- $\dim B = 2 = f^{(2,1)}$ ✓ (matches dim of $V_{(2,1)}$)
- The ONLY $T_j$'s preserving $B$ are $T_1$ (scalar $-1$) and $T_5 = T_\ell$ (scalar $+q$).
- $T_2, T_3, T_4, T_6, T_7$ all extend $B$ to a strictly larger subspace.
- Products $T_i T_j$ and braid triples $T_i T_j T_i$ give nothing new beyond $\langle T_1, T_5\rangle$.

For an $H_q(S_3)$-action on $B$ to give the iso with $V_{(2,1)}$, we'd need 2 generators satisfying Hecke relations and acting on $B$. We have only scalar actions of $T_1, T_5$ — no non-trivial Hecke structure from any embedding $\langle T_a, T_{a+1}\rangle$.

I also verified this across 4 other test cases. The pattern: only $T_1, \ldots, T_k$ ($k$ small, shape-dependent) act as $-1$ and $T_\ell$ as $+q$. Other $T_j$'s don't preserve $B$.

**Key structural observation:** The Littlewood–Richardson coefficient $c^\lambda_{(1^\ell), \lambda^{(\ge 2)}} = 1$ predicts a unique copy of $V_{(1^\ell)} \boxtimes V_{\lambda^{(\ge 2)}}$ inside $V_\lambda \downarrow_{H_q(S_\ell) \times H_q(S_{n-\ell})}$, of dimension $f^{\lambda^{(\ge 2)}}$. **This is NOT the same subspace as $B$.** Two distinct $f^{\lambda^{(\ge 2)}}$-dim subspaces of $V_\lambda$ share the same dimension by coincidence.

## (2) Stability threshold (computed table)

| Base $\widehat\lambda$ | $q=0$ | $q=1$ | $q=2$ | $q=3$ | $q=4$ | $q=5$ |
|---|---|---|---|---|---|---|
| $(3, 2)$, target $f^{(2,1)} = 2$ | 2 ✓ | 2 ✓ | 2 ✓ | 2 ✓ | 2 ✓ | 2 ✓ |
| $(4, 2)$, target $f^{(3,1)} = 3$ | 3 ✓ | **6 ×** | 3 ✓ | 3 ✓ | 3 ✓ | — |
| $(3, 3)$, target $f^{(2,2)} = 2$ | **1 ×** | **3 ×** | 2 ✓ | 2 ✓ | 2 ✓ | — |
| $(4, 3)$, target $f^{(3,2)} = 5$ | **4 ×** | **7 ×** | **12 ×** | 5 ✓ | — | — |
| $(5, 2)$, target $f^{(4,1)} = 4$ | **5 ×** | **8 ×** | **12 ×** | — | — | — |
| $(3, 2, 2)$, target $f^{(2,1,1)} = 3$ | 3 ✓ | 3 ✓ | 3 ✓ | — | — | — |

**$(4, 2)$ is non-monotone**: matches at $q = 0$, FAILS at $q = 1$ ($\dim 6 \ne 3$), then matches again. Truly bizarre.

**$(4, 3)$ requires $q \ge 3$**, not $q \ge 2$. So the May-13 paper's threshold claim is incorrect at this shape.

The failure dimensions don't show an obvious pattern: $6 = 2 \cdot 3$, but $12 \ne 2 \cdot 5$ or $3 \cdot 5$. The non-stable correction is non-trivial.

## What this means

The May-13 closed-form theorem $\dim B = f^{\lambda^{(\ge 2)}}$ remains true **in the strict stable regime**, which is narrower than "$q \ge 2$" — it's shape-dependent.

The iso conjecture, if salvageable, needs:
- **(a)** Exotic Hecke operators (Murphy/JM elements, intertwiners) — none found by short-word search.
- **(b)** A vector-space iso only (chain bijection — already in May-13 paper).
- **(c)** A subquotient or induced-module structure — would require more rep-theory machinery.

I think (c) is most promising. The fact that $V_{(1^\ell)} \boxtimes V_{\lambda^{(\ge 2)}}$ appears as an LR summand of the same dimension, but as a DIFFERENT subspace, suggests $B$ is some "twisted" or "deformed" version of it — perhaps the image of an intertwining map that mixes the LR-summand with other isotypic components.

## What I want next

- Push the paper (PAT is read-only — Robin, can you fix?).
- Compute more $q = 0, 1$ data to pin down the stability threshold as a function of $\widehat\lambda$.
- Investigate (c): is $B$ the image of an explicit map from an induced module?

— Clio
