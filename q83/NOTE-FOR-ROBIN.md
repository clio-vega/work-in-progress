# Q83 is closed — and both hypotheses came off

**5 September 2026, PROVE session.**
Paper: https://github.com/clio-vega/proofs/blob/main/2026-09-05-Q83-sharpness-all-k.tex
PDF + probe code: https://github.com/clio-vega/work-in-progress/tree/main/q83
Commits: `clio-vega/proofs@936ca79`, `clio-vega/work-in-progress@486e7df`

## The result

For $R_e(t)$ the height-graded $e$-ribbon operator and
$\mathcal C_k=[R_{e_1},[R_{e_2},[\dots,[R_{e_{k-1}},R_{e_k}]\dots]]]$, with $e_i\ge2$:

> The $(1+t)$-adic valuation of the gcd of the entries of $\mathcal C_k$ is exactly $1$
> **if and only if $e_{k-1}\ne e_k$** — for every $k$, with **no distinctness** assumption on
> $e_1,\dots,e_{k-2}$ and **no condition** on where the largest size sits.

Yesterday's target asked for this under "pairwise distinct, and $\max\{e_i\}\ne e_1$". Both
hypotheses are gone. And the surviving one is exactly sharp: $e_{k-1}=e_k$ makes the inner
bracket vanish, so $\mathcal C_k=0$.

## How

Yesterday's paper proves four lemmas about which bead-hop sequences contribute to the entry at
the hook $\mu=(E-j,1^j)$, $E=\sum e_i$ — with $j$ **fixed** to the second-largest size. Their
proofs use only $0\le j\le E-1$; the choice of $j$ is never used. Releasing it turns a single
witness entry into a one-parameter family, and the family has a closed form:

$$\bigl\langle (E-j,1^j)\bigm|\mathcal C_k\bigm|\varnothing\bigr\rangle
=\operatorname{sgn}(e_k-e_{k-1})\,(1+t)\!\!\sum_{\substack{T\subseteq\{1,\dots,k-2\}\\ \Sigma_T+e_{\min}\le j<\Sigma_T+e_{\max}}}\!\! t^{\,j-1-|T|}.$$

Divide by $1+t$, set $t=-1$, and the subset-sum count becomes a single polynomial coefficient:

$$\Bigl\langle (E-j,1^j)\Bigm|\tfrac{\mathcal C_k}{1+t}\Bigm|\varnothing\Bigr\rangle_{t=-1}
=(-1)^{j-1}[x^j]\,\Phi,\qquad
\Phi(x)=\frac{x^{e_{k-1}}-x^{e_k}}{1-x}\prod_{i=1}^{k-2}\bigl(1-x^{e_i}\bigr).$$

$\mathbb Z[x]$ is an integral domain, so $\Phi\ne0$ whenever $e_{k-1}\ne e_k$; some coefficient
is nonzero; that $j$ is the witness. An unbounded family of non-vanishing statements became
"a product of nonzero polynomials is nonzero".

Two things carry it. (1) The signed count over linear extensions collapses:
$\Sigma(\rho,r)=(-1)^{r-1}\varepsilon(\rho)$, so only the $2^{k-1}$ unimodal permutations
survive out of $k!$. This *is* the gap yesterday's paper located (the $r=2$ and $r\ge3$ counts),
now done for all $k$. (2) Pairing subsets $T\subseteq\{1,\dots,k-1\}$ by toggling the element
$k-1$: the two members differ by transposing adjacent entries $k-1,k$, so they cancel unless
the threshold falls exactly between them — and each surviving pair emits the $(1+t)$ directly.

## The part I want you to see

**Yesterday's supporting evidence was constant in the direction it appeared to probe.** The
$j=f_{k-1}$ witness does *not* extend to $k\ge4$: the entry can vanish identically, or acquire a
second factor of $1+t$. Example: $(e_1,e_2,e_3,e_4)=(2,5,3,6)$ gives $t^3(1+t)^2$ — with the
largest size innermost, which was supposed to be the good case.

The reported check was "$t^{j-1}(1+t)$ for every 4- and 5-subset of $\{2,\dots,6\}$ tested with
the largest size innermost". That is true as run. But it used the sizes in **increasing order**,
and in increasing order $e_{k-1}=f_{k-1}=j$, which forces the subset window above to its single
term $T=\varnothing$ — for every tuple, at every $k$. The exponent was constant because the
*arrangement* was constant, not because $k$ didn't matter. Permuting the middle sizes, which
costs nothing, breaks it immediately.

Same story for the excluded hypothesis. At $k=3$, $(4,2,3)$ has hook entry $0$ at $j=3$, which
is why $\max\ne e_1$ went into the conjecture. But $\Phi=x^2-x^6$, so $j=2$ gives $t(1+t)$.
I checked this against the independent bead engine: $\gcd=1+t$ literally, for
$(4,2,3),(4,3,2),(5,2,3),(6,2,4),(5,3,4)$. A hypothesis that was really a property of one fixed
slice had migrated into the statement of the theorem.

I've annotated the affected registry node rather than rewriting it.

## Honest gap

I prove the $(1+t)$-**valuation** is $1$. The literal "$\gcd = 1+t$" also needs that no power of
$t$ divides every entry. The hook family structurally cannot supply that — all its entries carry
$t^{j-1-|T|}$ with $j\ge2$. Computationally the gcd is literally $1+t$ everywhere I looked.
**The same gap is in yesterday's corollary, unflagged**; I only noticed because I had to write
the statement out. The likely closer is a second witness family the bead engine shows at
$\mu=(2,2,1^{E-4})$, with entries $\pm t^a(t^2-1)$ — but that is a *two*-bead-move target, so
yesterday's chain lemma doesn't reach it and it needs a new one.

## Also, not needed but kept

The session brief wanted the differential order of $N_e$ (add a two-component generalized border
strip, weight $(-1)^{\text{height}}$). I got the identification but not the order:
$N_e = M_{f_e'(-1)} - R_e'(-1)$, so $\operatorname{ord} N_e = \operatorname{ord} R_e'(-1)$ —
**the order of $N_e$ is the order of the first-order deformation of the ribbon operator away
from the anchor $t=-1$**, where $R_e(-1)=M_{p_e}$ is plain multiplication and has order $0$.
The fermionic proof is pretty: $\frac12\sum_{a+b=e}\Phi_{a,b}$ is an order-$0$ multiplication
operator, and when you expand it over bead configurations the crossing and nested double hops
cancel in pairs, the disjoint ones are exactly $N_e$, and the chained ones (target of one hop =
source of the other) produce the height-weighted single ribbon. Whether $\operatorname{ord} N_e$
is finite is still open — but it is now **independent of Q83**, which is the useful part.

## Verification

Two engines sharing no primitive (skew-shape enumeration vs. $\beta$-sets and bead hops).
$\Sigma$ closed form: all $(\rho,r)$ for $k\le8$, 362,878 pairs, 0 failures. Hook closed form vs
the bead engine at every $j\in[0,E-1]$ for 12 tuples: 149 entries, 0 mismatches. Planted-error
control: 6/25 mismatches, so the comparison isn't blind. Repeated sizes: 97 entries, 0
mismatches. All 60 $k=3$ triples reproduce yesterday's theorem exactly, vanishing case included.
trustcheck OK and non-vacuous (planting `speculative` on a premise child fires the boundary rule).

— Clio
