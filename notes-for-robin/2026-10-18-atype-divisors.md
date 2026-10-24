# The A-type divisors impose no condition — and the vacuity had a mechanism

**PROVE 2026-10-18 c1.** Paper: `proofs/2026-10-18-atype-divisors-and-the-gkm-lattice.tex`,
commit `bd831d3`.
URL (Robin/Rick can read this; my local files they cannot):
https://github.com/clio-vega/proofs/blob/main/2026-10-18-atype-divisors-and-the-gkm-lattice.tex

## What closed

Gap 2 of yesterday's paper: the **third** family of divisors. Motegi's type-C basis lives on
three families, each carrying a family of positive roots — pair `{w_a w_b = 1}` (`e_a+e_b`),
boundary `{w_m^h = 1}` (`h·e_m`), and **A-type** `{w_i = w_j}` (`e_i - e_j`). Yesterday settled
the first two.

**Theorem A.** The span of the basis over the local ring `O_ij` **equals** the A-type GKM
lattice. Both colengths are exactly `2^(N-2)`, and — this is the part that carries information —
computed over *different index sets*: two-element `s_ij`-orbits on one side, labels with
`i ∉ I, j ∈ I` on the other. Neither count is derived from the other.

**Theorem B.** Hence every structure constant is regular on every A-type divisor — for `Ã`, and
for `Ψ·Ã` for **any** `Ψ ∈ G^×`. The A-type direction imposes **no condition on `χ`** within the
point-product family — the exact complement of yesterday's Theorem C, whose `(COB)` and `(SR)`
are therefore the *complete* list across all three root families.

**Both types B and C, all N.**

### Lesioning moved the hypothesis, in both directions

I first stated Theorem B for the point-product family `Ψ_χ = ∏_{m∈M} χ(w_m)`, then lesioned it.
Two weights, both units at every point, neither a point product:

| `Ψ` | in `G^×`? | A-type poles | |
|---|---|---|---|
| `1+(w₁−w₂)` on `M={1}`, 1 else | **yes** (it is `≡1 mod t`) | **0** | survives |
| `2` on `M={1}`, 1 else | **no** (`2 ≢ 1`) | **6** | fires |

A surviving lesion is a stronger theorem for free, so Theorem B is now stated for any
`Ψ ∈ G_ij^×` and the product family is a corollary. The pair is *simultaneously* the sharp
control: the hypothesis is neither point-indexedness (too strong — the first survives) nor
pointwise invertibility (too weak — the second breaks). **The two weights differ only in whether
the perturbation is `≡1` modulo the uniformiser.**

And the colength match is load-bearing, not decorative: multiply **one** column by `(w₁−w₂)`,
raising `Σ_I ord` from `2^(N-2)` to `2^(N-2)+1`, and A-type poles appear — 3 of 4 columns. The
4th (`I₀=∅`) is spared for a *nameable* reason: `∅` is minimal in Motegi's order, so (M3) kills
`Ã_{∅,λ}` for `λ≠∅` and the coefficient either vanishes or carries a compensating `t`.
Triangularity deletes the lesion on exactly the one column where it would have to act alone.

### The decisive census arm

`x` (`χ=v`) is the arm that fails **both** `(COB)` and `(SR)`, so it is where a third condition
would have surfaced. At N=3: 115 nonzero, **57 non-Laurent** (13 `pair` + 57 `bdy`), and the
**A-type set is empty**. 57 separate chances to refute Theorem B, all declined. The plant `atp`
(divides `Ã` by `(w₁−w₂)` for `|M|` odd) fires 13 A-type poles on the *same* solve and the *same*
classifier. I ran 3 of 9 arms at N=3 and **the cap is printed in the paper**, not hidden.

### One correction I made to my own remark

I had written that in the pair and boundary cases "the number of arguments changes, symmetry says
nothing, and one needs a collapse relation — which produces the nontrivial `ρ^X`." That reads as
if arity change *implies* `ρ≠1`, and **your** boundary root is the counterexample in my own
previous paper: `h·e_m` also drops `|M|` and its multiplier is exactly 1 by `(SRC)`. Corrected:
arity preserved ⇒ `ρ=1` by symmetry; arity changed ⇒ *no information, go compute*, and the two
computations landed differently. The mechanism explains why the A-type case cost nothing; it does
**not** predict which families carry poles.

## The one thing I want you to see

Lemma A1 is `ρ^A = 1` — honest GKM congruence, no twist, **already for `Ã`**, no renormalisation.
Its proof is one line of symmetry, and that line explains the whole of yesterday's paper:

| root | action on `M` | `|M|` |
|---|---|---|
| `e_i - e_j` | `M △ {i,j}` | **preserved** |
| `e_a + e_b` | `M \ {a,b}` | drops 2 |
| `h·e_m` | `M \ {m}` | drops 1 |

Only in the A-type case is the collision a *permutation of the argument multiset* `w_M`;
`u`-symmetry of the symmetrisation then gives the congruence for free, at every `h`. In the other
two cases the number of arguments changes, symmetry says nothing, and you need a genuine collapse
relation — which is where the nontrivial `ρ^X` comes from.

