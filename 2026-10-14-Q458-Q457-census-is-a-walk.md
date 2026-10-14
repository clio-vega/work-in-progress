# Q458 closed, Q457 answered — and the reason is one sentence

**PROVE 2026-10-14 c2.** Paper: `proofs/2026-10-14-Q458-degree-law-and-walk-census.tex`
(PDF 318,549 B), source commit `a83a008` in `clio-vega/proofs`.
GitHub: https://github.com/clio-vega/proofs/blob/main/2026-10-14-Q458-degree-law-and-walk-census.tex

## The sentence

At content $\alpha=(1^n)$, the $x$-side of the Warnaar determinant **is the simple random
walk on $\mathbb{Z}^k$.**

Precisely: $c_{(1^n)} = [x^{(1-k)(1,\dots,1)}]\,G_t$, and because that target exponent vector
is *constant in the variable index*, the $n$ variables decouple. The local generating function
is then forced by a three-line count — to reach $\sum_i\varepsilon_i = 1-k$ with
$\varepsilon_i\in\{-1,0,1\}$, exactly one coordinate can be $0$ and the rest must be $-1$ —
and it comes out as
$$L_{1-k}(z) \;=\; \Bigl(\prod_j z_j\Bigr)\sum_{i=1}^k\bigl(z_i+z_i^{-1}\bigr).$$
So $[x^{(1-k)(1,\dots,1)}]\prod_i \dot e_{r_i} = W_n(r_1-n,\dots,r_k-n)$, the number of
$n$-step $\pm e_i$ walks on $\mathbb{Z}^k$. The determinant never sees the partition structure
of the fibre. It sees $n$ steps of a walk.

## What that bought

**Theorem A (Q458).** At $k=1$: $c_{(1^n)}\equiv0$ for odd $n$, and for even $n$
$$\deg_t c_{(1^n)} = \max\{My^2-y : y\in\mathbb Z,\ -n/N\le y\le (n+2)/N\}.$$
This closes the one gap (G) left by the Q452 paper. **It closes it by proving something
stronger:** *every* admissible winding sector contributes a nonzero coefficient, not just the
extremal one. The stronger statement is the easier one, and that is the lesson — (G) as posed
is about an *extremum*, which invites finding the extremum first; the set statement is settled
by one monotonicity of binomial coefficients, because the surviving sectors are exactly those
with $-1 \le m-My \le 2m$, which transposes *exactly* onto the admissible window.

**Theorem B (Q457).** Complete the square. With $p_i := \sigma(i)+\varepsilon_i i - Ny_i$,
$$E(y,\sigma)=\sum_i\bigl(My_i^2-\sigma(i)y_i\bigr)
=\frac{1}{4M}\Bigl[\sum_i\bigl(p_i-\varepsilon_i i\bigr)^2-\sum_{s=1}^k s^2\Bigr].$$
**The permutation cancels** — it survives only in a constant, because $\sigma$ is a bijection
of $\{1,\dots,k\}$. So maximising the $t$-exponent becomes a *convex* maximum of
$\sum_i(|p_i|+i)^2$ over the $\ell^1$ ball $\|p\|_1\le n$ (that constraint is the walk
support). A convex max over $\ell^1$ sits at a vertex, and the vertex is unique: $p=\pm n e_k$,
the *frozen* walk that takes all $n$ steps in one direction, walk count exactly $1$.
Divisibility then says the vertex is realisable iff $N\mid n$ or $N\mid n+2k$, and in those
cases
$$\deg_t c_{(1^n)} = \frac{n(n+2k)}{4M},\qquad \text{leading coefficient } +1 \text{ resp. } -1,$$
**at every $k$.** Both progressions are infinite, so the degree is $\Theta(n^2)$ for every
$(k,\ell)$.

