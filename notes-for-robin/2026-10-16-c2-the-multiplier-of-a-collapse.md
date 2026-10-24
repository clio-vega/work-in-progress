# The long-root divisor was a collapse all along — twisted by a scalar

**PROVE 2026-10-16 cycle 2.** Paper:
https://github.com/clio-vega/proofs/blob/main/2026-10-16-c2-longroot-multiplier.tex
(PDF built, 13 pages, page 1 verified with `pdftotext`; commit `d18e983`.)
Code and logs:
https://github.com/clio-vega/proofs/tree/main/code-1016c2-nonvanishing

## The one-paragraph version

Yesterday I proved *jump ≤ 1 ⇒ Laurent* for Motegi's type C structure constants
and left the converse as a gap. Rick's review said: at `q = 0` every structure
constant is Laurent — which looked like a refutation. I reproduced it on my own
engine. It is **true and it is vacuous on exactly the triples it was aimed at**:
`ord_q(c) = 1` in 25/25 pole records, so the non-Laurent constants are precisely
the ones that *vanish identically* at `q = 0`. Zero is Laurent. The pole does
not cancel; the whole function degenerates.

Then I asked *where* that factor of `q` lives, and it gave me the mechanism.

## The mechanism

On a long-root divisor `H_ab = {w_a w_b = 1}` we have `w_b = w_a⁻¹`, so the
inversion `x ↦ x⁻¹` swaps `w_a` and `w_b`. In Motegi's branching formula, every
factor with **one** leg in `{a,b}` turns out to be accompanied by its own image
under that swap, and the ratio is 1. So the branch index drops out, the
complement drops out, the unselected variables drop out — and what survives is
the single factor with **both** legs inside `{a,b}`:

    Ã_{M,I} ≡ ρ · Ã_{M∖{a,b},I}   (mod w_a w_b − 1),   for every I,
    ρ = (1−q)² / [(1−q w_a²)(1−q w_a⁻²)],

with `ρ` independent of `M`, of `I`, of the branch index, and of `N`. Types C
*and* B — that is the first type B number in this program, and it is the same `ρ`.

So a long-root divisor **is** a collapse. My previous paper said long roots are
*not* collision divisors and called that "the whole asymmetry." The conclusion
was right and the reason was incomplete: the specialisation *points* do not
collide, but the *rows* do — projectively. What distinguishes a long root is not
the absence of a collapse but the presence of a **multiplier**.

And then everything falls out of one line:

    ρ − 1 = q (w_a − w_a⁻¹)² / [(1−q w_a²)(1−q w_a⁻²)]

Basis elements collapse with multiplier `ρ`; their products collapse with `ρ²`.
Since `ρ² ≠ ρ`, the product cannot be a combination of restricted basis
elements, so the coefficients must blow up. That is the pole, and `ρ − 1` is its
size. Three readings of the same line:

1. **`ρ ≠ 1` ⇒ the poles are real.** This is the converse direction.
2. **The numerator has exactly one factor of `q`** ⇒ every long-root residue has
   `ord_q = 1`. I derived that from the formula and *then* checked it against the
   25 records. A prediction, not a fit.
3. **`ρ|_{q=0} = 1`** ⇒ at `q = 0` the twist trivialises, the long-root divisor
   *becomes* an honest collision divisor, and my own collision theorem forbids a
   pole. **That derives Rick's measurement.** His counterexample was not a
   counterexample to the theorem; it was the theorem's degeneration, and it told
   me where to look.

## What is proved, and what is not — please read the second list

**Proved.** (i) The collapse above. (ii) The `⇐` half of what was a conjecture
in the last paper (the exact pole divisor, hyperplane by hyperplane) — this now
generalises yesterday's main theorem, divisor by divisor. (iii) **Every
long-root pole is simple.** (iv) For `ν` *minimal* with the pole condition, the
created pole is real, with a closed-form residue — verified 19/19 at `N = 3`,
three plants in two blocks, all behaving as pre-registered.

**Not proved, and this is the part I want you to see.** (iv) above is
conditional on one measured non-vanishing statement (`ord_H Ã_{M,I} = 0` when
`M ≥ I` and `{a,b} ∩ M = ∅`; measured 64/64 with a discriminating control). I
graded that node `computed`, not `proved`, and the registry's boundary rule
agrees — I checked that a planted promotion fires.

More importantly: **the minimal stratum shrinks.** Coverage of the jump-≥2
triples is

    N = 2:   1/1     100%
    N = 3:  12/13     92.3%
    N = 4:  99/127    78.0%
    N = 5: 690/1136   60.7%
    N = 6: 4335/9748  44.5%

**Decreasing.** If I had reported only `N ≤ 3` this would have read as a
closure. It is not one. The residual gap (propagation) is the *bulk* of the
problem. What I can offer is that it is now a sharp statement rather than a
vague one: the residues obey an exact recursion, and the gap is precisely that
its two terms do not cancel — a non-cancellation between two written-down
quantities, not "absence of conspiratorial cancellation" among branch terms.
Opened as **Q499**, with the pre-registered caution that the `q`-adic grading is
probably *not* the tool, since every residue sits at `ord_q = 1` and so there is
no separation at leading order.

## One thing for you, and one correction to my own brief

**For you.** The gate instruction in my brief told me that if the `q=0`
measurement reproduced, the converse was false and I should amend the paper
first. I reproduced it and the inference does not follow — the structure
constants live in `ℂ(q)(w)` where `q` is an *indeterminate*, so "has a pole" is
already generic in `q` and specialisation `q → 0` does not commute with it. I
withdrew the instruction rather than following it. The general shape, which I
think is the session's transferable lesson: **a counter-measurement can refute
an inference drawn from a claim without refuting the claim** — and the way to
tell the difference is to ask what *object* each side measured. Rick measured
`c|_{q=0}`. I measure the denominator of `c` over `ℂ(q)`. Both correct; different
objects.

**My own brief also carried a number it had not re-derived**: it said the
conjecture "predicts 19 poles at `N = 3`". The figure 19 appears neither in the
paper it cites nor in any measurement; the truth is 13 triples / 25
(triple, divisor) records, which is what my previous paper's own verification
section already said. I only caught it because I recomputed instead of
comparing against the carried figure.

## Nothing needed from you

This is a report, not a request. If you want a single thing to look at, it is
the coverage table above — I would rather you saw the shrinking stratum than the
four theorems.
