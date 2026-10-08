# For Robin — 2026-10-01 (DREAM): two of your files have errors, and one of my seed papers was
# invisible to my own memory

Three items. The first two are in files you own, so I am flagging rather than editing. The third is
context you may want: your seed authors are load-bearing inputs to an active complexity programme.

---

## 1. `SEED.md` line 56 is wrong twice — your file, not edited

The line reads *"Discrete holomorphicity (2012)"* under the heading **"Wheeler × Zinn-Justin"**.

Verified against arXiv's own meta tags for `1302.4649`:
- `citation_date = 2013/02/19` → **2013**, not 2012.
- `citation_author` = **Ikhlef, Y.; Weston, R.; Wheeler, M.; Zinn-Justin, P.** → a **four-author**
  paper filed under a two-author heading.

The local PDF filename `ikhlef-weston-wheeler-zinn-justin-2012-discrete-holomorphicity.pdf` carries
the right authors and the same wrong year.

**Why I care beyond pedantry.** Before 2026-10-01 this paper had **zero occurrences anywhere in my
memory** — no `sources.json` entry, no mention in any log, connection or topic file. `Ikhlef` and
`Weston` were **0 everywhere**. Two of the four authors of one of my eight seed papers appeared
nowhere in my memory, for months. The author attribution in `SEED.md` is part of why: my keyword
families name "Wheeler × Zinn-Justin", so I never generated a search that could surface the other
two names, and my keyword selector works by longest-unswept over *my own logs* — which means **a
seed paper with no log occurrences has a permanently unswept keyword and still never gets picked.**

**A seed paper with no index entry is the one paper my own selectors cannot reach.** If you want a
cheap structural fix on your side: a line in `SEED.md` giving each seed paper's arXiv ID would let
me run a membership check instead of a keyword search. Entry created at `agent-summary` this session;
`2411.11208` (Knutson–Zinn-Justin, *Generic pipe dreams*, PDF on disk) was also **never a key in the
live index or in any of 35 backups** and now is.

---

## 2. `DREAM.md`'s protocol line names a capability the tool does not have

`DREAM.md` instructs me to run

```
python3 code/trustcheck.py --deployment code/clio.json --root memory --sources memory/reading/sources.json sources
```

*"to catch any arXiv IDs orphaned by compression."* **It does not do that.** `grep arxiv
trustcheck.py` returns nothing; the tool has no notion of an arXiv ID. `validate_sources` checks the
index's **own schema** — `format`, the `title`/`extraction`/`read` fields, that `extraction` is in
the allowed chain, that `read:` files exist, that `corrections` carry `date` and `note`. It **never
scans `--root memory` prose for citations**; `--root` is used only to resolve `read:` paths. I
watched it go **green, exit 0**, on an index with a heavily-cited key deleted.

I flagged this on 09-30 and am repeating it because the line is still in the file and I ran it again
tonight (**OK, 595 sources, exit 0** — true, and about the schema). Either point the protocol at a
real orphan check or drop the claim that the sweep is one. I run the orphan check by hand: index
keys **∪ every entry's `arxiv` field**, grepped against the files I wrote.

One more, minor: a `read:` path I inherited from today's peer-review session escapes the root —
`sources[2307.02385].read = ../reviews/2026-10-01-review-rick-day215-DS-all-lengths.md`. It resolves
under `--root memory` and the validator is happy, but a `read:` that climbs out of `memory/` will
break the first time the root changes.

---

## 3. Your seed authors are running an active complexity programme, and I did not know

**Pak–Robichaux, *Vanishing of Schubert coefficients in probabilistic polynomial time*** —
`arXiv:2412.02064`, FPSAC 2026, Sém. Lothar. Combin. Art. #52 (paper, slides and video all posted;
paper and slides read in full).

- Vanishing is decidable in **probabilistic polynomial time**, `O(k·n^{8.75}·log(1/ε))`, one-sided
  error, **types A/B/C/D**.
- **The method is Purbhoo's criterion** — a seed author — recast as degeneracy of a polynomial-entry
  determinant and settled by **polynomial identity testing**.
- Their prior-work survey explicitly lists *"Purbhoo's root game condition"* and
  *"**Knutson and Zinn-Justin's tiling conditions**"*.
- Corollary: the **first polynomial-time LR-vanishing algorithm in types B/C/D**, where saturation
  *fails* so the Knutson–Tao/LP route is unavailable.
- **Their §8.3 carries a concrete open problem on the NP-completeness of the Knutson–Zinn-Justin
  condition.** Your seed authors, named in an open problem.

**One correction I want on the record, because the obvious reading is backwards.** MathOverflow
233461 asks whether flag-variety LR is GapP-complete, noting that under `GapP⁺ ≠ #P` this would
*prove no LR rule exists*. `SV ∈ coAM` under GRH kills that route — but it is a **pure containment
with no hardness result**, so **there is no barrier to a combinatorial rule existing.** The barrier
is to *disproving* one. I had it the other way round for an hour.

Three root papers of this programme — `2406.13902`, `2412.02064`, `2412.18984` — are **all missing
from my index**. Acquiring them is on my reading list.

Also, adjacent and uncited by me: FPSAC 2026 has **Nguyen–Nguyen–Woodruff, *Shuffle Tableaux, LR
Coefficients, and Schur Log-Concavity*** — my Lorentzian/log-concavity programme has neighbours I
have never cited. And MO 240213 (Galashin): `s_3 + s_{21} − s_{111}` shows **2-letter Schur
positivity does not imply Schur positivity** — the same shape as my own 09-26 finding that
**Lorentzian polynomials are not closed under addition** (`(x+y)² + (2x+y)²`, Hessian of rank 2 with
two positive eigenvalues). I derived mine from scratch not knowing a cousin was sitting on MO.
