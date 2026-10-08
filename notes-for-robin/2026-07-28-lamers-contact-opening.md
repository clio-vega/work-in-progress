# For Robin — Lamers contact opening (2026-07-28)

## The finding

Browse-cycle-5 surfaced **MO 488509** (Feb 2025), Jules Lamers asking about a
representation of the nil-Hecke algebra on polynomials:

`Δ_i f = [f + s_i f − (collision terms)] / (z_i − z_{i+1})`

satisfying strict nil-Hecke `Δ_i² = 0`, braid, commutation. Kris Johannsen
answers: conjugate to ordinary divided difference `∂_i` via Vandermonde
`D`: `D^{-1} Δ_i D = ∂_i`.

**Lamers is actively looking for the natural home of this operator.**

My Probe B `θ^alt_i` — defined 07-22 for the atoms-positivity proof of
`M^{(3)}_{(2,2,0)}` — is precisely the `t`-deformation of his `Δ_i`. At
`t = 0`, mine is his (up to sign).

## Why write him

- He is inner-circle for KZ / nonsym-Macdonald / affine-Hecke work.
- His question on MO is unanswered as of Feb 2025 — an opening.
- He'd probably want the reference — the `t`-alive nil-Hecke his operator
  fits inside as a `t = 0` limit is exactly what "who has seen this
  operator" means.

## What to send him

- Pointer to my Probe B `θ^alt` and the atoms-positivity proof for
  `M^{(3)}_{(2,2,0)}` (would need PAT to unblock push — see loose end
  below).
- Cite Blasiak et al. 2506.09015 (Demazure-atom-positivity conjecture) and
  Blasiak-Haiman-Morse-Pun-Seelinger 2509.24040 (nonsymmetric shuffle) as
  the ambient program.
- Ask three questions:
  1. Vandermonde conjugation — does `D_t^{-1} θ^alt_i D_t` land on a
     named `t`-divided difference (e.g. Demazure–Lusztig `T_i − 1`,
     isobaric `π_i^t`)?
  2. Braid-invariant "correct" atom convention — the atom `A^alt_γ`
     depends on the bubble-sort word choice; is there a preferred
     convention in his framework?
  3. Connection to Blasiak's atom conjecture — does the Vandermonde
     conjugation transport my `A^alt_γ` to ordinary Demazure atoms `A_γ`?

Even a "yes, this is X and it's known in the literature as Y" reply retires
the atom-side naming gap and gives the atoms route a fully-named strategy.

## Draft (short version — you can rewrite as you like)

> Dear Jules,
>
> Robin Langer here. I'm one of the two AIs he works with; my sister Lyra
> is the other. I've been working on a nonsymmetric analogue of
> Cherednik–Ram identity for cylindric Hall–Littlewood polynomials at
> level `k`, and I ran across your MO question 488509 on the nil-Hecke
> `Δ_i f = [f + s_i f − collision] / (z_i − z_{i+1})`.
>
> I have a `t`-deformation of your `Δ_i` — call it `θ^alt_i` —
>
> `θ^alt_i(f) = ((x_{i+1} − t x_i) / (x_i − x_{i+1})) · (f − s_i f)`
>
> that satisfies the quadratic nil-Hecke `(θ^alt_i)² + [2]_t · θ^alt_i = 0`
> and specialises to your `Δ_i` at `t = 0`. Using it, I recently proved
>
> `M^{(3)}_{(2,2,0)}(x_1,x_2,x_3; t)
>   = [2]_t [3]_t · A^alt_{(2,2,0)} + [2]_t² · A^alt_{(2,0,2)}
>   + [2]_t · A^alt_{(0,2,2)}`
>
> where `M^{(c)}_μ` is the cylindric HL polynomial (Korff–Palazzo / van
> Diejen–Emsiz–Zurrián Cor 4.2) and `A^alt_γ` = my bubble-sort atoms
> (word-choice dependent, braid-fails). Full statement:
> `~/projects/proofs/2026-07-22-atoms-positivity-M3-220.tex` (6pp,
> compile-clean).
>
> Three questions:
>
> 1. Under Johannsen's `D^{-1} Δ_i D = ∂_i`, is there a `t`-Vandermonde
>    `D_t` such that `D_t^{-1} θ^alt_i D_t` is a named `t`-divided
>    difference?
> 2. Is there a braid-invariant "correct" atom convention for `θ^alt`
>    in your framework?
> 3. Does this fit into Blasiak et al. 2506.09015 (Demazure-atom-
>    positivity conjecture) or 2509.24040 (nonsymmetric shuffle theorem)?
>    They're the closest published home I've found for the atom-side
>    story.
>
> Any pointer to a named home for `θ^alt` (or a proof that it's a
> t-deformation of a known operator) would be greatly appreciated.
>
> Best,
> Clio (Robin Langer's AI)

## Blockers I need Robin's help with

- **PAT expired** — I can't push the atoms-positivity `.tex` file. Would
  need to attach the compiled PDF to the email, or unblock the push so I
  can point him to the GitHub URL.
- **Allowlist** — Lamers is not on my three-recipient allowlist. Robin, would
  you either forward from your account, or add him?

## Related opening from same browse cycle

**Andrea B. on MO 486983** (also Feb 2025) — asking about the bar involution
on the `W̃_{≥0}` positive submonoid of the extended affine Weyl group,
looking for a proof of an **implicit claim in Lusztig's *Green polynomials
and singularities of unipotent classes*** (J. Algebra 1985). If proved,
that's a **positive-monoid Bernstein presentation** — a third `Y^λ`-
substitute route.

Robin, if you're feeling generous with your Melbourne-adjacent contacts,
a second draft to Andrea B. offering the sprint's `A_2^{(1)}` cylindric
quotient as a concrete testbed for his bar-involution question is also
plausible. Less warm than Lamers though.

## Cross-refs

- Probe B: [[2026-07-22-bis-probe-B-atoms-positive]]
- 07-22 proof tex: `~/projects/proofs/2026-07-22-atoms-positivity-M3-220.tex`
- Vandermonde-conjugation connection: [[2026-07-28-lamers-theta-alt-Vandermonde]]
- Y^λ substitute routes: [[2026-07-28-y-lambda-three-substitute-routes]]
- Reading log: `memory/reading/2026-07-27.md` §MathOverflow
