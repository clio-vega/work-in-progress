# For Robin: Lyra's Levi-length conjecture falsified; a cleaner coset-Poincaré identity emerges

**Date:** 2026-07-26 (afternoon PROVE session)
**Files:**
- Report: `projects/proofs/2026-07-26-lyra-levi-exponent-conjecture.pdf` (7pp)
- Probe: `projects/probes/2026-07-26-lyra-levi-exponent/compute_c_gamma_22210.{py,out}`
- Verifier: `projects/probes/2026-07-26-lyra-levi-exponent/verify_coset_poincare.py`
- Paper update: `projects/papers/2026-07-26-modified-HL-boundary/paper.tex` (Remark 5.6 rewritten, Next-Steps item 3 rewritten)

## What happened

I tested Lyra's Levi-length conjecture at the proper falsifier μ=(2,2,2,1,0) (n=5, W_μ=S_3, orbit size 20, non-chain). Prior probe at μ=(2,2,2,0) was in the wrong laboratory — chain regime forces pure Gaussians and there's nothing to attach an exponent to.

**Result: Lyra's conjecture is falsified.**

- Predicted [k]_{t^3} factor at μ=(2,2,2,1,0)? Absent from all 20 c_γ.
- Predicted [k]_{t^4} factor at secondary μ=(2,2,2,1,1)? Absent from all 10 c_γ.
- Naive |W_μ| alternative (m=6, m=12)? Also absent.

Observed exponents uniformly m ∈ {1, 2}. The m=2 hits are entirely explained by algebraic identities like [4]_t = [2]_t · [2]_{t²} — no Levi invariant is doing work.

## The replacement conjecture (much cleaner)

Reading the top c_μ across all cases suggests a stronger, simpler pattern:

**Conjecture (Coset Poincaré).** For any partition μ of length ≤ n,
```
                     [n]_t !                     _____
    c_μ(t)  =  ─────────────────  =  Poincaré( S_n / W_μ )(t)
               Π_i [m_i(μ)]_t !
```
where m_i(μ) is the multiplicity of i in μ, and c_μ(t) is the top atom coefficient at γ=μ in the Mason atom expansion of P_μ.

**Verified at 12 partitions** (n = 3, 4, 5; orbit sizes 3 to 20): (2,1,0), (2,2,1), (2,2,0), (3,2,1), (2,2,0,0), (2,2,1,1), (3,3,1,0), (3,3,2,0), (3,2,2,0), (3,2,2,1), (2,2,2,1,0), (2,2,2,1,1). Every case matches exactly.

Examples:
- μ=(2,2,0,0): c_μ = [4]_t·[3]_t/[2]_t = [3]_t · [2]_{t²} — coefficients [1,1,2,1,1]. The [2]_{t²} comes from [4]_t/[2]_t = 1+t², *not* from ℓ(w_0^{S_2×S_2})=2.
- μ=(2,2,2,1,0): c_μ = [5]_t·[4]_t = [5]_t · [2]_t · [2]_{t²} — coefficients [1,2,3,4,4,3,2,1]. Same story: the [2]_{t²} is a Gaussian factorization artifact.

## Why this matters

1. **Structural upgrade.** The coset Poincaré identity is a cleaner, sharper conjecture than either Lyra's or the naive |W_μ| version. It also *implies type-invariance for the top coefficient* immediately, since [n]_t!/Π[m_i]_t! depends only on the multiplicity profile.

2. **Lyra's original observation was still a real pattern** — she noticed that m=2 at (2,2,0,0) fits ℓ(w_0^{S_2×S_2})=2. The pattern was real; the causal explanation wasn't. The true cause is the algebraic identity [4]_t = [2]_t · [2]_{t²}. Lyra saw two thirds of the right thing (the exponent 2, the parabolic input); what she missed was that the exponent is not Levi-controlled — it's Gaussian-identity-controlled.

3. **Paper updated.** Remark 5.6 (formerly "Levi length") is now "Coset Poincaré for the top coefficient" and states the new identity explicitly. Next-Steps item 3 is now "prove coset Poincaré" instead of "resolve type-invariance + Levi length". Paper still 11 pages, compiles cleanly.

4. **Open question (highest-value follow-up).** Prove the coset Poincaré identity. Two natural approaches:
   - **Representation-theoretic.** Identify c_μ(t) as the graded character of the coinvariant algebra of W_μ acting on the polynomial ring in n variables. This is exactly [n]_t!/Π[m_i]_t! (Chevalley-Shephard-Todd for S_n restricted to W_μ).
   - **Combinatorial.** Direct extraction of the coefficient of x^μ in P_μ under Macdonald III.(1.4), followed by tracking contributions from lower atoms via the θ^alt bubble word.

5. **Sprint status.** The falsification is a POSITIVE result — it retires a candidate conjecture cleanly and replaces it with a stronger one. Byproduct paper's structural claims are unchanged; only the interpretation of the two-parameter Gaussian factor sharpens.

## Numerical highlights (μ=(2,2,2,1,0))

Bruhat length distribution on the 20-element orbit: (1,2,3,4,4,3,2,1) at lengths (0,...,7). Sum of c_γ(1) across orbit... actually the top c_μ(1) = 5·4 = 20 = |orbit|. Consistent with coset Poincaré (which specializes to |cosets| = |orbit| at t=1).

Full 20-row table in the report PDF §3.1.

## What I'd like from you

- **Sanity check** on the coset Poincaré identity — does this ring a bell as a known result? It has the flavor of a very natural Hall-Littlewood identity that might be in Macdonald III somewhere. If it's already there, I want to cite it correctly; if it's not, the "conjecture" label is appropriate.
- **Direction preference** for the proof attempt: coinvariant-algebra route vs. direct coefficient extraction from Macdonald III.(1.4). My inclination is the coinvariant route because it *explains* the identity structurally (rather than just deriving it).

## For Lyra (if you pass this along)

Lyra — your conjecture is falsified in its stated form, but the observation that prompted it (exponent 2 at (2,2,0,0) matches something involving W_μ) turns out to be the shadow of a **much stronger** identity: c_μ(t) *is* the coset Poincaré polynomial of S_n/W_μ. Your instinct that W_μ dictates the structure was correct; only the *mechanism* was different from what we guessed. The falsifier at (2,2,2,1,0) doesn't just refute the original — it hands us a cleaner conjecture that neither of us would have seen without the discipline of testing at the proper laboratory. Thank you for the push.

—Clio
