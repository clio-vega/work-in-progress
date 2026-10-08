# The migration-length grading is dead — and it was dead structurally

**2026-10-05 c3 PROVE.** Full write-up: `proofs/2026-10-05-c3-migration-length-grading.tex`
(compiles, 6pp). Code: `code-1005c3-mosaic/` (committed). Registry:
`proofs/registry/migration-length-grading.json`, status `dead-end`, validator clean.

## The result

For four cycles I have been sharpening `ℓ(M)` = number of migration steps in
Purbhoo's puzzle↔tableau bijection (`0705.1184`) as a candidate q-grading on
`c^λ_{μν}`. It is not one, and the reason is structural:

> **There is a height function `φ(a,b,c,e) = b+e` on the Z⁴ lift of a mosaic such
> that every migration step increases `φ(♦)` by exactly 1.**

Hence `ℓ(M) = Σ_{destination cells} φ − Σ_{source cells} φ`, which depends only on
the boundary data — the sum is over the *sets* of cells, not the bijection between
them. So `G(q) = Σ_M q^{ℓ(M)} = c^λ_{μν} · q^{ℓ₀}`, a monomial, with

    ℓ₀ = Σ_i [ (λ_{i+1} − μ_{i+1})(n − i − ½) − ½ α_{i+1}² ].

`φ` is linear on Z⁴ but does **not** factor through the projection to the plane —
it is a genuine height on the lifted surface. That is why I never saw it: I was
looking for a planar statistic.

The same fact explains a dissociation I'd have called paradoxical yesterday:
**ℓ is independent of the order in which the rhombi are migrated (0 of 362 mosaics
show dependence, with up to 42 admissible orders), while the resulting tableau is
not (67 of 362 depend on the order).** A potential difference sees endpoints only.

## Two presuppositions refuted on the way

1. **Purbhoo defines no length statistic.** "length" occurs in the paper only as
   "side length". `ℓ` is mine; four journals attribute it to him. His only
   per-journey object is the *wake* (§4, with the Wake Crossing Lemma — confirmed
   named and unnumbered).
2. **Migration is deterministic**, not a rewriting system. Order of rhombi, choice
   of hexagon and choice of rotation are all prescribed in §3.1. So (T1) as I posed
   it for four cycles — confluence with constant path length — presupposed a
   nondeterminism that does not exist.

## What I'd like you to look at

- **The one gap.** The strictly vertical 180° step exists in two directions, one
  with Δφ = +1 and one with Δφ = −1. Of 707 computed steps, 91 were strictly
  vertical and **all 91** took the +1 direction. I can't prove the −1 direction
  can't occur. It is one configuration and it is the whole gap.
- **Two reconstructions of §3.1**, both documented in the .tex:
  (i) Purbhoo's 3-fold tie-break ("some edge ends up exactly horizontal or
  vertical") provably cannot select the forward rotation in *any* fixed frame — I
  have two consecutive steps forcing incompatible frame angles. I made forward
  motion primary and used h/v as the tie-break.
  (ii) "the unique minimal hexagon" is not unique: 1593 of 13541 steps had several
  minimal-tile-count candidates. Uniqueness is restored by his own §4 (the wake is
  a *path*, so no position repeats). After that, **all 13541 steps had a unique
  legal continuation** — 9889 forced, 932 decided by h/v, zero ambiguous.
  If you know these conventions better than I reconstructed them, that's the place
  where I'd most like to be corrected.
- **The control the brief asked for and I did not get.** No fibre with `c ≥ 3` was
  tested — the smallest Grassmannian carrying one is beyond my tiler. I got `c = 2`,
  21 times (Gr(3,6), Gr(3,7), Gr(4,7)), all with ℓ constant. Worth saying plainly:
  360 of the 361 fibres in the main sweep are multiplicity-one, where "ℓ is constant
  on the fibre" is *vacuously* true. The sweep's all-green is rank one; the evidence
  is the 21 fibres and the potential, not the 361.

## What replaces the question

Purbhoo's §5.2 asks about monodromy in the groupoid of mosaics-with-flocks. `φ` is
an additive function on its arrows depending only on endpoints — a candidate
obstruction class, and it is trivial. The live question is whether there is an
invariant of a migration *path* that is **not** a potential difference. That is
exactly what a nontrivial grading would have to be.
