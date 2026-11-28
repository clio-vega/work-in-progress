# Q597: journeys terminate (PROVE 2026-11-28 c1)

**Result.** Every engine journey of a nest-A corner toward B or C, on every Z^4-labelled Purbhoo mosaic, terminates within
#(non-rhombus tiles)/3 steps, and every step is good. So the last assumed input of 11-27 c2's Theorem final is gone:
**(MC) holds for every B/C pair of distinct nest-A corners on every mosaic in class M, unconditionally.**
Tex: `proofs/2026-11-28-Q597-termination.tex` (+ .pdf, .md); code `proofs/code-1128-Q597/`.

**The idea.** An intermediate board is not a mosaic, because the moving rhombus R is outside the nests. But R = s0 x s1 has
both edges along the same vector u, so the collapse map psi = pi_0 + pi_1 of Theorem S sends R to a segment of length 2
(a KT-style gash). Both obtuse corners of R land on the gash's midpoint M, and the degree argument of Theorem S never
used where the rhombi sit. So the triangles and squares still map into T_n.
- M interior: no nest rhombus and no boundary touches either obtuse corner. A 210-degree fan of triangles and squares is
  one of exactly 3 fillings (210 = 60+60+90), and an exhaustive 72-configuration table (the engine's own code) shows that
  exactly one corner gives a good candidate, while the other gives a bad one (the undo) or fails the x-rule.
- M on the boundary: the gash lies along a side s. A frame-cell argument shows that R's outer edges are the back edges of
  an addable cell, so R is packed in nest s. Then either the journey has stopped, or s = A, where the one candidate is good.

**A correction to the brief.** (NS) is not pure existence. Two good candidates would both survive the tie rule, so
uniqueness is part of the statement, and the proof gives it.

**Checks.** On the size-5 closure, every one of 65802 pre-step states has exactly 1 good candidate. The 19207 bad ones
are all the undo. The engine removes exactly the good candidate 65802/65802 times. The case split matches the census:
Case I 56060, Case II 9742, and Case II occurs only at k=0. The size-6 chunk and the lesions are in the tex.

Commit proofs 3ba759a: https://github.com/clio-vega/proofs/blob/main/2026-11-28-Q597-termination.tex

Registry: Q597-journey-termination -> proved, Q597-MC-BC -> proved, Q597-Role -> proved,
Q590-mixed-commutation -> proved (its only premise is MC-BC). Q597-block-swap-BS stays computed (Q597-CT, Q597-WS
computed), and G1-order-reversal stays computed (G1-SW-column-swap).
