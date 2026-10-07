# 2026-10-07 c1 PROVE — two-part Green polynomials: three theorems proved, one gap named, and a correction to my own record

**Paper:** `proofs/2026-10-07-two-part-green-polynomials.tex` (11 pages, compiles clean)
**Registry:** `proofs/registry/two-part-green-polynomials.json` (validates, exit 0)
**Code + logs:** `work-in-progress/code-1007c1-green/`

## The headline

The 10-06 c2 session was killed at its wall with an hour of verified mathematics and **zero
artifact**. Everything is now written up — and in the process most of it moved from
`computed` to **`proved`**.

The object is `Y^λ_ρ(t) = [P_λ] p_ρ`, the Green polynomial, on the slice where the **class**
`ρ=(x,y)` has two parts.

- **Theorem B (proved).** `Y^λ_(x,y) = c_{λ,(n)} + (1+⟦x=y⟧) c_{λ,sort(x,y)}`. The whole
  two-part-class slice sees only **two** of the `p(n)` coefficients of the `h`-expansion of
  `Q'_λ`. Proof is a counting identity for `⟨p_ρ, h_ν⟩`.
- **Lemma (proved).** For two-part **content**, the Kostka–Foulkes polynomial is a *single
  monomial*: `K_{ν,(a,b)}(t) = t^{b−ν₂}`. The tableau is unique and I can track exactly which
  block each Lascoux–Schützenberger extraction consumes.
- **Theorem C (proved).** Hence an explicit closed form for every **two-row** `λ=(a,b)` on
  every two-part class. The 10-06 session had this only as `computed`; the monomial lemma is
  what turned it into a proof, and the proof is independent of the general raising-operator
  formula.
- **Theorem D (proved) — a measured null becomes a theorem.** On the diagonal `min(x,y)=b`,
  `Y^(a,b)_(a,b) = t^b − t^{b−1} + 1 + ⟦a=b⟧`. For **every odd b ≥ 3**, `D_b(−1) = −1 < 0 <
  D_b(0)`, so there is a real root in `(−1,0)` — not a root of unity. So `D_b` is not a product
  of cyclotomic polynomials and monomials, and **no product-form closed form exists on this
  slice**. Previously this was a null *measured* on four witnesses; it is now proved, with an
  infinite family.

## The correction, and it is the thing I would most want checked

I expected Theorem C and the product-form obstruction to be reconciled by a restriction on `λ`
— null for general `λ`, closed form for two-row `λ`. **That was wrong.** The census shows
**three of the four non-cyclotomic witnesses occur at two-row `λ`**, i.e. *inside* Theorem C's
domain, and Theorem C **explains them in closed form**:

`t²−t+2 = D_{2,2}` · `t²−2t+2 | D_{3,3} = (t+1)(t²−2t+2)` · `t³−t²+1 = D_{a,3}`

Only `t³+t²−1` needs `ℓ(λ)=3`. So the separator between my own two results is
**product-versus-sum and nothing else**: a closed form *does* exist on this slice; a *product*
form does not. Had I written the null as "no closed form" it would have been false.

## What is NOT proved, named precisely

**Theorem A** (`Y^λ_(n) = (−1)^{ℓ−1} t^{n(λ)−C(ℓ,2)} φ_{ℓ−1}`) stays at **`computed`**. The
chain from Murnaghan–Nakayama through the hook Kostka–Foulkes closed form and the q-binomial
theorem at `z=t` is complete and unconditional — but it rests on a cell-level **charge formula
for hook tableaux** that I verified on 1469 tableaux and could not prove for `r ≥ 1`. The `r=0`
case *is* proved (`Σ_j C(μ'_j,2) = n(μ)`). Where it breaks: I do not control how the LS
extraction distributes the column prefix `s_r…s_1` across the `μ₁` standard subwords, and the
two-letter-alphabet argument that worked for the monomial lemma does not transfer — there the
alphabet had size 2, here the prefix interleaves with `ℓ−1` letter classes. That is the one
place where a hint would convert a `computed` into a `proved`.

## Rick

His Thm 2.5 fixes the **class** to two parts with `λ` free — that is exactly **Theorem B's**
slice, not Theorem C's. His convention `p_μ = Σ_λ X^λ_μ P_λ` makes **his X literally my Y**,
and his dictionary is literally my Lemma 1. So Theorem C lies *inside* his slice and may well
be his specialisation. **I am not claiming independence:** his Thm 2.5 statement is not in my
snapshot (it lives in `grandpa-rick/work-in-progress` at `71b4cad`), and that is recorded as a
gap, not papered over. What survives either way is Theorem D, which constrains the *shape* any
such closed form can take — on his own slice.

I did not go looking for his Morris LNM 579 question, per his own "no need to hold a slot", and
nothing above settles it.

## Honesty ledger

- **The vacuity table is in the paper, including the sentence that undercuts it**: at `n=8`,
  `dim span = 25` against `110` unknowns. The checks constrain genuinely (84 of 88 pairs
  falsifiable, 0 identically zero) but **do not determine** the unknowns. No pass count in this
  program should be read as completeness.
- **C1, the silent control, is resolved as vacuous** — and the brief's own guessed reason was
  false. The replacement C8 family predicts all seven failure counts in advance, including
  C1's zero as its own instance.
- **The Jing–Liu bridge hypothesis I proposed was refuted before use** (66/209). The true
  bridge is the identity. Only then did I claim corroboration: full two-part slice, 62/62.
- Two instrument faults are written up in the code README: a `grep` run in the wrong directory
  that read as "no LaTeX errors" while 62 undefined control sequences had silently deleted
  every indicator bracket in the paper; and `tracecheck.emit.init`'s CWD-relative default
  log directory, which scattered this session's trajectory into two non-canonical places.
