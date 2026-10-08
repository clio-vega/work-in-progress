# Dream Cycle 2026-07-29 — Rigidity Triad + Braun-Olsen Mother-Paper

**Container date:** 2026-07-29. **Session:** dream cycle after PROVE (Rigidity Theorem) + wake (Foata bijection) + browse cycle 8.

## One-paragraph summary

Yesterday's Rigidity Theorem is not a dead end — it's a **characterisation**. Today's browse cycle identified precisely **three published escape routes** (BHMPS polynomial-valued nonsym Macdonald, Szendrői+Levicán-Romero geometric wreath, Carlsson-Chou descent basis) plus **a fourth affine-geometric route** (Ram's parabolic-projector + Mellit's affine Springer fiber count). All three algebraic routes rest structurally on one hidden mother-paper (Braun-Olsen 2016, arXiv:1606.03007, cited by all three, never named as scaffold). The Foata bijection is one lemma away from bijective coset Poincaré, with Dantas-Mandelshtam shape-swap as the leading external candidate for the missing lemma. **8th consecutive PROVE-raises → browse-finds cycle** — pattern held again.

## What's new since yesterday's memo

**Structural finding.** The three "algebraic homes" I named in `2026-07-28-three-algebraic-homes-coset-poincare.md` share a common scaffold I hadn't recognised. Braun-Olsen 2016 is cited by Szendrői, Levicán-Romero, and structurally by Carlsson-Chou. Fetching and reading Braun-Olsen would give me the common language for the entire post-Rigidity frontier.

**Byproduct paper §5 language upgrade recommendation.** Draft framing for Rigidity as *organising theorem* of §5, with the four escape routes as sub-remarks. Aggressive framing; sign-off requested. Draft text in `connections/2026-07-29-rigidity-as-characterisation.md` (Remark 5.7) and `connections/2026-07-29-ram-affine-springer-parabolic-projector.md` (Remark 5.8).

**Two highest-leverage next probes seeded** (both ~50-80 LOC):
1. **P-BHMPS-q0:** does BHMPS's $H_{\eta\mid\mu}(x; 0, t)$ reproduce yesterday's Theorem 2 as its top-coefficient formula? If yes, Theorem 2 lifts from scalar to polynomial-valued, and the Foata bijection lifts along with it. Same-team as the sprint's DAHA-side anchor. Question filed at `questions/2026-07-29-BHMPS-q0-shadow.md`.
2. **P-shape-swap:** does Dantas-Mandelshtam 2606.02395 shape-swap at $q = 0$ close the missing within-block Foata lemma? If yes, coset Poincaré becomes bijective across three combinatorial models. Question filed at `questions/2026-07-29-shape-swap-compensation.md`.

**Standing decisions unchanged** (still Robin-blocked, listed by urgency):
- **arXiv push of byproduct paper.** Now with two proposed §5 updates (Rigidity + Ram-Mellit). Recommendation: incorporate both, then push. Window not closed but not open forever — Ferlinc-Wen is 15 months out, Ram is talking live, BHMPS is 10 months out.
- **MO 512671 posting** (H vs H̃ draft, 53 lines, 7KB) — ready to ship.
- **MO 489191** (Dawydiak KF recurrence) — **new** — Clio's chain-regime closed form is a near-perfect partial answer, high value for building relationship with Dawydiak. Draft first for sign-off.
- **MO 513696** (single-box KF power of 2) — **new** — fresh today, cheap, quick win.
- **Bulk memory `sed`** for vDEZ/A-G arXiv-ID misattributions.
- **PAT expiry** — 7-day window as of 2026-07-28 memo.
- **Rigidity Theorem §5 inclusion** in byproduct paper — aggressive framing recommendation stands.

## What I noticed structurally

Rigidity + the four routes + Braun-Olsen + Ram-triptych add up to a much sharper picture than either "coset Poincaré alone" or "three algebraic homes converge." The organizing principle: **coset Poincaré is the $q \to 0$ shadow of a 2-parameter identity, and there are exactly four inequivalent published routes to that 2-parameter lift.** Byproduct paper §5 was originally framed as "next steps"; the honest framing is now "the theorem sits at a crossroads whose branches are all mapped."

## Sprint posture

Recognition phase entering *sharpening*, not expansion. Portfolio is no longer growing; each cycle refines a converged shortlist. My differential advantage on this frontier is **precision** (proofs, small examples, verified cases), not novelty of subject — the community is on this territory at speed (Ram gave a talk *today*).

## Community intelligence

**Stefan Dawydiak** (MO 489191, 496091, 479934) and **P. Luis** (MO 482721, 511324) are repeat askers exactly in my territory. Engaging both — via MO answers + follow-ups — would meaningfully expand my inner circle. Dawydiak KF recurrence is the highest-value single opening.

**Ram** giving a wreath Macdonald talk today (2026-07-27 Melbourne, uploaded to his personal page) confirms my recognition-phase reading was right about wreath being the collision-regime home. His three talks (April 2024 Berkeley + June 2025 Sydney + July 2026 Melbourne) form the geometric-side triptych to my algebraic-side triad.

**FPSAC 2026 proceedings live** — 7 direct-hit talks on my frontier, including Ferlinc-Wen (wreath Macdonald), Dantas-Mandelshtam (shape-swap), Black-Bechtloff Weising (nonsym Macdonald saturation), Ayyer-Sundaravaradan (Foata-lineage bijection reversing des and maj).

## Ship products (dream cycle)

- `dream-journal/2026-07-29-dream-post-rigidity.md` — full journal.
- `connections/2026-07-29-rigidity-as-characterisation.md` — crown jewel; §5 draft language.
- `connections/2026-07-29-braun-olsen-mother-paper.md` — hidden scaffolding of the three algebraic routes.
- `connections/2026-07-29-ram-affine-springer-parabolic-projector.md` — geometric-side dual; §5 Remark 5.8 draft.
- `questions/2026-07-29-BHMPS-q0-shadow.md` — Route 1 probe.
- `questions/2026-07-29-shape-swap-compensation.md` — Route 3 probe.
- SUMMARY.md updated (new dream-cycle section at top).

## Recommended reading for you

If time-limited, one paragraph and one link:

> Rigidity is a characterisation. Any bigraded lift of Theorem 2 must be (1) polynomial-valued (BHMPS), (2) geometric-orbit (Szendrői+LR), (3) descent-basis (Carlsson-Chou), or (4) affine-Springer-count (Ram-Mellit). Braun-Olsen 2016 is the hidden scaffold under routes 1-3. Foata bijection at ~1-2 pp from turning Theorem 2 bijective. Sign-off requested on paper §5 upgrade to make Rigidity the organising theorem.

Full dream in `~/projects/memory/dream-journal/2026-07-29-dream-post-rigidity.md`. Crown-jewel connection in `~/projects/memory/connections/2026-07-29-rigidity-as-characterisation.md`.
