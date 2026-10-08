# For Robin — PROVE 2026-08-29: C5 at level $\ell$ is false, and one page of Uglov is blocking the rest

## The short version

You set me the lift of C5 from level 1 to level $\ell$, and explicitly said a
clean refutation would be a success outcome. It is a refutation.

**Conjectured:** $\varepsilon_i(v^{[\ell]}_{k'}) \le 1$, level-independent.
**True:** the bound is $\#\{j : s_j \not\equiv i \bmod e\}$ — it grows
linearly in the level. Proved unconditionally on the crystal side, with
sharpness. `proofs/2026-08-29-C5-higher-level.tex` (12pp, compiles).

The smallest counterexample is four boxes: $e=2$, $\ell=2$, multicharge
$(0,0)$, $i=1$, the bipartition $((2),(2))$. Its $1$-signature is $AARR$ —
nothing cancels — and the crystal string is
$((2),(2)) \to ((1),(2)) \to ((1),(1))$, two genuine removals of $1$-nodes.
You can check it by hand in a minute.

## Why the level-1 proof doesn't lift, precisely

This is the part I think is worth your time, because the failure is
structural and not an artefact of my bookkeeping.

The level-1 proof had two moving parts: a **block analysis** showing the
$i$-signature of $e\lambda$ is $(AR)^n A^\delta$, and a **cancellation
argument** showing such a word reduces to at most one surviving $R$.

The block analysis lifts *verbatim*, once per component, charge-shifted. That
part is fine and I proved it. What does not lift is the second part, and the
brief's proposed patch — "concatenate the component words and re-reduce; the
running max plausibly stays $\le 1$" — mis-models the object in two ways:

1. The global signature is a **merge by content**, not a concatenation. The
   components interleave.
2. More importantly: by the bracket lemma, $\varepsilon_i$ of any word is the
   maximum over suffixes of $(\#R - \#A)$. Restricted to one component that
   quantity lies in $\{0,1\}$. Globally it is a **sum** over components, not a
   running maximum of one of them. So $\ell$ components can each contribute
   $+1$ at the same cut — and I give an explicit construction (all components
   single columns, lengths tuned mod $e$) showing they always can.

So the level-1 theorem was never really a theorem about the bound being $1$.
It was a theorem about *one component*, and $1$ was a coincidence of $\ell=1$.
Seen that way the result is the natural one, and I'd rather have this than the
lift I went in expecting.

Two robustness points, because this literature is full of convention traps:
the bound holds for **every** tie-breaking convention on equal contents (the
value of $\varepsilon_i$ does not — it changes in ~11% of sampled cases), and
the counterexample sits at multicharge $(0,0)$, so it survives whatever
$\Delta(\mathbf s)$ normalisation turns out to be right. That defensively
answers the Q51 gate my BROWSE flagged this morning.

## The ask: Uglov, Prop 3.16

**Uglov, "Canonical bases of higher-level $q$-deformed Fock spaces and
Kazhdan–Lusztig polynomials", Progr. Math. 191 (2000), Proposition 3.16.**
A PDF, a scan, or a photograph of that page.

Here is why I cannot get around it. To carry the result from the
multipartitions $e\boldsymbol\lambda$ to the actual Heisenberg descendant
$B_{-1}^{k'}|\emptyset;\mathbf s\rangle$ I need one hypothesis, (H2): that the
descendant reduces at $q=0$ to exactly those multipartitions. Given (H2) the
transfer is automatic and I prove it (all multiplicities are positive and
$\tilde e_i$ is injective where nonzero, so nothing cancels). Testing (H2)
needs $B_{-1}$ at level $\ell$, which needs $q$-wedge straightening, which is
Prop 3.16.

I have Iijima's restatement (his Prop 5.1) locally and I implemented it. It:

- reproduces **all four** of Iijima's own worked examples exactly;
- reproduces his wedge $\leftrightarrow$ multipartition dictionary, Example 2.6
  included;
- reproduces, at $\ell=1$, the Leclerc–Thibon formula
  $B_{-1}|\lambda\rangle = \sum(-q^{-1})^h|\mu\rangle$ on 79 partitions with
  zero mismatches;
- reproduces the level-dependent Heisenberg commutator
  $[B_1,B_{-1}] = \frac{1-q^{-2n}}{1-q^{-2}}\cdot\frac{1-q^{2\ell}}{1-q^2}$
  for every **constant** multicharge I tried.

And it is still wrong. The rewriting system is **not confluent** — leftmost-
versus rightmost-ascent straightening disagree on 244 of 2400 random wedges,
smallest instance $u_{-3}\wedge u_{-1}\wedge u_2$ at $n=\ell=2$. Since
$\Lambda^{\mathbf s}$ is a quadratic quotient, a correct two-factor rule must
be confluent, so what I have is not it. I then searched 98,304 readings of the
printed formula (all plausible case-splits for $\alpha,\beta,\gamma$, both
index assignments, an optional extra $q^\alpha$); **none** is both
example-consistent and confluent. That tells me the *shape* of the formula I'm
reading is wrong, not merely a case split, and no further grinding on the
local text will fix it.

Two concrete defects in that text, for whoever looks:

1. $\gamma$ is **undefined** when $d_1 = d_2$ — the printed definition covers
   only $d_1 < d_2$ and $d_1 > d_2$. Iijima's Example 2.5 forces $\gamma = 1$
   there.
2. At $q=1$ all correction terms vanish and the exchange in a semi-infinite
   wedge should be $-1$. The printed leading coefficient gives $+1$ when
   $d_1 \ne d_2$, and Iijima's own Example 2.1(ii) exhibits exactly this
   ($u_{-2}\wedge u_4 = u_4 \wedge u_{-2}$ at $q=1$). Either there is a sign
   twist in the identification with the classical wedge that I haven't
   accounted for, or something is transcribed wrong.

This blocks **all** $\ell \ge 2$ computation in the Fock programme, not just
C5. Everything else in the pipeline is built and validated; it is one
function.

## One correction to the brief

"Step 1 ($v \in \mathcal L$) lifts verbatim" is false as written. $B_{-1}$ has
coefficients in $\mathbb Z[q^{-1}]$, so $B_{-1}^{k'}|\emptyset\rangle$ is not
in the lower crystal lattice at all ($q^{-2}$ appears already at $k'=2$). The
level-1 theorem is about $P_e$, which is the coefficientwise bar-conjugate of
$B_{-1}$. The repair is clean — use $P^{[\ell]}_e$, or the upper lattice — and
it actually *improves* the level-1 statement from "equal up to a correction"
to equal on the nose. But it is the third normalisation trap in this programme
in a month, after the $B_{\pm1}$ convention and the Kwon–Lee $\psi$-twist, and
this morning's BROWSE independently flagged the pattern as structural. I am
now treating normalisation as the first thing to check, not the last.

## What I did not do

- (H2): untested, and I have not claimed the C5 statement. §6 of the paper
  says exactly why, reproducibly.
- The vertical/transpose observation ($\varepsilon_i \equiv 0$ for
  multipartitions whose parts repeat $e$ times, 497,814 checks): stated as a
  computational observation only. It is presumably Gerber–Norton's bicrystal
  commutation, but Gerber is only at agent-summary depth in my citation index
  and I will not cite what I have not read.
- The exact threshold in $k'$ above which sharpness kicks in.

## Sage

Flag #7. Not needed today — everything was hand-written exact-integer Python —
but still absent.
