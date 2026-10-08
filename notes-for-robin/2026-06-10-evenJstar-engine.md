# For Robin — 2026-06-10: a clean engine for the d=4 fiber, and what it does/doesn't prove

Hi Robin,

Today's prove session was the "even-|J*| crux" of the $d=4$ fiber law
$G_\lambda(i)=0\iff\lambda=(2,2)$. I did **not** close even-$|J^*|$, but I think I found the right
machine and proved several clean things around it. Honest summary below.

## The clean reformulation (rigorous)

The whole problem lives in two power sums. Since $\psi=h_2+ie_2=p_2+\pi e_2$ ($\pi=1+i$),
$$G_\lambda(i)=\langle s_\lambda,(p_2+\pi e_2)^m\rangle=\sum_{r=0}^m\binom mr R_r\,\pi^r,\qquad
  R_r=\langle s_\lambda,p_2^{m-r}e_2^r\rangle\in\mathbb Z,\ \ R_0=\chi^\lambda(2^m).$$
This is cleaner than last cycle's $A_\lambda(i-1)$ form and makes the $\pi$-adic Newton polygon
($\mathrm{val}(r)=r+2v_2(\binom mrR_r)$) immediate.

## A one-line congruence (rigorous)

Every $r\ge1$ term is divisible by $\pi$, so
$$\boxed{G_\lambda(i)\equiv\chi^\lambda(2^m)\equiv f^\lambda\pmod\pi.}$$
(The second $\equiv$ because $p_1^2\equiv p_2\bmod2$ forces $\chi_k\equiv f^\lambda$ for all $k$.)
This re-derives the parity non-vanishing criterion ($f^\lambda$ odd $\Rightarrow G\neq0$) as
literally the constant term of the expansion, and shows **every tie has $f^\lambda$ even.** Tiny,
but it's the kind of inevitability I like — the criterion was never a separate fact.

## The engine (rigorous)

With $\Phi(z)=\langle s_\lambda,(p_1^2+zp_2)^m\rangle=\sum_k\binom mk\chi_k z^k$, the identity
$p_1^2+zp_2=(1+z)p_2+2e_2$ gives an **exact 2-adic lift**
$$\Phi(z)=\sum_r\binom mr 2^r R_r\,(1+z)^{m-r}\ \Longrightarrow\ \Phi(z)\equiv\chi^\lambda(2^m)(1+z)^m\pmod2.$$
So when $\chi^\lambda(2^m)$ is odd, the Newton minimum locus is *exactly the binary submasks of $m$*
— a 2-adic box, by Lucas. That is the box phenomenon, proved, on the leading layer.

## What I could not do (honest)

The locus that actually controls $G$ (the sharp $J^*$) is *coarser* than the engine sees, and the
tie case is exactly where $\chi^\lambda(2^m)$ is **even**, so the leading $(1+z)^m$ vanishes mod 2.
The next 2-adic layer involves $e_2\bmod2$, and there the clean "$p_1^2\equiv p_2$" collapse is gone.
So the full box (and even-$|J^*|$) is **reduced to**, but not proved: *the leading 2-adic layer of
the tilt-scaled generating polynomial is a shifted power of $(1+\cdot)$ mod 2.* I verified this
exhaustively (coarse $4114/4114$, sharp $1624/1624$ ties, all $m\le12$) — it is certainly true; it
needs a mod-$\pi^k$ argument I don't yet have. And none of this touches Step 2 / non-vanishing,
which stays open (cancellation depth is unbounded).

Net: the reformulation, the congruence, and the engine are new and clean and rigorous; the box is a
crisp, verified, well-posed remaining target. Files: `proofs/2026-06-10-evenJstar-box-steplaw.{md,tex,pdf}`,
scripts `code/job_*.py`.

— Clio
