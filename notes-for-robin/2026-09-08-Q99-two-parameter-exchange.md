# Q99 closed — and the brief I was given contained two errors, one of which would have made me reject the correct theorem

**Robin — 8 Sept 2026, PROVE c1.**
Paper: `proofs/2026-09-08-Q99-two-parameter-exchange.tex` (7pp, compiles clean).
Registry: 16 nodes under `fock-ribbon-sign-operator`, `trustcheck` OK.

## The mathematics

**Theorem A.** For two *independent* parameters $s,t$, the Hall–Littlewood vertex operators satisfy
$$(z_1-tz_2)\,H_t(z_1)H_s(z_2)\;=\;(sz_1-z_2)\,H_s(z_2)H_t(z_1).$$
The proof is one sentence long once you see it: **both orderings normal-order to the same series.**
Write $\Phi=\sigma[Xz_1]\sigma[Xz_2]f[X-\frac{1-t}{z_1}-\frac{1-s}{z_2}]$. The argument of $f$ is
symmetric in the two shifts, so all the asymmetry between the orderings is a single scalar
contraction; clearing each ordering's own denominator gives $(z_1-z_2)\Phi$ both times.
Setting $s=t$ recovers the known one-parameter relation — which I therefore *derive* rather than
assume, so nothing here rests on the Zabrocki thesis (only known to me at agent-summary level).

**Theorem B, which is the real content.** The exchange factor is a scalar exactly on $st=1$, where
it is $1/t$. Everyone's instinct — mine included, and the brief's — is that the modes then form a
quantum torus, $H^t_mH^{1/t}_n=t^{-1}H^{1/t}_nH^t_m$. **They don't.** You cannot divide the
generating identity by $(z_1-tz_2)$: the two orderings are supported on *different cones*, and
$(z_1-tz_2)\delta(tz_2/z_1)=0$. The contact term survives, and I computed it:
$$H^t_mH^{1/t}_n-t^{-1}H^{1/t}_nH^t_m\;=\;(1-t^{-1})\,t^{-m}\,h_{m+n}\bigl[(1+t)X\bigr]\cdot$$
— multiplication by a symmetric function. It vanishes identically **iff $t=1$**, and there only
because at $t=1$ the operator degenerates to multiplication by $\sigma[Xz]$.

**The mechanism is the part I find beautiful.** The $\delta$-term lives on the diagonal $z_1=tz_2$.
On exactly that diagonal, when $st=1$, the two plethystic shifts $-\frac{1-t}{z_1}$ and
$-\frac{1-t^{-1}}{z_2}$ *cancel each other identically* — so $f$ passes through untouched and only
the two $\sigma$'s survive. The hyperbola is the locus where the singular support of the exchange
coincides with the vanishing locus of the total shift. That is why the obstruction is a
multiplication operator: the simplest thing it could be without being zero.

## The thing you should probably know about

**The brief's prescribed negative control was false**, and it was written in the imperative:
"At $t=s=1$ … the naive corollary predicts that the Bernstein operators commute. *They do not.* …
**Any derivation of the mode relation that does not break at $t=1$ is wrong.**"

They do commute. At $t=1$ the shift $(1-t)/z$ is zero, so $H^1_m$ *is* multiplication by $h_m$
(checked 16/16 independently), and multiplication operators commute. The brief's supporting
observation — that (2.14) at $t=1$ is strictly weaker than commutativity — is true, but "does not
imply" is not "is false". Had I obeyed the control, I would have thrown away Theorem B.

A second, independent defect in the same brief: its contraction sketch gave
$\sigma[-(1-t)z_2/z_1]=\frac{1-tz_2/z_1}{1-z_2/z_1}$, which is the **reciprocal** of the truth.
Followed literally it produces the relation with the two factors on opposite sides — precisely the
variant that fails 12/12 in my own planted-error control.

Both were caught the same way: by recomputing the small thing instead of transcribing it. I'd
flag this as the general lesson — **a control is a claim, and briefs state controls with more
confidence than they state conjectures**, because a control feels like methodology rather than
mathematics. Mine are written by me the previous evening, so this is a note to myself as much as
to you.

## What I did *not* claim

I did **not** claim that $st=1$ is the hidden structure behind my ribbon commutator. In fact I can
now say the opposite, which was the actual open question:

**The two $st=1$ witnesses are distinct.** On the ribbon side (Q96 Cor 4.2(iii)) the *plain*
commutator $[R_e(t),R_f(s)]$ vanishes on *all* of $ts=1$. On the vertex-operator side the plain
commutator does *not* vanish there — $[H^t_1,H^{1/t}_1]\cdot1=\frac{t^2-1}{t}h_2$ — and the
twisted commutator vanishes only at the single point $t=1$. Same equation, different content.
The transport between the two sides was not attempted; the obstruction is named in §5 ($R_e(t)$
is the connected truncation of the ribbon-move expansion, and the enumeration runs over single
bead moves, not over $\sigma[Xz]$).

## Verification

Engine written this session, code-disjoint from the browse agent's scripts (which I read to
establish what they compute, then did not run). Untuned anchors: $t=1$ multiplication 16/16;
$t=0$ Bernstein $H_ms_\lambda=s_{(m,\lambda)}$ against independent Jacobi–Trudi 13/13, including
correct straightening. Theorem A: 126/126, generic symbolic $t,s$, negative modes included.
Theorem B: 138/138 plus 28/28 at higher degree; the 18 vanishing cases factor as exactly
$3\times6$ — the three pairs with $m+n<0$ — and for no other reason. The proof's two middle steps
were checked *separately* so the final agreement isn't the only evidence. Planted-error control:
five perturbations of the exchange factor, each failing 12/12; only the true one passes.

## Open, and worth a look

The defect is multiplication by $h_{m+n}[(1+t)X]$, the alphabet with generating function
$\prod_i(1-x_iz)^{-1}(1-tx_iz)^{-1}$. Is that the image of something Hall–Littlewood-theoretic —
a Macdonald specialisation, or the $t$-analogue of a boson–fermion normal-ordering constant? At
$t=-1$ it collapses to $2(-1)^mh_{(m+n)/2}[X^2]$ for $m+n$ even and $0$ for $m+n$ odd. A parity
structure appearing at the free-fermion point is not nothing, and I'd like to know what it is.

— Clio
