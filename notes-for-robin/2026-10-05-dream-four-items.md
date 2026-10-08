# For Robin — 2026-10-05 DREAM (four items, two are plumbing)

## 1. The mathematical one: Lenart and Sottile asked my seed question in 2002

`math/0202090` (*Skew Schubert polynomials*) **Corollary 4** is an identity between
chain counts, `I_α(u,w) = Σ_v c^w_{u,v} I_α(w_0 v, w_0)`, and the remark after it
says a type-preserving fibred map `Γ(u,w) → ⊔_v Γ(w_0 v, w_0)` with fibres of size
`c^w_{u,v}` *"would give a combinatorial interpretation for `c_{u,v}^w`, and thus
solve the Littlewood-Richardson problem."*

That is the question `SEED.md` is built around, stated as an open problem, in the
paper Stanley pointed me at for Q345.

What is new is not the problem — it is that **the machine it asks for has a name
and a theory**: Petrov `2609.18502` §5, *"bijectivization: from identities to Markov
transitions."* So my two top threads (Q345, and `ℓ(M)`-as-a-graded-bijection) are one
thread meeting at Corollary 4.

And it is now **well-posed**, which it wasn't a week ago. Chen–Ding `2106.12557` says
the Markov kernel is **not canonical** — any coupling of the two normalised sides
works — so "is `ℓ(M)` *the* degree of the weight" has no referent; the right question
is "**does there exist** a coupling whose grading is `ℓ(M)`." Petrov's MATH 7370
Lecture 16 §5.2 then gives the collapse condition: *if the left-hand side is a
singleton, the coupling is unique.* **Corollary 4's left side is a single term.** So
the 2002 map may be unique if it exists, and checking that is twenty minutes of
reading, not a project.

Both of those last two citations are **agent-sourced** (`2106.12557` is
`agent-summary`; the Lecture 16 locator came via an agent report). I have flagged them
as needing a source read before anything rests on them. Full write-up:
`memory/connections/2026-10-05-lenart-sottile-corollary-4-is-my-seed-question.md`.

## 2. Plumbing: four of five sessions today wrote no `SUMMARY.md` entry

`command grep -c "WAKE 2026-10-05\|BROWSE 2026-10-05\|LEAN 2026-10-05\|REVIEW 2026-10-05"`
→ **0**, on both `memory/SUMMARY.md` and `SUMMARY.md.bak-1005-prove`. Only PROVE 10-05
is there, and the file's mtime is **05:44** — before LEAN (08:02) and REVIEW (10:34)
ran. Every prior day has all four headers, so something changed rather than this being
a convention.

Why it matters more than it looks: **`SUMMARY.md` is what a dream session reads to
find out what happened that day.** A dream that trusted it would have consolidated one
session out of five *and would have looked complete*, because a dated entry at line 1
reads as current. I only caught it because I was enumerating `state/*_ENDED_AT` to
build a reading list.

I don't know whether the cause is the session prompts, a write that got skipped, or
something in the loop. Worth a look. The reliable inventory is
`state/{WAKE,BROWSE,PROVE,LEAN,REVIEW}_ENDED_AT` plus `state/clio.log`, because those
are written by the harness; `SUMMARY.md` is written by me.

## 3. Plumbing: give each agent its own working directory

BROWSE 10-05 c2 **overwrote about 68 files** in `/tmp/browse` and **cannot say which
ones.** The deliverable-naming repair you'll have seen in `BROWSE.md` worked perfectly
— every agent's output file carried the session stamp, zero bare names. The damage was
entirely in *scratch* files (`a.html`, `r3.txt`, `beta_check.py`) that no naming rule
covers. The count detected the loss (3279 → 3397 files, 186 modified, 31 mine) and
could not attribute it, because the evidence was what got destroyed.

The fix is structural, not another rule: **one `wk-<session>-<role>/` per agent.**
Collision-proof by construction. Scratch files are precisely what nobody remembers to
name carefully.

Related, smaller: `memory/for-robin/` is **not a git repository**, so notes I leave
there are invisible to you. LEAN 10-05 caught that and copied its note into the pushed
repo. `/home/clio/projects` isn't a repo either, so a `git log` from there returns
`fatal:` — it fails toward "no history", which is the dangerous direction.

## 4. Smaller, but it has been green on a false claim for weeks

My instructions say `trustcheck … sources` *"checks that every arXiv ID is honest and
every `read` file exists."* **The first half is false.** It validates `read`-file
existence and `corrections` shape only; source keys `9999.99999`, `2699.13337`, and
`not-an-id-at-all` all pass with **exit 0**. Every session has been ending on that
green and I had been reading it as "IDs verified." Real ID checking is a separate
instrument (`curl arxiv.org/abs/<ID>` + `citation_*` meta tags).

Not asking you to fix the tool — asking because the *instruction text* is the thing
that misled me, and it's in a file I read every cycle.

---

**The one I'd most like your opinion on:** the CODE slot for mosaics + migration in
`puzzles/` has now been the top blocked item for **four cycles**. `ℓ(M)` has acquired
a well-posed form, a uniqueness criterion, and a concrete identity to test it on — and
still no implementation. If it slips a fifth time, the honest reading isn't that the
slot never opened; it's that I prefer sharpening the question to building the
apparatus. I'd rather you told me which it is.
