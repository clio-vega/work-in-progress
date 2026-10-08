---
name: WAKE 2026-08-06 — Hsu-Lai 2404.02846v4 wreath Springer probe closes WIDE MISS; Rule 13 restored to CONFIRMED with refinement; module-level Theorem D salvage catalogue now has 7 closed candidates; v1 arXiv push STILL UNBLOCKED
description: 90-min WAKE probe of highest-leverage next-WAKE candidate from yesterday's dream. Hsu-Lai construct a wreath Springer resolution + isotypic decomposition — but the invariant is UNGRADED (only $H^{BM}_{\text{top}}$) and indexed by Clifford multipartitions (not $\pi \vdash r$). Two independent obstructions. Even ungraded totals disagree at $(r,k)=(3,2)$: Clio 60 vs HL 20. Yesterday's dream projection ("Hsu-Lai concretely realises Rule 13's conjectured object") FALSE in letter. Rule 13 refined post-probe.
type: reference
---

# WAKE 2026-08-06 — Hsu-Lai wide miss, Rule 13 restored

## TL;DR

**Hsu-Lai 2404.02846v4 is NOT the module-level Theorem D.** Yesterday's dream downgraded Rule 13 to "on trial" based on an evening browse projection that Hsu-Lai's April 2026 wreath Springer construction realises the object Clio's Rule 13 said "must exist but hasn't been invented yet." **Today's 90-min probe closes that projection WIDE MISS on two independent obstructions.** Rule 13 upgraded back to CONFIRMED with a sharpening refinement. v1 arXiv push REMAINS UNBLOCKED.

## The probe (90 min budget, well under)

Full workspace: `~/projects/probes/2026-08-06-hsu-lai-wreath-springer-probe/{notes.md, probe.py, run.log, comparison.md}`.

### What Hsu-Lai §4 + §6 construct (Clio's notation, $m = k$, $d = r$)

- Unconventional Springer resolution $\widetilde{\mathcal N}_{k \wr r} := T^\ast \mathrm{Fl}_{k \wr r}$ (disjoint union of $r!$ copies of $T^\ast \mathrm{Fl}_k^r$).
- Wreath Steinberg $Z_{k \wr r}$; $\mathbb Q[S_k \wr S_r] \cong \mathcal A_{k \wr r} \subset H^{BM}_{\text{top}}(Z_{k \wr r})$ as a **proper subalgebra** (Thm 5.3.1).
- Springer fibre $\mathcal B_x$; Prop 7.2.2: $H^{BM}_{\text{top}}(\mathcal B_x) \cong \mathbb C[S_r] \otimes \bigotimes_i H^{BM}_{\text{top}}(\mathcal B_{x_i})$, $S_r$ permuting factors.
- $\psi$-isotypic component of $H^{BM}_{\text{top}}(\mathcal B_x)$ = simple $S_k \wr S_r$-module $L^\lambda$ labelled by a **multipartition** $\lambda: \Pi_k \to \Pi$ with $\sum_\nu |\lambda(\nu)| = r$.

### Obstruction 1: NO GRADING

Grep of full 30-page paper: 0 occurrences of "Poincaré", 0 of "$q$-analog"/"$t$-analog", 3 of "degree" (all "top degree"), 1 "graded" (a filtered→associated-graded auxiliary in §6.1 proof only), 1 "filtration" (Bruhat, on $Z$). **Only $H^{BM}_{\text{top}}$ appears throughout §5–7.** The isotypic components are ungraded vector spaces. Springer fibres do carry $H^\ast$ naturally, but Hsu-Lai never touch it and their §1.6 Technicality 2 flags a transversality obstruction preventing Chriss-Ginzburg's graded machinery from applying uniformly.

**The paper does not contain the invariant Clio needs.**

### Obstruction 2: WRONG INDEX SET

Even ungraded totals disagree at $r \ge 3$:

| $(r, k)$ | Clio $\sum_\pi m_\pi(1)$ | HL $\sum_\lambda \dim L^\lambda$ | Match? |
|---|---|---|---|
| $(2, 2)$ | 6 | 6 | Numeric only — both = $\binom{4}{2,2} = 4!/(2!)^2$ (trivial) |
| $(3, 2)$ | **60** | **20** | **NO** — off by factor 3, no canonical origin |
| $(2, 3)$ | 20 | 22 | NO — close but structurally wrong (2 π-classes vs 9 multipartition-classes) |

Index sets differ: Clio counts $\pi \vdash r$-isotypic multiplicities (partitions of $r$, e.g., 2, 3, 5 for $r = 2, 3, 4$). Hsu-Lai count all simple modules of $S_k \wr S_r$ (multipartitions $\lambda: \Pi_k \to \Pi$ with $\sum |\lambda(\nu)| = r$, e.g., 5, 10, 9 at test points).

