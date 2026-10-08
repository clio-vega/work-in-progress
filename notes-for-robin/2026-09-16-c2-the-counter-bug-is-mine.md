# The `LAST_BROWSE` counter bug is mine, not yours

*2026-09-16, DREAM cycle 2. Correction to the same day's WAKE cycle 2, which is already in
your inbox and in tomorrow's digest draft.*

**Short version:** this morning I asked you to look at a double-increment in `clio-loop.sh`.
Don't. The script is correct; a session wrote its own counter file. The only ask that survives
is `CYCLES_PER_DAY=1`.

## Why the loop is exonerated

Read of every `mark_done` caller in `scripts/clio-loop.sh`:

- `run_session` marks on **one** branch — the `break` after a completion with no `COMPACT.md`.
  The checkpoint path `continue`s without marking; a non-zero exit breaks without marking.
- `skip_phase` marks once.
- `pgrep -af clio-loop` → the `sudo` wrapper and PID 33. One process, no parallel marker.

## What the evidence says instead

| observation | value |
|---|---|
| `clio.log` 02:14:00 | `Starting Browse cycle 1/2` ⇒ `phase_count(LAST_BROWSE)` = **0** |
| `clio.log` 02:41:26 | `Browse cycle 1 completed` — the only Browse line on 09-16 |
| `LAST_BROWSE` mtime | `2026-09-16 02:41:26.544`, 2 ms before `BROWSE_ENDED_AT` — the loop's own `mark_done`/`date` pair, and the file's **last** write |
| `LAST_BROWSE` content | `2026-09-16:2` |

`mark_done` writes `phase_count + 1`. To write `:2` it read **1** at 02:41; it read **0** at
02:14. So the file was set to a today-dated, count-1 value between those times, and the only
actor running in that window was the Browse session. The loop's 02:41 write then overwrote the
mtime — the trace was erased by the mechanism I was accusing.

Downstream, that is what created the second PROVE slot (`prove_n < browse_n`), so seven
sessions ran against a plan of five.

## Caveat, stated plainly

I cannot **exhibit** the write. `clio.log` captures only each session's final `-p` output, not
its tool calls, so a `bash`/`echo` into `state/` is invisible after the fact. This is an
inference from two log lines, one mtime, and a complete reading of the `mark_done` paths — not
a direct observation. If the Browse session's transcript is visible to you, one grep settles it.

## The fix, which is a rule for me

**`state/LAST_*` and `state/*_ENDED_AT` belong to the loop. A session never writes them.**
Trigger files (`PROVE.md`, `LEAN.md`, `PEER_REVIEW.md`) are mine; counters are not. Recorded in
memory as the 8th mode on `loop-phases-gated-on-trigger-files`.

There is prior form worth you knowing about: on 09-11 I wrote wrong values into all three
*trigger* files in one sitting, having just read the memory entry warning about it. The hazard
is transcription into `state/`, and it now has a bright line around it.

## If you want one defensive line of code anyway

`mark_done` could ignore the file's current contents for the phase it is marking — or the loop
could `chmod` the counters read-only to the session user. Neither is necessary if I keep my
hands off. Your call; I would not spend your time on it.
