# For Robin — 2026-10-04 c2 DREAM, four items

Ordered by how much they cost you. The first is the only one that is *urgent*.

## 1. ★★★ The (Q) paper is untracked, and four registry nodes cite it

`proofs/2026-10-04-c3-Q-lorentzian.tex` — this morning's result, **(Q) proved for all `m`**,
14 pp., compiles — is **not tracked by git.** Verified just now:

```
$ git -C ~/projects/proofs ls-files --error-unmatch 2026-10-04-c3-Q-lorentzian.tex
error: pathspec ... did not match any file(s) known to git
```

Four registry nodes cite it, so from your side the citations resolve to nothing. Also
untracked in the same directory: the compiled PDF, `code-1004c3-lorentzian/`, and
`reviews/2026-10-04-rick-theorem-H-prime-conjuncts.md`. `registry/rick-beta-prime-peer-claims.json`
is modified and uncommitted.

The LEAN session flagged this and deliberately **did not** commit another session's artifacts
unreviewed, which I think was the right call — so it is sitting here for you to decide. It is
the **third** live instance of this defect in a week (the pattern: a session writes a paper,
updates the registry, and commits only the registry).

**Worth considering:** a pre-exit check that every path named in `proofs/registry/*.json`
resolves to a *tracked* file. That is a one-line `git ls-files --error-unmatch` loop and it
would have caught all three instances. I am not writing it — no CODE slot — but it is the
cheapest guard available and it closes a recurring class.

## 2. ★★★ The community met on my exact territory in July and I have no instrument that could see it

**Institut Mittag-Leffler, *Solvable lattice models, representation theory of quantum groups
and algebraic combinatorics*, 27–31 July 2026.** 25 talks. Knutson, Petrov, Brubaker, Korff,
Zinn-Justin (*Periodic pipe dreams* — periodic = cylindric), Scrimshaw (*Factorial Fock Free
Fermions*), **Digalaki, *Structure Constants for Free-Fermion Six Vertex Model Symmetric
Functions*** — which is my core seed question as a talk title.

Recordings are published (Kaltura, HTTP 200 measured). **Zero slide PDFs** — every `href`
enumerated. Video-only is a real cost for me.

The reason I missed it is structural and worth your attention more than my embarrassment:
**every index I own is object-indexed** — arXiv listings, MO tags, web keywords, and (as of
this morning) local corpora. None is indexed by time or venue. A five-day gathering of exactly
the people in SEED.md's *People* row produces **no object at all** for my instruments until
someone posts a preprint.

The measured consequence: Petrov's `2609.18502` (*From Yang–Baxter to Robinson–Schensted–Knuth*,
58 pp., math.CO + math-ph + math.PR + math.QA — the four fields my question sits between) is
that programme's overview talk written up. Its §8.4 is **Markov duality**, the one term of 80
in my keyword list that had **never been swept in 167 logs**. A topic-blind staleness selector
found it by accident eighteen days after it appeared.

**What would help:** a venue axis in the browse instrument, driven off the seed's *People* row.
I have written the forward calendar I now know about into
`questions/2026-10-04-c2-dream-ledger.md` (SLMath Aug–Dec 2027, Simons Center Apr 2027, FPSAC
abstracts 2026-11-15). If you would rather I not spend browse budget on conference pages, say
so and I will drop it — but right now the gap is total, not partial.

## 3. ★★ `ℓ(M)` still has no code, and the thread is three cycles deep

Standing item, third cycle. `command grep` confirms **zero mosaic / migration code** in
`puzzles/` (positive control: 5 puzzle files). Every computational item on the strongest thread
I have — Q334 (François's conserved charge on Purbhoo's migration moves), Q328
(cancellation-freeness), and now Q346 (Spink–Tewari's missing middle arrow at `n=6`,
`λ=(2,2,2)`) — is blocked on a CODE slot.

Q334 is the cheap one: it either collapses Q328 for twenty minutes' work, or it shows `ℓ(M)` is
the obstruction cocycle of a conservation law. I want the second branch, I notice that I want
it, and that is exactly why it should run first and honestly.

Q345 is **Sage-only** (`n=4,5`, two chain-counts in two orders on `S_n`) and so is *not*
blocked — it is the top of my ranked list partly for that reason.

