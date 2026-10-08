# PROVE session 2026-08-08 — Chou-Hanada $r=3$ rectangular graded Frobenius CLOSED

## Result

**Theorem.** For all $k \ge 1$,
$$\mathrm{Frob}_q(R_{3k,(k,k,k),3}) \;=\; \sum_{\substack{\lambda \vdash 3k \\ \ell(\lambda) \le 3 \\ \lambda \dom (k,k,k)}} q^{n(\lambda)}\, [K_{\lambda,(k,k,k)}]_q\, s_\lambda,$$
where $n(\lambda) = \lambda_2 + 2\lambda_3$, $K_{\lambda,(k,k,k)}$ is the Kostka number, and $[m]_q = 1 + q + \cdots + q^{m-1}$.

**Standalone proof**: `~/projects/proofs/2026-08-08-chou-hanada-r-three-conjecture.{tex,pdf}` (7 pp).

## Structure of the proof

Three-step reduction plus a direct SSYT enumeration:

1. **Apply Chou-Hanada Cor 2.33** at $(n,\lambda_{\text{CH}},s) = (3k,(k^3),3)$: the second-slot rectangle collapses ($\mu = \emptyset$), giving
$$\mathrm{Frob}_q = \sum_{S \in \SYT(3k),\ \des(S) \le 2,\ \ctype(S) \dom (k^3)} q^{\cocharge(S)}\, s_{\sh(S)}.$$

2. **Descent constraint is redundant.** Blasiak's algorithm has the property that any cocharge label $a$ in the initial word eventually contributes a box to some row $\ge a+1$ of $\ctype$. So $\des(S) \ge 3 \Rightarrow \ell(\ctype(S)) \ge 4 \Rightarrow \ctype(S) \not\dom (k^3)$. Contrapositive gives redundancy.

3. **Apply Lascoux-Schützenberger** (Blasiak Prop 2.19): the ctype-catabolisable SYT cocharge sum equals the modified/cocharge Kostka-Foulkes polynomial $\widetilde K_{\lambda,\mu}(q) = q^{n(\mu)} K_{\lambda,\mu}(1/q) = \sum_{T \in \SSYT(\lambda,\mu)} q^{\cocharge(T)}$. This reduces to computing $\widetilde K_{\lambda,(k^3)}(q)$.

4. **Closed form for $\widetilde K_{\lambda,(k^3)}(q)$ (the substantive new content).** Parametrise $\SSYT(\lambda,(k^3))$ by $y_2 \in [\alpha, \beta]$ where $\alpha = \max(\lambda_3, 2k-\lambda_1)$, $\beta = \min(\lambda_2, 2k-\lambda_2)$, $y_2$ = # $2$'s in row 2 (English convention). Then $K_{\lambda,(k^3)} = \beta - \alpha + 1$, and via a segment-by-segment analysis of the LS charge algorithm on the reading word $w = 3^{z_1} 2^{y_1} 1^k \cdot 3^{z_2} 2^{y_2} \cdot 3^{\lambda_3}$ (partitioned into six run segments $A,B,C,D,E,F$),
$$\cocharge(T_{y_2}) = n(\lambda) + (y_2 - \alpha).$$
Sum: $\widetilde K_{\lambda,(k^3)}(q) = q^{n(\lambda)} [K]_q$.

The cocharge calculation splits into two sub-cases ($\lambda_2 \le k$ vs $\lambda_2 \ge k$), producing the same final formula in each. The core object is the "$E$-rounds / $B$-rounds" bookkeeping on the LS extraction, with 6 subword types (indexed by which segment provides the $2$ and the $3$) and their charges $\{0, 1, 1, 2, 2, 3\}$.

## Aesthetic reading

**Rank 2 was multiplicity-free-per-shape** (each Schur coefficient was a single $q^j$, forced by $\des \le 1 \Rightarrow \ell(\lambda) \le 2$ AND uniqueness of the qualifying SYT per two-row shape).

