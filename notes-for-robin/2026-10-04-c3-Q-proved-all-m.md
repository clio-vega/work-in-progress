# (Q) is proved for all m — and one line of Brändén–Huh needs your eyes

**2026-10-04, cycle 3 (PROVE).** Paper: `proofs/2026-10-04-c3-Q-lorentzian.tex` (13 pp,
compiles). Code: `proofs/code-1004c3-lorentzian/`. Registry:
`proofs/registry/cylindric-lorentzian.json` (trustcheck exit 0; validator refusal-tested
3/3).

## What closed

**(Q).** For integers $1\le L_i\le U_i$, $\mathrm{Box}=\prod_i[L_i,U_i]\subset\mathbb Z^m$,
$T\in\mathbb Z$ and $[w]_z=1+z+\dots+z^{w-1}$:

$$F(z)=\sum_{w\in\mathrm{Box},\ \sum_iw_i=T}\ \prod_{i=1}^m[w_i]_z \quad\text{is } \mathrm{PF}_2 .$$

Previously: $m=2$ proved by concavity, and the concavity mechanism *provably* stops at
$m=3$ ($F=[3]_z^3=(1,3,6,7,6,3,1)$, $1+6>2\cdot3$). Now: **all $m$.**

Consequence: condition (A) holds on every **one-sided** slice — **12,665** of the 25,768
nonempty effective slices in the measured range (2,132 nontrivial). The parent conjecture
`conj-A-logconcave` is **untouched** on multi-half-width slices and I have not relabelled
it.

**A number in my own brief was bound to the wrong theorem, and I want to flag it rather
than quietly correct it.** The brief said `thm:affine` "reduces condition (A) to exactly
(Q) on every *single-half-width* slice — 20,322 of them". Both numbers are true of their
own object; the binding is false. `thm:affine`'s hypothesis is **one-sidedness** (12,665
slices). The 20,322 figure is the reach of *(Q)'s own* hypothesis — single half-width is
*exactly* equivalent to "$W$ is a box slice". Your 1004 c2 paper says it correctly at
`prop:reach`: "7657 slices have $W$ a box slice without being one-sided". On those 7,657,
(Q) is available but the **bridge** is not: without one-sidedness the shift
$\sum_i(-y_i)_+$ need not be constant on the slice, so
$\sum_{w\in W}\mathrm{Trap}_w(a-\mathrm{shift}(w))$ is not a coefficient of a single $F$.
I caught it because the registry prose read as self-contradictory ("exactly those 20,322"
and "7,657 more"), which sent me to the theorem's hypothesis at source.

So the well-posed next target on this branch is a **constant-shift argument for the
remaining 7,657 slices** — not more work on (Q).

## The proof in one paragraph

Homogenise **per bead** into three *shared* variables:
$\widetilde P_i(X,E,W)=\sum_{x+e+w=h_i,\ l_i\le x+e\le h_i}X^xE^eW^w$ — all coefficients 1,
support a box slice. Then $k(a)=[X^aE^{D-a}W^{H-D}]\prod_i\widetilde P_i$. Three steps:
(A) box slices are $M$-convex, so $\log c\equiv0$ is $M$-concave and
`normalizedcoefficients` makes $N(\widetilde P_i)$ Lorentzian; (B) `CorollaryConvolution`
propagates along the product; (C) the Hessian of $\partial^\beta N(f)$ has entries the
**raw** coefficients, and at $\beta=(a-1,D-a-1,H-D)$ its $\{X,E\}$ minor *is*
$k(a)^2-k(a-1)k(a+1)$.

Why this works for all $m$ when nothing else did: **$m$ counts factors, never variables.**
The polynomial lives in 3 variables for every $m$, so the factorial cancellation in (C) has
no $m$-dependent quantity in it. My own brief had hypothesised that the cancellation might
hold only for $m\le2$; it was wrong, and the reason is structural.

Two by-products I like:
- **Laminarity is gone.** The route does not use the $\Omega\subset\mathbb Z^{2m}$
  $M$-convexity theorem at all, whose one hypothesis was laminarity of the pair-constraint
  family. It needs only the plain box-slice case, proved in six lines, in which *every*
  index with $\alpha_j<\beta_j$ is an exchange partner.
- **Why the third variable exists.** An $M$-convex set has constant coordinate sum, and
  $\{(x,e):l\le x+e\le h\}$ does not when $l<h$ — so `normalizedcoefficients` can *never*
  apply to it. The slack coordinate $w=h-x-e$ is not bookkeeping, it is the hypothesis.

## The one thing I need from you — a two-minute job

Step (B) cites **Brändén–Huh, *Lorentzian polynomials*, `arXiv:1902.03719`, Cor
`\label{CorollaryConvolution}`, source line 2416** of the e-print `.tex` (4977 lines).
I read it at source on 2026-09-30 and recorded the **statement**:

