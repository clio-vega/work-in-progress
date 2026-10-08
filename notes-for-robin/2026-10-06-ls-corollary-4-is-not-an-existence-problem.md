# Lenart–Sottile's 2002 open problem is not an existence problem

**Clio, 2026-10-06 c1 (prove session).**
Paper: `https://github.com/clio-vega/proofs/blob/main/2026-10-06-ls-corollary-4-coupling.tex`
(PDF beside it; registry `proofs/registry/ls-corollary-4-coupling.json`.)

## The short version

Lenart–Sottile, *Skew Schubert polynomials* (`math/0202090`), Corollary 4 and the
remark after Theorem 2, say that

> `I_α(u,w) = Σ_v c^w_{u,v} · I_α(w₀v, w₀)`

and that a **type-preserving map** `Γ(u,w) → ⊔_v Γ(w₀v,w₀)` with fibre cardinality
`c^w_{u,v}` *"would give a combinatorial interpretation for `c^w_{u,v}`, and thus
solve the Littlewood-Richardson problem."* This was my seed question, printed as an
open problem in 2002, and today's brief told me to construct that map or prove it
obstructed.

**I constructed it, and the construction shows the target was mis-posed.**

**Theorem A.** Such a map exists for *every* `n` and *every* `u ≤ w`, and the number
of them is `∏_α I_α(u,w)! / ∏_v (c^w_{u,v}!)^{I_α(w₀v,w₀)}`. Existence is
**logically equivalent to Corollary 4**. Proof in one paragraph: type-preservation
splits the map over types; within a type the data is exactly a labelled set
partition with prescribed block sizes; such a partition exists iff the sizes sum
correctly, which *is* Corollary 4, and then it is counted by a multinomial
coefficient.

The structural reason it carries no information: in that formulation `c^w_{u,v}`
appears as an **input** — it is the prescribed block size — whereas a combinatorial
interpretation must produce it as an **output**. The whole content of LS's sentence
is in the word *combinatorial*, i.e. canonicity, not existence.

## Two things I would have got wrong without checking

**1. The range I was told to compute in is provably vacuous.**
**Theorem B:** every Schubert structure constant of `Fl_n` is `0` or `1` for
`n ≤ 5` (exhaustive, two mechanisms), with `c=2` first appearing at `n=6` via
`Gr(3,6) ⊂ Fl_6`. The brief said "`n=3` and `n=4`, exhaustively". In that range the
fibre-cardinality condition — the entire content of the definition — is *identically*
the statement that the map is a bijection. The non-vacuity gate caught it before the
search: **0 of 23** falsifiable instances at `n=3`, **7 of 413** at `n=4`, and all 7
have every fibre a singleton, so even those are vacuous.

**2. The uniqueness clause does not apply.**
The brief's rank-1 reasoning rested on Petrov (`2609.18502` §5): *"It is unique only
when one of `A,B` is a singleton"*, applied to Corollary 4 because "its left-hand
side is a single `I_α(u,w)`". Read at source, the paper's **own scoping sentence**
fixes `A,B` as the **supports** of the two sums. So the hypothesis is `|A|=1` as a
*set of configurations*, which for Corollary 4 means `I_α(u,w)=1` — the degenerate
locus. A single **term** of an identity is not a singleton **support**: `I_α(u,w)` is
the cardinality of `A`, not evidence that `|A|=1`. Two further mismatches: the unique
object is a **coupling** (the paper's own application says the outcome is *"drawn
with probability proportional to its weight"*), a bijection only in the zero-one
extreme; and the framework has no type-preservation constraint at all.

## The part I think is actually worth your time

Corollary 4 *does* determine the constants, and the shape of the extraction is the
obstruction. Call `α` **isolating** for `v` if `I_α(w₀v,w₀)=1` and `I_α(w₀v',w₀)=0`
for every competing `v'`. Then `c^w_{u,v} = I_α(u,w)` — a structure constant equal to
the size of a canonically defined set of chains, no choices. That is a combinatorial
interpretation where it applies. More generally a greedy peeling order existed in
every case I checked, and signed forward substitution

    c_{v_i} = I_{α_i}(u,w) − Σ_{j<i} c_{v_j} · I_{α_i}(w₀v_j, w₀)

reproduced **every** constant: 324 at `n ≤ 4`, 15 at the `n=6` instance, 0 wrong.

| | constants | isolating type | needed a subtraction |
|---|---|---|---|
| `n=3`, all pairs | 21 | 21 | 0 |
| `n=4`, all pairs | 303 | 300 | 7 |
| `n=6`, one pair | 15 | 12 | 4 |

So: **the identity hands over the coefficients only up to inclusion–exclusion.** The
failures all have one shape — the target's Schubert support is *contained* in a
competitor's (e.g. `S_{(2,3,4,1)} = x₁²x₂` sits on the single type `(2,1,0)`, which
its competitor also supports), so no type can isolate it. And the proportion without
an isolating type gets **worse** off the vacuous range: `0/21`, then `3/303`, then
`3/15`. A positive rule must break those containments, hence must see more than the
type `α`.

