# Ω-trace reciprocity proved; min-degree reduced to one combinatorial lemma

**2026-05-21 prove-session.** Target: reciprocity + minimal degree of
$\chi^\lambda(\Omega)=\mathrm{tr}_{V^\lambda}(\Omega)$ where
$\Omega=\prod_{\mathrm{red}(w_0)}(T_i+1)\in H_n(q)$ (staircase word, length $\binom n2$).

Proof: `~/projects/proofs/2026-05-21-omega-trace-reciprocity-mindegree.tex` (8 pp, compiles clean).

## What's done

**(A) Reciprocity — PROVED, unconditional.**
$\chi^\lambda(\Omega)(q^{-1}) = q^{-\binom n2}\chi^\lambda(\Omega)(q)$ (palindromic, span $\binom n2$). Two ingredients:
1. The KL bar involution $b$ (the $\sigma$-semilinear ring automorphism with $b(T_i)=T_i^{-1}$, $b(q)=q^{-1}$) sends $b(T_i+1)=q^{-1}(T_i+1)$, hence $b(\Omega)=q^{-\binom n2}\Omega$. One line from the quadratic relation.
2. **Bar-self-duality of $V^\lambda$**: $\chi^\lambda(b(h))(q^{-1})=\chi^\lambda(h)(q)$ for all $h$. I prove this directly (not just cite KL): the twisted rep $\tilde\rho=\sigma\circ\rho^\lambda\circ b$ is a genuine $K$-rep; decompose $\tilde\chi=\sum m_\mu\chi^\mu$; specialise at $q=1$ where $b\to\mathrm{id}$ and $\sigma\to\mathrm{id}$, giving $\tilde\chi|_{q=1}=\chi^{S^\lambda}$, so $m_\lambda=1$, rest $0$.

Combine: $P(q)=\chi^\lambda(b(\Omega))(q^{-1})=q^{\binom n2}P(q^{-1})$. Done.

This was the part PROVE.md flagged as "the only real work" — it's closed.

**(B) Minimal degree — REDUCED, plus upper bound.**
- **Reduction (proved, modulo Hoefsmit positivity):** $\min\deg_q\chi^\lambda(\Omega)=\mathsf{mincost}(\lambda)$, the minimum cost of a closed walk on $\mathrm{SYT}(\lambda)$ along the staircase word. The cost rule falls straight out of the $q\to0$ orders of the Mathas/Hoefsmit matrices of $T_i+1$: a step (letter $i$, current tableau $U$) costs **1** iff $U$ has $\mathrm{content}(i{+}1)<\mathrm{content}(i)$ (same-column is forbidden, factor 0); else **0**. Hoefsmit positivity ($T_i+1$ entries in $\mathbb Q_{\ge0}(q)$) guarantees no low-order cancellation, so $\min\deg$ = the min-cost.
- **Upper bound (proved):** for every $\lambda$ with at most one part $=1$ (in particular **all two-row shapes**), the all-stay walk at the row-superstandard tableau $T_{\mathrm{rs}}$ is valid and has cost $\sum_{r}(n-P_r)=\sum_s s\lambda_s=n(\lambda)$ exactly (clean telescoping, $P_r$ = partial sums of $\lambda$). So $\min\deg\le n(\lambda)$ there.

## The one remaining gap

**Core Lemma (lower bound):** $\mathsf{mincost}(\lambda)\ge n(\lambda)$ for all nonzero $\lambda$. Equivalently: every closed staircase-walk has $\ge n(\lambda)$ content-descent steps.

- Verified **exactly** on all **29 non-vanishing shapes with $n\le7$** (mincost $=n(\lambda)=\min\deg$, and $\max\deg=\binom n2-n(\lambda)$), zero exceptions. Reciprocity (A) also re-verified $29/29$.
- Clean reformulations in the writeup: $n(\lambda)=\sum_j\binom{\lambda'_j}{2}$ (per column). Two-row → a **ballot (U/D) walk** (cost-1 = a $UD$ adjacency at prefix-excess $\ge2$; height-1 peaks forbidden); hooks → a **leg model** with "lift-and-restore" swaps giving $\binom{m+1}2$.
- The natural proof is a **charge/injection**: assign each same-column cell-pair a distinct cost-1 step (a column of length $c$ forces $\ge\binom c2$ descents). I could not make the injection rigorous in general, nor find a closed-form shortest-path potential. **This is where I'd want your eyes.** The obstruction to a clean induction: pinning value $n$ (it's forced to stay) leaves the values-$<n$ walk running a *non-reduced* word (staircase$(n-1)$ + an extra descending run), so the induction hypothesis doesn't apply directly.

## Files
- Proof: `~/projects/proofs/2026-05-21-omega-trace-reciprocity-mindegree.tex`
- DP + verification: `~/projects/scratch/walklib.py`, `verify_all.py`, `mindeg_dp.py`
- (Not yet pushed to GitHub — flag me if you want it up.)
