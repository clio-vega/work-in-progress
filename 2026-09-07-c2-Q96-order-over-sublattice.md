# Q96 — the order stays infinite, and the base can shrink to a single generator

**7 September 2026, PROVE (c2).**
Paper: https://github.com/clio-vega/proofs/blob/089bffd/2026-09-07-c2-Q96-order-over-sublattice.tex
(9 pp, compiles clean — 0 errors, 0 undefined refs.  PDF beside it.)
Code: https://github.com/clio-vega/proofs/tree/089bffd/q96
Registry: `clio-vega/proofs@143197f`, 13 new nodes under `Q84-ord-R-e-all-specialisations`; trustcheck OK.

## The question and the answer

$R_e(t)$ adds a connected $e$-ribbon weighted by $t^{\mathrm{ht}}$. I proved last week that it has
infinite differential order over the full base $\Lambda$ — it is not a differential operator at all.
Q96 asked whether that was an artifact of measuring the deformation against *all* the power sums:
shrink the base to $\Lambda^{(e)} = \mathbb{Q}(t)[p_e, p_{2e}, \dots]$, the sublattice where Leclerc's
$q$-deformation lives, and does the order become finite?

**No — and by a wide margin.** The order is infinite already over $\mathbb{Q}(t)[p_e]$: one generator,
the smallest base for which the question isn't vacuous. Order is monotone *decreasing* in the base,
so $\Lambda^{(e)}$ and $\Lambda$ come for free. The witness is one line:

$$\langle s_{((d+1)e-1,\ 1)},\ \mathrm{ad}(M_{p_e})^d\big(R_e(t)\big)\,s_\varnothing\rangle \;=\; (-1)^d\,(1+t)
\qquad (e \ge 2,\ d \ge 1).$$

The deformation away from $t=-1$ is genuinely transverse to the sublattice. The anchor's specialness
is not a choice of coordinates.

## Why it turned out to be short

I expected a long route-counting fight. Instead the channel collapses. For the source $\varnothing$ and
that hook target there is **exactly one** legal sequence of $e$-moves on the abacus, and it is unique as
an *ordered* sequence:

- Each move preserves the residue class mod $e$, and the net occupancy change is a divergence. In every
  class but one the divergence vanishes, and zero divergence with finite support forces zero moves. In the
  surviving class the divergence pins the multiset exactly — $d+1$ moves, one per step.
- Legality then orders them: for $k \ge 1$ the site $-2+ke$ is unoccupied to begin with, so move $k$ can
  only follow move $k-1$.

So the matrix element is a $(d{+}1)$-term alternating binomial sum in which only **two** weights appear:
$t$ (the first hop, whose window contains the bead at $-1$) and $-1$ (every later hop, whose window is
empty). The sum collapses to the single correction term. That's the whole proof.

The trick is entirely in *where the walk starts*. Start the bead at $-1$ instead of $-2$ — the single-row
target, the obvious first thing to try — and every window sits at non-negative sites, is empty, all weights
are $1$, and the sum is $0$ for every $d$. That channel is perfectly correct and completely blind. I wrote
it into the paper as a remark, because it is the one you reach for first.

## Two things you may want to push back on

**1. Your reduction was right, and I checked it before building on it.** $M_{p_e} = R_e(-1)$ by
Murnaghan–Nakayama, so every multiplication operator generating $\Lambda^{(e)}$ is a ribbon operator at
the anchor. I re-verified it in the first twenty minutes against a third engine that shares no code with
the abacus — Jacobi–Trudi in $\mathbb{Q}[p_1,p_2,\dots]$, multiply by the *symbol* $p_e$, re-expand.
29/29.

**2. Negative control 1 in the brief is misstated, and I'd like you to know I checked at source rather
than around it.** The brief says $e=1$ must return $\infty$, "the Q84 answer". It must not. Q84's Theorem A,
Theorem B and Corollary 4.9 all carry the standing hypothesis $e \ge 2$, and at $e=1$ a border strip of
size 1 is a single cell of height 0 — so $R_1(t) = M_{p_1}$ is $t$-independent and has order **0** over
every base. It is still a genuine control (0 versus $\infty$, and my machinery does return 0 there), and
the proof localises the failure precisely: the weight lemma needs $e \ge 2$ for $-1$ to lie in the first
window. Only the expected value was wrong.

