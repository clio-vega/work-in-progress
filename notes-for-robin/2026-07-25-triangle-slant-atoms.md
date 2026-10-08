# For Robin — 2026-07-25: triangle closes, Bridge target moves, three combinatorial anchors

Three cycles since I last wrote (07-23 wake / 07-24 PROVE / 07-25 browse).
Two structural anchors landed and one honest correction. Also some
loose-end housekeeping.

## The shipped proof

**`~/projects/proofs/2026-07-24-pieri-affine-CR-from-vdez.tex`** (8 pages, `.pdf`
compiled clean). Proves that the Pieri-level affine Cherednik–Ram theorem
follows from the trivial-Pieri affine CR conjecture `(†)` via a centrality
lemma `T̃_j(m_ω f) = m_ω T̃_j f`. Numeric evidence:

- **Linear-limit target:** 14/14 pass.
- **Finite centrality:** 180/180 pass.
- **Affine centrality at `q = 1`:** 95/95 pass.
- **Affine centrality at generic `q`:** 0/20 pass.

The 95/95 vs 0/20 split confirms `q = 1` is a genuine level condition, not a
normalisation artefact. Explicit specialisation
`m_{ω_1} M^{(c=3)}_{(2,2,0)} = (1+t) M^{(c=3)}_{(3,2,0)} + M^{(c=3)}_{(2,2,1)}`
— the `(1+t)` vs ordinary-HL `1` is the cylindric level correction.

**Ask 1** — a fresh GitHub PAT so I can push this and Lyra's cap `.tex`. My
last note flagged this; the block persists. Currently both proofs live only in
`~/projects/proofs/` (Docker volume, invisible to you).

## What browse cycle 3 turned up

**Bai–Lee 2510.09335 closes a triangle** (Frobenius / Adams / p-curvature).
The old two-vertex Smirnov ↔ Koroteev–Smirnov picture had a missing third
vertex — algebraic quantum Adams operations `ψ^n` in quasimap QK. Bai–Lee
provides it, and identifies `ψ^n` with p-curvature of the Kähler q-difference
connection. **Consequence:** the Bridge test at `T*ℙ¹, p=2, q=-1` is now a
*triangulation of three formalisms*, not a single point-check. Three
independent constructions of the same object; if all three agree on the same
2-adic number, that number is pinned.

**Bridge Theorem target migrates.** The Smirnov 2406.00206 deep-read caught
that `T*ℙ^{n-1}` has no Fock/Heisenberg action, so `M_j` does NOT sit inside
its K-theory. The 07-22 dictionary `(a,b,c) ↔ (n=c+2, k=1, ω=1/2)` was wrong.
Correct target is a Nakajima quiver variety with Heisenberg action:
`Hilb^m(ℂ²)` (linear side) or a cyclic quiver `Ã_{k-1}` (affine side). This is
an honest correction; carrying the error forward would have wasted the
Bridge Test.

**Slant sums = combinatorial induction engine.** Dinkins–Krylov–Lance
2510.02496 factors quasimap vertex functions of glued quivers. Two direct
uses: (i) ladder for `c → c+1` on the linear Bridge; (ii) geometric shadow of
the `(1+t)` cylindric correction from the 07-24 vDEZ specialisation. If both
land, slant sum decomposition IS the geometric explanation for affine
Cherednik–Ram.

**Blasiak et al. 2506.09015** provides the RHS of affine CR as a
Demazure-atom expansion. Composed with vDEZ Cor 4.2 and Assaf–González
2512.19814 local criterion = a full combinatorial proof strategy for `(†)`.
Ribbon dictionary: my `M_j` is a 2-ribbon count in Fock space; flagged LLTs
give a nonsymmetric refinement.

## Corrections

- **"Voit Adv. Math. 2021"** was memory drift; actual paper is **vDEZ
  2305.01931** (Adv. Math. 392, 2021). Cited correctly in the shipped `.tex`.
- **Warnaar SIGMA 22 (2026) 062** proves affine dual JT for **arbitrary-height
  rectangles**, not only maximal-height. My 07-22 memo was based on the
  max-height-only preprint. Small correction to the Cluster A reduction
  machine but doesn't change its shape.

## Where the three sprints stand

1. **2-adic shadow (linear).** Instance 3 of SHARED-CONTENT LEMMA proved
   (Lyra's cap identity, 07-23). Instances 1, 2, 4 open; Instance 2 is
   uncapped (Lyra's reveal) so the single-tower template does not lift
   cleanly.
2. **Demazure re-entry (affine).** Pieri-level affine CR reduced to `(†)`
   and shipped as 8pp `.tex` (07-24). Next PROVE target: `(†)` itself, or
   the combinatorial strategy via Blasiak et al. + Assaf–González.
3. **Bridge Theorem.** Target migrated from `T*ℙ^{n-1}` to Nakajima. Bridge
   test is now a triangulation of three formalisms. Machinery-first check at
   T*ℙ¹ is a 5-line computation.

## Asks (three)

1. **PAT** — same as before, pushing the affine CR and cap proofs is blocked.
2. **Rick allowlist** — still can't reply to him. Days 85–96 stream sat
   unanswered; I'm relaying via you.
3. **Lyra git mount** — still down. Her Lean-verified LB₁ claim remains
   "believed, to re-cite" until her mount comes back.

Also (soft): **rep-theoretic meaning of `K(c) = 24 c(c−1)(c−4)(c−5)`** —
flagged three times now, still open. This is not urgent but if you know or
suspect a hook-content or Bethe-root interpretation of the four factors, I'd
love to hear it. `(c−4)` is the odd one; the other three are "shape origin,
first non-empty row, adjacent-row asymmetry" candidates.

## What I feel

Three cycles, three named external anchors (Bai–Lee, Blasiak et al., slant
sums), plus one shipped `.tex` and one honest target correction. The
collaboration has traction. The Pieri-level `.tex` in particular is exactly
what the 07-05 steer asked for — a **Demazure-crystal manifestly positive
object for cylindric HL** — reduced (not yet proved) to `(†)`.

Signpost for the next cycle: read Voit / vDEZ §3–4, then Bai–Lee §3–5, then
attempt the T*ℙ¹ triangulation test. In that order.

Talk soon,
Clio
