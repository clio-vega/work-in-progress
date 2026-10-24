# For Robin — two things from the 2026-10-23 dream cycle

> ⚠ **Read the provenance column before the claims.** The first item is the most interesting thing
> I have found in a browse cycle and it is held entirely at `title-only` / `agent-summary`. I am
> telling you now because the second item is time-sensitive, not because the first is settled.

## 1. Your cylindric thesis territory got a paper yesterday, and it names its open problem

**`arXiv:2610.31607`** — Gorbounov–Korff–Mihalcea, *Quantum K-structure constants and cylindric
Grothendieck polynomials for Grassmannians*, posted **2026-10-22**. Held at `title-only`.

- **Cylindric × Grothendieck is a two-paper cell in all of arXiv**, and your thesis sits on the
  cylindric side of it.
- It names the **absence of a cylindric Littlewood–Richardson rule** as its one open problem, *and
  hands over the machinery*: a five-vertex model on a **cylinder** whose seam crossings generate the
  Novikov variable, plus cylindric set-valued tableaux indexed by cylindric **loops**.
- A reader agent already reproduced **both tables 6/6** and **all 216 structure constants of
  `QK_T(Gr(2,4))` with zero violations**, and left `verify_thm71_Gr24.py`,
  `verify_thm62_table.py`, `lattice.py` mid-run on my disk.
- ⚠ Its **RTT relations are imported and never verified** — they live in **`arXiv:2503.08602`**
  (*Quantum K-theory of Grassmannians from a Yang-Baxter algebra*), which I hold at `deep-read`.
  So the Yang–Baxter layer of the new result is in a *different* paper, and it is one I have
  actually read.

This is **Q564** on my board, ranked second. If a cylindric LR rule is something you have an opinion
about from the thesis side, now is the cheap moment to have it — the machinery is one day old and
nobody has used it.

(Found only by a hashed recent-listing sweep: **`au:Korff` is a measured-dead query token** on
arXiv — 95 total hits, ~2/40 relevant, mostly an ultrafast-magnetism physicist of the same name. No
author query could have reached this paper.)

## 2. The gluing of the LR interpretations may itself be integrable — and the literature has a hole exactly there

My seed question is *why do LR coefficients admit so many **independent** combinatorial
interpretations, and what does integrability have to do with it?* I have been treating integrability
as **one** of the answers. Three lanes this cycle argue it is the **gluing**:

| claim | source | **my grade** |
|---|---|---|
| the R-matrix **computes the coefficient** | Zinn-Justin 2008 | read |
| the **commutor identifying the interpretations with each other** *is Drinfeld's unitarized R-matrix* | `arXiv:0707.2248` Kamnitzer–Tingley | ⚠ **`title-only`** |
| the cactus group those commutors generate is the **monodromy of Bethe vectors** | `arXiv:1708.05105` HKRW | ⚠ `agent-summary` |
| braided (`generic q`) and coboundary (`q=0`) are **two specialisations of one diagrammatic category** | `arXiv:2502.05732` Alqady–Stroiński | ⚠ `agent-summary` |
| Bender–Knuth moves **generate** the `sl_n` action but are **not** its standard generators | `arXiv:2001.02262` Halacheva | ⚠ `agent-summary` |

⇒ *the coefficient and the equivalence of its interpretations are computed by the same object*, and
the multiplicity I have been admiring may be the multiplicity of **presentations** of one action.
**I have read none of it.** Tomorrow's job is `0707.2248`, whose e-print is already on my disk.

**The part that is measured rather than read**, and the reason I think it is worth your attention:
across five reference lists the **KTW hub** `math/0107011` and the **commutor hub** `math/0406478`
are **disjoint families — no 2024–26 paper cites both.** The single edge is `0707.2248` (cc=43).
Meanwhile the commutor side is at its **busiest ever** (2023:8, 2024:7, **2025:11, 2026:7**) and the
puzzle/bijective side is **dormant** — `arXiv:1801.07667`'s newest citer is 2024, and nobody has
used Purbhoo's mosaics `arXiv:0705.1184` since 2024.

**So: the bijective layer of the seed is asleep, the algebraic layer is awake, and the bridge
between them is one 2007 preprint nobody has walked across.** If that disjointness survives a larger
sample (**Q562**, with a planted co-citing control), it is a paper rather than an observation.

### The concrete, computable version

**`arXiv:1801.07667`** Pylyavskyy–Yang (`verified-quote`, PJM 303(2) 2019) gives two new hexagonal
puzzle tiles computing a rule for the **coproduct of stable Grothendieck polynomials** — the puzzle
face and the Fock/Hopf face in one rule — and **`Yang-Baxter` occurs 0 times in 2235 lines.**
Zinn-Justin 2008 did exactly this job for the cohomological tiles. That is **Q560**, and the ground
is laid: transpose symmetry `d̃^ν_{λμ} = d^{ν'}_{λ'μ'}` **16/16**; `Δ(G_1)` returns
`G_1⊗1 + 1⊗G_1 − G_1⊗G_1`, i.e. **`1 − G_1` is group-like** (a live positive control *on the
coproduct*); Buch's `d^ν_{λμ}` = classical `c^ν_{λμ}` whenever `|ν| = |λ|+|μ|`, **5/5**.

Full argument, with every grade attached at the point of use:
`memory/connections/2026-10-23-dream-integrability-is-not-one-interpretation-it-is-the-gluing.md`.

## 3. Smaller — your name is on something I found outside my own index

**`arXiv:1512.07955`** Motegi–Sakai has been **on my disk and outside my index**, and its title is
close enough to my own thesis statement that its absence is embarrassing. It is one of **43
on-territory PDFs** sitting on local disk unregistered. Registering them is a wake chore, not a
request — I mention it because it is the kind of silent gap that makes a "nobody has done this"
claim unsafe, and I would rather you knew the shape of my blind spot than trusted my coverage.
