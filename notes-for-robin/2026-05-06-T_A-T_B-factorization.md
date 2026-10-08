# T_A and T_B factorize as q² · σ₁ at S_5

**Date:** 2026-05-06 (evening prove session, late)
**Output:** `~/projects/proofs/2026-05-06-D-cross-T-A-factorization.tex` (+ pdf, 4 pages)
**Builds on:** `~/projects/proofs/2026-05-07-trace-identity.tex` (this session's earlier writeup)

## What I found

The May-7 trace-identity writeup reduced the surprising $D(q) = \mathrm{cross}_{(3,1,1)\to(3,2)}(q)$ identity to a residual:

$$
v\,\mathrm{tr}(P_{(3,1,1)}\,\Pi^{S_5}\,P_{(3,2)}\,M_5\,R_5') = (1+q)(T_A + T_B)
$$

with $T_A = q^6(1+q)^2$ and $T_B = q^5\bigl((1+q)^4 + 2q(1+q)^2\bigr)$.

I noticed a clean factorization that the May-7 writeup didn't flag:

- $T_A = q^2 \cdot \sigma_1(V_{(2,2,1)})\big|_{S_5}$
- $T_B = q^2 \cdot \sigma_1(V_{(3,1,1)})\big|_{S_5}$

(Verified by polynomial multiplication: $\sigma_1(V_{(2,2,1)})|_{S_5} = q^4(1+q)^2$, $\sigma_1(V_{(3,1,1)})|_{S_5} = q^3((1+q)^4 + 2q(1+q)^2)$.)

So the May-7 residual rewrites as

$$
v\,\mathrm{tr}(P_{(3,1,1)}\,\Pi^{S_5}\,P_{(3,2)}\,M_5\,R_5') = (1+q)\,q^2\,\bigl[\sigma_1(V_{(2,2,1)})|_{S_5} + \sigma_1(V_{(3,1,1)})|_{S_5}\bigr].
$$

The right-hand side is now wholly intrinsic to the smaller two summands of $V_{(3,2,1)}\downarrow S_5$. The "sink" summand $V_{(3,2)}$ is conspicuously absent.

## Why I think this is the right view

1. The factorization is too clean to be coincidence — both summands have the same $q^2$ multiplier, both involve standalone $S_5$-cell $\sigma_1$ values (no mixing).

2. It clarifies the asymmetry "cross-flow goes only into $V_{(3,2)}$": the trace identity decomposes $\sigma_1(V_{(3,2,1)})$'s M-step contribution as $(1+q)q^2 \cdot \sigma_1$ of each "source" summand. The "sink" summand $V_{(3,2)}$ is the receiver.

3. The natural conjecture is the **branching factorization** (Conjecture 4.1 in the .tex):
   $$\mathrm{tr}_{V_{(3,2,1)}}\!\bigl(\Pi^{S_5}\, P_\mu^{\mathrm{KL}}\, R_5'\bigr) = q^2\, \sigma_1(V_\mu)\big|_{S_5}$$
   for $\mu \in \{(2,2,1), (3,1,1)\}$.

The conjecture asks: why does $R_5'$ — a 4-letter Bott-Samelson factor that is "redundant" in the reduced-word sense (since $\Pi^{S_5}$ already covers the longest element of $S_5$) — contribute exactly $q^2$ to the trace, when restricted to the source summands?

## What's still open

- A proof of the branching factorization. Two routes mentioned in the writeup:
  - $R_5'$ acts on $V_\mu \subset V_{(3,2,1)}\downarrow S_5$ as $q^2 \cdot I$ + trace-zero correction. (Plausible; requires explicit matrix check.)
  - Functorial branching argument: the redundant factor $R_5'$ contributes a clean $q^2$ multiplier on the source summands, but a more complex cross-flow on the sink $V_{(3,2)}$.

- Whether the same pattern holds for other $\lambda \vdash n$ and other branchings.

## Next steps if I had time

- Compute $R_5'$ explicitly on $V_{(2,2,1)}$ and $V_{(3,1,1)}$ (as $H(S_5)$-modules at $S_5$). Check whether $R_5' = q^2 I$ on each, or $R_5' - q^2 I$ has trace zero against $\Pi^{S_5}$.
- Test the analog for $\lambda = (4,2)$, $(3,3)$ at $S_6 \to S_5$ branching.

## GitHub status

Read-only PAT still blocking pushes. Two unpushed commits from May 6 (twin-multiset, Theorem B multiset). Today's writeups (`2026-05-07-trace-identity.{tex,pdf}`, `2026-05-06-D-cross-T-A-factorization.{tex,pdf}`) ready to add when push works.
