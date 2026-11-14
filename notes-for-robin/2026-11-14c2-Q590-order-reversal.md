# Q590 (PROVE 2026-11-14 c2): Order Reversal is not a single-migration growth diagram

Artifact: https://github.com/clio-vega/proofs/blob/main/2026-11-14c2-Q590-order-reversal-switching.tex (commit `3fb80b68369e`; code `code-1114c2-Q590/` @ `64131e56a304`).

**Status of G1 (Purbhoo Prop 5.1 (ii)=(iii)): still computed, not proved.**

1. **Step 0.** The brief's control was "reverse the (ii) B-list and apply ι". That *is* Order Reversal, so it is the target in disguise.
   Order Reversal is still not bookkeeping. The (iii) journeys are not the (ii) journeys run backwards:
   - step strings match on only 86/606 journeys;
   - the total move counts differ, 4262 vs 3612;
   - no cell matches fully.
   The hexagon's only symmetries (for d≠n−d) are the 120° rotations, and these move A.
2. **Q590 as stated is ill-posed.** The B-chain and ι(reversed C-chain) are the *same* chain, so the growth diagram has no second input.
   **The natural well-posed form is refuted.** That form says single migrations out of A form a growth over the ideals of α. It fails in 233/1100 ideals (to B) and 129/1100 (to C).
   The smallest witness is λ=μ=(2,1), ν=(3,2,1). Swapping the order of two corners sends the second rhombus to (0,2) instead of (2,0).
3. **New computed fact: mixed commutation.** An A→B migration and an A→C migration of distinct corners commute. This holds 1558/1558, including 262 cases where the journeys interact.
   Two A→B migrations commute in **0** of their 440 interacting cases. The order information sits entirely in same-direction interactions.
   Commutation alone does **not** give Order Reversal. The needed count hypothesis fails in 342/740 classes.
4. **Where the gap now sits ("Exchange").** Induct on ℓ(α) by first sending the top row to B. The commutation grid covers the (iii) steps until (iii) reaches the top row.
   After that, (iii) on M and (iii) on M₁ move *different physical rhombi*. This is the precise missing local lemma.
5. **The coplactic lemma for G4 now has a first-hand quote.** van Leeuwen math/9908099, §3.3, `\copcommthm` (number 3.3.1 inferred from the subsection counter), switching form. I quoted it verbatim from the TeX source.
   The G4-with-K node stays at computed. Two reasons: I did not check vL's proof, and I have not matched the reading-order conventions.

Question for you: is the Exchange step something you recognise from Purbhoo's "long but straightforward" omitted proof? Or does it hint that (ii)=(iii) really needs the Prop 5.2 jdt dictionary?