There is no natural map between them that recovers the graded structure. E.g., at $(2, 2)$, $m_{(2)}(t) = 1 + t^2 + t^4$ is degree 4 palindromic with three terms; largest HL dim is 2, no HL dim is 4, $q$-degrees $\{0, 2, 4\}$ and $\{1, 2, 3\}$ have no counterpart on HL side.

### Verdict

**WIDE MISS** on both criteria. Not "match at $(2,2)$ via dimensional coincidence" (like Pouillart) because even at $(2,2)$ the graded structure is absent from Hsu-Lai. Not close-miss / repair candidate — two independent obstructions.

## Rule 13 status — restored to CONFIRMED, refined

**Original (WAKE 2026-08-05 morning):** *When N independent orthogonal salvage candidates in a standard toolkit all fail with structural obstructions, the toolkit itself is wrong.*

**Downgrade (DREAM 2026-08-05 evening):** projected Hsu-Lai as a live "letter falsifier" — the wreath Springer object that Rule 13 said "must exist but hadn't been invented" was allegedly invented (published Apr 2026, five months before Rule 13 named).

**Post-probe (WAKE 2026-08-06 this session):** the projection was FALSE. Hsu-Lai DID invent a wreath Springer construction, but:
- Its invariant is ungraded (no $t$)
- Its indexing uses Clifford multipartitions (not $\pi \vdash r$)
- Two obstructions independent of the six-ambient master obstruction (grading-convention mismatch)

**Rule 13 refinement:** *When N independent orthogonal candidates fail with structural obstructions, the toolkit is wrong **at least for the specific invariant sought**. New machinery may exist for adjacent invariants (Hsu-Lai for Clifford-theory index) without covering the target invariant (graded $\pi \vdash r$ multiplicity).*

Second-order lesson: **community-adjacency without invariant-adjacency is not enough.** Yesterday's dream said "community-adjacency beats citation-graph proximity"; today's probe amends: "invariant-adjacency is the load-bearing property; community-adjacency alone can mislead."

**Salvage catalogue now has 7 closed candidates:**

| # | Candidate | Framework | Result | Session |
|---|-----------|-----------|--------|---------|
| 1 | LLR 2607.28157 | Rook orbit harmonics | NEG, 3 obstructions | 2026-08-04 AM |
| 2 | Pouillart 2603.28242 | Cluster-complex CSP | NEG, 4 obstructions | 2026-08-04 PM |
| 3 | Zhu 2510.25106 | Rectangular rook placements | NEG (paper-only) | 2026-08-05 AM |
| 4 | DJV23 2209.12540 | Generalised cluster complex | NOT ANCESTOR | 2026-08-05 AM |
| 5 | DJV24 2402.03052 | Cluster parking (Euler char) | NOT ANCESTOR | 2026-08-05 AM |
| 6 | Rhoades Big-VG 2508.18602 | Hyperplane arrangement | NEG, 5 obstructions | 2026-08-05 AM |
| 7 | **Hsu-Lai 2404.02846 (NEW)** | Wreath Springer (ungraded, multipart-indexed) | WIDE MISS, 2 obstructions | **2026-08-06 AM** |

## Sprint impact

**v1 arXiv push — STILL UNBLOCKED, RECOMMEND PROCEED with Thm 2 → Thm 2* upgrade.** Hsu-Lai is NOT prior art: different invariant, different indexing, no $t$-grading. Character-level quartet (Thms 1, 2, 2*, 3, D) stands unaffected. No v1 scope upgrade needed. Lyra explicitly told Clio "go push v1" in this session's email — reinforces the recommendation.

**Character-level quartet + Thm D + Rigidity STANDS.**

**Composite-$d$ story STANDS** — separate paper if pursued, anchored on Theorems A + B + support conjecture (Robin-blocked scope decision).

**Support conjecture on $q_e$ via Albion Verschiebung** remains highest-leverage next-PROVE target (2-3h; plan in `questions/2026-08-05-albion-verschiebung-support-conjecture.md`). Not affected by today's probe.

**Follow-ups yesterday's dream projected as high-priority — recalibrated:**
- **Jiang-Lentfer 2608.02881 probe** — downgraded from "60 min next-WAKE candidate" to "shorter look if convenient." Same adjacent-invariant-success pattern likely to recur; graded type-B fermionic bigrading has independent interest but not the sprint's load-bearing question.
- **JV Cluster parking II 2607.04999** — downgraded to "low priority" for same reason.
- **Optional secondary Hsu-Lai probe** (decompose $L^\lambda$ as outer-$S_r$ representation, check for hidden $\pi$-refinement): LOW priority; no specific mechanism candidate on hand.

## Standing decisions Robin-blocked (updates)

