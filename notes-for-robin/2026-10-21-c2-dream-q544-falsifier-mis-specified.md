# Q544's falsifier is mis-specified — please read before tomorrow's prove slot spends on it

**Dream 2026-10-21 c2.** Short note, one actionable item. Tomorrow's prove slot is armed on Q544
and the question as I wrote it this afternoon would have had me read a confirmation as a
refutation.

## What's wrong

This morning's G3 proof (`proofs/2026-10-21-c2-G3-boundary-diagonal-typeB.tex`, `thm:BD`,
L255–257) gives

```
  ord_{S^ε_m} Ã^X_{I,I} = [m ∈ I] · #{ a > 0 : a·t_m ∈ Δ⁺(X_N)  and  ε^a = 1 }
```

where `S^ε_m := {w_m = ε}`. **`ε` is the divisor parameter — it is not `q`.** `q` is transcendental
over ℂ in `F` and enters by exactly one route, as `lem:T`'s hypothesis `q ≠ ε^{-h}`.

The second factor is two predicates on the same index `a`, **intersected** — so the non-reduced
case doesn't simply double, it doubles *at one value of `ε`*:

| | `ε = 1` | `ε = −1` |
|---|---|---|
| `B_N` | 1 | **0** |
| `C_N` | 1 | 1 |
| `BC_N` | **2** | 1 |

I wrote Q544's falsifier as *"compute `ord_S` in `BC_N` at `q = 1` and get anything other than 2
for every `I`"* — **no `ε`**. At `ε = −1` the theorem predicts 1; at `ε = i` it predicts 0
everywhere (that `ε = i` arm is my own control). So two of the three `ε`-values the falsifier
admits return "not 2" *while the theorem is perfectly true*.

## The part I think you'll find more interesting than the bug

I went looking for where the `ε` got lost, expecting to owe a registry repair. I owe none:

- the **tex** is right (`cor:red`, L300–302: *"ord = 2 at `ε = 1` and 1 at `ε = −1`"*);
- **both registry nodes** are right — `general-master-formula-all-eps` carries the full
  `ε`-parametrised statement verified **306/306** over nine arms (`{B,C,BC} × {1,−1,i}`), and
  `reducedness-is-the-order-one` carries the `BC` row at 49/49;
- the **digest** is wrong in four places: the dream journal, the SUMMARY banner, the note I sent
  you this afternoon, and Q544's own statement.

So the fault is confined exactly to the compression layer. **My summaries are not downstream of my
registry** — they're a parallel channel written from memory of the session, and nothing validates
them against the field of record. Every guard I run checks an artifact or a node; nothing checks
the sentence I write *about* one. That's now §P-digest-3 in `topics/methodological-principles.md`,
and it amends the two earlier entries that treated digest error as a wrong *value* (too strong,
10-18; unconstrained in sign, 10-19). This one isn't a wrong value. It's an **unquantified** one —
a column reported as a table.

It also happened inside the cycle whose headline principle is *a count without its domain is
uninformative in both directions*. I wrote that sentence at 15:00 and violated it in the same
document, which I think is worth knowing about me: stating a principle in a document does not
immunise that document.

## The repair makes it a better question — but not the way I first thought

**First repair, rejected.** Re-aim Q544 at `lem:T`: *is `q ≠ ε^{-h}` irremovable?* It's **already
proved**, from the same session — node `BD-split-complementary-hypotheses` exhibits it as a lesion:
at `q := 1 = ε^{-h}`, `ε = 1`, the `m ∈ I` half is **inert** (1 → 1, 129/129) and the `m ∉ I` half
**breaks** (0 → 1, 129/129), both types, `N ≤ 5`. Re-aiming there would have spent a slot
re-deriving something I hold. (Lesson I keep relearning: grep my **own** registry before opening a
question.)

**Second repair, also rejected.** Declare Q544 pre-determined — `ε = 1`, `BC_N`: count 2,
indicator 1, colength `2^{N+1}`, done. This is wrong, and why is the actual content:

> The two "doublings" aren't two factors of one valid formula. Non-reducedness is a **value** of
> the formula. But `q → 1` at `ε = 1` means `q = 1 = ε^{-h}` — precisely where `lem:T`'s hypothesis
> **fails**. So it isn't a value of the formula, it's the formula's **breakdown**. The composition
> point `(BC_N, ε = 1, q = 1)` lies **outside the master formula's domain of validity**, and the
> formula therefore cannot predict it.

So Q544 is determined by nothing I currently hold. Each half is measured separately (49/49 in `BC`
at generic `q`; 129/129 in `B`/`C` at `q = 1`); the single point where both act at once is
**unmeasured**, because the only instrument that could measure it is inapplicable exactly there.
`2^{N+1}` is a guess with no derivation behind it. That's a genuinely open question with a cheap
arm, which is better than what I had.

**Corrected falsifier:** compute `ord_S Ã^{BC}_{I,I}` at **`ε := 1` *and* `q := 1`**, all `I`,
`N ≤ 4`. Multiplicativity predicts 2 for every `I`. Refuted by anything else — in particular 1 on
the `m ∉ I` sets, or an order not constant in `I`. The script exists; it needs **both**
substitutions, and the `ε`-stripped version concealed one of them.

## New question: Q546 — the colength may be a pair, not a number

> Is `(ord at ε = 1, ord at ε = −1)` a complete invariant of the ambient root system in this family?

The measured pairs `(1,0) / (1,1) / (2,1)` separate `B / C / BC`, and **no single `ε` does**: at
`ε = 1`, `B = C`; at `ε = −1`, `C = BC`. Only the pair resolves all three.

Why I think this matters beyond bookkeeping: the colength is the invariant the whole
boundary-divisor programme *reports*. If the pair is complete, then every colength I've stated as a
single integer is a **projection of a two-component invariant along an unstated `ε`** — and the
report should become a pair of numbers at the two special divisors. Falsifier: two distinct ambient
systems in the family with equal pairs. Arm: tabulate both columns in the script I already have.

One thing I'm deliberately **not** claiming: the `ε = ±1` column pair is the divisor-side shadow of
this afternoon's root-factor-ratio unification (`Z(1 + w^{-1}) = Z(2α) \ Z(α) = {−1}` is exactly
the `B`-vs-`C` entry at `ε = −1`). That makes it the **same** observation read a fourth way, not a
fourth witness — my own *convergence of instruments is not independence of evidence* from four
hours earlier. I've recorded the refusal in the connection file so a later cycle can't harvest the
table as fresh support.

## The one thing to action

**Before tomorrow's prove slot computes on Q544, read the corrected ledger entry** —
`questions/NEXT-FREE.md`, the `CORRECTION (dream 10-21 c2)` block under Q544. The c1 text is
retained verbatim above it (annotate, don't rewrite), so the block is where the live target is.

Also, separately and unrelated to the mathematics: today's review slot sent you and Rick a junk
one-character email. That's the fifth occurrence of the same fault, and I found out this cycle that
the fix I wrote on 10-11 named a capability `email_client.py` doesn't have — there's no subcommand
that reads the Sent folder, so the only verb available in the verifying position was `send`. Full
write-up in
`connections/2026-10-21-c2-dream-a-correction-that-names-an-unavailable-capability-cannot-fire.md`.
The working check is `ls -t /home/clio/mail/sent/`, and I ran it this time rather than writing it
down.
