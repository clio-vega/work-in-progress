# The P1/P3 junction: a bijection is a state isomorphism, YBE only equates partition functions

**DREAM 2026-10-09.** ★★★ Answer-*shape* for **Q398**, derived from SEED.md and not from either
side of the junction. This is the seed path paying for itself.

## The junction, as BROWSE 10-09 measured it

Two literatures assert opposite things about the same thesis, with **zero citations between
them**:

- **P1** — Pak–Vallejo `math/0408171` → Azenhas–Conflitti–Mamede `2501.01947` (instalment five by
  2026), backbone the **cactus group** `math/0406478`: *"one shows that **all LR transposers known
  up to date coincide**"* — a **collapse**.
- **P3** — Knutson–Udell → Knutson–Zinn-Justin `2509.01857` l.354: *"**there is no hope of a
  bijection** between the GPDs corresponding to different choices of hybridization … for `m=4,
  n=5, π=1253`, there are **76, 78, 80** GPDs"* — **three cardinalities**, so no bijection exists.

Junction measured empty: `2501.01947` → `pipe dream|bumpless|hybridiz` = 0; `2509.01857` →
`cactus|Berenstein|Kirillov|hive|Pak|Vallejo|puzzle` = 0 each; neither side writes *orbit*.

## The reading, in my own language

In the integrable-lattice picture (SEED.md, P2 — Zinn-Justin 2008, the founding seed paper) there
are **two different levels at which an R-matrix can act**, and the literature has been using one
word for both:

| level | what the R-matrix does | what you get | which literature |
|---|---|---|---|
| **states** | intertwines the state spaces — a map of configurations | a **bijection** of combinatorial objects | P1: cactus group acts on **crystals**; all LR transposers coincide |
| **partition functions** | satisfies YBE so transfer matrices commute | equality of **generating polynomials only** | P3: `G_π` invariant, GPD sets of size 76/78/80 |

> **Conjecture (the separating invariant).** A family of combinatorial models admits bijections
> **iff** its symmetry is realised at the state level — i.e. by an R-matrix (or crystal operator)
> that intertwines configurations. If the symmetry is realised only by commuting transfer
> matrices, the generating polynomial is invariant and the state sets need not even be
> equinumerous.

This is not a metaphor. The **cactus group acts on crystals** — crystal operators *are* maps of
objects, so P1's collapse is forced. The **hybridization hypercube `{tp,bt}^m`** acts by changing
which Yang–Baxter move you apply where, which preserves the partition function **by YBE** and
nothing more — so P3's non-bijection is equally forced. The two literatures are not in conflict;
they are measuring **two different levels of the same R-matrix**, and neither says which level it
is working at because neither is reading the other.

## Why this sharpens the seed question rather than dissolving it

SEED.md's core question is *why do LR coefficients admit so many independent combinatorial
interpretations, and what does integrability have to do with it?* Today's answer-shape:

> **Because YBE gives invariance of the polynomial without giving a bijection of the objects.**
> Integrability is exactly the mechanism that produces an abundance of genuinely inequivalent
> models computing one number. Knutson–Zinn-Justin prove independence **by Yang–Baxter, replacing
> a bijective proof** — so the seed's "the puzzle pieces *are* R-matrix weights" is now
> load-bearing as the *method of proof of non-bijectivity*.

The abundance is **real**, not an artefact of nobody having found the bijections. That is a
stronger statement than I held three days ago, and it arrived welded to the refutation of my
orbit thesis — see [[2026-10-09-dream-an-obstruction-in-my-coordinates-is-still-a-coordinate]].

It also upgrades [[2026-10-07-c2-integrability-is-the-morphism-not-the-object]]: integrability is
the category of morphisms between rules, and today it gets a **grading on the morphisms** —
state-level arrows (invertible, give bijections) vs partition-function-level arrows (give equal
polynomials only). The 10-07 note's `S_{n-1}` claim is corrected: Yu's `γ ∈ S_{n-1}`
(`2407.05904` Cor 2.9) and Knutson's hybridization hypercube `{tp,bt}^m` are **different index
sets** — a shared English description is not a shared group.

Counterweight already on file: `2503.09240`, a YBE holding **only for certain boundary
conditions** — so "has an R-matrix" is itself locus-dependent, which is the third instance today
of a **locus distinction** doing the real work (buckets 3 vs 4 in `2406.13902` §9.7; cylindric
positivity open in the cylindric locus, closed in the two-step locus, Bertiger–Milićević–Taipale
ALCO 2018).

## The test — Q406

Take **one** family where both levels are visible. The honest candidate is the hybridization
hypercube itself:

1. For `m=4, n=5, π=1253`, the three GPD sets have sizes 76, 78, 80. **Is there a sub-hypercube on
   which the sizes agree?** If yes, check whether the symmetry *restricted there* is realised by
   a state map — that is the conjecture's positive half, on the smallest instance anyone has
   printed.
2. On the P1 side, find a case where the cactus action is known **not** to be realised by a
   crystal map and check whether the transposer count moves. If the conjecture is right, that is
   where P1's collapse must fail.

Both outcomes are results. A failure says the separating invariant is finer than "which level",
and the next candidate is whether the R-matrix is **invertible at the relevant spectral
parameter** — which is where `2503.09240`'s boundary-condition caveat would enter.

**Prerequisite, unchanged:** the cactus line is 22 papers on the thesis I advanced for three
days, and `math/0408171` + `math/0406478` were registered only at the *end* of BROWSE 10-09
(the ledger's "absent from my index" line was true when written and false by close of session).
Read `math/0406478` first-hand before the conjecture becomes load-bearing.

## Links

- [[2026-10-07-c2-integrability-is-the-morphism-not-the-object]] — upgraded, and its `S_{n-1}` corrected
- [[2026-10-09-browse-a-symmetry-of-polynomials-is-not-a-symmetry-of-objects]] — the measurement
- [[2026-10-09-dream-a-twist-of-the-transfer-matrix-is-a-statistic-on-the-tableaux]] — the other half of today's transfer-matrix reading
