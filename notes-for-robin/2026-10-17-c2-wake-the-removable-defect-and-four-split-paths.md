# For Robin — WAKE 2026-10-17 c2: a peer's hunch may demolish my frame, and it is a one-line corollary of my own theorem

> Written 14:50 UTC. Thinking session, no computation beyond verifying the brief.

## The mathematics, in one paragraph

Yesterday I proved `ρ^X = (1−q)²/((1−q w_a^h)(1−q w_b^h))`, the long-root collapse
multiplier, with `h` the length of the boundary root. Rick, independently and from Motegi's
`u`-symmetry rather than from my collapse ratio, proved a **stronger** statement the same
day (his Lemma QC): the collapse is an **identity**, uniform in the basis label, with
multiplier exactly my `ρ^C`. I checked the two agree symbolically. Then he attached a
hunch, flagged as a hunch: *Clio's poles measure the normalisation defect* — that a
geometric normalisation (Koncki's twisted motivic Chern classes, which Motegi matches in 15
of 16 entries for `LG(2,4)`) would have **no long-root poles at all.**

He is right about half of it, and the proof is one line of my own algebra. Write
`φ(w) = (1−q)/(1−q w^h)`. On the collision divisor `w_b = w_a^{−1}`, so

> **`ρ^X = φ(w_a) · φ(w_b)`, and `φ` depends on one variable, not on the pair `{a,b}`.**

That is the coboundary condition. So rescaling the basis by `∏_{m∈M}(1−q w_m^h)/(1−q)`
makes the collapse multiplier **exactly 1**, for every long-root pair at once. Verified at
`h = 1,2,3,5`. Rick's hunch, confirmed, for the **basis**.

And here is where I think he over-generalises, and it is today's prove target: that
rescaling factor is **regular and non-vanishing at the generic point of the collision
divisor**, so it cannot cancel a pole there. The defect of the **basis** is removable; the
poles of the **structure constants** should not be. Two different objects. His sentence
identifies them silently.

I have pre-registered the falsifier in `state/PROVE.md`: re-run Q491's census (Laurent ⟺
`|ν| − max(|λ|,|μ|) ≤ 1`, 225/225) on the renormalised constants and compare **the set, not
the count**. If the non-Laurent set moves, my "Pfaffian-category obstruction" — the half of
Q500 I claimed yesterday was the half nobody else has — is an artefact of my own choice of
normaliser, and I will say so in the title. **Two days after a retraction whose cause was
also a normaliser.** I expect the split to hold, which is historically when I am wrong.

## Four things about my own plumbing, and one is a question for you

**1. `memory/` is not a git repository.** Nor is `expository/`. `proofs/`, `reviews/`,
`work-in-progress/`, `lean/` and `tworow-d4-kernel/` all are, all clean, all pushed as of
09:58 today. But every dream journal, every `connections/` file, every `questions/` ledger
— seventeen days of the methodological record, including the three corrections below — is
**local-only in a Docker volume and invisible to you, to Lyra and to Rick.** CLAUDE.md is
explicit that only GitHub makes a file shareable. **Should `memory/` be a repo? That is
your call, not mine, so I have not created one.** If the answer is no, I would like to know
what the intended channel is, because right now the record exists only where nobody can
read it — which is the exact failure I spent this morning naming.

**2. Two directories exist at two paths each, and both are generator faults.**
`for-robin/` (found this morning: `memory/for-robin/` 10 notes, `projects/for-robin/` 8 —
the LEAN skill writes to the second). And now **`peers/`**: `projects/peers/` has 131
files, `/home/clio/peers/` has **0 — but carries the skeleton `rick/{proofs,emails}`.** The
second is worse than a split: `ls peers/rick/proofs/` returns a clean empty listing rather
than an error, so a session writing there sees success and silence. I caught it only because
an `md5sum` cross-check printed an empty destination hash. I have marked the decoy with a
`DO-NOT-USE-WRONG-PATH.md` and left the 131 files alone. **The fix is in the skills that
emit those paths, not in the files.**

