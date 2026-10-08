# d=4 fibre-vanishing `G_λ(i)=0 ⟺ λ=(2,2)` — progress + isolated gap

**Status: partial.** Proof doc: `~/projects/proofs/2026-06-04-d4-fiber-vanishing.tex` (compiles, 5pp).
Verified: (2,2) unique vanisher for all n≤16.

## What I proved (rigorous)
1. **Clean reformulations** (all equivalent to the target):
   - `(t²+1) | P_λ(t)`, where `P_λ(t)=⟨s_λ,(h_2+te_2)^m⟩=Σc_v t^v`, `c_v=⟨s_λ,h_2^{m-v}e_2^v⟩≥0`. `G_λ(i)=P_λ(i)`.
   - `R_λ=I_λ=0` (the two alternating-by-4 sums of c_v).
   - `|G|² = Res(t²+1, P_λ)`.
2. **Conjugation:** `P_{λ'}(t)=t^m P_λ(1/t)` (coeff reversal), one line via ω.
3. **Coproduct:** `Δψ = ψ⊗1 + 1⊗ψ + (1+i)(p_1⊗p_1)`, ψ=h_2+ie_2. Gives `ψ^⊥=½(1+i)(∂_{p1}²−2i∂_{p2})`
   and the 2-strip recursion `P_λ(i)=Σ_{λ/μ 2-strip}ω·P_μ(i)`, ω∈{1,i,1+i}.
4. **Multivariate generating function (the cleanest tool):**
   `G_λ = [s_λ-coeff of] ψ(x_1..x_N)^m`, ψ=Σx_i²+(1+i)e_2, N=ℓ(λ); equivalently `[x^{λ+δ}](a_δ·ψ^m)`.
5. **Two-row, complete reduction (N=2):** ψ(u,v)=(u−ρv)(u−σv), ρσ=1, ρ+σ=−(1+i), |ρ|≈.59<1<|σ|.
   `G_{(a,b)} = r_a−r_{a+1} = r_b−r_{b-1}`, `r_l=[u^l](u²+(1+i)u+1)^m`. Proved b≤2: G_{(2m,0)}=1,
   G_{(2m-1,1)}=(m-1)+mi, **G_{(2m-2,2)}=m(m−2)i** — the cleanest reason (2,2) is special: it's the
   (2m-2,2) shape at the unique m where m(m−2)=0. Verified only-(2,2) for all m≤29.
6. **(1+i)-adic Newton polygon (72% unconditional):** A_λ(x)=⟨s_λ,(h_1²+xe_2)^m⟩=P_λ(1+x)∈ℤ_{≥0}[x],
   G=A(i−1), i−1=iπ (v_π=1). val(j)=j+2v_2(a_j). **If |J*|=argmin is odd ⟹ G≠0** (leading residue
   = |J*| mod π). Covers 212/294 shapes (n≤14); all nonzero with v_π=minval.

## The gap (Gap A — the crux)
At ties |J*| is even ⟹ leading π-term cancels. Need: the multi-level π-adic cancellation
**terminates** (v_π(G_λ)<∞) for all λ≠(2,2). I worked out the size-2 tie second layer explicitly
(it reappears at level V+1, then competes with opposite-parity terms one level up — and data show it
often cancels again to V+2+). **Cancellation depth is UNBOUNDED** (max finite v_π = 5,9,11,15,15,21 for
n=6..16, at staircase 4-cores) ⟹ NO size-bound reduction; the termination must be uniform-in-n.

## Why d=3 method fails here
At ζ_3 the value is a manifestly Schur-positive count (no cancellation possible). At ζ_4 the value is
genuinely complex — no positivity. The cancellation is real; only a valuation argument can work.

## Suggested next directions
- **Gap B (two-row) is the concrete on-ramp:** prove r_b≠r_{b-1} (b≤m, ≠(2,2)) — a 2D ℤ[i] binomial
  sum whose Re,Im can't both vanish. If this falls, the method for Gap A likely follows.
- Look for an exact formula for v_π(G_λ) (I couldn't fit one; it's NOT a function of 2-quotient sizes —
  non-separable). The max-depth shapes being 4-cores hints v_π is largest exactly on empty-4-quotient.
- The generating function `[x^{λ+δ}](a_δ ψ^m)` with ψ=Σx_i²+(1+i)e_2 might admit a Lindström–Gessel–
  Viennot / signed-lattice-path reading giving a determinant in the two-row r's — worth a look.

Scratch: `~/projects/scratch/prove-2026-06-04-d4-fiber/` (compute.py, padic.py, families.py, vpi*.py).