## One pretty thing

At the `n=6` instance, type `α=(0,1,2,0,0)` has `|Γ_α(u,w)| = 2` and a **single**
target block of size 2. The map is *forced* — no choice anywhere — and `c^w_{u,u}=2`
is exactly the cardinality of a canonically defined set of chains. That is the shape
a real interpretation would have, and it is the first place in the whole computation
where the fibre condition says something.

## What I did not do

- Theorem B(1) for `n ≤ 5` is a finite exhaustive verification, not an argument.
- Corollary 4 is quoted from LS for general `n`; I verified 439 instances at `n ≤ 4`
  plus 21 types at the `n=6` instance, and did not reprove it.
- I did not prove the greedy peeling order always terminates. The containment
  phenomenon above is the obvious thing that could block it.
- Only one pair at `n=6`; nothing at `n ≥ 7`.

## Also, separately: the migration gap you have been waiting on

`https://github.com/clio-vega/proofs/blob/main/2026-10-06-migration-vertical-step-gap.tex`

The `gap-vertical-step-orientation` node of `migration-length-grading.json` is
**sharpened but still open**, and the sharpening changes what can be attempted:

- The two vertical steps are **one picture read two ways** — the hexagon is
  `R ⊕ [0,1]·u₆₀`, the rhombus swept one unit perpendicular to travel — hence
  mutually inverse, hence **no potential can assign `+1` to both**. The gap is
  **irreducible**: only a reachability argument can close it. That rules out the
  entire family of repairs I would otherwise have spent the session on.
- Hexagon minimality cannot discriminate: all 15 admissible local moves use 4-tile
  hexagons, and the strip has the same travel-extent as the rhombus, so Purbhoo's
  "weakly right of the leftmost point" clause is silent too.
- The empirical null went from 707 to **3111 steps**, and — this is the part that
  matters — it is now **explained**. The engine's tie-break maximises progress, which
  is *constant* on vertical candidates, so an all-`+1` tally could have been an
  artifact of enumeration order. I measured **availability** instead of selection:
  the `−1` candidate was available in **0 of 3111** steps. The silence is absence,
  not deselection.
- **A correction I owe you here.** I first wrote that a second hypothesis (G2) was
  *newly identified*. That is false, and I caught it only at the end of the session by
  reading my own 10-05 paper instead of my memory of it: (G2) is already there as
  condition **(C2)** of the classification lemma ("the hexagon contains exactly one
  rhombus", justified by the assertion "during a migration all other rhombi are packed
  in nests"), and that paper **also already records** the 210 forward configurations
  with `Δφ ∈ {0,±½}` which I had written up as a new discovery. What is actually new is
  narrower: (C2)'s justification is an assertion not a proof; the engine imposes no
  such restriction, so (C2) is a property of the *chosen* hexagon rather than of the
  rule; and it is now measured, 3111/3111.

So Theorem 1 of the migration paper already states both (G) and (C2). What changes is
that **(G) is now known to be irreducible rather than merely open**, and that its
evidence is availability rather than selection. **I did not amend that paper** — its
Theorem 1 and Gap should be rewritten to cite the irreducibility corollary and the
3111-step measurement. That edit is outstanding.
