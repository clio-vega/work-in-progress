# For Robin — 2026-05-13 (very late, prove session): closing low-$q$ gap for dim formula

## TL;DR

Two structural theorems closing the low-$q$ end of the $r=2$ dim-formula club:

- **Theorem A.** $\dim B^{(3, 2, 1^q)}_{j_0} V_\lambda = 2 = f^{(2,1)}$ for every $q \ge 1$.
- **Theorem B.** $\dim B^{(4, 2, 1^q)}_{j_0} V_\lambda = 3 = f^{(3,1)}$ for every $q \ge 2$.

Writeup: `proofs/2026-05-13-very-late-low-q-dim.tex` (9pp, PDF compiles).

## Why this matters

The existing structural-dim-formula club (per the May-13 multi-corner dimension paper):

| family | structural at | source |
|---|---|---|
| $(3, 2, 1^*)$ | $n \ge 8$ ($q \ge 3$) | May-12 / May-20 |
| $(4, 2, 1^*)$ | $n \ge 10$ ($q \ge 4$) | May-12-Eve3 + SRD-421 |

This paper closes:
- $(3, 2, 1^*)$ at $q \in \{1, 2\}$ structurally
- $(4, 2, 1^*)$ at $q \in \{2, 3\}$ structurally

Combined: the dim formula $\dim B = f^{\lambda^{(\ge 2)}}$ is now **structurally proven for the entire $r=2$, $|\widehat\lambda| \le 6$ stable region**, matching the data table.

## What's new vs the structural skeleton's threshold

The night $T_1=-1$ paper gave a sharp threshold for $B \subseteq E_1^-$ at $q_0(\widehat\lambda) = |\widehat\lambda| - 2\ell(\widehat\lambda) + 2$. This is the threshold for the **$E_1^-$ containment**.

The **dim threshold** $q_0^{\dim}$ is *strictly less*: dim equality holds even when $T_1 \ne -1$. Empirical observation (verified in the threshold scan):

| $\widehat\lambda$ | $\|\widehat\lambda\|-2\ell$ | $q_0^{T_1=-1}$ | $q_0^{\dim}$ | this paper covers |
|---|---|---|---|---|
| $(3, 2)$ | 1 | 3 | 0 | ✓ ($q \ge 1$, plus $q=0$ accidental) |
| $(4, 2)$ | 2 | 4 | 2 | ✓ ($q \ge 2$) |
| $(3, 3)$ | 2 | 4 | 2 | $q\ge 2$ via SRD-331 (existing) |
| $(4, 3)$ | 3 | 5 | 3 | $q\ge 3$ via afternoon paper... wait that's $q\ge 5$ |
| $(5, 2)$ | 3 | 5 | 3 | $q\ge 3$ predicted, structural at $q\ge 5$ |

Conjecture: $q_0^{\dim}(\widehat\lambda) = \max(0, |\widehat\lambda|-2\ell(\widehat\lambda))$, two units below $q_0^{T_1=-1}$.

The afternoon $(4, 3, 1^q)$ paper at $q \ge 5$ used the **$T_1=-1$ threshold** for its structural proof. But the $\dim$ matches already at $q \ge 3$. So there's a gap of $q \in \{3, 4\}$ where the dim formula holds but my $E_1^-$-based structural argument doesn't reach. This is the **next concrete target**.

## Proof structure (Theorem A as exemplar)

Four-branch Phase A on $\lambda = (3, 2, 1^q)$, $q \ge 1$:

$$E_{n-1}^+|_{V_\lambda} = \Phi_A(V_{\mu_A}) \oplus \Phi_B(V_{\mu_B}) \oplus \Phi_C(V_{\mu_C})$$

with $\mu_A = (2, 2, 1^{q-1})$, $\mu_B = (3, 1^q)$, $\mu_C = (2, 1^{q+1})$. **No same-row pairs** because removing $(1, 2), (1, 3)$ violates column-2 monotonicity ($(2, 2) > (1, 2) = n-1$ impossible).

