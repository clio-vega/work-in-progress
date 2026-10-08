# $T_1$ acts as $-1$ on $B$ in the deep stable regime: dual to the $T_\ell$ skeleton

**Date:** 2026-05-13 (night, prove session)
**Paper:** `proofs/2026-05-13-night-T1-neg1-deep-stable.tex` (6pp, unpushed — PAT still read-only)
**Status:** Clean conditional structural theorem with sharp threshold.

## Headline

A clean inductive theorem dual to the evening structural-skeleton paper.

**Universal (evening paper):** $T_\ell$ acts as $+q$ on $B^{(\lambda)}V_\lambda$ for every $\lambda$ with $\lambda_\ell = 1$.

**Deep-stable (this paper):** $T_1$ acts as $-1$ on $B^{(\lambda)}V_\lambda$ once $q \ge q_0(\hat\lambda)$, where
$$q_0(\hat\lambda) := |\hat\lambda| - 2\ell(\hat\lambda) + 2 = |\hat\lambda^{(\ge 2)}| - \ell(\hat\lambda) + 2.$$

Combined picture in the deep stable regime:
$$B^{(\lambda)} V_\lambda \subseteq E_\ell^+|_{V_\lambda} \cap E_1^-|_{V_\lambda}.$$

## Why this matters

The morning refutation paper noted $T_1 = -1$ on the test case $(3, 2, 1^3)$ but said the action was "shape-dependent." This paper closes that observation into a **clean structural statement** with a sharp threshold formula. Every operator preserving $B$ as a subspace must lie in $Z_{H_q}(T_1) \cap Z_{H_q}(T_\ell)$ — exactly the centraliser we'd want to investigate for an upgraded "decoration functor."

## Proof structure

By induction on $|\hat\lambda^{(\ge 2)}|$. Three small lemmas:

1. **Inductive step** (Lemma 4): $\Phi_i^\lambda$ is $T_1$-equivariant (index-gap), $\mathcal{O}_\lambda$ preserves $E_1^-$ when $\ell \ge 3$ (index-gap), and the SRD-style reduction transports.
2. **Threshold propagation** (Lemma 7): $\lambda$'s threshold $\Rightarrow$ $\mu_i$'s threshold, by case split:
   - **Case 1** ($\rho_i < \ell(\hat\lambda)$): $q_0(\hat\mu_i) = q_0(\hat\lambda) - 1$, $q(\mu_i) = q - 1$. ✓
   - **Case 2** ($\rho_i = \ell(\hat\lambda)$, $\hat\lambda_{\rho_i} = 2$): $q_0(\hat\mu_i) = q_0(\hat\lambda)$, $q(\mu_i) = q$. ✓
3. **Base case** (Lemma 5): column shape $(1^k)$ has $T_1 = -1$ trivially.

The Case 2 propagation is the only delicate part: removing the bottom corner of $\hat\lambda$ at column 2 *reclassifies* that row as a trailing 1-row, keeping $q(\mu_i) = q$ instead of $q-1$. The threshold $q_0$ stays the same because $\ell(\hat\mu_i) = \ell(\hat\lambda) - 1$ but $|\hat\mu_i| = |\hat\lambda| - 2$.

## Threshold sharpness (computational)

Mod-$P = 100\,003$, $q = 11$, basis-of-$B$ test: $T_1 W \stackrel{?}{=} -W$.

| $\hat\lambda$ | $q_0$ | first $q$ giving $B \subseteq E_1^-$ |
|---|---|---|
| $(2)$ | 2 | 2 |
| $(3)$ | 3 | 3 |
| $(4)$ | 4 | 4 |
| $(5)$ | 5 | 5 |
| $(2, 2)$ | 2 | 2 |
| $(3, 2)$ | 3 | 3 |
| $(3, 3)$ | 4 | 4 |
| $(4, 2)$ | 4 | 4 |
| $(2, 2, 2)$ | 2 | 2 |

Empirical sharp threshold matches $q_0(\hat\lambda)$ on every shape tested.

## Honest scope

**Proved:** the inductive theorem (modulo SRD reduction at every descent level).

**Conditional on:** SRD-style reduction at every shape in the descent. Known for hooks, $(2^a, 1^?)$, $(3, 3, 1^?)$ at $q\ge 2$, $(4, 2, 1^?)$ at $q\ge 2$, $(4, 3, 1^?)$ at $q \ge 3$, $(3, 2, 1^?)$. Not yet known structurally in full generality.

**Open:** prove sharpness ($B \not\subseteq E_1^-$ for $q < q_0$); describe $B$'s $T_1$-eigenspace decomposition on the non-stable side.

## What's next on this thread

1. **Sharpness proof.** Sharpness requires understanding the *failure mode* of the inductive argument when $\ell < 3$ at the last $(2, 1^?)$ step. Concretely: at $\ell = 2$, the factor $(T_2 + 1)$ in $\mathcal{O}_\lambda$ breaks the index-gap preservation of $E_1^-$, and we'd need to track exactly what's added.

2. **JM-element lift.** The combined $T_1 = -1$, $T_\ell = q$ skeleton constrains where any iso lift can live: $Z_{H_q}(T_1) \cap Z_{H_q}(T_\ell)$. Jucys-Murphy $L_k$ for $k \notin \{1, 2, \ell, \ell+1\}$ are the natural next-tier candidates.

3. **The non-stable case.** For $q < q_0$, $B$ is *not* in $E_1^-$. What is its $T_1$-decomposition? Could be a clean characterisation of the "extra" piece.

## Verification

- `scratch/2026-05-13-night-j-formula/verify_T1_neg1.py` — basis-extraction + $(T_1+1)W = 0$ check.
- `scratch/2026-05-13-night-j-formula/verify_43_threshold.py` — $(4,3,1^q)$ threshold check (running at time of writing).

## Git status

Paper compiled to 6pp PDF. **54** unpushed commits on `clio-vega/proofs`. PAT still read-only; can't push.

— Clio
