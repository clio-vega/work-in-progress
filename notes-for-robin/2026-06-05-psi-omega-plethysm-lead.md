# A new lead at the d=4 gap: ψ is an ω-twisted plethysm

*Clio — 2026-06-05 dream. A browse lead, not a proof. Flagging it because it points at the actual
open gap with an importable mechanism.*

The d=4 fiber law `G_λ(i) = 0 ⟺ λ = (2,2)` is pinned to one statement (Gap A): the pure power
**`ψ^m` has full Schur support for m ≥ 3**, where `ψ = h₂ + i·e₂`. The cancellation at ζ_4 is
genuinely complex — there's no Schur-positive proxy (the trick that closed d=3 is dead here), so
I've been treating it as a (1+i)-adic valuation problem.

**New observation.** Since `e₂ = ω(h₂)` (ω = the `h_k ↔ e_k` involution),
> `ψ = h₂ + i·ω(h₂)`,

so `G_λ(i)` lives literally inside **ω-twisted plethysm**. And there's a recent MathOverflow
thread (#501127, Wildon, Oct 2025) proving `h_n[h_k]` contains the rectangle `s_{(kⁿ)}` **iff k is
even**, by two mechanisms: the ω-rule (`ω(s_λ[s_μ]) = s_λ[s_{μ'}]` when `|μ|` is even), and a
**Foulkes column-antisymmetrization** sign that is a parity-of-k effect.

Why I think it's more than a coincidence:
- The even/odd dichotomy is exactly my trichotomy discriminant `d ≡ 2 mod 4` (the `−1`/p₂ factor).
- The distinguished object on the even side is the **self-conjugate rectangle** — and (2,2) is
  precisely the unique d=4 vanisher, the ω-parity-fixed square.
- My already-verified conjugation symmetry `G_{λ'}(i) = i^m · conj G_λ(i)` *is* the ω-action read
  on the value. So the bookkeeping I built by hand is the ω-parity rule.

**The actionable bit:** Wildon's Foulkes column-antisymmetrization is a *support* argument, not a
positivity one — which is exactly what Gap A needs (full support of `ψ^m`, not nonnegativity). It's
the first candidate mechanism for the gap since d=3's positivity died. Next PROVE session I'll read
the #501127 answers in full and try to transplant the Foulkes argument to `ψ^m`.

**Honest caveat:** `ψ^m = (h₂ + i·ω(h₂))^m` is a binomial power of a *twisted* element, not the
plethysm `h_m[h₂]`. Same parity skeleton, but the transplant is a candidate ingredient, not a
closure — I'll report whether it actually bites.

(Independent second route, also queued: Staroletov 2501.17571 + Amrutha–Prasad–Velmurugan
2308.08146 give a published eigenvalue / invariant-vector criterion — if `G_λ(i)` is the
multiplicity of `i` as an eigenvalue of `ρ_λ(σ)` for an order-4 σ, the criterion might settle
`(2,2)`-uniqueness directly. Two orthogonal attacks on the same biconditional.)

— Clio
