# For Robin — 2026-05-18: Support-size $2^a$ theorem **closed**

## TL;DR

**Closed Conjecture 5.6 of `2026-05-17-trajectory-uniform.tex`.**
The support-size $2^a$ statement is now a theorem for the entire
family $\lambda = (2^a, 1^{n-2a})$ at every $a \ge 2$, $n \ge 3a$.
This is the PROVE.md target.

Writeup: `2026-05-18-final-pair-identification.tex` (8pp, see scratch
`~/projects/scratch/2026-05-18-final-pair/`).

## What's new

**The final pair identification** — i.e., the explicit identification
$\{\bar\sigma(P_{a-1}^+), \bar\sigma(P_{a-1}^-)\} = \{T_{\tau L}, T_{\tau R}\}$
for each $T' \in S_{a-1}^{(n-2)}$ with encoding $\tau = \varepsilon(T')$.

The proof rests on four pieces, all short:

1. **Closed form for $S_a$**:
   $$T_\varepsilon = \{i-1 : \varepsilon_i = L\} \cup \{2a-i : \varepsilon_i = R\}$$
   (for $1 \le i \le a$). Proved by induction on $a$ from the recursion.
   The $L$- and $R$-bits fill disjoint halves of $[2a]$, mirror-symmetric.

2. **Case alternation along the trajectory**: at step $k$, the pair
   is in Case II iff $\tau_k = R$ (with step 0 always Case II).
   Follows from the May-17 encoding-bit identification corollary.

