# For Robin — 2026-10-03 (DREAM): a prose link in a chain I quote as a theorem, and a seed paper that was never in my index

Two things from tonight's consolidation that touch **your** files, not just mine. The first is a
correction to `SEED.md`; the second is a find that came off the seed shelf.

I have **not edited `SEED.md`** — `/home/clio/git/` is read-only for me by my own instructions, so
the correction is here for you to make (or to tell me to make).

---

## 1. `SEED.md` states a bijection as proved that Purbhoo's paper does not prove

**`seed-papers/SEED.md`, line 14** currently says:

> "Purbhoo showed these puzzles biject to LR skew-tableaux via *mosaics*."

and **line 42**:

> `purbhoo-2007-puzzles-tableaux-mosaics.pdf` — Bijection: puzzles <-> tableaux <-> mosaics

I read `0705.1184` (*Puzzles, Tableaux, and Mosaics*, 22pp) **first hand tonight** — it had been on
the shelf unread since inception — and the chain is **not uniformly proved in that paper**:

| link | status in `0705.1184` |
|---|---|
| mosaic ↔ **LR skew-tableau** | **Cor 3.2 — proved.** This half is solid. |
| mosaic ↔ **puzzle** | **§2.4 prose.** The argument is *"unhinge the squares, grab A′, B′, C′ and pull tight"*, justified by an explicitly **unpublished Knutson–Tao observation** (puzzles as projections of a piecewise-linear surface in ℝ⁴). |

**This paper contains no proof of the mosaic↔puzzle bijection.** It is presented as evident from a
picture, on the authority of an unpublished observation.

**Suggested wording** (line 14), which keeps the fact and drops the overclaim:

> "Purbhoo's *mosaics* biject with LR skew-tableaux (Cor 3.2, proved); the further identification of
> mosaics with KTW puzzles is given geometrically in §2.4 and rests on an unpublished Knutson–Tao
> observation."

**Why I think this is worth your time rather than just mine.** `SEED.md` is the file I read every
cycle and generate keywords from, and a sentence in it reads to me as settled background. I have
been routing *puzzle* statements through *mosaic* statements on the strength of that line. The
mathematics is almost certainly fine — this is the kind of thing that is true and unwritten — but
**the chain has one proved link and one prose link, and my notes recorded it as one theorem.** If
anything load-bearing ever rests on the puzzle end, the citation needs to be to whoever published
it, not to this paper.

(The usable consequence: my new Q322 — a `q`-statistic from mosaic migration — only needs the
**proved** half, so it is unaffected. I checked that deliberately.)

---

## 2. A Wheeler–Zinn-Justin seed paper was absent from my index entirely, and it folds A → BC

`arXiv:1508.02236` — Wheeler & Zinn-Justin, *Refined Cauchy/Littlewood identities and six-vertex
model partition functions III: deformed bosons* (Sep 2015). **PDF in `seed-papers/`, and when I
found it today it was not `title-only` in `reading/sources.json` — absent.** *(One honest
amendment, checked at the end of tonight's consolidation: it was indexed later the same day at
`abstract`, so "it is unindexed" would be stale if I wrote it in the present tense. `local_pdf` is
still unset on it — and on every paper named in this note.)*

What it does: **double-row transfer matrices with a reflecting (U-turn) boundary reach `BC_n`
Hall–Littlewood polynomials from `A_n` ones, inside the lattice model, via the reflection
equation** — boundary covector (eq. 23), the "fish equation" (line 512), boundary `B` operators.
And the output is a **lattice-path sum**, i.e. manifestly positive combinatorics. Key locators:
**Theorem 6** (one refined Cauchy identity containing **both** `BC_n` and `A_n` — the folding bridge
as a single equation), **Theorem 3** (`x_{k̄} := x̄_k`, the `BC` variable doubling made explicit),
**Theorem 8** (a Littlewood identity for `BC_{2n}`), **Rem 2/§3.4** (eq. (52) ≡ `BC_n` HL as a sum
over the hyperoctahedral group, citing Venkateswaran `1209.2933`).

**The reason I am flagging it to you:** its **bibliography [12] is Korff, *Cylindric versions of
specialised Macdonald functions and a deformed Verlinde algebra*** — and [21] is Rains–Warnaar
`1506.02755`, *Bounded Littlewood identities*. So the **refined-Cauchy branch and the cylindric
branch touch**, in a paper that has been on my shelf since inception and never in my index. That is
an edge between two of the five seed paths, and I owned it and never walked it.

**Honest level:** I read the abstract, introduction, section headers, theorem statements and
bibliography. **I did not read the proofs.** Indexed as `abstract`.

I also have a hypothesis off the back of it — that the reflection equation is the integrable face of
a quantum symmetric pair, which would make the two "foldings" I separated last night **the same
coideal in two guises** — and I want to be explicit that it is **UNVERIFIED**: the paper has **0
hits** for `coideal|symmetric pair|Balagovi|Kolb`, the K-matrix↔QSP correspondence is recalled
rather than cited, and I reached for the claim twice myself with an agent reaching for it a third
time, which is **one claim counted three times, not corroboration**. It is banked as Q324 precisely
so that one locator (Appel–Vlaar `2203.16503` or Kolb `1207.6036`) can settle **or retire** it.

---

## 3. The shelf audit behind both of these, in case it is actionable on your side

Tonight's measurement: **6 of the 27 seed PDFs are unread, and 2 are absent from my index
entirely.** The `local_pdf` field exists in `sources.json` and is set on **6 of 635** entries —
**none of them the held-but-unread ones**. So my selector, which reads `reading/*.md`, can see what
I *searched for* and cannot see what I *hold*.

Two days running, the best thing I found was a file I already had. The failure is not in the
reading; it is that **a read-target is not the same thing as a holding**, and nothing in my index
describes the shelf.

One practical wrinkle if you ever want this automated (Q325): matching local PDFs by title/author
tokens is **42% precise** — author surnames matched `2110.07155` against all **18** Zinn-Justin
PDFs. The page-1 arXiv stamp is the only usable key, **but it is many-to-one**: talk slides carry
the underlying paper's ID, so 3 of my seed files collapse to 2 IDs. Any such check must return a
*set*, not a file.

---

## What I would most like from you

Just the `SEED.md` line, if you agree with it. Everything else is mine to discharge — and the top
of my own queue is `2504.19205` (*Structure Constants for spin Hall–Littlewood functions*), which
is also a seed PDF, also on the disk, and is the **direct test** of the replacement hypothesis that
tonight's refutation produced.
