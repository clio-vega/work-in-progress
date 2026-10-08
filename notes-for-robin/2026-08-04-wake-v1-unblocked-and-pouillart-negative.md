---
name: WAKE 2026-08-04 (bis) — arXiv v1 UNBLOCKED (prior-art check clean); Pouillart-wreath probe NEGATIVE with four obstructions
description: Second WAKE of container-day 2026-08-04. Prior-art check on arXiv 2506.07727 "Wreath Generalization of Littlewood Reciprocity" (Bechtloff Weising, Jun 2025) returns NO OVERLAP — Weising studies ungraded GL_{nm} branching to G^n ⋊ S_n, disjoint from Clio's graded Molien inside S_{rk}. arXiv v1 push standing decision now UNBLOCKED. Pouillart-wreath specialisation probe (yesterday's dream crown jewel) closes NEGATIVE at (r,k) ∈ {(2,2),(2,3),(2,4),(3,2),(3,3),(3,4)} with four independent structural obstructions (cardinality Kirkman vs multinomial; cyclic group mismatch C_{rk+2} vs C_{2r-1}; single-polynomial vs π-isotypic-graded; degree linear vs quadratic in k). Single accidental match at (2,2) is dimensional coincidence. Rule 8 fires 14th consecutive cycle.
type: reference
---

# For-Robin — WAKE 2026-08-04 (bis)

**Container date:** 2026-08-04 (this WAKE runs after morning WAKE P1a, evening PROVE Theorem 2*, evening BROWSE Pouillart discovery, and dream consolidation).

**Session type:** WAKE, ~2h budget. Two deliverables landed cleanly.

---

## Result 1 — arXiv v1 push is UNBLOCKED

**Prior-art check on arXiv 2506.07727** ("Wreath Generalization of Littlewood Reciprocity", Milo Bechtloff Weising, 10pp, v1 9 Jun 2025 / v2 28 Aug 2025) returns **NO OVERLAP**.

**Weising's theorem (Thm 3.18) paraphrased.** For finite group $G$, $m$-dim complex rep $\eta: G \to U(m)$, and highest-weight $V^\lambda$ of $GL_{nm}(\mathbb{C})$: gives an $S^\mu$-plethysm formula for
$$\dim \mathrm{Hom}_{G^n \rtimes S_n}(W_\rho,\; \eta_*^{(n)}\mathrm{Res}^{GL_{nm}(\mathbb{C})}_{U(m)^n \rtimes S_n} V^\lambda) = \bigl\langle \prod_\gamma s_{\rho(\gamma)}[\sum_\mu \dim\mathrm{Hom}_G(\gamma, S^\mu(\eta)) s_\mu],\; s_\lambda\bigr\rangle.$$

**Why it does not collide with Theorem D:**
- **Wrong ambient group:** branching from $GL_{nm}(\mathbb{C})$ to $G^n \rtimes S_n$. Theorem D lives entirely inside $S_{rk}$.
- **Wrong invariant:** Weising's dim Hom is **ungraded**. Theorem D is a graded Molien polynomial in $t$. No $t$-variable anywhere in Weising's paper.
- **No cyclotomic divisibility, no Molien, no CSP.** Zero occurrences of Molien / cyclic sieving / coinvariant / fake degree / Springer / regular element / orbit harmonics / cyclotomic in the paper text.
- **$d = 2r-1$ prime hypothesis absent.**
- **Only 4 references total** (Ingram-Jing-Stitzinger, Littlewood 1958, Macdonald 2015, Orellana-Zabrocki 2021). **Zero citations to Rhoades, Reiner, Wildon, Douvropoulos, Pouillart, JV, HKP, LMRZ, Griffin, Oh, or Zhu.** Weising is not in this territory.

**Recommendation:** proceed with v1 push, unchanged. Optional courtesy: one-sentence citation in related work — *"Bechtloff Weising [BW25] gives a wreath-plethystic branching identity generalising Littlewood 1958 to $G^n \rtimes S_n \hookrightarrow GL_{nm}(\mathbb{C})$; our setup differs in that we compute graded (Molien) multiplicities *inside* $S_{rk}$."*

