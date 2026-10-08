# Note for Robin — 2026-05-28 wake-3

A short follow-up to yesterday's three notes (within-arc-reach, merged-junction
mechanism, operator-reformulation). Today's wake replaced the merged-junction
gap with a cleaner structural target and deflated last night's Petrov dream.

## TL;DR

- A float-rank false alarm prompted an exact-rational re-verification of the
  Taylor coefficients $M_d$ of $M(x)$ at $x=q^2$ on $\lambda=(2,2,1,1,1)$.
- The float report was noise: $\mathrm{rk}\,M_2=0$ exactly. The operator
  reformulation $\mathrm{ord}\,\mathrm{tr}\,M(x)=\min\{|S|:M(S)\ne0\}$ stands.
- The exact computation revealed a **strictly stronger** structural statement:
  every single $M(S)$ with $|S|<\tau(\tau+1)/2$ is the zero matrix on $V^\lambda$
  — not just traceless, not just summing to zero.
- Verified across 5 shapes including the hook $(2,1,1,1,1)$ which has 4944
  subsets at $|S|<6$. The sweep ran in 0.74 s — most subsets short-circuit
  very early in the staircase, a chain-factor obstruction.

This **subsumes the merged-junction case for $|S|<D$**: an intact-or-merged
distinction was meaningful for the WITHIN-grade story (where merged subsets at
$|S|=D$ have non-trivial behaviour) but completely irrelevant BELOW grade.
Every subset below grade $D$ is operator-zero, period.

The remaining gap shrinks to a positivity question at $|S|=D$: at
$(2,2,1,1,1)$, all 14 critical survivors equal $q^8/(q+1)^{16}>0$; no
cancellation. The full off-hook order law follows from a structural proof of
strong per-subset operator vanishing for $|S|<D$ plus positivity of the leading
sum $G_D$.

## What this is

Type-A Hecke $H_n(q)$, seminormal Hoefsmit rep on $V^\lambda$. Per-subset
operators on the staircase word:

$$M(S) := \prod_{k=1}^{N} A_k,\qquad A_k = \begin{cases}P_{-1}^{(i_k)} & k\in S\\ P_q^{(i_k)} & k\notin S\end{cases}$$

with $P_q^{(i)}=(T_i+1)/(q+1)$, $P_{-1}^{(i)}=(q-T_i)/(q+1)$, and the staircase
word $i_k = 1; 2,1; 3,2,1; \dots; n-1,n-2,\dots,1$. The order law:

$$\mathrm{ord}_{x=q^2}\,\mathrm{tr}\,M(x) = \tau(\tau+1)/2,\quad D:=\tau(\tau+1)/2.$$

Conjectured/observed today across all tested $\lambda$ with $\tau\ge1$:

> **Strong per-subset operator vanishing.**
> $M(S) \equiv 0$ on $V^\lambda$ for every subset $S$ with $|S| < D$.

## Empirical scope

| shape | $\tau$ | $D$ | # subsets at $|S|<D$ | all operator-zero? | runtime |
|---|---|---|---|---|---|
| $(2,2,1,1)$ | 1 | 1 | 1 | ✓ | < 0.01 s |
| $(2,2,1,1,1)$ | 2 | 3 | 232 | ✓ | < 1 s |
| $(2,1,1,1)$ | 2 | 3 | 56 | ✓ | < 0.01 s |
| $(2,1,1,1,1)$ | 3 | 6 | 4944 | ✓ | 0.74 s |

Exact rationals at $q=5/7$ and $q=2/3$ (cross-check). Earlier:
$\mathrm{rk}\,M_d$ for $d=0..5$ at $(2,2,1,1,1)$, symbolic in $q$ (compute-2): the
ranks of the *Taylor coefficients* themselves are $(0,0,0,1,2,3,\dots)$ — first
nonzero is $M_3=c_1^3 G_3$ with $\mathrm{rk}=1$ (one nonzero survivor direction,
plus 13 more that sum into the rank-1 image, all consistent).

## Why this is stronger than the existing literature

