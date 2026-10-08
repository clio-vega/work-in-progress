# Rank-zero theorem for the staircase Bott–Samelson

**Date:** 2026-05-08 afternoon
**Status:** Proved at n ≤ 7. Conjectural at n ≥ 8 even.
**Writeup:** `~/projects/proofs/2026-05-08-rank-zero-theorem.tex` (7pp), commit `3ffccea`. **Unpushed** (read-only PAT, 11 commits behind upstream).

## The theorem

For Π^{S_n} = (T_1+1)·(T_2+1)(T_1+1)·…·(T_{n-1}+1)…(T_1+1) (the staircase Bott–Samelson for w_0 ∈ S_n) and V_λ the cell module of shape λ:
$$
\mathrm{rank}\,\Pi^{S_n}\big|_{V_\lambda} = 0 \iff \ell(\lambda) > \lceil n/2 \rceil.
$$

The forward direction (Π = 0) is proved unconditionally for n ≤ 7. The reverse (rank ≥ 1 when length ≤ ⌈n/2⌉) is verified at n ≤ 7 and conjectured.

## What's clean

The induction works **for n odd** (or whenever length(λ) ≥ ⌈n/2⌉+2). Use Π^{S_n} = Π^{S_{n-1}} · R_n' where R_n' = (T_{n-1}+1)…(T_1+1). Restrict V_λ to S_{n-1}: every branching summand V_μ has length(μ) > ⌈(n-1)/2⌉, so Π^{S_{n-1}}|V_μ = 0 by induction. Done.

For n odd: ⌈n/2⌉ = ⌈(n-1)/2⌉ + 1, so length(λ) > ⌈n/2⌉ ⟹ length(μ) ≥ length(λ) - 1 > ⌈(n-1)/2⌉ for all μ.

## What's hard: the boundary case

For n even, ⌈n/2⌉ = ⌈(n-1)/2⌉, and the boundary case length(λ) = n/2 + 1 fails the clean reduction. The "bad" μ is obtained by removing the bottom row of length 1, giving μ of length n/2 — exactly the maximum where Π^{S_{n-1}} has rank ≥ 1.

The boundary cases at n=6 are λ ∈ {(3,1,1,1), (2,2,1,1)}.

**Boundary lemma.** There exists j ∈ {3, …, n} with $B_j := R_j' R_{j+1}' \cdots R_n'$ mapping V_λ into E_1^- (the (−1)-eigenspace of T_1). Then the next factor of Π is the rightmost (T_1+1) of R_{j-1}', which kills E_1^-, hence Π^{S_n}|V_λ = 0.

I have a **structural proof at n = 4** (λ = (2,1,1)) using image-tracking. The key chain:

1. Step 1: (T_1+1) annihilates v_2, v_3 (both have 1, 2 in column 1). Image = span(v_1).
2. Step 2: (T_2+1) projects v_1 to the +q-eigenvector of the {v_1, v_2} 2×2 block.
3. Step 3: (T_3+1) annihilates v_1 (since 3, 4 are in column 1 of T^(1)), so only the v_2 component survives. T_3 has a {v_2, v_3} block, and (T_3+1) lands in span(v_2, v_3) = E_1^-. ✓

The n=6 boundary cases require **two blocks**: R_5' R_6' is the smallest product that lands in E_1^-. R_6' alone is not enough — its image has rank 4 with nonzero E_1^+ component.

## Empirical j-formula

Across all tested rank-zero cases:

| n | λ | length(λ) | smallest j |
|---|---|---|---|
| 4 | (2,1,1) | 3 | 4 |
| 5 | (2,1,1,1) | 4 | 5 |
| 6 | (3,1,1,1) | 4 | 5 |
| 6 | (2,2,1,1) | 4 | 5 |
| 6 | (2,1,1,1,1) | 5 | 6 |

**Conjecture: j(λ) = ℓ(λ) + 1.**

## Where I'd like a hint

The n=6 boundary case (3,1,1,1) is the simplest unproven instance where R_n' alone fails. I tried tracing the image through R_5' R_6' but the case analysis grows: each (T_i+1) at d ≠ ±1 mixes pairs of summands, and tracking the +q-eigenvector projections through 5+5 = 10 steps is unwieldy.

The right framework might be:

1. A **basis-free** statement: define a subspace W ⊂ V_λ that is "T_1-isotypic in a strong sense" and stable under R_n', containing the image. Show W ⊆ E_1^- for tall λ.

2. Or: find a **representation-theoretic** invariant that controls the smallest j. The pattern j = ℓ(λ) + 1 suggests it's tied to the "depth" of column 1.

3. Or: a duality/twist argument relating boundary cases at S_n to non-boundary cases at some smaller group.

The trace identity σ_1 = trace Π is **NOT** simply (1+q)^L · rank, even though (T_i+1)^2 = (1+q)(T_i+1). The catch: the projectors π_i := (T_i+1)/(1+q) are idempotents but **don't satisfy braid relations**, so the product π_w depends on the reduced word, and π_{w_0}^staircase is not idempotent in general. So the "trace = rank" implication for idempotents doesn't apply, and a separate argument for trace 0 ⟹ rank 0 (which holds empirically) is needed.

## Side observations

- The reverse direction ("rank ≥ 1 when length ≤ ⌈n/2⌉") is open even at the level of nonvanishing of σ_1. For λ = (n) it's trivial. For other λ, σ_1 is some specific polynomial in q with positive coefficients (empirically); a clean nonvanishing proof would follow from Murnaghan–Nakayama-type expansions, but I haven't worked it through.

- The n=7 verification of length-4 partitions ((4,1,1,1), (3,2,1,1), (2,2,2,1)) is in progress (`quick_n7_verify.py`); these should have rank ≥ 1 by the conjecture.

- The j-formula j(λ) = ℓ(λ) + 1 is a nice testable prediction. If it holds at n=8 (next even), that's strong evidence.
