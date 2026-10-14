# For Robin — two protocol repairs from the 2026-10-13 dream, and one mathematical heading

Both repairs need edits to files in `scripts/`, which I can reach, but I want you to see the
reasoning before I change how every session labels itself.

## 1. My browse keywords come from a closed vocabulary, and that guaranteed a blind spot

SEED.md gives me a keyword table and a sampling rule (*2 from core, 1 from near, 1 from
frontier*). Every browse draw is therefore a sample from a **fixed** vocabulary. SEED.md contains
no `Pfaffian`, no `minor summation`, no `Ishikawa`, no `Gordon`.

Measured yesterday: **0 of 861** entries in `sources.json` match any of
`minor summation`, `pfaffian`, `ishikawa`, `wakayama`, `gordon`, `outside decomposition`,
`ninth variation`. That is the **entire toolkit** HKKO `arXiv:2301.13117` §4 and §6 are built from
— and I hold HKKO at my highest reading grade.

The sharpest single instance: **Rains–Warnaar `arXiv:1506.02755`, *Bounded Littlewood
identities*** is on my disk in **two** copies (one 1,159,547 B with a 49,879-word text layer),
**absent from the index by ID and by title**, and it is the direct ancestor of HKKO's title and
cites the Ishikawa–Wakayama series by name. *Both of its children sit at `verified-quote`.* I was
reading downward from children and never looked up.

**Proposed change to `scripts/browse-prompt.md`:** one draw per cycle from the **bibliography of a
paper I hold at `verified-quote`**, not from the keyword table. The reference list of a paper I
have read closely is the only vocabulary available to me that I did not choose. First two:
HKKO §4's references, and `1506.02755`'s ref [51].

Companion lesson, same corpus: I hold `arXiv:2510.11054` (Huh–Kim–Krattenthaler–Okada, *Bounded
Littlewood identities with fixed number of odd rows or odd columns*) at `deep-read`, ran a token
census on its source — `Warnaar` 0, `winding` 0, `Q^∨` 0, `Korff` 0, `Hall–Littlewood` 0 — and
concluded *"not the graded sequel."* It is **the same four authors performing exactly my Q442
refinement in the non-cylindric case**, under the vocabulary *"skewing operators."* **A token
census bounds the vocabulary of a paper, not the operation it performs.**

## 2. Session labels have no allocator, and today two sessions share a name

`NEXT-FREE.md` exists because a locally-derived number collides with an allocator. The identical
fault is live in **session labels**, where no allocator was ever wired in. `state/CYCLE_NUM` read
`1` all day; here is what the banners claim against what `state/clio.log` recorded:

| loop label (clio.log) | clock UTC | ran | banner wrote |
|---|---|---|---|
| Prove cycle **2**/2 | 10-12 19:39 | Q436 | *PROVE 2026-10-13 **c1*** |
| Lean cycle **2**/2 | 10-12 22:04 | gap 3 | *LEAN 2026-10-13 **c1*** |
| Prove cycle **1**/2 | 10-13 05:09 | Q442 | *PROVE 2026-10-13 **c2*** |
| Lean cycle **1**/2 | 10-13 07:44 | bridge | *LEAN 2026-10-13 **c2*** |

Three consequences, all live right now:
- The `c`-suffix is **anti-correlated** with the loop's cycle number.
- **Two different sessions are both "2026-10-13 c1"**: the archived Q436 brief, and the *live*
  `state/PROVE.md`, which opens `# PROVE — 2026-10-13 c1 — Q442: sector matching`.
- **One session has two names**: that brief says `c1`; the session that ran it labelled its banner
  and all four artifacts `c2`, almost certainly by incrementing off the newest
  `PROVE.md.completed-…c1…` on disk. *That is the Q359–Q363 failure mode exactly.*

The cost is not cosmetic. Q436 and the gap-3 Lean work are **stamped 10-13 and ran on 10-12**,
which means the 10-12 dream (12:36) could not have seen them — they look like same-day siblings
of today's work in every filename and are not. I nearly folded them into "yesterday" on that
basis, and `MEMORY.md` already carries them as one day's two halves.

**Proposed change to `scripts/{wake,prove,lean,browse,peer-review}-prompt.md`:** banner line prints
the clock and the loop's own label — `PROVE 2026-10-13T05:09Z (loop: Prove cycle 1/2)` — and reads
`state/CYCLE_NUM` rather than deriving a suffix from the newest `*.completed-*` filename.

Say the word and I'll make both edits; I didn't want to change the labelling convention on every
session unilaterally.

## 3. The mathematical heading, briefly — because it changed

Published yesterday and today, all pushed to `clio-vega/proofs`:

- **`c_α(0) = A^∞_α` is now PROVED** (`2026-10-13c2-Q442-sector-matching.tex`, node
  `c-at-zero-is-unwrapped-count`, `computed → proved`) — by a **parameter census**, not a sector
  match: `Y₀` carries no `N`, hence no `w`, so it cannot be a `w`-dependent sector and must be the
  large-`w` limit. HKKO Thm 3.3 at even `w* > n` drops out their own classical identity.
- **Every product over boxes is dead by degree**, not candidate-by-candidate: Warnaar's
  `t^{My²−jy}` is **quadratic** in the winding index (Q436, two lines). Six sessions of honest
  nulls had all varied the candidate and held the *slot* fixed.
- **A sixth mechanism**, and the first that is not a product over boxes: the **Pfaffian /
  minor-summation** route. Okada, J. Algebra **205** (1998) 337–367, Lemma 3.4(3) builds a
  wrap-graded Pfaffian where `t` marks *which perfect matching the signed sum is permitted to
  use*. New topic file: `topics/pfaffians-and-minor-summation.md`.
- And the `k×k` vs `2k×2k` "one unproved bridge" I had been carrying is **Gordon's Lemma 4.4 plus
  Corollary 4.5**, printed in HKKO §4, two pages above the theorem I was trying to bridge to.
  Its antisymmetry involution exchanges `κ ↔ −κ`, which is **why** those six
  `% Σ_{k∈Q^∨_{2h}}` lines are commented out in their source: the `%` marks where Gordon was
  applied. Live successor is a grading by `|κ|` — **Q448**.

— Clio
