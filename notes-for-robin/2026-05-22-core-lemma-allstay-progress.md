# For Robin — 2026-05-22: Core Lemma progress (all-stay lower bound proved)

**TL;DR.** The one open gap in the reciprocity/min-degree paper is the *Core Lemma
lower bound* (a min-cost closed walk on SYT(λ) costs ≥ n(λ)). I proved the **all-stay
case** unconditionally and isolated exactly why the general case is hard.

**Pushed:** `2026-05-22-core-lemma-allstay-lower-bound.tex` (clio-vega/proofs, commit
`e1b2f4c`, 7pp). →
https://github.com/clio-vega/proofs/blob/main/2026-05-22-core-lemma-allstay-lower-bound.tex

**What's new:**
1. **Lemma 3.1 (proved):** $D(T)=\sum_i(n-i)\delta_T(i)\ge n(\lambda)$ for every
   tableau, equality at $T_{rs}$. Clean argument: $D(T)=\sum_v\mathrm{des}_{<v}(T)$,
   and value $v$ at row $\rho$ has $\rho$ column-rungs above it forcing $\rho$
   **disjoint** content-descents below $v$, so $\mathrm{des}_{<v}\ge\rho_T(v)$; sum
   $=n(\lambda)$. This closes all *all-stay* walks.
2. **Correction to my own paper:** the §7 "same-column charge" sketch was wrong. The
   cost-1 steps land $i,i{+}1$ on *anti-diagonals*, never the same column. The
   column-rung charge above is the right version.
3. **Obstruction pinned down:** a closed walk's swaps compose to the identity, so every
   cost-0 *sorting* swap must be undone by a cost-1 *de-sorting* swap. The naive
   remaining-cost potential over-credits sorting swaps and fails on exactly those
   edges. The full proof must use the closed-walk identity constraint — three routes
   sketched in §5 / next PROVE.md (amortized potential, wiring-diagram/0-Hecke,
   de-swap straightening).

**Status of the chapter:** reciprocity PROVED; min-degree REDUCED + all-stay case
PROVED + LP-certified for all feasible λ⊢n≤7. Full lower bound is the next prove target.

**Ops nag (≈8 sessions now):** Gmail MCP still needs `/mcp` re-auth — I can't read or
send mail until you run it. SageMath still not installed (I'm on sympy/numpy/scipy).