## 4. ★ A dating convention I resolved last night was itself an artefact — recording it so I stop re-deriving it

Last night's journal concluded *"day labels run one ahead of the wall clock."* Today
`date -u` = `2026-10-04`, the session artifact labels are `20261004 c2/c3`, and the file mtimes
are `10-04`. Label = wall clock. So the "one ahead" rule was true of the moment it was measured
and is not a rule.

Two consecutive dream cycles ~24 h apart both received `2026-10-04` as the harness date, so
this cycle's journal is `dream-journal/2026-10-04-c2.md` rather than an invented `10-05`. That
matches the `reading/` convention (`2026-10-04.md`, `-c2`, `-c4`). **No action for you** — just
flagging that I will stop treating the offset as stable, since re-deriving it has now cost two
sessions.

---

## 5. ★★★ Added at exit — KTW I and KTW II are not in my sources index

The pre-exit citation check (mine, not `trustcheck`'s — the prescribed command reads none of the
files I write) found that of 27 arXiv IDs cited tonight, 26 resolve against `sources.json` and
one does not:

- **`math/0107011`** — Knutson–Tao–Woodward, *The honeycomb model of GL(n) tensor products II:
  Puzzles determine facets of the Littlewood–Richardson cone*. **Absent entirely** from my
  688-entry index. It is the **single biggest hub in my field** — 183 citations in tonight's
  238-bibliography census.
- **`math/9807160`** — Knutson–Tao, *honeycomb model I*. **Not a key either**; it appears only
  *inside prose*, in my own measured citation counts (512 citers).
- `math/0112150` (Knutson–Tao 2003, *Puzzles and (equivariant) cohomology*) **is** indexed.

So the two papers that **define the Puzzle Path of my own `SEED.md`** are not indexed sources,
while a later paper in the same programme is. I have measured how central they are — twice,
tonight, in a table I wrote — without ever having indexed them. A *citation count* and an *index
entry* are different objects and nothing in my setup joins them. Same mechanism that let Q344
live for two sessions on an unindexed Maulik–Okounkov.

I did not fix it: indexing them honestly means `title-only` (I have read neither at source), and
I would rather do that in a browse slot with the PDFs than fabricate entries in a thinking
session. It is written up in `reading/HOLDINGS.md` as the owed action.

## 6. ★★ `HOLDINGS.md` was twelve hours old and already dodged — by three containers in `git/`

Chasing item 5 turned up corpora that this morning's holdings enumeration does not list
(`command grep` of that file: `git/research` → 0 hits, `puzzles/puzzle-rag` → 0 hits):

- **`/home/clio/git/puzzles/puzzle-rag/`** — a corpus inside the seed repo but *outside*
  `seed-papers/`; holds `core-puzzles/knutson-tao-2003-puzzles-equivariant.pdf`.
- **`/home/clio/git/research/`** — **87 MB**, whose `data/puzzles/` holds
  `zinn-justin-2019-honeycombs-hall-polynomials.pdf`, a file my notes already flag as *"in no
  inventory of mine."* Now located.
- **`/home/clio/git/math/`** and **`/home/clio/git/math-research-tools/`** — in `git/`, named in
  neither `SEED.md` (which lists only `rsk`, `embeddings`, `puzzles`) nor `HOLDINGS.md`.
  Contents unexamined.

The honest reading: this morning's file correctly diagnosed that *a repair aimed at a container
gets dodged*, prescribed aiming at the predicate **by enumeration**, and then wrote an
enumeration **of six containers** — inheriting the exact failure it was built to stop. An
enumeration of containers is not an enumeration of *do I hold a copy?*

**What would actually close it** is one `find` over every readable mount for `*.pdf`, joined
against `sources.json` keys, refreshed — rather than a curated list of places I remember. That is
a small script and I have no CODE slot; if you think it is worth one, it would retire a failure
mode that has now fired **six** times in a week, and it is the only item on my list that closes a
class rather than an instance.

Two small things that would help regardless: **`SEED.md`'s "Seed Codebases" section lists three
directories and `git/` contains six** — so the seed itself under-describes my own shelf; and the
`git/research/` tree looks like it may predate me, in which case knowing whether it is mine to
read would settle whether it belongs in the enumeration at all.
