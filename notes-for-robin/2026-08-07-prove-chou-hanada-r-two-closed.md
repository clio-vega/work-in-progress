# Chou-Hanada $r=2$ rectangular graded Frobenius: CLOSED

**Session:** 2026-08-07 PROVE (~60 min). **Proof:** `~/projects/proofs/2026-08-07-chou-hanada-r-two-conjecture.{tex,pdf}` (5pp).

## Theorem

For every $k \ge 1$,
$$\Frob_q\bigl(R_{2k,(k,k),2}\bigr) \;=\; \sum_{j=0}^{k} q^{j}\, s_{(2k-j,\,j)}.$$

Here $R_{n,\lambda,s}$ is the Chou-Hanada $\Delta$-Springer ring (arXiv 2509.24252). One Schur module per two-row shape $(2k-j, j)$, each in its own graded degree $j$.

Ungraded: $\sum_{j=0}^k f^{(2k-j, j)} = \binom{2k}{k} = \dim R_{2k, (k,k), 2}$ (from CH Cor. 2.34). Matches.

## Why this is nice

Ungraded, the identity recovers the multiplicity-free branching
$$\Ind_{S_k \wr S_2}^{S_{2k}} \mathbf 1 = \bigoplus_{j=0}^k S^{(2k-j, j)}.$$
The theorem places each summand in degree = displacement from the trivial summand $S^{(2k)}$. It's a **graded Pieri decomposition** — the two-row Pieri sum $h_k h_k = \sum_j s_{(2k-j, j)}$ with grading.

## Proof shape (4 lemmas)

Reduces (via CH Cor. 2.33) to enumerating $S \in \SYT(2k)$ with $\des(S) \le 1$ and $\ctype(S) \dom (k, k)$; $\mu = \emptyset$ is forced.

1. **Row bound** (novelty here: I couldn't find this in the tableau literature at exactly this granularity, though it's likely folklore). For any SYT of shape $\nu$, $\des(S) \ge \ell(\nu) - 1$. Proof: for each $r = 2, \ldots, \ell$, the column-1 entry $v_r$ of row $r$ has $v_r - 1$ in row $< r$ (can't be in row $r$ since $v_r$ is minimum there; can't be in row $r' > r$ since column-1 strict increase forces $v_{r'} > v_r > v_r - 1$). So descent at $v_r - 1$.

2. **Uniqueness.** For $\des(S) \le 1$, exactly one SYT $S_j$ of each two-row shape $(2k-j, j)$ qualifies: the flat one with $1, \ldots, 2k-j$ in row 1 and $2k-j+1, \ldots, 2k$ in row 2. The single descent is at position $2k-j$.

3. **Cocharge.** By direct label count using CH Def. 2.14: labels $0$ for row-1 entries, $1$ for row-2 entries. Sum $= j$.

4. **Ctype via Blasiak's algorithm.** Cocharge word is $z = 1^j 0^{2k-j}$. Reading from the right: first $2k-j$ zeros consume into row 1 (always legal); then $j$ ones consume into row 2 (legal at each step iff $\nu_2 + 1 \le \nu_1 = 2k-j$, which holds throughout since $j \le k \le 2k - j$). Result: $\ctype(S_j) = (2k-j, j) \dom (k, k)$. The dominance is automatic in the range $0 \le j \le k$.

## Verification

Sage-free Python enumeration of the CH higher-Specht index set for $k = 2, 3, 4, 5$:
- $k = 2$: matches term-by-term, dim $= 6$ ✓
- $k = 3$: matches, dim $= 20$ ✓
- $k = 4$: matches, dim $= 70$ ✓
- $k = 5$: matches, dim $= 252$ ✓

Probe script: `~/projects/probes/2026-08-07-chou-hanada-graded-frobenius/probe.py`. Same script used in the 2026-08-07 WAKE that surfaced the conjecture; extended verification runs in seconds.

## What's next

Sibling note territory, orthogonal to v1. Two options:

(a) **Post-v1 short arXiv note.** 5pp already. Could rest as-is or grow with:
- discussion of Chevalley-Molien parabolic quotient scale vs coinvariant scale;
- comparison with Griffin's higher-Specht basis at other rectangular parameters;
- open question: what's the analogous formula for $r \ge 3$? (Rank-$r$ pattern is genuinely richer — coefficients like $q + q^2$ appear.)

(b) **Roll into composite-$d$ §6 as an aside.** Costs ~half a page in the composite-$d$ paper; sacrifices the standalone framing.

**My preference:** (a). The composite-$d$ paper is already tight, and this result is a $q$-graded lift of a classical branching identity — deserves its own citation home. Post-v1, 3-4 weeks out, low overhead.

**Your call.** Everything is ready and shippable.

## Position vs. composite-$d$

Orthogonal. The Chou-Hanada module $R_{2k, (k,k), 2}$ is parabolic-quotient scale (dim $\binom{2k}{k}$); the composite-$d$ ambient $H_n$ is coinvariant scale (dim $n!$). They meet only in that both use the same Frobenius symmetric-function machinery. The composite-$d$ story is about cyclic-action structure on $H_n$ (Coxeter regular element / promotion); this result is about a graded Pieri decomposition of an induction from $S_k \wr S_2$.

**One-line summary.** Chou-Hanada $r=2$ rectangular conjecture is proved, 5pp .tex+PDF ready. Sibling note post-v1.

—Clio, 2026-08-07
