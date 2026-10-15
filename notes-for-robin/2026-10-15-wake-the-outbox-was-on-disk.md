# Wake 2026-10-15 — the instrument I asked for was already on disk, and a timeout nearly ate a proof

## ★★★ I reported a missing capability and then asked another person to build it

Yesterday I told Robin, in writing, that there was *"no instrument that closes the loop"* on my
outbox, and asked him for a working sent-mail read or a local append-only send log.

**`/home/clio/mail/sent/` holds 408 JSON files**, one per send, newest
`20261014_145047_langer.robin.json` (10-14 14:50), each recording to / cc / subject / body /
attachments. It has been there the whole time.

The reasoning that failed is worth more than the fact. `[Gmail]/Sent Mail` **is** broken — 17
messages, newest 10-04 — and that is true and was measured. From it I concluded the *capability*
was absent. ⇒ ***A dead instrument licenses a search for another instrument, not a conclusion
that the measurement is impossible.***

**Fourth instance this month, and the first where I asked someone else to build what I held:**

| instance | the dead instrument | what it forbade |
|---|---|---|
| 10-12 | `sources.json`: *"PDF binary did not parse"* | re-fetching a file that **always** parsed (38,506 words) |
| 10-12 | `1704.00154` absent by ID, author, content | reading **my own `verified-quote` entry**, which answered it factor by factor |
| 10-12 | a hand-typed 3-root holdings audit | seeing `/home/clio/data` — **670 PDFs, 31%** |
| **10-15** | `[Gmail]/Sent Mail` | **`ls /home/clio/mail/sent/`** |

Rule, installed: **before reporting that a capability is missing, `ls` the place it would live.**
A recorded negative is worse than a gap — a gap invites a look, a negative forbids one.

**It paid for itself inside the hour.** A bucketed census against `mail/sent/` discharged **11 of
15** candidate debts by citing specific files — and surfaced a *genuine* one the inbox could never
have shown: **no send exists after 14:50 on 10-14, and the Q460 proof finished at 19:34**, so
yesterday's result had never been sent to anyone. The single Q460 mention in my outbox is in the
14:50 mail, where it is a *plan*. Sent to Rick this morning, 307.0 KB, a day late rather than a
duplicate. ⇒ ***A census that can only invent phantom debts also cannot find real ones; the same
blindness runs both ways.***

## ★★ Two readings of one file are not a control

My peer-review brief, armed on Rick's 207b `e_k ⋆ e_r` note, said:

> *"Both PDFs are the same size; treat `_2` as a re-download artefact."*

True, and useless. The two files it compared are **md5-identical** (`709cf23c…`): it measured one
document twice and called the agreement a check. Meanwhile Rick re-sent the note on **10-08
(UID 790) with four defects repaired, under the same filename** — `347,576 B` against
`305,497 B`, md5 `71bcf942…`.

Had the slot opened I would have re-reported defects he fixed a week ago, in a document whose own
first page credits me for reporting them. ⇒ ***A filename is not an address. When a neighbour
re-sends, the newer copy keeps the OLD name — compare md5 ACROSS UIDs, never within one.*** The
brief's own stated guard (*"print the byte size beside the filename"*) could not fire, because the
domain it printed was one document wide. Same shape as the holdings-root fault.

Also: the brief said Rick had re-raised this **five** times. A subject scan over all 804 messages
says **seven** (UIDs 779 and 790 were missing). Seventh unconsumed review slot; his FPSAC 2027
deadline is **11-15, 31 days out**.

## ★★ A 60-minute slot that commits at minute 55 is invisible for 55 minutes

```
[2026-10-14 21:41:43 UTC] Starting Lean cycle 2/2...
[2026-10-14 22:41:47 UTC] Lean cycle 2 timed out.
```

That session **proved D3** — the region condition, HKKO `2301.13117` Prop 2.7, the last of the
three-way split of `prop:dict` — compiled it (`.olean` 457,624 B at 22:29:57), captured its axiom
evidence at 22:35:44, and **committed nothing**. 17,847 B of finished, sorry-free Lean in a
working tree where one `git clean` ends it.

