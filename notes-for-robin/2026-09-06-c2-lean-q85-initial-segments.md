# Q85's Lean gap: the order half is closed, and the gap had mis-stated itself

*LEAN session, 2026-09-06 cycle 2.*

## What landed

The Q85 registry has carried a node, `Q85-prefix-sign-sum-lean-general-gap`, saying that
`prop:N` (the prefix sign sum, `2026-09-05-Q85-literal-gcd.tex`) is machine-checked only at
$k=3,4,5$ by `decide`, and that the whole obstruction to general $k$ was **one** lemma:

> for $T\subseteq\{0,\dots,k-1\}$ and $r\le|T|$: $\big((\mathrm{ascList}\ k\ T).\mathrm{take}\ r\big).\mathrm{toFinset}=S$
> iff $S\subseteq T$, $|S|=r$, and every element of $S$ is below every element of $T\setminus S$.

That lemma is now proved, sorry-free, at general $k$, as
`TworowD4Kernel.take_ascList_toFinset` —
[PrefixSignSum.lean](https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/PrefixSignSum.lean),
`tworow-d4-kernel@43a859e`. Six declarations, zero sorries, `#print axioms` returns exactly
`[propext, Classical.choice, Quot.sound]` on all six. `lake build` (2978 jobs) and `lake test`
both exit 0.

## The part I think is worth your attention

**The gap statement was wrong, in a way that has a general shape.**

$\rho_T = \mathrm{ascList}\ ++\ k::(\mathrm{ascList}\ D).\mathrm{reverse}$. The paper proof's second
case ($k\in\bar S$, regime $r>m+1$) reads the prefix off the **descending tail** — it picks out the
$r-m-1$ *largest* elements of $D$. `take_ascList_toFinset` says nothing whatsoever about that. So I
proved the mirror, `take_reverse_ascList_toFinset`, as well.

The two cases *are* symmetric, and that is exactly how the error got in: whoever wrote the gap
statement (me, yesterday) read the first case, saw the second was symmetric, and wrote down one
lemma. But symmetry between two cases is a reason to prove **two** lemmas, not a reason to prove
one and wave at the other. A gap statement produced this way undercounts by precisely the mirror —
which is the most invisible possible error, because the mirror is the thing you're confident about.

## The remaining gap, narrower

General `prop:N` is still not formalised, and I have left the node `unclassified` rather than
inflate it. But what remains is now of a different kind — none of it is order theory:

1. Splitting $\big((\rho\ k\ T).\mathrm{take}\ r\big).\mathrm{toFinset}$ across the append in the
   three regimes $r\le m$, $r=m+1$, $r>m+1$, via `List.take_append_eq_append_take`. The two lemmas
   above then identify each piece. No new mathematics.
2. **Two sum reindexings — this is where the work actually is.** Case $k\notin\bar S$ along
   $T=\bar S\sqcup B$ with $B\subseteq(\max\bar S,k-1]$; case $k\in\bar S$ along
   $T=(\bar S_0\setminus Y)\cup Y'$ with $Y'\subsetneq Y$. Both `Finset.sum_nbij'`-shaped.
3. The alternating sum $\sum_{B\subseteq C}(-1)^{|B|}=0$ — **free**, it is already in Mathlib as
   `Finset.sum_powerset_neg_one_pow_card_of_nonempty`.

A new sibling node `Q85-prefix-sign-sum-lean-initial-segments` is `lean-verified` on
`take_ascList_toFinset`. `registry_validate.py --proofs-dir /home/clio/projects` is clean.

Session note:
[2026-09-06-c2-lean-prefix-initial-segments.md](https://github.com/clio-vega/proofs/blob/main/2026-09-06-c2-lean-prefix-initial-segments.md)
(`proofs@5a73faa`). CI run `34060225239`.

## One small thing

The proof needed no induction on $r$, which is what the session brief expected. The existence half
falls out of `List.pairwise_append` applied to $L = \mathrm{take}\ ++\ \mathrm{drop}$: an element of
$T$ outside the prefix is *in the suffix*, and sortedness compares them directly. The uniqueness
half has no lists in it at all. Splitting a characterisation into "the object has the property" and
"the property determines the object" put the list reasoning entirely in the first half and left the
second as three lines of `Finset` order combinatorics. I would not have found that by attacking the
iff head-on.
