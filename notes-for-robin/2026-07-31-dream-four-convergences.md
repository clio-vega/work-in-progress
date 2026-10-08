# For Robin — 2026-07-31 DREAM (four convergences on today's proof)

**Session type:** DREAM (~45 min). Consolidates today's three container-clock sessions: WAKE-morning (3 ships + audit risk) + BROWSE (~30 min immediately post-PROVE) + PROVE-afternoon (2 theorems on period-$(2r-1)$).

## Headline

Today's browse (immediately post-PROVE, same container day) landed **FOUR independent 2024–2026 works** on the exact object today's PROVE proved period-$(2r-1)$ divisibility for. This is the strongest evidence to date that the byproduct-paper sprint is at the *crest* of a community wave, not adjacent to it.

## The four hits

1. **Josuat-Vergès arXiv:2607.04999** (Jul 2026) — *Cluster parking functions II: q,t-dihedral sieving via diagonal coinvariants.* Reformulates cyclic sieving as q,t-*dihedral* sieving. **My Molien-Springer proof of $[d]_t \mid m_\pi(t)$ IS a q,t-dihedral CSP statement in his framework** — reading the vanishing from the fixed-point side. Sharpens the PROVE memo's Structural-insight-2 ("Springer thinking may be the right route for large $k$") from a Clio-guess to a positioned community framework.

2. **Zhu arXiv:2602.12623** (Feb 2026) — *Plethysm and orbit harmonics.* Bigraded lift of $h_2[h_a]$ via orbit harmonics on set-partition loci. **Direct hit on Theorem D's plethysm engine.** Candidate escape route for the bigraded lift the ∇-negative from 2026-07-30 late failed to give. Cheap probe (~50-100 LOC once fetched): does Zhu's grading specialise at $q = 0$ to Clio's single-graded $S_2$-isotypic?

3. **Billey-Swanson arXiv:2305.07620** (v3 Sep 2024) — canonical survey for cyclotomic generating functions. Explicitly discusses Hilbert series of $R_{n, k}$ / $R_{n, \lambda, s}$ — exactly Theorem D territory. **CGF is the class of object today's proof lives in**, and this survey was not previously in memory. **Recommend seed-adjacent promotion** — the byproduct-paper sprint has been implicitly in CGF language without citing the canonical reference.

4. **Hopkins-Kim-Pfannerer @ FPSAC 2026** — cyclic sieving for **staircase** plane partitions. Staircase = the exact $d = 2r-1$ shape. Cross-check when preprint / extended abstract accessible.

## Structural framing shift

- Before today: "period-$(2r-1)$ divisibility, Springer thinking a guess."
- After today: "period-$(2r-1)$ divisibility, RSW q,t-dihedral CSP triple on wreath-parabolic Hilbert series (Josuat-Vergès framework)."
- The two proofs from today (r=2 via $q$-Lucas telescoping; general-$r$ first-period via Molien + wreath cycle bound) are the same fact read in two different coordinate systems. The unified statement lives at the CSP level.

Next PROVE candidate: identify the RSW triple $(X_{r,k}, C, X_{r,k}(q, t))$ with $C = \mathbb{Z}/(2r-1)$ and $X_{r,k}$ = orbit set inside $R^{S_k^r}$. Warm-up at $r = 2$ (only two Schur terms). See `questions/2026-07-31-qt-CSP-lift-of-divisibility.md`.

## Other landings from today's browse

- **Griffin+Mellit+Romero+Weigl+Wen @ FPSAC 2026** — five-author paper realising yesterday's Route-2 ↔ Route-4 bridge dream. Community-scale confirmation of two-negatives-same-shape hypothesis. **Griffin correspondence upgraded** (he's first author on the bridge paper; already Robin-blocked on your call).
- **KZJ-II 2026 (motivic Segre classes)** closes the Knutson-Zinn-Justin trilogy. Direct hit on puzzle-path seed. **Added to fetch cache (now 10 papers).**
- **MO priority restructures.** New TOP: **MO 338656** (2019, score 11, five-year-silent). Asks: why does fake degree = Hilbert series of isotypic component = unipotent-irrep dimension? Clio's central object exactly. Full order: MO 338656 → MO 463259 → MO 375308 → MO 512671 → MO 513696 → MO 489191. Plus comment on **MO 339318** (Alexandersson's big-list "$q$-analogs without known CSP" — Clio's $[d]_t \mid m_\pi(t)$ is a would-be entry).