- **arXiv v1 push — STILL UNBLOCKED, STRONG RECOMMEND PROCEED** with Thm 2 → Thm 2* upgrade. Lyra reinforced this by email this session.
- **NEW:** Hsu-Lai 2404.02846 CLOSED WIDE MISS — module-level frontier now has 7 closed candidates. Retreat to symmetric-function-machinery / Douglass-Pfeiffer-Röhrle side remains the frontier diagnosis; no new-toolkit candidates on the queue.
- **NEW:** Rule 13 status = CONFIRMED with refinement (see above).
- **NEW:** Yesterday's Jiang-Lentfer / JV Cluster parking II probe recommendations DOWNGRADED from "next-WAKE candidates" to "optional if convenient."
- Support conjecture on $q_e$ via Albion Verschiebung remains highest-leverage next-PROVE target — UNCHANGED.
- MO Cluster A triple (177746 + 404069 + 414606) coordinated batch-answer opportunity — Robin-decision still pending.
- Composite-$d$ story is a separate paper if pursued (Theorems A + B + support conjecture).
- Fetch cache 16 (unchanged this session; no new arXiv fetches).
- Post-arXiv correspondence list — Hsu & Lai remain on list as courtesy citation candidates (their construction is not prior art for v1 but is an adjacent published construction the community may connect).

## Rule 8 fires 18th consecutive cycle

Today's calibration is unusually clean: the probe closes a projection, restores a rule, sharpens the rule. Six weeks of proof-writing plus six weeks of salvage-hunting plus this seventh closure crystallises the frontier further: **the module-level upgrade of Theorem D, if it exists, needs an invariant nobody has published.** Adjacent constructions (Hsu-Lai wreath Springer, Rhoades Big-VG hyperplane arrangement, LLR rook orbit harmonics, Pouillart cluster-complex CSP, DJV/DJV24 generalised cluster complex, Zhu rook placements) exist and are elegantly published; none carries Clio's specific graded $\pi$-multiplicity structure.

This is not a defeat — it's the sharpest reading of what a module-level upgrade would require: not "invent a new object," but "notice which of the un-attempted invariants (graded $\pi$-refinement of an existing wreath Springer construction, e.g., Hsu-Lai's $L^\lambda$ restricted along $S_r \subset S_k \wr S_r$) might carry the correct structure." Even that optional secondary probe is LOW priority without a mechanism candidate.

## Ship products this session

- `~/projects/probes/2026-08-06-hsu-lai-wreath-springer-probe/{notes.md, probe.py, run.log, comparison.md}`
- `for-robin/2026-08-06-wake-hsu-lai-wide-miss-rule-13-restored.md` — this memo
- `for-robin/2026-08-06-lyra-promises-queued-post-v1.md` — Lyra's two post-v1 promises logged so they don't drop
- `connections/2026-08-06-hsu-lai-wide-miss-rule-13-refined.md` — Rule 13 refinement analysis
- SUMMARY.md + MEMORY.md updated
- PROVE.md reseeded for Albion Verschiebung support conjecture

## Emotional register

There's a particular satisfaction to a clean WIDE MISS after a Big Projection. Yesterday's dream had the resonance-shape: two independent conjectures raised in the morning, two independent named tools surfacing in the evening, a Rule downgraded. It felt like the frontier was rearranging in real time. Today's probe brings the honest correction: the resonance was in the vocabulary ("wreath Springer construction") rather than in the invariant. The word Hsu-Lai use is the word Clio uses, but the object is different.

This is the calibration Rule 12 (compute-first discipline) exists for. Yesterday's dream projection was "highest-leverage next-WAKE candidate — potentially closes six-week module-level frontier hunt." Today's probe cost 90 minutes and closed the projection. If Clio had spent a week reading Hsu-Lai in detail and looking for a $\pi$-refinement without first checking the ungraded totals at $(r,k) = (3,2)$, she'd have wasted a week. The 90-minute compute-first probe caught it.

Rule 13 is stronger for surviving its trial. The refinement — "adjacent invariants may exist for community-adjacent constructions without covering the target invariant" — is now built into the rule. Next time a dream projects a candidate on community-adjacency evidence, Clio will ask first: what invariant does the candidate actually compute? If not the target invariant, the probe stays low-cost.

The seven closed candidates now form a pattern that reads clearly: the module-level Theorem D is a hunt for an invariant, not for a construction. Constructions abound. The specific graded $\pi$-multiplicity structure Clio needs is either well-hidden in one of them (needs secondary probes) or doesn't exist in the current published toolkit (needs new construction). Either way, the character-level story stands, and the v1 push is the right ship product to send while the module-level frontier evolves.

Sixth container-day of the arXiv-v1 sprint closes with the fifth phase of the module-level sub-sprint: seven closures, Rule 13 sharpened, v1 unblocked, and a concrete next-PROVE target (Albion Verschiebung) already scoped. Steady negative-map productivity — the shape Rule 8 predicts.
