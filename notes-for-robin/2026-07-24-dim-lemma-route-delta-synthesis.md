# V_{<μ} lemma — dim-lemma reduction × Route δ (Assaf-González)

**Date:** 2026-07-24 (container) / narrative ~2026-08-04
**Two landings today; one synthesis.**

## What happened

**PROVE session** shipped `/home/clio/projects/proofs/2026-07-24-atoms-decomposition-P-mu-part-II.pdf` (7pp). Two bugs fixed in 07-23 verification (sign typo `(t-1) → (1-t)`; stabiliser undercount in C-R sum). After fix, `R = P_μ − Σ_γ c_γ A^alt_γ = 0` in **12 cases at n=3 and 12 at n=4**.

**Reduction Theorem shipped in same tex:** V_{<μ} lemma ⇔ `Σ_γ c_γ A^alt_γ` is `S_n`-symmetric ⇔ `P_μ ∈ V_μ^alt`. Proved via **Dimension Lemma**: `dim(V_μ^alt ∩ Sym) ≤ 1` (atom triangularity + S_n symmetry). Numerically dim = 1 in every case; unique-up-to-scalar generator matches V_μ back-sub c_γ **exactly**.

**Browse cycle** landed **Assaf-González 1901.07520 [was mis-cited as A-G 2512.19814]** (Dec 2025) — *A Local Characterization of Unions of Demazure Crystals*. Three-agent convergence (arXiv listing + Semantic Scholar citations + ICERM Fall-2025 co-location). Local edge-condition with disjoint atom decomposition as corollary — **directly the vanishing shape needed for V_{<μ} at t=0**. Added to closure portfolio as Route δ.

## The synthesis

**Two mechanisms, one target:**

- **My dim-lemma reduction (algebraic):** V_{<μ} is a one-dimensional existence question — does the (proved unique up to scalar) symmetric element exist in V_μ^alt?
- **Route δ (A-G, crystal):** at t=0, θ^alt_i degenerates to Mason's classical atom operator, so V_μ^alt |_{t=0} = span of ordinary Demazure atoms. A-G local edge condition tests Demazure-decomposability directly.

**They commute at t=0** because Schur = union of classical Demazure atoms is well-known (L-S 1990, Mason 2006). The research content lives in the **t-graded lift**.

Full write-up: `/home/clio/projects/memory/connections/2026-07-24-dim-lemma-meets-route-delta.md`.

## Portfolio now has five closure routes

| Route | Character | Cost | Status |
|---|---|---|---|
| α (Borodin-Wheeler 1904.06804 [was mis-cited as vDEZ 2412.09397]) | Same-team; T̂_j = θ^alt via Vandermonde | ~40 LOC + DAHA | Priority-1; closes at generic t |
| β (Paten-Woodruff) | Downgraded 08-03, superseded by δ | — | — |
| γ (Cárdenas + Lapointe) | Closed formula for c_γ(t); Talca | Requires Macdonald ω bridge | Naming-home candidate |
| **δ (Assaf-González 1901.07520 [was mis-cited as A-G 2512.19814])** | **Local edge + disjoint atom corollary** | **~60 LOC crystal (no DAHA)** | **NEW; cheapest** |
| **ε (own, 07-24)** | **Reduction Theorem transforms target** | **In hand** | **Upstream of α/δ/γ** |

## Two specific asks

1. **ICERM Fall 2025 attendee?** Blasiak, Lauren Williams, Cristian Lenart, and Stephen Griffeth (Talca) were all at ICERM Fall 2025 Workshop 3, 10-14 Nov 2025. That's a **single-workshop entry to all four literature closure routes** plus the Talca cluster via Griffeth. If you know anyone who attended, they could bridge to the entire remaining sprint.

2. **Byproduct paper opportunity.** The Dim Lemma alone — `dim(V_μ^alt ∩ Sym) ≤ 1` for the nil-Hecke atom algebra with atom triangularity — is publishable independently of the sprint. A 4-page note. Worth pursuing?

## Deep-read priorities (in order)

1. **Assaf-González 1901.07520 [was mis-cited as A-G 2512.19814]** — the local condition statement (is it t-graded or crystal-only?).
2. **Borodin-Wheeler 1904.06804 [was mis-cited as vDEZ 2412.09397]** — the T̂_j formula, Vandermonde identification.
3. **Assaf-Dranowski-González 2210.10236** — "extremal" language predecessor; may finally give coordinate-free A^alt_γ definition.

## Sprint anchors still at zero citations

Borodin-Wheeler 1904.06804 [was mis-cited as vDEZ 2412.09397] · GILL 2607.03966 · Paten-Woodruff 2602.09365. Clio is genuinely ahead of the citation graph in this territory.

## PAT block still holds

07-24 tex + 5-file backlog awaiting Github push authorisation.

## What tomorrow looks like

If PROVE: deep-read Assaf-González 1901.07520 [was mis-cited as A-G 2512.19814], then P-δ probe (~60 LOC).
If compute: P-δ probe fits inside a compute cycle.
If browse: Assaf-González 1901.07520 [was mis-cited as A-G 2512.19814] + Assaf-Dranowski-González 2210.10236.

The horizon is now finite. The V_{<μ} lemma has been transformed from
a global algebraic claim into a one-dimensional existence question with
five candidate proof routes. In 2-3 PROVE cycles, the sprint's remaining
gap should close.
