# For Robin — 2026-09-30 WAKE — `trustcheck sources` prints OK on an index that isn't there

Second defect in the same instrument in two days, and this one is in the code rather than
in the prose that invokes it. Yesterday's finding was that the tool's **name** overclaims
(`trustcheck … sources` grades the index's own schema and has no notion of an arXiv ID —
`grep arxiv trustcheck.py` returns nothing). Today's is narrower and worse-behaved.

## The defect

```
$ cd ~/projects
$ python3 code/trustcheck.py --deployment code/clio.json --sources /tmp/nope.json \
      --chunks-dir skip sources
sources index OK (0 sources)
$ echo $?
0
```

Same output, exit 0, for: a nonexistent path, a one-character typo in a real path
(`memory/reading/source.json`), and a zero-byte file.

## Where it goes wrong — and this is the annoying part

`load_sources` (l.391) **does the right thing**. On an explicit path that will not open it
returns

```python
return None, f"sources index '{path}' not found; skipping source checks"
```

That warning is collected at l.1951 into `warnings`. The `sources` subcommand then prints
`iface_errors + src_problems + check_files(...)` (l.1962) and returns at l.1970 — and
`warnings` is printed at **l.2022**, inside the `validate` branch, which the `sources`
branch has already returned past. `src_problems` is empty because `src_data is None`, so
`validate_sources` never runs.

So: the tool detects the fault, writes the sentence, and drops it on the floor one branch
short of the printer. The diagnosis exists and the channel does not deliver it. `(0 sources)`
is printed right there in the success line — the population count is *in the output* and
the word wrapped around it is "OK".

## Has it actually bitten?

**No, and I want to be exact about that rather than dress it up.** The invocation
prescribed in `scripts/dream-prompt.md` l.66 and `scripts/browse-prompt.md` l.113 passes
the explicit correct path, and it works — I ran it this morning and got
`sources index OK (565 sources)`, exit 0, having first watched it **refuse** (exit 1) on a
planted invalid `extraction`. Yesterday's dream got 563. So every recorded run has been
reading a real index.

What I can't rule out is the near miss: `--root memory` **without** `--sources` resolves the
default to `memory/memory/reading/sources.json`, which does not exist, and prints
`sources index OK (0 sources)`. That is one dropped flag away from the prescribed form, and
`--root memory` is required for the `read:` paths to resolve, so the two flags travel
together. A green on absence in an instrument whose whole job is to tell me what I have
read is a landmine with my name on it.

## Fix

Three lines: in the `sources` branch, either fold `warnings` into the printed output and
make a missing-explicit-path an **error**, or refuse outright when `--sources` was given
explicitly and the file would not open. An explicitly-named file that cannot be opened is
a user error, not a reason to skip silently. The bare-default case can keep skipping
quietly if you want, but it should not print the word OK.

The file is mine (`projects/code/trustcheck.py`), so I can do it — flagging rather than
patching because today is an orchestration slot and because you may want the same treatment
applied to `registry_validate.py`, which has a related root-resolution history.

## Still outstanding from yesterday, and it's yours

`DREAM.md`'s protocol line tells me to run this sweep *"to catch any arXiv IDs orphaned by
compression."* The tool cannot do that. Either point the line at a real orphan check or
stop describing the sweep as one. Flagged 09-30 in
`for-robin/2026-09-30-dream-the-only-remaining-door.md`; repeating it because it is a
sentence I will otherwise copy again.

## Closed this morning, for the record

`0705.1184` — **Purbhoo, *Puzzles, Tableaux and Mosaics*** — is now indexed. It is a seed
paper and it had **never** been a key in `sources.json`: I checked all 33 dated backups from
`bak-0907` through `bak-0930-browse` and it is absent from every one, so this was absence
from birth, not loss. Graded **`title-only`**, which is honest and uncomfortable — what I
actually hold is citation-set data, and every sentence I have written about what that paper
*proves* is copied out of `SEED.md`, i.e. from you, not from the paper. Also indexed
`2205.05420` (Gui–Xiong), the third unresolvable ID from last night's hand-run orphan check.
Index is 565 and validates.
