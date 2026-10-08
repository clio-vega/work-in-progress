# 2026-05-17 evening — Smoking gun explained

Hi Robin,

Today's evening prove session closed the "smoking gun" mystery from the
zero-diagonal residual question (open thread #5 in SUMMARY.md). The
theorem and proof are clean enough to land in 6 pages.

## What's new

**Theorem.** For $\lambda \vdash n$ with $\ell = \ell(\lambda)$, if values
$\ell$ and $\ell+1$ sit in the same column of $T \in \SYT(\lambda)$, then
$p_T(q) = \langle v_T, \Omega^{(\lambda)} v_T \rangle = 0$.

**Where the smoking gun fits.** $T_0 = ((1,2,5),(3,4,6),(7),(8),(9))$ at
$\lambda = (3,3,1,1,1)$ has values 5 at $(0,2)$ and 6 at $(1,2)$ — same
column — and $\ell = 5$. So the theorem fires with $(\ell, \ell+1) = (5,6)$
and gives $p_{T_0} = 0$ directly. Verified empirically:
$\Omega v_{T_0}$ has 72/120 nonzero components, but the
$T_0$-coefficient is exactly 0.

**Paper.** `clio-vega/proofs` commit `ce5afed`:
https://github.com/clio-vega/proofs/blob/main/2026-05-17-leftmost-factor-per-syt-vanishing.tex

## The proof in two lines

1. Leftmost factor: $\Omega = R'_{\ell+1} \cdots R'_n = S_\ell \cdot X$
   (extract the leftmost $S_\ell$ from $R'_{\ell+1} = S_\ell R'_\ell$).
   So $\Omega v_T \in \mathrm{im}(S_\ell) = E^+_\ell$.

2. Pair $(\ell, \ell+1)$ SC at $T$ means $v_T \in E^-_\ell$. Project
   $\Omega v_T = \sum c_{T,T'} v_{T'}$ onto $E^-_\ell$ along $E^+_\ell$.
   The seminormal basis is well-adapted: SR vectors land in $E^+_\ell$ (so
   project to 0), SC vectors are themselves in $E^-_\ell$, D vectors split
   inside their own 2-block. Reading the equation
   $0 = \pi_-(\Omega v_T)$ off the basis: the coefficient of $v_{T''}$ for
   any SC $T''$ is just $c_{T, T''}$, forcing $c_{T,T''} = 0$.
   In particular $c_{T,T} = p_T = 0$.

That's it.

## What this is and isn't

**Is:** A per-SYT refinement of the well-known leftmost-factor
containment $B^{(\lambda)} \subseteq E^+_\ell|_{V^\lambda}$
([[leftmost-rightmost-factor-technique]] memo, May-13 evening-2). I
expected this was implicit somewhere in the trace-vanishing toolkit, but
I didn't find it stated as a per-SYT theorem in our prior papers.

**Isn't:** A full characterisation of $\{T : p_T = 0\}$. At $(3,3,1,1,1)$,
the theorem accounts for 26 of 108 zeros. The remaining $108 - 26 = 82$
split as 14 descent-1 trivially-zero + 68 descent-0 D-class zeros where
pair $(5,6)$ is "diagonal" (different row, different column) but $p_T$
vanishes anyway. The mechanism for those 68 is the "interior sign-kill"
pattern noted in the May-16 dream-2 entry — still open.

## Sanity checked on 7 shapes

| $\lambda$ | $\ell$ | # SC SYTs | # of those with $p_T = 0$ |
|---|---|---|---|
| (2,2,1) | 3 | 2 | 2 |
| (3,2,1,1) | 4 | 8 | 8 |
| (4,2,1) | 3 | 6 | 6 |
| (2,2,2,1,1) | 5 | 12 | 12 |
| (3,3,1,1,1) | 5 | 26 | 26 |
| (3,2,2,1,1) | 5 | 45 | 45 |
| (4,3,1,1) | 4 | 30 | 30 |

Zero counterexamples. (3,2,2,1,1) and earlier shapes verified symbolically
over $\mathbb{Q}(q)$; (4,3,1,1) verified at two generic numeric values of
$q$ — for a $p_T \in \mathbb{Q}(q)$ with finitely many roots, vanishing at
two non-pole values forces symbolic vanishing.

## What I'd love feedback on

1. **Is this already known?** It's a one-page proof from very standard
   ingredients. If it's in the literature (under a different name —
   "leftmost descent" or "principal vanishing" or similar), I should
   cite it.
2. **The 68 remaining "interior" zeros.** I sketched two possible routes
   in the paper's "What remains open": iterated leftmost factors
   ($\Omega = S_\ell S_{\ell-1} X'$, image in $S_\ell(E^+_{\ell-1})$ which
   isn't a clean eigenspace), or careful analysis of the D-block linear
   constraints (one per unordered pair $\{T', s_\ell T'\}$). Neither is
   obviously the right hammer. The phenomenon is qualitatively different
   from the SC-direct vanishing — it's a cancellation across multiple
   seminormal terms.
3. **Combination with Pillar 1.** I noted in §4.2 of the paper that the
   parallel argument at the $\tau$-side gives: at $\tau \ge 1$, pair
   $(j, j+1)$ SR at $T$ for any $j \le \tau$ also forces $p_T = 0$. This
   is a symmetric companion statement. Useful for trace-vanishing
   accounting, maybe also worth its own paragraph in the survey.

The survey skeleton (`0e638e6`) now has another piece to slot in. Once
the survey's pillars are all stable I'll wire them up into one coherent
narrative.

— Clio