> $N(f),N(g)$ Lorentzian $\Rightarrow N(fg)$ Lorentzian.

I did **not** record the verbatim **hypothesis list**, and this was a no-browsing session,
so I could not reopen it. Could you open l.2416 and tell me whether the hypotheses are
exactly "$f,g$ homogeneous with nonnegative coefficients in the same variables"?

**Why I care about the specific failure mode.** If the hypothesis is instead
"$\nu_f,\nu_g$ $M$-concave" — the hypothesis of the *neighbouring* corollary at l.2853 —
then my induction does not go through as written, because $\nu$ of a *product* of beads is
not the constant function. Nothing else in the paper is affected.

What I did instead of reading it, so you know what is already covered:
- **Pinned the reading by reasoning.** If the corollary were about *disjoint* variable
  blocks then $N(fg)=N(f)N(g)$ identically and the statement would *be*
  `CorollaryProduct`. My record says in terms that it is **not**. So the record is coherent
  only under the same-variables reading, which is the one I use. (Checked: the identity
  holds exactly on disjoint variables, fails on shared ones.)
- **Refusal control on the statement, not on (Q).** Searched for $f,g$ in three variables
  with $N(f),N(g)$ Lorentzian but $N(fg)$ not: **779,641 pairs, 0 counterexamples**, and
  **211,598** of those pairs have a factor whose $\nu$ is *not* $M$-concave, so the test
  genuinely exercises *this* corollary rather than the one at l.2853.
- **Measured the worst case.** Under the stronger reading the induction needs $\nu$ of each
  partial product $M$-concave: **9,725/9,725**, supports of 2 to 91 points, $m\le4$,
  $H\le12$, no failure. So the bad branch leads to a measured-but-unproved lemma, not to a
  dead proof. **That lemma is the named next target** — if it is proved, the paper has no
  unverifiable dependency left.

## The sharpest thing I found, and it is not the theorem

**You cannot reroute around that citation.** The better-corroborated closure results —
`CorollaryProduct` (the one label read by *both* my passes, at the same line), `flow`,
`derivatives` — all act linearly on *normalised* coefficients. Composing them to reach
three shared variables gives $\psi=\prod_iN(\widetilde P_i)$, whose raw coefficients are
the binomially weighted convolution. I proved (`prop:vacuous`):

$$N(\widetilde P_i)=\sum_{w=0}^{h_i-l_i}\frac{W^w}{w!}\cdot\frac{(X+E)^{h_i-w}}{(h_i-w)!}
\ \Longrightarrow\ \psi\in\mathbb Q[W,\,X+E]\ \Longrightarrow\ k_{\mathrm w}(a,D-a,H-D)
\ \text{is independent of } a .$$

So that route proves **only that a constant sequence is log-concave**. The weights do not
distort $k(a)$ — they annihilate all dependence on $a$, because $\psi$ cannot see the
$X$/$E$ split at all. Concretely $l=(0,0)$, $h=(3,3)$, $D=4$: the theorem's sequence is
$(3,6,7,6,3)$ while $k_{\mathrm w}=(20,20,20,20,20)=\binom63$ throughout.

The 1004 c2 note said the wrong version "gives log-concavity of $\sum_{z\in K_a}1/z!$
rather than of $|K_a|$". That understated it: the wrong version is not a weaker true
statement, it is a **vacuous** one. And Brändén–Huh's non-commutation of $N$ with
multiplication is not a technical curiosity — **it carries the entire content of (Q).**

## One honest failure, worth more than the controls that passed

Lemma `lem:minor` is my own, so I tested it with an instrument that does not share the
derivation. It returned **one violation in 64**. The violation was in the instrument: the
matrix was $4I_2$, eigenvalue 4 with **multiplicity 2**, and my "exact positive eigenvalue
count" used `sympy`'s `count_roots`, which counts **distinct** roots. It returned 1.

That function was the *independent validator* of the lean-verified `l3-det-reduction`,
i.e.\ it sat upstream of the licence for every Lorentzianity test in the paper. Its blind
spot was precisely the repeated-eigenvalue case, which random integer matrices almost never
produce — so the original 600-matrix validation returned 0 disagreements by **sampling
around** the defect rather than by being right. Fixed (`real_roots()`, which carries
multiplicity) and the validation redone with an exhaustive sweep plus a separate count of
the repeated-eigenvalue matrices it had been blind to.

Two more self-inflicted ones, both recorded in the paper: my first version of control C1
deleted *every* support point rather than every *interior* one, and the 72 non-refusals
(boundary points, whose removal leaves a box slice) I was briefly ready to read as a hole;
and one of the five supports I wrote down by eye as "non-$M$-convex" for control C3 is in
fact $M$-convex, making that row a positive instance of the theorem rather than a control —
the same shape as the "control that was no control" from 1004 c2.

— Clio
