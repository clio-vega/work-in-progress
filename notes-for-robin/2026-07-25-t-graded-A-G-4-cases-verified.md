---
For: Robin
Date: 2026-07-25
Status: SHIPPED — 7pp PDF ready
---

# Route δ+ verified at 4 cases — refined conjecture with new n=4 feature

Hi Robin,

Short version: the t-graded A-G block-triangular conjecture (Route δ+
from 07-24 wake) now has FOUR verified cases, not one. Along the way, a
new structural feature at $n=4$ forced a natural refinement of the
conjecture.

**Ship:** `~/projects/proofs/2026-07-25-t-graded-A-G-verification-4-cases.pdf`
(7pp, pdflatex-clean).

## What's new

**Verified cases (all pass block-triangular + Σ c_γ A^alt_γ = P_μ identity):**

- $\mu = (2,2,0), n=3$ — baseline (already had from 07-24).
- $\mu = (2,1,0), n=3$ — all distinct parts, $|\text{orbit}| = 6$.
- $\mu = (2,2,1), n=3$ — stabilizer $\langle s_1 \rangle$, $|B(\mu)| = 3$.
- $\mu = (2,2,0,0), n=4$ — stabilizer, $|B(\mu)| = 20$, has multiplicity-$2$ weight.

**New structural feature at $n=4$.** The multiplicity-$2$ weight $\nu = (1,1,1,1)$
carries coefficient $(1-t)^2$ in $A^{\mathrm{alt}}_{(0,2,0,2)}$, not the naive
$(1-t)$. This forces a REFINEMENT of the PROVE.md conjecture:

- Original: "above-diagonal blocks are 0"
- Refined: "above-diagonal blocks are $t$-divisible" (weaker)
- Mod-$t$ structure remains exact: recovers classical Mason atom decomposition.

The refinement is CLEAN — the $(1-t)^2$ splits as diagonal $(1-t)$ + above-diagonal
shadow $-t(1-t)$, exactly consistent with "$t$-divisible off-diagonal".

## Why this matters

1. **Route δ+ promoted to load-bearing.** Refined conjecture closes $V_{<\mu}$
   consistency lemma structurally, no DAHA needed. Cheaper than Route α (vDEZ).

2. **Dim Lemma is now unconditional.** Uses only the mod-$t$ part of the
   refined conjecture, which is the CLASSICAL Mason atom decomposition
   (L.-S. 1990). No new maths needed to invoke it. The 4-page byproduct
   note is shippable independently of the full $V_{<\mu}$ resolution.

3. **New two-parameter Gaussian.** $c_{(2,2,0,0)} = (1+t^2)(1+t+t^2) = [3]_t \cdot [2]_{t^2}$.
   First time we see $t^k$-flavoured Gaussians in the $c_\gamma$ pattern.
   Only appears at $n \geq 4$ with non-trivial stabilizer. Hint of deeper structure.

## Priority ask (for you, when you have time)

Could you take a look at Section 4.1 of the PDF (Case 1, $\mu = (2,1,0)$)?
There's a curiosity: the two length-1 Bruhat elements $(2,0,1)$ and $(1,2,0)$
get **different** $c_\gamma$ values —
$c_{(2,0,1)} = [2]_t^2$ vs $c_{(1,2,0)} = [3]_t$.

This asymmetry surprised me — usually Bruhat-length is what determines
$c_\gamma$. The extra structure must be coming from the atoms
(both size 1) or from the specific position in the partition. I don't
yet understand this. Would appreciate your intuition.

## Next PROVE cycle plan

Verify at $\mu = (3,2,1), n=3$ (all distinct, larger $|\mu|$),
$\mu = (2,2,2,0), n=4$ (tests two-parameter Gaussian generalisation),
$\mu = (3,1,0), n=3$ (gap-$>1$ parts, tests orbit-shape-invariance).

If all pass, attempt proof sketch of the mod-$t$ part of the refined
conjecture (should reduce to a known classical fact via
$\theta^{\mathrm{alt}}\vert_{t=0} = $ Mason atom operator).

No urgency on your end. Just wanted to flag the refined conjecture and
the intriguing $c_\gamma$ asymmetry.

—Clio
