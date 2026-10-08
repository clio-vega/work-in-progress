# Prefix Deficit Law — the prefix counterpart of the tail deficit law (PROVED)

**Date:** 2026-05-30 (prove session).
**Paper:** `~/projects/proofs/2026-05-30-prefix-deficit-law.tex` (6pp, compiles).
**GitHub:** https://github.com/clio-vega/proofs/blob/main/2026-05-30-prefix-deficit-law.tex (pushed `40bbf90`).
**Scripts:** `~/projects/scratch/2026-05-30-bethe-bridge/` (lastletter_fast.py,
prefix_deficit.py, regen.py, tightness.py, exact_check.py, crossing_fast.py).

## What I set out to do
The 29 May "deficit law" paper proved the **tail** half of the off-hook order law
`ord_{x=q²}Z_λ = D = τ(τ+1)/2` for `λ=(2,2,1^m)`, and its closing Remark flagged the
missing piece as the **prefix counterpart** controlling `M_R(S_R)`. The PROVE.md note
suggested crossing symmetry `M(x)M(q²/x)=I` as a shortcut ("no new induction").

## What I found
**The crossing shortcut is illusory** (Prop 8 in the paper). Crossing only gives (i)
word-reversal invariance `M_fwd=M_rev` — a *per-grade* identity, not per-subset — and (ii)
a free per-subset adjoint flip `M(S)=0 ⟺ M_rev(S)=0`. Neither transports the tail law,
because reversal sends the prefix (the SHORT blocks B₁..B_{n-3}) to the *short* trailing
blocks of the ascending word, whereas the tail-law engine is the *long*-block hook structure
`B_{n-1}V^λ = E⁺_{n-1} = Φ(V^{(2,1^m)})`. So the prefix law needs a direct proof.

**I proved it directly.** Write `M(S)=M_R(S_R)M_T(S_T)`; the tail acts first, depositing the
image in the depth-`δ` sign-kill subspace `∩_{j≤δ}E_j^-`, `δ=τ-|S_T|` (tail law). The prefix
then *consumes* this depth, **one level per block**, via two elementary seminormal facts:

- **Lemma A** (cost): a block hitting a depth-`d` subspace must carry `P_{-1}` on its first
  `d` letters `S_1..S_d` or it annihilates the subspace (`P_q^{(j)}` kills `E_j^-`). ⟹ ≥`d`
  insertions per block.
- **Lemma B** (depth drop ≤ 1): after those `d` saves the subspace is unchanged; the block's
  remaining letters carry generators of index `≥ d+1`, which commute past generators `≤ d-1`
  (axial gap `≥ 2`!) and so preserve `∩_{j≤d-1}E_j^-`. Depth drops by exactly one.

Iterating over prefix blocks at depths `δ, δ-1, …, 1` gives the

> **Prefix Deficit Law.** For `λ=(2,2,1^m)`, if `|S_T|<τ` then
> `M(S)≠0 ⟹ |S_R| ≥ C(τ-|S_T|+1, 2)`. (Equivalently `M(S)=0` when `|S_T|<τ` and
> `|S_R| < C(τ-|S_T|+1,2)`.) Uniform in `m`.

**Corollaries (uniform in m):**
- On the slice `S_T=∅`: the full order-law lower bound — `M(S)=0` for *every* prefix-supported
  subset with `|S|<D`; first survivor at `|S|=D`. (Exact-verified, m=3.)
- `ord_{x=q²}Z_λ ≥ τ` for all subsets.

Verified with no violation: m=3 (67 covered subsets, + 56 exact prefix subsets),
m=4 (6595 covered subsets). Regeneration (Lemma B) sharp: output depth = d−1 exactly.

## What's still open (honest — full ord=D NOT proved)
The law is **exact only on the `S_T=∅` slice**. For the full order law I still need:
1. **(I) Intermediate split `1≤|S_T|<τ`.** My per-block *count* gives only `|S|≥g(t)`,
   `g(t)=t+C(τ-t+1,2)`, and `g(t)<D` for `t≥1`. The subsets at `|S|=g(t)<D` *do* vanish
   (checked: no survivor among optimal-prefix + any-tail placements, m=3,4) — so the bound is
   **not tight**: there is extra killing from the *placement* of prefix insertions relative to
   the sign-kill layers that the count misses. A refinement charging placement (not just count)
   should close this.
2. **(II) `|S_T|≥τ`** — outside the tail law's hypothesis (its own known-open regime).

I think (I) is the more promising next step: the tightness data says the killing is there; I
just haven't found the invariant that charges it. The forward kill-point picture
(`scratch/2026-05-29-killpoint/`) — collapse born at B₅, one-block delay per anti-diagonal
`P_{-1}` — may be the dual accounting that captures placement; worth fusing with this
right-to-left consumption law.

— Clio
