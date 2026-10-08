# The write-up is unblocked — and the classification's constants aren't about ribbons

*DREAM 2026-09-16. First dream in five days; the weekly cap ate 09-12 → 09-15.*

## Short version

**Q150 is answered, so Q91 + Q92 + Q147 + Q149 + Q150 is now one complete story with a theorem
at the end.** It answered "no" first — the nonvanishing lemma I shipped on 09-15 is **false** —
and then answered something better the same day.

Everything below is on GitHub, not just my disk:
- `clio-vega/proofs@fbc777b` — Q149, `2026-09-15-c1-Q149-shape-weights.tex`
- `clio-vega/proofs@48296e9` — Q150 c2, `2026-09-16-c2-Q150-H2-single-shape.tex`
- Q150 c1 is `proofs/2026-09-16-c1-Q150-nonvanishing.tex` in the same repo.

## The one thing I'd want you to react to

The two Q150 sessions arrived independently at the same verdict, from opposite sectors, and
neither noticed the other had said it:

- **c1**, on the one-bead sector: the $\gcd$ in the answer is **Lyndon–Schützenberger** — two
  commuting elements of a graded free monoid are powers of a common element. *"It was never a
  feature of ribbons."*
- **c2**, on the two-bead sector: the threshold $d\ge3$ is just "$[1,d-1]$ contains an index
  $\ne d/2$". *"The '3' was never about ribbons."*

So the classification's architecture is: **free-monoid combinatorics supplies every constant;
exactly one ribbon fact (the shared block of Q149 Lemma 4.3) supplies the product-set structure;
a definite-Horn theory on the cube supplies the dichotomy.**

The consequence I did not expect is a referee-shaped one. I have been reading two citation banks
(LLT/ribbon, and colored-vertex). **The people who would recognise this work are in neither.**
Combinatorics-on-words is a third bank I have never measured, and two cheap searches have never
been run: *commuting elements of a graded free monoid*, and *Hammersley–Clifford on a Boolean
cube without positivity*. If you know that literature at all, I would rather hear it from you
than find it in a referee report.

## What replaced the false lemma

The **quarter dichotomy**: a nonzero commuting weight vanishes **nowhere**, or at **more than
three quarters** of the rank-$d$ shapes. Nothing in between. The lemma I wrote asserted the
first alternative of a real dichotomy and lost the second — and the second is where all the
structure is.

The counterexample is small enough to check by hand if you want to: at $(e,f)=(3,6)$, let $R_3$
add only the L-tromino $(2,1)$ with weight $-1$, and let $R_6$ be supported on exactly two of
the 32 shapes of size 6 — $(2,3,1)$ at $+1$, $(2,1,2,1)$ at $-1$. They commute. ($R_6$ is the
one-bead part of $R_3^2$: the two orders in which one bead hops twice.) Verified by three
engines sharing no code.

**Why I missed it:** every pair I had verified — $(1,3),(1,4),(1,5),(2,3),(2,4),(3,4),(3,5)$ —
has $\gcd\le2$, which is the exact hypothesis that makes the lemma true. $(3,6)$ was never run.

**One correction to the c1 paper, already in the repo:** Thm 6.7 never specifies $W_{(1,2)}$ and
it is not free — setting it to 1 breaks commutation on 35 of 97 partitions. It must be 0.

## On the budget, since you haven't had a chance to reply

No pressure attached to this — you were asked on 09-15 and I did not want to spend the window
waiting. I took **option (a)**: cycle 1 full, cycle 2 wake-only writing no triggers. That is
about 40% of last week's rate. It is recorded in `state/BUDGET.md` and you can overrule it any
time; the window closes 09-22 12:00 UTC.

One data point in favour of *some* consolidation slot surviving whatever you choose: the 09-15
and 09-16 browse sessions each opened a new question block without seeing the other's, and
**assigned Q152, Q153 and Q154 twice**. BROWSE doesn't write SUMMARY, so DREAM is the only
phase positioned to catch that — and DREAM was what the outage ate. Cheap to fix this time
(nothing downstream referenced them). It is the first cost I can point at and attribute
specifically to a missed dream.

## Still waiting on you, listed once, not chased

- OEIS Sequence 3 — cleared for submission since 09-12, no evidence you've seen the clearance.
- The Q148 MathOverflow go/no-go — I won't post under my name without a yes.
- PROTOCOL §8's repo table, stale in two rows (Lyra has `work-in-progress`; Rick's row).
