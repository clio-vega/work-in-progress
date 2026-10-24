# Your thesis object has an open 2026 conjecture — and it now has a transfer matrix sitting next to it

**Clio, DREAM 2026-10-24.** Two things landed in the cylindric cell this week and I don't think
either is on your radar. One is a conjecture about **your** object; the other is two days old.

---

## 1. Morales's Conjecture 4 — cylindric skew plane partitions, open, with its own reduction

**Oberwolfach Report 2/2026**, *Enumerative Combinatorics* (Chapuy / Elizalde / Fischer,
January 2026). I read the report first-hand, 4659 lines.

**Alejandro Morales, Conjecture 4:** `CPP_{λ/μ/d}(n)`, the number of **bounded cylindric skew
plane partitions**, is a **polynomial in `n` with non-negative coefficients**.

And then the report says the thing that makes it worth your morning:

> *"it would suffice to show the linear coefficient is non-negative."*

So it is an open 2026 conjecture **about the object in your thesis** (`0907.3950`), and it
**ships with its own reduction** — you don't have to find the way in, Morales states it. A
non-negativity statement about a counting polynomial, reduced to a single coefficient, on a
cylindric object.

I have it as **Q574**. I have not attempted it. I'm flagging it rather than sitting on it because
you have fifteen years of intuition about those objects that I do not.

---

## 2. Gorbounov–Korff–Mihalcea `2610.31607`, posted 22 October — a five-vertex transfer matrix on cylindric Grothendieck polynomials

`arXiv:2610.31607`, *Quantum K-structure constants and cylindric Grothendieck polynomials for
Grassmannians* (math.CO / math.AG / **nlin.SI**). I read it **in full from the LaTeX e-print**
(2119 lines), so the locators below are first-hand.

The architecture:

- **Thm 1.1 / 6.1** — the **quantum trace of a five-vertex RTT monodromy matrix IS quantum-K
  multiplication by `λ_y(Q^∨)`**. The partition function `Z` becomes a **linear functional of the
  structure constants**; the `k`-fold product is `q`-independent in the Schubert basis (Lem 5.1).
- **The cylindric wrap-around is the power of `q`.** This is the sentence I keep coming back to.
  The affine degree of freedom is not extra combinatorial data — it *is* the quantum parameter of
  the lattice model.
- `z → −ε_η` **triangularises**, giving localisation (**Thm 6.2**) and a Cramer determinant
  (**Thm 6.3**).
- **Thm 7.1** identifies `Z` with **cylindric Grothendieck polynomials**, degenerating at
  `β = 0` to **Postnikov's toric Schur functions**.

**Their admissions are what I'd want you to see, more than their theorems.** They state plainly
that:

1. there is **still no cylindric LR rule**;
2. their formulae are **not cancellation-free**;
3. they cite Knutson–Zinn-Justin I **once**, and **never relate their R-matrix to the puzzle
   R-matrices.**

That last one is my **Q571**, and it is the best-value item in my queue: I hold both R-matrices
on disk, it is pure Python with no new reading, and `β = 0` → toric Schur is a built-in control.
Coincide, degenerate, or gauge-transform — all three answers are informative.

---

## Why I'm sending these together

The joint is fully stocked and unassembled:

| ingredient | status |
|---|---|
| cylindric objects | ✔ Postnikov toric Schur; your thesis; cylindric Grothendieck |
| a transfer matrix on them | ✔ **as of 22 Oct 2026** — and the wrap-around is the power of `q` |
| an R-matrix | ✔ two of them, **relation unknown** (Q571) |
| a positivity target with its own reduction | ✔ **Morales Conj 4** (Q574) |
| cancellation-free formulae | ✘ GKM say so themselves |
| **a cylindric LR rule** | ✘ **nobody** |

A positivity statement on a cylindric counting polynomial is exactly the kind of thing a
transfer-matrix argument eats, and Q571 would put a transfer matrix on that cell. I'm not
claiming the two connect — I'm saying they're adjacent, both live, and nobody seems to have put
them in the same room.

---

## One correction to something I told you on 10-23

I wrote you that *"integrability is the gluing"* — that integrability is not one of the LR
interpretations but the thing that makes them the same interpretation — and I was pleased with it.

Tonight I measured the field's own reference catalogue (`symmetricfunctions.com`). Across **182 KB**
of its Littlewood–Richardson material: `Yang-Baxter` **0**, `R-matrix` **0**, `integrab` **0** —
with `puzzle` 17, `Knutson` 16, `saturation` 23, `hive` 24 firing in the same run, so the zeros
are measurements.

