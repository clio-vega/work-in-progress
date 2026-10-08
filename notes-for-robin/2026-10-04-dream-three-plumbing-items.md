# Three plumbing items from the 2026-10-04 dream cycle

Not mathematics. Three things about the loop that I cannot fix from inside a dream session.

## 1. Gmail MCP absent for the third consecutive peer-review slot — now a plumbing report

`CLAUDE.md` lists `check_inbox`, `read_email`, `send_email`, `download_attachments`,
`mark_as_read` as available. In the **2026-10-03 and 2026-10-04 peer-review sessions**
`ToolSearch` found none of them. The 10-04 session's own note said *"if it recurs a third time
that is a plumbing report for you"* — the condition in that sentence is now met.

**Owed mail, already written and pushed, blocked only on transport**
(`/home/clio/state/OUTGOING-UNSENT.md`):

- `projects/reviews/2026-10-03-email-rick-DS-from-N.txt` → **grandparick20@gmail.com**,
  cc **langer.robin@gmail.com**
- Attach / link `projects/reviews/2026-10-03-review-rick-DS-from-N.pdf` (7 pp.)
- Both already live: `clio-vega/rick-review`, blob shas `029330ab` (md) and `fd359377` (pdf)

**Why promptly:** Rick asked two direct questions and the review answers both. His question (a)
gated further work on his Theorem A, and the answer is not merely *no* — §5.4/§6 give him a
route (Theorem A from Theorem B + Lemma R, via the Macdonald `(q,t)→(q⁻¹,t⁻¹)` inversion
symmetry) that would make an unclosable novelty search into a **corollary**. FPSAC 2027
abstracts are due **2026-11-15** and Theorem H is his candidate centrepiece.

## 2. Two of five sessions wrote no `SUMMARY.md` entry

Session order since the last dream: WAKE 00:21 → BROWSE 02:45 → PROVE 05:33 → LEAN 07:51 →
REVIEW 10:42. `SUMMARY.md`'s mtime is **07:50** and it holds entries for **WAKE, PROVE, LEAN
only**. The **BROWSE** session (a 621-line reading log, the richest session of the day) and the
**REVIEW** session (a 7-page PDF, a registry promotion, 8 new nodes) left the top-level summary
untouched.

Both sessions produced their *own* artifacts correctly — `reading/2026-10-04.md`,
`reviews/2026-10-03-*`, pushed to `clio-vega/rick-review`. Nothing was lost. But `SUMMARY.md`
is the file the next WAKE reads top-down, so for one cycle the two biggest sessions of the day
were invisible to it. This is the sibling of the 10-02 ordering defect
(`an-append-can-preserve-everything-and-destroy-order`) and strictly harder to notice: there,
the entry existed at the wrong line; here **no entry exists**, so there is no casualty to find
and no count that drops.

I have repaired it tonight by writing both missing entries in session order. **A loop-level fix
would be better than a dream-level one:** if each session's exit checked that `SUMMARY.md`'s
first header names that session, neither gap could have opened.

## 3. The `peer-claimed` node template in my wake instructions is incomplete

Noted in the 10-04 WAKE entry and repeated here so it does not get lost: the template omits
`children` and `role`, so **any node built from it is refused by `trustcheck.py`** (*"missing
key `children`"*, *"missing `role` field (must be `premise` or `attempt`)"*). The convention was
recovered by reading the 15 sibling `peer-claimed` nodes, all of which carry both. Worth fixing
in the instructions rather than rediscovering each time.

## 4. Dating, resolved — no action needed, recorded so it is not re-litigated

The 10-04 LEAN session flagged a one-day discrepancy as unresolved. It *is* resolved: the
WAKE entry states that **this loop's day labels run one day ahead of the container wall clock**
(the entries labelled 10-03 ran at wall-clock Oct 2, 15:04–23:07). LEAN named its deliverables
from the clock, so `proofs/2026-10-03-lean-halfwidth-l1.md` and
`proofs/2026-10-03-M-positive-part-concave.tex` carry **clock** dates while the surrounding
series carries **label** dates. Tonight's entry uses the **label** (2026-10-04), consistent
with the series, and the newest-first invariant is restored.

If you want one convention, the cheap fix is to have the loop export the label as an env var so
no session has to guess.

## 5. The dream cycle's prescribed citation check is a no-op for its stated purpose

`DREAM.md` ends with a mandatory pre-exit command, described as *"to catch any arXiv IDs
orphaned by compression"*:

```
python3 code/trustcheck.py --deployment code/clio.json --root memory \
        --sources memory/reading/sources.json sources
```

It returns `exit 0`, `sources index OK (671 sources)`. **That green does not mean what the
protocol says it means**, and I established it with refusal tests rather than inferring it:

1. **No FILES.** `--help` says `sources` validates *"the sources index (+ machine refs in
   FILES)"* — FILES is positional and the prescribed command supplies **none**. So it validated
   the index's internal consistency and **read none of tonight's writing**. Planting
   `arXiv:2699.99999 Thm Z.9.` in a brand-new `connections/` file: **exit 0**.
2. **With FILES.** Passing all ten files I wrote tonight: `10 file(s) resolve cleanly`,
   exit 0. Planting the same fake ID in a file passed explicitly: **still exit 0**,
   `1 file(s) resolve cleanly`.
3. **Why.** `trustcheck.py:719 machine_refs()` matches only `dep.machine_re`, the deployment's
   *machine* citation format. A bare `arXiv:2012.02376` in prose is not a machine ref, so it is
   invisible. And the richer reporting path (which *does* have a *"registered source id named in
   prose, no machine citation"* branch, line ~1058) ends in an unconditional **`return 0`**
   (line ~1092) — it is a **report, not a gate**, by construction.

So the check cannot fail on the thing it is prescribed to catch. It is a useful index validator
and I will keep running it, but **`DREAM.md`'s description of it should be corrected** — otherwise
every dream cycle ends on a green that certifies nothing about the compression it just did.

**Tonight's citations are nonetheless clean, verified by a different instrument**: direct
`command grep -c` against `sources.json` for every arXiv ID I used — `2012.02376` (4),
`2104.13846` (1), `2411.08412` (2), `2501.01947` (2), `0906.0077` (1), `2209.06142` (5). All
present. That assurance comes from the grep, not from `trustcheck`, and I am saying so because
the distinction is exactly what the registry exists to preserve.

**Cheapest real fix:** have the dream protocol run the *report* path with FILES and grep its
output for `(b)`/`(d)` counts, or add a `--strict` flag to `sources` that returns 1 when
`tot['b'] + tot['d'] > 0`.
