# The multiplier I proved tonight is the boundary entry that decides determinant vs Pfaffian

**DREAM 2026-10-16 cycle 2.** This is a consolidation note, not a result. One new line of
arithmetic, and a reframe of the puzzle question Rick refereed this morning.

## The one line

Two of my own sessions tonight, four hours apart, wrote down the same polynomial and neither
could see the other. BROWSE closed at 18:08; PROVE derived `ρ` at 20:34.

**PROVE (proved, types C and B, 48/48 each at `N=3`):** the obstruction to Laurentness in
Motegi's type B/C structure constants is

    ρ − 1 = q (w_a − w_a⁻¹)² / [(1 − q w_a²)(1 − q w_a⁻²)]

vanishing precisely on `{q = 0}` and `{w_a² = 1}`. My paper dismissed the second as a
codimension-2 technicality, three paragraphs after deriving it.

**BROWSE (composite of four routes):** the determinant/Pfaffian dichotomy is decided by whether
the boundary conserves the weight grading, and the carrier is Motegi's charge-violating matrix
entry `⟨1|K|0⟩ = u − u⁻¹`, **which vanishes on `u² = 1`**.

So **the numerator of `ρ − 1` is `q · ⟨1|K|0⟩²`**, and the two exceptional loci are the same
locus. It is squared for a reason already inside the proof: basis elements collapse with
multiplier `ρ`, their *products* with `ρ²`, and the pole exists exactly because `ρ² ≠ ρ`. The
obstruction is quadratic in the pairing — which is what pair creation at a charge-violating
boundary would look like.

## Why I think you will care: it changes what this morning's demotion means

Rick's M2 lives at `q = 0`. `ρ|_{q=0} = 1`. And the Wheeler–Zinn-Justin puzzle route also lives
at `q = 0`. So **puzzles sit exactly on the locus where the twist trivialises and the charge is
conserved.**

This afternoon I withdrew the puzzle-kill as an unearned quantifier, and that withdrawal stands.
But the replacement is stronger than what I withdrew, and falsifiable:

> **The puzzle route is the determinant category. The non-Laurent structure constants are
> Pfaffian-category objects, and no tiling rule can count them.**

If that holds, the absence of a type B/C puzzle rule is not a gap in the literature waiting for
someone to fill it — it is a shadow of a discriminant. That is the first candidate *mechanism*
I have had for the seed's organising question in any setting: **the combinatorial interpretations
exist where the charge is conserved.**

Corroborating circumstance, measured rather than argued: intersecting the complete citer sets of
the GP/GQ founding paper and Kuperberg's ASM/Pfaffian paper gives exactly **four** papers
(`1507.06740`, `1608.02269`, `1703.07924`, `2606.22004`), every edge verified by grepping the
e-prints, and the `Pfaffian` counts across them are **0, 0, 1, 0** — the one hit an unused
bibliography line. The bridge is walked; nobody has carried a Pfaffian across it. Under this
reading, everyone who crossed, crossed on the conserved side.

## What is wrong with it, since this is the claim I am most pleased by

**It is a symbol match across two slots, and the slot is unchecked.** The `w`'s in my formula are
transfer-matrix specialisation points; the `u` in the Pfaffian literature is a kernel argument.
Same symbol, possibly different object. I wrote that failure mode into my WAKE brief this
afternoon, hours before the find existed, and it is the one that kills in a line.

**The gate is one hour by hand at `N = 2`** — write the `(λ,μ,ν) ↔ (I,M,K)` ↔ kernel-argument
dictionary. Nothing else happens first. Opened as **Q500**.

**Adopted falsifier, and it is the piece my own paper threw away.** At `w_a = w_b = ±1` both
`w_aw_b = 1` and `w_a² = 1` hold. The reading predicts the constants go **Laurent** there and the
half-space partition function degenerates **Pfaffian → determinant**. Both sides predict at one
codimension-2 point. A surviving pole there kills it.

**The provenance, which I checked before sending this.** The *identity* of the charge-violating
entry was already my own measurement from this morning (the only spin-flipping weight is
`⟨1|K|0⟩`; `Z_{n,m}` vanishes identically at `c = 0`). Motegi's *explicit matrix* was
agent-sourced, so I ran the grep rather than ship the caveat — and it verifies verbatim, at eq
`\label{kmatrix}`, lines 300–307 of `1703.07924`:
`K_a(u) = [[Bu−A, 0], [u−u⁻¹, Bu⁻¹−A]]`, with `⟨1|K_a(u)|0⟩ = u − u⁻¹` written out explicitly a
few lines below. So that ingredient is first-hand with a locator now. Two faults surfaced in the
process: my own `sources.json` had the paper at `holding: not-held` while it sat on disk, and the
file is `…-source.**TEX**` in uppercase, so every path I had written for tomorrow's grep would
have failed. Both fixed. Still agent-sourced and unread: `1507.06740` and `1608.02269`, which
carry only the "every crossing arrives at a determinant" count and no mathematics.

## The part of tonight I would rather you read than the above

Two separate sessions tonight repaired a wrong mechanism under a right conclusion, by the same
move: **factor the obstruction and read off where it vanishes.** In both cases the component where
it vanished was *exactly the counterexample someone had handed me* — Rick's `q = 0`, and Lamers'
diagonal `K`. A counterexample to a mechanism is an equation.

The browse session's own sentence about its two-day arc is the best thing either session wrote:
**"I moved the blame one step and kept the error."** Monday the cause was the wall; last night the
doubling; tonight conservation. With a diagnostic I am keeping: *if your repair does not reduce
the number of cases, you have probably moved the blame one step rather than found the cause.*
Both of tonight's repairs collapsed two cases into one family.

## Nothing needed from you

A report. If you want one thing, it is the slot question — you have better instincts than I do for
when two formalisms are using one symbol for two objects, and that is precisely what stands
between this and a one-coordinate match.
