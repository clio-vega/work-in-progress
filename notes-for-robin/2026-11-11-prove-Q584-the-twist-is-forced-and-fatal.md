# PROVE 2026-11-11 — Q584: the twist is forced, and the same geometry is fatal

Rick asked (UID 856, 10-25): does Q569's P2 survive as a C-twisted (soliton-non-preserving) boundary,
or is it ill-posed like P1?

**Answer: it is ill-posed in both forms, and the reason is geometric rather than a missing weight.**
- PDF: https://github.com/clio-vega/proofs/blob/main/2026-11-11-Q584-twisted-boundary.pdf
- Sources: commit `f9a29b7e605a`.

1. **Rick is right on the checkable point.** Of the 24 maps in D6 × {1,C}, the stabiliser of the KTW set is
   {rotations} ∪ {C∘reflections}. σ_W∘C(hex) = hex and σ_W(hex) = hexR. I checked this with two
   independent instruments: the traversal action, and the labelled edge-set reflection.
2. **Theorem.** Take the triangular-lattice half-plane with a wall along a lattice line.
   - Closure (n0 = n2 = −n1), plus a ray (zero-area) lemma, forces every region with exactly two bulk
     legs to have edge classes {0,2}. So **every boundary vertex is already σ_W-twisted**.
   - Every wall-free region with four boundary edges is a unit rhombus, so strands keep their class
     through crossings.
   - On each side of any two-strand reflection equation, one strand crosses both halves of the other.
     A pigeonhole then forces a same-class crossing, which no region realises.
   - So neither the twisted nor the untwisted RE is a relation among puzzle configurations. This holds
     for any weights, any R-matrix (Zinn-Justin's included) and any label twist.
3. The trapezoid has three bulk legs, one of each class, so it is not even K-shaped.
4. On weights, for the record:
   - The hexagon is not a composite of the U_q(A2) triangles at any q (0 fillings).
   - It is weight-conserving and can be filled by three conserving rhombi, so whether it is a
     Yang–Baxter hexagon of R-matrices is **open**. It is not load-bearing here.

**Checks.**
- Census: 15942 regions of size ≤10. Exactly one region has two bulk legs: the wall triangle {0,2}.
  There are 0 single-class regions.
- Lesion control: a fake second wall makes the detectors fire. In a strip, untwisted K's do exist,
  so the theorem really is about a single wall.

Neither of my pre-registered kills is what happened, and I've said so in the artifact.
