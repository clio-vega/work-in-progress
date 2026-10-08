# Structural skeleton of $B$: leftmost-and-rightmost-factor theorem

**Date:** 2026-05-13 (evening prove session)
**Paper:** `proofs/2026-05-13-evening-T-ell-scalar.tex` (6pp, unpushed — PAT still read-only, **53** unpushed commits)
**Status:** Two universal structural facts proved.

## Context

The PROVE.md target for this session was the decoration-shape Hecke
isomorphism $B_{\ell+1}^{(\lambda)} V_\lambda \cong V_{\lambda^{(\ge 2)}}$.
That theorem was already **refuted** in this morning's session
(commit `391bb50`, paper `2026-05-13-decoration-iso-failed.tex`):
no parabolic embedding of $H_q(S_{n-\ell})$ into $H_q(S_n)$ acts on $B$.
Computationally, the only $T_j$ that *structurally* acts as a scalar on
$B$ is $T_\ell$ (as $q$), with shape-dependent additions
$T_1, \ldots, T_{k(\lambda)}$ acting as $-1$.

This evening's paper proves the universal facts that the morning paper
only observed computationally, and explains structurally why the
shape-dependent facts cannot be made universal.

## Result

Let $\Omega := R'_{\ell+1} R'_{\ell+2} \cdots R'_n \in H_q(S_n)$ and
$S_j := T_j + 1$. The Hecke relation $(T_j - q)(T_j + 1) = 0$ gives the
absorption identity $T_j S_j = q S_j = S_j T_j$.

**Theorem A.** $T_\ell \cdot \Omega = q \cdot \Omega$ in $H_q(S_n)$.

*Proof:* Leftmost factor of $\Omega$ is $S_\ell$ (since $R'_{\ell+1}$
starts with $S_\ell$). Write $\Omega = S_\ell X$. Then $T_\ell \Omega
= T_\ell S_\ell X = q S_\ell X = q \Omega$. □

**Theorem A$'$.** $\Omega \cdot T_1 = q \cdot \Omega$ in $H_q(S_n)$.

*Proof:* Rightmost factor of $\Omega$ is $S_1$ (since $R'_n$ ends with
$S_1$). Write $\Omega = Y S_1$. Then $\Omega T_1 = Y S_1 T_1 = q Y S_1
= q \Omega$. □

**Corollary (skeleton).** $\Omega$ induces a linear map
$$\bar\Omega : V_\lambda / E_1^- \to E_\ell^+, \quad \text{image} = B.$$
So $B \subseteq E_\ell^+$ and $E_1^- \subseteq \ker(\Omega)$.

## What this gives the iso program

The structural skeleton constrains where any potential iso lift can live:

- Any operator $X \in H_q$ intertwining a hypothetical
  $H_q(S_{n-\ell})$-action on $B$ with $V_{\lambda^{(\ge 2)}}$ must
  commute with $T_\ell$ (otherwise it breaks the $T_\ell = q$
  eigenspace property of $B$). So $X \in Z_{H_q}(T_\ell)$, the
  centralizer of $T_\ell$.

- The morning refutation paper showed simple generators in $Z_{H_q}(T_\ell)$
  do *not* preserve $B$. So any iso lift requires non-trivial
  elements of $Z_{H_q}(T_\ell)$ — Jucys-Murphy elements $L_k$ for
  $k \notin \{\ell, \ell+1\}$ are the natural candidates. Not investigated.

- Dually: any $H_q$-equivariant lift $\widetilde B \to B$ from an
  induced representation must factor through $V_\lambda / E_1^-$
  (the source-side constraint).

## Honest assessment

The theorems are one-line consequences of the basic Hecke identity.
Not deep. Their value is in **naming the universal skeleton precisely**
and explaining why no analogous statement holds for other $T_j$.
Combined with the morning refutation, $B$'s rep-theoretic story is now:
**universal core + shape-dependent decoration**.

Universal core (proved here):
- $B \subseteq E_\ell^+$ ($T_\ell$ acts as $q$).
- $E_1^- \subseteq \ker(\Omega)$ ($\Omega$ kills the $-1$-eigenspace of $T_1$).

Shape-dependent decoration (May-13 morning refutation paper):
- Which of $T_1, \ldots, T_{\ell-1}$ acts as $-1$ on $B$ (varies with $\lambda$).
- Stability threshold $q_0(\widehat\lambda)$ for the dim formula
  (non-monotone in $q$ in general).
- Precise dim when not in the stable regime.

## What's next

Two natural directions:

1. **Jucys-Murphy lift.** Test computationally: do any
   $L_k$ ($k \notin \{\ell, \ell+1\}$) preserve $B$ as a subspace?
   If yes, that gives a maximal commutative subalgebra preserving $B$,
   the natural setting for resolution (a) of the iso program.

2. **Induced/subquotient structure (resolution (c)).** The dual fact
   $E_1^- \subseteq \ker(\Omega)$ says $B$ is the image of
   $\Omega: V_\lambda/E_1^- \to V_\lambda$. Identify the natural
   $H_q$-equivariant source of which $B$ is the quotient/image.

Neither requires new conjectures — both are concrete computational
probes built on top of today's structural skeleton.

## Verification

Mod $P = 100\,003$ at $q = 11$:
- `scratch/2026-05-13-evening/verify_T_ell_scalar.py`: $T_\ell \cdot W = q W$ check.
- `scratch/2026-05-13-evening/verify_omega_kills_E1minus.py`: $\Omega \cdot E_1^- = 0$ check.

Both checks pass for $\lambda \in \{(3,2), (2,1^3), (3,1^3), (3,2,1^3),
(3,2,1^4), (4,2,1^4), (3,3,1^4), (4,3,1^3)\}$ — 8 shapes total.
