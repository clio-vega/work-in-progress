---
date: 2026-07-30 (late wake, ~1h)
subject: ∇ probe closed NEGATIVE (Rigidity reinforced); §5.2 Theorem D landed in paper (15pp clean); PAT confirmed expired
---

# Late wake — 2026-07-30

Short session. Two substantive outputs + one blocker.

## 1. The sole standing hour-1 probe closed NEGATIVE — with structure

Ran the ∇ $\widetilde{H}_{(2,2)}$ Schur-split probe (from this morning's dream, question doc `questions/2026-07-30-nabla-two-column-vs-wreath-isotypic.md`). Verdict: **no**, ∇ $\widetilde{H}_{(2,2)}$'s Schur decomposition does not split along the trivial/sign isotypic decomposition of $R_{(2,2)}$.

Full Schur expansion (agent computed via SymPy fallback; SageMath not installed in container):

- $[s_4] = q^2 t^2$
- $[s_{31}] = q^2 t^2 (q^2 + qt + t^2)$
- $[s_{22}] = q^2 t^2 (q^2 + t^2)$
- $[s_{211}] = q^3 t^3 (q + t + qt)$
- $[s_{1^4}] = q^4 t^4$

All Schur positive (as Qu 2605.20954 guarantees). But the $S_2 \times S_2$ isotypic pieces (dim 6 each at $q=t=1$) don't specialise to $T_2(t) = 1+t^2+t^4$ or $N_2(t) = t+t^2+t^3$ at any of $\{q=0, q=1, t=0, t=1, q=t\}$. Support degrees are $\{(0,0),(2,0),(0,2),(1,1)\}$, wrong pattern.

**Sizes explain it:** $\nabla \widetilde{H}_{(2,2)}$ at $q=t=1$ has dim $24 = 4!$; $R_{(2,2)}$ has dim $6$. Each isotypic block is dim 6 but the $(q,t)$-refinement spreads across $[q, q^4] \times [t, t^4]$.

**Interpretation:** $\nabla \widetilde{H}_{(2,2)}$ and $R_{(2,2)}$ live at different levels — any wreath-compatible bigraded lift must route through a further quotient or plethystic identity, not direct Frobenius pairing. **This reinforces the Rigidity Theorem** (Theorem 5.4): bigraded lifts via atom-symmetrisation are closed off; the ∇ side confirms the closure independently.

**Sprint impact:** No Route-1 ↔ Route-2 unification remark for the paper. Sprint holds at four theorems. Question doc updated with full resolution + interpretation.

Probe artefacts: `~/projects/probes/2026-07-30-nabla-two-column-probe/`.

## 2. §5.2 Theorem D landed in byproduct paper — 15pp clean

Added Theorem D (Wreath decomposition of the collision-regime coset Poincaré) as a fourth subsubsection in §5.2, between the current "Theorem C: the combinatorial witness" and "Corollary and remarks." Structure mirrors A/B/C:

- **Theorem 5.6 statement:** general $k$, formulated as $S_2$-isotypic decomposition of $R_\alpha = R_{2k}^{S_k \times S_k}$ via the block-swap involution, with $T_k(t)$ (trivial) $=\sum_i \widetilde f_{(2k-2i,2i)}(t)$ and $N_k(t)$ (sign) $= \binom{2k}{k}_t - T_k(t)$. Specialised to $k=2$ recovers $[3]_t \cdot [2]_{t^2}$.
- **Proof sketch:** Chevalley-Shephard-Todd + Frobenius reciprocity + plethysm $h_2[h_k] = \sum s_{(2k-2i,2i)}$ + complement + Szendrői cross-check at $t=1$.
- **Remark:** $k=2$ specificity of the clean product form; Szendrői bigraded lift as $(t,q)$-refinement; Levicán-Romero / Romero-Wen wreath refinement as open follow-up.

Introduction paragraph of §5.2 updated: "in three passes" → "in four passes" (semantic + structural + combinatorial + algebraic).

**Bib entries added:** `adin-brenti-roichman2001` (classical mother-paper, per today's dream), `romero-wen2025` (open follow-up citation). ABR cited in Theorem D's proof sketch as the classical ancestor of the descent-basis/wreath-invariant technology.

**Macros added** to preamble: `\Ind`, `\ch`, `\triv`, `\sgn` (all needed by Theorem D). One TeX fix: `\mathrm{Szendr\H{o}i}` → `\text{Szendr\H{o}i}` (since `\H` invalid in math mode) — replaced globally, 2 occurrences.

Paper compiled clean: `~/projects/papers/2026-07-26-modified-HL-boundary/paper.pdf` (15pp, no undefined refs).

## 3. PAT confirmed expired (GitHub email in inbox)

Email agent found GitHub email confirming PAT `clio-oci` (token id 14139669) has expired. **All GitHub pushes blocked** until you regenerate. arXiv push of the (now 4-theorem, 15pp) paper is stalled behind this.

Regen URL is in the GitHub email in your inbox.

## Standing sign-off queue (unchanged except paper page count)

1. **arXiv push** — paper is 15pp now (was 14pp; +1pp for Theorem D subsection). Four theorems in §5.2. Compiles clean. Blocked by PAT expiry.
2. **PAT expiry** — regenerate.
3. **MO 512671** (H vs H̃) — draft pending sign-off.
4. **MO 489191** (Dawydiak KF recurrence) — draft pending sign-off.
5. **MO 513696** (KF single-box power of 2) — fresh, ready.
6. **Bulk memory sed** — two arXiv-ID misattributions.
7. **Fetch cache** — six papers: BHMPS 2506.09015, Romero-Wen 2505.01732, Chou-Hanada 2509.24252, Hanada 2410.15514, Qu 2605.20954, ABR 2001 math/0112073.
8. **Bundle `clio-poincare-sketches` companion note** — now includes four proofs (add today's wreath decomposition to the three from 07-28/29). ~30-90min.
9. **Post-push email to Marino Romero** — single bridge between Route 2 and Route 4 (per dream cycle). Optionally email Dawydiak on chain regime.

## Owed to Lyra

I replied to her K4 harmonic-Gram email (fork choice: **(b)** beta-derived metric). She's due the explicit $\beta_{ij} \to M_e$ map "within a cycle or two." Blocking checks I flagged in reply: (i) vertex-orientation inheritance convention, (ii) T4-drop vs coboundary sign on rims. Follow-up in next cycle.

## What's next

- If PAT regenerated + arXiv push approved: push immediately, then bundle `clio-poincare-sketches` (now four proofs) as follow-up.
- If not: next session works on Chou-Hanada 2509.24252 restriction probe (Route 3 module-level lift) or the $\beta \to M_e$ map for Lyra.

Sprint status: four theorems in four sessions holds. ∇ probe closed cleanly. Paper ready to push behind the PAT wall.

— Clio
