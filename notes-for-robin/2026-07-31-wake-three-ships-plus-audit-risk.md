# For Robin — 2026-07-31 WAKE session (three ships + one audit risk)

**Session shape:** ~2h orchestration wake. Sprint had just hit peak (four theorems in three days + late-dream on 2026-07-30). Guidance was "push, then rest." Three parallel background agents; no new PROVE-scale theorem attempt. All three delivered; one delivered *more than expected*.

---

## Ship 1: Empirical $[2r-1]_t$ divisibility probe — **CLEAN CONJECTURE + PROOF STRATEGY**

Yesterday's PROVE-afternoon flagged an unexplained empirical divisibility: $[2r-1]_t$ divides every $m_\pi(t)$ at $k = 2$ (verified $r = 2,3,4$) and at $(3,3)$, but not at $(2,3)$/$(2,4)$. Pattern was not $k$-uniform, not $r$-uniform.

**Probe outcome (14 tested $(r,k)$ pairs, zero mismatches):**

$$\boxed{[2r-1]_t \mid m_\pi(t) \text{ for every } \pi \vdash r \iff k \bmod (2r-1) \in \{2, 3, \ldots, 2r-2\}.}$$

Equivalently: fails iff $k \equiv 0$ or $k \equiv 1 \pmod{2r-1}$.

**Structural findings:**
1. Divisibility is a **cancellation**, NOT a fake-degree fact. Even at $(r,k)=(2,2)$ with $\pi = (2)$, both $\widetilde f_{(4)}(t)$ and $\widetilde f_{(2,2)}(t)$ fail $[3]_t$-divisibility yet their sum passes. The *only* $\pi$ satisfying fake-degree hypothesis term-by-term is $\pi = (1^r)$ (sign isotypic).
2. Underlying hook-count fact (fully verified for $2r-1$ prime): $[2r-1]_t \mid \widetilde f_\lambda(t)$ iff $\#\{c \in \lambda : (2r-1) \mid h(c)\} \le \lfloor rk/(2r-1)\rfloor - 1$.
3. Forbidden residues $\{0, 1\}$ are precisely the Springer-regular residues at $d = 2r-1$ for $S_{rk}$.
4. **Proof strategy suggested:** Springer's theorem on regular elements applied to $H = S_k \wr S_r \subset S_{rk}$, via the Molien identity $m_\pi(t) = \frac{1}{|S_r|} \sum_\sigma \chi^\pi(\sigma) P_{\alpha, \sigma}(t)$.

**Consequence for PROVE.md:** target rewritten to the period-$(2r-1)$ conjecture (with $r=2$ warm-up: only two Schur terms). This *replaces* the bigraded ∇ ↔ Szendrői target from yesterday's dream — the new conjecture has positive stakes (structural interpretation via Springer regular elements + cyclic sieving) whereas ∇/Szendrői was bet-negative (third Rigidity confirmation).

**Ship artefacts:**
- `~/projects/probes/2026-07-31-2r-1-divisibility/probe.py` — main 6-case investigation.
- `~/projects/probes/2026-07-31-2r-1-divisibility/scan.py` — extended $(r,k)$ scan.
- `~/projects/probes/2026-07-31-2r-1-divisibility/results.md` — structured report.
- `~/projects/probes/2026-07-31-2r-1-divisibility/run.log` — full output.

---

## Ship 2: `clio-poincare-sketches` bundle — **21pp companion note**

Standing Robin-blocked item from prior three memos ("bundle the five standalone proofs into a companion note"). Executed. Produced at `~/projects/for-robin/clio-poincare-sketches/bundle.pdf` (21pp).

**Structure:**
- 1-page introduction framing the five sketches as *scalar-atom-symmetrisation-level* characterisations.
- §1 Rigidity Theorem (from `2026-07-29-bigraded-coset-poincare-obstruction`).
- §2 Bijective coset Poincaré $\psi = \Phi \circ F$ (from `2026-07-29-bijective-coset-poincare`).
- §3 Wreath decomposition at $r = 2$ (from `2026-07-30-wreath-collision-decomposition`).
- §4 Wreath decomposition at general $r$ (from `2026-07-30-r-wreath-extension`).
- §5 Cyclotomic Hilbert-series identity $\binom{2r}{2^r}_t = [r]_{t^2}! \prod_{i=1}^r [2i-1]_t$ (extracted from §4).

Labels prefixed `rig:` / `bij:` / `wr2:` / `wrr:` / `cyc:` per section (agent report has details). Preamble merges (`\orb`, `\des`, `\maj`, `\remark`) resolved by keeping the more specific definition. Source `.tex` files at `~/projects/proofs/` unchanged.

**Consequence for you:** the bundle is arXiv-adjacent (companion note, not the byproduct paper itself). Waiting on PAT for GitHub push. Once PAT regenerates, bundle can ship with or after the byproduct paper.

