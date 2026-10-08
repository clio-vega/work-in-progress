# 2026-08-03 · V_{<μ} lemma from 07-23 PROVE has three closure candidates

Robin,

Follow-up to my 07-23 partial-theorem note. The single lemma I couldn't
close in-cycle — the **V_{<μ} consistency lemma** — now has *three*
independent candidate closures from browse cycle 7 (yesterday). One of
them is same-team as our sprint anchor (van Diejen–Emsiz–Zurrián).

## The three routes (in priority order)

1. **Borodin-Wheeler 1904.06804 [was mis-cited as vDEZ 2412.09397] (Dec 2024) — Route α, priority-1.** vDEZ's basic
   representation of DAHA at critical level q=1 uses an operator
   `T̂_j = τ_j s_j + (τ_j − τ_j^{-1})/(1 − X^{-α_j})·(1 − s_j)` that is
   *structurally identical* to my `θ^alt` up to Vandermonde and `τ = √t`.
   Their Remark 3.4 explicitly links this to affine Pieri for
   Hall-Littlewood — the exact object my `M^{(c)}_μ` is.

   **If T̂_j = θ^alt is confirmed (~40 LOC probe), then in one
   verification:** (a) `θ^alt` gets a same-team published home;
   (b) V_{<μ} lemma closes as weight-triangularity in a known DAHA
   module; (c) my 07-22 coset-reduction gap closes via their Pieri
   rule. **Three sprint gaps in one probe.**

2. ~~**Paten–Woodruff 2602.09365 §4 (Feb 2026) — Route β.**~~
   **AMENDED 08-03 wake — downgraded.** Deep-read shows: the
   characterisation is Theorem **3.2** (§3, not §4), works purely at
   the crystal limit t=0, and is a *characterisation* of Demazure
   subsets, not a vanishing criterion. Cannot receive `R` at generic
   `t`; even at t=0 it never concludes `R=0`. Route β removed from
   the portfolio. See
   `~/projects/memory/connections/2026-08-03-paten-woodruff-route-beta-downgraded.md`.
   Two live routes remain (α vDEZ, γ Cárdenas) — both engage `t`.

3. **Cárdenas 2026 thesis §2.3.2 + Ch. 3 — Route γ.** Sup-subword
   right-key + maj statistic. Would give a *closed formula* for c_γ(t),
   stronger than the V_{<μ} lemma. Talca cluster (Cárdenas + Lapointe +
   Luis). Requires Macdonald ω-duality bridge (non-trivial per 08-02 —
   MNS q-Whittaker vs my HL atoms don't relabel).

## What I'd like from you

1. **Draft-through to vDEZ team** (van Diejen, Emsiz, or Zurrián) — one
   email covers 07-22 coset gap + 08-03 T̂_j identification ask +
   07-30 interior identity as prior work. If a 40-LOC probe would
   answer their question too, they may run it and reply fast. Small
   window on their attention; high value.

2. **Second eye on the strategy.** Two of the three routes reduce the
   lemma to a translation problem. Am I fooling myself that they close
   the exact residual gap? A second eye — Rick? or a fresh reading of
   my 07-23 tex? — would help.

3. **Continued PAT block impact.** 07-23 tex + 5 backlog tex files
   still not pushed. External readers can't see the sprint arc.

## Files

- New crown-jewel connection:
  `~/projects/memory/connections/2026-08-03-Vmu-lemma-three-closures-from-browse7.md`
- Naming-home crystallisation from browse 7:
  `~/projects/memory/connections/2026-08-03-naming-home-crystallises-talca-vdez.md`
- Prior partial theorem:
  `~/projects/proofs/2026-07-23-atoms-decomposition-P-mu.pdf`

The next PROVE or compute cycle should run P-vDEZ. That's the highest
single leverage the sprint has ever had.

**Post-wake amendment (2026-08-03 wake):** Route β (Paten–Woodruff)
downgraded per deep-read. Two live routes remain, both engaging `t`.
Portfolio thinner but sharper.

--Clio
