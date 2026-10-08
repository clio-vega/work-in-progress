# 2026-05-28 — Operator reformulation of the off-hook order law (merged gap update)

Robin —

This session pushed on the merged-junction gap left from the morning's within-arc
reach paper (`2026-05-28-offhook-within-arc-reach.tex`). The honest result: the gap
is not closed, but it now sits in a sharper place and a meaningfully cleaner frame.
Paper: `~/projects/proofs/2026-05-28-orderlaw-operator-rankflow.tex` (5pp).

## What's new

**Operator reformulation.** The trace-level order law lower bound is equivalent to an
**operator** statement:
$$\ord_{x=q^2}Z_\la \;=\; \min\{\,|S|\;:\;M(S)\ne0\text{ as an operator on }V^\la\,\},$$
where $M(S) = \prod_k A_k(S)$ is the ordered staircase product with $A_k$ either
$P_q^{(i_k)}$ or $P_{-1}^{(i_k)}$. Verified on every shape I tested
(hooks $(2,1^m)$, off-hooks $(2,2,1^m)$, $(2,1,1,1)$). For the lower bound it suffices
to prove $M(S)=0$ for $|S|<\binom{\tau+1}{2}$ — no traces, no cyclic factorisation.
**The intact/merged dichotomy that drove the trace approach dissolves at operator
level: it's one linear product, not a cyclic trace.**

**Monotone rank.** Read $M(S)$ right-to-left. Every factor is a projector, so the
running rank is monotone non-increasing. $M(S)\ne0$ iff running rank stays $\ge 1$
to the leftmost factor.

**Rank ladder for $\Omega$.** At $\la=(2,2,1^m)$, $\Omega$'s running rank ladder is
$$\dim\W_1=m+1\quad\xrightarrow{\text{first intact (1,n-1) crossing}}\quad 1
\quad\xrightarrow{\text{next intact (1,k) crossing}}\quad 0,$$
i.e. $\Omega$ dies after **just two** intact far-junction crossings (verified $m=2,3,4$).
The first crossing is a clean pinch onto $\W_1\cap\W_{n-1}$ (dim 1); the second is a
sign-kill.

**First-pinch theorem.** For any $S$, the rightmost intact far-junction crossing
pinches the running rank to $\le 1$. So every survivor enters a rank-1 regime
universally; verified for all 14 critical survivors at $(2,2,1,1,1)$ (rank stays
exactly 1 from the first crossing to position 0).

**Operator lift of the within-arc reach.** The morning's trace-level reach
(triple-pinch sign-kill + inert-top restriction) lifts verbatim to a rank-1
vector flow. Gives an unconditional operator-level lower bound for intact
subsets across the family $(2,2,1^m)$.

## Where the merged gap sits now

The merged case is no longer "trace cyclicity breaks" — that obstruction is gone.
The remaining genuine obstruction is **inert-top non-invariance**: when the
merged super-arc contains a generator adjacent to the surviving inert top,
no single $q$-eigenspace is invariant under the whole super-arc product. Two
candidate fixes were tested and refuted this wake:

1. **Glued top** $\W_{t_1}\cap\W_{t_2}$: zero, because the two tops are adjacent
   ($|t_1-t_2|=1$).
2. **$\W_1$ chip-firing**: gen 2 stays rank 4 on $\W_1$; $\W_1$ is the *source* of
   the rank-1 collapse, not its host.
3. **Empty-$++$-gap criterion**: refuted — 8/14 survivors at $(2,2,1,1,1)$ violate it.
   The carried rank-1 vector does not stay in the joint $q$-eigenspace across a
   generator adjacent to the inert top, so the next sign-kill does not fire.

## The route I think is right

A **sequential inert-top restriction**: walk along the merged super-arc, switching
the relevant inert top each time we cross a broken junction, and tracking a
specific rank-1 transfer across each break. This matches the "sequential two-top
transfer keyed on $T_5$'s entry" picture I left in the memory note this morning,
but the operator framing makes it a pure rank-1 vector flow with no trace
cyclicity to worry about. I haven't yet found the right inductive invariant.
If you see one — or recognise it from the literature — please tell me.

## Computational status

$(2,2,1,1,1)$, $\ord=3$, is computationally unconditional (all 232 subsets with
$|S|\le 2$ checked: $M(S)=0$ at operator level; the 14 survivors at $|S|=3$ all
$=q^8/(q+1)^{16}>0$). The intact case is now also rigorously closed via
Corollary~5.2 of the new paper. The merged structural lower bound for
$(2,2,1^m)$ at all $m$ is the precise open lemma.

— Clio
