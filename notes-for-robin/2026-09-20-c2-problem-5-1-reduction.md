# Problem 5.1 may fall out of yesterday's theorem — and it turns on one thing I can't check without you or a locator

*Clio, DREAM 2026-09-20 c2. Follow-up to `for-robin/2026-09-20-cylindric-M-convexity-solved.md`
(the solved Problem 5.2 note, already sent).*

## The short version

The theorem I proved this morning says the supports are **nested**:

> `supp(s^c_{λ/μ}(x₁..x_ℓ)) = {α : sort(α) ⊴ λ̂} = P_λ̂ ∩ Z^ℓ`, so `λ̂ ⊴ λ̂′ ⟹ P_λ̂ ⊆ P_λ̂′`.

A union of M-convex sets is **not** M-convex in general — but a union of a **nested** family is just
its largest member. So if an affine Stanley symmetric polynomial expands with **non-negative**
coefficients into cylindric skew Schur polynomials, then

> **`2401.14632` Problem 5.1 holds for `F_w` ⟺ the `λ̂` occurring in that expansion have a dominance
> MAXIMUM** — and when they do, `Newton(F_w) = P_{λ̂_max}` exactly, which is stronger than the
> problem asks.

That converts "find a combinatorial proof" into a finite, checkable statement about one expansion,
with a built-in falsifier: **one `w` whose expansion contains two dominance-incomparable `λ̂` kills
it.** I'd rather find that pair than prove fifty cases.

## Where I need help (this is the whole ask)

**The Lam relation between affine Stanley symmetric functions and cylindric skew Schur functions —
which direction, and with what positivity?** I hold it as *"Lam 2008 relates the two"*, which is a
relation, not a verified direction, and **positivity is carrying the entire argument above.** If the
expansion runs the other way (cylindric Schur expanded *into* affine Stanley), the argument does not
start. This is your thesis territory and you'll know it cold; I'd otherwise spend a browse session
chasing a locator. I have not asserted this anywhere outside my own disk, and I won't until it's
pinned.

Two smaller caveats I've already recorded against myself:
- The union must be taken at a **fixed number of variables `ℓ`**. My paper's §8 *asserts* λ̂'s
  monotonicity in `ℓ` rather than proving it, so that loose end is now load-bearing rather than
  cosmetic.
- Terms with different Postnikov shift `d` need normalising before "dominance" means anything —
  a bead set determines a cylindric shape only up to `d`, which is a correction I had to make to my
  own dictionary mid-proof.

## Why it might be unclaimed

Problems 5.1 and 5.2 have **3 citers in 30 months**. Bechtloff Weising–Black `2508.00336` prove
affine Demazure characters are M-convex (their Cor 1.2) — level-adjacent — but an agent grepped their
tex and bib: `affine Stanley` and `cylindric` return **zero hits**, and WZZ appears once as a bare
bib key. **Cited, not engaged.** And MO 424766 (Alexandersson, on cylindric/skew Kostka) still has
**0 answers after 4 years 3 months**.

Full argument, with the three checks spelled out:
`memory/connections/2026-09-20-c2-problem-5-1-reduces-to-a-dominance-maximum.md` → **Q206**.

*(Paper for Problem 5.2, if you want the context:
https://github.com/clio-vega/proofs/blob/main/2026-09-20-c1-cylindric-M-convexity.tex)*
