# Q151 answered no, and the write-up caught four things — 2026-09-17 c1 (PROVE)

**Files** (committed, `clio-claude/proofs@8eaac79`):
- `proofs/2026-09-17-c1-Q151-particle-hole.tex` / `.pdf` (9 pp)
- `proofs/2026-09-17-commuting-ribbon-weights-PAPER.tex` / `.pdf` (10 pp, skeleton)

## Q151: no, on two independent counts

Particle–hole conjugation `P(M) = {-1-x : x not in M}` is **not** Terwilliger's `†`
(`arXiv:2003.09668`).

1. **Variance.** `X -> P X P` is conjugation by an involution, hence an algebra
   *automorphism*. Terwilliger's `†` is an *antiautomorphism*. I named the separator before
   computing — the two agree on every product of length ≤ 1, **and coincide on the commuting
   locus**, so the test has to run on generic weights *off* the locus. Result: 5 rank pairs ×
   19 partitions, automorphism 19/19, antiautomorphism 0/19, with the two candidates genuinely
   differing on 15–19 of the 19 λ (the positive control).
2. **The fixing property.** `†` is *characterised* by fixing `A` and `A*` (Sec 4,
   `lem:antiaut`, read verbatim from the arXiv source). `P` fixes `R_e^W` only when
   `W ∘ T = W`, a proper subspace.

And `prop:threefourths`, the proposition whose transfer motivated the question, says: **any
three of four** one-sided tridiagonality conditions imply the fourth. Not three quarters of
anything. The resemblance to my `cor:quarter` was a collision of names.

## What I got instead

**Theorem A.** `P R_e^W P = R_e^{W∘T}`, `T` = reverse-and-complement of the occupancy word.
Three lines on the bead lattice. This *derives* Q149 `lem:transpose` (Lem 1.6), which had been
sitting there as a 1500-ribbon computation with no proof.

**The accounting.** Of the `(Z/2)^2` on words that Q150c2 `rem:sym` records, exactly `⟨T⟩` is
implemented by an operator (no invertible graded map implements reversal alone — the two
L-trominoes separate, one kills the vacuum and the other doesn't). And what `T` buys splits:

| part of the locus | action of `T` | worth |
|---|---|---|
| nowhere-zero (Q149 `W^γ`) | scalar `κ = (-1)^{e-1} γ(d/2)^{e/d}` | nothing |
| single-shape (Q150c2 `thm:main`) | free involution `w ↦ w^T` | halves the classification |

Fixed points of `T` on words = **antipalindromes** = exactly the `(2B**)` family of
`thm:singleton2`. So that theorem's count `2^{(d-1)/2}`, and the fact that it is *empty for
even d*, come out of a fixed-point count. That is the cleanest explanation I have of why the
even-`d` single-shape operators are new.

**I got this backwards first.** My first draft concluded "no work is free", because I used
Q149 `thm:main` — superseded by Q150c1. Check V9 refuted it within the session. Both the
refutation and the dead branch are in the file and in the registry.

## Four corrections the write-up caught (§Corrections of the skeleton)

- **C1** Q150c2 `def:border` **redefines** "non-overlapping" to mean (NB). The standard
  combinatorics-on-words meaning (unbordered) is strictly stronger, and the two differ from
  `d=5` on — 8 words vs 6, the difference being `0101` and `1010`. The mathematics of Q150c2 is
  right; the *name* would have corrupted the paper. Import the condition, not the word.
- **C2** Q149 Thm 5.2 is superseded and its Lem 8.2 is false for `gcd ≥ 3`. Labels at risk:
  8.1–8.5.
- **C3** `cor:quarter`'s prose says "vanishes at **more** than three quarters"; its display
  `#supp ≤ 2^{d-3}` is correct **and attained** — the cylinder indicator `1_{C_{j,b}}`
  satisfies (2B*) with support exactly `2^{d-3}` (all `j,b`, `3 ≤ d ≤ 8`). It must ship as
  "at least three quarters". This is the paper's headline, so it mattered.
- **C4** the `t^f - t^{f-2}` witness is Q92 `prop:psiwitness`, a **two**-bead element. The
  brief's own table filed it under the one-bead sector.

## Nothing I need from you

No blockers. The skeleton is a skeleton: §4 onward is stated and sourced but not written.
The open list is unchanged apart from one addition — for a seed with zeros that is not a
single shape, I do not know whether `τ ∘ T` is a scalar multiple of `τ` (H2c).
