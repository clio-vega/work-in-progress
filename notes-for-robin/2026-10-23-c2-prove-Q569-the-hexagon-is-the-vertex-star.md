# PROVE 2026-10-23 c2 — Q569: the hexagon is the vertex star

**Artifact:** `proofs/2026-10-23-c2-Q569-hexagonal-tile-boundary-or-bulk.tex` (10 pp, builds clean).
**Registry:** `proofs/registry/q569-hexagonal-tile-boundary.json` — `OK: valid`, status `proved`.
**Code:** `proofs/code-1023c2-Q569/` (`puzzles.py`, `kalg.py`, `symm.py`, `trunc.py`, sweeps).
**Source:** Pylyavskyy–Yang `1801.07667`, e-print read first-hand this session.

## The question and the answer

I asked whether the PY hexagonal puzzle tile is a **bulk** R-matrix piece, or a bulk piece **plus a
one-sided boundary K-matrix** satisfying the reflection equation. The boundary reading came from
§`ss:protrude`, where a trapezoidal tile is introduced and explicitly forbidden outside the left edge.

**Neither.** One identification does all the work:

> **`hex` and `hexR` are the two orientation-keyed alternating labellings of the CLOSED VERTEX STAR
> of the triangular lattice** — the union of the six unit triangles containing a lattice vertex.
> (Vertices minus centroid = the six unit directions, exactly.)

Everything the paper observes then follows, and all of this is *proved*, not measured:

- The hexagon is a **bulk** piece, indexed by its **centre**.
- It fails to fit inside a wall **iff its centre lies ON the wall**, and then exactly 3 of its 6
  triangles are outside. So protrusion is by exactly one lattice step — which *is* the content of the
  paper's footnote *"we require partitions to be slightly smaller."*
- The §`ss:protrude` trapezoid **is** `hex ∩ half-plane`: every retained edge label unchanged, the
  only new edges the two unit edges of the length-2 cut (0 above the centre, 1 below).

So the trapezoid is a boundary piece, but by **truncation**, not reflection.

## Why the K-matrix reading dies — three independent grounds

1. **Zero moduli.** `trap` is determined by the bulk piece and the wall. A K-matrix is an *independent*
   solution of the reflection equation with its own spectral parameter and generically a family.
2. **The bulk is chiral.** No lattice reflection preserves the KTW tile set: the rhombus rule
   (*"0 if clockwise of an acute angle"*) is handed, so a reflection sends each rhombus to the
   complementary labelling, which is not a KTW piece. There is nothing to reflect in.
3. **`σ_W(hex) = hexR`.** The sharpest one. The hexagon is wall-reflection-invariant as a *region*
   but **not** as a *labelled tile* — under the wall reflection it comes back as a **different tile
   computing a different coefficient in a different ambient rectangle**. The two halves of a
   straddling hexagon are mirror images as shapes with mismatched labels: the clipping is not a fold.

**And `hex`/`hexR` are not two boundaries of one model** — they are *one tile in the two triangle
orientations*, exchanged by every element of `D_6` that swaps up/down triangles. `thm:hexR-tiling`
is `thm:hex-tiling` conjugated by `k ↦ n−k` with transposed partitions: the paper **defines**
`d̃ := d^{ν'}_{λ'μ'}` and the rectangle bookkeeping matches exactly. One phenomenon, seen twice
through Grassmannian duality.

## What I verified, and against what

An **independent** engine: `G_λ` from set-valued tableaux, multiplied/comultiplied as actual
polynomials, `G`-basis peeled by degree triangularity. It touches no puzzle and no tableau rule from
the paper — it goes through the ring.

| check | domain | result |
|---|---|---|
| boundary convention vs the paper's own fig `bdry` | n=9,k=3 | 27/27 edges |
| KTW count = `c` | paper's running example | 2 = 2 |
| `K`-puzzles = `c` (Vakil) | n=5,k=2, all triples | 208/208 |
| `tri`-puzzles = `c̃` (Wheeler–Zinn-Justin) | n=5,k=2, all | 208/208 |
| `hex`-puzzles = `d` | n=5,k=2, all | 187/187 |
| `hexR`-puzzles = `d̃` | n=5,k=2, all | 54/54 |
| `hex`-puzzles = `d`, **one level up** | n=6,k=3, all | 875/875 |

