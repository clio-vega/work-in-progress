# For Robin — Compensation Lemma B is PROVED (the two-generator wall fell)

**2026-06-15 prove session.** Full win, with change to spare. The `a`-odd three-row `c=3` inequality —
Gap 2, the genuinely two-generator instance of the `e₂ mod 2` wall, the thing the whole three-row
program has been climbing toward — is now **unconditionally proved by hand**, and not just the `≥ 0`
half: the **entire tie classification** comes out too.

## What's proved

For `λ = (a,b,3) ⊢ 2m`, `a` odd, `b` even, `a ≥ b ≥ 4`, offset `j₀ = 3`, all interior `4 ≤ j ≤ b`:

> `Δ̃(j) = j + 3 − 2 s₂(j) + 2 U(j) ≥ 0`,
> with **equality only at `j ∈ {5,7,9}`**, all three together, **iff `a ≡ 1, b ≡ 2 (mod 4)`**.

So in the `a`-odd branch `J* = {3}` (generic) or the **full box `{3,5,7,9} = 3 + ⟨2,4⟩`** (when
`a≡1,b≡2`), giving `|J*| ∈ {1,4}` — both generators, locked. **This closes the `c=3` interior.** The
only thing left in the whole `c=3` family is Gap 3, the standard boundary residual `val(b+i) > val(j₀)`,
identical in nature to the lone residual we already carry in `c=1,2`.

## The shape of the proof (why I think it's the right one)

It is exactly **"Gap-1 doubled,"** as you predicted in the trigger file — and it collapses, after all the
bookkeeping, onto the most elementary fact imaginable: **`2 s₂(k) ≤ k+1`**.

1. **Reformulate.** With `P(j) = C(a+4,j) C(b+3,j) Q₃(j)`, the whole thing is
   `v₂P(j) ≥ v₂P(0) + g(j)`, `g(j) = s₂(j) − (j+3)/2`.
2. **Split `P = P₁ − P₂`** (heavy `(a−1)(b−2)·C·C·H` minus tip `720·C·C·C(j,6)`); the ultrametric
   inequality means I only need each piece to clear the target.
3. **Tip (generator 4, tight at `j=7`).** Feed `C(j,6)` into the `(b+3)`-binomial — the six consecutive
   integers `(b+3)^{\underline 6}` manufacture `β+β'+v₂(b)`; the matching `α+α'` comes from the *other*
   binomial via **Lemma B**, whose own dual `a`-side absorption makes the `α+α'` **cancel**, leaving
   `v₂(a+1) + v₂C(a−2,j−6) ≥ R(j)` with `R(j) ≤ 1 ⟺ 2 s₂(j−6) ≤ (j−6)+1`. That's Lemma A again.
4. **Heavy (generator 2, tight at `j=5`).** Two new factorisations do the work:
   `H = (a+3)(b+2)G − 6E` and **`E = C(j,2)·Φ`** with `Φ = ab+a+2b − (j−1)(j−2)` **odd**. One part
   carries `α'+β'` outright; the other absorbs `C(j,2)` and uses `v₂C(b+3,j) ≥ β'+g` (= the `c=1`
   Number Lemma + a digit lemma).
5. **Ties.** Even `j` die by parity; odd `j ≥ 11` die by a *strict* slack version of the same two digit
   lemmas; `j = 5,7,9` by an exact valuation case-split over `(a,b) mod 4`. The **lock** is transparent:
   `a≡1, b≡2 (mod 4)` is exactly the residue that simultaneously makes the heavy/`H`-valuations minimal
   (`α',β' ≥ 2`) *and* the binomial valuations minimal (`v₂(a+1)=v₂(b)=1`). That single coincidence is
   the `|J*| = 4` event.

## Two things for the paper

- The **`E = C(j,2)·Φ` factorisation** (with `Φ` odd) is new and clean; it's what makes the heavy part
  tractable and is probably worth stating as its own little identity in the `c=3` write-up.
- The proof needs **only**: Lemma A (`2s₂(k)≤k+1`), Lemma C (`2s₂(j)+2v₂(j(j−1))≤j+3`), and the
  `c=1` Number Lemma NL₁ (self-contained, one subset identity). NL_c for `c≥2` is *not* needed here —
  the heavy/tip split localises everything to `c=1`-level arithmetic. That's a nice simplification over
  what we expected.

## Verification

Every single link — the two digit lemmas, NL₁, Lemmas (i) and B, the heart `R≤1`, the tip and heavy
bounds, the main inequality, all the `j=5,7,9` formulas and per-residue cases, and the strict
positivity for odd `j ≥ 11` — was machine-checked with **0 failures** over all `a`-odd `(a,b,3)`,
`4 ≤ j ≤ b`, `m ≤ 79` (digit lemmas swept to `2·10⁵`). The `H` and `E` identities are confirmed
symbolically in `sympy`.

## Next

LEAN follow-on is now well-posed: formalise **Lemma B and Lemma (i)** (both reuse the existing
`vz_choose_ge` helper from the `c=2` Lean work). With Compensation Lemma C (c=1) and Number Lemma C2
(c=2) already in Mathlib-checked form, this would put the entire load-bearing arithmetic of the
three-row even-`|J*|` program under the type-checker.

Files: `proofs/2026-06-15-compensation-lemma-B-proved.md`, code `proofs/code/threerow-c3/c3gap2_*.py`
(esp. `c3gap2_FULLCHAIN.py`, the end-to-end check).

— Clio
