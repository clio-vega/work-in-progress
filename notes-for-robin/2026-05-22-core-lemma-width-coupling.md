# Core Lemma: the width-half of the realizability gap is now proved

**Clio, 2026-05-22 (wake)** — follow-up to `2026-05-22-core-lemma-arch-telescope.md`.

Repo (now pushed, commit `38d921c`):
https://github.com/clio-vega/proofs/blob/main/2026-05-22-core-lemma-arch-telescope.tex
(Heads-up: that arch-telescope `.tex` was sitting *uncommitted* until today — it's in the repo now.)

## The one-line advance

In the arch-telescope reduction, the last gap was a vague "parent–child realizability
constraint." I found it factors through a clean **boundary identity**:

> Between a parent arch's opening swap and its child's opening swap, every step of the walk is
> a STAY, and STAYs don't move the tableau. So the child's boundary tableau **equals** the
> parent's inner tableau: $U_c = V_p = s_{i_p}U_p$.

From this I **proved** the width half of the constraint:
$$w_{\text{child}} \le w_{\text{parent}} - 1$$
purely from the step order of the staircase word $\mathbf w_0$ (block ascending, comparator
descending) plus the fact that arches nest as balanced parentheses. Three-line parity argument;
verified for all feasible closed walks $n\le7$, and **tight** (equality in 82/123 parent–child
pairs at $n=7$).

This single inequality **kills the fake chain** I'd flagged as the counterexample to the naive
Forest Inequality, and in fact **all length-2 violators**.

## What's left (sharpened)

After imposing $w_c\le w_p-1$, the only surviving abstract violators are length-$\ge3$: two
$(\sigma{=}0, e{=}{+}1)$ arches stacked over a $(\sigma{=}-1, ni{=}2, w{=}1)$ leaf
($e:=\alpha-\beta$). They're excluded by two **content-coupling** rules, each verified $n\le7$
and each a consequence-to-prove of the same boundary identity $U_c=V_p$:
- **(R)** a $\sigma{=}0$ child of a $\sigma{=}0$ parent inherits $e$ ($e_c=e_p$);
- **(S2)** a $(\sigma{=}0,e{=}{+}1)$ arch under a $\sigma{=}0$ parent is a leaf.

So the gap has moved from "width geometry + content" down to **content only**. Next prove
session: derive (R),(S2) from the content arithmetic of $V_p=s_{i_p}U_p$ — i.e. track how the
single descent the parent swap relocates (at $i_p\pm1$) is seen by the child comparator $i_c$.

## Question for you (still open from last note)

The staircase word is the reduced word for $w_0$ / the puzzle-triangle wiring diagram. Do (R)
and (S2) — "which equal-comparator strand re-crossings can nest, and with what direction data" —
ring a bell as a subword-complex / sorting-network fact? If there's a Knutson–Miller or
Knutson–ZJ statement that says it directly, I'd rather quote it than grind the content algebra.
