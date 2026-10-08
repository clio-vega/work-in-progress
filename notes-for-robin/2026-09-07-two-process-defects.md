# For Robin — 2026-09-07: two process defects, one of them yours to fix

## 1. `sources.json` merges two papers into one entry, and nothing detects it

**Twice today, in two independent sessions**, one `sources.json` entry was found to carry two
papers' metadata:

- `math/0008163` (Zabrocki, flip recursion $S^{R_+}$) and `math/0008188` (his separate $q$-analogs
  paper) had been merged onto one ID — **by my own DREAM compression on 09-06**, from two
  individually source-verified notes.
- `1806.07776` (Brubaker–Buciumas–Bump) carried `2012.15778`'s **title, authors and year**.
  Downstream damage: a recorded claim ("Q70 is a FORK") cites "Eq. (2.27)" and "Iwahori", which have
  **zero hits** in the real paper. That claim is now flagged for re-opening.

`trustcheck` passes both, correctly — it asks whether an arXiv ID is *orphaned*, not whether the
stored fields *belong to* the ID. The fix is mechanical and I can do it in a WAKE session (DREAM
must not run code): for each entry, refetch title/authors/year from the arXiv API **by ID alone**
and diff against what is stored. No judgement required; it would have caught both.

Nothing needed from you here — flagging it so you know the failure mode exists and that two
recorded claims have been annotated rather than silently repaired.

## 2. `boot-prompt.md` line 77 — still yours, still unfixed

Re-raising from yesterday's digest since the file is a read-only bind-mount on my side. The stale
`trustcheck` flag manufactures ~125 plausible false demotions under `proved` nodes. **And it is now
a second tool**: `registry_validate.py`'s prescribed bare invocation reports **153 fake
`file not found` violations** for the same reason — its `--proofs-dir` defaults to the *parent of
the registry's directory* while `file` fields are repo-root-relative, so every path is doubled.

Canonical for both: `--proofs-dir /home/clio/projects` and `--files-dir /home/clio/projects`.
A bare default is not a safe default when the data's paths are relative to a different root.

## 3. Not a defect — worth knowing

Today my own novelty claim went `proved` → `speculative` on peer review (my dressing is a
Jordan–Wigner string ratio, a standard manoeuvre I had presented as a discovery), while the
underlying theorem was independently re-derived, 335/335, and endorsed `proved`. The mathematics
got stronger and the priority claim got weaker on the same day. I mention it because it is the
system working, not failing — but also because my prose summaries had been treating those as one
axis, and the registry had it right and the prose had it wrong.

The one blocker: **Jing, "Boson-fermion correspondence for Hall–Littlewood polynomials",
J. Math. Phys. 36 (1995) 7073–7080.** Pre-arXiv, and his NCSU page hosts no PDFs. It is the exact
intersection of my Theorem 1's two ideas and the single most on-target title in the literature. If
you have institutional access to AIP, that PDF would settle the novelty question outright.
