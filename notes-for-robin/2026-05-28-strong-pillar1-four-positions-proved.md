# Strong Pillar 1 — four positions structurally closed

**Date.** 2026-05-28, third prove session (after wake-3 reseed + |S|=0 + per-subset-identity sessions earlier today).
**Paper.** `~/projects/proofs/2026-05-28-strong-pillar1-structural-four-positions.tex` (8 pages, compiles).
**Previous note.** [[2026-05-28-prove-strong-per-subset-progress]] (where I left off after morning sessions).

## What I proved

For $\lambda = (2,2,1,1,1)$ ($\tau = 2$, tail = 11 positions), the factor-removed tail chain $\Omtail^{[\widehat{\{p\}}]}$ acts as the **zero operator** on $V^\lambda$ for $p \in \{12, 13, 16, 17\}$.

These are exactly the four rank-0 positions in the table from this morning's per-subset paper. Combined with the two structurally proven positions (p=10, 15) from the morning paper, this brings us to **6/11 positions with structural proofs**. The 5 remaining are rank-1 (Strong Pillar 1 holds, $\subseteq E_1^-$, but operator is nonzero).

## The mechanism

Two ingredients, each clean in its own right:

**Key identity (K1):** $S_1 S_2 = q I$ on $E_1^+|_{V^\lambda}$ for $\lambda = (2,2,1,1,1)$.

This comes from a single Hoefsmit calculation: vectors in $E_1^+$ have 1, 2 in row 1, hence 3 forced at $(2,1)$, hence axial distance $d=-2$ for the unique non-degenerate 2×2 block at position 2. The on-diagonal piece propagates back to $\Eplus 1$ with coefficient $q/(q+1)$; the off-diagonal piece lands in $\Eminus 1 = \ker S_1$. One line later: $S_1 S_2 e_T = q e_T$.

**Consequence (K2):** $S_1 \Rp_n = q \cdot S_{n-1} \cdots S_3 \cdot S_1$ on $V^\lambda$ for $n \ge 4$. Direct from K1 + the Coxeter commutation that lets $S_1$ slide rightward past $S_3, S_4, \ldots, S_{n-1}$.

**Lemma A** (the critical one for positions 12, 13): $S_1 \Rp_7 \cdot V^\lambda \subseteq \Eminus 3 \cap \Eminus 4|_{V^\lambda}$.

Proof: by K2, the image equals $q \cdot S_6 S_5 S_4 S_3 \cdot E_1^+|_{V^\lambda}$. Now the punchline — $E_1^+|_{V^\lambda}$ is the span of SYTs with 1, 2 in row 1, and these correspond bijectively (via relabeling $i \leftrightarrow i-2$) to SYTs of the sub-shape $\nu = (2,1,1,1)$ for entries 3..7. The action of $S_3, S_4, S_5, S_6$ on $E_1^+|_{V^\lambda}$ matches the action of $\tilde S_1, \tilde S_2, \tilde S_3, \tilde S_4$ on $V^\nu$. So $S_6 S_5 S_4 S_3$ acts as $\tilde \Rp_5$ on $V^\nu$. And $\nu = (2, 1^3)$ is a hook with $\tau(\nu) = 2$: Pillar 1 gives $\tilde \Rp_5 V^\nu \subseteq \tilde E_1^- \cap \tilde E_2^-$, which translates back to $E_3^- \cap E_4^-$ in $V^\lambda$.

**Lemmas B, C** (for positions 16, 17): $(\Rp_5)^2 V^\lambda \subseteq E_6^-$ and $(\Rp_4)^2 V^\lambda \subseteq E_5^-$.

Proof: $S_6$-branching of $V^\lambda$ + iterated $S_5$-branching pin the surviving image of $(\Rp_5)^2$ to the $V^{(2,2,1)}$-summand where 6, 7 are forced into column 1. There $T_6 = -1$, so $S_6 = 0$. Similarly $(\Rp_4)^2$ lives in $V^{(2,2)}$ where 5, 6 are column 1 → $S_5 = 0$.

## How positions 12, 13, 16, 17 close

- **pos 12** = $S_5 S_4 S_2 S_1 \Rp_7$. Apply right-to-left: $S_1 \Rp_7 v \in E_4^-$ by Lemma A; $S_2$ commutes with $T_4$, preserves; $S_4$ kills. Done.
- **pos 13** = $S_5 S_4 S_3 S_1 \Rp_7$. Same, with $S_3$ killing directly via Lemma A's $E_3^-$ containment. Done.
- **pos 16** = $S_5 S_6 (\Rp_5)^2$ by commutation. $(\Rp_5)^2 v \in E_6^-$ by Lemma B; $S_6$ kills. Done.
- **pos 17** = $S_5 S_4 S_6 S_5 (\Rp_4)^2$. $(\Rp_4)^2 v \in E_5^-$; the rightmost-applied $S_5$ kills. Done.

## What I couldn't prove

Strong Pillar 1 at the rank-1 positions $p \in \{11, 14, 18, 19, 20\}$. The empirical fact $S_1 \cdot \Omtail^{[\widehat{\{p\}}]} = 0$ holds at all 11 positions (uniformly, by exact-rational check), but my structural toolkit doesn't directly close the rank-1 cases. They don't admit a clean $(\Rp_k)^2$ factorization or the Lemma A inner-$S_1$ collapse, because the chain factor structure is "off" in different ways:

- pos 14 drops the inner $S_1$ from $\Rp_6$, so the operator's $\Rp_7$ tail still ends in $S_1$ but Lemma A's collapse can't propagate through $S_5 S_4 S_3 S_2$ (the second $S_2$ breaks commutation).
- pos 20 drops the $S_1$ from $\Rp_7$, so K2's $S_1 \Rp_7$ collapse is not even available.
- pos 11, 18, 19 are similarly stuck.

The empirical $S_1$-kill across all 11 positions is so clean it must have a uniform reason — probably some "Pillar 1 derivative" identity that captures how the chain responds to letter removal. I haven't found it yet.

## What I'd like your eye on

- Is the "row-1-pair embedding" trick (Lemma A's reduction to Pillar 1 on a sub-shape) something you've seen before? It feels like a natural duality, but I haven't seen it stated as such.
- The 5 open rank-1 positions: any intuition for a uniform mechanism? The linear-combination identity from the morning paper reduces per-subset Pillar 1 to "Strong Pillar 1" at uniform level, so the 5 open positions are the last gap before the 229/232 structural closure.

I'll push the paper to GitHub on request.
