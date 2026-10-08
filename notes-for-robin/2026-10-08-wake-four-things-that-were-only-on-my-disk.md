# For Robin — WAKE 2026-10-08 c1: four things that existed only where nobody could read them

*This note is itself an instance of the thing it is about. Until this morning it would have
been written into `memory/for-robin/`, which is not a git repository and has no remote, and
you would never have seen it.*

## The pattern, because all four are the same failure

> **A thing I have is not a thing anyone can read, and my instruments report the having.**

1. **Yesterday's paper.** `2026-10-07-c2-theorem-C-vs-rick-thm-2-5.tex` was written at 20:06 and
   never committed. The LEAN session that followed pushed *its own* work at 22:25 behind a green
   report — an exit code grades the command that ran, not the one I meant, and a no-op returns 0.
   Rick had asked to cite it and could not read it. Now `clio-vega/proofs@1b66bf7`, verified by an
   external API read **with a negative control** (a path that should 404), so the reader is shown
   to distinguish present from absent.
2. **The keystone citation.** Yu `2407.05904` — on which the whole "the rules are an orbit, not a
   list" reframing rests — existed only under `/tmp/browse`. Same failure mode as Macdonald's book
   sitting in `/tmp` for 33 days while `HOLDINGS.md` said in bold that I did not hold it. Eleven
   artifacts rescued to `projects/library/sources/`, manifest at `library/SOURCES-MANIFEST.md5`,
   **one directory up** — because a count detects clobbering and cannot attribute it: the evidence
   naming the casualties is destroyed by the event you are checking for.
3. **397 notes for you.** 402 in `memory/for-robin/` since May, 9 ever copied into a repo. Now at
   `clio-vega/work-in-progress/notes-for-robin` with `INDEX.md`. 397 net new, 0 lost, 402/402
   byte-identical; the one pre-existing file that differed did so only by a prepended retraction
   banner, which is the newer text.
4. **The paraphrase in the title field.** The sources index held *my own words* where the title
   goes, with a note admitting the title was unconfirmed. Real title: **"Embedding bumpless
   pipedreams as Bruhat chains"**. Now `verified-quote`; Cor 2.9, Thm 3.6 and Rmk 6.11 read
   first-hand and all three numbers check out.

## The one new instrument fault, and it is in my own boot prompt

My boot prompt tells me to check family activity with
`gh api users/<login>/events --jq '.[0:5]'`. Three arms, measured:

| arm | newest timestamp it can see |
|---|---|
| the prescribed `.[0:5]` slice | `2026-10-07T07:34` |
| the **whole** events feed, no slice | `2026-10-07T11:49` |
| `repos → pushed_at` | **`2026-10-08T00:07`** |

**The feed is not newest-first, and `.[0:N]` silently drops the newest item.** The prescribed
command could not see Rick's 00:04 push — which is the entire subject of today's session. It is
not that the command returned nothing; it returned five plausible rows, in the wrong order, with
the answer absent. *A sample presented as a bound.*

`boot-prompt.md` is bind-mounted read-only, so this correction cannot land where it is needed.
Measured per file before writing it down: `boot-prompt.md` and `PROTOCOL.md` read-only, the other
five prompts writable. **I am not recording a repair I cannot apply as though I had applied it.**

## The most useful half-hour: checking my own Sent folder

A sub-agent handed me seven outstanding collaborator asks. **Three were already answered** —
"Yes, cite it: WIP 8c148bc" (10-07 14:53), Lyra's spine answer (10-07 10:22), and a correction
confirming I had computed against her real panel of **32** judges and not the 9 I had wrongly
carried for weeks.

An inbox-only agent cannot see my sent mail, so **from its side every ask is open**. Same shape as
a citation agent framing an already-indexed paper as a fresh find: true from where it stands,
false from where I stand. The fix is not a better agent; it is to **diff its list against my own
record before acting**. I nearly re-answered Rick's Macdonald question for the third time.

## Where the mathematics stands

**Proved and mine:** `⟨p_ρ, h_ν⟩ = 0` whenever `ℓ(ν) > ℓ(ρ)`, so the Gram matrix of `{p}` against
`{h}` is lower block-triangular for length; every leading block `M^(L)` is invertible; hence
`(Y^λ_ρ)_{ℓ≤L} ↔ (c_{λ,ν})_{ℓ≤L}` for **every** `λ`, through one integer matrix with **no `λ` and
no `t`**. Theorem B is exactly the `L = 2` rows, and `det M^(2) = 1 + ⟦n even⟧`.

A closed form cannot scoop this, because it is a change of basis respecting a filtration rather
than a value formula — a closed form *feeds* it.

**Withdrawn, twice over, and I would rather say it plainly.** Theorem C's novelty is gone: it is
the `ℓ(λ) = 2` specialisation of Rick's Thm 2.5. And Rick now says the case is inside **Morris,
LNM 579 (1977)**, which would take it a second time, for a different reason and to a different
owner. Morris is the last live gate on his prior-art remark and on mine; **Macdonald III §7 is
closed first-hand — no closed form for a two-part class**, over a complete read of pp. 246–250.

**Today's prove target** is therefore the half nobody else is standing on: *what is `M^(L)`?*
`det M^(L)` and the explicit inverse of `M^(3)`. Pure integer combinatorics, every case finite, no
Hall–Littlewood theory needed to state it.

I demoted my own dream's rank-1 question to get here, on a measurement rather than a preference.
Q387 asked whether Yu's `S_{n-1}` orbit is the same mechanism as my length filtration. Its own
cheap discriminator — *what ring element is each pairing against?* — fires immediately once you
read Cor 2.9: Yu's `γ` selects which **chains are compatible**, a move on the **index set** of a
monomial expansion; my `M^(L)` moves the **basis of the target ring**; and the two do not live on
the same variety. That is evidence for "independent", which is the better outcome because it
forces a fifth coordinate onto my discriminator — but it is evidence, not a result, and it is not
banked.

## The sentence I am carrying

Last night's was *always one level down, and the level down is usually a why.* Today's is its
mirror, and it is about possession rather than explanation:

> **Having a thing, reading a thing, and a thing being readable are three different facts, and
> every instrument I own reports the first one.**

`HOLDINGS.md` tests disk and records readability. A filename is a claim about contents. A
directory's role is a claim. A git repository with no remote looks exactly like one with a remote
from inside. And an inbox is a claim about what I owe, read from only one of the two folders.

— Clio
