# Dream c2, 8 Sept — two things worth your attention, and one retraction of my own

## 1. The reading log is predicting the proof, and I keep meeting it going the wrong way

Twice now (09-06, and today) the evening browse session has produced the *shape* of the next
proof session's answer, hours in advance, from papers whose objects aren't mine — and both times
the prediction needed exactly one inversion to become true.

Today: WAKE said the separator for Q105 "must be first order at $t=-1$." BROWSE said that was one
rung too low, citing three papers whose degeneracies at $t=-1$ are *ladders* that grow
(Rozhkovskaya's pole of order $\lfloor(n-l)/2\rfloor$; Harnad–Orlov's vanishing even power sums;
Zabrocki's pole order jumping under $\partial_q$). PROVE then found that the ribbon side has **no**
ladder — order exactly 1, uniformly, 2588/2588 — while the vertex side has the full one. **The
ladder wasn't the obstacle; its one-sidedness was the answer.**

The process change I'm making: **read the browse log at the start of PROVE, not only write it at
the end of BROWSE.** Cheap, and it's now cost me two sessions of rediscovery.

## 2. The two citation banks are disjoint for a structural reason, and I can now name it

PROVE gave my ribbon operators a coordinate for the first time:
$\widetilde H_{a,b}(z)f=\sigma[Xz]f[X-\frac{a-b}{z}]$, whose contraction has its **zero at $a$** and
its **pole at $b$**. My $(1+t)$ eats only the pole; the published twist alphabet eats both.

BROWSE then read `0809.2392` (Zinn-Justin 2008, *LR coefficients and integrable tilings*) at source
— one of my own seed PDFs, which had been sitting at extraction level `abstract`. **It has no
deformation parameter at all.** No $q$, no $t$; one spectral parameter, integrable at every value.
§5.2 calls its Fock space presentational and then drops it.

So the disjointness of my two banks isn't sociology. **They're indexed by different data.** Bank A
distinguishes *values* of a deformation parameter (a pole, an order, a pairing locus); Bank B has
no parameter for anything to be distinguished in. No census of citers, at any size, could have
found an overlap — and the citation trail measured it independently and harder: Gunna–Wheeler–
Zinn-Justin `2504.19205` shares **zero of its 32 references** with each of seven Bank A lists, not
even Macdonald's book.

The practical reading: the bridge SEED.md asserts between its Fock path and its Integrable-Lattice
path is not in the literature. It has to be built. That's the room, and it's smaller and more
precisely located than I thought a week ago.

## 3. Retraction — last night's "7 bridges" was a database artifact

DREAM cycle 1 (this morning) crowned a finding: *"7 Shimozono–Zabrocki citers that do not cite Jing
1991 — that's where someone who reads both banks would be standing"*, and ranked a retrieval on it.

Recomputed tonight **with denominators**: 3 real non-citers, 3 duplicate records, 1 linguistics
false positive, 1 untestable null. **Lu–Ruan–Wang cites Jing** (33/33 references, checked at
source), so the ıHall line is *inside* Bank A and the rank-4 rationale is void. The count was doing
the argumentative work and I hadn't factored it.

One real bridge survives — Blasiak–Morse–Pun `2007.04952` — reaching the LLT/ribbon half of Bank B
and stopping short of the puzzle/vertex half.

Annotated in place, **not rewritten**, per the standing rule.

## 4. One tooling defect, small

`tracecheck.emit.init()` opens a new file per **process**, so a session run across separate shell
calls fragments into several trajectories with colliding event ids. Today's PROVE session became
four; I consolidated by hand into a 9-event file. The emitter should probably key on a session id.

## 5. A second tooling disagreement — and this one is a question, not a bug

`registry_validate.py` rejects `peer-claimed` as an invalid trust level (its enum is `computed,
dead-end, in-progress, lean-verified, peer-reviewed, proved, published, speculative,
unclassified`), while `trustcheck.py` passes clean on the same tree. All three nodes of
`rick-beta-prime-peer-claims.json` are flagged.

`peer-claimed` is a level I use deliberately — *asserted by a peer, no artifact of mine* — and it
is doing real work in my prose and in review verdicts. So the question isn't "fix the file": it's
**which of the two is authoritative**, the schema or my usage. I'd rather the schema gained the
level, but that's your call and I haven't touched code (dream session). The grades themselves are
unchanged and correct.

## Nothing is blocked on you.
