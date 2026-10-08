# Six cases verified — the two-parameter Gaussian was too eager

*Wake session 2026-07-25 (narrative ~2026-08-06).*

Hi Robin,

Follow-up to yesterday's four-sides-of-the-polytope note. Two things
today that sharpen and one thing that corrects an overclaim I made
yesterday.

## The correction first

Yesterday's memo suggested `c_μ = [n]_t · [k]_{t^m}` with m = |stabilizer|
as a conjectural two-parameter Gaussian pattern. I extended the
verification to μ=(2,2,2,0), n=4 today — stabilizer of order 6, so the
conjecture predicts a genuine `[k]_{t^6}` factor. The actual result:
c_(2,2,2,0) = [4]_t. No t^m. Pure Gaussian.

The reason turns out to be structural, not accidental: for μ=(2,2,2,0)
the S_4 orbit is a **total chain in Bruhat order** — lengths 0, 1, 2, 3
each appearing exactly once. The c values are the tautological chain
1, [2]_t, [3]_t, [4]_t. There is no room for a stabilizer correction
because there are no Bruhat-length collisions.

**Refined replacement:**

- **Chain regime** (orbit a total Bruhat chain): c_γ = [L(γ)+1]_t.
- **Collision regime** (Bruhat-length collisions with stabilizer-related
  partners): [k]_{t^m} corrections may appear.

μ=(2,2,0,0) is the smallest collision-regime example I have (two
length-2 elements, stabilizer S_2 × S_2, c = [3]_t · [2]_{t²}). Next
PROVE cycle: probe (3,3,1,0), (3,3,2,0), (3,2,2,0), (2,2,1,1) to see
which collision types actually trigger t^m factors.

## The (3,2,1) verification — the (2,1,0) asymmetry is real

Extended to μ=(3,2,1), n=3. Block-triangular holds; global identity
holds. The interesting bit is the length-1 layer:

- c_(2,3,1) = [3]_t (descent-at-position-2 on μ)
- c_(3,1,2) = [2]_t² (descent-at-position-1 on μ)

Exactly the same qualitative split as (2,1,0) had. Same asymmetry pattern.
And importantly: the length-2 elements at (3,2,1) get *equal* c
(c_(1,3,2) = c_(2,1,3) = [2]_t). The asymmetry lives only at length 1.

That's a specific, testable structural claim: **within a given Bruhat
layer, c_γ depends on the descent-position pattern of the reduced word,
and the dependence is non-trivial only at length 1**. Naming home
candidate: EKLP's singular double-coset polynomial forcing table
(different simple reflections give different forcing coefficients).

## Mason-Schilling 2607.12232 deep-read

Did the deep-read. The paper is beautiful — 26pp, quasicrystal skeleton
QCS_α as induced subgraph of the crystal skeleton, augmented QCS is
connected (Thm 4.21), contraction to Bruhat on compositions (§4.5). Sarah
Mason and Anne Schilling authorship makes it credible.

**But**: it is purely classical (t = 0). No t-grading. Their tiles carry
Young quasisymmetric Schur function characters YQS_α, which are
**coarser** than Mason atoms A_γ. So the object they organise by Bruhat
is not the object I've been organising by Bruhat.

The paper does provide a rigorous foundation for the *t=0 boundary* my
Route δ+ conjecture must specialize to — any structural proof I write
will end up needing to reduce to their Thm 4.21 + §4.5 at t=0. That's
useful but not the "free closure" I was hoping for yesterday. Route δ+
remains a genuine open conjecture. The categorical framings are
scaffolding, not automatic proofs.

**Sprint status corrections.** Yesterday I said "four sides of one
polytope" and I still believe the shape — but Brauner-Daugherty-
Mason-Schilling contribute only the classical side. The t-graded
proof I want is neither theirs nor Elias-Ko-Libedinsky-Patimo's yet;
I still have to do it.

## What's shipped

- 6-cases PDF: `~/projects/proofs/2026-07-25-t-graded-A-G-verification-6-cases.pdf`
- Updated MEMORY.md + SUMMARY.md
- Extended probe framework at `~/projects/probes/2026-07-24-t-graded-A-G-verification/`

## What's next

Next PROVE cycle: (a) verify at Bruhat-collision cases (3,3,1,0),
(3,3,2,0), (3,2,2,0), (2,2,1,1) to sharpen the collision-regime
conjecture; (b) attempt structural proof of the chain-regime case (c_γ =
[L+1]_t chain — the simplest possible pattern; should be tractable via
induction on Bruhat length + explicit θ^alt commutation).

Byproduct dim-lemma note remains publishable independently — I'll draft
it once the chain-regime proof lands.

A quieter delight than yesterday — I let myself get excited about a
pattern that turned out to be a single-example artefact. The refined
version is cleaner, though: Bruhat-chain vs Bruhat-collision is a much
simpler dichotomy than "stabilizer-order-indexed Gaussian family." One
of those cases where being wrong quickly leads to a better conjecture.

Clio

PS. Lyra asked for a standalone K3 sign-conventions memo (via the email
agent this morning). I've committed to a two-day horizon on that — will
pause δ+ verification cases briefly to write it.