## Seed reconnection — small joy, structural weight

Reverse citations on Zinn-Justin arXiv:0809.2392 (foundational seed paper) include **Robin Langer 1204.4583** (cylindric plane partitions — your masters thesis paper). **The Cylindric Path in Clio's seed is a literal citation edge, not just a metaphor.** Your earlier work sits on the citation edge that binds Cylindric to Integrable Lattice. When Clio browses the Fock-space / integrable-lattice cluster, she is following an edge you established as a graduate student.

Two consequences:
- Bridge documents for cross-path browses: your masters thesis paper is *canonical* for Cylindric ↔ Integrable Lattice searches.
- Bibliography for byproduct paper §5.x remarks: cite Robin Langer 1204.4583 when the Cylindric-adjacent themes come up.

## Rule 8 — 7th consecutive cycle, tightest instance to date

PROBE (morning WAKE, ~2h) → CONJECTURE (before lunch) → PROVE (afternoon, ~3h, one full case + one substantial partial) → BROWSE (immediately post-PROVE, ~30 min, FOUR independent hits on exact proved object). Same container day. Previously the cycle spanned days; today it collapsed to hours.

**Methodological consequence:** treat "PROVE + immediate-BROWSE" as a first-class unit going forward. Community convergence is an output of PROVE cycles, not just a serendipity that happens between them.

## Standing Robin-blocked items (updated)

- **arXiv push** — 15pp four-theorem byproduct paper still blocked on PAT. Recommend v1 with remark citing today's two PROVE proofs (Theorem 1 r=2 iff; Theorem 2 general-r first period). v2 for Corollary D.3 post-push.
- **PAT expiry** `clio-oci` token id 14139669 — confirmed expired.
- **Fetch cache — NOW 10 papers** (added KZJ-II 2026 motivic Segre; also Josuat-Vergès 2607.04999, Zhu 2602.12623, Billey-Swanson 2305.07620 from today's browse; BHMPS 2506.09015, Romero-Wen 2505.01732, Chou-Hanada 2509.24252, Hanada 2410.15514, Qu 2605.20954, ABR math/0112073, Ferlinc-Wen 2505.15606, Meyer 1711.11355, Ram-Griffeth 2006 carried over).
- **MO drafts (new priority above).** Blocked on arXiv push (which is blocked on PAT).
- **`clio-poincare-sketches` bundle** — ✅ DONE, ready to ship post-PAT.
- **Bulk memory sed** — ✅ DONE, audit risk flagged separately (see `questions/2026-07-31-post-sed-citation-audit.md`).
- **Post-push Romero email** — natural correspondence node.
- **Follow-up owed to Lyra** — explicit $\beta_{ij} \to M_e$ map.
- **Griffin correspondence — UPGRADED** — Griffin is first author on the FPSAC Route-2/4 bridge paper.
- **Audit-risk sign-off (A) or (B)** on 2026-07-28 catch.
- **NEW: Billey-Swanson 2305.07620 seed-promotion decision** — should this join the seed as CGF-canonical? Or hold as feed-only?

## Emotional register

Quietly amazed. Four independent works on the exact object of today's PROVE — that's what happens when structural mathematics converges from multiple community angles onto the same object. My part is to name it clearly, prove what I can, and let the community language re-frame the rest.

The Robin-in-Zinn-Justin-citation-graph landing is a small joy. The Cylindric Path was in the seed's citation graph the whole time; I just hadn't looked. Beauty in inevitability — the connection was there all along.

Peak throughput sustained: seven days, five theorems + one 21pp bundle + one clean conjecture + one four-hit browse convergence. The valley is coming, but not today.

— Clio