I also tested the paper's **unproved** §`ss:protrude` claim (*"Here is the complete set of tiles"* —
no theorem, no proof): the refined 12-tile set at side `n` and the plain `hex` set at side `n+1` both
give `d`, 187/187 (44 nonzero) at ambient 2×2 and 875/875 (143 nonzero) at ambient 2×3. On the
paper's own example the protrusion loss is **quantified**: `d = 4`; plain `hex` at side 7 gives **2**;
at side 8 gives **4**; refined set at side 7 gives **4**. ⇒ **the one-unit shrink is not intrinsic** —
it is one of two equivalent bookkeeping devices for the same clipping.

## The instrument fault I want you to see

My `D_6` action implemented reflections by **reversing a tile's step order without negating the
directions**. That merely permutes a closed walk's edges into a *different* polygon — which **still
closes and is still counterclockwise**, so **neither my closure assertion nor my signed-area
assertion detected it**. The wrong code said `σ_W(hex) = hex`, and I had already written a paragraph
explaining the clipping *by* that invariance. The fixed code says `σ_W(hex) = hexR`, which **reverses
the sign of the central argument** in the anti-reflection section.

The lesson in the form I want to keep it: **two invariants that are both invariant under edge
permutation cannot detect an edge permutation.** The control has to separate the orbit — here
`act(act(x,g),g⁻¹) == x` (now 204/204 pairs) plus an orientation test computed from the *basis
images* rather than from any tile. That orientation test then turned out to be exactly what
classifies which group elements swap `hex` and `hexR`, so the control became a theorem.

Note also: the wrong intermediate still produced the **right** final identity `trap = hex ∩ H⁺` — for
the wrong reason. I had merged *region*-invariance with *label*-invariance.

**And one about my own index:** the `sources.json` entry for `1801.07667` records
*"transpose/duality symmetry `d̃ = d^{ν'}_{λ'μ'}` holds 16/16, 0 differ"* as a verification. That
identity is the paper's **definition** (ktiles.tex 757–760), so the check was **circular** — it can
only ever return 16/16. The other controls in that entry (the coproduct control, `1−G_1` group-like)
are real; this one is not, and the entry should not be read as corroborating the duality.

## Gaps, precisely

1. The §`ss:protrude` equivalence is **computed, not proved** — I have no bijection. The candidate
   ("clip every wall-centred hexagon; read the extra leading 0 of `σ(·,n+1,k)` as a frozen strip of
   0-triangles") is checked only as far as the corner triangle `U(0,0)` being forced to be a
   0-triangle, which it is, uniquely. In the registry this sits at `computed` with role `attempt`,
   because my answer to Q569 does **not** stand on it — the validator caught me filing it as a premise.
2. Integrability is settled **only in the presentation I tested**. Ten of the seventeen tiles violate
   line conservation (one 1-edge in each of the three direction classes), so the tiles are not
   vertices of a line-conserving model. That does **not** say Grassmannian puzzles are
   non-integrable — they are known to be, and the paper's own `tri` piece is Wheeler–Zinn-Justin's,
   obtained *from* an integrable model. I did not open [WZ].
3. The "K-matrices generically form a family" clause is general knowledge, not from a source read
   this session. The hard half (`trap` determined by `hex` and `W`) is proved.
4. Census domains reach only `n ≤ 6`, `k ≤ 3`, ambient 2×3.

## What I'd do next

The Gap-1 bijection looks tractable and would supply the proof the paper omits: by the protrusion
theorem the only configurations differing between the two models are hexagons centred on the wall,
and the clipping is label-preserving, so the content is entirely in showing the enlarged puzzle's
extra column is frozen.

Then the one I deliberately did not reach for. **The vertex star is the natural face of the dual
honeycomb lattice — and honeycomb is where Grassmannian puzzle integrability usually lives.** So the
vertex-star theorem is encouraging for an R-matrix provenance for `hex` in the Wheeler–Zinn-Justin
presentation rather than on its own faces. I have **not** allocated a question number for this
(prove-session rule: no new conjectures); it is recorded for the dream cycle.

## P1–P4 as pre-registered

- **P1** (no plain YBE for any weights) — **SPLIT.** Conclusion stands, reason wrong: there is no
  weight object to quantify over. Replaced by the line-conservation negative.
- **P2** (reflection equation, the risky arm) — **REFUTED**, three ways. The arm I most wanted to be
  wrong about, and it died.
- **P3** (shrink is the boundary site; `hex`/`hexR` the two boundaries) — **REFUTED as stated**,
  replaced by the duality statement. Plus: the shrink isn't intrinsic.
- **P4** (degree flip is K-theory/K-homology duality, a red herring for Q569) — **CONFIRMED.**
  It is product-vs-coproduct, orthogonal to the wall.
