# Q149 — shape weights force a transpose-equivariant gcd-periodic character

**2026-09-15, prove session c1.** Artifact:
https://github.com/clio-vega/proofs/blob/main/2026-09-15-c1-Q149-shape-weights.tex
(14 pp, compiles clean; PDF beside it; code in `code/2026-09-15-c1-Q149/`; commit `fbc777b`).

## What was asked

Gap (1) of my Q147 note. Q147 showed that giving each ribbon *height* its own free weight
does not loosen the cross-rank commutator: $[R_e^w,R_f^{\bar w}]=0$ still forces
Murnaghan–Nakayama. The obvious next hypothesis to test is not a parameter but a **form**:
does the weight need to see only how many rows the ribbon has? So let the weight see the
whole **shape** — $2^{e-1}$ parameters, one per composition of $e$, instead of $e$.

## The answer

Index the weight by the occupancy word $u\in\{0,1\}^{e-1}$ of the interval $(b,b+e)$
(equivalently by the ribbon's row-length composition). With $d=\gcd(e,f)$ and $K$ a domain:

$[R_e^W,R_f^{\bar W}]=0$ iff one weight vanishes identically, or

$$W(u)=\alpha\prod_{j=1}^{e-1}\bigl(-\gamma(j\bmod d)\bigr)^{u_j},\qquad \bar W \text{ likewise, same }\gamma,$$

for some $\gamma:\mathbb Z/d\to F^\times$ with $\gamma(0)=1$ and $\gamma(\delta)\gamma(-\delta)=1$.

Said structurally: **the weight must be a multiplicative, $d$-periodic character of the
occupancy word which is equivariant under transposing the ribbon.** The one-bead sector of
the commutator contributes "multiplicative + $d$-periodic"; the two-bead sector contributes
"transpose-equivariant".

## Three things I think are worth your time

**1. The division of labour inverts Q147.** In Q147 the one-bead sector was the strong one —
it forced the anchor outright — and the two-bead sector only gave multiplicativity. Here the
one-bead sector is *blind* to $\gamma$: it imposes nothing beyond $\gamma(0)=1$, and the
entire cut is made by the two-bead sector. Which explains why nobody would see this at
$\min(e,f)=1$: there is no two-bead sector there, and $d=1$ anyway.

**2. The sign was never the content.** Substituting $\sigma(u)=(-1)^{|u|}W(u)$ makes *both*
sectors' matrix elements sign-free — every equation becomes a difference of two products
with $+$ signs. The alternating Murnaghan–Nakayama sign is a change of coordinates the
commutator cannot see. This is the cleanest statement I have of why "the MN sign is not a
choice of parameter": it is not a parameter at all.

**3. For $\gcd(e,f)>1$ the locus is genuinely bigger — and genuinely tame.** At $(3,6)$ a
symbolic one-parameter family $\gamma=(1,t,t^{-1})$ annihilates the commutator *identically
in $t$*. But every point of it is Murnaghan–Nakayama seen through a $d'$-quotient — the
operators become $\sum_r p_{e/d'}$ and $\sum_r p_{f/d'}$ on the runners, which commute
because power sums do — or a diagonal gauge of one. I give the gauge explicitly:
$D=\mathrm{diag}\bigl(\prod_\delta x_\delta^{\Lambda_\delta(M)}\bigr)$ where
$\Lambda_\delta(M)=\#\{(i,j):i<j,\ i\notin M,\ j\in M,\ j-i\equiv\delta \bmod d\}$, which is
finite because $i\notin M$ is bounded below and $j\in M$ bounded above. Your instinct in the
brief — that a residual should be tested for gauge before being celebrated — was right, and
the gauge group turned out to be **larger** than the back-of-envelope in the brief suggested
(that one gave only global rescaling).

## Two corrections to the brief, both caught by controls

- The word↔composition dictionary in the brief dropped a **reversal** (in beta-coordinates a
  larger bead sits in an *earlier* row). The Young-diagram-vs-Maya cross-check failed on its
  very first case. Without the reversal the two L-trominoes exchange names — precisely the
  distinction the session was about.
- The brief said ribbon transposition is **reversal** on compositions. It is **reversal
  followed by complementation**, $(u^T)_i=1-u_{e-i}$; plain reversal agrees on only 75 of
  765 tested ribbons. So the induced $\mathbb Z/2$ does *not* fix height-only weights
  pointwise (it acts by $w_N\mapsto w_{e-1-N}$) and does *not* swap the L-trominoes: for
  $e=3$ it fixes both and swaps $(3)\leftrightarrow(1,1,1)$. This one mattered — transpose
  equivariance is the two-bead condition.

## The gap, precisely

The necessity argument forms ratios $\sigma(u|u_j{=}1)/\sigma(u|u_j{=}0)$, so it needs:
*if neither weight vanishes identically, then no individual value vanishes.* I prove this
for $e\le2$. For $e\ge3$ the induction does not terminate — the two-bead relation shows the
zero set of $\sigma$ is flip-closed at position $\delta$ unless $\bar\sigma$ vanishes on a
cylinder, and the cylinder produced has length $e-\delta$ rather than $e-1$. It is verified
exhaustively over $\mathbb F_p$ for $(1,3),(1,4),(1,5),(2,3),(2,4)$ (solution set *equals*
the predicted set, no extras, no missing, degenerate strata included) and by ideal
saturation at $e=3$ for $(3,4),(3,5)$. I would like a clean argument; I suspect it is two
lines and I am not seeing them.

A second, smaller gap: the $\mathbb Z/2$ at $\delta=d/2$ (even $d$) is *not* in the image of
my explicit gauge, but a spanning-tree cocycle test says it is gauge anyway — 0 violations
over ~150k edges, against non-commuting controls that fire ~49k times. For $d=2$ I can see
the statistic (a cross-runner inversion number) but have not written its regularisation.

## Question back to you

Is the "multiplicative + $\gcd$-periodic + transpose-equivariant" trio a known shape
anywhere? It smells like a Klein-factor / statistics-twist condition on the $d$-quotient
tensor decomposition, and $\gamma(\delta)\gamma(-\delta)=1$ is exactly the condition for the
twist to cancel between two different runners. If that is a recognised gadget under another
name, the $d>1$ half of this is somebody's lemma and I should cite it rather than re-derive it.
