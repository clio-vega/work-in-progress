# For Robin — 2026-05-19 prove session

## The result

**SC-at-1 trivial reduction of converse Diagnostic 4.**
For $T \in \mathrm{SYT}(\lambda)$ with $\lambda = (\hat\lambda, 1^q)$,
$\tau(\hat\lambda) = 0$, and $T$ having $2$ in cell $(2,1)$ (an SC pair at
index 1):

$$T_1 v_T = -v_T \implies S_1 v_T = (T_1+1) v_T = 0 \implies R'_n v_T = 0
\implies \Omega v_T = 0 \implies p_T(q) = 0.$$

One-line proof. The right end of $R'_n = S_{n-1} \cdots S_2 S_1$ is $S_1$,
and SC at 1 puts $v_T$ in the $T_1 = -1$ eigenspace.

## Why this matters

Combined with yesterday's universal SC necessity, this closes the
converse for **378 of 514 zero diagonals** (≈ 73.5 %) across the 12-shape
corpus. The fact that the cleanest known reduction is a 5-line algebraic
calculation is consistent with [[try-simple-arguments-first]] —
yesterday's positivity argument and today's pointer argument are
strictly smaller than the Markov / categorical machinery I was eyeing
last week.

The paper is at `~/projects/proofs/2026-05-19-sc-at-1-trivial-reduction.tex`
(commit `faa9f13` in `clio-vega/proofs`).

## What remains open

The full converse now reduces to the **SR-at-1 stratum** (2 in cell
$(1,2)$): 136 of 514 zero diagonals. Stratification trace results:

- **Right-collapse normal form:** for every SR-at-1 zero diagonal with
  finite $k_R$, the collapse step is $(k_R, 1)$ — the partial product
  $R'_{k_R+1} \cdots R'_n v_T$ already lies in $\ker S_1$ = SC-at-1
  eigenspace. So the chain *steers $v_T$ into the trivially-killed
  subspace.* Why? Open.

- **Left-collapse normal form:** every $\Omega^*$ collapse is at
  $(k_L, k_L-1)$ — the rightmost factor $S_{k_L-1}$ of $L_{k_L}$
  vanishes the running vector. Equivalently
  $L_{k_L-1} \cdots L_{\ell+1} v_T \in \ker S_{k_L-1}$.

- **$\Omega$-survivors:** 12 of 136 have $\Omega v_T \ne 0$. **All 12
  have one of two specific tableau patterns:**
  - $1, 2, 3$ all in row 1 of $T$ (11 cases)
  - $1, 2$ in row 1 and $3, 4$ in cells $(2,1), (2,2)$ of row 2 (1 case)

Conjecture: these are exactly the cases where $\Omega^*$ takes over.

- $k_R[0]$ is **not** $\max\{j : T \text{ has SC at } j\}$ (tried), and
  not $\min \mathrm{SC}$ either. Some deeper invariant.

## What I tried but couldn't close

- Predict $(k_R, k_L)$ from a single combinatorial invariant of $T$.
  Distributions show $k_R - \max\mathrm{SC} \in \{-1, 0, 1, 2, 3, 4, 5\}$.
  Multiple invariants would be needed.
- Extend the trivial argument to SC-at-$j$ for $j \ge 2$. **Doesn't
  work:** the would-be configuration "$1, \ldots, j$ in row 1 and $j+1$
  in $(2, j)$" is impossible in any SYT for $j \ge 2$ (row-2-must-be-increasing
  contradicts $(2, j-1) < (2, j) = j+1$ when $(2, j-1)$ must be $> j+1$).

## Memory pointers I added

- [[sc-at-1-trivial-reduction]] (today's main result)
- [[stratification-normal-forms]] ($k_R[1]=1$ and $k_L = (k, k-1)$)
- [[omega-survivor-pattern]] (12-case structural feature)

## Email status

Still need `/mcp` re-auth for Gmail (now 4 wake sessions). When you have
a moment.
