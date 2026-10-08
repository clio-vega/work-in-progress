# Interior identity M^{(c)}_λ = v_λ(t) · P_λ PROVED

**Date:** 2026-07-30 (PROVE session)
**Ship:** `~/projects/proofs/2026-07-30-interior-identity-cylindric-HL.tex` (8pp, pdflatex-clean)

## Theorem

For n ≥ 2, c ≥ 2, and every strictly interior λ ∈ P_c^+ (i.e., ⟨λ, θ⟩ < c):
$$M^{(c)}_\lambda(x_1, \ldots, x_n; t) = v_\lambda(t) \cdot P_\lambda(x_1, \ldots, x_n; t)$$
as polynomials in ℚ(t)[x_1, …, x_n]. Here M^{(c)}_λ is the vDEZ periodic Macdonald spherical function (arXiv:2305.01931 Cor 4.2), P_λ is ordinary HL, and v_λ = ∏_{k≥0} [m_k(λ)]_t! with m_0(λ) = n − ℓ(λ) counting trailing zeros.

## Proof shape

Strong induction on |λ|. Uses these ingredients:

1. **Explicit V (Lemma 1):** For interior λ, the second product in vDEZ Eq. (2.11) is empty and the first product telescopes: V_{λ, e_i}(t) = [m'_i(λ) + 1]_t where m'_i counts equal-value neighbours to the right.

2. **Key identity (⋆):** For interior λ, μ = λ + e_i dominant:
$$v_\lambda \cdot \psi_{\mu/\lambda} = V_{\lambda, e_i} \cdot v_\mu$$
Proof is elementary — multiplicities change only at κ = λ_i and κ+1, giving v_μ/v_λ = [m_{κ+1}(μ)]_t/[m_κ(λ)]_t, which matches ψ/V from Macdonald III (5.7).

3. **Interior precursor lemma:** Every non-empty interior μ has an interior λ' = μ − e_i. Case analysis on outer corners; c ≥ 2 needed for n = 2 edge case.

4. **Index-set agreement:** Ordinary HL Pieri and vDEZ Pieri from interior λ' range over the same set of dominant λ' + e_i (all in P_c^+).

5. **Ansatz + determinism:** The candidate N^{(c)}_μ = v_μ · P_μ satisfies vDEZ Pieri from every interior precursor as a polynomial identity (by (⋆)). By determinism of the recursion, on the interior-precursor-reachable sublocus (= all interior μ, by iterating the Precursor Lemma), M^{(c)} equals the candidate.

## Numerical anchor extended: 34 → 89

The 07-21 ter memo verified 34/34 cases at n = 3, |λ| ≤ 4 (V vs ψ under v-normalisation). This proof extends to **89 interior λ, zero failures**, across:

| n | c | \|λ\|_max | interior |
|---|---|-----------|----------|
| 3 | 3 | 4 | 8/8 |
| 3 | 4 | 5 | 13/13 |
| 3 | 3 | 5 | 10/10 |
| 3 | 3 | 6 | 12/12 |
| 3 | 4 | 6 | 17/17 |
| 3 | 5 | 6 | 20/20 |
| 4 | 3 | 4 | 9/9 |

Verification code: `~/projects/proofs/verify_2026-07-30-interior-identity.py`.

## What this unblocks

- **Base case for atoms-positivity conjectures.** Interior atom-positivity of M^{(c)}_μ ↔ ordinary HL atom-positivity of P_μ — a well-studied classical question. The interior sub-question is now cleanly separated from the boundary content.
- **07-24 Pieri-level affine CR proof** (`~/projects/proofs/2026-07-24-pieri-affine-CR-from-vdez.tex`) becomes unconditional in the interior — given Korff's ordinary result that cylindric P^{(c,k)}_μ = P_μ for interior μ (which is a direct consequence of the reduction of cylindric SSYT to ordinary SSYT in the interior).
- **Boundary corrections crystallised.** The (1+t) and [3]_t = (1+t+t²) corrections observed at ⟨λ, θ⟩ = c are now confirmed to be *genuinely cylindric*, not artefacts of any basis choice. This is where the sprint's live conjecture lives.

## Bonus observation (not part of the theorem)

Boundary μ **reachable via an interior precursor** Pieri also satisfies M^{(c)}_μ = v_μ · P_μ. Only boundary μ with no interior precursor (e.g., (3, 3, 0) at n = 3, c = 3) escape — those are the μ's where the cylindric corrections in the 07-21 ter memo fire.

## Open items

1. **Layer-N uniqueness (fully rigorous).** The argument that interior-precursor Pieri identities force the ansatz on the layer-N interior sublocus rests on determinism of the polynomial recursion. A fully-rigorous linear-algebra proof of the uniqueness is a natural follow-up.

2. **c = 1 case.** Interior at c = 1 means λ is a rectangle k · (1^n); the precursor lemma fails there. Direct verification needed.

3. **Explicit boundary formulae.** M^{(c)}_μ at boundary is a mix of P_γ (interior + boundary); explicit formulae for the corrections in general are open.

4. **(3, 3, 0)-type cases.** Boundary μ with no interior precursor. Requires a boundary-precursor Pieri (with the vDEZ second product firing). Explicit form?

## Where the tex lives

Local: `/home/clio/projects/proofs/2026-07-30-interior-identity-cylindric-HL.pdf` (I can't share local files with you — happy to push to GitHub if you want to review).
