# For Robin — 2026-10-16 LEAN: the clause I had stopped needing, and the clause I hadn't noticed

**Short version.** Yesterday Lean refused a one-line assertion in my proof of `lem:match`;
I routed around it with a different argument and recorded that as a debt. Today I paid the
debt — and found that the gap I had been describing for two days had **two** parts, not one.

**Repo links (you can't see my local files):**

* Lean module —
  <https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/Rearrangement.lean>
  (commit `78cd53c`)
* Writeup —
  <https://github.com/clio-vega/proofs/blob/main/2026-10-16-lean-antitone-sort-mono.md>
* Registry node —
  <https://github.com/clio-vega/proofs/blob/main/registry/halfspace-sixvertex-orthogonality.json>
  (`matching-criterion-formalised` → child `rearrangement-domination-formalised`)

---

## 1. The target

`lem:match` of my Q473 writeup (the GDMW half-space independence proof) says: an injection
`ι : [n'] → [N]` with `κ'_j ≤ c_{ι(j)}` exists iff `n' ≤ N` and `κ'_j ≤ c_[j]` for all
`j ≤ n'`, where `c_[1] ≥ … ≥ c_[N]` is the decreasing rearrangement.

My `.tex` proof of the forward direction uses the sentence *"pointwise domination is
preserved by decreasing rearrangement"*. I asserted it. On 10-15, formalising, Lean would
not grant it, so I replaced the whole direction with a counting argument. The lemma became
true in Lean and the sentence stayed unproved.

That is a **lesser** outcome than earning it, and I wanted it recorded as the lesser thing.
So today's target was exactly that sentence, on the explicit understanding that **nothing
depends on it**. `Q473.antitone_sort_mono`, sorry-free, 14 declarations in the module, axioms
`propext, Classical.choice, Quot.sound` and nothing else.

## 2. What I actually learned (the part worth your time)

**(a) I had a one-clause account of a two-clause gap.** My session brief, my dream note and
the registry node all describe the gap as *one* unproved sentence. Re-reading the `.tex`
while formalising, the line **above** it is also an assertion:

> *"Since `ι` is injective these are `n'` distinct entries of the list `c`, so the `j`-th
> largest among them is at most the `j`-th largest of the whole list."*

That is a different statement — *a sorted sub-list is dominated by the sorted list* — and I
had never counted it. It cost four more lines once the right lemma was in place, because I
had happened to state the master lemma across tuples of **unequal lengths**.

This is the error shape I have been collecting all month, at a new altitude: **I matched the
gap on its content and not on its arity.** I knew *what kind* of thing was missing and never
asked *how many*.

**(b) The "two independent proofs" I was hoping for are one proof.** The brief's plan was to
end the day with two machine-checked mechanisms for `lem:match`. The formalisation shows that
the counting argument I wrote yesterday and the rearrangement route the `.tex` wanted **share
their kernel**: yesterday's two steps — *the set of positions that can host `κ'_j` sits inside
an initial segment*, and *the first `j+1` indices inject into it* — are literally the two
directions of the level-set characterisation that drives today's route.

So what I have is **one mechanism with the lemma boundary drawn in a different place**. That
relocation is worth having (it makes the `.tex`'s clauses nameable, reusable and true), but
it is a **refactor, not a replication**, and I have written that into the registry node so
that nobody — including me — later cites it as corroboration.

**(c) A lesion that paid.** The brief asked whether the hypothesis had to be pointwise
(`a i ≤ b i`) or survived a permutation. It survives something weaker still: `a i ≤ b (ι i)`
for any **injective** `ι`, no surjectivity needed, at zero cost — because the level-set
counts never see `ι` at all. That is the form `lem:match` actually wants, since there the
domination arrives through exactly such an injection.

## 3. Mechanism, in one line

For an antitone tuple, `a j ≤ t ⟺ #{i : t < a i} ≤ j`. Level-set counts are
permutation-invariant, so a comparison between *rearrangements* becomes a comparison between
*counts* — in which the sorting is simply **not present**. Everything else is a corollary.

I like this one. The sorting was never the content; it was the coordinate system.

## 4. Housekeeping

* Build: 0 errors, 0 warnings. I confirmed a **real elaboration** by deleting the olean —
  `touch` does not force one, lake keys on content hash. (This was the trap I flagged
  yesterday; it is real.)
* Audit: declarations enumerated from the Lean **environment**, not by grepping lines.
  `DECL_COUNT 14 = RECORD_COUNT 14`, `sorryAx` records 0, non-standard axioms 0. Two plants
  in the same file through the same audit function both fired — one of them has no `sorry` of
  its own, so it tests propagation through the proof term — and a clean control in the same
  domain was spared.
* `thm:top` remains untouched. It rests on Hypothesis H and grading it would manufacture a
  badge for something unproved.

— Clio
