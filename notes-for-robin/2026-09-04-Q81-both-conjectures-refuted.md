# Q81 — both conjectures refuted, and the refutation is the better result

**4 September 2026, PROVE cycle 2.**
Paper: `proofs/2026-09-04-Q81-nested-bracket.tex` (10 pp, compiles).
On GitHub: <https://github.com/clio-vega/work-in-progress/blob/main/q81/2026-09-04-Q81-nested-bracket.pdf>

## What I was asked to test

Two conjectures about the $k$-fold nested bracket
$\mathcal{C}_k=[R_{e_1},[R_{e_2},[\dots,R_{e_k}]\dots]]$ of the ribbon operators:

- **(A) depth**: the gcd of the entries is $(1+t)^{k-1}$.
- **(B) components**: every entry is $\pm t^a(1+t)^{k-1}(1-t)^{m-1}$, $m$ = number of
  connected components of $\mu/\lambda$.

Both are false. The brief anticipated that possibility and said the falsification would be the
more valuable outcome. I think that turned out to be right.

## (B) dies in Phase 0, and the way it dies is the interesting part

The brief said to spend thirty minutes confirming the refactoring on the *existing* $k=2$ data
before building anything. That check killed the conjecture on the spot: **$m=1$ for all 283
nonzero entries.** Not "mostly 1" — identically 1. And at $k=3$, identically 1 again, on 9524
entries.

The reason is structural, and it is the thing I would most like you to look at. Two bead hops
produce a *disconnected* skew shape exactly when their diagonal intervals are **disjoint**. The
commutator's closed form (proved yesterday) says the entry is nonzero exactly when the intervals
**cross**. So the component count is constant on the commutator's support *because the commutator
was built by a cancellation that annihilates every multi-component target*.

That is a sharper version of the failure mode I already had in memory ("a check can be correct and
still be constant in the direction it tests"). The new content: the kernel was not accidental. I
transported a statistic from the commuting family $g_e$ — where it genuinely varies — onto the
image of an antisymmetrisation designed to kill exactly that variation. **No data set drawn from
$[R_e,R_{e'}]$, of any size, could have caught it.** The diagnostic is to look at the *support* of
the operator before believing a statistic read off its *values*.

(The statistic the $k=2$ data was actually measuring is the number of moving beads, $m_{\rm hop}$
— a perfect fit, 0/283 violations. That one then fails at $k=3$: it holds on 7067 of 9524, and the
residues stop being $\pm1$. So the two-shape rigidity of $k=2$ is a $k=2$ phenomenon.)

## (A) dies too — and here is what replaces it

The gcd of $\mathcal{C}_k$ is exactly $(1+t)$, for every $k$: 190/190 configurations at $k=3$,
and again at $k=4$. The exponent does not deepen.

Two theorems, both proved and both resting only on my own earlier papers:

1. **$(1+t)$ divides every entry of $\mathcal{C}_k$, for all $k\ge2$ and all $e_i\ge2$** — no
   distinctness hypothesis. Four lines from $R_e = M_{f_e}-(1+t)E_e$ (Q75) plus commutativity of
   $\Lambda$. This generalises the $k=2$ corollary of the Q75 paper.

2. **A reduction of level $k$ to level 2:**
   $$\frac{\mathcal{C}_k}{1+t}\bigg|_{t=-1}
   = \mathrm{ad}_{p_{e_1}}\cdots\mathrm{ad}_{p_{e_{k-2}}}\bigl(Q_{e_{k-1},e_k}(-1)\bigr),$$
   where $Q_{e,e'}=[R_e,R_{e'}]/(1+t)$ is exactly the quotient from yesterday's paper. All but two
   of the $k$ first-order terms vanish identically, for a trivial reason. This is what explains
   (A)'s failure rather than merely recording it: the mechanism produces one factor of $(1+t)$,
   and only one, for every $k$. At $k=2$ the observed exponent $1$ happens to equal $k-1$, and
   that coincidence is the whole of (A)'s evidence.

   Verified entrywise against an engine sharing no code with the first: 1310 entries at $k=3$,
   270 at $k=4$, zero mismatches, all nonzero.

3. **Sharpness at $k=3$, uniform in the sizes**: with $j$ the second-largest of $e_1,e_2,e_3$,
   the entry of $\mathcal{C}_3$ at $\mu=(E-j,1^j)$, $\lambda=\varnothing$, is $t^{j-1}(1+t)$ when
   the largest size sits innermost, $-t^{j-1}(1+t)$ in the middle slot, and $0$ in the outer slot.
   This contains the $k=2$ witness of the previous paper as its $k=2$ case. Sharpness is verified
   computationally out to $k=6$.

## The one gap, precisely

The three lemmas behind the witness (paths are spatial chains; the height depends only on the
chain and equals $t^{j-r+1}$; the nested bracket expands over exactly the *unimodal* time orders
with sign $(-1)^{\#\text{before the peak}}$) hold for **all** $k$. What I have not proved for
$k\ge4$ is the signed count of chains with threshold $r\ge2$. At $k=3$ the case $r\ge3$ is
vacuous, which is why $k=3$ closes. It is pure sign combinatorics — no $t$ in it — and it is
where I would start tomorrow.

## Provenance note

Nothing here depends on Jing–Liu `2310.15730`. The commuting-family route to divisibility would
have needed their Cor 4.4, which I still hold only at `agent-summary` level; Theorem 1 replaces it
with my own proved decomposition. The standing caveat in the brief is discharged by avoidance, not
by verification.
