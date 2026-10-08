# PROVE 2026-07-30 (afternoon): r-wreath extension of Theorem D — PROVED

**Session:** 3h PROVE. Session status: **positive result**, single theorem proved to the end.

**Proof file:** `~/projects/proofs/2026-07-30-r-wreath-extension.pdf` (5pp)
**Probe:** `~/projects/probes/2026-07-30-r3-wreath-extension/`

## Headline

Theorem D at $r = 2$ (this morning) extends cleanly to general $r$ and $k$.
The isotypic decomposition of $R_{(k^r)} := R_{rk}^{S_k^r}$ under the
residual $S_r$-action is:

$$
\Frob_t(R_{(k^r)}) \;=\; \sum_{\pi \vdash r} m_\pi(t) \, s_\pi,
\qquad
m_\pi(t) \;=\; \sum_{\lambda \vdash rk} \widetilde f_\lambda(t) \cdot
\langle s_\pi[h_k],\, s_\lambda\rangle.
$$

Proof method (identical structure to $r = 2$ case): CST decomposition of
$R_{rk}$, exact $(-)^{S_\alpha}$ functor, Frobenius reciprocity for
$H = S_k \wr S_r$, classical plethysm formula for wreath induction of
"trivial on base $\times V_\pi$." Direct — 2 lines of chain
$\Hom_{S_r}(V_\pi, V_\lambda^{S_\alpha}) = \Hom_H(\ldots) = \Hom_{S_n}(\ldots)$.

## Bonus: cyclotomic Hilbert-series identity at $k = 2$

Independent structural result:

$$
\boxed{\;\binom{2r}{2^r}_t \;=\; [r]_{t^2}!\cdot \prod_{i=1}^r [2i-1]_t.\;}
$$

Elementary proof (2 lines): $[2i]_t = [2]_t [i]_{t^2}$; split $[2r]_t!$
into even/odd factors, cancel $[2]_t^r$ against $([2]_t!)^r$.

- $r=2$: $\binom{4}{2,2}_t = [2]_{t^2} \cdot [1]_t[3]_t = [3]_t[2]_{t^2}$ (matches this morning)
- $r=3$: $\binom{6}{2,2,2}_t = [2]_{t^2}[3]_{t^2} \cdot [1]_t[3]_t[5]_t = [5]_t[3]_t[3]_{t^2}[2]_{t^2}$
- $r=1,\ldots,6$: verified symbolically

Combinatorial interpretation: matchings of $\{1,\ldots,2r\}$ decompose
as (matching selection) $\times$ (pair ordering); $q$-analogue splits
the two, pair-ordering costs $t^2$-inversions because pairs are stored
in increasing order.

## Cyclotomic ≠ isotypic (interesting negative)

**The cyclotomic factorisation of $\binom{2r}{2^r}_t$ does NOT align
with the $S_r$-isotypic decomposition.** Specifically at $r=3, k=2$:
$\Phi_3 = [3]_t$ divides the total but no individual $m_\pi(t)$
(checked at cube-root-of-unity: $m_{(3)}(\omega) = 3 \neq 0$).

**Different empirical divisibility:** $[2r-1]_t$ (top factor of the
cyclotomic form) divides *every* $m_\pi(t)$ when $k = 2$ (verified
$r = 2, 3, 4$), and also at $(r,k) = (3,3)$; but not at $(2,3)$ or
$(2,4)$. Suggests a rank-2 phenomenon that's not explained by this
framework. Flagged as follow-up question — no attempt to resolve here.

## Computational verification (r,k) pairs

Full identity $\dim_t R_{(k^r)} = \sum_\pi f^\pi m_\pi(t) = \binom{rk}{k^r}_t$
verified for:
$(r,k) \in \{(2,2), (2,3), (3,2), (2,4), (3,3), (4,2)\}$
via `probe verify_full.py`. All match.

Cyclotomic identity verified for $r = 1, \ldots, 6$.

## Byproduct paper implications

The paper's §5.2 Theorem D subsection (added today morning at $r=2$)
extends cleanly to general $r$. Two options:

**(1) Minimal edit.** Add remark to Theorem D at $r=2$ saying "extends
to arbitrary $r$; see companion note *r-wreath extension* (2026-07-30
afternoon)." Cite the standalone `.tex` in the bibliography once posted.

**(2) Broaden §5.2.** Rewrite the Theorem D subsubsection as
"$r$-parameter family" and include the general statement + Corollary
(cyclotomic factorisation at $k=2$). Adds maybe 1pp, brings paper to
~16pp. Would need updating the "wreath decomposition" language in the
introductory four-passes paragraph.

**Recommendation:** Option 1 for the current arXiv push (already 15pp
with four theorems; extending is neatening, not sprinting further).
Save Option 2 for a v2 revision or the natural sequel paper on wreath
Hilbert-series identities. Await your call.

## Standing decisions (unchanged from morning)

- arXiv push still queued (paper 15pp; PAT expiry confirmed but push
  itself blocked, not the writing)
- Six-paper cache-fetch list unchanged (Romero-Wen 2505.01732,
  Levicán-Romero 2504.19008, Szendrői 2602.15017, BHMPS 2506.09015,
  BHMPS 2509.24040, ABR math/0112073)
- MO 512671, 489191, 513696 all still pending post
- Bulk memory sed still queued
- `clio-poincare-sketches` bundling now covers FOUR proofs plus this
  fifth (r-wreath extension): 5 proofs (Rigidity, Bijective, Wreath
  r=2, Wreath r=general, cyclotomic k=2).
- Post-push Romero email: now definitely warranted — this note plus
  today morning's note gives him a natural conversational hook.
- Lyra β_ij → M_e follow-up still owed (from morning wake); flagged
  fallback in PROVE.md not needed here (main line closed positive).

## Rule reinforced (13th consecutive cycle)

Hour-1 target decisive again. The hour-1 probe (compute $\binom{6}{2,2,2}_t$
+ plethysm) landed the entire result cleanly:
- Cyclotomic factorisation dropped out at line 3 of output
  (`(t**2+1)*(t**2-t+1)*(t**2+t+1)**2*(t**4+t**3+t**2+t+1)`)
- Plethysm formula → isotypic multiplicities → sum-verification
  all in the same hour
- Extension to general $(r,k)$ was just running the same loop

Total session time to closed theorem + PDF: ~90 min. Remainder used
for structural remarks and Robin memo. Fallback (Lyra $\beta \to M_e$)
untouched — main line went through cleanly.
