# Q150, prove cycle 2 — an operator that adds ONE ribbon shape and still commutes

**2026-09-16, cycle 2.** Follows this morning's cycle-1 refutation
(`for-robin/2026-09-16-Q150-nonvanishing-refuted.md`). Cycle 1 asked you to hand-check its
$(3,6)$ counterexample before anything else. **I did that first** — see below — and then went
after the gap it left, (H2).

- Paper: https://github.com/clio-vega/proofs/blob/main/2026-09-16-c2-Q150-H2-single-shape.tex
  (11 pp, compiles clean) — PDF alongside it, code at `code/2026-09-16-c2-Q150-H2/`,
  commit `clio-vega/proofs@48296e9`.

## 1. The cycle-1 counterexample survives an independent check

I rewrote the operator from Q149 Convention 1.2 alone — a fresh engine sharing no code with the
Q149 or Q150 engines. It reproduces the word↔ribbon-shape dictionary on 1375 bead moves with no
mismatch, and $[R_3^W,R_6^{\bar W}]$ annihilates all 195 partitions with $|\lambda|\le11$. Seven
perturbations all break it; a Murnaghan–Nakayama positive control is correctly silent. So the
refutation is real and you can trust the object.

**One correction.** Cycle 1's Theorem 6.7 lists $W_{(2,1)}=-1$, $W_{(3)}=W_{(1,1,1)}=0$ — and
says nothing about the fourth composition of 3. It is not free: setting $W_{(1,2)}=1$ breaks
commutation on 35 of 97 partitions. The intended value is 0 (the proof builds $\tau$ as an
indicator, so the *object* is right; only the displayed statement is incomplete). Fixed in §3 of
the new paper. Nothing else in cycle 1 changes.

## 2. The headline

> For every $d\ge3$ there is an operator that **adds exactly one ribbon shape, and nothing
> else**, and commutes with an explicit partner of every rank $kd$.

The refuted lemma said a commuting partner forces every weight value to be nonzero. The sharpest
possible refutation isn't "some value vanishes" — it's "all but one vanishes". Which single
shapes work is a condition on the *word's borders*:

> $c\cdot\mathbb{1}_w$ satisfies (2B$^*_d$) $\iff$ for every border length $p$ of $w$,
> $w_{p+1}\ne w_{n-p}$  ($n=d-1$; $p=0$ is always a border).

The $p=0$ clause alone says: **exactly one of the two end rows of the ribbon has length 1.** For
$d\le5$ that is the whole criterion; from $d=6$ the longer borders bite (first failure $w=01001$,
which has period $3=d/2$). Counts: $2,4,8,12,28,48,104$ shapes for $d=3,\dots,9$.

Smallest genuinely new case, $(e,f)=(4,8)$: $W_{(1,3)}=-1$ and the other seven rank-4 values
zero; $\bar W_{(1,4,3)}=+1$, $\bar W_{(1,3,1,3)}=-1$, the other 126 zero. That's the whole pair.

These are new even given cycle 1: its Theorem 6.6 routes through the strong condition
(2B$^{**}_d$), and **for even $d$ no single-shape weight satisfies (2B$^{**}$ )** — the
solutions there are exactly the antipalindromes $w_i\ne w_{n+1-i}$, which need $d$ odd. So the
$d=4,6,8$ examples are invisible from that side.

## 3. Half of (H2), and where the "3" comes from

Cycle 1 had observed computationally at $d\le5$ that every proper support sits inside one of the
cylinders $\mathcal{C}_{j,b}=\{w_j=b,\ w_{d-j}=1-b\}$. That is now a theorem for all $d$, with a
refinement: for the *minimal* such $j$, the support is invariant under flipping every coordinate
in $\{1..j-1\}\cup\{d-j+1..d-1\}$. The proof is a short induction — at step $j$ the two-bead
condition says two product sets are equal, which forces either two new flip-symmetries or
containment in a cylinder; if the second branch never fires, the support is flip-invariant
everywhere, hence empty or everything.

Two things fall out that I like more than the theorem:

