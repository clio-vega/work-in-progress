# `prop:N` is formalised at general $k$ — Q85's last Lean gap is closed

**`tworow-d4-kernel@27a59f1`**, CI run `34095463557`.
File: https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/PrefixSignSum.lean

```lean
theorem prefixSignSum_eq (hk : 2 ≤ k) (hS : S ⊆ Icc 1 k) (hne : S.Nonempty) :
    prefixSignSum k S = prefixSignSumRHS k S
```

Zero sorries in the file. `lake build` (2978 jobs) and `lake test` both exit 0. `#print axioms`
is exactly `[propext, Classical.choice, Quot.sound]` on all fourteen new declarations — no
`native_decide`.

The definitions `prefixSignSum` / `prefixSignSumRHS` are unchanged from the `decide`-at-$k=3,4,5$
version of two days ago, so this proves the paper's statement rather than a restatement. Those
three theorems are now corollaries; I kept them as independent kernel-level cross-checks that the
two definitions agree with each other.

## The one thing worth your time

The brief (mine, from yesterday) said the session's work was **two** `Finset.sum_nbij'`
reindexings, one per case of `prop:N`. There is **one** lemma, used twice:

```lean
theorem sum_interval_sign (A Y U : Finset ℕ) (hAY : Disjoint A Y) (hAU : A ⊆ U) (hYU : Y ⊆ U) :
    ∑ T ∈ U.powerset, (if A ⊆ T ∧ T ⊆ A ∪ Y then ((-1 : ℤ)) ^ T.card else 0)
      = (-1) ^ A.card * (if Y = ∅ then 1 else 0)
```

Case $k\notin\bar S$ is $A=\bar S$, $Y=(\max\bar S,k-1]$; case $k\in\bar S$ is
$A=\bar S_0\setminus Y$, $Y=$ `topBlock`. It took two iterations to prove.

And **inside** the case $k\in\bar S$, the two regimes the paper separates are one object. The
write-up splits $r=m+1$ (a single term $T=\bar S_0$ — "this is one term and it always occurs")
from $r>m+1$ (an alternating sum over $T\subsetneq\bar S_0$), then adds the contributions. But
the admissible $T$ are exactly the interval $\bar S_0\setminus Y\subseteq T\subseteq\bar S_0$,
and $T=\bar S_0$ is its **top element**. The separate term and the addition are artefacts of the
split. The paper isn't wrong — the two computations agree — but if it's ever rewritten, that
paragraph collapses to one sentence.

I note this partly against myself: yesterday's lesson was that a gap stated as one lemma was
really two, and it would have been easy to read that as "always expect more work than stated."
The actual generalisation is that the prose's regime decomposition needn't match the proof's,
and it can be *coarser* as well as finer.

## One thing I'd like checked

I replaced the paper's $Y=(m^*,k-1]$, $m^*:=\max([k-1]\setminus\bar S_0)$ with the convention
$m^*:=0$ when that set is empty, by

```lean
def topBlock (k : ℕ) (S₀ : Finset ℕ) : Finset ℕ := (Icc 1 (k - 1)).filter (fun x => Icc x (k - 1) ⊆ S₀)
```

Same set, no empty-case convention, no nonemptiness hypothesis, and — the reason I had to change
it — decidable as written, where the bounded-$\forall$ transcription was not. Since that
definition is *mine* and not yours, I gave it its own warrant rather than trusting the
equivalence: the tests transcribe your $Y$ literally as `topBlockPaper` (with `Finset.max`
and `.getD 0`) and assert the two agree on **every** $\bar S_0$ for $k=6,7$, plus both extremes
of the convention at $k=2$. Negative control: moving `topBlockPaper`'s upper endpoint
$k-1\to k-2$ makes the check fail, and `topBlock 6` takes at least three distinct values across
inputs, so this isn't a constant matching a constant.

If you disagree that those two sets are equal, that's the place to look.

## Tooling, in case it bites you

`python3 code/registry_validate.py <registry>` — the bare form — reports **153 `file not found`
violations for files that exist.** `--proofs-dir` defaults to the *parent of the registry's
directory* (`projects/proofs`) while the `file` fields are repo-root-relative (`proofs/…`), so
every path is doubled. Correct invocation:

```
python3 code/registry_validate.py proofs/registry/<name>.json --proofs-dir /home/clio/projects
```

which returns `OK`. This is the same defect `trustcheck` had (`--files-dir /home/clio/projects`).
Two tools now, same shape: a bare default isn't safe when the paths in the data are relative to
a different root.

— Clio
