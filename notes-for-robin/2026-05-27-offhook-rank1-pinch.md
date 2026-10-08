# Off-hook order law: the rank-1 pinch (2026-05-27 prove session)

**Headline.** I found the right generalization of the hook proof's "rank-one collapse"
to off-hook shapes, and PROVED the structural heart for the whole family (2,2,1^m).
The order law `ord_{x=q²} Z_λ = τ(τ+1)/2` for (2,2,1,1,1) (τ=2, ord 3) is reduced to a
reach principle that exactly parallels hooks, with two reach lemmas verified-not-proved.

Paper: `~/projects/proofs/2026-05-27-order-law-offhook.tex` (6pp, compiles).

## The mechanism (the prize)

Hooks worked because every q-eigenprojector P_q^{(i)} is **rank one**, collapsing c_S into
scalar sandwiches. Off hooks that fails (rank 4 on (2,2,1,1,1)). The correct replacement:

1. **Matrix transfer.** Rank-factorize P_q^{(i)}=R_i L_i^T; then c_S = tr(cyclic product of
   4×4 transfer blocks). Scalars become matrices. [proved, linear algebra]

2. **Rank-1 PINCH (the theorem).** For |a-b|≥2 the generators commute, so P_q^{(a)}P_q^{(b)}
   is the orthogonal projector onto the joint q-eigenspace W_a∩W_b, and
       dim(W_a∩W_b) = ⟨Res^{S_n}_{S₂×S₂} V^λ, triv⊠triv⟩ = ¼(f^λ + 2χ^λ_(2) + χ^λ_(2,2)).
   For EVERY (2,2,1^m) this equals 1. It's a **class function** — that's why the off-band
   rank is uniformly 1, and why this is the honest generalization of "rank one": on hooks the
   single-generator projector is rank one; off hooks the *commuting-pair* projector is.
   [PROVED; MN-verified m=2..5]

3. **Pinch factorization.** The only off-band word-adjacencies are the far junctions (1,k),
   k≥3. Their rank-1 Gram blocks pinch the cyclic trace into a product of **arc-scalars**.
   c_∅ = ∏ σ_j, and exactly **τ of the arcs vanish**, located in blocks B_4,…,B_{n-2}.

4. **Arc reach principle.** Fixing the zero arc in B_k costs k-3 insertions (B4:1, B5:2),
   summing to Σ(k-3) = C(m,2) = τ(τ+1)/2 — the exact off-hook twin of the hook junction cost
   k-2 (Σ = C(m,2) too). Lower bound PROVED for all subsets that leave far junctions intact.

## What's proved vs. verified

- **Proved:** matrix transfer; the rank-1 pinch (character theorem, whole family); pinch
  factorization; lower bound when no far junction is broken (∑ disjoint arc costs = τ(τ+1)/2).
- **Verified, not proved from scratch:** (i) within-arc cost = k-3 (expected: localized hook
  chip-firing on the descending run with rank-1 boundary); (ii) merged-arc cost when the shared
  pinch is broken — the two zero arcs of (2,2,1,1,1) share junction (1,5); breaking it merges
  them and needs ≥3, verified. These two are the precise remaining gaps.
- **Equality:** 14=C₄ critical survivors, all equal q⁸/(q+1)¹⁶ > 0 ⇒ G_3≠0.
- ord=3 for (2,2,1,1,1) is computationally certain (min-support=3 over all subsets, q=5,7/3).

## Why this matters

(2,2,1^m) is the exact off-hook twin of the hook (2,1^m): both have τ=m-1, ord=C(m,2). The
rank-1 pinch turns the off-hook problem into the SAME reachability question as hooks, now on an
arc graph (far junctions = pinch nodes, zero arcs = blocks B_4..B_{n-2}). Closing the two reach
lemmas would give the order law for an infinite off-hook family.

**Question for you:** the within-arc scalar is y^T(∏ band-P_q over a descending generator run)x
with y,x the rank-1 pinch vectors. Is there a clean reason it reduces to the hook path-graph
chip-firing? If the pinch vectors are themselves joint q-eigenvectors of (T_1,T_k), maybe the
arc collapses to a hook-type rank-one computation on a subquotient. That's the crux I couldn't
close.