## The pin was innocent — and I think that matters

Q84's proof iterated $\mathrm{ad}(M_{p_1})$, and $p_1 \notin \Lambda^{(e)}$ for $e \ge 2$. That is exactly
why Q96 was open rather than a corollary, and the brief flagged it as the fifth firing of "a fixed
parameter can be the whole obstruction."

It wasn't. The same phenomenon is visible against $M_{p_e}$ alone. Better: the new witness **re-proves
Q84's Corollary 4.9 uniformly in the parameter**, including the scalar $c=0$ — the case Q84 needed an
entire second theorem for, because there the leading route weight degenerated. Here $c=0$ gives
$(-1)^d$, visibly nonzero.

So the heuristic has a negative half I hadn't recorded: *checking whether the pin is load-bearing is
cheap, and sometimes the answer is that it never was.* When it isn't, you usually get a shorter proof of
the old theorem as change.

## Side result: the two-parameter commutator

The brief asked for $[R_e(t), R_f(s)]$ — one parameter per operator. It's in §4, closed form, both
sectors, verified on **1829/1829** matrix elements ($1 \le e,f \le 4$; all 30 partitions $|\lambda| \le 6$;
every nonzero target). Two things are worth your eye:

- **The two-bead sector depends on $(t,s)$ only through the product $ts$**, as
  $\sum_{\text{legal assignments}} t^{P-k}s^{Q}(1-(ts)^k)$, and vanishes identically exactly on the locus
  $ts = 1$. That is a *second* distinguished locus for the family, alongside $s=t$; the anchor $t=s=-1$
  lies on both. I have not looked at what survives there — flagged as open, not examined.
- **The one-bead sector is a two-coloured dressing.** Each term dresses the interval $(a, a+e+f)$ with
  $t$ on the sub-interval traversed by $R_e$ and $s$ on the one traversed by $R_f$ — and the two orderings
  split the interval at *different* points ($a+f$ versus $a+e$). At $s=t$ the colours merge and the clean
  one-parameter form $-\frac{1+t}{t}\Phi_{e,f}$ appears. When $s \ne t$ there is no collapse. That merge
  failing is, I think, the real structural reason a change of parameter can't be gauged away here.

**And a correction to my own Q92 paper.** Its clause "if $e=f$ the two-bead element is 0" is a
*one-parameter* statement: at $e=f$ **two** assignments are legal, and they cancel only when $s=t$. With
$t \ne s$ the sector is nonzero — e.g. $(t-s)(1-st)$. I found this because a first version of the formula
imported the clause verbatim and the sweep reported exactly 61 disagreements; all 61 were $e=f$ two-bead
entries. The count named its own cause. I've fixed the reading and recorded it in the registry.

## Honesty notes

- **No literature claim is made anywhere in the writeup.** No source was read this session beyond my own
  earlier files. Nothing above asserts priority or novelty about anything.
- The argument never passes through Lam's LLT map $\Phi$. It couldn't: $\Phi$ sends these operators to
  multiplication operators, which have order 0, so an argument routed through it could not tell order 0
  from order $\infty$. Everything here is legal $e$-moves on Maya sets, the height statistic, and a
  binomial identity. Stated explicitly in the paper.
- One instrument failure, recorded in the paper. The abacus-free cross-check returned $-2$ where the
  theorem predicts $-t-1$. $-t-1$ at $t=1$ *is* $-2$: the coefficient extractor used
  `as_coefficients_dict`, which returns only the numeric part and had silently dropped the symbolic $t$.
  The instrument was wrong, not the claim. Rewritten; 5/5 after.

## What this closes, and what it doesn't

**Closes:** the reading of Q96 under which a "yes" would have given Q91 a conditional normal form over
$\Lambda^{(e)}$. Whatever normal form $R_e(t)$ has, it is not one with finitely many $\partial_{p_{me}}$.

**Leaves open, and I did not attempt:** $\mathrm{ord}_{(e)}(R_g(t))$ when $e \nmid g$ — the flow argument
needs every move to have the same step size, and with two sizes the multiset is no longer forced by
divergence alone; and the meaning, if any, of the $ts=1$ locus.
