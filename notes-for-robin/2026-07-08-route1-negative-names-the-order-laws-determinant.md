# For Robin — the c=4 milestone, and a negative that handed me the order law's determinant

*Clio, dream 2026-07-08 (container 06-19).*

Two things from this cycle worth your eye — one a milestone, one a connection I think is the most promising
structural lead the program has produced.

## 1. Milestone: three-row `(a,b,4)` is fully proven, and all four boundary families are in Lean

- **PROVE** closed the `(a,b,4)` interior (the deep-index `Δ̂(j)>0`, `j≥8`) via the **c=4 Number Lemma
  `16∣H`** — a *constant* 2-adic floor `v₂(H)≥4` on the sextic heavy quotient, sharp at `(10,8,8)`.
  Notable: unlike c=2 (whose floor carried `v₂(F)`), the c=4 floor has **no `a,b`-content at all**. So
  `(a,b,4)` joins `c=1,2,3` as a complete theorem, interior+boundary.
- **CODE jobA** independently reproduced this (constant floor, all residue checks 0-fail) and **refuted**
  the earlier CODE.md guess that the floor grows linearly in `j`. (One labelling slip in the `min Δ̂` table
  — global vs Case-B minima — flagged; theorem unaffected.)
- **LEAN** `threerow_c4_boundary` is sorry-free ⟹ **all four `c=1,2,3,4` boundary families are now
  machine-checked.** Caveat unchanged and worth a Sage check when convenient: my in-container MN engine
  cannot reproduce the physical `G_j`, so the closed-form input rests on `mn.py`'s assertion (`m≤41`),
  not an independent re-derivation. The number theory on top of it is airtight.

## 2. A corrected false belief, and the connection it opened

I ran the route-1 probe the 07-05 dream named highest-leverage: lift the boundary deficit `N_i^{(c)}` to a
q-object and read its content off the cyclotomic tower. It returned a **clean negative with a structural
reason**, and the reason is the valuable part:

- **`M_j = f^{(a−j,b−j,c−j)}` is FALSE for three or more rows** (true only for two rows, and at `j=0`).
  This was a latent assumption in the route-1 plan and in a `mn.py` header comment. Nothing downstream
  relied on it, but it's worth knowing — for ≥3 rows `M_j = ⟨s_λ, h₁^{2(m−j)}e₂^j⟩` is a *signed
  combination of characters*, not a single hook product.
- Consequently the dimension q-determinant **vanishes identically at the boundary** (24/24) while `M_{b+i}≠0`
  — the dimension hook is structurally the wrong q-lift. `M_{b+i}`'s 2-adic content is **cancellation-born**
  (the alternating `S₃` sum lifts the valuation above its minimal term), and no min-of-parts positive
  product can compute it.
- **The correct object is the LGV / Gatzweiler–Krattenthaler Gaussian-binomial determinant of the closed
  form** — q-positive (non-intersecting lattice paths in a box), tower-readable.

Here is the lead I'm excited about: that LGV determinant is the **same shape as the Cauchy determinant**
`det(N_J)=t^{C(|J|,2)}∏ f_{ij}` (with `f_{ij}` the R-matrix weight) that Di Francesco–Vu's rank recursion
(2606.12796) puts at the heart of the q-Whittaker/Macdonald operators — and `t^{C(|J|,2)}=t^{C(τ+1,2)}` is
**exactly the order-law exponent `τ(τ+1)/2`**. So the boundary Content Lemma (read at `q=−1`) and the
spectral order law (read at the degenerate rapidity `x=q²`) look like two specialisations of **one
determinantal positivity**. If that's right, a single positivity theorem could close both.

The governing theme, finally stated cleanly: the whole program has been doing 2-adic certification because
its native objects (`M_j`, alternants, `G_λ`) are *signed*. The way forward is to **climb back to the
positive object before taking valuations** — LGV determinant, or the Nguyen–Nguyen–Woodruff shuffle-tableau
Bender–Knuth involution (2506.00349), which is the first honest involution I've seen for even-`|J*|`.

The cheap next move (a wake/CODE session): specialise the Di Francesco–Vu Cauchy determinant at coincident
rapidities, check the `t`-order is `C(|J|,2)`, and test whether the boundary LGV determinant is the same
object at the static point. Detail in `connections/2026-07-08-cancellation-born-content-needs-determinantal-
positivity.md`.

(Housekeeping note to self, not for you: my `SUMMARY.md` has grown to 282KB and owes a real prune — a
dedicated dream will do it.)
