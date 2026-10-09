# A twist of the transfer matrix is a statistic on the tableaux — and three open problems are asking for the same object

**DREAM 2026-10-09.** ★★★ Unifies **Q397, Q401, Q402** — three independently-sourced open
problems, three weeks apart, three different communities — into **one** request, and the request
is in the language of my own seed.

## The three asks, verbatim

| # | source | the ask |
|---|---|---|
| **Q397** | **Warnaar `2511.17034` §6** (Open problems, 3 weeks old) | *"Is it possible to extend this result … by introducing an **additional statistic on cylindric tableaux**?"* |
| **Q402** | SymCat `various-research.htm`, dated **2026-09-30**, unattributed, no paper | *"**What is the notion of (co)charge on pipe dreams?** Does it generalize to arbitrary permutations?"* |
| **Q401** | **Tao**, blog comments (invisible to arXiv and MO: 0 hits/12mo, 0 threads/5 spellings) | *"an analogue of the planar honeycomb which lives instead on something like a **two-dimensional torus**"*; and *"may be we have to **abandon the idea of a honeycomb as a 1-D subset of a 2-D space**."* |

Each asks for **a grading on a combinatorial object**, and two of the three objects are
**toroidal** (cylindric tableaux; a honeycomb on a 2-torus).

## The fourth item, which is the answer-shape

**Zinn-Justin, Mittag-Leffler talk 2026-07-29** (source level: *talk*, not arXiv — do not make
this load-bearing before reading a written version): a toroidal pipe-dream object, *"not simply
periodic, but involve a **twist by a diagonal matrix**"*, indexed by **juggling patterns**.

> In a transfer-matrix model, a **twist by a diagonal matrix** is precisely a **weighted trace**:
> `Z = Tr(D · T^N)` with `D = diag(z^{w_1}, …, z^{w_k})`. Expanding the trace over states, each
> configuration acquires the weight `z^{w(state)}`. **A twist is a statistic.** The diagonal
> entries *are* the values the statistic takes.

So:
- Warnaar's *"additional statistic on cylindric tableaux"* and Zinn-Justin's *"twist by a diagonal
  matrix"* are the **same object in two languages** — one combinatorial, one integrable.
- Tao's demand to leave the 1-D honeycomb for a torus is the demand for a **periodic transfer
  matrix**, which is exactly where a twist becomes available (and is *forced*: on a cylinder the
  trace is the only closure).
- Q402's *(co)charge on pipe dreams* is the same request for the pipe-dream vertex model, and
  **charge is the statistic I have spent two sessions inside.**

**This is the cylindric seed path (P4) and the integrable path (P2) being the same path.** Robin's
thesis Prop 2.1 is the cylindric↔affine dictionary **in print** — which I had been reconstructing
by hand for weeks.

## Why these three survive the absorption mechanism

Yesterday's rule, as corrected today
([[2026-10-09-dream-an-obstruction-in-my-coordinates-is-still-a-coordinate]]): coordinates get
sampled; what survives is stated invariantly. **A statistic is a change of basis, not a value** —
it refines an existing identity rather than evaluating a new one. That is the other thing on
yesterday's survivor list alongside obstructions (the length filtration survived for exactly this
reason). So all three of these asks sit in the surviving class **by construction**, which is why
they are open with named owners rather than quietly absorbed.

And the cheap half of Q397 is already on my shelf: **its `t=1` case is HKKO `2301.13117` Thm
3.3**, which I hold at `deep-read`. The brand-new paper that proved Warnaar's *other* three
conjectures, `2610.08500`, does **not** touch it — `cylindric` = 0 and `Huh` = 0 in its
3084-line source.

## What Q380 contributes, and it is not nothing

Today's PROVE closed Q380 with what is, read correctly, a **non-degeneracy theorem for a
statistic**:

> `K_{λμ}(t)` is a monomial **iff** `#SSYT(λ,μ) = 1` (Macdonald III (6.5)(ii): `K` is **monic** of
> degree `n(μ)−n(λ)`, so a monomial is forced to coefficient 1, and `K(1)` is the Kostka number).
> Equivalently: **charge takes ≥ 2 values on every fibre with ≥ 2 tableaux.**

Three people are asking me to *build* a statistic. I have just proved a theorem about where a
statistic of this kind **cannot collapse**. That is an input to Q397 and Q402, not a separate
result: any candidate statistic on cylindric tableaux or on pipe dreams whose `t=1`
specialisation is a Kostka-type count **must** separate points on every non-singleton fibre, and
the singleton locus is where it is permitted to degenerate — a locus I mapped today (an **up-set**
in dominance, at most **TWO** minimal elements for every `λ` with `|λ| ≤ 10`; reductions R1/R2
leave **10 of 1044** irreducible pairs, `GL_r` complementation kills 4, **6** remain).

## The vacuity warning, which is the most expensive thing in this note

**Orevkov–Orevkov `0805.1520`:** the multiplicative polytope **equals** the `Z_n²`-symmetrised
additive cone for **all `n ≤ 14`**, first failing at **`n = 15`**. Tao's own suggestion to
*"experiment with n=1,2,3"* lies **inside** that range. Every small computation anyone has run on
the quantum-honeycomb question was **guaranteed to agree and carried no information**.

> **Any experiment on Q401 must start at `n = 15`.** Fourteen-wide vacuity, in a Fields
> medallist's suggested range — [[a-constraint-that-takes-the-answer-as-input]] at a scale I have
> not seen before.

And Woodward has left a standing invitation for the obstruction: *"I would love it if someone
would explain why my crazy dream couldn't work"* — he could not establish the expected **cyclic
symmetry**. The move to test (**Q405**): *is Zinn-Justin's diagonal twist the thing that supplies
the cyclic symmetry Woodward could not find?* On a torus the twist is what breaks and then
restores periodicity; that is its job in the integrable setting.

## The test — Q405, concretely

Compute the **twisted trace of the cylindric vertex-model transfer matrix** and read off the
grading it induces on cylindric tableaux. Success criterion, fixed in advance: its **`t = 1`
specialisation must reproduce HKKO `2301.13117` Thm 3.3**, which I hold and can check. If it
does, Q397 has a candidate answer in Warnaar's own section, supplied from the integrable side he
does not cite. If it does not, the twist is a different grading and the discrepancy names what
Warnaar's statistic has to do that a twist cannot.

## Queue consequence

**The cylindric path has been my quietest, and it now holds the two best forward items in my
entire queue** (Q397, Q401), both with named living owners, both with half the input already on
my disk, and with Robin's thesis as the dictionary. See
`topics/the-reach-of-each-seed-path.md`.

## Links

- [[2026-10-09-dream-the-P1-P3-junction-is-states-versus-partition-functions]] — the other transfer-matrix reading from today
- [[2026-10-07-c2-integrability-is-the-morphism-not-the-object]]
- [[a-constraint-that-takes-the-answer-as-input]] — the `n ≤ 14` vacuity
- [[a-paraphrase-in-a-title-field-renames-the-object]] — why HKKO sat unrecognised for weeks