- it **reproves** the $\gcd\le2$ nonvanishing (cycle 1's Thm 6.1) at the level of supports, with
  no case analysis;
- it **explains the threshold**. $\mathcal{C}_{j,b}$ is nonempty exactly when $j\ne d-j$. So
  proper supports exist iff $[1,d-1]$ contains an index $j\ne d/2$ — iff $d\ge3$. The "3" in
  "$\gcd(e,f)\ge3$" was never about ribbons; it is the smallest $d$ whose index set has an
  asymmetric element.

## 4. What I'd like you to look at

1. **The border criterion.** It is short enough to check by hand at $d=6$: $w=01001$ has border
   $p=2$ and $w_3=w_3$, so it fails — and the explicit two-bead witness in `witness.py` shows
   the commutator really is nonzero there. I'd value a second pair of eyes on the substitution
   $p=n-\delta$ in the proof of Theorem 4.2; it is the only place indices could go wrong, and I
   got it wrong once already (see below).
2. **Is the border condition known?** "For every border $p$, $w_{p+1}\ne w_{n-p}$" is a
   free-monoid condition and feels like something Lothaire would name. The counts
   $2,4,8,12,28,48,104$ are not a sequence I recognise. If this is a known class of words the
   whole of §4 is a citation rather than a proof. **I did not browse** — prove sessions don't —
   so this is genuinely unchecked.
3. **What remains of (H2)** is the interior of a cylinder: which sets of *middle* words are
   admissible. I reduce it to a condition of the same shape as the original but with a pinned
   letter beside the toggled one, and it does **not** self-reduce. Counts $1,3,11,31,356$. The
   jump $31\to356$ says it is not a product formula. Stated precisely as (H2a) in §9.

## 5. Two instrument failures, recorded

Both are the kind I keep re-committing, so they are in the code README.

- My constraint-propagation search reported 2 and 4 admissible supports at $d=4,5$ where brute
  force gives 8 and 26 — it failed to undo assignments made during a propagation that ended in a
  conflict. The brute-force calibration is what caught it.
- **A silent negative control.** Scanning small partitions for a nonzero commutator is
  degenerate: the two-bead witness needs a window of width $e+f$, which no partition of size
  $\le14$ realises. My first run of the control was silent and I nearly read that as support for
  the criterion. The fix was to construct the witness from the bead geometry rather than sample
  — and an off-by-one in *that* ($\delta=n+1-p$ instead of $n-p$) then made it report zero for
  the positive cases too, which is how it was caught. 112/112 hard cases now fire, $d\le10$.

## 6. Status of the publishable unit

Q91+Q92+Q147+Q149+Q150 still needs Q150 folded in with one corollary changed, as cycle 1 said.
Nothing here blocks that; §4–§5 are a clean extra section ("the extreme counterexamples") and §6
turns one of cycle 1's computational remarks into a theorem. PROTOCOL §4.2 says the write-up
goes through Rick first.

---

## ADDENDUM (same session, later) — the statement the refuted lemma should have had

Two more corollaries, and they change what the headline is.

**The maximal proper supports are exactly the cylinders $\mathcal{C}_{j,b}$** — each is
admissible (cycle 1's Lemma 6.5), every proper one sits inside one (Theorem C), and they all
have the same size $2^{d-3}$ so none contains another.

**Hence a dichotomy.** A nonzero rank-$d$ weight satisfying (2B$^*_d$) either vanishes
**nowhere** or vanishes at **more than three quarters** of all rank-$d$ ribbon shapes
($|\mathrm{supp}\,\tau|\le 2^{d-3}=\frac14 2^{d-1}$). Nothing in between. In operator terms:
if $[R_e^W,R_f^{\bar W}]=0$ with both nonzero, then either $W$ is nowhere zero or it is
supported on at most a fraction $4^{-e/d}$ of the $2^{e-1}$ shapes of rank $e$.

This is what Q149's Lemma 8.2 was reaching for. It asserted the *first* alternative of a genuine
dichotomy and lost the second. The 09-16 browse had suggested exactly this retargeting (on the
strength of Terwilliger's PA2/PA5 being independent conditions, and the shape of
Shiraishi–Yamaguchi); it turns out to be provable here, and it is a better theorem than the
nonvanishing lemma would have been.

**And a generation theorem.** $Z$ is admissible iff closed under one rule: if $u,v\in Z$ are
$\delta$-linked ($u_{[\delta+1,n]}=v_{[1,n-\delta]}$ and $u_\delta=v_{n-\delta+1}$) then $u$
with position $\delta$ flipped and $v$ with position $n-\delta+1$ flipped are both in $Z$.
Consequently the admissible sets are closed under arbitrary intersection — they are the models
of an explicit definite-Horn theory — and Theorem A is exactly the statement
$\langle\{w\}\rangle=\{w\}$. This is also my reason for not expecting a product formula in
(H2a): counting models of a Horn theory rarely has one.

**Where the ribbon structure enters** (the question the browse appendix asked me to answer
before attempting). Not connectivity — a multiplicative structure on the cube does *not* force a
product support without positivity, which is why Hammersley–Clifford assumes $P>0$, so any
connectivity argument here would prove something known false. What the proof uses is the
*shared block* $\pi'$ in Q149's Lemma 4.3 — the overlap of the two bead windows. It makes the
two sides of the two-bead condition an equality of **product sets**, and product-set rigidity is
what forces the dichotomy. The only escape is an asymmetry between positions $j$ and $d-j$,
which is precisely what $\mathcal{C}_{j,b}$ is.

Paper is now 13 pp; commit `clio-vega/proofs@d1827f8`.

## Closing note — the obvious next step is closed

Theorem C's induction works because the maximal proper admissible sets have a *uniform shape*:
they are exactly the cylinders, all of size $2^{d-3}$. One level down that fails. The maximal
proper admissible **subsets of** $\mathcal{C}_{1,0}$, in middle-word coordinates, number
$3,4,11$ at $m=2,3,4$ with sizes $\{2,3,3\}$, $\{4,4,5,5\}$,
$\{4,4,5,5,5,5,6,6,7,9,13\}$ out of $2^m$. None is a sub-cylinder; from $m=3$ none is even a
co-singleton. **There is no uniform maximal shape to induct on**, so the argument has no second
step, and I'd rather record that than have a future session spend three pages rediscovering it.

Combined with the Horn framing, my expectation is that (H2a) has no closed-form answer and the
right statement is the dichotomy plus the closure operator. If you disagree I'd like to know —
it's the kind of judgement I'd rather not make alone.

Final: 13 pp, `clio-vega/proofs@` (see `git log`), registry validates, trajectory has one
acknowledged circular edge (the constructed control, flagged in §8 V5$'$).
