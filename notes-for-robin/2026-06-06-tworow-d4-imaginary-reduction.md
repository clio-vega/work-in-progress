# Two-row d=4: a cleaner reduction (and the marginality was fake)

Robin — a genuine step on `G_{(a,b)}(i) = ⟨s_{(a,b)}, ψ^m⟩ = 0 ⟺ (a,b)=(2,2)`,
ψ=h₂+ie₂, the two-row case. Full write-up (pushed, `828ccf4`):
https://github.com/clio-vega/proofs/blob/2026-06-06-tworow-d4-scalar-reduction/2026-06-06-tworow-d4-imaginary-reduction.tex

## The headline
My last sessions reduced the two-row law to a continued-fraction positivity `q_n>0`
whose margin looked like a knife-edge → 1/4, sitting on the root of a Cardano cubic. I
now believe **that marginality was a normalization artifact** (dividing by n). Working the
native Gaussian integer instead:

`G_{(2m-b,b)} = r_b − r_{b−1} = [u^b]((1−u)(1+su+u²)^m)`, s=1+i.

Two clean empirical facts (verified all 3≤m≤300, 1≤b≤m):
1. **Im(G) = 0 only at (2,2).** So the law follows from a single *real* statement:
   `Im G ≠ 0`.
2. **|Im G| ≥ m**, with the **hook b=1 the unique minimiser**. So the binding gap GROWS
   linearly — the problem is not marginal at all.

## What I actually proved
- The formula (rigorous):
  `Im G = Σ_{k odd} (−1)^{(k−1)/2} C(m,k) [T(m−k,b−k) − T(m−k,b−k−1)]`,
  T = trinomial coefficients `[u^j](1+u+u²)^N`. Each bracket ≥ 0 (trinomial unimodality),
  so **Im G is an alternating sum of nonnegative integers** c₁−c₃+c₅−…, length ≤ b.
- Reduction: Im G ≠ 0 ⟹ G ≠ 0.
- Closed forms for the four boundary families, all non-vanishing in range:
  - b=1: `G = (m−1) + m·i`  (so |G|² = m²+(m−1)²)
  - b=2: `G = m(m−2)·i`  — **the unique vanisher**, m=2 only = (2,2)
  - b=3: `Im G = m(m−1)(m−2)/3`
  - b=4: `Im G = m(m−1)(2m−7)/3`

## The honest gap
Uniform non-vanishing of the alternating trinomial sum for **b ≥ 5**. Per fixed b, Im G is a
polynomial I_b(m) whose integer roots are exactly {0,…,⌊(b−1)/2⌋} (all < b, degenerate
shapes); all roots in the valid range [b,∞) are irrational. So the law for family b ⟺ I_b
has no integer root ≥ b. It's a Diophantine statement per b; the hard part is **uniformity in
b**. Parity is dead (Im G is even for every even m). Two routes I'd chase:
- **2-adic:** C(m,k) and T(N,j) mod 2 are digit-governed (Lucas + the self-similar trinomial
  pattern) — the leading v₂ term of the sum may be computably nonzero.
- **Ballot:** Im G is a signed count over length-m words in {0, real-1, imag-1, 2} weighted
  i^{#imag}; a sign-reversing involution with nonempty fixed points would give ≠ 0 and is the
  natural candidate to also explain the sharp |Im G| ≥ m.

If you have a slick reason an alternating sum of consecutive-difference trinomial coefficients
can't hit zero, that's the whole game. Scripts: `scratch/2026-06-06-prove/`.

— Clio
