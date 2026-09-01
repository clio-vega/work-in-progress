# Q63 — the level-ℓ telescope

**Grade: `proved` for the telescope; `computed` for the deformed dichotomy.**

Does the Q59 closed form $[e_i,R_e(t)]_{\nu\lambda}=\varepsilon q^kt^b(1+qt)$ survive to
Uglov level $\ell\ge2$?

**Proved.** The level-$\ell$ Chevalley weight is $\ell$ per-runner step-$e$ telescopes
**plus** a cross-runner tie term $\tau$ with $|\tau|\le\ell-1$, supported at one shifted
content. 36 816 checks, 0 failures; the $\ell=1$ reduction is exact (350/350).

**Refuted, exactly.** Hypothesis (H3) — that the telescope decomposes per runner with no
cross-runner term — fails on precisely the 10 888 cases with $\tau\neq0$, and on no others.
It was stated as an explicit hypothesis before being built on. The refutation is the result.

**Proved, and the more consequential half.** Uglov's $B^{[e]}_{-1}$ at $\ell\ge2$ is *not*
a sum over single-bead moves: it carries cross-component terms, all $(q-q^{-1})$-divisible.
So the interpolation $R_e(-q)=P_e$, $R_e(-q^{-1})=B_{-1}$ that *defines* Q59's object has
**no level-$\ell$ analogue**, and the dichotomy at level $\ell$ is a statement about an
operator no longer known to be the representation-theoretic one.

**Named gaps, ranked, in §gaps of the paper.** (1) the deformed dichotomy is `computed`, not
proved; (2) the conjecture $j=1+\Delta\tau$ is supported *only* by the range of $j$ — the
entry-by-entry check was not done, and it is the cheapest next step; (3) **the wedge/Fock
normalisation is unresolved** ($[e_i,B_{-1}]\neq0$ on 13 of 126 cases, an unidentified
$q$-power not absorbed by any normalisation linear in component sizes) — this must be settled
before any quantitative claim about $B_{-1}$ at level $\ell$; (4) all sweeps have $|\lambda|\le4$.

**The observation the paper is really about.** Every deviation from level 1 is proportional
to $(q-1)$ and vanishes at $q=1$. That is a *mechanism* for the obstruction recorded twice
independently in the literature (Hill, MO 41033; arXiv 2505.07806 Rem 4.2) — crystal-limit
arguments stop working at the crystal limit. The level-1 theory is not wrong at level $\ell$;
it is its $q\to1$ shadow, which is exactly why level-1 work can never see level-$\ell$
phenomena.
