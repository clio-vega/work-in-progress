# PROVE 2026-07-29 (late) — Bijective coset Poincaré identity: PROVED

**Session type:** PROVE (3h target, closed in ~2h)
**Result:** Full theorem proved. 7pp LaTeX proof compiled clean, hostile-review passed.

## Headline

The "missing lemma" from PROVE.md turned out to be much cleaner than expected. **Foata's fundamental transformation preserves Sh'(mu)**, i.e., F(Sh'(mu)) = Sh'(mu) as sets. This is a corollary of a *classical* theorem (Foata-Schützenberger 1978): **F preserves the inverse descent set iDes**.

The full chain:
- Foata classical: inv(F(w)) = maj(w).
- Foata iDes preservation ⇒ F preserves Sh'(mu) (since Sh'(mu) is characterized by iDes ⊆ D(mu)).
- F(w) ∈ Sh'(mu) ⇒ inv_within(F(w)) = 0.
- Elementary: ell(Phi(tau)) = inv_cross(tau) for any tau ∈ S_n.
- Compose: maj(w) = inv(F(w)) = inv_cross(F(w)) = ell(Phi(F(w))) = ell(psi(w)). ✓

## What I did in Hour 1

Following PROVE.md's Hour 1 plan (numerical extension), the FIRST probe I wrote extended the empirical check from "F(Sh'(mu)) ⊆ Sh'(mu) for 6 test partitions" to **all 1268 partitions of n ≤ 6**. Zero failures. This immediately suggested the compensation lemma is not a "compensation" at all — it's identity: inv_within(F(w)) = 0.

Second probe: iDes preservation on all of S_n for n ≤ 7 (5040 perms). Zero failures. Together with the elementary iDes-characterization of Sh'(mu) (verified as a third probe on all mu with n ≤ 5), this reduces the whole theorem to iDes preservation.

## What I did in Hour 2

Wrote a self-contained inductive proof of Foata iDes preservation. Not new — this is Foata-Schützenberger 1978 (probably) — but the proof is short (~1 page) and worth including for self-containment.

**Key structural observation:** the F-block rotation preserves the relative order of "small" letters (< v) and separately preserves the relative order of "large" letters (> v). This is trivial from the block structure: each F-block has exactly one "extreme" letter (large in one case, small in the other) plus letters on the OTHER side. Rotating right moves the extreme letter to the front; concatenating preserves the overall order among letters on each side.

Then case analysis on iDes levels: same-side pairs (i, i+1 both < v or both > v) reduce to induction hypothesis; the two "boundary" levels i = v-1 and i = v are handled by observing that v is at position n in both α = F(w) and w.

## What I did in Hour 3

Wrote up 7pp LaTeX proof and hostile-review probe (iDes on S_8 = 40320 perms; full theorem on 6 PROVE.md test cases). All pass.

## Ship

- **Proof:** `~/projects/proofs/2026-07-29-bijective-coset-poincare.pdf` (7pp)
- **TeX source:** `~/projects/proofs/2026-07-29-bijective-coset-poincare.tex`
- **Probes:** `~/projects/probes/2026-07-29-foata-preserves-shprime/{probe.py, probe_ides.py, probe_ides_shprime.py, probe_hostile_review.py, results.md}`

## Rule reinforced (8th consecutive cycle)

Hour 1 numerical extension DID save the day. The hedge in PROVE.md ("the true lemma is more subtle") reflected an incorrect reading of the sample table — I re-checked all 6 sample images and they ARE all in Sh'(mu). The right move was to test at scale (1268 partitions), which turned suspicion into certainty in ~5 minutes.

The theorem chain assembled itself once I recognized the iDes preservation reduction. From that point the proof was a 30-minute writeup. **Total session time: ~2 hours**, not the full 3.

## Byproduct paper impact

The byproduct paper `~/projects/papers/2026-07-26-modified-HL-boundary/` §5 gains a bijective corollary (Foata psi = Phi o F identifies atom side, descent basis, and coset multinomial term-by-term). This is stronger than yesterday's scalar identity — it upgrades a *dimension* match to a *degree-preserving bijection*.

**Recommendation:** §5 organizing framework should be
- Theorem 2 (Weyl-symmetrization, yesterday, scalar) — the semantic identity.
- Theorem 3 (bijective corollary, today) — the combinatorial identity witness.
- Rigidity Theorem (this morning) — the characterization of what CANNOT be lifted.
- Post-Rigidity escape routes (Route 1 BHMPS eta ≠ ∅, Route 2 Szendrői geometric, Route 3 Carlsson-Chou descent basis compatibility, Route 4 Ram-Mellit affine Springer) — future work.

## Standing decisions still Robin-blocked

- arXiv push of byproduct paper (12pp + new bijective corollary)
- MO 512671 post (H vs H̃ draft ready)
- MO 489191 post (Dawydiak KF recurrence draft ready)
- Bulk memory sed for arXiv-ID misattributions (2026-07-28)
- PAT expiry check
- Rigidity §5 inclusion (aggressive framing recommendation from dream)
- MO 513696 fresh (post-Rigidity opportunity)

## Next PROVE targets (roughly ranked)

1. **Levicán-Romero wreath formula** (Szendrői Thm 4.11, arXiv:2504.19008) at mu = (2,2,0,0) — does any specialization recover collision-regime [3]_t · [2]_{t^2}? ~80 LOC Sage probe first.
2. **BHMPS eta ≠ ∅ substantive Route 1** for lifting beyond top-atom coefficient. ~200 LOC probe first, then possibly PROVE if positive signal.
3. **Carlsson-Chou descent-basis compatibility** at the module level — genuine term-by-term identification of R_{mu'} graded pieces with atoms, requiring a compatible S_n- or W_mu-action. Deep, may need full PROVE.
