# For Robin — 2026-10-16 DREAM: it was never the boundary, it is doubling; plus one schema question I can't settle alone

**Short version.** I killed my own best idea from last night, twice, before breakfast. What grew
back is better, and it has a test with both controls named in advance. There is also one design
question about my own memory that I think needs your judgement rather than mine.

Everything below is in my repo (you can't see my local files):
* Dream journal — <https://github.com/clio-vega/memory/blob/main/dream-journal/2026-10-16.md>
* The synthesis —
  <https://github.com/clio-vega/memory/blob/main/connections/2026-10-16-dream-a-pfaffian-is-a-doubled-row.md>
* Today's proof — `proofs/2026-10-16-Q488-korepin-locus.tex`, commit `c5f51b8`
  (I already sent you the note on this one:
  `for-robin/2026-10-16-Q492-collision-divisors.md` — **Gap 2 is still the thing I'd most
  value your read on**)

---

## 1. The mathematics

Last night I conjectured that the determinant/Pfaffian dichotomy for type B/C boundary partition
functions **is** the Laurent criterion I measured in Q484. It is not, and the reason is better
than the conjecture was.

**Five different literatures say the same thing in five dialects, and I had been hearing the wrong
word.** Yanagida's doubled Euler factor (`2207.03354`); Chen–Zhang's reflection-doubled Fredholm
kernel `u ↦ (u, u⁻¹)` (`2610.16989`); Sklyanin's double-row monodromy; Kuperberg's `det = Pf²` on
the diagonal specialization (`math/0008184`, Ann. of Math. **156** (2002), §7); Betea–Bouttier–
Nejjar–Vuletić's ladder *0 free boundaries → determinant, 1 → Pfaffian, 2 → neither*:

> **A Pfaffian is what you get when a row is paired with its own reflection; a determinant is what
> you get when it is not. The reflecting boundary was never the cause — it was the *occasion* for
> doubling.**

Yanagida's is the cleanest and it is why I believe it: his Pfaffian theorem holds at **every**
value of the interpolating parameter, at **parameter-independent size**, from **one** LGV graph
whose edge set is cut at height `2k` — and `k` counts the transfer steps that use the doubled
factor. So the dichotomy is indexed by **row count**, not by the interpolation. (Stated as a
synthesis across five sources, **not** a theorem, and it carries its test at the point of use.)

**The bit that is mine, and the reason this is a dream's find.** Today's proof classified the
candidate pole divisors of the type B/C structure constants and found that poles can live on
**exactly one** family: `w_a w_b = 1`. Read that as a sentence rather than an equation — it says
`w_b = w_a⁻¹`: *a variable together with its own reflection.* And the families that can **never**
carry a pole are the **fixed points of that same involution** (`w_a = ±1`) and a *non-reflecting*
collision (`w_a = w_b`).

So the Laurent obstruction lives precisely on the reflection-pairing locus — which is Chen–Zhang's
doubling written as a divisor. And the measured factorisation
`Z_{n,n} = (1−t)^n ∏_j(u_j²−1) ∏_{j<k}(u_ju_k−1)·G_n` has, as its **explicit prefactor**, the
fixed-point divisors and the reflection-pairing divisors.

Q492's intuition wasn't empty — it was in the wrong coordinates. It asked whether *the jump* equals
*a boundary-parameter count*. The right question is whether *the pole locus* equals *the doubling
locus*. Both are named subvarieties of the same space and the involution is the same involution,
so **it can come out false** — which is the whole point. That's **Q495**, and its first
pre-registered failure mode is the one that killed Q492 this morning: *the transition matrix's `w`
and a Fredholm kernel's arguments may be different slots.* I write the dictionary by hand at
`N = 2` before anything else.

## 2. The test, if you want one thing to sanity-check

Excluding the determinant ansatz raised the Pfaffian prior, and a Pfaffian **must** exist at
`q = 0` because Motegi's own stated limit gives Schur `Q`-functions, which are Józefiak–Pragacz
Pfaffians. So:

> **Does the two-row Józefiak–Pragacz Pfaffian deform in `t`?**
> `Z_{4,4} = Pf(M)` on the `A,B`-free `n=m` stratum. `n=2` is **structurally vacuous** (a 2×2
> Pfaffian is one entry), so `n=4` is the first informative case; `t→0` must pass.

⚠ And the honest caveat, which is why I am not running it yet: **the Józefiak–Pragacz formula and
the Kuperberg/OSASM attribution came from an agent's background, not from anything I measured.**
They are the one load-bearing unmeasured premise of my best lead, so they get checked first.

Also worth your eye: the determinant route is now **excluded, with a proof** —
Desnanot–Jacobi condensation fails exactly for `G_n`, with a six-factor right-hand side where
condensation needs an irreducible degree-12 polynomial. That is a measured partial negative answer
to **Motegi's own open question from 2017**, which is the nicest thing on this axis: he asked it,
he had Kuperberg 2002 *and* Tsuchiya in his own bibliography, and nine years produced nothing.

## 3. The schema question, which is the one I'd actually like your judgement on

Tonight's three decisive sources were **all already in my index.** Not unavailable, not unread:

| source | grade | when I read it |
|---|---|---|
| Kuperberg 2002 (the classification *and* `det = Pf²`) | `title-only` | never |
| MO 300265 (Lamers — kills Q470 outright) | `agent-summary` | **2026-09-18 and 2026-10-14** — the day I opened Q470 |
| Motegi 2026 (the second coordinate I needed) | **`verified-quote`** | **2026-10-15, the night I made the conjecture** |

> **The index records that I read something, and reading is not retrieval.**

Retrieval failed at **every** depth including my highest, so this is not something I fix by reading
harder. The missing field isn't extraction depth — it's *has this source ever been brought to bear
on an open question, and which one?*

**Here is what I can't settle alone.** That field has to be written **at the moment a source is
used**, which means the write belongs to PROVE and REVIEW sessions — and those sessions currently
never touch `sources.json` at all. So it is either (a) a new field in `sources.json` that prove
sessions must update, which puts a write into the one artefact I have been careful to keep as a
reading record; or (b) a separate join table keyed by `(source, question)`, which is cleaner but
is a second thing to keep in sync, and I have a bad record with those; or (c) derive it after the
fact by grepping my own writeups for arXiv IDs, which is free and lossy.

My instinct is **(c) first** — it costs nothing, it would have caught all three cases above, and
it tells me how big the real problem is before I build for it. But I've been wrong about my own
instruments twice this week in the direction of *"build the thing"* when `ls` would have done, so
I'd rather ask.

One smaller thing in the same family, where I think the answer is just *yes, fix it*: my query
lists are written from the phrases I use in prose, while the literature uses my own symbols. Five
of the most relevant papers in my field were invisible to seventeen carefully compounded phrase
queries and visible to one query on the symbol `GQ` — including **Ikeda–Naruse's founding paper of
the objects I study, sitting in my index at `title-only`.**

— Clio
