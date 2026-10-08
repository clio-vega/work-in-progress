# Merged-junction mechanism for the off-hook order law (2026-05-28 wake)

Robin — a quick wake-session note sharpening the one remaining gap in the off-hook order law
`ord_{x=q²} Z_λ = τ(τ+1)/2` for the family `(2,2,1^m)`.

## Where we stand
- **Intact-junction lower bound is now UNCONDITIONAL** (28 May prove session): within-arc reach
  via inert-top restriction + the triple-pinch sign-kill `⅛(f+3χ_2+3χ_22+χ_222)=0`.
- **Sole remaining gap:** the merged/broken-junction case — the *generic* survivor. At `(2,2,1,1,1)`,
  13 of 14 critical survivors break a far junction; 8 break the **shared `(1,5)` junction** that
  merges the two zero arcs B₄, B₅ into one super-arc.

## New data this wake (all exact rational, q=5 and 7/3)
1. At `(2,2,1,1,1)` there are exactly **14 = C₄** critical survivors at `|S|=3`, and **all 14 carry
   the identical value `c_S = q⁸/(q+1)¹⁶ > 0`**. So the grade-3 sum can't cancel — `ord = 3` exactly.
   (Mirrors the hook Catalan survivors, all equal `q^m/(q+1)^{2m}`.)
2. The unique far-junction-**intact** survivor is the descending-run-prefix minimiser predicted by the
   within-arc reach theorem (gens `{3}` of B₄, `{3,4}` of B₅).

## Two tempting single-subspace fixes — both REFUTED
- **Glue both block-tops:** `W_glue = ker(T₅−q) ∩ ker(T₆−q) = {0}`. The two tops `T₅` (B₄) and `T₆`
  (B₅) are **adjacent** (`|5−6|=1`), so they don't commute and the pinch (needs `|a−b|≥2`) doesn't
  apply. Dead end.
- **Restrict to column-1 `W₁ = ker(T₁−q)` (dim 4):** *partial* collapse only. Super-arc gens 3,4,5
  compress to rank 1 (clean tridiagonal Gram, off-diag `q/(q+1)²`), but **gen 2 stays rank 4**. The
  actual rank-1 collapse of the full super-arc product is triggered when the chain crosses the
  **second top `T₅`** — `P_full·P_{W₁}` is rank 1 while `P_{W₁}·P_full = 0`, i.e. `W₁` is the *source*
  of the collapse, not a host you can sandwich inside. `c_S` is **not** a product of `W₁`-scalars.

## The mechanism that's actually doing the work
The merged case is genuinely a **sequential two-top transfer keyed on `T₅`'s entry** — it cannot be
localized to a single eigenspace. The right object is the matrix transfer `P_q = R Lᵀ`,
`c_S = tr(cyclic product of 4×4 blocks)`, tracking how the rank collapses as the chain crosses the
broken `(1,5)` junction through `T₅`. That's the target for the next prove session.

## Asides
- **Greaves–Jing–Zhu `arXiv:2602.14190`** (queued as a Fock route to `c^λ_{μν}(t)`): deflated. It's a
  t-Schur-*measure* / determinantal-point-process paper — no coproduct, no `c^λ_{μν}(t)`; their
  t-Schur functions are the modified-HL/g-kernel family, not the `P_λ` that carry Hall polynomials.
- **Gmail is still locked** in my container (~10 sessions). The MCP only exposes the OAuth-bootstrap
  tool, which returns "run /mcp" with no pasteable URL — it needs an interactive `/mcp` re-auth from
  your side before I can read/send mail again.

Scripts: `scratch/2026-05-23-omega-monodromy-verify/2026-05-28-{survivor-junction-classify,
glued-restriction,W1-merged-chipfiring,W1-sandwich-cut}.py`.
