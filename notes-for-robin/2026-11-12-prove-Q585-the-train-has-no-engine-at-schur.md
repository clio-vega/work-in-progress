# PROVE 2026-11-12: Q585 is ill-posed at the instrument. At the Schur point the puzzle model's own crossing cannot carry a train.

Note: https://github.com/clio-vega/proofs/blob/main/2026-11-12-Q585-ybe-train-vs-commutor.tex
(pdf alongside; code `code-1112-Q585/` @ 4641a0145b29; result commit 0a0d607)

Robin, Q585 asked whether the map LR(λ,μ;ν)→LR(μ,λ;ν) that a YBE "train" on Knutson–Tao puzzles would
induce at the 0/1 point equals the Henriques–Kamnitzer crystal commutor. The brief made me check first that
the train exists as a *deterministic* map. As far as I can make it from the model itself, it does not:

- Cut the puzzle into diamonds (Δ over ∇) plus the bottom row. It becomes SE-lines (λ) crossing SW-lines (μ)
  and fusing into ν. The crossing D0 = ∇∘Δ factors through the middle horizontal edge, so **rank D0 = 3 of 9**
  (proved). It is not a braiding.
- D0 **kills the input (SE,SW)=(0,1)**. That is where the equivariant rhombus sits, and its weight y_j−y_i is zero
  at the Schur point. In this model, the 0/1 point and an invertible crossing cannot both be had.
- The bundle crossing B_N is never single-output for N=2..5, and it does the swap only on constant words (computed).

So the falsifier cannot fire, and "yes" is neither confirmed nor refuted. Two things remain open. One is a train
with a *foreign* defect R; I couldn't write its YBE without a source stating the argument. The other is the HK
octahedron commutor on hives (ID recalled as math/0408114, not verified), which may already be the theorem.
I suspect "KTW prove commutativity by moving an R-vertex" was a mis-memory of that octahedron work.

The commutor side is reusable. Two instruments (crystal operators; RSK+evacuation) agree 1308/1308 over 67 c≥2 cells.
A lesion differs on 1298. The lex-matching control separates on 67/67, and reverse-lex agrees on 67/67, so it would
have been a blind control.

Also this session: Rick's three SHOULD items are fixed in the .tex files, recompiled clean, and the Q565 dimension-count
node is promoted to peer-reviewed.
