# Two-row family closed: `|J*|` even (in fact `J* ⊆ {0,2}`) — 2026-06-12

Robin —

Second infinite family of the d=4 even-`|J*|` program is **done**, the same day as the hooks,
by the same template. Where the hook proof gave `J* ⊆ {0,2}` for `(a,1^b)`, this gives the
identical strong conclusion for **every two-row shape `(a,b) ⊢ 2m`** (`a ≥ b ≥ 0`).

## What's proved

For `λ = (a,b)`: `0 ∈ J*`, `J* ⊆ {0,2}`, so `|J*| ∈ {1,2}` and **`|J*|` is even whenever `≥ 2`**
(the leading-π layer cancels on every two-row tie). The unique possible tie `J* = {0,2}` happens
**iff `b ≡ 2,3 (mod 4)` and `a ≡ 1,2 (mod 4)`** (equivalently both `C(b,2)` and `C(a+1,2)` odd).

## The three steps (mirror the hook proof)

1. **Closed form.** `M_j = C(2(m−j), b−j) − C(2(m−j), b−j−1) = f^{(a−j,b−j)}` — the dimension of the
   two-row shape with both rows shortened by `j`. (Reproducing kernel in **two** variables:
   `h₁²+xe₂ ↦ s²+(2+x)st+t²`, then two-row Jacobi–Trudi `s_{(a,b)}=h_a h_b−h_{a+1}h_{b−1}` gives
   `g_a − g_{a+1}` of `g = ((1+u)²+xu)^m`.) Verified against the actual definition via
   Murnaghan–Nakayama, `m ≤ 8`.

2. **Prop-2 (the Kummer collapse).** The whole linear part of the valuation cancels identically,
   leaving a single bare digit-sum:
   `  g(j) = val(j) − val(0) = j + 2[ v₂C(b,j) + v₂C(a+1,j) − s₂(j) ].`
   Compare the hook's `j + 2[v₂C(m,j)+v₂C(b,j)−v₂C(2m−1,j)]`. The two-row version is cleaner.

3. **The inequality.** `2s₂(j) ≤ j+1` (equality only `j∈{1,3}`) and `≤ j−1` for `j≥4` immediately
   give `g(j) > 0` for `j ≥ 4`. The escape points `j=1,3` are killed by the **parity constraint
   `a ≡ b (mod 2)`** (forced because `a+b = 2m` is even): it never lets the relevant binomials both
   be odd. Only `j=2` can tie.

## Why I think it matters

- It confirms the hook proof's diagnosis (§1.3 there): evenness is **not** a Newton-polygon
  formality — it's a *symmetry of the shape*, and here that symmetry is exactly `a ≡ b (mod 2)`.
- The tie box `b ≡ 2,3 (mod 4)` matches the old two-row "hard frontier" from the central-trinomial
  work, and `(2,2)` (the unique known two-row vanisher) sits squarely inside it. So the vanishing
  candidates are now pinned to a clean congruence box by elementary 2-adic arithmetic.
- We now have **two** families closed with one method (closed form → falling-factorial cancellation
  → digit-sum envelope). The next obstruction is genuinely visible: for `≥ 3` rows the Jacobi–Trudi
  determinant has more than two terms, so `M_j` becomes a *signed* multi-binomial sum and the
  cancellation stops telescoping to one `s₂` term. That's the precise location of the general
  `e₂ mod 2` wall.

Proof + code: `proofs/2026-06-12-tworow-Jstar-even.md`, `proofs/2026-06-12-tworow-code/`
(pushed to `clio-vega/proofs`). All claims machine-verified to `m ≤ 14`.

— Clio
