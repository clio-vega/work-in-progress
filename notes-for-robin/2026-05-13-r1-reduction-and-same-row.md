# r=1 inductive reduction: the same-row obstruction surfaces

**Date:** 2026-05-13 (late evening — second prove session after the iso refutation)
**Paper:** `2026-05-13-r1-inductive-reduction.tex` (6 pp, commit pending — PAT still read-only)
**Status:** Partial structural result + a surprising new conjecture isolated.

## Headline

The PROVE.md decoration-iso target was refuted earlier today. I pivoted to a smaller target — extending the May-15 inductive reduction from `(2^a, 1^*)` to all r=1 rank-zero shapes. **The verbatim generalisation is FALSE.** I found a clean counter-example: at λ = (3, 3, 1^4), `dim E_+|_{V_λ} = 85` but `dim Φ_*(V_{μ_1}) = 64`. There is a **21-dim same-row part** of E_+ unaccounted for.

The good news: the reduction formula `B^(λ) = (outer factors) Φ_*(B^(μ_1))` **still holds** at λ = (3, 3, 1^4) — verified computationally to give the right 2-dim subspace on both sides. The reason: the same-row part `S ⊂ E_+` gets killed by subsequent R'-applications. So the formula salvages, but the May-15 proof strategy doesn't directly apply.

## What this opens up

A new structural conjecture:

**Conjecture (Same-row dies).** For every r=1 rank-zero λ satisfying the standard non-degeneracy, the same-row part S of E_{n-1}^+|_{V_λ} satisfies
  `R'_{ℓ+1} R'_{ℓ+2} ... R'_{n-1} S = 0`.

This is verified at (3, 3, 1^q) for q ∈ {2, 3, 4, 5} with a striking decay pattern:

| q | dim S | after R'_{n-1} | after R'_{n-2} | after R'_{n-3} |
|---|-------|---------------|---------------|---------------|
| 2 | 10    | 4             | 1             | 0             |
| 3 | 15    | 5             | 1             | 0             |
| 4 | 21    | 6             | 1             | 0             |
| 5 | 28    | 7             | 1             | 0             |

The "go to 1 then to 0" pattern looks like an iterated j-formula leakage, but I haven't found the right structural setup. The obstacle: the natural iso S ≅ V_{(3, 1^{q+1})} as H_q(S_{n-2})-module ONLY holds for the action of T_1, ..., T_{n-3}; the factor T_{n-2} in R'_{n-1} moves vectors OUT of S, breaking the iso correspondence.

## What I actually proved

1. **Algebraic commutation through Φ_*** carries through verbatim from May-15 (Lemma 5 in the paper). On the Φ_*(V_{μ_1}) piece alone, the May-15 commutation argument is shape-independent — only uses index-gap arguments and Φ_* equivariance.

2. **Conditional reduction formula** (Theorem 9): assuming the same-row-dies conjecture, the May-15 formula holds for all r=1 shapes.

3. **dim B^(3,3,1^q) = 2 for q ∈ {2, 3, 4, 5}** (Theorem 12), combining (1)+(2) with May-12 evening on μ_1 = (3, 2, 1^{q-1}).

## What I learned

- The May-15 framework is **more shape-specific than it looks**. It works for (2^a, 1^*) because that family has NO same-row pairs in E_+ — but this is a property of (2^a, 1^*), not of "r=1 in general."
- For r=1 shapes WITH same-row pairs (like (3, 3, 1^*) and hooks (k, 1^*) for k ≥ 3), the Phase A endpoint E_+ has more dimensions than V_{μ_1}. The "extra" is the same-row part S.
- The reduction formula EQUATION still holds (computationally) for these shapes, but the proof is now more subtle: the same-row part dies under the iteration, but for a non-obvious reason.
- This is essentially the same flavour of obstruction we saw in May-12 evening's "C-piece vanishing via j-formula leakage" — but propagated through one more level of iteration, and harder to derive.

## A structural insight (not in the paper)

After the paper was done I noticed a striking pattern. The decay
`f^(3, 1^{q+1}) → q+2 → 1 → 0` matches **exactly** the rank-zero iteration on `V_{(3, 1^{q+1})}`:

- `dim V_{(3, 1^{q+1})} = f^{(3, 1^{q+1})}`.
- `dim E_+|_{V_{(3, 1^{q+1})}} = q + 2` (= `dim V_{(2, 1^q)} + 1 same-row` for the hook).
- `dim B^{(3, 1^{q+1})}_{sharp} = 1` (by j-formula on hook).
- Applying one more R' beyond sharp = 0 (rank-zero).

That's the **exact** decay we observe.

So the structural claim should be: the iso `S ≅ V_{(3, 1^{q+1})}` (which holds at the level of T_1, ..., T_{n-3}) extends — in a more subtle way — to make the iterated R'_k^{(λ)}|_S correspond to the iteration B^{(μ_S)} on V_{μ_S} = V_{(3, 1^{q+1})}. The "subtle" part is handling the extra T_{n-2} factor in R'_{n-1} which takes us out of S.

I suspect there's a clean intertwining: even though (T_{n-2}+1) moves things out of S, the subsequent R'-factors land back in a subspace isomorphic to the next stage of V_{μ_S}'s iteration. Maybe there's an analog of the Φ_* construction that picks up the (T_{n-2}+1) factor as a "Phase A endpoint" within V_{μ_S}.

This would be a very satisfying structural proof if it works.

## What I want next

- Cash in the structural insight above: prove the same-row-dies conjecture by showing that the iteration on S corresponds (via a sophisticated extension of the SYT iso) to the rank-zero iteration on V_{(3, 1^{q+1})}.
- The general claim: for any r=1 shape with same-row part `S = V_{ν}` for some sub-hook ν, the decay corresponds to ν's rank-zero iteration. This would close the same-row-dies conjecture in great generality.
- Once the conjecture is proven structurally, the May-15-style reduction extends to a clean theorem covering all r=1 shapes (including hooks, (k, k, 1^*), and (3, 3, 1^*)).
- This would substantially unify the dim-formula proof program.

## Honest self-assessment

This session caught a real bug in my initial plan to "generalise May-15 verbatim." The bug surfaced on the second computational test (q = 4 of (3, 3, 1^*)) when I noticed dim E_+ ≠ dim V_{μ_1}. The paper now correctly states the obstruction and isolates the conjecture. The deeper question — why does S die? — is open and looks structurally interesting.

The PROVE.md target (decoration-iso) is refuted. This session's partial result is mostly anatomical: I now understand the May-15 setup better than I did this morning, and I have a clean computational pattern for the same-row decay.

**38 unpushed commits** total once this one lands (PAT still read-only — please fix when you have time, Robin).

— Clio
