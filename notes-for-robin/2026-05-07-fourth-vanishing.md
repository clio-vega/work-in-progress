# For Robin — 2026-05-07: fourth cross-trace vanishing

## What's done

Proved the fourth (and last) off-diagonal cross-trace vanishing in the $S_5$-block decomposition of $\sigma_1(V_{(3,2,1)})$:
$$\mathrm{cross}_{(2,2,1)\to(3,1,1)}(q) = 0.$$

This was Conjecture 4.3 from the May 6 cell-ideal-cross-trace.tex (the empirical fourth zero whose three-term reduction had been left open).

## What I found

The vanishing is much stronger than a three-term cancellation: **column $j$ of $\Pi_q^{S_5}$ on $V_{(3,2,1)}$ is identically zero for every $j \in V_{(3,1,1)}^{\text{desc}} = \{6, 12, 14\}$**. For $j = 12, 14$ this is trivial ($1 \in D_L(j)$ kills via the rightmost $T_1+1$). For $j = 6$ ($1 \notin D_L$) it is genuine — I trace 5 explicit steps of the $W$-graph evolution to show $(T_1+1)(T_4+1)(T_3+1)(T_2+1)(T_1+1)C_6 = 0$, with the surviving span concentrating in the 1-descent subspace after step 3 and being killed by the next $T_1+1$ at step 5.

There was also a quiet gap in the May 6 Lemma 4.2 proof: the inner-index sum was conflated with a full matrix product. With the column-vanishing theorem this evaporates.

## Output

- `/home/clio/projects/proofs/2026-05-07-fourth-cross-trace-vanishing.tex` (and `.pdf`, 7 pages)

**Push blocked**: GitHub PAT remains read-only after Oracle Cloud migration. The two May 6 commits and today's are still local. I emailed you about this on May 6.

## Honest limits

- I tried a clean structural conjecture (consecutive descent $\Rightarrow$ kernel). **Refuted by counter-example** in our own data: SYT [1] of $V_{(3,2,1)}$ has $D_L = \{3, 4\}$ but column 1 is nonzero. So the simple "two consecutive descents kill" pattern doesn't generalize beyond $\{2, 3\}$.
- The right structural characterization for "which $C_T$ are killed by $\Pi_q^{S_n}$" is open. The data shows the answer involves the temporal evolution under the staircase, not just a static $D_L$ condition.
- The surprising identity $D(q) = \mathrm{cross}_{(3,1,1)\to(3,2)}(q)$ from May 6 remains open — needs a different angle.

## Status of the cross-trace decomposition story

All four off-diagonal vanishings in the $S_5$-block decomposition of $\sigma_1(V_{(3,2,1)})$ are now proved:
- Three by cell-ideal triangularity (May 6).
- The fourth by the column-vanishing theorem (today).

So the cross-trace decomposition $\sigma_1(V_{(3,2,1)}) = \sum_{(\mu_i, \mu_j)} \mathrm{cross}_{\mu_i \to \mu_j}$ is fully understood at the level of WHICH cross-traces vanish. Five are nonzero, four are zero, and we now have structural reasons for each.
