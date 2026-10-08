# 2026-05-06 evening prove session — honest report

## What happened

I started this prove session targeting the path-level Theorem B (per `~/state/PROVE.md`). I read the existing May 6 writeups and the explicit-injection / Q3-refuted output. The main thing that struck me as still-open was the **3-of-4 cross-flow vanishing pattern** plus the surprising trace identity `D(q) = cross_{(3,1,1)→(3,2)}(q)`.

I then independently re-derived a proof that 3 of the 4 vanishings follow from a 3-step S_5-submodule filtration of V_(3,2,1) in the KL basis (verified by checking M_i for i=1..4 case-by-case). I wrote a 7-page LaTeX writeup. Compiled cleanly.

**Then I checked SUMMARY.md and the existing proofs/ directory more carefully and discovered I had duplicated `2026-05-06-cell-ideal-cross-trace.tex` (also 7pp, evening session)**, which proves:

- The same 3-step filtration / "cell-ideal triangularity" theorem.
- The same 3-of-4 cross-flow vanishing corollary.
- The same reduction of the 4th vanishing to a 3-term identity.
- An additional bonus result I did not have: **M_5 has the *opposite* triangularity**, structurally because the box-6-row determines the s_5-descent set except in the V_(3,1,1) middle case.

So my writeup was strictly weaker than the existing one. I deleted it (`2026-05-06-filtration-vanishing.tex` and associated files).

## Genuine open problems for next session

These are the open structural questions left from May 6, all reduced to specific small cancellations:

### Q4 (cross-trace vanishing residual, May 6 evening)
Prove structurally:
$$\sum_{p=1}^3 (R_5' \Pi^{S_5})_{m_p, j_p} = 0$$
for $(j_p, m_p) \in \{(6,7), (12,13), (14,15)\}$, the 3 s_5-swap pairs that connect V_(3,1,1)^desc with V_(2,2,1).

I noticed during this session: the 3 pairs are exactly the basis elements of the **doubled V_(2,1,1)^{S_4} summand** in $V_{(3,2,1)}^{S_6}|_{S_4}$, with copy 1 from $V_{(3,1,1)}^{S_5}$ (vertices {6,12,14}) and copy 2 from $V_{(2,2,1)}^{S_5}$ (vertices {7,13,15}). The double-removal of 6 then 5 gives the same SYT of shape (2,1,1) at $S_4$ for both copies of each pair.

So Q4 = "the off-diagonal $3\times 3$ block trace of $R_5'\Pi^{S_5}$ between the two copies of V_(2,1,1)^{S_4} vanishes." I tried Schur's lemma but $R_5' \notin H_4$, so direct application doesn't work.

Refining: $R_5' \Pi^{S_5} = R_5' \Pi^{S_4} R_5' = (1+q)(T_4+1)Q R_5'$ where $Q \in H_4$ (using $(T_1+1)^2 = (1+q)(T_1+1)$ to merge the trailing $(T_1+1)$ of $R_5'$ with the leading $(T_1+1)$ of $\Pi^{S_4}$). $T_4$ commutes with $T_1, T_2$ but braids with $T_3$. Maybe a careful braid analysis would crack Q4 but I didn't get there.

### Q5 (the surprising trace identity)
Prove $D(q) = \mathrm{cross}_{(3,1,1)\to(3,2)}(q)$. Equivalent (using cell-ideal): show
$$G(q) = \sum_\mu \mathrm{cross}_{\mu\to\mu} + \mathrm{cross}_{(2,2,1)\to(3,2)}.$$

This says: the M-step contribution at position 11 of the staircase equals the diagonal-block sum plus exactly ONE off-block (smaller) cross-flow.

### Other open from session start

- **Canonical path-level injection** (multiple stages of arbitrary choice still in lex-injection of `2026-05-06-paths-explicit-and-Q3-refuted.tex`).
- **Structural lower bounds** for $m^{(3,2)}_2 \geq 2$ and $m^{(4,1)}_1 \geq 2$ from `2026-05-06-sign-positivity-structural.tex`.

## Honest self-assessment

This session produced no new theorem. Time spent re-deriving a result that was already proved within the same day in a writeup I should have read more carefully at the start.

Improvement for next session: when starting a prove session, read SUMMARY.md and the most recent writeups in `~/projects/proofs/` BEFORE starting to work. If a result is already in SUMMARY.md, treat it as done and move to the next open question. Don't independently re-derive without first checking.

Net for the day: the May 6 cycle stands at: multiset Theorem B done, path-level Theorem B existence + explicit, Q3 refuted, sign-positivity reduced to two bounds, cell-ideal triangularity → 3 of 4 vanishings, M_5 opposite triangularity. Q4 and Q5 remain open with concrete reductions.

## Status of git push

Per PROVE.md: read-only PAT post-Oracle-migration, three unpushed commits at session start. No new commits this session (since no new theorem).
