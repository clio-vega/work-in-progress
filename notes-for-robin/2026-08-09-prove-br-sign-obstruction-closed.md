# PROVE 2026-08-09 — BR sign-obstruction theorem CLOSED

**Result.** The Bhattacharya-Rhoades sign-obstruction hypothesised in
today's WAKE (from the empirical $(6,3)$ probe finding) now proved as a
general theorem, in a cleaner and stronger form than PROVE.md suggested.

## Theorem (final form)

Let $e \ge 2$, $n = e k'$ with $k' \ge 2$. For every $r \ge 1$ and $0 \le k \le n$,
let $M_{n,r}^{(k)}$ be the fermionic-degree-$(n-k)$ slice of Bhattacharya-
Rhoades $SR_{n,r}$, restricted to $S_n$. Let $q_e^{(n)} := p_e^{k'}$. Then
$$q_e^{(n)} \;\notin\; W_n^{\mathrm{BR}} := \mathrm{span}_\mathbb Q\{\mathrm{Frob}(M_{n,r}^{(k)}): r \ge 1, 0 \le k \le n\}.$$

Moreover $W_n^{\mathrm{BR}} = W_n := \bigoplus_{\ell=1}^n \mathbb Q \cdot P_\ell$
where $P_\ell = \sum_{\ell(\mu)=\ell} \varepsilon(\mu)/z_\mu \cdot p_\mu$.
So $\dim W_n^{\mathrm{BR}} = n$ (INDEPENDENT of $r$), codim $= p(n) - n$.

The explicit functional $L_\nu(\phi) = z_{(e^{k'})}/\varepsilon((e^{k'})) [p_{(e^{k'})}]\phi
- z_\nu/\varepsilon(\nu) [p_\nu]\phi$ (with any $\nu \ne (e^{k'})$ of length $k'$,
e.g. $\nu = (e+1, e^{k'-2}, e-1)$) annihilates the entire BR span and
detects $q_e^{(n)}$ with value $z_{(e^{k'})}/\varepsilon((e^{k'}))$.

## What's new / stronger than PROVE.md predicted

1. **All $r \ge 1$, not just $r \ge e$.** The obstruction is uniform in $r$;
   composite-$d$ hypothesis $r \ge e$ was overly conservative.
2. **The span has closed form** — $n$-dim polynomial-in-$m$ image via
   generating function $\bar E^m$. This is the KEY structural insight PROVE.md
   was reaching for but hadn't isolated.
3. **The Kostka argument was NOT the right one.** The obstruction is not
   Kostka-cone (nonnegativity) but the length-graded structure of $\bar E^m$.
4. **The proof is 6 pages, single clean argument** via three
   propositions: (i) generating function $[x^n](\bar E^r - 1)^k \bar E^{r-1}$;
   (ii) power-sum expansion $F_m = \sum \varepsilon(\mu) m^{\ell(\mu)}/z_\mu \cdot p_\mu$;
   (iii) length-support analysis of $W_n$.

## Key insight

The BR wreath superspace is, in Frobenius language, a plethystic-
exponential machine: $r$ colors + $k$ ordered blocks + $Z$-block gives the
generating function $(\bar E^r - 1)^k \bar E^{r-1}$. Sums (via $r, k$) span
only the "length-graded" image of $\bar E^m$, which is exactly
$n$-dimensional.

$q_e^{(n)} = p_{(e^{k'})}$ is a DELTA at one partition of length $k'$.
BR gives a SMOOTHED-OUT length-$k'$ combination of the form
$\alpha \sum_{\ell(\mu)=k'} \varepsilon(\mu)/z_\mu \cdot p_\mu$. Delta $\ne$
smoothed sum unless the length class is a singleton (which requires $k' = 1$).

So: **composite-$d$ has $k' \ge 2$ precisely means length class $\{\ell(\mu) = k'\}$
has $\ge 2$ elements, which is exactly what fails BR.**

## What this teaches us about composite-$d$

The virtual-character theorem (yesterday) said: composite-$d$ has mixed Schur
signs. Today: even after allowing arbitrary multiplicities via BR permutation
representations, no signed linear combination reaches it. **This is a
STRONGER obstruction** — it rules out virtual-character realisability from
the entire BR family, not just individual modules.

More importantly, it shows the obstruction is **length-cycle-type mismatch**:
BR sees only length-graded structure; $q_e^{(n)}$ demands cycle-type-graded
resolution. These are different filtrations of $\Lambda_n$, and the finer
one (cycle-type) can't be captured by the coarser one (length).

## For post-v1 v2

This theorem RULES OUT the entire BR family. Post-v1 v2 direction must:
1. Go beyond permutation-rep-like structure (which forces length-graded);
2. OR find a construction whose Frobenius family spans a DIFFERENT subspace
   of $\Lambda_n$ — one that includes at least one partition of length $k'$
   in isolation.

Candidates that MIGHT survive this criterion:
- **DAHA at $\zeta_e$** (Etingof-Ma): rational Cherednik with cyclotomic
  parameter, NOT a permutation-rep family. Whether its Frobenius family lies
  in span$\{P_\ell\}$ is not immediate. **Highest-priority v2 target.**
- **BGG complex + Euler characteristic** (Johnson-Freyd MO 56188 idea):
  $q_e^{(n)}$ as $\sum (-1)^i \mathrm{Frob}(M^i)$; each $M^i$ is a genuine module,
  Schur-positive individually, but signed alternating sum picks up mixed
  signs. Does the alternating sum lie in $W_n$? Probably not — but need to
  check what family of Frobenii the BGG family spans.
- **Colored fermionic vertex model** (Aggarwal-Borodin-Wheeler): physics-side
  fermionic. Whether its transfer-matrix Frobenii live in $W_n$ requires
  computation.

## The empirical $L_1, L_2, L_3$ from today's probe

Confirmed to lie in the annihilator of $W_6$. They're Schur-basis functionals
which are $\mathbb Q$-linear combinations of the length-2 sign-ratio
detectors from the theorem. This shows the empirical finding was the
codimension-5 shadow of the codimension-$(p(6)-6)=5$ structural fact.

## Robin: what to look at

**Standalone proof:** `proofs/2026-08-09-br-sign-obstruction.{tex,pdf}` (6pp).

**Verification scripts:** `proofs/2026-08-09-br-work/`
- `verify_gf.py`: generating function identity at $(6,3)$.
- `verify_span.py`: rank $=n$ verified at $n \in \{4,5,6,8,9,12\}$; obstruction
  verified at 9 cases $(n,e)$ from $(6,2)$ to $(12,6)$.
- `verify_probe_L.py`: empirical $L_1, L_2, L_3$ annihilate all $P_\ell$ at $n=6$.

**Composite-$d$ has EIGHT proved theorems** now (previous count 7, add BR
sign-obstruction).

## v1 arXiv push

**STILL UNBLOCKED 10th day.** v1's §6 already gets both:
1. Yesterday's virtual-character sign-pattern theorem (closed formula for
   Schur coefficients);
2. Today's BR sign-obstruction (uniform-in-$r$ non-realisability).

The two theorems compose cleanly: (yesterday) $q_e^{(n)}$ has mixed signs
$\Rightarrow$ no single $S_n$-module hosts it; (today) even $\mathbb Q$-signed
sums of BR fermionic slices can't reach it. §6 becomes 2-3pp with:
```
Theorem A (yesterday): closed Schur formula with mixed signs.
Theorem B (today): BR uniform non-realisability with explicit functional.
Corollary: post-v1 v2 must go outside permutation-rep-like families.
```

**STRONG RECOMMEND push v1.**

## Aesthetic note

I like this one. The proof is short, the mechanism is clean, and the "why"
is transparent: BR sees length; composite-$d$ demands cycle type. Two
different filtrations of $\Lambda_n$, one strictly finer than the other,
and the obstruction is the mismatch in resolution.

The Levi-stability coordinating-theme reading applies again: BR is "one
level of resolution below" what composite-$d$ needs. Every module-family
Clio has tested this month has fallen at the same abstraction step. That's
suggestive of a theorem: **any Frobenius family generated by "sums over
combinatorial families with $S_n$-permutation structure" lies in some
length-graded subspace of $\Lambda_n$; composite-$d$ demands cycle-type-
graded resolution, which permutation structures cannot provide.** Post-v1
essay direction.
