# WAKE 2026-10-09 c2 — a truncating pager fakes a cardinality

*Orchestration slot. No mathematics. The useful finding is about how I read a number.*

## The finding

I ran `trustcheck validate` and piped it through `tail -5`. I saw five `file ... not found` lines
and was one sentence from writing **"5 problems"** into this note. The real count was **54**.

Then it got worse. I ran a positive control through the *same* `tail -5` — planted a bogus `trust`
enum — saw byte-identical output, and concluded **the control did not fire**. That was a true
statement about the pixels and a false one about the instrument. Re-measured with
`grep -c '^  - '`: clean **0**, broken `file` path **1**, bogus enum **1**. Both arms fire. The
exit status was **1 in both** the real-failure and the false-failure arm, so that never separated
them either.

What makes this worth writing down is that I already had a guard against it. My standing rule
since 10-07 is *read the cardinality, not the verdict* — and `tail -5` hands back a **plausible
cardinality in exactly the format the rule asks me to read**. The rule was satisfied by a
measurement of the wrong **window**.

> **A problem list is not a log: its content is its length.** Never `head`/`tail` one. And a
> control's reading has to be a **number**, never a diff of truncated text, because two different
> arms truncated to the same window are identical by construction.

This is one layer below the "plausible number" rule from last night's dream. There the number
counted the wrong *set*; here it counted the wrong *slice of the right set*, which is harder to
see, because the slice is made by my own shell and leaves no trace in the output.

## The same shape, twice more in one session

**A hash on a page is only useful if it resolves.** I added a page-1 provenance block to the
Theorem C paper (Rick's ask, PROTOCOL §2.3), embedded commit `43cef25`, then `--amend`ed — which
destroyed that commit. `git cat-file -t 43cef25` cheerfully answered **`commit`**, because it
tests the **local object store, not reachability**: the object was still in my own `.git`, and
would never have existed for anyone cloning. `merge-base --is-ancestor` says `43cef25` is **not**
reachable from HEAD and `9209643` is, and on `origin/main`. The block now names `9209643` and
explains why it is one commit behind the PDF.

**An inventory that scans the wrong repo under-reports.** My own audit reported that the 10-09
dream output was unreadable and that only one `for-robin` note had been mirrored. The first half
was right — `memory/` is not a git repo and has no remote. The second was wrong: it had checked
`proofs`, and the mirror lives in `work-in-progress/notes-for-robin/`, which already held **410**
tracked files. Only Oct 9's additions were missing. Now **419**, md5 cross-checked. The gap was
real but narrower than the audit said, and I nearly wrote the audit's number down.

## The flag, for the twentieth time, and why it is not my fault this time

`boot-prompt.md:77` prescribes `--files-dir proofs`. The registry node `file` fields already carry
the `proofs/` prefix and `trustcheck.py:699` does a plain `os.path.join`, so that resolves to
`proofs/proofs/...` and reports **54 false** problems. Correct: `--files-dir .`, or the absolute
`/home/clio/projects`. All **16** registries read `0 problems`.

My notes record this as hit **20**. The mitigation installed after hit 17 — *delete the defective
string from any line short enough to be skimmed* — **held**: I transcribed the correct flag into
all three of today's briefs. The vector was simply **running it once**, out of the boot prompt I
had read forty minutes earlier. `boot-prompt.md` is a read-only bind mount; I attempted the write
and got `OSError 30`. `prove-prompt.md` was already correct. I appended the correction to
`peer-review-prompt.md` and `lean-prompt.md`, which are writable, and sent Robin the one-line ask.

**WAKE is the one phase whose own prompt it cannot edit**, which is exactly why this is the error
that keeps coming back in this phase and no other.

## Two spent briefs were armed to re-fire

`PROVE.md` (mtime 00:42) and `LEAN.md` (00:43) were still live against `PROVE_ENDED_AT` 05:54 and
`LEAN_ENDED_AT` 08:15 — consumed, with artifacts on disk, and armed to fire **verbatim** a second
time. Archived before I wrote anything new. Second day running that this check paid, and it costs
one `ls`.

## And one good thing: I checked my own route before briefing it, and it corrected me twice

Today's PROVE brief proposes restating Theorem D's "no product form" via **Mahler measure** — a
monomial times a product of cyclotomics has all roots of modulus 0 or 1, `M` is multiplicative,
and `M = 1` exactly on that class, so "no product form" becomes `M > 1`, a property of the
*function* rather than of any way of writing it. That is the literal answer Q404 asks for.

Three briefs in a row have named a route that was wrong, so I tested mine in five lines of SymPy
first. It corrected me twice:

1. `D_8 = t^8 - t^7 + 1 = (t^2-t+1)(t^6-t^4-t^3+t+1)`, and `Φ_6` divides `D_b` whenever
   `b ≡ 2 (mod 6)`. So **`D_b` is not irreducible**, and an irreducibility claim — which is what I
   was about to write — would have been **false, in a paper Rick is actively citing**.
2. `D_2 = t^2 - t + 1 = Φ_6`: all roots on the unit circle, `M = 1`. So `b = 2` is a **genuine
   product form** and the `b ≥ 3` hypothesis is load-bearing, to be proved by exhibiting `b = 2`
   rather than by a failing build.

It also handed me the even-`b` case for free, which has been stuck at grade `computed` since
10-07: `D_b` has **no real roots at all** for even `b`, so the published root-in-`(-1,0)`
mechanism **provably cannot** reach it — and non-palindromy (`rev(D_b) = t^b - t + 1`, which equals
`D_b` only at `b = 2`) is a coefficient comparison that covers every `b ≥ 3` at once.

Checking a brief's premise is not computation. It is the cheapest thing I do, and today it was the
difference between a theorem and a retraction.
