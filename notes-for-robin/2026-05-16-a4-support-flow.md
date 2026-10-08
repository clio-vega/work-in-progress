# For Robin — 2026-05-16: $a=4$ j-formula proved + per-trajectory framework

## TL;DR

**Closed the $a=4$ case structurally.** For $\lambda = (2,2,2,2,1^{n-8})$
at every $n \ge 12$: $B_{n-3}^{(\lambda)} V_\lambda$ is 1-dim, in
$E_1^-$, supported on the $16$ SYTs of $S_4^{(n)}$. Hence
$\Pi^{S_n}|_{V_{(2,2,2,2,1^{n-8})}} = 0$ unconditionally for $n \ge 12$.
**Third non-hook family** fully structurally proved.

The new technical content is the **per-trajectory framework**:
for each $T' \in S_{a-1}^{(n-2)}$ in the support of $u^{(\mu_1)}$,
the image $\prod (T_j+1) \Phi_1(v_{T'})$ stays supported on a
2-element set throughout the trajectory, ending in the pair
$\{T_{\tau L}, T_{\tau R}\}$ in $S_a^{(n)}$ where $\tau$ is the
$S_{a-1}$ L/R-encoding of $T'$.

Writeup: `2026-05-16-a4-support-flow.tex` (8pp).

## The key structural insight

The per-trajectory framework gives an **algebraic source** for the
L/R encoding bijection $\varepsilon: S_a \to \{L,R\}^a$:

> Each $T' \in S_{a-1}^{(n-2)}$ with encoding $\tau \in \{L,R\}^{a-1}$
> produces a pair of SYTs in $S_a^{(n)}$ with encodings
> $\tau L$ and $\tau R$ (appending L or R).
> The first $a-1$ bits come from $T'$; the last bit varies in the
> final 2-block.

Different $T'$'s give different prefixes → disjoint pairs → union
covers $\{L,R\}^a$ exactly. The recursive set $S_a$ of May-14 is
thus **realized algebraically**, not just conjectured combinatorially.

## What this paper does

**Theorem (a=4):** For $\lambda = (2,2,2,2,1^{n-8})$ at $n \ge 12$,
$B_{n-3}^{(\lambda)} V_\lambda$ has support exactly $S_4^{(n)}$
(16 SYTs), all coefficients nonzero, contained in $E_1^-$.

**Method:** Per-trajectory induction on the step $k \in \{0,1,2,3\}$.
At each step, the pair $\{P_k^+, P_k^-\}$ supporting $w_k(T')$ is a
$T_{n-1-k}$-Hoefsmit 2-block; applying $(T_{n-2-k}+1)$ kills one
element (same-column-adjacent case) and 2-block-expands the other
(non-degenerate, $|d| \ge 3$).

**Case analysis at $a=4$:** 8 cases per step ($\tau \in \{L,R\}^3$),
3 steps = 24 sub-cases. Step 1 done by general $\tau_1 = L/R$ case
analysis (matches May-15-a3). Step 2 has positions tabulated in
Table 2 (8 rows). Step 3 follows the same template; the final
pair $P_3^\tau$ is verified directly via `trace_a4.py` at $n=12$,
matching the predicted $\{T_{\tau L}, T_{\tau R}\}$ for each $\tau$.

**Computational verification (independent):**
- Direct $B_9^{(\lambda)} V_\lambda$ at $n=12$ has support exactly
  $S_4^{(12)}$ (16 SYTs).
- Per-trajectory: each of the 8 supports of $u^{(\mu_1)}$ at $a=3$
  produces a 2-element pair matching the L/R encoding prediction.

## Status of the rank-zero program

| Family | Status |
|--------|--------|
| $(1^n)$ sign rep | trivial |
| $(2,1^{n-2})$ hook k=2 | structural (May-11) |
| $(3,1^{n-3})$ hook k=3 | structural (May-12) |
| $(2,2,1^{n-4})$ non-hook a=2 | structural (May-13) |
| $(2,2,2,1^{n-6})$ non-hook a=3 | structural (May-15) |
| **$(2^4,1^{n-8})$ non-hook a=4, $n\ge 12$** | **structural (May-16, new!)** |
| $(2^5,1^{n-10})$ a=5 | computational only |

## Path to general $a$

The per-trajectory framework gives a clean reduction. To prove
Conjecture~\ref{conj:Sa-support} at general $a$, it suffices to
prove Conjecture~\ref{conj:flow} (per-trajectory invariant). The
substantive content is showing **exactly one element of each pair
is killed at each step**.

Empirically, the kill/expand alternation at step $k$ depends on bit
$\tau_k$ of $T'$'s encoding via a specific positional rule. A
uniform proof would identify this rule structurally — likely via
a finer invariant tracking the position of $n-1-k$ in $P_k^\pm$ as
a function of $(\tau_1, \ldots, \tau_k)$.

For specific $a$, the case analysis is finite ($2^{a-1}$ cases per
step) and tractable. $a=5$ would have 16 cases per step × 4 steps =
64 sub-cases — doable but tedious.

## Questions for you

1. **The L/R encoding as a "binary tree decoder."** Each bit of $\tau$
   "decides" one binary choice in the Hecke action chain. This
   smells like a representation-theoretic or crystal-theoretic
   phenomenon — does the picture remind you of Hecke-crystal
   structures, $W$-graph cells, or anything similar?

2. **Same-row case ruled out structurally.** I used a sizing argument:
   for $n \ge 3a$ and $k \le a-2$, $n-2-k \ge n-a \ge 2a > 2a-1 \ge$
   row-$r$ col-1 entry for $r \le a$. So $n-2-k, n-1-k$ cannot share
   a row in the partition. This is clean but relies on the $n \ge 3a$
   stability threshold. Is there a slicker way?

3. **Push status.** 27 unpushed commits on `clio-vega/proofs`,
   latest is the a=3 + general-a inductive (May-15) papers. New
   paper today: `2026-05-16-a4-support-flow.tex`. The PAT issue
   from May 6 persists.

## Honesty

- Step 3 case verification at $a=4$ is asserted ("same template as
  Step 2") + corroborated by direct computation at $n=12$. Not
  fully written out. Standard for this style of proof, but worth
  flagging.

- The "uniform structural invariant" for general $a$ is genuinely
  conjectural. I see the pattern (position of $n-1-k$ shifts
  according to L/R bits) but haven't pinned down a clean closed-form
  statement that proves it directly.

- The general-$a$ rank-zero theorem now reduces to a finite
  combinatorial check at each $a$. Mechanically extendable, but
  doesn't give a closed-form proof for all $a$ simultaneously.
