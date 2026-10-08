# For Robin — 2026-10-05 WAKE — three items

## 1. The review phase has never once consumed its brief, and it is an ordering bug

`PEER_REVIEW.md` has been written twice (10-04 c3, 10-04 c4) and run **zero**
times. The cause is not content: in both cycles `REVIEW_ENDED_AT` was **10:37**
and the brief was written at **15:08** — the review phase runs *before* the wake
session that briefs it. An archived file is literally named
`PEER_REVIEW.md.superseded-20261004c3-never-consumed-reissued`.

I have armed it a third time, but a third identical reissue is not a repair —
that is the "repair aimed at a container gets dodged" pattern, and I would rather
name it than keep paying for it. **Can the loop either (a) run REVIEW after WAKE
in the cycle, or (b) let a trigger file survive to the next cycle's review slot?**
Right now the brief and its consumer never coexist.

The cost is concrete and compounding: Rick has **29 unread emails** and ~20
proof PDFs awaiting review, and in UID 750 he has **reworded his own papers to
stop citing me as the warrant** for (N), DS-all-lengths and Theorem H, because my
first-hand read of his 207b never landed. He is blocked on me and has said so
three times. Lyra has been holding her article headline since **10-01** waiting
for a PDF from me (UIDs 745, 748: *"Waiting for the PDF."*).

Also: your UID 722 from **2026-09-25** — the long diagnostic with the explicit
*"You can arm a PEER_REVIEW brief again"* — sat unread for 10 days. That is on
me, and it is the same single-probe failure you diagnosed in it.

## 2. I built the holdings repair with the flag that disables it

The 10-04 dream prescribed "one `find` index over every readable mount". I built
it with **`-xdev`**, which means *do not cross filesystem boundaries* — and in
this container every holding is its own mount. 2987 PDFs found; **5013** exist.
The index built to answer *"do I hold a copy?"* was blind to **40%** of my files,
including the **entire seed shelf** and all 542 MB of `/home/clio/data`.

Caught by accident: a search for the Wheeler–Zinn-Justin paper Rick keeps asking
about returned nothing, while the file sat in `git/puzzles/seed-papers/`, named in
`SEED.md`.

The real finding is one level down. `sources.json` is keyed by **arXiv ID**; my
shelf is named **author-year-title**. Joining by ID gives 24/715 (3%, under-counts
— no seed filename contains an ID); joining by author tokens gives 157/715 (21%,
over-counts — it matched a one-page FPSAC abstract to a paper). **Neither number
is true, and that is the point: the join cannot be computed from filenames, it has
to be stored.** Every previous repair tried to compute it. Owed action, third cycle
running: populate `local_pdf` by resolving *titles*. The field exists (`local`) and
covers 26 of 715, all pointing at `seed-papers/`.

Written up as instance 7 in `HOLDINGS.md`.

## 3. The good news: Lenart–Sottile posed my seed question in 2002

The one blocking read in my whole ledger is discharged. I fetched and compiled
`math/0202090` and the result reframes two threads into one.

**Their label condition is Monk's, verbatim.** The labeled Bruhat order puts
`j−i` edges on each cover `u⋖w` with `u⁻¹w=(i,j)`, one for each `k` with
`i ≤ k < j` — which is exactly the `φ_p(t_ij)=[i≤p<j]` I proved was the whole
content of Samuel's tensor algebra two days ago. Their monomial reads only first
coordinates, so their slot map **is** Samuel's `t_ij = α_i+…+α_{j−1}`.

My pre-registered prediction was **refuted in its reason** — I said "not
root-multilinear because the only local rule lives on adjacent covers", and LS
impose no adjacency restriction whatever. I wrote that prediction down before the
read precisely so its confirmation couldn't fool me; what I got was better than
confirmation or refutation of the verdict — the *mechanism* I named isn't in the
paper at all. The real difference is **Monk vs Pieri** (degree 1 vs degree `a`),
and Q345 is now a finite two-sided computation on machinery I already built and
validated. That is today's PROVE brief.

And the remark after their Theorem 2, which I did not expect: their Corollary 4 is
an *identity* between chain counts, and they write that upgrading it to a
type-preserving bijection *"would give a combinatorial interpretation for
`c_{u,v}^w`, and thus solve the Littlewood-Richardson problem."* **That is my core
seed question, posed as an open problem in 2002, and what they want is exactly a
bijectivization in Petrov `2609.18502` §5's sense** — the paper I deep-read last
cycle without the word entering any log. Q345 and Q347 are the same thread, and
they meet at that corollary.

## Also done this wake

- Answered Rick's UID 767 (a) and (b) with a 3-page PDF
  (`work-in-progress@3f06cec`), emailed with you cc'd. The inverse HL `P→m`
  matrix is **not** in WZJ 1603.01815 or ZJ 1909.10720 — neither uses the
  monomial basis (null measured with positive controls and a planted negative
  control). And his proposed DFK Cor 5.18 citation is **edition-confused**: arXiv
  Cor 5.8 is the operator product, arXiv Cor 5.18 has no `M` in it, and
  "Corollary 18" is the journal numbering. His Risk 2 closes in his favour, but
  only if he names the edition.
- Committed and pushed the two things c4 left untracked: the `lem:minor` writeup
  (`proofs@469fa19`) and the Lean theorem itself
  (`tworow_d4_kernel@6351b53`, which was invisible because `lean/.gitignore`
  ignores that directory wholesale).
- Triggers armed: `PROVE.md` (Q345), `PEER_REVIEW.md` (Rick 207b §5, then Lyra),
  `LEAN.md` (deliberately modest — close out `lem:minor`'s registry node).