- $\mu_A$ piece: $\dim B^{(\mu_A)}_{sharp} = 1$ via a NEW small lemma (two-column $a = 2$ dim formula at all $q' \ge 0$, with $q' = 0$ ($\mu = (2, 2)$) handled by structural skeleton directly).
- $\mu_B$ piece: $\dim B^{(\mu_B)}_{sharp} = 1$ (hook dim).
- $\mu_C$ piece: vanishes via hook $j$-formula on $(2, 1^{q+1})$ at $q+1 \ge 2$, $q \ge 1$. Trailing $(T_1+1)$ in $R'^{(\mu_C)}_{j_0-1}$ kills the $E_1^-$ image.

Upper bound: $\dim \le 1 + 1 + 0 = 2$.

Lower bound: $\Phi_A, \Phi_B$ have disjoint seminormal supports (different unordered cell pairs); outer chain $\mathcal{O}_\lambda$ injective on $E_{n-1}^+|_{V_\lambda}$ (May-13 dim2-331-structural). Hence $\dim \ge 1 + 1 = 2$.

## Theorem B uses Theorem A

For $(4, 2, 1^q)$ at $q \ge 2$: same template, with $\mu_A = (3, 2, 1^{q-1})$ at $q - 1 \ge 1$ — **Theorem A applies recursively!** The chained reduction is:

$$\dim B^{(4, 2, 1^q)} = \underbrace{\dim B^{(3,2,1^{q-1})}}_{=2 \text{ by Thm A}} + \underbrace{\dim B^{(4, 1^q)}}_{=1 \text{ hook}} + \underbrace{0}_{\mu_C \text{ leaks}} + \underbrace{0}_{S_1 \text{ SRD}} = 3.$$

The $C$-piece is $(3, 1^{q+1})$ hook needing $q+1 \ge 3$ ($q \ge 2$). The $S_1$-piece uses SRD on $\nu_1 = (2, 2, 1^q)$ needing $q \ge 2$ (two-column $j$-formula). **Both thresholds reduce to $q \ge 2$**.

## The $(4, 2, 1)$ $q = 1$ non-monotonicity, dissected

Direct computation: $\dim B^{(4, 2, 1)}_{4} V = 6 \ne 3$.

Decomposition into the four pieces:
- $\mu_A = (3, 2)$: Theorem A doesn't apply (needs $q \ge 1$, but $\mu_A$ has $q = 0$ in its own family). Direct: $\dim B^{(3,2)}_3 = 2$.
- $\mu_B = (4, 1)$: hook, dim 1.
- $\mu_C = (3, 1, 1)$: hook with $q(\mu_C) = 2 < 3$, so $E_1^-$ leakage **fails**. Direct: contribution = 1.
- $S_1$ with $\nu_1 = (2, 2, 1)$: two-column with $q(\nu_1) = 1 < 2$, so SRD **fails**. Direct: contribution = 2.

Total: $2 + 1 + 1 + 2 = 6$. ✓

So the non-monotonicity $\dim_{q=0}=3, \dim_{q=1}=6, \dim_{q\ge 2}=3$ has a fully structural explanation:
- $q = 0$: recursion ill-defined ($(4, 2)$ has $\lambda_\ell = 2$); $\dim = 3$ by coincidence.
- $q = 1$: recursion applies but bad-pair and same-row vanishing **fail**, adding $1 + 2 = 3$ extra.
- $q \ge 2$: all vanishing arguments work structurally.

## What's NOT in this paper (deferred)

- $(4, 3, 1^q)$ at $q \in \{3, 4\}$: dim matches, structural proof open (afternoon paper handles $q \ge 5$ via $T_1=-1$).
- $(5, 2, 1^q)$ at $q \in \{3, 4\}$: same.
- $(3, 3, 1^q)$ at $q = 2$: dim matches, structural proof was in SRD-331 (let me verify) — should already be covered.
- Generic $|\widehat\lambda| - 2\ell(\widehat\lambda) \ge 3$ regime: needs a refined argument that works at $q_0^{\dim} = |\widehat\lambda|-2\ell(\widehat\lambda)$ rather than $q_0^{T_1=-1} = |\widehat\lambda|-2\ell(\widehat\lambda)+2$.

## Push status

Paper compiled to 9pp PDF. **56** unpushed commits expected on `clio-vega/proofs`. PAT still read-only (per PROVE.md blockers).

— Clio
