# For Robin — PROVE 2026-10-24, Q565: the locus I was hunting was a restriction, not a zero

**Artifact:** `proofs/2026-10-24-Q565-zero-locus-in-M.pdf` (11 pp), pushed.
https://github.com/clio-vega/proofs/blob/main/2026-10-24-Q565-zero-locus-in-M.tex
Provenance commit `008f8ef5`, verified resolvable on the remote against a failing
negative control (a fabricated hash returns 422).

## The mathematics, in one sentence

I went looking for the zero locus of my `Psi^C_{(1^r),theta}` in `M` and found that the
locus I had been treating as a set of zeros — `w_a w_b = 1` — is where the function
**forgets the pair**: `Psi(M) = Psi(M \ {w_a, w_b})`, and `Psi(M) = Psi(M \ {w_a})` when
`w_a² = 1`. Both are two-line proofs: the terms touching the pair die on the pair factor,
and for the terms avoiding it the two cross factors multiply to *exactly* 1.

I like this one because it makes the previous result inevitable rather than true. My
`prop:recip` said "a reciprocal pair forces zero when `n ≤ r+1`" and I had no idea why
`r+1`. The answer is that nothing is being forced to vanish at all — `Psi` is descending
to a smaller `M`, and `n ≤ r+1` is just where the descent lands below rank `r`, so the
sum is over an empty index set. Which immediately generalises: `mu` disjoint reciprocal
pairs descend `2mu` steps, so the real condition is a **covering** condition
`2mu + nu > n - r`, and two pairs kill `r = 2, n = 5` — three steps above the threshold
`prop:recip` could see.

`r = 1` then came out completely: the head sum **is** the sum of residues of
`z^{m-1}H(z)` over the poles `w_a`, with `H(z) = prod (z w_t - 1)/(z - w_t)`, so it equals
minus the residues at `0` and `infinity`, i.e. a Taylor coefficient of `H`. Prettiest
special case: `Psi_{(1),(0)}(M) = 1 - e^{-2}` for *every* `n` — it sees the whole set only
through the product.

## The three things I want to flag, because they are all about instruments

**1. My own sampler had a fourth exclusion I had never written down.** The brief told me
(correctly) that the Q559 counts — `424/424`, `386/386`, `336/336` — are *zero* evidence
on this axis, because the sampler excludes `w_a = ±1`, `w_a w_b = 1`, `w_a = w_b`, which
is a restatement of the question. True. But the sampler draws
`Fraction(randint(2,40), randint(1,7))`, so **every `w_a` is positive**, and that is the
exclusion that was actually load-bearing: all three vanishing mechanisms need a sign.
Restricted to the positive orthant the hygienic sampler gives 0 zeros in 1800 draws. So
the evidence was blind on *two* axes and the second one is where the answer lives, and I
only found it because I went to read the sampler rather than my description of it.

The general form, which I think is the real lesson: **a sampler's support is a hypothesis
whether or not it is written as one.** I wrote three exclusions as hypotheses and left the
fourth implicit in a call to `randint`.

**2. The control the brief told me must stay green fired, and it was right.** Brief
control 1: "the Q559 sampler must find no zeros; a zero means my engine regressed." Mine
found 19 in 540. The engine was fine — I had reproduced the three *named* exclusions and
not the unnamed one. Classifying the 19 gave 18 of one mechanism and exactly **one** that
was the pre-registered P1 falsifier I had been searching for by other means and failing to
find. Third session running where the control I expected green from was the discovery
instrument. I think the sharper statement is: a control is a prediction about an
*instrument*, so when it fires, check first whether I rebuilt the instrument or only its
description.

**3. The brief's own decisive test would have given me a false close** — and this is the
one I would most like you to look at, because it is subtle and I nearly ran it. The brief
said: factor the numerator; *"if every irreducible factor is of the form `(w_a w_b - 1)`
or `(w_a² - 1)`, P1 is confirmed and I have the proof, because a product of those factors
is exactly the structural locus."* That last clause is false. A product of those factors
cuts out a **codimension-1** union of hypersurfaces; the structural locus (every `B(T)`
vanishing) is a **codimension ≥ 2** covering condition as soon as `n ≥ r+2`. The two
conditions coincide only for `n ≤ r+1`. So the outcome labelled "confirmation" is itself a
refutation — and I would have written it up as a close.

What unsettles me is the shape: the brief spent a paragraph warning me that the question
was "one word over two mechanisms" and then committed exactly that fault in the sentence
setting up the test designed to avoid it. Naming a failure mode in advance did not
inoculate the next paragraph against it. (It also turned out to be *three* mechanisms, not
two — there is a Schur-vanishing mechanism, `s_lambda(T) = 0` on every live term, that is
invisible to any argument about `B` and that neither the brief nor I had in view.)

## Where it stands

`proved`: Theorem R, the covering structural locus, the corrected `w_a = ±1` threshold
(a retraction of my own sentence), which reciprocal polynomials divide the numerator
(`17/17`, by symbolic division — a different instrument from the evaluations), the
dimension count refuting P1 for all `n ≥ r+2`, the `r=1` closed form, the negation
covering law. `computed`: the witness `M = {-7,2,3,7,-2}`. `dead-end`: determinant
ansätze in the `r=1` data (the pair factor is a type-C Gaudin kernel, not free-fermionic,
so a Jacobi–Trudi shape was the wrong guess — and every apparent hit was a `0 = 0` cell).

Carried, with honest grades: **Q576**, `Psi = 0` iff `r ≥ f+2` for `lambda` negation pairs
and `f` free elements, measured `26/26` both directions with the boundary clean — the
surviving terms pair under the involution reversing one negation pair and I cannot find
the sign. **Q577**, a contour formula with the type-C Gaudin kernel that I derived by
matching residues and have **not checked in a single case**; it is in the registry as
`speculative` and nothing rests on it.

One housekeeping note against myself: the trajectory emitter's default `log_dir` is
relative and its default session tag is a fresh timestamp per process, and its source
carries a warning about this addressed to me from 2026-10-09. Both defaults fired again
today — two orphan files, each restarting ids at `evt-0001`, so one `inputs` reference
resolved to a different event than the one I meant. Consolidated into
`state/trajectory/clio-prove-Q565-20261024-prove.jsonl` and wrapped in
`code-1024-q565/trace.py` so it cannot recur today. A warning in a docstring is not a
guard.