Rescued: `tworow_d4_kernel` **`67b890e`**, `proofs` **`066f8bb`**, both pushed and both verified
with `git ls-remote --heads origin main` against local `HEAD`. 20 declarations, no `sorry` as a
term, 34 axiom records with `sorryAx` absent, two *independent* witness checks and two ablations
that fire. Also deleted an orphan `ScratchPlant.olean` — no source on disk, untracked, unimported,
and the **only** `sorryAx` bearer in the build cache, so `strings | grep sorryAx` is a valid
instrument again.

**Deliberately not graded.** This is an orchestration session and I did not re-run the checker, so
grading here would be a published grade with no reading behind it. The commit message says so in
those words and `LEAN.md` is rewritten to grade rather than redo. ⇒ The usual fault is *grading
without pushing*; this is its mirror, and the repair is the same sentence read backwards:
***commit as soon as a declaration compiles, not at the end of the session.***

## ⚠ A bump goes to one PAST the last number used

`NEXT-FREE.md`, my question allocator, read **472** while **Q472 was already allocated**. Last
night's browse took five numbers (468–472) and bumped by four — and wrote the error down **twice,
consistently** (§9 header and §11 close), which is why nothing caught it. Off-by-one in the
direction that *collides*. Repaired to **474**; this session took **473**.

## Today: Q473 — closing a published conjecture by closing its one missing lemma

**Garbali–de Gier–Mead–Wheeler, `2312.14348`**, *Symmetric functions from the six-vertex model in
half-space*. Their Conjecture `conj:F-orth` is an orthogonality statement, and at **line 3907**
they reduce it to exactly one thing:

> *"it remains conjectural as we have not established that the functions
> `lim_{c→∞} G_κ(x_1,…,x_L)` are linearly independent."*

Close the independence, their conjecture becomes a theorem. **Wheeler is a seed author**;
`Pfaffian` **44** hits against `determinant` **2** — the minor-summation toolkit my own index
recorded as **0 of 861 sources** on 10-13, two days before I found a seed author using the word
44 times.

Why three hours and not three weeks: their sum-over-subsets Theorem is fully explicit, the
`c→∞` limit is printed, and **I reproduced that printed factorisation by hand while writing the
brief** (`h = ac(1-x²)/((a-x)(c-x))` ⇒ `1-h → x(1-ax)/(x-a)`, matching their
`∏ x_i(1-ax_i)/(x_i-a)`). So `lim G_κ` is a finite sum of rational functions SymPy can hold — no
contour integrals anywhere.

And the mechanism is **yesterday's instrument reused**: `κ` enters only through the `y`-alphabet,
so `G_κ` cannot involve `y_j` for `j > max(κ)` — a filtration for free — and the poles should read
off `κ` exactly as a pole order read off the arc type in Q460. ***Full rank IS linear
independence***, and three sessions of capacity bounds were three sessions of building rank
engines.

Two honesties, pre-registered. The **intro** of that paper states the lemma *without* the
`c→∞` limit and the **in-text** version states it *with* — the limit is the whole difference
between hard and tractable, and the loose paraphrase is the one a careless reading takes. And the
authors say *"we plan to return to its proof in a later text"*: **they have claimed the problem.**
I am doing it because it is a stated open problem in a published paper; contact is Robin's call
under PROTOCOL §1 and §5.

## Held, not acted on: MathOverflow vs PROTOCOL §5

Last night's browse set my first task as posting MO-509068 — in hand since June, greenlit twice
by Robin **in June**. PROTOCOL is dated **2026-08-31** and supersedes earlier informal practice,
and §5.1 makes publication Robin's act. MO is not in the enumerated list but is public posting
under an identity. ⇒ I read the June permission as void and the question as open. **Not posted;
asked Robin.** Four months of deferral is not an argument for acting without an answer.
