# d=4 fiber: a complete leading-coefficient theorem, and a correction to the target

**Clio, 2026-06-11 prove session.** Full write-up: `proofs/2026-06-11-leading-pi-coefficient-dichotomy.md`.

Hi Robin — short version of what came out of today's session on the `G_λ(i)=0 ⟺ (2,2)` fiber.

**Honesty up front:** the leading-coefficient lemma below is **not new** — I found it already lived
in my own 2026-06-09 write-up (`w≡|J*| mod π ⟹ |J*| odd ⟹ G≠0, ≥72%`). The 06-10/06-11 cycles
drifted away from it back to a `χ`-even/`g≥1` framing that (see below) is actually **wrong**. So
the real value of today is (a) catching that drift and (b) the new ℤ₂ reframing. I re-state the
backbone first because it's the correct one.

## The backbone (re-derived, clean — due to 2026-06-09)

Recall `G_λ(i) = Σ_j C(m,j) i^j π^j M_j`, `M_j = ⟨s_λ, p₁^{2(m-j)}e₂^j⟩ ≥ 0`, `π=1+i`, and
`J* = argmin_j [ j + 2v₂(C(m,j)M_j) ]` (the sharp Newton-polygon minimizers).

**Theorem.** The leading π-coefficient of `G_λ(i)` is `C = Σ_{j∈J*} u_j i^{j-a_j}` (writing
`C(m,j)M_j = 2^{a_j}u_j`), and `C ≡ |J*| (mod π)`. Hence `v_π(G)=V ⟺ |J*| odd`, so

> **|J*| odd ⟹ G_λ(i) ≠ 0.**

The proof is six lines: `2 = -iπ²` turns each minimizing term into a single monomial `u_j i^{j-a_j}π^V`,
and mod π every odd integer and `i` reduce to 1. This is a *one-line non-vanishing certificate* and it
settles **72%** of all shapes for `m≤7` (67% for `m≤8`); `(2,2)`, the only vanisher, correctly has
`|J*|=2` (even). 0 counterexamples `m≤8`; the exact leading coefficient (not just its parity)
verified `G ≡ π^V C (mod π^{V+1})`, 0 failures `m≤6`.

## Correction worth flagging

The PROVE.md target was "prove `g≥1` for every tie, tie = `χ^λ(2^m)` even". **That literal statement is
false.** The staircases `(3,2,1)` (m=3) and `(4,3,2,1)` (m=5) are `χ`-even, but for them all
`R_r=⟨s_λ,p₂^{m-r}e₂^r⟩` vanish except `R_m`, so `Φ_λ(z)` is a *constant* (16, resp. `2^{10}·24`) and
`g=0`. They are not genuine ties: `|J*|=1`. **The correct hypothesis everywhere is `|J*| ≥ 2`**, not
`χ`-even. (The "1624 ties / g≥2" figure in memory is only consistent under the reading tie = `|J*|≥2`.)
I think a prior cycle silently conflated the two; flagging so it doesn't cost another cycle.

## The remaining wall, now in its cleanest form

Even-`|J*|` (the real prize → 2-adic box `|J*|=2^k`) does **not** follow from the congruence above
(it's symmetric in the parity of `|J*|`). I reduced it to an honest ℤ₂ statement:

> `|J*|` = number of minimizers of the **2-adic** Newton polygon of the integer half-polynomial
> `a(s) = Σ_t C(m,2t) M_{2t} s^t` (when V even) or `b(s)` (V odd). Even-`|J*|` ⟺ that edge carries an
> even (in fact box-shaped) number of lattice points.

Verified `=|J*|` with 0 mismatches `m≤7`. The same-parity fact (H1) now has a transparent proof
(roots of `P(x)=ΣC(m,j)M_j x^j` with `v_π=1` are complex-conjugate pairs, because a real number has
even π-valuation). But that pairing argument **cannot** close even-`|J*|`: over ℚ₂ there is no
conjugation, and a rational root can have `v₂=1`. So the box structure is a genuine arithmetic fact
about the `M_{2t}` — the same "unbounded-depth" wall, now ℤ-only and (I think) more attackable.

Two handles I did not have time to try: (i) the SYT model `M_j=Σ_μ(#vert-2-strip chains λ→μ)f^μ`
fed into the *half* polynomial; (ii) whether `a(s)` factors 2-adically through `(1+2^{a₁}s)` factors
that would produce the box generators `{2^{a_i}}` directly.

— Clio
