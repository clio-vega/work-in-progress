# Q191 answered: a combinatorial proof of the M-convexity of cylindric skew Schur polynomials

**2026-09-20, PROVE c1. Status: proved, all (n,m,ℓ). One compact step flagged as Gap 1.**

**Paper:** https://github.com/clio-vega/proofs/blob/main/2026-09-20-c1-cylindric-M-convexity.tex
(PDF and the verification code `code-q191/cyl.py` are in the same commit, `c2e9771` + follow-ups.)

## What was asked

Wang–Zhang–Zhang, `2401.14632`, Problem 5.2 (verbatim, `wzz.tex:945`):

> Find a combinatorial proof of the M-convexity of cylindric skew Schur polynomials based on
> their tableau interpretation.

The truth is not in question — it is their own Corollary 4.9. What is wanted is a proof that
does not *import* it. The motive is stated one paragraph above the sibling Problem 5.1
(`wzz.tex:929-936`): *"One of the key ingredients of our approach is Theorem [Lam, Cor 8.5], a
deep result obtained by Lam. It would be interesting to find a direct proof … based on the
definition given by (4.1)."* So the success criterion is checkable: **does the argument still
consume Lam's Cor 8.5?** Mine does not. §7 of the paper lists every external input; the list of
substantive ones is empty.

## What I proved

> **Theorem.** Let λ/μ be a cylindric skew shape in C^{n,m}, ℓ ≥ 1, and suppose the polynomial
> is nonzero. Let λ̂ be the sorted weight of the *greedy chain* g⁰=μ, gᵗᵢ = min(gᵗ⁻¹ᵢ₊₁ − 1, λᵢ).
> Then
>   supp(s^c_{λ/μ}(x₁,…,x_ℓ)) = {α ∈ ℕ^ℓ : sort(α) ⊴ λ̂} = P_λ̂ ∩ ℤ^ℓ.
> In particular s^c is M-convex, is SNP, and Newton(s^c) = P_λ̂.

This is **stronger than WZZ Cor 4.9**: it names the polytope, by an explicit greedy algorithm.

## The idea, in one paragraph

Put the whole thing on the periodic Maya diagram. A cylindric shape in C^{n,m} becomes a
strictly increasing x : ℤ → ℤ with x_{i+m} = x_i + n; a semistandard cylindric skew tableau
becomes a chain x⁰ ⊆ x¹ ⊆ … ⊆ x^ℓ with interlacing steps; and — this is the first of the two
things that happen — **the weight linearises**: α_t = u(xᵗ) − u(xᵗ⁻¹) where u(x) = Σᵢ₌₁ᵐ xᵢ. The
weight of a cylindric tableau is the increment sequence of a *single integer statistic*, so
α₁+…+α_r telescopes. The second thing is that **the chain decouples**: the condition that steps
t and t+1 are both horizontal strips constrains xᵗᵢ only through xᵗ⁻¹ and xᵗ⁺¹, never through
xᵗⱼ for j ≠ i. So with its neighbours fixed, a row of the chain ranges over a *box*
∏ᵢ[Lᵢ,Uᵢ], Lᵢ = max(pᵢ, r_{i−1}+1), Uᵢ = min(p_{i+1}−1, rᵢ).

Everything else is bookkeeping on that box, and the only identity to check is

  **Σᵢ₌₁ᵐ (Lᵢ + Uᵢ) = Σᵢ₌₁ᵐ (pᵢ + rᵢ),**

whose proof is "max + min = sum" plus one wrap-around term. From it, in order: the reflection
xᵗᵢ ↦ Lᵢ+Uᵢ−xᵗᵢ is a **cylindric Bender–Knuth involution** (so I reprove Postnikov's symmetry
theorem rather than cite it); the window of achievable α_t is palindromic about N/2, so if
α_t > α_{t+1} then xᵗ is not at the left corner of its box and **one bead can slide one site
left**, which is the M-convex exchange; that gives the dominance-ideal property; the greedy
chain dominates every chain coordinatewise in every row, so by telescoping it maximises every
partial sum *simultaneously*, giving the unique dominance maximum; and a from-scratch
tight-set argument turns "symmetric dominance ideal with a maximum" into M-convexity without
Rado.

**The prettiest part, and the one I'd point a referee at:** that wrap-around term contributes
exactly **+n**, and it is what makes the identity true. Drop it and you get Σ(pᵢ+rᵢ) − n, and
with it the false conclusion that cylindric Bender–Knuth fails. *The cylindric case works
because of the periodicity, not in spite of it.* I made exactly that slip in my first
derivation and the computer caught it.

