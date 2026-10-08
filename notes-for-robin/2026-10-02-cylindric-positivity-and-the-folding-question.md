# For Robin — 2026-10-02 (DREAM)

Four things, in order of how much I think you'll care.

## 1. There is an open conjecture in your thesis territory, unpublished, with its own reduction stated

**Oberwolfach Report 2/2026, Problem 7 (Alejandro Morales), Conjecture 4** — January 2026,
not on arXiv:

> `CPP_{λ/µ/d}(n)`, the number of **cylindric** plane partitions of cylindric shape
> `λ/µ/d` with entries in `1..n`, is a polynomial in `n` with **non-negative coefficients**.

Status: straight shapes done (Fomin–Kirillov), skew just done (Morales–Ferroni–Panova),
**cylindric open**. And Morales states the reduction himself: **it suffices to show the
linear coefficient is non-negative.**

Two practical notes. **OEIS has no cylindric-partition sequence**, so the table does not
exist publicly — building it is step one and is independently useful regardless of the
conjecture. And a caution I want to state before you or I get excited: a partition function
with positive Boltzmann weights gives positivity **of the count**, not of the **coefficients
of the polynomial interpolating the count in `n`**. Those are different objects. The
transfer-operator machinery is the right *shape* of instrument but it does not hand this over
for free.

Also from the same report, queued but not pursued — **Problem 10** (Konvalinka, from Igor
Klep): maximise `Δ(λ,µ,ν) = η(λ) − η(µ) − η(ν)` over triples with `c^λ_{µν} ≠ 0`. An
optimisation over the LR **support**.

**Oberwolfach reports were not on my `feeds.md` and were the highest-yield source I found
this week.** They are now.

## 2. My seed question was missing its second half, and I think the answer is a chain

I had been asking *why does `c^ν_{λμ}` admit so many independent combinatorial
interpretations?* The honest question is *why so many **in type A**, and what is the shared
reason they all stop?*

Tonight's answer-shape: **they don't stop in the same place.** Three walls, nested —

- **hives** fail outside type A (MO 33712, Knutson/Kamnitzer; "hives for BCD" is a recorded
  open problem);
- **KZJ `d`-step puzzles** run on simply-laced diagrams (`d=1 → sl_3`, `d=2 → spin_8`, and
  the `Z_3` puzzle symmetry *is* `D_4` triality, `d=3 → E_6`, `d=4 → E_8` non-minuscule),
  with **equivariance provably dying at `d=3`**;
- **canonical-basis positivity** fails off simply-laced — Tsuchioka gives explicit negative
  structure coefficients in `G_2`, `C_3`, `B_4`, so **Leclerc's Conjecture 52 is false**.

So `A ⊊ {minuscule, simply-laced} ⊊ {simply-laced}`, and the *gradient between the walls* is
more informative than any single rule. Grading honestly: the Tsuchioka result and the Dynkin
dictionary are both **`agent-summary`** in my index — read at one remove, not reproduced. The
chain is a hypothesis about the shape of the answer.

The reason I'm telling you rather than just filing it: **the crossing has a name and it's
quantum symmetric pairs (ıquantum groups) — folding.** And there may be a split worth
chasing: the *geometric* folding (Halacheva–Knutson–Zinn-Justin `1811.07581`, **self-dual
puzzles**, `Gr → SpGr`) keeps positivity trivially, because its coefficients are **tiling
counts**; the *algebraic* folding is where Tsuchioka's minus signs are. If that holds,
positivity is a property of **which coefficients**, not of the type.

The trap I'm watching for, and please hold me to it: `1811.07581` computes coefficients of a
**restriction map**, not type-C LR structure constants. Swapping those would be a real error
dressed as a result.

## 3. Five of my seed PDFs are unread, including Purbhoo — and that's the interesting part

`1811.07581`, **Purbhoo `0705.1184`** (a core seed paper), the Brauer loop pair
(`1001.3335`, `math/0503224`), and type-Ĉ `1410.0262` all sit at **`title-only`** in
`sources.json`. Yesterday my keyword selector named `brauer loop` and `orbital variety` as
never-swept and I dispatched **four web agents** to hunt them — while
`knutson-zinn-justin-2010-brauer-loop-scheme-orbital.pdf`, titled with both, sat on disk at
251 KB, unopened.

The cause is structural and worth a fix on your side if you agree: **my reading logs record
what I searched, never what I hold.** The selector is deliberately topic-blind so my own
verdicts can't fool it, which is right — but it has no notion of a shelf, so it fails toward
the *most expensive available action*. `sources.json` wants a **`local_pdf`** field, and a
keyword whose best match is a held-unread PDF should route to a READ, not a search.
`title-only` also conflates *couldn't read* with *haven't read*, which is a second
distinction worth having.

## 4. Three things about the container and the tooling

- **The Gmail MCP server was not connected in the PEER REVIEW session** — `ToolSearch` finds
  no `send_email`, despite `CLAUDE.md` listing it. **The review email to Rick never went
  out.** Full text at `reviews/2026-10-02-email-rick-nabla-transport.txt`, flagged in
  `state/OUTGOING-UNSENT.md`, pushed with the PDF so the links work without an attachment.
  **FPSAC 2027 abstracts are due 2026-11-15 — 44 days — and his Theorem H is gated on my
  verdict.** I'd like this sent, or the MCP reconnected so I can send it.
- **SageMath is absent from the container**, also despite `CLAUDE.md`. I built Macdonald `P`
  by diagonalising `D_1` instead, which made the instrument *more* independent — but don't
  plan a session around Sage without checking.
- **`trustcheck.py` is fine; my shell was broken.** I was one step from recording in my
  memory index that *your* `trustcheck` exits 0 on planted violations. `$?` after a pipe is
  the pipe's last command. `trustcheck.py:1964` has `return 1`, and unpiped it is **exit 1
  dirty / 0 clean**. The thing that actually needs your eye is the **wake routine's
  prescribed command**: `validate <registry> --files-dir proofs` fails every node's file
  check, because node `file` paths are relative to `projects/` — it wants `--files-dir .`.
  (And `registry_validate.py` genuinely lacks the flag, which is how I confused the two.)
