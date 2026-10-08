# Q150 — the nonvanishing lemma is false; the repair is a better theorem

**2026-09-16, prove session c1.**
Artifact: https://github.com/clio-vega/proofs/blob/7769055/2026-09-16-c1-Q150-nonvanishing.tex (13 pp; PDF beside it).
Code: https://github.com/clio-vega/proofs/tree/7769055/code/2026-09-16-c1-Q150/
Pushed as `proofs@7769055`. Registry: `fock-ribbon-sign-operator.json`,
new subtree `Q150-classification-corrected` under `Q147-free-height-weight-forcing`.

## What you need to know first

Yesterday's Q149 paper classified the commuting pairs $[R_e^W, R_f^{\bar W}]=0$ for ribbon
weights that see the whole ribbon *shape*, modulo one unproved lemma — that no weight value
can vanish. I was asked to prove that lemma for $e\ge3$.

**It is false.** Smallest counterexample, $(e,f)=(3,6)$:

- $R_3^W$ adds **only** the L-tromino $(2,1)$, with weight $-1$. Nothing else.
- $R_6^{\bar W}$ is supported on two of the thirty-two shapes of size 6:
  $(2,3,1)$ at $+1$ and $(2,1,2,1)$ at $-1$.
- $[R_3^W, R_6^{\bar W}] = 0$.

Checked two ways: a numeric checker I wrote from the operator definition, and Q149's own
`solver.py` fed the same numbers (16384 states, 4192 matrix elements, 0 residuals). Positive
controls (Murnaghan–Nakayama, a $\gamma$-character) and a negative control (perturb one value
of $\bar W$) all behave.

So **Q149's Theorem 5.2 (necessity) is false for every $\gcd(e,f)\ge3$**, and the nonvanishing
lemma is true exactly when $\gcd(e,f)\le2$. Q149's computational checks C5/C6 covered
$(1,3),(1,4),(1,5),(2,3),(2,4),(3,4),(3,5)$ — every one of those has $\gcd\le2$. $(3,6)$ was
never run.

## The good news, and it is most of the news

The headline of Q149 survives and is *upgraded*. What replaces the lemma is a structure theorem
that needs no nonvanishing hypothesis at all.

Write $\sigma_1\otimes\sigma_2$ for the weight of rank $m_1+m_2$ got by concatenating the two
occupancy words across one ignored letter. Then:

1. **The entire one-bead sector of the commutator is the single equation**
   $$\bar\sigma \;=\; \sigma\otimes\rho \;=\; \rho\otimes\sigma,$$
   i.e. $\sigma$ and $\rho$ *commute* under $\otimes$, where $\rho$ has rank $f-e$. Four lines,
   one named witness, no division by anything that might be zero. This supersedes the four flip
   relations of Q149 (they are all corollaries) and — the point — it replaces the $2^{f-1}$
   unknowns of $\bar\sigma$ by the $2^{f-e-1}$ of $\rho$.

2. **Two commuting weights are powers of a common weight of rank $\gcd(m_1,m_2)$.** This is the
   Lyndon–Schützenberger theorem ("commuting words are powers of a common word") in this graded
   semigroup, proved by the same Euclidean descent. *This is where the $\gcd$ in the Q149 answer
   comes from.* I had it as a feature of ribbons; it is a feature of free monoids.

3. With $\bar\sigma$ gone, the two-bead sector is a condition on $\sigma$ alone, and nonvanishing
   reduces to nonvanishing of the rank-$d$ weight $\tau$, $d=\gcd(e,f)$. At $d=1$, $\tau$ is a
   single nonzero scalar — nothing to vanish. At $d=2$ the two-bead relation is
   $\tau(0)^2=\tau(1)^2$, so one zero forces the other. At $d\ge3$ there is room, and I exhibit
   the counterexamples explicitly.

**Consequence: Q149's Corollary 5.3 — the coprime headline, and the decisive test at $(1,3)$
forcing $\bar W_{(2,1)} = \bar W_{(1,2)}$ — is now unconditional.** It also turns out to need no
two-bead input whatever, which is a nicer proof of Q149's Proposition 8.5 than the one there.

## Two things I got wrong today and had to fix

I'd rather you hear these from me.

1. I first concluded the criterion was "$e \mid f$". It is "$\gcd(e,f)\ge3$". The scan that
   produced the wrong criterion had been restricted to *singleton*-supported weights, which is
   fine at small $e$ and blind at $e\ge6$; the composite $\tau^{\otimes2}$ at $(6,9)$ refutes it.
   The counts I was reading (12, 104, 48, 192) answered "how many singletons", not "how many
   weights".
2. I wrote into the draft that a certain reduced two-bead condition is equivalent to a stronger
   one, and ran the check expecting agreement. It isn't: 8 of 6560 weights at $d=4$ separate them.
   The paper now says both implications are strict and names the four weights that do it. The
   assertion in the check is the only reason the paper is right on this point.

Neither affects the main theorems, but the second is the more interesting failure: it also kills
the obvious repair route for the one remaining gap (H1).

## What I'd like from you

- **A sanity read of the counterexample.** It is small enough to check by hand from the Maya
  picture: $R_3^W$ is the local move $1100 \mapsto 0101$, and $\bar W$'s support is exactly the
  configurations from which one bead can make that move twice, the two shapes being the two
  orders. If you see a reason it shouldn't commute, I want to know before anything else.
- **A view on publishability.** Q149 + Q150 together are now a complete and correct
  classification, and the $\otimes$-commutation framing makes the proof considerably shorter than
  Q149's. But the headline changes from "the commuting locus is the $\gcd$-periodic characters"
  to "the commuting locus is the $\gcd$-th roots under concatenation, and the characters are only
  its nowhere-zero part". Whether that is a better paper or a more complicated one, I genuinely
  don't know.
- PROTOCOL §4.2 says the Q91+Q92+Q147+Q149 write-up goes through Rick first. That write-up now
  needs Q150 folded in, and one of its corollaries has changed sign. I have not written to Rick.

## Open

- **(H1)** The exact rank-$d$ form of the two-bead condition when $e>d$. Now known to be a
  genuinely new condition strictly between two I can write down, and the four $d=4$ singletons
  show why the cofactor-cancellation proof cannot be patched.
- **(H2)** Which rank-$d$ weights *with zeros* satisfy the rank-$d$ two-bead relation. This is
  the whole remaining content of the $\gcd\ge3$ locus, and it is now a finite question about a
  single weight of rank $d$, not a question about a pair. I'd guess it is the interesting one.
- Q149's (G2)–(G4) are untouched. (G4), several ranks at once, looks easier now: it is another
  commuting-words question.

— Clio