## Two corrections to the brief I was given

1. **The ribbon move was the wrong move.** The BROWSE addendum sent me at Q198 — the converse
   of Naprienko `2301.12110` Lemma 4.4, where a ribbon becomes one bead hopping k → K+1. That
   is a real and well-posed question, but it is not on the path to Q191. A **ribbon** of size r
   is one bead hopping r sites, jumping *freely over occupied sites*; a **horizontal strip** of
   size r is several beads hopping right with pairwise **disjoint** closed trajectories — no
   bead may pass or land on another. Cylindric skew Schur functions are built from horizontal
   strips. Recorded as a dead-end node with `reason`.
2. **`--files-dir` in the brief was wrong**, and wrong in the same way the registry README is:
   it wants `/home/clio/projects`, not `/home/clio/projects/proofs`, because a node's `file`
   carries the `proofs/` prefix. Third carrier of that value now.

## What I checked before I trusted anything

- **Anchor** (is this the right object?): at n = 20 the bead model agrees in all 13 coefficients
  with an independently coded *ordinary* skew Kostka computation for (8,5)/(3,2).
- **Positive control**, untuned, published by other people, and *signed*: WZZ's own Example 4.2.
  For w = s₂s₁s₀s₂ ∈ S̃₃ they record F̃_w = m₁₁₁₁ + m₂₁₁ + m₂₂ = **s₂₂ − s₁₁₁₁**. A search over
  C^{3,m} with d = 4 finds exactly one realisation and the model reproduces this **exactly**,
  negative Schur coefficient included. The anchor pins the object; the negative coefficient is
  the separator that proves I am not computing ordinary skew Schur functions in disguise.
- Decoupling 380/380 · palindrome identity 470/470 · greedy maximum 462/462 · ideal + unique
  max 1932/1932 · raw exchange axiom by exhaustive search 409/409 · coefficient symmetry
  339/339 · **end-to-end supp = P_λ̂ ∩ ℤ^ℓ, 1160/1160.**

## The gap I flagged, and then closed

I first proved Proposition 2.4 — the dictionary from Postnikov's lattice paths to the bead
model — by *local reduction* to the classical partition case, and flagged the window
bookkeeping as the one step not written at full length. Late in the session I closed it. The
right bead coordinate is

  **xᵢ = Rᵢ + i,  Rᵢ = the right-hand column of row i, rows indexed downwards,**

and from that formula all three statements (containment, box count per fundamental domain, "at
most one box per column" ⟺ interlacing) fall out directly in half a page. No windows.

Two errors on the way there, both now in the paper:

1. My first draft claimed a bijection with periodic bead **sets**. False — a bead set
   determines the path only up to *diagonal translation*, and the datum it loses is exactly
   Postnikov's shift `d` in `λ/d/μ`. Indexing beads by height restores it.
2. My first draft of the sign used `Rᵢ − i`, by reflex from the usual β-set. False: along a
   cylindric shape with rows indexed downwards the row lengths **increase**, so `Rᵢ − i` is not
   even strictly increasing.

I fixed the sign by **compiling WZZ's own Figure 5.1 and reading the boxes off the picture** —
`n=5`, `m=2`, weight `(1,2,1,2)` — rather than guessing from their LaTeX source. Converted, it
is `μ=(0,2)`, `λ=(3,5)` in `C^{5,2}`, and their printed tableau is the chain
`(0,2) ⊆ (0,3) ⊆ (1,4) ⊆ (2,4) ⊆ (3,5)`, every step of which the model independently certifies
as a cylindric horizontal strip, of sizes `1,2,1,2` exactly as printed. That is now the second
control in §7, and it is the one that decided the convention.

**So the paper has no remaining gap of substance.** Two cosmetic items are still listed in §8:
Rado's theorem is quoted (not proved) for the purely decorative identification
`P_λ̂ ∩ ℤ^ℓ = {α : sort α ⊴ λ̂}`, which nothing depends on; and the monotonicity of `λ̂` in `ℓ`
is asserted without proof.

## What I'd like from you

Whether §7's accounting is the accounting WZZ would accept — i.e. whether "combinatorial proof
based on their tableau interpretation" is satisfied by an argument that reformulates the
tableaux as bead chains before moving a single bead. I think yes, and I think the bead model
*is* the tableau interpretation in better coordinates. But that is a judgement about what the
authors want, and you read intent better than I do.

— Clio
