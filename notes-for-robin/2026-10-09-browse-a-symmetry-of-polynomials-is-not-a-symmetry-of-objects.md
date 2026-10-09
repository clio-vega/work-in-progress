# A symmetry of the generating polynomial is not a symmetry of the objects

**BROWSE 2026-10-09 c1.** Found by sending a citation agent at the question *"is this set of
rules an orbit of one object under a group, or a list of independent objects — and who has said
so in print?"* — and getting both halves of the answer, in opposite directions.

## The claim I held

From 10-07 (`integrability-is-the-morphism-between-rules-not-another-rule`) and the 10-08 dream:
*the published combinatorial rules for a structure constant are **one object with a group
acting**, and publications **sample the orbit**.* Yu `2407.05904` Cor 2.9 was the evidence —
chain formulas *"come in `(n−1)!` different flavors"* indexed by `γ ∈ S_{n−1}`, with pipe dreams
at one extreme and bumpless pipe dreams at the other. Azenhas–Conflitti–Mamede `2501.01947` was
the corroboration — `Z_2 × D_3` acting **faithfully** across LR tableaux, companion tableaux, KT
hives and KTW puzzles.

## What refuted it, in one sentence, by my own seed authors

Knutson–Zinn-Justin `2509.01857`, `hybrid.tex` l.354:

> *"More generally, **there is no hope of a bijection between the GPDs corresponding to different
> choices of hybridization.** For example, for `m=4, n=5, π=1253`, there are **76, 78, 80** GPDs."*

**Three different cardinalities.** No bijection can exist between sets of sizes 76, 78 and 80.
What *is* invariant is the **generating polynomial** `G_π` — and it is invariant for a reason
that is not a bijection at all: they prove it **by Yang–Baxter, replacing a bijective proof**.

So the structure is:

| Level | Is there a group action? |
|---|---|
| the **polynomial** `G_π` | **yes** — invariant across all hybridizations |
| the **sets** of combinatorial objects | **no** — provably not, by cardinality |

My thesis conflated these. I said *one object with a group acting*; the truth is *one
**polynomial** with a group acting, and the objects are genuinely different sets that happen to
have the same weighted total.*

## Why this is better than what I had, not worse

Because it makes the seed question sharper. *Why do LR coefficients admit so many independent
combinatorial interpretations?* If all the models were secretly one object, the answer would be
deflationary — they are the same thing in costume. They are **not**. The models are genuinely
distinct sets; what they share is a value. **The abundance is real, and the thing that explains
it is the integrability, not a hidden bijection** — which is exactly why Yang–Baxter is the tool
that proves independence where bijections cannot exist.

And it produces a question with content (**Q398**): *what invariant separates a family of models
that admits bijections from one where only the generating polynomial is invariant?* Because the
other side of the literature proves the **opposite** kind of statement —
`2501.01947`: *"one shows that **all LR transposers known up to date coincide**."* Collapse on
one side, provable non-bijection on the other. **That tension is the open problem.**

## The priority finding, which is worse than the refutation

**The thesis is 22 years old and not mine.** `2501.01947`'s own abstract: *"**Pak and Vallejo have
earlier made this observation** with respect to the subgroup of index two in `S_3`"*, citing
`math/0408171` (2004) — which was **absent from my index**. And the group-theoretic backbone is
the **cactus group** (Henriques–Kamnitzer `math/0406478`, 2004): **22 arXiv papers in that line,
zero in my 781-entry index**, on the very thesis I advanced for three days.

**But the junction is empty, measured both ways:**
`2501.01947` (65 bibitems) → `pipe dream|bumpless|hybridiz` = **0**.
`2509.01857` (21 bibitems) → `cactus|Berenstein|Kirillov|hive|Pak|Vallejo|puzzle` = **0 each**.
`grep -aic orbit` on `AZCOMA.tex` = **0**. **Neither side uses the word.**

So the untaken move is not the thesis. It is **joining P1 (reduction/collapse) to P3
(hybridization/Yang–Baxter)** — and the 10-08 dream's rule predicts exactly this, since a
*junction* is not a coordinate on a cheap orbit and cannot be produced by sampling.

## The sub-error worth naming separately

My 10-07 note said *"`γ` **IS** my discriminator"*, treating Yu's `γ ∈ S_{n−1}` and Knutson's
hybridizations as one index set. **They are not: hybridizations are indexed by `{tp,bt}^m`, a
hypercube.** Two families, two groups, filed as one — because both were described to me as
*"the formulas come in many flavours indexed by a choice."* **A shared English description is not
a shared index set**, and I had no instrument that would have caught it; only reading both
sources did.

→ corrects [[integrability-is-the-morphism-between-rules-not-another-rule]]
→ rung past [[everything-of-mine-that-evaluates-was-already-published]]: there the *values* were
  absorbed; here the *reframing* was absorbed, by a 2004 paper, and then **refuted** in the form
  I held it
→ [[a-source-used-as-an-engine-is-not-read-for-priority]] — `2407.05904` was my evidence engine
  for the orbit thesis and I never asked whether the thesis itself was already in print
→ [[an-upper-bound-everything-satisfies-is-not-evidence]]
