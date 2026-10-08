# For Robin — 2026-05-06 evening: Conjecture A via lift coefficients

## What I did this session

The PROVE.md target was the path-level Theorem~B, which was already proved earlier today (multiple files). So I redirected to two open conjectures from the day's work:

1. **Conjecture~A** (from `2026-05-06-cell-ideal-cross-trace.tex`): the three-term cancellation $\sum_p (R_5'\Pi_q^{S_5})_{m_p, j_p} = 0$ for the three $M_5$-pair entries.
2. **Surprise identity** (from `2026-05-06-paths-explicit-and-Q3-refuted.tex`): $D(q) = \mathrm{cross}_{(3,1,1)\to(3,2)}(q)$.

I attacked Conjecture~A using a different angle than the column-vanishing proof you (or the earlier prove session) wrote up in `2026-05-07-fourth-cross-trace-vanishing.tex` (created at 17:20 today): the **lift-coefficient framework**.

## What's new

Two structural results that I haven't seen elsewhere in the May 6 file family:

1. **Diagonal of the rep-projector = SET indicator.** $(E_\mu^{\mathrm{rep}})_{w,w} = \chi_{V_\mu^{\mathrm{set}}}(w)$ in the KL basis. This is a clean direct-sum-meets-cellular-triangularity fact.

2. **The lift matrix $Y$ for $V_{(3,1,1)}^{\mathrm{rep}} \subset V_2$ has a closed form**: exactly seven nonzero entries, each equal to $1/(1+q)$. The seven nonzero positions are at the four $M_i$-edges (forced by the $v$-degree equation) plus three "matching $D_L^{S_5}$" pairs (forced by the $v^2$-degree consistency).

Both follow from a clean two-equation system derived from $S_5$-equivariance of the lift $\widetilde C_j = C_j + v\sum_m Y[m,j] C_m$.

## Honest comparison with the May 7 column-vanishing proof

- The May 7 proof is **strictly stronger**: it proves $\Pi_q^{S_5} C_j = 0$ for all $j \in \{6, 12, 14\}$, which implies entry-by-entry vanishing of $R_5'\Pi_q^{S_5}$ in column $j$ (so all 5 entries of column 6 vanish, not just the one we cared about).
- My proof verifies the three specific entries $(R_5'\Pi_q^{S_5})[m_p, j_p] = 0$ via direct matrix product, after using the lift framework to determine $Y$.
- Both close Conjecture~A. The May 7 proof has more explanatory power for "why these specific entries"; my proof has more explanatory power for "what is $Y$".

## Where the lift framework might still earn its keep

The surprise identity $D = \mathrm{cross}_{(3,1,1)\to(3,2)}$ is still open. Both sides involve traces of operators times projectors. The lift framework reduces the partial traces to specific finite linear-algebra in $Y$, $X$, $X'$ (lift matrices for the other branching summands too). I haven't pushed it through but the setup is in place.

## Output

- `/home/clio/projects/proofs/2026-05-06-conjecture-A-proven.tex` (and `.pdf`, 7 pages).
- Computation: `/home/clio/projects/scratch/2026-05-06-Y-lift/compute_Y.py`.

**Push blocked**: read-only PAT (you knew). All today's commits remain local.

## Mistake I made and corrected mid-session

My first pass had a "Lemma 4.2" claiming $(R_5'\Pi_q^{S_5})[m,j] = (Y \pi^{(3,1,1)} - \pi^{(2,2,1)} Y)[m,j]$ — an off-block-as-commutator formula. This is wrong: the $S_5$-equivariance constraint actually gives **two** independent equations (one from $v^1$-coefficient, one from $v^2$-coefficient), not a single commutator. The commutator-style equation only applies to the $v^2$ part (equation~II in the writeup); the $v^1$ part gives the $(1+q)(D_i(j) - D_i(m)) Y[m,j]$ formula.

I caught this when checking the formula against $(M_1)_{11,1} = 1$ (gives 1 on the LHS, 0 on the proposed RHS). Fixed in the final writeup.

## What's still open

- Surprise identity $D = \mathrm{cross}_{(3,1,1)\to(3,2)}$.
- Whether the closed form $Y = 1/(1+q)$ generalizes to $\lambda \neq (3,2,1)$.
- Whether the lift-coefficient framework gives a generalizable proof of Conjecture~A type vanishings beyond the present small example.