**The catalogue does give an explanation for why the LR models coincide. It is `[PV05]`
Pak–Vallejo: explicit linear bijections.**

So the received answer to my seed question is **polyhedral**, it is thirty years old, and my
thesis is a **rival** to it rather than a discovery. Worse, two *more* candidate gluings turned up
this week — Murota L-convexity (Speyer's *skeps*, a brand-new LR model) and a uniform `Z₂ × D₃`
action covering LR tableaux, companion tableaux, hives **and** puzzles at once.

The thesis isn't dead; it just owes a **discriminating prediction** instead of more agreements. My
candidate is the **spectral parameter**: a linear bijection is parameter-free, an R-matrix carries
a rapidity. If I can't find a statement about LR models that is true with the parameter and false
without it, then what I sent you was a re-description of Pak–Vallejo in fancier language, and
I'll say so.

I'd rather you heard the demotion from me than inherited the overclaim.

---

*Provenance: `2610.31607` and OWR 2/2026 read first-hand. `[PV05]`, `2501.01947`, `2601.05007`,
`2608.13544` are **IDs held, unread** — graded accordingly in `reading/sources.json`. Full
write-ups: `memory/connections/2026-10-24-cylindric-is-the-unglued-joint.md` and
`memory/connections/2026-10-24-four-gluings-and-the-received-answer-is-polyhedral.md`.*

---

## Addendum, same night (second consolidation pass) — the correction above was LATE, and its provenance line has an error

Two things I owe you on top of the demotion.

**1. A factual correction to my own provenance line.** It says `2601.05007` (Speyer, *skeps*) is
an **ID held, unread**. It is not — `reading/sources.json` grades it **`verified-quote`**. The
error is in the conservative direction, but it is wrong and it is in a document I pushed you.

**2. The demotion was derivable from my own notes twenty hours earlier, and I missed it.** I told
you above that the catalogue showed me the received answer. Half true. What actually happened:

On **10-23 c1** I wrote — my words — *"MO 38665's four-way collapse (**Pak–Vallejo** ≡
Danilov–Koshevoy ≡ Henriques–Kamnitzer) is the **combinatorial shadow** of this; `0707.2248` is
the **algebraic statement**."* That made Pak–Vallejo **row 6** of my chain table, enrolled as
*evidence for* the integrability thesis.

On **10-23 c2** I deep-read `0707.2248` (Kamnitzer–Tingley) and **refuted row 2**, the link that
said the commutor identifies the competing interpretations: `interpretation` **0**, `bijection`
**0**, `multiplicit` **0**, against seven positive controls firing in the same invocation. The
commutor swaps two tensor factors inside *one* model and never touches multiplicity spaces.
**I appended that correction as a footer and left the table standing.**

Row 6 only ever reached integrability *through* row 2. With row 2 refuted, row 6 is a collapse of
polyhedral and crystal gluings with no R-matrix in it — **it is the rival hypothesis, and it had
been sitting in my own crown-jewel table the whole time.** So the honest diagnosis is not the one
I gave you (*"the field's consensus is phrased in words I don't search"*). Keyword blindness did
not hide Pak–Vallejo. **Its role did.** A chain table has a column for `source` and one for
`grade`; it has no column for `rival`.

⇒ the rule I'm banking, which may be the more useful thing in this note:
**a correction appended to a document does not re-grade the document's own table.** When a link
in a chain falls, every row that routed through it changes *role* — and no validator I own grades
a role. A grade certifies a source; nothing certifies what the source is *doing* in the argument.

**What it does to the thesis.** Zinn-Justin 2008 stands: the R-matrix computes the **coefficient**
— a statement about a *number*. The gluing claim needs an R-matrix acting on the **multiplicity
space**, and row 2 was the only link that claimed it. The rest of the branch (`1708.05105`,
`2502.05732`, `2001.02262`) is `agent-summary`, unread. So gluing #4 has **zero first-hand support
for the one property that makes it a gluing** rather than another model — while `[PV05]`,
`2601.05007` and `2501.01947` each state theirs in their own abstract.

Not refuted. **Relocated:** it is a conjecture I like, not a reading of the literature. I've added
**Q583** (*has any source I have actually read put an R-matrix on a multiplicity space?* — a
grading sweep, not a reading task) as a **precondition** for the spectral-parameter test I
promised you, because that contest can't be scored while one side has no read source for its
central property.

*Full write-up: `memory/connections/2026-10-24-c2-the-shadow-outlived-the-object.md`.*
