# For Robin — 2026-05-17: Uniform per-trajectory invariant proved

## TL;DR

**Closed May-16 Conjecture 4.4 (support flow lemma) uniformly for all $a \ge 2$.**
The per-trajectory invariant — that $w_k(T') = \prod_j (T_j+1) \Phi_1(v_{T'})$
remains a non-degenerate $T_{n-1-k}$-2-block at every step $k$, with both
seminormal coefficients nonzero — was previously verified case-by-case at
$a=2,3,4$ (May-13, May-15-a3, May-16, with $2^{a-1}$ cases per step).
The new proof is structural and uniform: it reduces to a four-case lemma
depending only on which columns of $\lambda=(2^a,1^{n-2a})$ the three
consecutive entries $\{n-2-k, n-1-k, n-k\}$ occupy.

Writeup: `2026-05-17-trajectory-uniform.tex` (7pp).

## The structural lemma

For each step $k \in \{0, \ldots, a-2\}$, let $e_1 = n-2-k$, $e_2 = n-1-k$,
$e_3 = n-k$. Given $\{P_k^+, P_k^- = s_{e_2} P_k^+\}$ a non-degenerate
$T_{e_2}$-2-block, the claim is: exactly one of $\{P_k^+, P_k^-\}$ is
killed by $(T_{e_1}+1)$, the other yields a non-degenerate $T_{e_1}$-2-block.

**Proof in four cases.** By the same-row exclusion (May-16 Claim (4),
which uses $n \ge 3a$), each of $e_1, e_2, e_3$ lies in either
{col-1 row $> a$} or {col-2 row $\le a$} — only two "regions."
The non-degenerate $T_{e_2}$-2-block hypothesis forces $e_2, e_3$ into
*different* columns (one each in col-1 and col-2). So:

- **Case I**: $e_2$ in col-1, $e_3$ in col-2 (in $P_k^+$); swap roles in $P_k^-$.
- **Case II**: $e_2$ in col-2, $e_3$ in col-1 (in $P_k^+$); swap roles in $P_k^-$.

And $e_1$ is in col-1 (sub-case a) or col-2 (sub-case b), giving
$2 \times 2 = 4$ sub-cases. In each, the SYT-elementary fact
"consecutive integers in the same column occupy consecutive rows"
immediately identifies which element of $\{P_k^+, P_k^-\}$ has
$\{e_1, e_2\}$ same-column-adjacent (hence killed). The other has
$\{e_1, e_2\}$ at different rows and columns, with axial distance
$\ge 2$ (by the row-region separation), hence a non-degenerate
2-block.

The argument is symmetric across the four sub-cases — no encoding
bits, no inductive bookkeeping. The $n \ge 3a$ bound enters exactly
once, in the same-row exclusion.

## Why this matters

The May-16 paper's path-to-general-$a$ identified two pieces of
substantive work:

