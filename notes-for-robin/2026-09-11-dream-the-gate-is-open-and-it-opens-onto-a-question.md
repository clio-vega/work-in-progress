# The novelty gate is cleared — and the thing that cleared it is the next question

*Clio, DREAM 2026-09-11 c1*

## The short version

The paper `2402.04500` (Fan–Guo–Su–Xiong, motivic Chern classes on Grassmannians) was the last
open novelty gate on my ribbon operator $R_e(t)$, and it had been blocking all writing for eleven
days. **It is cleared.** Read at LaTeX source this morning; their weight is not mine, on three
independent counts, and it fails at $e=1$ — the smallest case there is.

But the *reason* it isn't mine is the interesting part, and I didn't see it until the dream.

## The reason, and why it is a question rather than a relief

Their weight carries $t_{\mathtt h}$ — a parameter **indexed by** the ribbon's landing position.
Mine carries $t^{\mathrm{ht}-1}$ — one parameter **raised to** the height. That difference is the
whole separator.

That difference is also a named operation with a history. Novelli–Thibon (`2502.09072`, 2025) do
exactly it — $t^{1+\mathrm{leg}(u)} \to t_{1+\mathrm{leg}(u)}$ — and credit it to **Lascoux–Leclerc–Thibon,
LMP 35 (1995)**, one year before the ribbon paper. A third literature, "spin Hall–Littlewood",
does it to the lattice site, with one free parameter per site — and that family includes
**Gunna–Wheeler–Zinn-Justin `2504.19205`**, i.e. authors from my own seed shelf.

Three literatures. One operation. Three statistics: charge/leg, landing bead, lattice site.
**None of them cites the others** — zero spin-HL papers among the 265 distinct LLT citers, and
FGS's 50-item bibliography contains no LLT, no Hall–Littlewood, no Fock space at all.

**Nobody has run the operation on ribbon height.**

## The sting

My forcing theorem — different ribbon sizes cannot share an algebra unless $t=-1$ — **was proved
for a single $t$.** Multi-$t$ is strictly more freedom. So the object that the FGS refutation
points at, $R_e(t_1,\dots,t_e)$, is precisely the direction in which my own best theorem might
not survive. That's Q147, and it's now my top item.

I'd rather flag that than let it sit. It's the honest shape of the situation: my novelty is
smaller than I thought (Blasiak `1411.3646` shows the one-parameter weight was already LLT's
$\bar q$), what's left that is genuinely mine is the bracket **across** different $e$ — and that
is the same object as the obstruction. The claim and its obstruction are one thing.

## One concrete thing, if you want a pointer

My two banks — ribbon/LLT and integrable/vertex-model — are joined by **exactly one paper**:
Corteel–Gitlin–Keating–Meza `2012.02376`, *A Vertex Model for LLT Polynomials*. That is the
highest-value unread item in my container, and it's where the seed's own thesis (puzzle pieces
*are* R-matrix weights) says the bridge ought to be.

## Also worth knowing

**Rick's Day 184, from this morning's review** (already emailed him, cc you): the OEIS line is
cleared for submission — I re-derived $p_{21}$ digit-for-digit and the counterexamples are exactly
$k = 21,30,39,42,48,57$. Two defects found: his `log_concavity_bk.py` hard-codes a $b_k$ that is
wrong from $b_6$ on (six of ten rows are wrong numbers — **the conclusion is nonetheless correct**,
and I extended it to $k=58$), and a mod-3 lemma in the write-up is false at every multiple of 9.
Neither touches the submittable line.

One thing I could **not** do: the brief asked me to read a rational-function-degree argument that
is **404 in both of his repos**, verified against the API in-session. Two nodes stay
`peer-claimed` — that's a missing artifact, not a verdict on his mathematics.

And a structural flag: **neither of his repos is canonical.** `work-in-progress` has no registry
at all; `rick-research`'s `proofs/` stops two days earlier. His stated decision that
`work-in-progress` is canonical would orphan the registry and all of Day 184. Worth a word from
you, since it's a process question rather than a mathematical one.
