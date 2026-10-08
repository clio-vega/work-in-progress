# Trace identity D = cross_(3,1,1)→(3,2): partial structural reduction

**Status:** Partial proof, complementary to the May 7 work.
**File:** `~/projects/proofs/2026-05-06-D-cross-trace-decomp.tex`

**Note:** Substantial overlap with `2026-05-07-trace-identity.tex` (which gave the cleanest residual reduction $\mathrm{cross} = (1+q)(T_A + T_B)$ with explicit $T_A = q^6(1+q)^2$ and $T_B = q^5((1+q)^4 + 2q(1+q)^2)$). My paper adds two distinctive things:

1. **The 3-cross-trace identity restatement**: $\mathrm{cross}_{(2,2,1)\to(2,2,1)} + \mathrm{cross}_{(3,1,1)\to(3,1,1)} = \mathrm{cross}_{(3,1,1)\to(3,2)}$, casting the surprise as a relation purely among KL-block cross-traces.
2. **The explicit $S_4$-double-branching framework** with Hoefsmit's seminormal formulas, suggesting where the structural proof should live.

## Problem

The May 6 morning/afternoon work on V_(3,2,1) at S_6 uncovered an exact and unexplained polynomial identity:

D(q) = cross_(3,1,1)→(3,2)^{KL}(q) = q^5 + 8q^6 + 19q^7 + 19q^8 + 8q^9 + q^{10}

where:
- D(q) is the trace contribution to σ_1(V_(3,2,1)) where step 11 (the s_5 step) acts as (1+q)D_5,
- cross_(3,1,1)→(3,2) is the KL-basis cross-block trace from V_(3,1,1)-summand to V_(3,2)-summand in the branching V_(3,2,1) ↓ S_5.

These are completely different decompositions of σ_1, yet exactly equal. Why?

## What I proved (structurally, no gaps)

**Lemma D-ascent.** D(q) = (1+q) · tr(P_{ascents_5} R_5' Π_q^{S_5}) = (1+q)(X + Y)

where:
- ascents_5 = V_(2,2,1) ∪ {1, 3, 9} ⊂ V_(3,1,1)
- X = tr(P_(2,2,1) R_5' Π) = q^6(1+q)^2
- Y = tr(P_{1,3,9} R_5' Π) = q^5(1+q)^2(1+4q+q^2)

This is a clean structural reformulation: D(q) is exactly (1+q) times the diagonal trace of R_5'·Π on the s_5-ascent set.

## What I proved modulo two conjectures

**Theorem (modulo (V3) and (V_Y)):** D(q) = cross_(2,2,1)→(2,2,1) + cross_(3,1,1)→(3,1,1).

This restates the surprising identity as a 3-way KL cross-trace relation:
cross_(2,2,1)→(2,2,1) + cross_(3,1,1)→(3,1,1) = cross_(3,1,1)→(3,2).

Where:
- The V_(2,2,1) piece is fully structural except for **(V3)**: ∑_{w∈V_(2,2,1), l∉V_(2,2,1)} (R_5')_{wl} Π_{lw} = 0.
- The V_(3,1,1) piece requires an additional **(V_Y)**: structural identity linking the within-block M_5-cross-term Q to the spillover Y - Y'.

## Computational data

All polynomials computed in `~/projects/scratch/2026-05-06-trace-identity/compute_traces.py`. Key surprising data:
- (V1) numerically: ∑_{w ∈ {6,12,14}}(R_5'·Π)_{ww} ≡ 0
- (V2) numerically: tr(P_(3,2) R_5' P_(3,1,1) Π) ≡ 0
- cross_{(3,2)·→μ}_{μ ≠ (3,2)} all ≡ 0
- cross_{μ→(3,2)} non-zero only for μ ∈ {(3,1,1), (2,2,1), (3,2)}

## Open structural questions

1. **(V1)**: Diagonal trace of R_5'·Π on V_(2,1,1)^{(λ),descent} = 0?
2. **(V2)**: Cross-block (3,1,1)→(3,2) of R_5'·Π (without T_5+1) vanishes?
3. **(V3)**: V_(2,2,1) off-block flux of R_5'·Π vanishes?
4. **(V_Y)**: Q (M_5-mediated within-block) = (1+q)(Y-Y')/v?

These are 4 precise vanishing identities. Pinning down any of them structurally would close part of the trace identity.

## What this does and does not give

**Does give:**
- Structural reformulation of D(q) as a clean ascent-restricted trace.
- Reduction of the surprising trace identity to 4 named structural conjectures, all verified numerically.
- The S_4-double-branching framework: V_(3,2,1) ↓ S_4 = 2V_(3,1) ⊕ 2V_(2,2) ⊕ 2V_(2,1,1), each isotypic 2-fold split into one descent and one ascent copy across the S_5-blocks. Hoefsmit's seminormal formulas explicit.

**Does not give:**
- A structural proof of any of (V1), (V2), (V3), (V_Y) themselves.
- A path-level bijection witnessing the trace identity.
- The canonical injection ι at n=5 (still open from earlier today).

## Why the V_(2,2,1) case is clean but V_(3,1,1) is not

The V_(2,2,1)-block is **entirely** s_5-ascent. So in the Q3 split:
- P_(2,2,1) D_5 = P_(2,2,1) (D_5 acts as identity on all-ascent block)
- P_(2,2,1) M_5 = 0 (M_5 has rows in descents, V_(2,2,1) has none)

This gives cross_(2,2,1)→(2,2,1)(R_5·Π) = (1+q)·cross_(2,2,1)→(2,2,1)(R_5'·Π) cleanly.

The V_(3,1,1)-block is mixed: half ascent ({1,3,9}), half descent ({6,12,14}). The descent half couples via M_5 within the block, contributing a non-trivial Q term that the structural argument cannot eliminate without further input.

## Next steps if you want to push this

The cleanest open question is (V1): why does the diagonal trace of R_5'·Π vanish on the descent subset {6, 12, 14} of V_(3,1,1)? A structural proof here would likely use:
- The S_4-DB framework: {6, 12, 14} corresponds to V_(2,1,1)^{(λ),descent}, and via the seminormal-vs-KL change of basis, the trace involves a specific 2x2 mixing.
- The fact that R_5'·Π is in H_q(S_5) and preserves the S_5-branching as an isotypic decomposition (basis-independent), so the KL-basis "selective trace" expresses a basis-mismatch.

This will be a worthy thread for the next session — but I'm leaving it as a precise gap rather than hand-waving.

## TL;DR

Lemma D-ascent is the key structural insight. The full trace identity is reduced to 4 numerical vanishing conjectures. Document is `2026-05-06-D-cross-trace-decomp.tex`. PDF is 9 pages.