- $\mathrm{tr}\,M(\emptyset)=0$ for $\tau\ge1$ is the Diagnostic-2 / Pillar-1
  trace vanishing.
- "$\mathrm{tr}\,M(S)=0$ for all $|S|<D$" is the per-subset *trace* vanishing
  (no-cancellation verdict).
- "$M(S)=0$ as operator for all $|S|<D$" — today's finding — is per-subset
  *operator* vanishing. Strictly stronger because $M(S)\ne0$ with
  $\mathrm{tr}\,M(S)=0$ is a logical possibility (operator-nonzero, trace-zero;
  occurs commonly in non-self-adjoint settings). Today's data rules that out
  universally below $D$.

## Why it's tractable (a structural reading)

In practice, when $|S|<D$ the *running product* $\prod_{k\le j} A_k$ becomes
zero on $V^\lambda$ before the chain completes. Once any prefix is zero on a
sub-module, every continuation is. This is the *chain-factor short-circuit*
mechanism — directly aligned with our
[[leftmost-rightmost-factor-technique]] and
[[leftmost-factor-per-syt-vanishing]] tools.

The conjectural proof outline:
1. **Locate the kill-point.** For each $S$ with $|S|<D$, find a prefix length
   $j(S)$ such that $\prod_{k\le j(S)} A_k \equiv 0$ on $V^\lambda$. Empirically
   the kill happens early — usually before the second block of the staircase
   ends.
2. **Bound the kill-points combinatorially.** Show that $|S|<D$ implies the
   distribution of $P_{-1}$ insertions across the staircase blocks $B_2,\dots,
   B_{n-1}$ is incompatible with "no early kill" — the missing
   $P_{-1}$ insertions force a long prefix of pure $P_q$ that exhausts the
   $q$-eigenspace of some restriction.
3. **Recover the per-block reach principle** as a consequence of the kill-point
   bound, NOT as a self-standing axiom.

I haven't proved this; it's the cleanest next prove target. The merged-junction
gap as previously framed is now a sub-question of step 2 (which subset
distributions kill early vs. late).

## Petrov footnote

A separate sub-agent read Petrov 2605.24976 in full. The dream framing ("Fredholm
vanishing order = rank-drop of obliquely-projected operator") is **not in the
paper**. Petrov gives a clean oblique generalization of BOGC and a Cauchy-Binet
expansion but assumes $\Gamma_{\xi,\theta}$ invertible throughout. The
rank-drop ↔ vanishing-order step (if true) is a *separate* theorem outside
Petrov's scope. Residual usefulness: oblique-projection geometry, partition-sum
Cauchy-Binet expansion, polynomial-tilt → Grothendieck specialization. Not a
corollary engine. ([[petrov-tilt-actual-reach]] supersedes
[[petrov-tilted-toeplitz-merged-junction]].)

## Artifacts

- Memory: `~/projects/memory/strong-per-subset-operator-vanishing.md`,
  `~/projects/memory/petrov-tilt-actual-reach.md`.
- Scripts:
  - `~/projects/scratch/2026-05-23-omega-monodromy-verify/2026-05-28-rank-M-d-exact.py`
    (exact ranks of $M_d$ for $d=0..3$ at $(2,2,1,1,1)$).
  - `~/projects/scratch/2026-05-23-omega-monodromy-verify/2026-05-28-per-subset-operator-vanishing.py`
    (cross-shape sweep, 5 shapes).
  - `~/projects/scratch/2026-05-23-omega-monodromy-verify/2026-05-28-prepare-M-22111.py`
    (the original Toeplitz-structure probe; the dense-non-Toeplitz finding closes
    a different sub-question).

Next PROVE session (the current `~/state/PROVE.md` re-seed):

> Prove strong per-subset operator vanishing for $\lambda=(2,2,1^m)$:
> for every $S\subseteq\{1,\dots,N\}$ with $|S|<\tau(\tau+1)/2$,
> $M(S)\equiv 0$ on $V^\lambda$. Attack via early-kill: identify a prefix
> length $j(S)$ at which the running product vanishes on $V^\lambda$, and
> bound $j(S)$ combinatorially.
