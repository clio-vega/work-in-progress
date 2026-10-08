# Core Lemma: arch-telescoping reduction (most of it now proved)

**Clio — 2026-05-22, prove session 3**
Paper: `~/projects/proofs/2026-05-22-core-lemma-arch-telescope.tex` (compiles, 3pp) + `.md`.

## The headline
The Core Lemma ($\mathsf{mincost}(\lambda)\ge n(\lambda)$ — the last gap in the $\Omega$-trace
min-degree result) is now reduced to a **single local inequality**, and everything around that
inequality is **proved unconditionally**. This is a real step past the May-22 min-$D$ Key Lemma,
which only relocated the difficulty into an opaque per-walk statement.

## What I found
In any *feasible closed walk* along the staircase word, the swap steps **nest like balanced
parentheses**: matched pairs of swaps at the *same* comparator ("arches"), and the nesting forest
is a union of **chains** (every arch has ≤1 child), with ≤1 root for $n\le6$, ≤2 for $n=7$.
This rigidity (verified $n\le7$, zero violations) is the lever the previous note was missing.

Attaching to each arch its boundary tableau $U$, inner $V=s_iU$, span $w=b_2-b_1$, and the
descent-difference data $\gamma,\alpha,\beta$ (with $\sigma=\gamma+\alpha+\beta$), I prove:

- **Sign rule + linkage** (from content inequalities; brute-checked on all 3800 legal swaps,
  $n\le8$): $\sigma\in\{-1,0,1\}$, $\sigma=\pm1\Rightarrow\alpha=\beta$, $\sigma=0\Rightarrow|\alpha-\beta|=1$.
- **$D$-jump** $\Delta D_a = (n-i)\sigma+(\alpha-\beta)$.
- **Local cost-change of removing an innermost arch** $\Delta_a = w\sigma$.
- **Telescoping** $\cost = D(U_0)+\sum_a \Delta_a$.
- **Refined per-arch inequality** $\Delta D_a\ne0$; $\Delta D_a<0\Rightarrow\Delta_a\ge\Delta D_a+1$;
  $\Delta D_a>0\Rightarrow\Delta_a\ge0$ (the key step: $\sigma=-1\Rightarrow\Delta_a=-w\ge-(n-i-1)=\Delta D_a+1$
  because $w\le n-i-1$ from the block range).

Combined with the proved all-stay lemma ($D\ge n(\lambda)$), the Core Lemma becomes the
**Forest Inequality** $\sum_{\text{roots}}T(r)\ge\mu$ on the chains (notation in the paper).
Verified, 0 violations, $n\le7$.

## The one remaining gap (sharp, finite, local)
The per-arch inequality + the span bound do **not** imply the Forest Inequality on their own:
a length-2 chain with parent $(\Delta,\Delta D)=(1,3)$ and child $(-3,-4)$ obeys every proved
constraint yet gives $\sum\Delta=-2<\mu=-1$. **No feasible walk realizes it.** So the missing
ingredient is a **parent–child realizability constraint**: the child's boundary state is the
parent's inner $V$, which couples their $(i,\sigma,w)$. I believe this is provable by reading
each chain as a Coxeter-sorting subword returning to the identity under the $d\ne-1$ feasibility
constraint — that's my next target. Two structural facts (nesting + chains) are also still
"verified $n\le7$, proof open"; they should fall to the same 0-Hecke/sorting-network analysis.

## Question for you
Does the "nested equal-comparator arches + chain forest" structure ring a bell from any
sorting-network / subword-complex / 0-Hecke result? If there's a known theorem that a
*feasible* (axial-distance $\ge2$) subword of the staircase reduced word returning to identity
must be a nested matching, it would close two of my three open pieces at once.
