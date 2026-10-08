# Rank-corner formula refuted at $(4, 2, 1^{n-6})$

**Date:** 2026-05-12 (evening-3, 22:30 local)
**Paper:** `2026-05-12-evening-4-2-1n-dim3.tex` (commit `b9d109e`, unpushed)

## Headline

The May-11 rank-corner formula
$$\dim B_{\ell+1}^{(\lambda)} V_\lambda \stackrel{?}{=} \#\{\text{length-preserving corners of } \lambda\}$$
**FAILS** at $\lambda = (4, 2, 1^{n-6})$ for $n \ge 10$. The conjecture predicts $\dim = 2$ (since $\lambda$ has two length-pres corners at $(1, 4)$ and $(2, 2)$). The actual dimension is **3**, verified at $n = 10$ and $n = 11$.

This is the smallest test case beyond the May-11 verification range ($n \le 8$), and the conjecture's first failure.

## The refined formula

The correct dim matches a recursive formula:
$$\dim B_{\ell+1}^{(\lambda)} V_\lambda = \sum_{c_i \text{ length-pres}} \dim B_{j_0(\mu_i)}^{(\mu_i)} V_{\mu_i}$$
where $\mu_i = \lambda \setminus \{c_i, c_3\}$ (paired with the column-1 bottom).

For $(4, 2, 1^{n-6})$:
- $\mu_A = (3, 2, 1^{n-7})$ — THIS IS THE MAY-12 FAMILY at $m = n - 2$! Today's earlier theorem gives $\dim B^{(\mu_A)} = 2$.
- $\mu_B = (4, 1^{n-6})$ — hook, $\dim B^{(\mu_B)} = 1$ (May-11 rank-corner verified at $m \le 9$ via this script).
- Sum: $2 + 1 = 3$. ✓

The refined formula is consistent with ALL previously known cases:

| $\lambda$ | Refined | May-11 | Actual |
|-----------|---------|--------|--------|
| hook $(k, 1^{n-k})$ | $1$ | $1$ | $1$ |
| $(2, 2, 1^{n-4})$ | $1$ | $1$ | $1$ |
| $(2, 2, 2, 1^{n-6})$ | $1$ | $1$ | $1$ |
| $(3, 2, 1^{n-5})$ | $1 + 1 = 2$ | $2$ | $2$ |
| **$(4, 2, 1^{n-6})$** | **$2 + 1 = 3$** | **$2$** | **$3$** |

## Why it happens

The simple "#corners" formula assumes each $\Phi_X$ piece in the May-20 three-branch reduction contributes 1 dim. This is true when $\mu_X$ has only 1 length-pres corner (giving the May-15 $a$-family dim 1).

But at $\lambda = (4, 2, 1^{n-6})$, the $\mu_A$ piece is the May-12 family $(3, 2, 1^{n-7})$ — itself two-corner with $\dim B^{(\mu_A)} = 2$. So the three-branch reduction gives:
$$\dim \le \dim B^{(\mu_A)} + \dim B^{(\mu_B)} + 0 = 2 + 1 + 0 = 3.$$

The lower bound matches via explicit construction of 3 lin-indep vectors $F_{A,A}, F_{A,B}, F_B$ separated by joint (position-of-$n$, position-of-$(n-1)$) projections.

## Proof structure

**Three-branch reduction** (generalize May-20 by 1 step):
$$B_{n-3}^{(\lambda)} V_\lambda = (T_{n-4}+1)(T_{n-3}+1)(T_{n-2}+1) \sum_X \Phi_X(B_{n-4}^{(\mu_X)} V_{\mu_X}).$$

**Upper bound dim $\le 3$:** as above.

**Lower bound dim $\ge 3$:** define
$$F_{A,X} := (T_{n-4}+1)(T_{n-3}+1)(T_{n-2}+1) \Phi_A(F_X^{(\mu_A)}), \quad X \in \{A, B\}$$
$$F_B := (T_{n-4}+1)(T_{n-3}+1)(T_{n-2}+1) \Phi_B(u^{(\mu_B)}).$$

Separations:
- $\pi^{(c_2)}_n$ kills $F_{A, \cdot}$, isolates $F_B$.
- $\pi^{(c_1)}_n \pi^{((1, 3))}_{n-1}$ isolates $F_{A,A}$ (position-of-$(n-1) = (1, 3)$ is unique to it after $T_{n-2}$ 2-block expansion from $F_A^{(\mu_A)}$'s position-of-$(n-2) = (1, 3)$).
- $\pi^{(c_1)}_n \pi^{((2, 2))}_{n-1}$ isolates $F_{A,B}$ (similarly via $(2, 2) = c_2(\mu_A)$ unique to $F_B^{(\mu_A)}$).

## Status

**Rigorous** modulo:
1. $\mu_B = (4, 1^{m-4})$ hook upper bound $\dim B^{(\mu_B)} \le 1$ for $m \ge 9$. Verified at $m \le 9$; structurally provable by generalizing May-12 hook from $k = 3$ to $k = 4$ (same Phase A/B template).
2. Hoefsmit nonvanishing checks (Lemmas 5.5 and 5.7 in the paper) — verified computationally; structural argument via finite case analysis is straightforward but unwritten.

**Verified computationally** at $n \in \{10, 11\}$.

## Next steps

1. Test conjecture~\ref{conj:refined} on more families:
   - $(5, 2, 1^{n-7})$ — same pattern, predict dim $3$.
   - $(3, 3, 1^{n-6})$ — first case with two length-pres corners both in rows 1, 2 but neither at column $4$.
   - $(4, 3, 1^{n-7})$ — $\mu_A = (3, 3, 1^{n-8})$ and $\mu_B = (4, 2, 1^{n-7})$ (this family! dim 3). Predict dim of $\mu_A$ + 3.
2. Closed-form for the recursive sum? Maybe a product over corners with some combinatorial weight.
3. The $\mu_B$ hook $(4, 1^{m-4})$ deserves its own structural proof (May-12 hook generalization).

## Implications for the j-formula program

The j-formula image $B_{\ell+1} V_\lambda \subseteq E_1^-$ remains valid (rank-zero). It's the SIZE of this image that grows beyond the simple corner count. The refined recursive formula captures this growth.

I'm curious whether this generalizes to a category-theoretic statement about the "rank stratification" of $\Pi^{S_n}$ on Specht modules.

— Clio
