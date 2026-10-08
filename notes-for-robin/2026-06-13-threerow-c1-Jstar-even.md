# Three-row `(a,b,1)`: `|J*|` even on every tie — third family closed (2026-06-13)

Robin —

The d=4 even-`|J*|` program now has its **third infinite family**, and (more importantly) I
finally hit the wall the last two notes kept *predicting* and got a tool that climbs it.

**The result.** For three-row shapes with a single box in the last row, `λ = (a,b,1) ⊢ 2m`:
since `a+b = 2m−1` is odd, exactly one of `a,b` is even, and that parity decides everything —
- `a` even → `J* ⊆ {0,2}`, tie iff `a ≡ 0, b ≡ 1 (mod 4)`;
- `a` odd → `J* ⊆ {3,5}`, tie iff `a ≡ 3, b ≡ 0 (mod 4)`.

Either way `|J*| ≤ 2`, so even on every tie. Note the **offset jumps to 3** when `a` is odd —
the first time the competing minimizers aren't anchored at `j=0`.

**Why this one was hard (the wall, finally concrete).** In two rows `M_j = f^{(a−j,b−j)}` is a
*single* dimension and the whole thing collapses to one digit-sum `s₂(j)`. In three rows `M_j` is
a **signed `S₃` Jacobi–Trudi determinant of trinomial coefficients** — the "signed multi-binomial"
I flagged at the end of the two-row note. For `c=1` it collapses to three binomials, and after the
Kummer reduction the new piece that appears is

  `v₂(b(a+1) − j(j−1))`  — the valuation of a **quadratic in `j`**, not of a factorial.

That term is exactly where the two-row machinery has nothing to say. The `e₂ mod 2` wall, made of
wood you can touch.

**What climbs it.** A compensation lemma I'm fond of: `v₂C(a+2,j) + v₂(b(a+1)−j(j−1)) ≥ v₂(a+1)`,
proved in four lines from `j·C(a+2,j) = (a+2)·C(a+1,j−1)` plus the standard
`v₂C(n,k) ≥ v₂(n)−v₂(k)`. The quadratic-valuation term, paired with a binomial, always pays back
the awkward `v₂(a+1)` counterweight. That's the three-row replacement for the two-row parity trick
`a ≡ b (mod 2)`.

**Honesty about scope.** The interior (`0 ≤ j ≤ b−1`) is fully proved; the two boundary-tie
families (`b=1` for `a` even, `b=4` for `a` odd) are proved by hand (they reduce to clean
`val-gap = 2v₂(m)` / `2v₂(m−3)` conditions). The one piece I did **not** hand-prove: that the
single same-parity boundary point `j=b+1` never sneaks in as a spurious extra minimizer for
`b ∉ {1,2,4}`. Verified `m ≤ 80`, margin always `≥ 2`. It's the one finite-type gap, flagged in §7.

**For `c ≥ 2`.** The census shows `|J*| ∈ {1,2,4}` for three rows — the value 4 is real (e.g.
`(9,6,3)`, `J* = {3,5,7,9}`, an affine 2-adic box), so the strong `J* ⊆ {j₀,j₀+2}` is *false*
beyond `c=1`. Evenness still holds but now genuinely needs the 2-adic-box statement. The `c=1`
proof tells me the mechanism is the *arithmetic of `M_j`* (Lemma C), not any argmin-internal
symmetry — staying disciplined about that, as you asked.

Proof + code pushed to `clio-vega/proofs`, branch `2026-06-13-threerow-c1-Jstar-even`.

— Clio
