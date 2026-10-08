# Note for Robin — 6 May 2026 (evening prove session)

## TL;DR

I returned to the cross-trace mystery from this afternoon (`2026-05-06-paths-explicit-and-Q3-refuted.tex`, Theorem 4–5) and proved the structural reason for **three of the four** off-diagonal cross-trace vanishings in the $S_5$-block decomposition of $\sigma_1(V_{(3,2,1)})$. The fourth and the surprising identity remain open, but the fourth is now reduced to a clean three-term polynomial identity over $W$-graph data.

## Result

**Cell-ideal triangularity.** In the KL basis of $V_{(3,2,1)}$ at $S_6$, every off-block entry of $M_1, M_2, M_3, M_4$ (the $S_5$-Hecke off-diagonal operators) goes "down in dominance": output branching cell $\trianglelefteq$ input branching cell. Verified directly on all 9 off-block entries (out of 46 total) of $M_1\ldots M_4$ on $V_{(3,2,1)}$.

**Corollary.** $\Pi_q^{S_5}$ is block lower-triangular wrt the dominance ordering of branching cells. Three of the four off-diagonal cross-traces vanish immediately:
- $\mathrm{cross}_{(3,2)\to(3,1,1)} = 0$
- $\mathrm{cross}_{(3,2)\to(2,2,1)} = 0$
- $\mathrm{cross}_{(3,1,1)\to(2,2,1)} = 0$

These are the three pairs $(\mu_i, \mu_j)$ with $\mu_i \triangleright \mu_j$ (output strictly dominates input).

## What's left over

**Open:** the fourth vanishing $\mathrm{cross}_{(2,2,1)\to(3,1,1)} = 0$ is **NOT** forced by cell-ideal triangularity. Cell-ideal allows this entry. But empirically the trace pairing with $R_5$ kills it.

I reduced the fourth vanishing to a three-term identity:
$$\sum_{p=1}^{3}(R_5'\,\Pi_q^{S_5})_{m_p, j_p} = 0$$
where $(j_p, m_p) \in \{(6,7), (12,13), (14,15)\}$ are the three $s_5$-edges of $M_5$ that connect $V_{(3,1,1)}^{\text{desc}}$ to $V_{(2,2,1)}$. This is a "summed-diagonal" of $R_5'\Pi_q^{S_5}$ over a $W$-graph-natural 3-pair sub-block. The conjecture is empirically true (verified by independent Lagrange interpolation) but I have no structural proof.

## Bonus observation: $M_5$ has the OPPOSITE triangularity

While $M_1\ldots M_4$ go "down in dominance," $M_5$ goes **up**: every off-block entry has output dominance $\trianglerighteq$ input dominance. I prove this is forced by the rigid box-6-row structure of the self-conjugate shape $(3,2,1)$:
- $V_{(3,2)}$ is the "$s_5$-descent block" (box 6 in row 2, box 5 always above).
- $V_{(2,2,1)}$ is the "$s_5$-ascent block" (box 6 in row 0, box 5 always below).
- $V_{(3,1,1)}$ is the only block with mixed $s_5$-status.
- $M_5$-edges go from ascents (input) to descents (output), so off-block they always raise dominance.

This is special to $(3,2,1)$ — for general $\lambda$, the box-$n$ row doesn't induce a total order on branching cells matching dominance.

## Files

- LaTeX writeup: `~/projects/proofs/2026-05-06-cell-ideal-cross-trace.tex` (7 pages, compiles).
- Builds on data from `~/projects/scratch/2026-05-06-paths/`.

## Honest assessment

**Achieved:** structural explanation for three of four cross-trace vanishings; reduction of the fourth to a clean three-term identity; structural account of why $M_5$ has opposite triangularity.

**Not achieved:** structural proof of the three-term identity (Conjecture 4.3). Structural proof of the surprising identity $D(q) = \mathrm{cross}_{(3,1,1)\to(3,2)}(q)$ — also still open.

This is incremental progress. The afternoon writeup observed five facts; this morning we now have a structural explanation for three of them. The remaining two open questions are both about the **same** missing structure: why does the $V_{(2,2,1)} \to V_{(3,1,1)}$ block "cancel out" but the $V_{(3,1,1)} \to V_{(3,2)}$ block exactly equal $D(q)$? I believe both are governed by some Mullineux-style symmetry of $(3,2,1)$ that I haven't pinned down.

## Blockers (unchanged)

- Read-only PAT after Oracle migration. Cannot push to GitHub. PDF is local only.

## What might come next

- The two open identities ($\mathrm{cross}_{(2,2,1)\to(3,1,1)} = 0$ and $D = \mathrm{cross}_{(3,1,1)\to(3,2)}$) might be proved together by an explicit $S_5$-equivariant change of basis (KL → seminormal). Both would become: "in seminormal basis, certain matrix entries vanish." The challenge is the basis-change is over $\mathbb{Q}(q)$ and computationally intensive.
- The cell-ideal triangularity I used is a special case of a general property of cellular bases under restriction. Worth writing up for arbitrary $\lambda$ — it would justify the present approach more broadly.

— Clio
