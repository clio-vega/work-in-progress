---
name: For Robin — Q173 closed, the HMMS pin is total, and Q177 is a NO
description: PROVE 2026-09-19 c1. Speyer does not cover the chain regime (estimand mismatch + degenerate evidence); HMMS's LR claim is entirely a Kostka claim, now proved; free-fermion six-vertex partition functions are generically not Lorentzian, so the literature gap is an obstruction.
type: project
---

# The gap is an obstruction, not an absence

**Paper:** https://github.com/clio-vega/proofs/blob/main/2026-09-19-c1-lorentzian-obstruction.pdf
**Source:** https://github.com/clio-vega/proofs/blob/main/2026-09-19-c1-lorentzian-obstruction.tex
**Registry:** https://github.com/clio-vega/proofs/blob/main/registry/lorentzian-six-vertex.json
**Code:** https://github.com/clio-vega/proofs/tree/main/code-2026-09-19
**Commits:** `clio-vega/proofs@0305474`, `clio-vega/proofs@be90d5e`

Three results. All negative. I think the third one is worth something.

## 1. Q173 is closed, and the July attribution is now replaced by a reason

I told you in July that Speyer `2601.05007` was the naming home for my chain-regime
log-concavity. I withdrew that yesterday because I had the mechanism wrong (L-convexity,
not Lorentzian). Today I can say what is actually true.

**Speyer does not cover it, and not because a hypothesis is missing — because the
estimands differ.** Speyer's theorems are about functions on the weight lattice `Z^n`
valued in LR/skep counts, with log-concavity taken in the *lattice* variable. My object is
the coefficient sequence of `c_gamma(t)` in `Z[t]`, indexed by *t-degree*. There is no `t`
anywhere in his paper.

**And the evidence was degenerate anyway.** In the chain regime `c_{gamma(L)}(t) = [n-L]_t`
is the all-ones sequence, so "log-concave" is the equality `1*1 >= 1*1`. All 10/10
chain-regime entries in my July probe are all-ones; 44 of the 70 overall. A theorem
"covering" the chain regime would be covering nothing. I also cannot reproduce the
`46/46` I quoted at you — the probe has 34 entries in chain ∪ (3,3,*,0).

## 2. The pin inside HMMS is total — and now proved, not just suspected

My 09-18 hunch was that HMMS's Littlewood–Richardson statement "may be a Kostka theorem
wearing an LR costume". It is, completely:

- one-box-per-column `⟺ kappa_i >= nu_{i+1}` for all `i`;
- on that locus the row intervals are disjoint, so `s_{nu/kappa} = prod_i h_{nu_i-kappa_i}`,
  and Pieri gives `c^nu_{kappa,lambda} = K_{lambda, nu-kappa}` for **every** lambda;
- so the value depends only on `(lambda, nu-kappa)` — **the label `nu` is redundant** — and
  by HMMS's own converse every Kostka number arises.

927 shapes, 1019 triples, zero violations. Their abstract concedes it ("in the special case
of Kostka numbers"). Their genuinely-skew statement is only a *conjecture*, tested to 12
boxes. And the general Okounkov LR log-concavity is *refuted*. So the Lorentzian bank has
never proved a genuinely-LR log-concavity statement, and the general one is false.

## 3. Q177: free-fermion six-vertex partition functions are generically NOT Lorentzian

This is the one I'd want you to look at.

I built a Lorentzian checker to HMMS Definition 2.1 — it passes 16 untuned positive
controls (normalized Schur, which must pass by their Theorem 3) and fails correctly on
three negative controls, one per condition. Then I enumerated 1554 homogeneous nonnegative
free-fermion weight families and tested 40 of them across all boundaries.

Of 352 non-monomial partition functions: **252 are not Lorentzian** — 170 failing
M-convexity of the support, the most basic condition, before any eigenvalue is computed.
The 100 that pass are all products of linear forms, so they carry no information either.

Smallest witness: with `(a1,a2,b1,b2,c1,c2) = (x,y,y,x,2x,y)` (free-fermion, since
`xy + xy = 2xy`), `Z = 2 x1 x2 (x1 y2 + x2 y1)`. The support of that last factor is
`{(1,0,0,1),(0,1,1,0)}` — the two points differ by `(1,-1,-1,1)`, which is not an exchange
`e_i - e_j`, so the support is not M-convex.

**So the census answers itself.** Zero of 238 Brändén–Huh citers mentions a vertex model.
That is an **obstruction**, not an absence — the edge I proposed to build in July does not
exist. HMMS say the mechanism themselves in a §3.1 footnote: the Newton polytope of any
homogeneous strongly log-concave polynomial must be a type-A generalized permutohedron,
every edge parallel to some `e_i - e_j`. That is exactly what my witnesses fail.

Why Schur survives and does not deform: the five-vertex Schur model has four of its five
weights equal to 1, i.e. degree 0. Its partition function is homogeneous because of the
*boundary*, not the weights. So the x-degree is a genuine statistic with permutohedral
support. Make the weights homogeneous — which any general six-vertex model needs for `N(·)`
to be defined — and the support collapses onto an antidiagonal graph.

## What went wrong, because you always want this part

- **One experiment was vacuous and I nearly banked it.** My first homogeneous family gave
  114/114 Lorentzian. They were also 114/114 *monomials*: the grading I picked coincided
  with the model's conserved particle number, so `Z` was forced to be a monomial. A perfect
  pass rate worth exactly zero. I caught it only because I counted supports afterwards.
- **A structural conjecture of mine was refuted by my own test.** I thought the row-degree
  lemma forced M-convexity to fail for every non-monomial `Z`. False — 441 of 769
  non-free-fermion cases do have M-convex support. The obstruction is specific to the
  free-fermion locus, and *why* is the open question I'm leaving behind.
- **I didn't check prior work.** A browse session the same morning had already read HMMS at
  source, promoted the entry to `verified-quote`, and established two corrections my PROVE
  brief still asserted: HMMS is **not** a cut vertex (it doesn't cite Knutson–Tao at all;
  Pak `2209.06142` spans both banks without it), and the LR statement is intro prose, not a
  numbered corollary. I re-derived B1 from scratch and agree with all of it, but I should
  have read my own index first.

## Also: an erratum in Lê–Nguyễn

`2608.13544` Example 1.3 has `nu` and `pi` interchanged as printed — `pi - x = (0,1,1,2)`
is not a partition. The reading that reproduces their published `6 > 5` is
`nu=(6,5,4,2)`, `pi=(9,5,3)`, giving `2*3 > 1*5`. Their refutation of Speyer's Question 2.17
stands; only the labels are swapped.

## Open

Why does the free-fermion condition specifically break M-convexity, when general six-vertex
weights often don't? That's the question worth the next slot.
