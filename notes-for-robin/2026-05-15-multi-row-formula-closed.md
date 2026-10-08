# Note for Robin — 15 May 2026 (wake + dream cycle)

## TL;DR

**The multi-row extended sign-kill formula is empirically closed.** All 24 multi-row datapoints (3+ row $\hat\lambda$, varied $|\hat\lambda|$) match the refined formula
$$\tau(\lambda) = \max\big(0,\, q + 2\ell(\hat\lambda) - 1 - |\hat\lambda|\big).$$
The 2-row meta-theorem (yesterday, commit `18fdbc0`) is the $\ell = 2$ specialisation. Multi-row needs only bookkeeping extension to the same proof template — contributor recursion preserves $\tau$ exactly in both Case 1 (row-$\ge 3$ corner) and Case 2 (bottom-row $\hat\lambda_\ell = 2$ corner).

## What I'd flag

1. **75 unpushed commits**. PAT still 403. When you refresh it, the headline commits to see are `18fdbc0` (meta-theorem) and the 8 case-by-case papers `2026-05-14-extended-sign-kill-*.tex`.

2. **Structural reading of $\tau$.** Rewriting: $\tau > 0 \iff q$ exceeds the *excess of $\hat\lambda$ beyond a $2 \times \ell$ rectangle*. Trailing 1-rows buy eigenspace containment at unit rate against rectangular excess. This is the quantitative form of the [[r-additivity-meta-theorem]] picture.

3. **Crown-jewel connection** (`connections/2026-05-15-three-paths-to-threshold.md`). The threshold $\tau$ is visible from three angles:
   - My Hecke seminormal eigenspace work (proven)
   - TL immanants / KL basis (Nguyen-Pylyavskyy arXiv:2605.12880) — *hypothesis*: $\mathrm{tr}_{V^\lambda}(B^{(\lambda)} \cdot C_w')$ factors through non-crossing matchings whose depth is bounded by $\tau$
   - Spin Hall-Littlewood lattice (Gunna-Wheeler-ZJ arXiv:2504.19205) — *hypothesis*: asymmetric Murphy $b'$ ↔ spin parameter; $\tau$ as partition-function vanishing degree

   If the TL immanant Sage check on $\lambda = (3,2,1)$ confirms factorisation, the case-by-case proofs collapse into one immanant identity. Most actionable next step.

4. **Memory hygiene.** The `connections/` directory was empty until today; the SUMMARY.md was a 37k-token session log. I pruned SUMMARY hard and started the connections file. Going forward: every dream cycle produces or sharpens at least one connection file.

## Next session

PROVE.md is now multi-row meta-theorem (general $\ell$). Strategy memo at `~/projects/scratch/2026-05-15-multi-row-tau/PROOF-STRATEGY.md`. Template extends almost verbatim; should be a straightforward induction extending the 2-row proof.

## Honest moment

Yesterday I encoded the multi-row obstruction in memory as "the formula needs row-$\ge 3$ correction terms." That was a *prediction* I promoted to a content statement. The data refuted it cleanly this morning. Lesson: don't bake unverified predictions into memory as facts. The dream-journal entry has the full reasoning trace.
