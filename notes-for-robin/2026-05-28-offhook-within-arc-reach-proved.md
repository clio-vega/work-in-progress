# Off-hook order law: the within-arc reach lemma is PROVED (the crux you were left)

**2026-05-28 prove session.** Robin — the crux I flagged for you on 2026-05-27
("why does the within-arc scalar reduce to hook path-graph chip-firing?") is now
**answered and proved**, for the whole family $\lambda=(2,2,1^m)$.

Paper: `~/projects/proofs/2026-05-28-offhook-within-arc-reach.tex` (6pp, compiles).

## The mechanism (two ingredients, both clean)

**1. Inert-top restriction restores the hook rank-one collapse.**
A zero arc has generators $T_2,\dots,T_a$ (descending run), right boundary
$x\in W_1\cap W_{a+2}$, left covector $y\in W_1\cap W_{a+1}$. Restrict to
$W:=W_{a+2}$, the $q$-eigenspace of the **inert top generator** $T_{a+2}$ — which
commutes with every arc generator. Then each $P_q^{(j)}\!\restriction_W$ ($1\le j\le a$)
is **rank one**, image $W_j\cap W_{a+2}$, because $\dim(W_j\cap W_{a+2})=1$ is the
**pinch character value** $\frac14(f+2\chi_2+\chi_{22})$. So off hooks the
*single*-generator projector isn't rank one, but its restriction to the inert-top
eigenspace is — uniformly, because it's a character value. The hook world is restored
*on a subspace*.

**2. A triple-pinch sign-kill pins the left boundary to the two bottom vertices.**
New identity: $\frac18(f+3\chi_2+3\chi_{22}+\chi_{222})=0$ for all $(2,2,1^m)$, $m\ge2$
(verified $m\le6$; it's the trivial-isotypic dim of $S_2^3$ on three disjoint
transpositions — "three $q$-alignments can't coexist in a two-column shape"). Consequence
(**far sign-kill**): for $b,c\ge3$, $|b-c|\ge2$, the 1-dim joint $q$-eigvec $W_b\cap W_c$
is a $(-1)$-eigvec of $T_1$ (since $\dim(W_1\cap W_b\cap W_c)=0$). Hence any $q$-eigen-
covector $y$ of $T_1$ kills it: $q\,y^Tp = y^TT_1p = -y^Tp \Rightarrow y^Tp=0$.
Applied with $b=j,c=a+2$: **$y^Tp_j=0$ for $3\le j\le a$**.

**The reach.** One-line walk expansion of $\sigma_a(S)=y^T(\prod_{j=a}^2 A_j)p_1$ on $W$:
every term carries the factor $y^Tp_{\max V}$ with $V\supseteq Q=$ (the $P_q$ positions).
If any position $\ge3$ is left as $P_q$ then $\max V\ge3$ and **every** term dies. So
$\sigma_a(S)\ne0\Rightarrow\{3,\dots,a\}\subseteq S$, i.e. cost $\ge a-2$, unique minimiser
$\{3,\dots,a\}$. Strikingly, the lower bound needs **only** the rank-one collapse + the
sign-kill — not even tridiagonality (that's only for exhibiting survivors). Cleaner than
the hook proof.

Summing over the $\tau=m-1$ zero arcs ($a=3,\dots,n-3$):
$\sum(a-2)=\binom m2=\tau(\tau+1)/2$. **Intact-junction lower bound is now unconditional
for the family.**

## The one remaining gap (sharpened, localised)

The lower bound above covers subsets that leave all far junctions intact. But — important
discovery — at $(2,2,1,1,1)$, $|S|=3$, **13 of the 14 critical survivors BREAK a far
junction**; only 1 is intact. So the merged (broken-junction) case is the *generic*
survivor, not a corner. And it provably escapes the single-subspace trick: a merged
super-arc straddles two inert tops $T_{a+1},T_{a+2}$ joined by a defect generator adjacent
to the top, so no single $q$-eigenspace is invariant under all super-arc generators (I
verified forcing it into $W_6$ annihilates spuriously).

**Conjectural fix (your call):** mirror the hook merged-junction lemma — replace the single
restriction by a *sequence* of per-block restrictions glued at broken junctions; target
statement "a super-arc covering zero arcs $a_1<\dots<a_p$ needs $\ge\sum(a_i-2)$ insertions,
broken positions included." That closes the order law unconditionally for the infinite
family $(2,2,1^m)$ — the first non-hook instance.

$(2,2,1,1)$ and $(2,2,1,1,1)$ already hold outright (exhaustive min-support); the structural
*reason* for their lower bound is now supplied.

Scripts: `~/projects/scratch/2026-05-23-omega-monodromy-verify/2026-05-28-*.py`.
See [[offhook-rank1-pinch]] (crux now resolved), [[hook-orderlaw-chipfiring-proof]],
[[tau-closed-form-column1-charge]].
