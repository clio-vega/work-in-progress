# NL_c proved for all c — and c=3 Gap 1 closed as a corollary

**2026-06-14 prove session. Win condition met in full.**

## Headline

The general-$c$ Number Lemma is **proved**, with an explicit, sharp constant:

> For $c\ge1$, even $F\ge2$, $2c\le j\le F+2c-1$:
> $$v_2\binom{F+2c-1}{j} + v_2(j^{(2c)}) \ge v_2(F) + \beta(c), \qquad \beta(c)=(c-1)+v_2((c-1)!)=2(c-1)-s_2(c-1).$$

$\beta(1)=0,\ \beta(2)=1,\ \beta(3)=3,\ \beta(4)=4,\dots$ — recovers the hook/two-row $R\ge0$ ($c=1$)
and the Lean-checked $c=2$ Number Lemma. The constant is sharp (equality attained).

This is the single falling-factorial tip bound that closes the **interior** of the three-row
even-$|J^*|$ family for *every* $c$ simultaneously.

## The proof is short

Three moves, exactly the $c=2$ proof lifted:

1. **Subset identity** $\binom{F+2c-1}{j}\binom{j}{2c}=\binom{F+2c-1}{2c}\binom{F-1}{j-2c}$ →
   $v_2\binom{F+2c-1}{j}\ge v_2\binom{F+2c-1}{2c}-v_2\binom{j}{2c}$.
2. $j^{(2c)}=(2c)!\binom{j}{2c}$ → the $v_2\binom{j}{2c}$ **cancels**, leaving the $j$-independent
   bound $v_2\binom{F+2c-1}{2c}+v_2((2c)!)$.
3. **Anchor identity** (the one new ingredient, and it's clean): the numerator of $\binom{F+2c-1}{2c}$
   is $2c$ consecutive integers from $F$, so
   $$v_2\binom{F+2c-1}{2c}+v_2((2c)!)=\sum_{i=0}^{2c-1}v_2(F+i)=v_2(F)+\sum_{k=1}^{c-1}v_2(F+2k)\ \ (F\text{ even}).$$
   Writing $F=2G$: the tail $=\;(c-1)+v_2\binom{G+c-1}{c-1}+v_2((c-1)!)\ \ge\ \beta(c)$, since
   $v_2\binom{G+c-1}{c-1}\ge0$. Sharpness: that binomial is odd for $G=2^t\ge c$.

**The broken assumption you flagged was exactly right.** $\binom{F+2c-1}{2c}$ does *not* behave like a
fixed shift in $c$ — but the clean object is the *combination* with $(2c)!$, which is an exact sum of
valuations over consecutive integers. Once you see that, $\beta(c)$ is a one-line minimisation.

## Bonus: c=3 Gap 1 (L3″-A) fully closed

The $a$-even Compensation Lemma A,
$v_2\binom{b+3}{j}+v_2 Q_3(a,b,j)\ge v_2(b+3)+1$, now follows. Split
$\binom{b+3}{j}Q_3 = T_1 - T_2$ along $Q_3=(a-1)(b-2)H - 720C(j,6)$:

- **Tip $T_2$:** subset identity → $T_2=(b+3)^{(6)}\binom{b-3}{j-6}$; the five consecutive integers
  $b-2,\dots,b+2$ give $v_2\ge3$, so $v_2 T_2\ge v_2(b+3)+3$.
- **Heavy $T_1$:** expand $\binom{b+3}{j}H$ term-by-term with $\binom{b+3}{j}j^{(k)}=(b+3)^{(k)}\binom{b+3-k}{j-k}$;
  **every** one of the 5 terms carries $b+3$ plus an extra factor 2 (from a coefficient 6, or from
  $a+4$/$ab+a+2b$ even since $a$ is even, or from consecutive integers), so $v_2 T_1\ge v_2(b+3)+1$.

$v_2(T_1-T_2)\ge\min\ge v_2(b+3)+1$. Unconditional, all $b$. Closes Gap 1 of the $c=3$ write-up.

## What's still open

**Gap 2 (Compensation Lemma B, $a$ odd):** $\tilde\Delta(j)=j+3-2s_2(j)+2U(j)\ge0$, $4\le j\le b$. This
is the genuine **two-generator** inequality — it couples $s_2(j)$ with the full Prop-2 valuation, and is
*not* a pure tip bound (the per-$v_2(j)$ minima of $U$ are the irregular $\{-6,-5,-5,-4,-5,\dots\}$).
NL$_3$ controls the tip inside $U$ but not the $s_2(j)$-coupled superposition. That, plus the tie
classification S2 ($|J^*|=4$ iff $a\equiv1,b\equiv2\bmod4$), is the $e_2\bmod2$ wall proper — next
target.

## Files

- Proof: `projects/proofs/2026-06-14-numberlemma-general-c.md`
- Scripts: `projects/proofs/2026-06-14-numberlemma-general-c-code/` (all 0 failures)
- Suggested next: Lean follow-on (NL$_3$ / general NL$_c$, reusing `vz_choose_ge`).