3. **Three-piece $\sigma$-decomposition**: at step $k$,
   $\sigma(P_k^+) = A_k \sqcup M_k \sqcup U_k$ where:
   - $A_k$ (lower range $\{n-2a+1,\ldots,n-2-k\}$) = $\sigma(T') \cap$ this range
     — by the May-17 $\sigma$-invariant.
   - $M_k$ (middle $\{n-1-k, n-k\}$) — determined by the case.
   - $U_k$ (upper $\{n-k+1, \ldots, n\}$) = $\{n-j : 0 \le j \le k-1, \tau_{j+1} = R\}$
     — by induction on $k$ using the kill/expand case analysis.

4. **Match the formula against the closed form**: at $k = a-1$, the
   lower-range $\bar A_{a-1}$ collects the $L$-bit contributions of
   $\tau$ (positions $i-1$ for $i \in [1, a-1]$, $\tau_i = L$); the
   upper-range $\bar U_{a-1}$ collects the $R$-bit contributions
   (positions $2a-i$ for $i \in [1, a-1]$, $\tau_i = R$); and the
   middle pair $\bar M_{a-1} \in \{\{a-1\}, \{a\}\}$ matches the
   "$a$-th bit" position ($a-1$ for $L$, $a$ for $R$) in the closed
   form of $T_{\tau L}, T_{\tau R}$. The pair has both
   middle-positions, so $\{\bar\sigma(P_{a-1}^+), \bar\sigma(P_{a-1}^-)\}
   = \{T_{\tau L}, T_{\tau R}\}$.

## Consequence: support theorem

Combined with the May-17 dimension bound $\le 1$ and the disjoint-pair
argument over $T' \in S_{a-1}^{(n-2)}$:

**Theorem.** For every $a \ge 2$, $n \ge 3a$,
$B_{n-a+1}^{(\lambda)} V_\lambda$ is exactly $1$-dimensional with
seminormal support $S_a^{(n)}$ ($|S_a^{(n)}| = 2^a$), all coefficients
nonzero in $\mathbb{Q}(q)$.

Hence the **rank-zero theorem** $\Pi^{S_n}|_{V_{(2^a, 1^{n-2a})}} = 0$
holds for every $a \ge 1$, $n \ge 3a$, conditional only on the Phase A
endpoint $R'_n V_\lambda = E_{n-1}^+|_{V_\lambda}$ at general $a$
(proved at $a \le 3$; "mechanical" but unwritten at $a \ge 4$).

## Computational verification

Direct $\sigma$-level trajectory simulation verifying
$\{P_{a-1}^+, P_{a-1}^-\} = \{T_{\tau L}, T_{\tau R}\}$:

| $a$ | $n$ | trajectories | result |
|-----|-----|--------------|--------|
| 2 | 6, 7, 8 | 2 each | PASS |
| 3 | 9, 10, 11 | 4 each | PASS |
| 4 | 12, 13, 14 | 8 each | PASS |
| 5 | 15, 16 | 16 each | PASS |
| 6 | 18 | 32 | PASS |

Total: **12 cases, 106 trajectories**, all matching the closed-form
prediction. The $a=6$ case is new — beyond the prior May-17
verification range.

The closed-form $S_a$ formula was also independently verified against
the recursive definition for $a \le 6$, with encoding round-trips
through both directions.

## How this fits the May 13–17 arc

| Date | Result |
|------|--------|
| May 13 | $(2,2,1^{n-4})$: first non-hook, $a=2$, support $4$ by hand. |
| May 14 | Phase A at $a=3$ + conjectural $2^a$ family + recursive $S_a$. |
| May 15 | $(2,2,2,1^{n-6})$ $a=3$ support $8$ by hand + general-$a$ inductive reduction. |
| May 16 | $(2^4,1^{n-8})$ $a=4$ via per-trajectory framework + Conj 4.4/4.5. |
| May 17 | Uniform per-trajectory invariant (Conj 4.4) + σ-invariant + encoding bits. |
| **May 18** | **Final pair identification (Conj 4.5/5.6) → support theorem unconditional (mod Phase A).** |

The "support is exactly $S_a$ of size $2^a$" claim of May 14 is now
fully proved.

## What this paper does NOT close

1. **Phase A at general $a$**: the orthogonal piece. Was conditional
   in May-17, remains conditional today. The structural argument at
   $a = 2, 3$ is concrete; for $a \ge 4$ it's a routine generalization
   I haven't sat down to formalize. **Likely a separate session.**

2. **The "support stability" theorem with optimal threshold**: I've
   proved it at $n \ge 3a$. The $n=3a$ threshold is empirically sharp
   from earlier data (PROVE.md table: $a=5$ stable at $n=15=3a$;
   $n=14$ gave 31, not 32). The structural argument uses $n \ge 3a$
   exactly once, in the same-row exclusion (Lemma 3.2 of May-17).
   The bound is therefore likely tight, but I haven't proved tightness.

## Push status

**30 unpushed commits**, latest will be this one. The PAT issue from
May 6 persists — I cannot push. The 29-commit backlog includes the
entire $a=2 \to a=6$ structural program. Robin, this is the longest
the read-only state has gone — when you regenerate the PAT,
`git push` will deliver all of it.

## Questions for you

1. **Is the "L-bits fill the low half, R-bits fill the high half"
   picture clean enough to be the recommended description of $S_a$?**
   The recursion is conceptually motivated by the $L/R$ trajectory
   choice, but the closed form is what makes the verification clean.
   Maybe the right way to describe $S_a$ in the paper is "the set
   of $a$-element subsets of $[2a]$ realizable as $L$-contributions
   in the bottom half plus $R$-contributions in the top half."

2. **Phase A as a focused session?** I think one wake of dedicated
   work could close Phase A at general $a$ using the May-14
   formulation. Worth doing?

3. **Beyond $(2^a, 1^{n-2a})$ — next family?** Empirically the next
   rank-zero non-hook is $(3, 2, 1^{n-5})$ (PROVE.md backup target),
   where $j$-formula doesn't immediately collapse. The per-trajectory
   framework should generalize but with TWO "L/R" choices per step
   instead of one. Worth thinking about.

## Files

- Writeup: `~/projects/proofs/2026-05-18-final-pair-identification.tex` + `.pdf`
- Verification scripts: `~/projects/scratch/2026-05-18-final-pair/`
  - `verify_closed_form.py` — closed-form $S_a$ vs recursion
  - `verify_trajectory.py` — final pair identification at $a \in \{2,\ldots,6\}$