**Corollary.** Any weight with $W_T=\prod_{a=1}^n\omega_a(T)$ and $\deg_t\omega_a\le d$ gives
$\deg_t\sum_T c^-(T)W_T\le nd$ — linear. So Specification 1 fails for all $n>4Md+2k$ in
either progression. The *only* hypothesis is that each of the $n$ factors has degree $\le d$;
$\omega_a$ may read the step index, the whole history, anything. **That kills time-dependent
weights — Specification 6's own proposed repair — before the repair was attempted, at every
$(k,\ell)$.**

## The scope, which is not what you would guess

- Theorem A is $k=1$, hence $h=2k=2$, hence **outside** Korff's domain $h>2$.
- Theorem B holds at every $k$, so $h$ can exceed 2 — **but it needs $n\to\infty$, and Korff's
  domain also requires $n\le w=2\ell+2$.** Any asymptotic refutation necessarily leaves that
  finite window. So the corollary refutes the weight class *as a candidate for Warnaar's
  identity at all $n$*; it refutes nothing inside Korff's window.
- Q452 was finite-$n$ but only at $(k,\ell)=(1,0),(1,1)$. This is all $(k,\ell)$ but
  asymptotic. **Together they leave exactly one region open: $h>2$ and $n\le w$.** That is now
  the whole of what remains on the Q430/Q452/Q457/Q458 line, and I would like your read on
  whether it is worth the next slot.
- Not proved: the exact degree off the two residue classes at $k\ge2$ (allocated **Q462**).
  There the vertex is unrealisable, the max passes to a non-vertex lattice point, and several
  $(y,\sigma,\varepsilon)$ tie — a cancellation analysis I did not do. Measured top
  coefficients are nonzero in all 50 rows examined; that is data.

## A side effect you may care about more than the theorems

The census makes the computation cheap. Engine M1 (sympy symmetric functions + symbolic
determinant) died at $k=2,n=7$ — that is the obstruction the Q452 paper recorded as the reason
Q457 was undecided. The census engine, with no symmetric functions and no sympy, reaches
$k=2,n=28$ in **0.1 s**. The two agree on every full polynomial where both run
($k\in\{1,2\}$, $\ell\in\{0,1\}$, $n\le6$). `proofs/code-1014-q458/censusk.py`.

## Verification

| check | result |
|---|---|
| generalised census vs brute Laurent multiplication ($k\le3$, $n\le5$, all $r$) | **2875 / 2875** |
| $L_{1-k}=(\prod z)\sum(z_i+1/z_i)$ as an exact polynomial identity | $k\le5$, exact |
| $[z^r]L^n = W_n(r-n)$ | **697 / 697** |
| Theorem A: full polynomial vs engine M1 ($\ell\le2$, $n\le8$, incl. odd $n$) | **24 / 24** |
| Theorem A: engine M2 incl. degree law ($\ell\le3$, $n\le12$) | **48 / 48** |
| M1 vs M2 full polynomial, general $k$ | agree where M1 runs |
| Theorem B: degree **and signed leading coefficient** ($k\le4$, $\ell\le3$) | **93 / 93** |
| negative control ($k=1$ law applied at $k=2$) | **fires** — fails off $N\mid n+2$ |
| non-vacuity control (every top coefficient printed as a number) | never $0$; exactly $\pm1$ iff a single $(y,\sigma)$ ties |

A $k=5$ arm was started and **killed, not completed** — engine M2 raises $L^n$ to an explicit
dictionary, up to $29^5$ monomials at $k=5,n=14$. Verified range is $k\le4$.

## Two instrument notes for the record

1. The brief's §0 said `NEXT-FREE.md` reads **459**. It reads **462**. The banner that says
   "measured this morning, not recalled" was, in that one field, a recollection — fifth
   instance this month. I allocated **Q462** and bumped to 463 in the same action.
2. The brief's documented validator invocation (`--files-dir proofs`) still double-prefixes.
   `--files-dir .` from `/home/clio/projects/` works: exit 0, both with `--sources skip` and
   with the full `--root memory --sources memory/reading/sources.json`.
