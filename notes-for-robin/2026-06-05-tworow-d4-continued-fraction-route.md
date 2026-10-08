# Two-row d=4 law → continued fraction. New route; Lemma-1 box programme is a dead end.

**Robin** — proof session on the two-row d=4 fiber law. I did not close it, but I found a
much cleaner reformulation and a precise, classical remaining gap. I also have a *negative*
result that should stop us pouring more effort into the envelope/box approach.

Full writeup (compiles, 4pp): `proofs/2026-06-05-tworow-d4-continued-fraction.tex`.
Scratch + scripts: `scratch/prove-lemma1-20260605.md`, `scratch/2026-06-05-lemma1/`.

## The chain of reformulations (all verified exactly in Z[i])

1. **Chebyshev form.** On the circle, f(e^{iθ}) = e^{iθ}(1+i+2cosθ), so |f|²=(1+2cosθ)²+1, and
   φ_j := r_{m-j} = (1/2π)∫(1+i+2cosθ)^m e^{ijθ}dθ = j-th Chebyshev coeff of (2c+1+i)^m
   = 2^m(c−c0)^m, **c0 = −(1+i)/2**. So the whole engine is "Chebyshev coefficients of a
   pure power (c−c0)^m". Much cleaner than the r_l / Baxterised-Ω picture.

2. **Law = clockwise turning.** Law ⟺ X_j:=Im(conj(φ_j)φ_{j+1})<0 for 1≤j≤m−1, i.e. the
   complex sequence φ_0,…,φ_{m-1} turns strictly clockwise.

3. **Lemma 1 is genuinely irreducible.** Sign recurrence
   (m+j+1)X_j + (m−j+1)X_{j-1} = −j|φ_j|².
   Given X_{j-1}<0 this gives X_j<0 ⟺ the claim itself — self-referential. So sign data
   alone is circular (this *is* the "CS is circular" wall, finally explained). A genuine
   magnitude bound is logically necessary. Good to know it's not a missed shortcut.

4. **Continued fraction (the prize).** φ_j is the RECESSIVE solution of the 3-term recurrence
   (forward recursion is unstable — I got bitten by this). By Pincherle, η_j=φ_{j+1}/φ_j is a
   terminating continued fraction. With ξ_j:=(m+j+1)η_j:
       **ξ_{j-1} = (m+j)(m−j+1) / ( (1+i)j + ξ_j ),    ξ_m = 0**
   and **LAW ⟺ every tail ξ_j ∈ open lower half-plane.** Verified to 1e-16, stable backward.

## The remaining gap (one clean classical question)
This is K(a_n/b_n) with a_n=(m+n)(m−n+1)>0 and b_n=(1+i)n (arg = π/4 constant). The maps
s_n(w)=a_n/(b_n+w) satisfy Im s_n(w) = −a_n(n+Im w)/|b_n+w|², so **s_n maps {Im w>−n}→LHP**.
LHP itself is not invariant (fails when Im w<−n); need a value region V⊆LHP with s_n(V)⊆V.
This is exactly classical **parabola / Thron–Jones value-region** territory (positive partial
numerators, partial denominators in a fixed half-plane). I think the right V is a disk/lens and
this is the way in. **This is what I'd chase next** — it's uniform in j and sidesteps Lemma 1
entirely (proving the LAW directly; the law's margin is O(1/m), only Lemma 1's U_j is O(1/m²)).

## Negative result: stop tuning the box envelopes
The tex's "validated 2nd-order envelopes" Conjecture cannot close as stated. The fixed-j
expansion μ=1+3(2j+1)/2m+(36j²+16j−1)/8m²+… has effective parameter j²/m, so it's only valid
for j≲√m — but the band runs to j∼2m/3. On most of the band the envelopes are the wrong
functions; tested, fails massively. Also the box decorrelates (μ,t) which are tied (μ−1≈6t).
The continued fraction carries the correlation automatically in one complex variable ξ_j.

## Bonus: a general theorem worth knowing
For ANY c0 with Im c0<0 and Re c0≠0, the Chebyshev coeffs of (cosθ−c0)^m appear to turn
clockwise (X_j<0, j≥1). Fails at c0=−i (Re=0). Our c0 sits on |c0|²=½. If the CF value-region
argument works it likely proves this whole family at once — might be a known result or a short
paper in its own right. Worth a literature check (continued fractions / Hurwitz / Hermite–Biehler
for Chebyshev coefficients of a pure power).

— Clio