**Rank 3 is $q$-integer-per-shape** (each Schur coefficient is $q^{n(\lambda)}[K]_q$ — $K$ SSYTs, cocharges forming a contiguous run). The multiplicity is now genuine, but organised as an arithmetic progression of graded degrees.

**Rank 4 breaks** (e.g., $f^{(2,2)}(q) = q^2 + q^4$ has a gap). So the $q$-integer-per-shape phenomenon is *specifically a three-row story* — driven by the descent bound $\le 2$ pinning shapes to $\le 3$ rows AND the $y_2$-parametrisation of SSYT being one-dimensional (single parameter for three-row weight $(k^3)$).

This is the *right level* of the pattern: the arithmetic-progression phenomenon captures both the ungraded Kostka number $K$ and the graded shift $n(\lambda)$ in a single clean formula, which specialises to the $r=2$ case ($K \equiv 1$, coefficient $q^j$).

## Verification

- $k = 1$: matches coinvariant algebra $H_3$ (3 shapes, dim 6). ✓
- $k = 2$: 7 shapes, dim 90. ✓
- $k = 3$: 12 shapes, dim 1680. ✓
- $k = 4$: 22 shapes, dim 34650. ✓ (**extra cross-check beyond the paper's stated $k \le 3$**)

Probes: `~/projects/probes/2026-08-08-chou-hanada-r-three/{probe_r3,kostka_foulkes,compare_kf}.py`.

## Position

**Orthogonal to composite-$d$ v1.** This is a "$q$-graded lift of a rectangular Pieri" style result, sibling to the $r=2$ note already written. Together they form the first two rectangular ranks $(r=2, r=3)$ of the Chou-Hanada modules at their diagonal $s = r$ parameters. **Post-v1 territory.**

Not blocking v1 arXiv push. This is a standalone 7-page note, worth posting separately (or as a short series with the $r=2$ note, since they share aesthetic and template).

**v1 arXiv push STILL UNBLOCKED 8th consecutive day. STRONG RECOMMEND.**

## Ring-level footnote (not proved here, but implied)

The identification $\mathrm{Frob}_q(R_{3k,(k^3),3}) = \sum_\lambda \widetilde K_{\lambda,(k^3)}(q) s_\lambda = H'_{(k^3)}(x;q)$ says $R_{3k,(k^3),3}$ has the same graded Frobenius as the DeConcini-Procesi ring $\mathcal R_{(k^3)}$. So $R_{3k,(k^3),3} \cong \mathcal R_{(k^3)}^{DP}$ at the graded-character level (probably as graded $S_{3k}$-modules too, via CH's construction). This context isn't needed for the proof but is noted in the discussion section.

## Emotional register

Delight is quiet. The pattern **$c_\lambda(q) = q^{n(\lambda)}[K_{\lambda,(k^3)}]_q$** is a rare kind of formula: three separate ingredients (a Kostka number, a partition statistic, a $q$-integer) fitting together with no leftover degrees of freedom. When I saw the data — every polynomial an arithmetic progression, starting at a specific power — the shape was immediately visible before any structural understanding.

The proof took ~90 minutes: 20 minutes running probes and reading the data, 15 minutes recognising it as cocharge KF via the $q \leftrightarrow 1/q$ symmetry, 30 minutes case-analysing the LS extraction on the six-segment reading word (this was the hardest part), 20 minutes writing up. The writeup went cleanly because the case analysis had already resolved into a single closed formula.

**The right level of the pattern is what makes it worth writing up.** Not "here are 22 polynomials for $k \le 3$", but "each polynomial is one $q$-integer per Schur function, with a specific shift." The graded degrees form an arithmetic progression *because* the SSYT parametrise as $y_2$ over an interval and cocharge increments with $y_2$ by exactly 1 per step. That is the story: SSYT and their cocharges form a one-parameter family whose cocharge is a rank function.
