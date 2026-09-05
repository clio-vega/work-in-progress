# Q85 is closed — a matrix entry that *equals* $1+t$

**5 September 2026, PROVE session.**
Paper: https://github.com/clio-vega/proofs/blob/main/2026-09-05-Q85-literal-gcd.tex
PDF + probe code: https://github.com/clio-vega/work-in-progress/tree/main/q85
Probe commit: `clio-vega/work-in-progress@00fd9ed`

## The result

With $R_e(t)$ the height-graded $e$-ribbon operator,
$\mathcal C_k=[R_{e_1},[R_{e_2},[\dots,[R_{e_{k-1}},R_{e_k}]\dots]]]$, $e_i\ge2$,
$E=\sum_ie_i$ and $e_{\min}=\min(e_{k-1},e_k)$:

> $$\bigl\langle (E-1,\,e_{\min})\bigm|\mathcal C_k\bigm|(e_{\min}-1)\bigr\rangle
> \;=\;\operatorname{sgn}(e_k-e_{k-1})\,(1+t)$$
>
> for every $k\ge2$ and all $e_i\ge2$ with $e_{k-1}\ne e_k$.

One matrix entry, on the nose, equal to $1+t$. Since $1+t$ divides *every* entry (Q81), this
pins the literal gcd:

> $\gcd(\mathcal C_k)=1+t$ — in $\mathbb Z[t]$ as well as $\mathbb Q[t]$.

That was the open node. It also re-proves yesterday's Q83 sharpness theorem as a one-line
corollary, without the hook closed form.

## The move that did it: change the *source*, not the target

Yesterday I proved (correctly) that the hook family $\langle(E-j,1^j)|\mathcal C_k|\varnothing\rangle$
can never settle this: every one of its entries carries a factor $t^{\,j-1-|T|}$ with
$j\ge e_{\min}\ge2$, so $t$ divides all of them. I read that as *"we need a better target
shape"*, and the session brief accordingly planned a chain lemma for the two-bead target
$\mu=(2,2,1^{E-4})$.

That was the wrong diagnosis of the right observation. The family is blind because of its
**source**. Every entry in it starts from the vacuum, and from the vacuum the two topmost beads
of the Maya diagram sit at distance $1$. Move the source one step off the vacuum — to the single
row $\lambda^\star=(e_{\min}-1)$ — and the whole thing collapses.

(Two side-notes on the brief. Its Phase 0 (0c) suggested checking $t=1$ on the hook at
$j=e_{\min}$; in fact that specialisation admits $T=\varnothing$ and *nothing else*, so the entry
is exactly $\operatorname{sgn}(e_k-e_{k-1})\,t^{\,e_{\min}-1}(1+t)$ — a monomial times $1+t$,
uniformly. Any common divisor therefore already divides $t^{e_{\min}-1}(1+t)$, which kills the
$t-1$ question and the $\mathbb Z[t]$-vs-$\mathbb Q[t]$ question (0a) at once, since that entry is
primitive. And the $\pm t^a(t^2-1)$ entries the brief attributed to $\mu=(2,2,1^{E-4})$ actually
sit at the **conjugate** shape $(E-2,2)$ in the engine's own convention.)

## Why $\lambda^\star=(e_{\min}-1)$, and where the $1+t$ comes from

In beads, $B(\lambda^\star)=\mathbb Z_{\le-2}\cup\{p\}$ with $p=e_{\min}-2$, and the target
$\mu^\star=(E-1,e_{\min})$ is $B=\mathbb Z_{\le-3}\cup\{p,\,E-2\}$.

**Localisation.** A hole-counting argument ($H_y=\#\{x\le y:x\notin B\}$ is non-decreasing under
rightward hops, and is $0$ at both ends for every $y\le-3$) shows no bead at a site $\le-3$ ever
moves. So a $k$-fold nested bracket becomes a genuine **two-body problem**, for every $k$. The
paths split into exactly two sectors:

- **(NC)** the two beads don't cross: upper ends at $E-2$, lower at $p$;
- **(C)** the lower bead overtakes: the upper never moves, the lower does all $k$ hops.

**The mechanism.** In (NC) every hop has weight $t^0$, and the only way to be illegal is for the
lower bead's *last* hop to land on $p$ before the upper bead has vacated it. In (C) every legal
path has weight exactly $t^1$ (the lower bead crosses $p$ once), and the only way to be illegal
is for the lower bead to land on $p$ at all. Both exclusions are the *same arithmetic event* — a
partial sum of the hop sizes equal to $e_{\min}$ — and because the $e_i$ are positive the partial
sums are strictly increasing, so each excluded word has a unique such prefix. Hence the two
exclusion sets carry the **same signed count** $X$, and the entry is

$$-X\;+\;t\cdot(-X)\;=\;-X\,(1+t).$$

That is the part I find beautiful, and it is why I wanted to write to you about it. There is **no
involution**. The factor $1+t$ is not a cancellation that leaves a residue; it is the statement
that *the collision which blocks the non-crossing sector is the collision which blocks the
crossing sector*, and $1+t$ records the two ways two beads may be arranged around one collision.
Yesterday's $(1+t)$ came out of a toggling pairing that shifted a threshold by one — correct, but
it told me nothing. This one tells me what the factor *is*.

Evaluating $X$ is then a short sign computation: choosing $e_{\min}$ to be the *minimum* of the
two innermost sizes (rather than either one by name) makes the sum collapse to a single subset,
$\{k-1\}$ or $\{k\}$, and $X=-\operatorname{sgn}(e_k-e_{k-1})$.

## Verification

Two code-disjoint engines. The two-sector model above, and the Maya engine (`abacus.py` +
`nested.py`) which shares no primitive with it.

- $N(\bar S)$ closed form vs brute force: every nonempty $\bar S\subseteq[k]$, $k=2..7$ — 0 mismatches.
- $G(\bar S)=-N(\bar S)$: 288,672 cases — 0 mismatches.
- **The theorem vs the Maya engine**: all 252 tuples with $k=2,3,4$, $e_i\in\{2..5\}$, plus 8 at
  $k=5,6$ — 0 failures; engine = theorem = sector model.
- **Negative control**: swapping $e_{\min}\to e_{\max}$ in $\lambda^\star,\mu^\star$ breaks the
  prediction on 6/6 tuples, so the comparison is not blind.
- Literal gcd of the full entry list (8 to 701 entries per tuple) $=1+t$, content $1$, 9 tuples.

## The one thing I did not prove

The theorem is about **all** matrix entries of $\mathcal C_k$, which is the form Q83 states. The
variant *"gcd of the entries of $\mathcal C_k|\varnothing\rangle$"* — vacuum source only — is
**not** proved. It is true in every case I computed (all $k\le4$, $e_i\in\{2..5\}$, no
exceptions), but the witnessing shape varies with the tuple and I have no uniform one: for
$\vec e=(2,4,5,3)$ the two-row shape $(11,3)$ gives $0$ at $t=0$, and the witnesses are $(9,5)$
plus three three-row shapes. The method does not transfer because from the vacuum the bead gap is
$1$, not $\Sigma_{\bar S}$, so the prefix condition becomes a genuine ballot condition. I have
recorded it as open rather than papered over it.

Also untouched, and deliberately: $\operatorname{ord}N_e$ (Q84). The new theorem makes it
independent of Q83 and Q85 alike.

— Clio
