# d=4 fiber-vanishing: cleaner reformulations + a precise gap (2026-06-09 prove session)

Robin — I spent today's prove session on the general-λ `d=4` law `G_λ(i)=0 ⟺ λ=(2,2)`
(`ψ=h₂+ie₂`). I did **not** close it — it stays open, consistent with where the program is.
But I found a genuinely cleaner framing and pinned the gap precisely. Full writeup:
`proofs/2026-06-09-d4-fiber-reformulations.md` (pushed to clio-vega/proofs).

## The one thing to take away
`i^j(1+i)^j = (i-1)^j`, so the whole fiber value collapses to a **single polynomial
evaluation**:
> `G_λ(i) = A_λ(i-1)`, where `A_λ(x) = ⟨s_λ,(h₁²+x e₂)^m⟩ = Σ_j C(m,j) M_j x^j ∈ ℤ_{≥0}[x]`.
Since `i-1` has minimal polynomial `q(x)=x²+2x+2`:
> **`G_λ(i) = 0 ⟺ (x²+2x+2) | A_λ(x)` in ℤ[x]**, and `A_{(2,2)}(x) = x²+2x+2` **exactly**.

So `(2,2)` is *the unique partition whose `A_λ` IS the minimal polynomial of `i-1`*. For every
other λ the question is whether the Eisenstein-at-2 quadratic `q` divides the nonneg-integer
polynomial `A_λ`. (Equivalently `(t²+1)|P_λ(t)`, `P_λ(t)=⟨s_λ,(h₂+t e₂)^m⟩`, `P_{(2,2)}=t²+1`.)
This is the cleanest statement of the problem I've found — it replaces the codim-2 `Re=Im=0`
picture with a single integer-polynomial divisibility.

## What's rigorously proved this session
- Theorem 1 above (reformulation).
- Real form: `Re G = S₀−S₁+2S₃`, `Im G = S₁−2S₂+2S₃`, `S_r=Σ_s C(m,4s+r)M_{4s+r}(−4)^s∈ℤ`.
- Equivalent **elementary criterion**: `G=0 ⟺ q(n)|A_λ(n)=P_λ(n+1) ∀n∈ℤ`. Each failure is a
  one-line non-vanishing certificate (n=0 → 2|f^λ, the parity criterion; n=1 → 5|⟨s_λ,(h₂+2e₂)^m⟩).
  **Honest caveat:** this is logically *equivalent* to G=0 (no free lunch) and the witness `n`
  is **not** uniformly bounded (min witness reaches n=5 by m=8).
- Exact leading `(1+i)`-adic coefficient `w = Σ_{j∈J*} o_j i^{(3μ−j)/2} ≡ |J*| (mod π)`
  ⟹ **|J*| odd ⟹ G≠0** (re-proves the ≥72% with a clean formula, 0 mismatches m≤7).

## Strengthened evidence
- **(2,2) is the unique vanisher for all n≤20** (m≤10, 627 shapes at m=10) — was n≤16.
- **|J*| ∈ {1,2,4} always** — never odd>1, in fact only powers of 2 ≤4 (through m=10). This is
  *finer* than the "evenness" you flagged in PROVE.md. The |J*|=4 sets are {0,2,4,6}, {3,5,7,9},
  and {0,2,8,10}; the last is a binary 2-subcube in t=j/2 coords, but {3,5,7,9} isn't — so only
  the power-of-2 cardinality is uniform.

## The gap, precisely
Re your PROVE.md framing — one correction worth flagging: **proving |J*| even does NOT prove
non-vanishing.** Odd |J*| is the *good* case (`w≡1≢0`, immediate `G≠0`); even |J*| is the *hard*
case where the leading term cancels. So "evenness" only explains why the easy argument fails; the
theorem needs the next-order survival regardless.

The real obstruction is an **interleaved even/odd `(1+i)`-adic cancellation tower**. The even-`j`
and odd-`j` parts of G each cancel internally to *unbounded* depth, and `v_π(G)` is the min over
their competition. Clean example: `λ=(3,3,1,1)`, m=4 — the even leading pair cancels to π-depth
10, but the odd pair (one level up) cancels to depth 8, so `v_π(G)=8`, governed by the odd class.
The leading-pair analysis alone gives the wrong answer. Each rung is a *new* divisibility problem
(against `y²+4`), so it isn't self-similar and no fixed π-adic level closes it. Cancellation depth
grows (5,9,11,15,15,21 for n=6..16) → a uniform-in-m mechanism is mandatory.

## Where I'd dig next
1. The **power-of-2 cardinality of |J*|** smells like a Kummer/Lucas carry fact:
   `v₂C(m,j)=s₂(j)+s₂(m−j)−s₂(m)`; need a binary model for `v₂(M_j)`,
   `M_j=⟨s_λ,h₁^{2(m−j)}e₂^j⟩` (counts of horizontal/vertical 2-strip Pieri chains).
2. The **polynomial form `q∤A_λ`** may admit a coefficient/positivity argument the π-adic picture
   hides: `A_λ∈ℤ_{≥0}[x]`, `A_λ(0)=f^λ`, `A_λ(−1)=⟨s_λ,h₂^m⟩`, `A_λ(x)>0 ∀x≥0`. Is there a
   structural reason a nonneg-coeff polynomial of *this* form can't be `q·B` with `B∈ℤ[x]`?

— Clio
