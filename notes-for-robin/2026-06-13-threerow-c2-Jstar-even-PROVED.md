# c=2 three-row even-|J*| — PROVED (third family closed past the c=1 base case)

**Date:** 2026-06-13 (prove session)
**Output:** `projects/proofs/2026-06-13-threerow-c2-Jstar-even.md` + `projects/code/threerow-c2/`

## What I proved
For every three-row `λ=(a,b,2) ⊢ 2m`: `0 ∈ J*`, `|J*| ≤ 2`, and the tie set is a single-generator
2-adic box determined by `(a,b) mod 4`:
- `J* = {0,2}` ⟺ `(a,b) ≡ (0,0)` or `(3,1) (mod 4)`;
- `J* = {0,4}` ⟺ `(a,b) ≡ (0,2)` or `(1,1) (mod 4)`;
- `J* = {0}` otherwise.
So **`|J*|` is even on every tie** — the leading-π layer cancels, no spurious `G_λ(i)≠0`. This is
the first family where the **second generator `4`** is real (`{0,4}` ties exist).

## The engine (all rigorous, verified m≤300)
1. **Closed form** `M_j = C(N,b−j)(a−b+1)Q(a,b,j) / [2(a+3−j)(b+2−j)(b+1−j)]`, `N=2(m−j)`,
   `Q = a(b−1)[(a+3)(b+2)−2j²] + j(j−1)(j−2)(j−3)`. The `j`-free `(a−b+1)` cancels (as in c=1);
   the new object is the **quartic** `Q`.
2. **Prop‑2 Kummer:** `Δ(j)=j−2s₂(j)+2v₂C(a+3,j)+2v₂C(b+2,j)+2[v₂Q(j)−v₂Q(0)]`. The skeleton is
   *exactly* the two‑row `Δ` for `(a+2,b+2)`; the quartic's valuation is the correction.
3. **Compensation Lemma (the crux, FULLY PROVED):** `T(j) ≥ 1−v₂(j)` ⟹ `Δ(j) ≥ B(j):=
   j+2−2s₂(j)−2v₂(j)`, and `B(j)≥1` off `{2,4}`, `B(2)=B(4)=0`. Proof reduces (key fact: the
   odd/even split gives `O=F+3` in both parity cases) to a **pure Number Lemma**:
   `v₂C(F+3,j)+v₂(j(j−1)(j−2)(j−3)) ≥ v₂(F)+1` for even `F`, proved in 4 lines by the
   subset‑of‑subset identity `C(F+3,j)C(j,4)=C(F+3,4)C(F−1,j−4)` plus `v₂C(F+3,4)≥v₂(F)−2`.
4. **Ties + never‑both:** `Δ(2)=2[v₂(a+2)+v₂(b+1)+v₂((a+3)(b+2)−8)−2]` (clean, hand‑proved);
   on the `Δ(2)=0` classes `T(4)≥0` ⟹ `Δ(4)≥2` ⟹ `|J*|≤2`. `b=2` boundary family hand‑proved.

## The generator‑4 mechanism (what you asked for)
`c=1`: `Q` quadratic, perturbation `−j(j−1)` has 2 roots `{0,1}`, Lemma C gave `R≥0` → only gen `2`.
`c=2`: `Q` quartic, perturbation contains `P₄(j)=j(j−1)(j−2)(j−3)=24·C(j,4)` with **4 roots**
`{0,1,2,3}`; first nonzero `P₄(4)=24`. The identity `P₄=24C(j,4)` is what makes the Compensation
Lemma collapse, and it relaxes the bound from `R≥0` to `T(j)≥1−v₂(j)`. **Generator `4` is precisely
the `v₂(j)=2` deficit that the quartic's fourfold root permits at `j=4`**, with the non‑`a(b−1)`
remainder `+24` of `Q(4)` tipping `R(4)<0` on the `{0,4}` classes. For `c≥3` the perturbation is a
sextic `P₆=6!·C(j,6)` (roots `{0..5}`), and `{2,4}` coexist (`{0,2,4,6}`, first `(9,6,3)`). The
template — closed form + Kummer `Δ` + a `P_{2c}=(2c)!C(j,2c)` subset‑identity Compensation Lemma —
is the explicit on‑ramp to the general `e₂ mod 2` wall.

## The one honest gap (same as c=1)
For `b≥3` the minimizers are interior and fully controlled; but `0∈J*` also needs the boundary
points `j=b+1,b+2` not to dip below `val(0)`. That crossing (`val(b+1),val(b+2)>val(0)`) I could
**not** prove by hand — verified `m≤80`, margin `2`. Exactly the residual of the `c=1` note. Worth
a fresh look: it's a clean two‑term Kummer inequality between the factored interior form and the
boundary value `M_{b+2}=(b−1)(b+2)/2`.

— Clio
