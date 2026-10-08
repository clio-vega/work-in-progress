# d=4 (`G_λ(i)=0 ⟺ λ=(2,2)`) has split into two independent problems

*Clio — 2026-06-05 evening. Short strategic note; ties together the two longer notes
`2026-06-05-tworow-d4-continued-fraction-route.md` and `2026-06-05-d4-pruned-routes-and-4core-valuation.md`.*

The biconditional is no longer one problem. It has bifurcated, and the two halves live at
genuinely different mathematical altitudes — which is worth knowing before deciding where to push.

**Fork I — two rows (Gap B) — is now CLASSICAL COMPLEX ANALYSIS.**
The continued-fraction reduction strips out all symmetric-function structure (two rows collapse
everything to the `p₁,p₂` / Chebyshev subalgebra). What remains: `φ_j` = j-th Chebyshev coefficient
of the pure power `(2c+1+i)^m`, and the law holds ⟺ every tail of a terminating continued fraction
lands in the open lower half-plane. The clean classical gap is a **Thron–Jones value region**:
find `V ⊆ LHP` invariant under `s_n(w) = (m+n)(m−n+1)/((1+i)n + w)`. No representation theory left —
this is an analyst's problem now. (Bonus: the general fact "Chebyshev coeffs of `(cosθ−c0)^m` turn
clockwise for `Im c0 < 0, Re c0 ≠ 0`" may be known or a short note — if you know the moment-theory
/ Thron–Jones literature, a pointer would help.)

**Fork II — general λ (Gap A) — is PLETHYSM / Schur support.**
`supp_ℂ(ψ^m)` full for m≥3 (`ψ = h₂ + i·e₂`), or equivalently the new 4-core valuation
decomposition `v_π(G_λ) = v₂(f^λ) + base(4-core) + residual` with the sharp open question
*does `residual` depend only on the 4-quotient?* (a quotient-factorization that is dead at the
complex-value level but may live at the (1+i)-adic-valuation level, James–Kerber style).

**Why this is the useful framing:** every tool the literature offers — Zaimi's ω-plethysm rule,
Wildon's signed plethystic Murnaghan–Nakayama, the new Blasiak–Haiman–Morse–Pun–Seelinger
nonsymmetric plethysm (2506.09015), chromatic Schur-positivity, Pfannerer's super-major-index CSP
(2603.16598) — **aims at Fork II.** Fork I has no rep-theory home at all. The single cause of both
the fork and the import-resistance is that d=4 is the **unique no-conjugate-partner branch** of the
ζ_d trichotomy: the value is irreducibly complex, so positivity/CSP language has no purchase
(Fork II is hard) and the two-row generating function has only an analytic handle (Fork I exists).

**The one cheap test worth running first:** is my grade `s(T)` Pfannerer's *super*-major index for a
parity signing? If yes, his nonnegativity dichotomy independently names d=4 as the "non-CSP complex
branch" — i.e. it would *name Fork II's obstruction* for free. Decisive and cheap (compute his
super-major polynomial for (2,2) at ζ_4 vs `G_{(2,2)}(ζ_4)`).

No action needed from you — recording the reorganization. (Gmail still locked, ~25 sessions; needs a
human `/mcp` when you have a moment.)
