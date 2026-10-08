# For Robin — Converse trace-vanishing direction, prove session 2026-05-17

**TL;DR:** Per-SYT positivity is now PROVED (was conjectured yesterday). The converse trace-vanishing direction now follows modulo a column-descent-free SYT existence lemma, which is verified exhaustively for all $|\lambda| \le 14$ (210 shapes, no exceptions).

## What was open this morning

After yesterday's forward direction (commit `92a5323`), the converse direction was:
- For $\hat\lambda$ rows $\ge 2$, $\tau(\hat\lambda) = 0$, $\lambda = (\hat\lambda, 1^q)$: prove $\mathrm{tr}_{V^\lambda}(\Omega^{(\lambda)}) \ne 0$.

Per-SYT positivity (each diagonal $p_T \in \mathbb{Q}_{\ge 0}(q)$) was an empirical observation across 7 shapes, no proof.

## What's new

### Lemma 1 (Hoefsmit positivity) — PROVED

In the asymmetric $b'=1$ Hoefsmit seminormal basis, EVERY matrix entry of $T_i + 1$ is in $\mathbb{Q}_{\ge 0}(q)$:

- Diagonal: $0$ (if $d=-1$), $q+1$ (if $d=1$), or $[d+1]_q/[d]_q$ (if $|d| \ge 2$).
- Off-diagonal: $1$ (the $b'=1$ side) and $q\,[d-1]_q[d+1]_q/[d]_q^2$ (the other side).

For $d > 0$ both ratios are explicit polynomials in $q$ with non-negative coefficients divided by polynomials with non-negative coefficients. For $d < 0$, the substitution $[-k]_q = -q^{-k}[k]_q$ converts everything to the same form. Verified symbolically for $|d| \le 6$.

### Per-SYT positivity — IMMEDIATE COROLLARY

Matrix products preserve "all entries in $\mathbb{Q}_{\ge 0}(q)$". Apply to $\Omega^{(\lambda)} = \prod_k \prod_j (T_j+1)$. Hence every diagonal $p_T(q) \in \mathbb{Q}_{\ge 0}(q)$.

### Converse direction — PROVED MODULO EXISTENCE

Trace vanishes iff every $p_T$ vanishes (Corollary). To show trace nonzero, exhibit one $T^*$ with $p_{T^*} \ne 0$.

For any $T^*$ with **no column-descents** (i.e., no consecutive integers $j, j+1$ in the same column of $T^*$), the "stay walk" gives $p_{T^*} \ge \prod_j [T_j+1]_{T^*,T^*}^{e_j} > 0$ in $\mathbb{Q}_{\ge 0}(q)$.

**Existence conjecture (Conjecture):** Every $\tau = 0$ shape $\lambda = (\hat\lambda, 1^q)$ with $q \ge 1$, $\hat\lambda$ rows $\ge 2$, admits a descent-0-at-1 SYT with no column-descents.

**Verified:** 210 shapes, $|\lambda| \le 14$, no exceptions (brute force).

**Explicit constructions:**
- $q = 1$: $T_{rs}$ (row-superstandard) works — its only potential descents are within the tail, which has $q-1 = 0$ pairs.
- $q \ge 2$: interleaved construction (alternate tail cells with col-3+ cells in a specific order) works for most shapes.
- Remaining cases (specifically $\hat\lambda$ with multiple consecutive length-3 rows): brute-force confirms existence; explicit construction left open.

## Paper

`~/projects/proofs/2026-05-17-converse-per-syt-positivity.tex`, commit `3282849` on `clio-vega/proofs`. URL: <https://github.com/clio-vega/proofs/blob/main/2026-05-17-converse-per-syt-positivity.tex>

7 pages, builds clean.

## Status of the conjecture

This is the cleanest the converse direction can get without further combinatorial work. The "existence of $T^*$" gap should be closeable by a routine cascade-swap argument on $T_{rs}$, but I haven't pinned down a single uniform construction. The empirical verification at $|\lambda| \le 14$ is strong evidence, and the local structure (only the boundary between $\hat\lambda$ and tail in column 1 is problematic, and there are always enough "buffer" cells in cols $\ge 2$ of $\hat\lambda$ — at $\tau = 0$ we have $|\hat\lambda| \ge q + 2L - 1$, giving $|\hat\lambda| - L \ge q - 1$ buffer cells, exactly the count needed for $q-1$ cascade swaps) suggests this is a routine verification.

If you want to close the existence lemma, the cleanest approach is probably:
1. Define $T^*$ as $T_{rs}$ with a cascade of value-swaps.
2. Show the cascade terminates (uses buffer cells in cols $\ge 3$ of $\hat\lambda$, which exist when $\hat\lambda$ has a row of length $\ge 3$).
3. For shapes with all $\hat\lambda$-rows of length 2 (i.e., $\hat\lambda = (2^L)$), $\tau = 0$ only at $q \le 1$, handled by Regime A.

## Methodological note

The proof was surprisingly clean once Lemma 1 was stated correctly. The empirical conjecture (each $p_T \in \mathbb{Q}_{\ge 0}(q)$, with denominators like $(q^2+q+1)$ etc.) tracked back directly to the asymmetric Hoefsmit form's individual matrix entries. The choice of basis matters: in the symmetric/orthogonal Hoefsmit basis, off-diagonal entries have $\sqrt{\cdot}$ terms and positivity is murkier. The $b' = 1$ asymmetric form makes positivity transparent.

[[hoefsmit-positivity]] [[two-sided-sign-kill]] [[trace-vanishing-conjecture]] [[per-syt-positivity-refined]]
