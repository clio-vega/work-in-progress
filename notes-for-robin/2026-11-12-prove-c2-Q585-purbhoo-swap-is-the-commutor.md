# For Robin — PROVE 2026-11-12 c2: Purbhoo's swap is the crystal commutor (computed)

Robin, the short version: **Purbhoo's bijective commutativity map (arXiv:0705.1184, Cor 3.4, built by migrating
rhombus flocks through mosaics) agrees with the Henriques–Kamnitzer crystal commutor on every cell I tested:
518/518 highest-weight elements in 190 cells with c^ν_{λμ} ∈ {2,3,4,5} (gl_4).** It holds under two different
tableau↔crystal bijections, and his Prop 5.4 (the swap is an involution) checks out with 0 failures.

- How: I built migration exactly from his definitions (KT puzzle → mosaic through the R^4 lift, integer
  coordinates). I validated it against his Thm 1 and Cor 3.2 on 139 mosaics × 8 orientation variants before
  computing the swap.
- One honest flag: in 956 steps his "unique minimal hexagon" is not unique as worded. I break the tie by the rule
  his two figures show, and the other choice breaks his Theorem 1 (it gets stuck on 63/142 mosaics). It is written
  up as an interpretation.
- What it is not: a proof. A proof needs his §5.1 migration ↔ jdt dictionary (proofs omitted in the paper) plus an
  identification of the resulting jdt composite with the commutor.
- Why it matters for my seed question: the puzzle-side "train" that moves rhombi is, at the Schur point, the
  coboundary commutor. The next question (Q587) is whether his migration groupoid's monodromy is the cactus group.

PDF: https://github.com/clio-vega/proofs/blob/main/2026-11-12-Q585-purbhoo-swap-vs-commutor.pdf
Also: Q584 revised per Rick's referee reply (Thm 8 now tested non-vacuously).

## Addendum (re-entry, same session): where the proof must go
There is now an intermediate map: tableau switching Σ against u_κ. On the same 518 elements, M = Σ exactly (H1), and
Σ = C under both bijections (H2). So the open gap is two gaps. H1 is a proof about mosaics: Purbhoo's two B→A migrations
compose to switching, and his §5.1 jdt dictionary omits its proofs. H2 is a reading task that does not involve Purbhoo:
switching = commutor on highest-weight elements. I hold that only at agent-summary grade. Neither half is proved.
Code: `proofs/code-1112c2-Q585/switch.py` @ 3257a1d79e78.
