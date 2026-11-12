# Dream 2026-11-12: the commutativity "train" for Q585 is Purbhoo's migration, by KZJ I's own pointer

Robin, a short one.

This morning's PROVE (Q585, `clio-vega/proofs` `0a0d607`) showed that a crossing built *from puzzle triangles* has rank 3
and cannot carry a commutativity bijection. It then marked the question blocked on finding a source for "the train".
Tonight I found that source on the seed shelf:

- **KZJ I** (`arXiv:1706.10019`, p.24): the same-color crossings in their YBE argument are *"closely related to the
  (150°, 30°) rhombi in [Pur08]"*.
- **Purbhoo** (`arXiv:0705.1184`) migrates exactly those rhombi to swap two flocks. That gives a **bijective** proof of
  commutativity. The swap is an involution (Prop 5.4), and migration is a sequence of jeu de taquin slides (§5.1).

So the rank-3 result is the bootstrap degeneracy, not an obstruction, and Q585 becomes concrete: **does Purbhoo's swap
equal the crystal commutor?** The commutor side is already built and controlled (67 cells with c ≥ 2).

Purbhoo's §5.2 then asks whether the groupoid of migrations has monodromy. That is the Henriques–Kamnitzer cactus question
in puzzle language, now Q587.

**Grade:** both quotes are first-hand from the local PDFs. The step "KZJ crossing = Purbhoo migration" is my inference;
KZJ say only "closely related". Nothing here is computed yet.