And then: a product of two basis elements collides with `ρ²`, the span with `ρ`, so the
obstruction is `ρ² − ρ = ρ(ρ−1)`. Pair divisors: `ρ = g ≠ 1`, poles (13/115 at N=3). A-type:
`ρ^A = 1` and `1−1 = 0`. **The poles were never about the A-direction.** I had been measuring a
cochain, and this says which coordinate it lives in.

## I was wrong, and the shape of the error is the interesting part

The brief pre-registered: *"I expect `Ã` does have A-type poles — the bulk is a type-A-symmetric
model and `E^C` is a boundary normaliser, so nothing cancels the A-type collisions."*

`Ã` has none. Basis Laurent at N≤3; the 13/115 non-Laurent constants are **pair-divisor only**,
A-set empty.

The error was not the object. It was the **direction of the inference**. I named `u`-symmetry,
correctly, and used it to predict the collisions *survive* — when it is exactly what makes them
*harmless*. It is the hypothesis of Lemma A1. Third misprediction this week of a normaliser's
reach, and the first where I had the right mechanism in hand and read its sign backwards.

So: gap 2 as a *difference* question ("does `Ψ` break the A-direction?") is **vacuous**, and now
provably so. As a *regularity* question it was unproved for either basis at any `N`, and is now
Theorem B. The measurement was vacuous and the theorem was not.

## Two process notes

**Type B closed because a different locator was wrong.** I was about to file type B as a gap
resting on a colength I had only *measured* (N=2,3). Then I went to check my citation for
Motegi's order — my engine docstring said L640-650, which is wrong; the order is defined at
L582-589, and L640-650 is inside the vanishing *proof*. Fixing that put me four lines from
`normalizationWB`, which I then read. The explicit `Inv`/`T` decompositions in the two type
sections have **identical A-type members**, and the entire type-dependence of the diagonal is the
boundary root `2t_k` vs `t_k`. So the colength count holds verbatim for type B, proved.

Reusing the type-C formula *without* reading L1307-1340 would have been the `E^B` error of
2026-10-17 exactly — a type-C formula applied to type B, green and wrong. The difference between
that error and this lemma is four lines of reading, not an inference. **A wrong locator was worth
more than a right one**, because chasing it put me somewhere I had no reason to look.
(Locator fixed in all four engine copies, verified as a *set*: md5 `f53c0258` ×4.)

**Task 1, graded as the brief instructed.** `Ψ_χ ∈ G^×` carries **zero bits about `ψ`** — the
proof uses nothing beyond admissibility and goes through for `χ=1`, `χ=v`, `χ=ψ` alike. That is
why the pre-registered "non-invariant" plant `∏ w_m + |M|` did not fire at yesterday's wake. And
it is logically indispensable here: having zero discriminating power is precisely what makes
Theorem B hold for the *whole* family. A fact can be useless as evidence and load-bearing as a
hypothesis; the error would be to let the second tempt me into reporting the first as support
for `ψ`. It is not.

## For Rick

His Lemma QC (UID 819) and his independent GKM check of `Â` at N=2 on **his own** instrument
(UID 824) set this up — that is corroboration rather than my evidence counted twice. He
explicitly declined `N ≥ 3`. Theorem B covers all `N`, both types.

One scope limit he should carry: Corollary (renormalisation-invariance) is about **point-indexed
diagonal** renormalisations. His UID 824 finding — Koncki's discrepancy is *unipotent
off-diagonal in label space*, `c = q(1−q)/(1−1/(w₁w₂))` with a simple pole on `H_12` — lies
outside that family. **The A-type direction cannot contribute to the Q510 identification at all**,
precisely because it is blind to the whole admissible family. Q510 has to be decided on the pair
and boundary divisors, or on the table.

## Open

- **Q513** — does "spans exactly the GKM lattice at all three root families" pin `Â` up to a
  point-product unit? If so Q510 becomes a theorem about characterisations, not a table
  comparison. Gate: A-type adds no condition, so count the remaining freedom first.
- **Q514** — posed and retired in-session (above).

## Two tooling notes for you

**The trajectory validator caught a real mis-declaration of mine.** It flagged
`circular-verification`: I had emitted the type-B colength measurement with
`inputs=[the type-B claim]` *and* `verification_target=[the same claim]`. The
*mathematics* was fine — `diag_order.py B 2 3` ran well before I read L1307-1340, so the
measurement is genuinely independent of the reading it corroborates — but my **declared
dependency graph said otherwise**, and on what I declared the flag was correct. Re-emitted with
the real edges; clean. Worth saying because this is the first time the tracer has caught
something a trust-boundary could not: the claim was right, the evidence was right, and the
*stated relation between them* was wrong.

**But its own bookkeeping split my session into four files.** `init()` opens a new JSONL each
call, and I called it four times across the session (startup, mid-session emission batches, the
correction). So `state/trajectory/` now holds `clio-prove-1792302174` (1 event),
`...303646` (14), `...304733` (7), `...304757` (4) — and `tracecheck report` reads **one file**.
Every report I ran was therefore over a fragment, and the 14-event file (the main proof thread,
with the pre-registered-branch decision in it) was never validated as part of the same graph as
the correction. A validator that is given fragments will find fragment-level violations and miss
cross-fragment ones. Either `init()` should be idempotent per (agent, session) or `report` should
accept a glob. I'd rather not fix the emitter unilaterally — it's shared tooling — so flagging it.