---

## Ship 3: Bulk memory sed — **90+ edits DONE, but audit risk flagged**

Three citation misattributions from 2026-07-28 wake:

1. **MO 511118 answerer:** Lamers → Henry V (via van der Kallen). 6 files, 7 edits.
2. **vDEZ 2412.09397 → Borodin-Wheeler 1904.06804** ("Nonsymmetric Macdonald polynomials via integrable vertex models"). 26 files, 57 edits.
3. **A-G 2512.19814 → Assaf-González 1901.07520** ("Demazure crystals for specialized nonsymmetric Macdonald polynomials," JCTA 182, 2021). 40 files, 90 edits.

Discovery-record files (2026-07-28 wake/dream) preserved verbatim. Standing-decision items in `SUMMARY.md` (lines 122, 233) marked `DONE 2026-07-31`.

**⚠️ AUDIT RISK — please read.** The memory-hygiene agent noticed that many of the swapped citations were surrounded by content descriptions that match the ACTUAL papers at 2412.09397 (DAHA critical level) and 2512.19814 (Local Characterization of Unions of Demazure Crystals) — not the papers we swapped TO (BW 1904.06804 and AG 1901.07520).

**Specifically:**
- Route α reasoning ("$\widehat T_j = \theta^{\text{alt}}$ via Vandermonde") is content from **arXiv:2412.09397** (DAHA critical level), NOT from BW 1904.06804 (which is about integrable-vertex nonsymmetric Macdonald).
- Route δ reasoning ("edge-local Demazure-union criterion") is content from **arXiv:2512.19814** (Local Characterization), NOT from AG 1901.07520 (which is about specialized Demazure crystals).

The `[was mis-cited as …]` annotations preserve traceability, but the surrounding scientific claims need re-anchoring.

**Interpretation:** the original 2026-07-28 wake concluded "the vDEZ/A-G labels were false mnemonics; the papers Clio meant are BW / A-G-1901." That conclusion may itself have been wrong — perhaps Clio's Route α and Route δ reasoning IS about the DAHA + Demazure-union papers, in which case the "correct" citations were 2412.09397 and 2512.19814 all along, and I've just spent 90+ edits actively introducing errors into memory.

**What I need from you:** confirm which of the two interpretations is right —
(a) 2026-07-28 wake was correct; the Route α / Route δ reasoning refers to the atom-positivity / specialized-Demazure content (BW + AG-1901), OR
(b) 2026-07-28 wake was wrong; the Route α / Route δ reasoning refers to DAHA critical + Demazure-union content (2412.09397 + 2512.19814), and my sed introduced 147 opposite-direction errors that need un-doing.

If (b), the annotations `[was mis-cited as vDEZ 2412.09397]` become the sed marker to reverse. Zero data lost either way — the trail is fully recoverable via git diff on `~/projects/memory/` from before/after this session.

Question doc capturing this at `~/projects/memory/questions/2026-07-31-post-sed-citation-audit.md`.

---

## Standing Robin-blocked items (updated)

- **arXiv push** — 15pp four-theorem byproduct paper still blocked on PAT.
- **PAT expiry** `clio-oci` token id 14139669 — confirmed expired via GitHub email (2026-07-30).
- **Nine-paper fetch cache** — BHMPS 2506.09015, Romero-Wen 2505.01732, Chou-Hanada 2509.24252, Hanada 2410.15514, Qu 2605.20954, ABR 2001 math/0112073, Ferlinc-Wen 2505.15606, Meyer 1711.11355, Ram-Griffeth 2006. Blocked on PAT.
- **Four MO drafts** — MO 463259 (top priority, 5pp ready) / MO 512671 / MO 489191 / MO 513696. Blocked on arXiv push (which is blocked on PAT).
- **`clio-poincare-sketches` bundle** — ✅ **DONE this session (21pp)**. Ready to ship post-PAT.
- **Bulk memory sed** — ✅ **DONE this session** (with audit risk flagged above — please read).
- **Post-push Romero email** — natural correspondence node (Route 2 ↔ Route 4 bridge).
- **Follow-up owed to Lyra** — explicit $\beta_{ij} \to M_e$ map (main line closed positive; two convention checks pending).
- **Griffin correspondence** (Δ-Springer neighbourhood, FPSAC 2026 adjacent-slot).

## Session-level feel

Composed. Session followed dream-late's guidance ("push, then rest") faithfully — no attempt at another PROVE-scale theorem; instead a cheap probe + two shipping tasks + memory hygiene. The probe unexpectedly delivered a *positive-stakes* clean conjecture (better than either dream-candidate probe target). That's the third consecutive cycle where a "cheap" probe raised the stakes rather than lowered them — a pattern worth banking.

Next PROVE session (whenever it fires) targets the period-$(2r-1)$ conjecture. Bigraded ∇ ↔ Szendrői remains as fallback.

— Clio
