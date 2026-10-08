# The deletion bridge — off-hook order law, split problem dissolved

**Date:** 2026-05-31 (prove session). Paper: `~/projects/proofs/2026-05-31-deletion-bridge-order-law.tex` (6pp, compiles).

## TL;DR
The split-independent off-hook order law for λ=(2,2,1^m) — `M(S)≡0 ∀|S|<D=C(m,2)`, regardless
of how S splits between tail and prefix — was stuck because the per-block count bound
`g(t)=t+C(τ−t+1,2)` is loose (<D) for tail-insertion count `t≥1`, and the killing came from
*placement* not count (the intermediate-split residual in the 2026-05-30 prefix-deficit paper).

**I found a clean reduction that removes the split entirely.** Since `P_{-1}=I−P_q`, expanding
the ordered product gives a Möbius bridge between *insertion* and *deletion* operators:
```
   M(S) = Σ_{U⊆S} (−1)^{|S|−|U|} Π_del(U),     Π_del(U) = Ω with factors in U deleted (set to I).
   Π_del(U) = Σ_{V⊆U} M(V).
```
Two consequences, both **fully proved, m-uniform**:
- `ord = ddel := min{|U| : Π_del(U)≠0}`.
- **The split-independent per-subset order law ⟺ the single split-free statement**
  `Π_del(U)=0 for all |U|<D`. (If |S|<D every U⊆S has |U|<D, so M(S)=Σ±Π_del(U)=0.)

So the whole intermediate-split / heavy-tail casework was an artefact of writing the word with
`P_{-1}` instead of `I−P_q`. The honest object is `ddel`: min factors to delete from the
degenerate staircase Ω to revive it.

## Then: rank-1 collapse → single-vector walk
Verified (m=3 exhaustive over |U|≤D, m=4 random): for `|U|≤D`, the two longest blocks (the tail)
collapse V^λ to **rank ≤1 — a line ⟨w⟩**. So the prefix is a single-vector walk on w. This is
EXACTLY the setting of the unconditional hook chip-firing bound C(m,2) (`hook-orderlaw-chipfiring`).
The deletion order law `ddel≥D` becomes a **single-vector reach bound**: every tail-deposited
line w (with u_T tail deletions) needs `≥ D−u_T` prefix deletions to survive.

## What's verified
- Bridge identities (both directions) as exact matrices: m=3,4. ✓
- `ddel=D`: m=2,3 exact exhaustive; m=4 generic-q screen (all |U|<6 give 0, survivor at 6). ✓
- rank-1 collapse after tail for |U|≤D: m=3 exhaustive, m=4 random. ✓

## The crux that remains (Conjecture in §4–5)
The single-vector reach bound `Ψ(w) ≥ D−u_T`. **Lower-bound obstruction = the old merged-arc /
merged-junction gap**: a support-based reach principle UNDERSHOOTS when few deletions break a
shared pinch (concrete m=3 example: line with support incl. the target (2,4), min column-1-charge
0, but true Ψ=1). So Ψ is not a function of support/E^- signature — it sees the coefficients.
This is the same residual you were asked about in `offhook-rank1-pinch` ("why does within-arc
reduce to hook chip-firing").

**My read:** the bridge + collapse are the real new leverage. The reach bound now lives on a
*single vector* and is the literal off-hook twin of a bound we proved unconditionally for hooks
(via walk-necessity, no positivity). Transcribing the hook's walk-necessity reach principle to
the collapsed off-hook line — charging merged pinches correctly — is the path I'd take next. The
two missing rigor pieces: (1) m-uniform proof of the rank-1 collapse (expect: rank-1 pinch +
forward-backbone collapse); (2) the reach principle on the line.

Scripts: `~/projects/scratch/2026-05-31-intermediate-split/probe_*.py` (bridge, ddel, collapse,
cost-to-go, potential hunt).
