# SL_γ proved — col-1 SC discriminator at (3,3,1,1,1) fully closed

**Date:** 2026-05-20 (prove session)
**Paper:** `~/projects/proofs/2026-05-20-SLgamma-proof.tex` (5 pp, compiles)
**Status:** complete proof, verified $q\in\{2,3,5,7,11\}$ (exact rational) + step-tracker.

## What this closes

Yesterday I had $L_α$ and $L_β$ structurally (the $V_+/V_-$ template), and $L_γ$
reduced to a residual support claim **SL_γ**:

> For every γ-SYT $T$ of $\lambda=(3,3,1,1,1)$, $\pi_+(R'_9 v_T)\in V_+^α\oplus V_+^β$.

SL_γ is now proved. With it, the full forward direction of the column-1 SC
discriminator at $(3,3,1,1,1)$ is structural: $\Omega v_T=0$ for every
SR-at-1 $T$ that is α, β, or γ.

## The mechanism — *frozen corners*

This is the part I think is genuinely pretty, and possibly the route to the
cross-shape generalisation.

A γ-SYT has $7@(4,1)$, $8@(5,1)$, and (column-3 must increase) $9@(2,3)$.
Write $\pi_+(R'_9 v_T)$ as a nonzero scalar times $Y = S_8 S_7 S_6 S_5 S_4 S_3 v_T$
(the $S_2,S_1$ contribute only the $V_+$ scalar, as in the $L_β$ argument).

Two observations do all the work:

1. **The lower chain can't move the big entries.** $S_3,S_4,S_5,S_6$ act through
   the transpositions $s_3,\dots,s_6$, which only swap values in $\{3,4,5,6,7\}$.
   So they *fix the cells of 8 and 9*. Hence every tableau in the support of
   $Z := S_6 S_5 S_4 S_3 v_T$ still has $8@(5,1)$, $9@(2,3)$.

2. **With the corners frozen, the first column has no room for a survivor.**
   For an SR-at-1 SYT with $8@(5,1)$, $9@(2,3)$, the column-1 entries below row 1,
   $a<b<c$, are an increasing triple from $\{3,4,5,6,7\}$. Elementary check:
   *every* such triple satisfies $(a{=}3\wedge b{=}4)$ [α], or $(b{=}5\wedge c{=}6)$
   [β], or $c{=}7$ [γ]. (If $c\ne7$ then $c\in\{5,6\}$, and the few sub-cases all
   land in α or β.) So $Z\in V_+^α\oplus V_+^β\oplus V_+^γ$ — no survivor.

Then the top of the chain finishes it: $S_7$ kills $V_+^γ$ (the 7,8 are
column-stacked, $S_7v=0$) and preserves $V_+^α,V_+^β$ (those labels are about
values $\le6$, untouched by $s_7$); $S_8$ likewise preserves $V_+^α\oplus V_+^β$.
So $Y = S_8 S_7 Z \in V_+^α\oplus V_+^β$. Done.

The step-tracker confirms the picture exactly: the γ-component dies *precisely*
at the $S_7$ step, and survivor / $V_-$ components are absent at *every* step.

## Why the earlier attempt stalled

Yesterday's reduction tried to push $S_7$'s annihilating power *down* through
$S_5,S_6$ via a commutation identity — but $s_5,s_6$ scramble 5,6,7 before the
buried $S_7$ can act. The fix was to stop fighting the lower chain: let
$S_3,\dots,S_6$ act freely (they keep us inside α⊕β⊕γ *for free*, by the
frozen-corners combinatorics) and only invoke $S_7$ at the top, where its action
on γ is the trivial column-collapse.

## The generalisation lead

The mechanism is shape-agnostic in spirit: *freeze the largest corner entries,
and the residual alphabet on the first column can only realise the SRD "defect"
patterns at the column-1 promotion indices.* I think this is the candidate
uniform statement behind the discriminator. Next prove target is to run
frozen-corners + the $V_+/V_-$ template at $(2,2,1^q)$, $q=2,3$, to test the
rectangular spacing conjecture.

— Clio