**3. My slot statistics were wrong all day, and the error is the same one I congratulated
myself for catching this morning.** `clio.log` carries both `Starting Prove` (87) and
`Starting prove` (259). My c1 wake note measured the capitalised spelling only and
concluded "the review slot fires 92× in cycle 1 and 8× in cycle 2"; the c1 `LEAN.md`
concluded "the lean slot is roughly even, 38 vs 29". Case-insensitive, over 119 cycle-2
wakes: **prove ~100 %, browse ~100 %, dream 47 %, lean 27 %, review 10 %.** The lean slot
is *not* even — it is a 27 % slot, which changes how a cycle-2 lean brief has to be written
(it needs the same MERGE-not-replace header as the review brief, and now has one). *A count
measures a name*, third generation; and fixing the sampling does not fix the matching.

**4. This morning's new instrument has 19 false positives and is already disarmed.** The
dream prescribed detecting a died-mid-write session by set-differencing dates with a
`sources.json.bak-*browse*-pre` against dates with a `reading/*-browse*.md`, claiming zero
false positives over 17 days. Outside the window `10-06 → 10-17` it returns **nineteen**
dates — all because before 10-06 the browse logs had no `browse` in the filename. And run
today, `2026-10-17` is **absent from the difference**, because the dream's own 12:01
recovery wrote the very file the detector looks for: *the repair consumed the signal.* The
instrument worth keeping is the other one — `sources.json`'s mtime and md5 against its own
`.bak-*-pre` — because it is keyed on the target, which no recovery touches. All of this is
appended as corrections to the connection file itself.

## The operational item, and it is the one with a deadline

**Rick's refresh token expires around 2026-10-18 and needs `/login` from you.** My own
health mail has been counting it down — 2.5 days, 1.9, **1.4 as of 04:17 today**. I
escalated it on 10-15 and twice on 10-16, and then it **dropped out of my 00:15 wake mail
this morning**, exactly as the deadline got close. Nobody is currently carrying it, so I am
carrying it again, at the top of today's digest. It is in §6 territory and I should not have
let it decay.

## What is armed

- `PROVE.md` — the coboundary theorem and the basis/structure-constant split above.
  Fires ~100 % at cycle 2, so this is the load-bearing brief.
- `LEAN.md` — the level set `ρ = 1 ⟺ q = 0 ∨ w ∈ μ_h` over a field, with the roots-of-unity
  connection to Mathlib. 27 % slot, flagged MERGE.
- `PEER_REVIEW.md` — Rick's UID 819/820 packet, with the instruction to read **820 before
  819** (his filenames carry no version marker and 820 reverses 819's own conclusion six
  hours later). 10 % slot, flagged MERGE.
- Nine of Rick's claims registered in `proofs/registry/rick-q488-converse.json`, graded
  `peer-claimed` / `computed` / `speculative` / one `dead-end` (his own retraction, kept
  because a recorded objection is worth as much as an endorsement). `trustcheck` green,
  with a two-arm control that fires on both arms.

## One thing I would like your view on

`publishable-result` has not moved in **44 days** and nothing from the Q473/Q484/Q488/Q492
arc is in it, even though Q488 and Q492 have been through Rick extensively — which is
PROTOCOL §4.2's bar. The thing stopping me is §4.3: the email has to say *what the result
is and why it is ready*, and I am under a gate of my own making (Q504 — Digalaki and
Wheeler have a paper in preparation that may hold the positive half of my conjecture, and I
hold it only as a summary off a programme page with no arXiv ID). **Is a push to
publishable a priority claim, or just a timestamp?** §5.4 says the latter. If it is the
latter I should push the Q488/Q492 material now and let the timestamp do its work. If it is
the former I should read Digalaki–Wheeler first. I lean toward pushing, but I would rather
ask than guess.
