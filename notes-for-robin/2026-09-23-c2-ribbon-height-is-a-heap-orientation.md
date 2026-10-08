# For Robin — 2026-09-23 c2 (PROVE, Day 201): the height of a ribbon is the orientation of a heap

**Paper:** `proofs/2026-09-23-c2-ribbon-height-is-a-heap-orientation.tex` (+ PDF, 9pp).
**Code:** `proofs/code-q237/` (`anTL.py`, `ribbon_check.py`). **Registry:**
`proofs/registry/ribbon-height-heap-orientation.json`, validates clean.

## The one-sentence version

Postnikov builds two elements $\mathbf e_r,\mathbf h_r$ out of **two special orderings** of a
set of generators in the affine nil-Temperley–Lieb algebra $\mathscr A_n$. The orderings in
between are not noise: for an interval $J$ of length $e$ in $\mathbb Z/n\mathbb Z$, the
$2^{e-1}$ monomials of $\mathscr A_n$ with support $J$ are the $2^{e-1}$ ribbons of size $e$,
and **the number of "up"-oriented edges of the heap is the height of the ribbon**. So my whole
$t$-family $R_e(t)=\sum_h t^h N_e^{(h)}$ sits inside $\mathscr A_n[t]$ as an orientation sum,
with $\mathbf h_e$ at $t=0$ and $\mathbf e_e$ at $t=\infty$.

That is the answer to Q237's "index identification", and it is **proved**, not computed.

## The three questions the brief asked, answered

1. **Index set.** Same set. Postnikov's own l.2806 already says monomials $\leftrightarrow$
   cylindric shapes mod $\sim$; what I add is the *statistic*.
2. **Truncation.** The brief feared: *"If there is no mechanism on my side that produces the
   cutoff, that is the obstruction and the answer is no."* **There is one.** The cutoff is the
   exclusion of $I=\mathbb Z/n\mathbb Z$ — i.e. of the ribbon that wraps all the way round,
   $e=n$. The correction term of `eq:e-h-AN` equals $(-1)^{n-k}q\cdot\mathrm{Id}$, which is
   the single quantum relation $e_kh_{n-k}=q$. The obstruction is to the *semi-infinite wedge*
   (index set $\mathbb Z$, no wrap), not to the $t$-family.
3. **Parameter.** The brief predicted "nil" and $t=-1$ would be in tension and might kill the
   branch in ten minutes. **They are not.** Nil constrains which *states* a monomial acts on,
   not the height. And $t=-1$ turns out to be the unique point where $R_e(t)$ commutes with
   the strip-adders — the cylindric twin of Q75.

Three predicted blockers, three false. That is now five instances in 96 hours of
*a named obstruction is never the object of the check*.

## What is proved vs. what is computed — please read this bit

**Proved:** Theorem A (orientation $=$ height, with the full legality argument), its two
corollaries, and Theorem C (the truncation, from Postnikov's presentation `eq:QH`).

**Computed only:** Theorem B. Two statements, both verified exactly and symbolically but
**not proved**:
* $t=-1$ is the unique $t$ with $[R_e(t),\mathbf h_j]=0$ ($n\le6$, $2\le k\le n-2$);
* Newton's identity $r\mathbf h_r=\sum_e R_e(-1)\mathbf h_{r-e}$ holds for $r\le n-1$
  ($n\le7$, all $k$), failing at $r=n$ by exactly $(-1)^{k-1}(n-k)q$.

The missing proof is, I think, a sign-reversing involution on pairs (cylindric horizontal
strip, signed ribbon). I looked for it and did not find it. Gap (G1).

## The pretty bit

One relation, $e_kh_{n-k}=q$ — the only difference between $H^*(\mathrm{Gr}_{kn})$ and
$\mathrm{QH}^*$ — shows up four times: as Postnikov's correction term $(-1)^{n-k}q$; as the
failure of Newton at $r=n$, of size $(-1)^{k-1}(n-k)q$; as $\varphi(h_n)=(-1)^{k-1}q$; and as
$\varphi(p_n)=(-1)^{k-1}kq$, the full-wrap ribbon. The arithmetic tying the last three
together, $n=(n-k)+k$, is just **"$n$ steps round the cylinder $=$ $(n-k)$ gaps $+$ $k$
beads"**. I like this one a lot.

## A dead end, recorded

I guessed the orientation-and-subset sum $Q(z;t)$ was the affine Hall–Littlewood generating
function $H(z)E(-tz)$. **False**, and minimally so: at $n=2,k=1$ the discrepancy is a factor
$(1-t)$. Reason: $t^{\text{height}}$ and $(1-t)^{\#\text{components}}$ are different
statistics; they agree only at the endpoints. Written up in
`proofs/code-q237/2026-09-23-c2-dead-end-HL-factorisation.md`.

## Novelty — I claim nothing

This morning's browse found Korff–Vasilev `2606.06352`, Benkart–Meinel `1505.02544`, and a
sixty-work affine-nilTL literature with **zero** coverage in my index. The operator bridge is
Korff–Stroppel 2010. I have **not** checked Theorem A against any of them. The paper says so
in a Novelty section that also lists the three sentences no draft of mine may contain.

## Also done this session (the carried defect)

`proofs/2026-09-20-c1-cylindric-M-convexity.tex` — the paper in Rick's hands — had a Gaps
clause saying $\hat\lambda(\lambda/\mu,\ell)$ "grows with $\ell$". **It is false**: the
recursion defining the greedy chain has no $\ell$ in it. Replaced by
Proposition 5.4, proved: $\hat\lambda$ is independent of $\ell$ on its whole domain, and the
promised "easy monotonicity statement" does not exist because there is nothing to be
monotone. Cover block records it as the first *mathematical* correction to that file; no
theorem of §§1–7 is affected.
