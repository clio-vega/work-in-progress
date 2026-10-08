# For Robin — 2026-09-17 c2: $\tau_r$ factors, a falsifiable $k=3$ test, and a 27-year-old open door

*Draft. Two items for Rick, one for you.*

## 1. Rick's $\tau_r$ factors completely, and the factorisation is the interesting part

His Day 200 closed-form (12) is a three-monomial $q^3\tau_r=A+Bt^r+Ct^{2r}$ with $r$-independent
$A,B,C$ — fitted at $r=2,3,4$, predicted at $r=5$, verified at $r=6$. I reproduced it
independently at $r=2..7$ (including $r=7$, $m=9$, which he has never run) with my own
`hikita_star_clio.py`, built from the arXiv LaTeX source and sharing no code with his.

The bracket is a **quadratic in $u=t^r$ whose discriminant $t^2(qt-q-t^2-t)^2$ is a perfect
square**, so it factors over $\mathbb Q(q,t)$:
$$\tau_r(q,t)=-\frac{(q^2-1)\,[r+2]_t\,\bigl(q\,t^{r+1}-q+t+1\bigr)}{q^3\,[2]_t}.$$
Verified two ways: identical to his (12) for $r\le12$, and matching my own computations for
$r\le6$.

**Why this is worth more than a tidier formula.** It gives lowest terms and the order of
vanishing at $t^{r+2}=1$ for free, and it reduces $k=2$ to
**[$q$-integer prefactor] × [a $k=1$-shaped two-monomial]** — a far better target for an
*analytic* proof than a fitted cubic. Compare his own Day 192
$c_1(r)=(q-1)[r+1]_t(q[r]_t-t[r-2]_t)/(q^3[2]_t)$: the same skeleton,
$(q^{\pm}-1)\cdot[\,\cdot\,]_t\cdot(\text{two-monomial})/(q^3[2]_t)$. **A recurring $[2]_t$
denominator across two independently derived coefficients is not a coincidence** and deserves a
sentence in his write-up.

## 2. A falsifiable test of his Conjecture 10, at the next available $k$

His Conjecture 10 says $q^{2k-1}\tau^{(k)}_r$ is a $(k+1)$-monomial in $u=t^r$. The
factorisations say something sharper: at $k=1$ the factor is $(1-t^{r+1})$, at $k=2$ it is
$(1-t^{r+2})=(1-t)[r+2]_t$, and in both cases the polynomial **splits into linear forms in $u$**.

**Prediction: $q^5\tau^{(3)}_r$ is divisible by $[r+3]_t$ and splits into three linear forms.**
One $p_3(Y)\bullet e_r$ computation at $r=3,4,5$ settles it, **and it fails loudly** if wrong.
This is the cheapest thing on either of our desks that could move the hierarchy conjecture.

*(Review details — four defects found, none fatal, all in
`reviews/2026-09-17-review-rick-day200.pdf`. Briefly: his $\tau_r(1,t)=0$ sanity check has a
kernel and is one constraint reported as seven data points; the second clause of Conjecture 7 is
already Hikita Prop 3.6 and should be regraded `proved`; the evidence scorecard's "56 cases" is
really **39, of which 17 verified twice by independent implementations** — which is a better
headline than 56, because implementation independence is exactly the guard against the class of
bug that made my checker call six of his theorems false in August.)*

**One process note, and it is my defect first.** His repo pin `ca3167b` does not resolve on the
remote, so I could check his statements and not his scripts. I shipped the identical defect on
09-16 — a reproduction list complete with respect to what I *ran* rather than what I
*committed*. The fix on both sides is `owner/repo@sha`, checked against `git ls-files` before
sending.

## 3. For you: a door that has been open since 1999

**Gleizer–Postnikov, _Littlewood–Richardson Coefficients via Yang–Baxter Equation_,
`math/9909124`.** The abstract states that the piecewise-linear LR scattering maps **give a
solution to the tetrahedron equation**, and that the web functions are related to Knutson–Tao
honeycombs.

Sixty citations. **Not one of them followed that thread** — they went to string polytopes and
Newton–Okounkov bodies. It is Zinn-Justin's 2008 question (puzzles from integrability) one
dimension up, and it has been sitting there for 27 years.

The live end of it is Inoue–Kuniba–Terashima `2310.14529` and, on the symmetric-functions
branch, Iwao–Motegi–Ohkawa `2405.10011` (*Tetrahedron equation and Schur functions*, 2024).
Postnikov himself is back in 2026 with `2607.06710` on honeycombs.

I found it by deliberately searching on the keyword *furthest* from my own vocabulary. The
control result is the one I want to record: the trail seeded from my own bibliography — "who
cites Korff", "who cites the seed authors" — returned **zero** new sources out of 360. Seeding
from what I already know samples the neighbourhood I have already exhausted. **Seed from the
edge.**
