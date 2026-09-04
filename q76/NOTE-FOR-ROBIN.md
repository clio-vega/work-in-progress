# Q76 — the commutator quotient, closed. And a priority correction on Q75.

**4 September 2026 · prove session · `q76/2026-09-04-Q76-commutator-quotient.pdf`**

## The short version

Yesterday's paper proved that $(1+t)$ divides every entry of $[R_e(t),R_{e'}(t)]$ and left two
things open: whether that is *sharp*, and what the quotient *is*. Both are now proved, by one
computation. And a bounded prior-art phase settled the question yesterday's paper flagged and
left open — **against me**. Details below, in that order of importance to you.

## 1. What is proved

Move to the Maya diagram, where adding an $e$-ribbon is a bead hopping $b \mapsto b+e$ with
weight $t^{\#\text{beads jumped}}$. Then $[R_e,R_{e'}]$ is a signed sum over **two-hop paths**,
and there are exactly three kinds of path. Classifying them gives every entry:

- If $\mu/\lambda$ is an $(e+e')$-ribbon of height $h$: the entry is
  $(\epsilon_e - \epsilon_{e'})\,t^{h-1}(1+t)$, where $\epsilon_j = 1$ if the ribbon turns
  *upward* between its $j$-th and $(j{+}1)$-st cells (read from the bottom-left end). So it is
  nonzero exactly when the ribbon turns up at exactly one of its two cut points.
- If two beads move: the entry is $\pm t^{H-1}(1-t^2)$ when the two hops **cross**, and $0$
  otherwise.
- Everything else: $0$.

So every entry of $Q = [R_e,R_{e'}]/(1+t)$ is $0$, $\pm t^a$, or $\pm t^a(1-t)$ — at most two
terms, coefficients in $\{0,\pm1\}$.

**Sharpness**, which was the open half of the programme's rigidity claim: two witness families,
uniform in $2\le e<e'$, both from $\lambda = \varnothing$:
$$\mu=(e',1^e)\ \rightsquigarrow\ t^{e-1}(1+t), \qquad \mu=(e',e)\ \rightsquigarrow\ 1-t^2 .$$
The first gives $Q(-1)=(-1)^{e-1}\neq0$; the second gives a $Q$-entry $1-t$, not divisible by
$t$. Together the gcd of the entries of $[R_e,R_{e'}]$ is **exactly $t+1$** — not observed on
three pairs, proved for all of them. In fact something stronger holds: *every* nonzero entry is
divisible by $(1+t)$ exactly once.

**The pretty corollary.** Because a bead hop $b\mapsto b+e$ produces a ribbon occupying exactly
the diagonals $(b,b+e]$, the two-bead criterion is geometric:

> Two ribbon additions commute, *as graded operators*, unless the intervals of diagonals they
> occupy properly cross.

Disjoint intervals commute — expected. **Nested** intervals also commute, which I did not
expect: a small ribbon sitting entirely inside the diagonal span of a large one is invisible to
it. At $e=e'$ this specialises to the criterion $|b-c|\ge e$ that sits, answered and
uncited, on MathOverflow 292312.

Verification: 238594/238594 entries against brute force, $|\lambda|\le8$, all $2\le e<e'\le7$.
The nonzero split (8408 crossing pairs + 2952 ribbons) reproduces counts computed earlier the
same day by a completely different route. Six negative controls, each with its variation named
before it was run; all fire. The one I would trust is the height-convention control — perturbing
$h \to h+1$ breaks the formula on 761/6665 entries, so the check is not blind to the grading,
which is the part of the object that is mine.

## 2. The correction, which you should read before the mathematics

Yesterday's Theorem A — the Pieri rule $\langle s_S, f_e(t)\rangle = t^{h}(1+t)^{c-1}$ — is
**classical**. It is the $q$-Murnaghan–Nakayama rule for Iwahori–Hecke algebra characters,
transported by the involution $\omega$ and a global sign.

I read the statement at source myself (Jing–Liu `2310.15730` §4.2, e-print `mn.tex`, lines 626 /
728 / 744) and then verified the dictionary in my own engine on two routes that share no code:
generating functions ($e\le5$) and the weight formula (541/541 skew shapes, with a negative
control firing on 327/541). It is not a shape match; it is the same theorem.

**So: yesterday's paper is not a `publishable-result` candidate on Theorem A's novelty, and I
have not pushed it there.** The brief anticipated the opposite outcome and told me to say so
loudly if the search came back "not classical". It came back classical. That is the seventh time
in nine days that one of my objects turned out to be standard, and it happened the day after I
wrote the paper claiming it — the value of yesterday's session is now entirely in
Corollary "multiplication iff $t=-1$", which is a statement about $R_e(t)$, and in the new proof
of Murnaghan–Nakayama by the two-splittings trick.

Two near-misses were checked and excluded, so nobody re-walks them: Okada `1904.03386` Cor 6.8
(= Morris 1964) and Fayers `2003.07713` Prop 3.6 both live in the shifted / Schur $P$–$Q$ world
with weight $2^{\#\text{components}}$ and no $t$. Fayers' unpublished Hall–Littlewood version,
which I had flagged as a lead, concerns *that* rule, not mine. Dead lead, struck.

**What is honestly open on priority:** today's Theorem 8 (the commutator closed form) is
**unsearched**. I spent the capped prior-art budget on Theorem A. I am not claiming it is new.

## 3. Two things worth your eye

- **The proof needed no involution.** The brief suggested looking for a sign-reversing involution
  on intermediate shapes. What actually worked is the same move as yesterday: a small exact
  count. In the ribbon case, exactly two of four candidate paths are ever valid, and the four
  indicator cases collapse to $(\alpha-\beta)t^{N-1}(1+t)$ in one line. Twice now the
  two-element count has beaten the involution.

- **A tooling correction.** The canonical `trustcheck` invocation recorded in my notes is
  incomplete, and the incomplete form *passes vacuously*: without `--root memory` you get 232
  spurious "read file missing" lines, and without an explicit `--sources` the index silently
  loads as empty and every source check is skipped while the run reports `OK`. The invocation
  that actually checks anything — I confirmed by planting a bad source id and watching it fire —
  is
  ```
  python3 code/trustcheck.py --deployment code/clio.json --root memory \
      --sources memory/reading/sources.json validate proofs/registry/<name>.json --files-dir proofs
  ```
  A validator that says OK because it loaded nothing is the same failure as a verification whose
  passing set is everything.

## 4. Gaps, stated precisely

1. Prior art for today's Theorem 8: **unsearched**.
2. The onward attribution of the $q$-MN rule (Ram 1991, Halverson 1995, Halverson–Ram 1995) is a
   citation chain read *inside* Jing–Liu. None of the three is opened; none is on arXiv. The word
   "classical" rests on that chain.
3. The Hall–Littlewood identification $f_e(t)=P_{(e)}(x;-t)$ still rests on two Macdonald III
   displays quoted from memory. Jing–Liu's prose corroborates that $\tilde h_r$ is a one-row
   Hall–Littlewood function, but does not supply those two displays.
4. I have not characterised, intrinsically in terms of the skew shape $\mu/\lambda$ alone, which
   shapes arise in the two-bead case. For the ribbon case this is done.
