# Hook order law: a chip-firing proof (prove session, 2026-05-26)

**File:** `~/projects/proofs/2026-05-26-projector-grading-vanishing.tex` (compiles, 7pp).

## What I set out to prove
The order law `ord_{x=q²} Z_λ(x) = τ(τ+1)/2` for the uniform-rapidity staircase-monodromy
trace, on **hooks λ=(2,1^m)** (there τ=m−1, so the order is C(m,2)). Via the scalar-`s`
linearization (PROVE.md), this equals `ord_{s=0} P_λ(s)` with
`P_λ(s)=Σ_S s^{|S|} c_S`, `c_S = tr_{V^λ} ∏_k A_k`, `A_k ∈ {P_q^{(i_k)}, P_{-1}^{(i_k)}}`.
Target: `c_S = 0` for all `|S| < C(m,2)`, and `G_{C(m,2)} ≠ 0`.

## The key structural discovery
**On the hook V^{(2,1^m)}, every q-eigenprojector P_q^{(i)} has rank one.** (T_1 is
diagonal; for i≥2 the q-eigenvalue has multiplicity exactly 1 because a same-row pair needs
the corner value 1.) Writing P_q^{(i)} = r_i l_i^T, the trace c_S **factorizes** into a
product of scalar "sandwiches" cut at the rank-one Q-positions:
`c_S = ∏_gaps  l_a^T (∏ P_{-1}) r_b`.  So `c_S = 0 ⟺ some gap sandwich = 0` — a per-subset
statement, exactly matching the verified "no cancellation" verdict.

Two more reductions:
- The Gram matrix `G[a,b] = l_a^T r_b` is **tridiagonal** (`G≠0 ⟺ |a−b|≤1`), and since the
  off-diagonal products are constant (αβ) it is similar to a **symmetric** tridiagonal `G̃`
  (off-diag γ=√q/(q+1)).
- Each gap sandwich becomes a **chip-firing process on the path graph 1–2–···–(m+1)**:
  start with a tent at `a`, fire the mid-indices in order (fire j ⇒ zero w_j, push −γw_j to
  neighbours), read w_b. Verified exact-match to the real sandwich vanishing (0 mismatches /300).

## What is fully proven (all m)
- Rank-one collapse + sandwich factorization + tridiagonal/symmetric reduction + chip-firing.
- **Walk-necessity:** F is a signed sum over unit-step subsequence walks a→b; no walk ⇒ F=0.
- **Lower bound `ord ≥ C(m,2)`, unconditional for all m.** The only orthogonal adjacencies are
  the m−1 block junctions (1,k), k=3..m+1. Breaking a junction opens a gap whose sandwich needs
  a unit-step walk; a **reach principle** (a descending run raises the reachable max by ≤1, and
  only if it *contains* that value) gives: a gap covering junctions k..k′ needs ≥ Σ_{i=k}^{k′}(i−2)
  insertions (single junction k costs exactly k−2; merging is strictly worse). Summing over the
  disjoint junction-gaps: |S| ≥ Σ_{k=3}^{m+1}(k−2) = C(m,2).
- **Explicit critical survivor** S* (suffix of length k−2 of each left block B_k), with
  `c_{S*} = q^m/(q+1)^{2m}` (this corrects PROVE.md's typo `q^{m+1}`).

## The one remaining gap (toward equality for all m)
`ord = C(m,2)` (vs `≥`) needs `G_{C(m,2)} = Σ_{|S|=C(m,2)} c_S ≠ 0`, i.e. no cancellation among
critical survivors. The clean sufficient statement, **verified m≤4**: *every* critical survivor
has `c_S = q^m/(q+1)^{2m}` (all equal ⇒ positive ⇒ G = C_m·value ≠ 0). I believe this telescopes
(each survivor is a product of single-junction monomials βα^{k−2} times empty-gap G-factors,
constrained to a common value) or follows from Hoefsmit positivity. The Catalan count C_m of
survivors is a bonus, begging for a ballot/Dyck bijection on the (u_k,v_k) splittings with
u_k+v_k=k−2.

**Bottom line:** order law unconditional for m≤4; for general m everything is proven except the
single positivity input G_crit≠0. The rank-one→chip-firing reduction is, I think, the real prize —
it turns a Hecke-trace order computation into elementary lattice combinatorics, and points at the
off-hook generalization (firing on the seminormal branching graph of λ̂).

Would value your eyes on: (a) whether the equal-value/telescoping claim has a slick proof, and
(b) whether the chip-firing picture rings a bell from an existing integrable/affine-Hecke source.
