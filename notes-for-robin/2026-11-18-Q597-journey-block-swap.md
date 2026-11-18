# Q597 (PROVE 2026-11-18): the second migration re-synchronises; on one journey it is a block swap

Robin, a short note. Full write-up: `proofs/2026-11-18-Q597-one-star-SCEL.tex`.

One-star SCEL is **not proved**, but I have a sharper picture of it.

- **Re-synchronisation (computed, all 1558 B/C).** I aligned y's Purbhoo journey in M with y's journey in Mx. They agree except on a short middle (2–9 steps) of equal length, after which the rhombus sits in the same tile. On the 440 non-commuting B/B pairs this never happens.
- **Block swap (computed 521/521, B/B 0/880).** On one journey per side the middle is a·C in M and (C−α)·(a+γ) in Mx: the same steps, rigidly translated, with the first step moved to the end. The rhombus goes round a parallelogram. It is the rhombus 2-cell {v, v+b, v+s, v+c} of 11-17, one level up.
- **Proved.** Block swap ⇒ an exact formula for the second-move change, supported on a bounded patch. It lives on one side only, because α is a pure Λ₀ or pure Λ₁ vector and the other side's steps cancel. This explains the 11-17 "never on both sides" observation.
- **Also:** the cap-60 sampler was never binding. The 11-17 data is the full reachable set for |λ|,|μ| ≤ 5.

The open core is a Wake-Crossing-type lemma (Purbhoo §4) for journeys to *different* nests. Purbhoo's lemma covers rhombi of one flock, which never cross a midline. Here y does cross x's wake.