1. **Claim (1): exactly-one-killed per step** — said to need
   $2^{a-1}$ cases per step *at each $a$*, or a uniform positional
   invariant ("position of $n-1-k$ in $P_k^+$ vs $P_k^-$ follows a
   specific pattern determined by $\tau_1, \ldots, \tau_k$").
2. **Encoding identification: $\tau L / \tau R$**.

The new result closes (1) uniformly. The "positional invariant"
turns out to be \emph{trivial}: just which column $e_1$ is in.
Everything else follows from elementary SYT structure.

This means the rank-zero theorem
$\Pi^{S_n}|_{V_{(2^a,1^{n-2a})}} = 0$ for all $a \ge 2, n \ge 3a$ now
follows from the May-15-gen inductive reduction plus the May-13
base case, **conditional only on the general-$a$ Phase A endpoint**.

## What remains

(1) **Phase A endpoint at general $a$** — orthogonal piece, called
   "mechanical generalization" in May-15-gen, proved at $a=2,3$,
   not formalized for $a \ge 4$. Could be closed in a focused session.

(2) **L/R encoding identification (partially closed today)**.
   The paper adds a σ-invariant proposition:
   $$\sigma(P_k^+) \cap \{n-2a+1, \ldots, n-2-k\} = \sigma(T') \cap
   \{n-2a+1, \ldots, n-2-k\}.$$
   Proof: induction; the swap $s_{e_2}$ only affects entries $e_2, e_3$,
   both above $n-2-k$, so the lower range is unchanged by the swap;
   both elements of the pair carry the same lower-range $\sigma$,
   regardless of which survives.

   **Corollary**: the sub-case (a/b) at step $k+1$ is determined
   exactly by $\tau_{k+1}$ — Sub-case (b) iff $\tau_{k+1} = R$.

   This means: **the kill/expand trajectory is uniquely determined
   by the encoding $\tau$**.

   Still open: identifying the final pair as $\{T_{\tau L}, T_{\tau R}\}$
   in $S_a^{(n)}$ requires tracking $\sigma$ at the upper end
   $\{n-a, \ldots, n\}$ through the trajectory. Verified at $a=2$
   in the paper; conjectural at general $a$ (Conjecture conj:final-pair).

Without (2 full): rank-zero theorem and dimension bound $\le 1$.

With (2 full): full Conjecture 4.5 of May-16 — support exactly $S_a^{(n)}$.

## Computational verification

Exhaustively verified the structural lemma at:
- $a=2, n=6$: all 6 non-degenerate 2-blocks at $k=0$. Pass.
- $a=3, n=9$: all 56 across $k=0,1$. Pass.
- $a=4, n=12$: all 450 across $k=0,1,2$. Pass.
- **$a=5, n=15$: all 3432 across $k=0,1,2,3$. Pass.** (The case May-16 left open.)

[Verification script: `~/projects/scratch/2026-05-17-trajectory-uniform/verify_lemma.py`]

## Questions for you

1. **Trivial positional invariant.** The May-16 paper anticipated
   a complex positional invariant, but the resolution is dirt-simple:
   just column-of-$e_1$. The complexity in the case-by-case approach
   was illusory — it came from indexing by encoding bits when those
   bits weren't actually needed for the kill/expand step. Do you see
   a representation-theoretic principle this reflects? It feels like
   it's saying the kill/expand structure of $T_j$-action is "local"
   in a way that doesn't see the global combinatorics of $S_a$.

2. **Encoding identification via $\sigma$-tracking.** Sketch of the
   approach: $\sigma(P_k^+)$ alternates between two patterns
   depending on the kill/expand history. If I track $\sigma$
   explicitly through the four sub-cases at each step, the
   recursive structure of $S_a$ should emerge directly. Is this
   worth a separate session, or should I work on Phase A instead?

3. **Push status.** 28 unpushed commits, latest will be this one
   (`2026-05-17-trajectory-uniform.tex`). The PAT issue from May 6
   persists — I cannot push.

## Status of the rank-zero program

| Family | Status |
|--------|--------|
| $(1^n)$ sign rep | trivial |
| $(2,1^{n-2})$ hook | structural (May-11) |
| $(3,1^{n-3})$ hook | structural (May-12) |
| $(2,2,1^{n-4})$ non-hook a=2 | structural (May-13) |
| $(2,2,2,1^{n-6})$ a=3 | structural (May-15-a3) |
| $(2^4,1^{n-8})$ a=4 | structural (May-16) |
| **$(2^a,1^{n-2a})$ general $a$, $n \ge 3a$** | **structural conditional on Phase A (May-17, new!)** |

## Honest assessment

The result is more modest than it looks at first glance: the
**rank-zero theorem** is now uniformly proved (modulo Phase A), but
the **support-size $2^a$** statement (Conjecture 4.5) is NOT closed
uniformly — only the per-trajectory invariant, which gives a
2-element support per trajectory but doesn't show disjointness
across trajectories.

That said, the rank-zero theorem is the main mathematical content
of the family. The support identification is a refinement that
explains the specific structure $S_a^{(n)}$.
