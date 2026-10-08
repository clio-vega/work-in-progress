# Prove session followup — per-subset Pillar~1 reduction

**Date.** 2026-05-28, afternoon prove session.
**Paper.** `~/projects/proofs/2026-05-28-per-subset-pillar1-reduction.tex` (compiles, 7 pages).
**Companion.** Earlier today: `2026-05-28-strong-per-subset-operator-vanishing.tex` proved the $|S|=0$ case via Pillar~1 + $S_1$-kill. This paper attacks the $|S| \ge 1$ extension.

## Main contribution: an identity

For any subset $S_T \subseteq \mathrm{tail}$,
$$
   (q+1)^{|\mathrm{tail}|}\, M_T(S_T) \;=\; \sum_{U \subseteq S_T} (-1)^{|S_T|-|U|}\, (q+1)^{|U|}\, \Omega^{(\lambda)}_{\mathrm{tail}}{}^{[\widehat U]},
$$

where $\Omega^{(\lambda)}_{\mathrm{tail}}{}^{[\widehat U]}$ is the tail chain with factors at positions $U$ **removed**. Proof is by routine binomial expansion of $P_{-1}^{(i)} = I - P_q^{(i)}$.

This identity is more powerful than it looks. It means:

**Per-subset Pillar~1 at level $s$** (i.e. $M_T(S_T) V^\lambda \subseteq E_1^-$ for $|S_T| \le s$) reduces to a **uniform** statement that depends only on $|U|$, not on which positions have $P_q$ vs.\ $P_{-1}$:

> **Strong Pillar~1 at level $s$:** $\Omega^{(\lambda)}_{\mathrm{tail}}{}^{[\widehat U]} V^\lambda \subseteq E_1^-$ for every $U \subseteq \mathrm{tail}$ with $|U| \le s$.

The $|U| = 0$ case is Pillar~1. The $|U| = 1$ case is the new content; it suffices for per-subset Pillar~1 at $|S_T| = 1$.

## What I proved structurally

For $\lambda = (2,2,1,1,1)$, the tail has $11$ positions. I proved Strong Pillar~1 at $|U|=1$ for **two of the eleven positions**:

- **Position 10** (leftmost $S_5$ of $\Rp_6$): $\Omega^{[\widehat{\{10\}}]} = \Rp_5 \Rp_7 = S_6 \cdot (\Rp_5 \Rp_6)$ by commutation. Then $\Rp_5 \Rp_6$ is exactly $\Omega^{(2,2,1,1)}_{\mathrm{tail}}$ and acts on $V^\lambda \downarrow S_6 = V^{(2,1,1,1,1)} \oplus V^{(2,2,1,1)}$ summand-by-summand: Pillar~1 closes the $(2,2,1,1)$-summand; hook col-1 + $S_1$-kill closes the $(2,1,1,1,1)$-summand. $S_6$ commutes with $T_1$, preserves $E_1^-$.
- **Position 15** (leftmost $S_6$ of $\Rp_7$): $\Omega^{[\widehat{\{15\}}]} = (\Rp_6)^2 = S_5 \cdot \Rp_5 \Rp_6$ by associativity (using $\Rp_6 = S_5 \Rp_5$). Same branching argument; $S_5$ commutes with $T_1$.

The other 9 positions I verified computationally only.

## Why the other 9 positions don't yield to the same argument

The "naive" extension would use the Coxeter braid $S_i S_{i+1} S_i = S_{i+1} S_i S_{i+1}$, but this is **false** for $S_i = T_i + 1$:

$$S_i S_{i+1} S_i - S_{i+1} S_i S_{i+1} = q\,(T_i - T_{i+1}).$$

For positions deeper in $\Rp_6$ or $\Rp_7$, the factor-removed chain entangles $S_5$ (or $S_6$) with lower letters, and pulling apart requires the braid. The $q(T_i - T_{i+1})$ correction breaks the clean "outer $\subseteq E_1^-$" form.

## Methodological point

The two "easy" positions (10 and 15) are exactly the **leftmost factors** of the two tail blocks $\Rp_6$ and $\Rp_7$. Removing the leftmost factor of $\Rp_k$ yields $\Rp_{k-1}$, which combines cleanly with $\Rp_n$. This is the structural reason these two positions are special.

## Status / call-out

This is *real* progress on per-subset Pillar~1:

1. **The reduction is clean and complete.** Per-subset Pillar~1 at $|S_T| = 1$ is now equivalent to Strong Pillar~1 at $|U| = 1$, which is a single uniform statement instead of one statement per subset.

2. **Two positions structurally closed.** The branching method works cleanly here.

3. **Nine positions empirically verified but structurally open.** I would like your eye on whether there's a unified structural argument I'm missing — possibly via integrating the $q(T_i - T_{i+1})$ braid defect, or via a different decomposition of the tail.

4. **The 3 outliers at $|S_T| = \tau$** still need the inductive $\Om_{S_\ell}$-kernel argument (the residual gap from the morning paper).

If you have time, push to GitHub on request.
