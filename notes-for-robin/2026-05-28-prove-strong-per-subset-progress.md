# Prove session followup — strong $\Omega$-vanishing $|S|=0$ closed

**Date.** 2026-05-28, prove session (after wake-3 reseed).
**Paper.** `~/projects/proofs/2026-05-28-strong-per-subset-operator-vanishing.tex` (compiles, 6 pages).
**Previous note.** [[2026-05-28-strong-per-subset-operator-vanishing]] (which raised the empirical finding; this note reports the proof attempt).

## What I proved

For $\lambda = (2,2,1^m)$ with $m \ge 2$, **$\Omega = 0$ as an operator on $V^\lambda$**.

This is the $|S| = 0$ case of strong per-subset operator vanishing. The proof is a two-line corollary of your Pillar 1 meta-theorem:

1. Pillar 1: $\Om^{(\lambda)}(V^\lambda) = B^{(\lambda)} \subseteq E_1^-$ when $\tau \ge 1$.
2. Split $\Omega = R \cdot \Om^{(\lambda)}$ with $R = \Rp_2 \cdots \Rp_\ell$. The rightmost factor of $R$ is $\Rp_\ell$, whose rightmost component is $S_1 = T_1+1$, which kills $E_1^-$. So $\Omega(V^\lambda) = R(B^{(\lambda)}) \subseteq R(E_1^-) = 0$.

Specialised to $\lambda = (2,2,1^m)$: $\hat\lambda = (2,2)$ satisfies Pillar 1's hypotheses; standing hypothesis $q \ge 2$ is $m \ge 2$.

This **upgrades the trace-vanishing forward direction** ([[two-sided-sign-kill]]) to a full operator vanishing — a strict strengthening. It's the cleanest one-line consequence of Pillar 1 I noticed in the prove session.

## What I couldn't push through ($|S| \ge 1$)

The general $|S| < D$ conjecture, where $D = m(m-1)/2$. The empirical picture at $m=3$ (the $232$-subset sweep):

| case | count |
|---|---|
| $M_T(S_T) V^\lambda \subseteq E_1^-$ AND prefix has $P_q^{(1)}$ at some last-of-block $s_1$ position | 229 |
| $M_T(S_T) V^\lambda \not\subseteq E_1^-$ AND $\not\subseteq E_2^-$ | 3 |

All 232 give $M(S) = 0$ on $V^\lambda$, but **only the sub-case where the rightmost prefix position is not in $S$** extends the $|S|=0$ proof verbatim. The rest need either:

- **A per-subset Pillar 1**: $M_T(S_T) V^\lambda \subseteq \bigcap_{j=1}^{\tau-|S_T|} E_j^-$ for $|S_T| < \tau$. If true, prefix factors at letter $s_j$ preserve containment in $E_j^-$ (since they project onto $E_j^\pm$), and any $P_q^{(j)}$ in the chain provides a kill.
- **The 3 outliers** at $|S_T| = \tau$ ($S = \{11,12\}, \{12,15\}, \{15,16\}$): all $S_R = \emptyset$, so $M_R = \Omega_{S_\ell}$, which kills $\tau \ge 1$ summands by induction. Image of $M_T$ projects into $\ker(\Omega_{S_\ell}|_{V^{(2,2,1)}})$ — verified case-by-case but no structural reason yet.

## Refined conjecture (target for next session)

**Per-subset Pillar 1.** For $\lambda = (\hat\lambda, 1^q)$ in your Pillar 1 regime and any $S_T \subseteq \{\binom{\ell}{2},\ldots,N-1\}$ with $|S_T| < \tau$:
$$M_T(S_T) V^\lambda \subseteq \bigcap_{j=1}^{\tau-|S_T|} E_j^-.$$

Track which $E_j^-$ layer each $P_{-1}$ in $S_T$ "consumes". The proof would extend your multi-row meta-theorem to mixed $P_q/P_{-1}$ chains: $\Phi$-embedding + threshold-matching, but per-subset. Each $P_{-1}$ flip degrades the containment by at most one level.

The $|S_T| = \tau$ boundary (where the refined statement says nothing) is where the 3 outliers live — they need the inductive-kernel mechanism on the $\tau = 0$ summand. So the full proof structure is **two complementary pieces**.

## Where I'm honestly stuck

- Cannot prove "running result stays in $E_j^-$ through prefix factors at letter $s_k$ with $k \ne j$". $T_k$ doesn't commute with $T_j$ for $|j-k| = 1$, so the layered $E_j^-$-containment is not obviously preserved.
- The refined per-subset Pillar 1 is exactly what would resolve this, but proving it requires lifting your meta-theorem machinery to per-subset — non-trivial.
- The 3 outliers at $m=3$: I have empirical verification but no clean structural reason. They all have $S_T$ = adjacent letter-pairs in the tail: $\{s_4, s_3\}, \{s_3, s_6\}, \{s_6, s_5\}$. Pattern unclear.

## Methodological note

The wake-3 conjecture (read after this session) suggested attacking via "kill-point combinatorics" — bound the prefix length where the running product first vanishes. The script verified this is the right phenomenon: kills happen at the first $T_\ell$ or first $T_{\ell+1}$ in the staircase, with prev-rank always 1. But the kill mechanism turns out to be the *backwards* read: not "prefix kills early", but "tail image is restricted, prefix has $S_j$ kill to dispatch it". Both are valid framings; the second is the one that connects to Pillar 1.

## What I'd like your eye on

- Does the per-subset Pillar 1 conjecture look plausible? It's a natural extension of your meta-theorem.
- The $|S|=0$ argument feels too short. Is there a hidden hypothesis I'm using? (Pillar 1's standing hypothesis is the only one.)
- The 3 outliers: any pattern recognition from a wider perspective?

Push to GitHub on request.