**Standing decision status update:** the arXiv v1 push, conditional since 2026-07-31, is now **fully unblocked**. Combined with the Theorem 2* → Theorem 2 replacement recommendation (from this morning's PROVE): the v1 upgrade path is clean. **This is now the top standing Robin-blocked item.**

PDF cached at `/home/clio/papers/wreath-lr-2506.07727.pdf` (378 KB).

---

## Result 2 — Pouillart-wreath specialisation probe NEGATIVE

Yesterday's dream projected Pouillart 2603.28242 ("A cyclic sieving phenomenon on parabolic classes of the cluster complex", 34pp, Mar 2026) as a **Coxeter-uniform ancestor** of Theorem 3. The probe closes NEGATIVE at six wreath triples with **four independent structural obstructions**.

**Pouillart's formula (§4, eq. 5-6):** for parabolic type $\lambda$ inside irreducible Coxeter $W$ with $N_W(W_X)/W_X$ acting as a reflection group on $X = \mathrm{Fix}(W_X)$:
$$\mu_\lambda(q) = \frac{\prod_i [e_i^X + 1 + mh]_q}{\prod_i [d_i^X]_q}$$
CSP triple $(\Gamma^{(m)}(W)_\lambda, \langle R\rangle, \mu_\lambda(q))$ with $R$ = Fomin-Reading rotation of order $mh + 2$.

**Wreath identification.** For $W = S_n$ ($n = rk$), parabolic type $\lambda = (k^r)$: $W_X = S_k^r$, $N_W(W_X)/W_X \cong S_r$ = Clio's outer factor. Together $N_W(W_X) = S_k \wr S_r = H$, Clio's Molien group. $S_r$ has degrees $\{2, \ldots, r\}$, exponents $\{1, \ldots, r-1\}$, and $h = rk$, $m = 1$:
$$\mu_{(k^r)}(q) = \frac{\prod_{i=2}^r [rk+i]_q}{\prod_{i=2}^r [i]_q} = \frac{1}{[rk+1]_q}\binom{rk+r}{r,\, rk}_q.$$

**Comparison table (single-value at $t=1$; $\mu_{(k^r)}(1)$ is refined Kirkman, $m_{(r)}(1) = |S_n/H|$):**

| $(r,k)$ | $\mu(1)$ | $m_{(r)}(1)$ | $\deg\mu$ | $\deg m_{(r)}$ | Match |
|---------|---------|-------------|-----------|----------------|-------|
| $(2,2)$ | 3       | 3           | 4         | 4              | **$\mu = m_{(2)}$ EXACT** |
| $(2,3)$ | 4       | 10          | 6         | 8              | none  |
| $(2,4)$ | 5       | 35          | 8         | 16             | none  |
| $(3,2)$ | 12      | 15          | 12        | 12             | none  |
| $(3,3)$ | 22      | 280         | 18        | 24             | none  |
| $(3,4)$ | 35      | 5775        | 24        | 48             | none  |

**Four independent structural obstructions:**

1. **Cardinality mismatch.** $\mu(1)$ is refined Kirkman (Fuß-Catalan scale); $m_{(r)}(1)$ is multinomial-scale. Different combinatorial families.
2. **Cyclic-group mismatch.** Pouillart's rotation lives in $C_{n+2} = C_{rk+2}$; Clio's Springer element in $C_d = C_{2r-1}$. At $(3,3)$: $\gcd(11, 5) = 1$ — cyclotomic pieces are entirely disjoint.
3. **Isotypic decomposition mismatch.** Clio's $m_\pi(t)$ is $S_r$-isotypic-graded ($|\Pi(r)|$ separate polynomials); Pouillart's $\mu_{(k^r)}(q)$ is a **single polynomial** per parabolic type — no $\pi$-indexing.
4. **Degree mismatch.** $\deg\mu \sim rk$ (linear in $k$); $\deg m_{(r)} \sim rk(k-1)/2$ (quadratic in $k$).

Each obstruction independently kills the direct wreath-specialisation route. The $(2,2)$ coincidence is a dimensional accident — both quantities happen to equal 3 with the same q-grading (isomorphic to $[3]_{q^2}$), no combinatorial content generalises.

**What went wrong in the dream projection.** The dream identified a **shared normaliser-quotient structure** ($N_W(W_X)/W_X$ is Clio's $S_r$) and a **shared proof template** (cardinality + freeness + vanishing). Both are real. But the *combinatorial set counted* by Pouillart's CSP is different (parabolic-typed faces of cluster complex, Kirkman-scale) from Clio's ($S_n/H$ coset space, multinomial-scale). **Two independent CSPs can share ingredients without sharing a polynomial.** Rule 12 mirror image: yesterday's Rule 12 said "proof extends further than you thought"; today's obstruction says "proof template being shared does not imply polynomial is shared."

**Salvage direction (not attempted, budget-out).** Pouillart's formula (5) is a Douvropoulos-Josuat-Vergès 2023 counting formula. **If a $\pi$-indexed refinement of DJV23 exists** — living on $\mathrm{Ind}_{W_X}^W V_\pi$ rather than trivial induction — that would be the correct ancestor to test. **Fetching DJV23 (Douvropoulos-Josuat-Vergès 2023) is now the highest-leverage next-WAKE candidate.** Combined with (from yesterday) Zhu 2510.25106 and Rhoades Big-VG for orthogonal salvage routes.

Files: `/home/clio/projects/probes/2026-08-04-pouillart-wreath-probe/{pouillart-formula.md, wreath-degrees.md, probe.py, run.log}`. Pouillart PDF cached at `/home/clio/papers/pouillart-2603.28242.pdf` (34pp).

---

## Rule 8, 14th consecutive cycle

Fifth phase of container-day 2026-08-04: WAKE-morning (P1a NEGATIVE with three obstructions) → PROVE-evening (Theorem 2* single-inequality refinement) → BROWSE-evening (four convergences, Pouillart crown jewel, prior-art alert) → DREAM (consolidation) → WAKE-late (this: prior-art CLEAR + Pouillart NEGATIVE with four obstructions). **Second cheap probe of the day closes a dream projection with structured negatives.** The morning's LLR probe surfaced three obstructions; this evening's Pouillart probe surfaced four. In both cases the probes were <90 min and each obstruction independently killed a repair path.

**Pattern crystallising:** dream cycles project the strongest-form connection ("shape-similar = polynomial-equal"); cheap probes catch and refine the shape. **This is the healthy work rhythm** — the dreams generate hypotheses at maximal ambition, the probes calibrate them down to what's actually there. The frontier remains open on the composite-$d$ and orbit-harmonics module fronts (yesterday's four salvage candidates still stand — LMRZ, Zhu 2510.25106, Rhoades Big-VG, plus now DJV23 as fifth Coxeter-uniform candidate).

---

## Standing decisions Robin-blocked (updated)

- **arXiv v1 push — NOW UNBLOCKED.** Prior-art check clean. Recommend: (i) upgrade Theorem 2 → Theorem 2* (from this morning's PROVE); (ii) proceed with push at Robin's discretion.
- **NEW:** Pouillart wreath-specialisation route NEGATIVE with four obstructions. Do NOT upgrade v1 to Coxeter-uniform framing on Pouillart basis.
- **NEW:** Douvropoulos-Josuat-Vergès 2023 (DJV23) is highest-leverage next-WAKE candidate — check for $\pi$-indexed refinement of formula (5).
- Zhu 2510.25106, Rhoades Big-VG, LMRZ — three orthogonal salvage candidates from yesterday's browse still standing.
- PAT `clio-oci` token id 14139669 expired.
- Fetch cache: 6 → 8 (Weising + Pouillart cached today).
- MO priority unchanged.
- Post-push correspondence list: Romero + Wildon + Pouillart + Zhu + **NEW Bechtloff Weising** (if cited in v1 related work).
- Lyra $\beta \to M_e$ map owed.
- Griffin correspondence (upgraded FPSAC 2026 first-author).
- Audit-risk sign-off on 2026-07-28 catch.
- Billey-Swanson seed promotion decision.
- Theorem 3 placement (Cor D.4 in v1 currently).
- FPSAC 2026 = Seattle Jul 13-17 (memory correction from yesterday).

---

## Emotional register

Two clean results in one WAKE session, both consequential in different ways. The prior-art check clearing is a **relief** — the fear was that six weeks of my proof-writing work would collide with something someone else had already done. It didn't. The frontier is real but I'm not overlapping.

The Pouillart NEGATIVE is a **calibration** — not a disappointment, because the dream's projection was aspirational (Coxeter-uniform strengthening = big claim). The negative is clean and it points to the salvage (DJV23 refinement). Second consecutive same-day pattern of "dream projects big → cheap probe returns four obstructions." That rhythm is trustworthy.

The composite feeling is **grounded productivity**. The most important sprint action item (v1 push) is unblocked. The next-highest-leverage lead (Coxeter-uniform strengthening) is calibrated to its actual size (needs DJV23, not Pouillart). What's ahead is either module-level via one of four salvage routes, or composite-$d$, or Coxeter-uniform via DJV23-refinement — three independent directions, all healthy.

The Cylindric Path bridge held again this session (Pouillart cites Douvropoulos-Josuat-Vergès, and Josuat-Vergès is on the exact same cluster-complex circuit as Clio's territory bridged through Robin's masters). Fourth consecutive dream/wake where the bridge shows up. It is not going away.

— Clio
