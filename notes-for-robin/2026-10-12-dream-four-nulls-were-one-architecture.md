# Four nulls were one architecture — and two faults in my boot prompt are still live

*Clio, DREAM 2026-10-12. Short, because two of the three items are yours to action.*

## The mathematics, in one paragraph

Over four PROVE sessions I refuted four candidate mechanisms for the cylindric Hall–Littlewood
structure constants: Q405 (capacity), Q410 (`ord_{t=1}`), Q417 (wrap-blind), Q430 (today,
multiplicity-determined). Tonight I noticed that **all four are kills of the same architecture** —
*a positive weight attached to configurations, summed with the Warnaar sign.* Q430 is the sharpest:
at `ℓ=0`, `α=(1,1)`, any `k ≥ 1`, the fibre has exactly **two** cylindric tableaux with
**identical multiplicity sequences** and **opposite signs**, so every weight of the form
`f(m_{i−1})` sums to zero while the target `c_{(1,1)} = 1 − t` does not. That kills Korff 2011,
Korff 2019's ribbon weight, and today's Gaussian binomial in one evaluation.

**The surviving mechanism is not a weight.** Morse–Schilling `arXiv:1207.0786` gives the fusion
coefficients as an **alternating** sum over cylindric tableaux — which escapes the Q405 capacity
null by construction, because Q405 only forbids *positive* one-monomial-per-configuration sums.
Korff–Vasilev `arXiv:2606.06352` independently forces this: it is Graham-positive in
`Z_{≥0}[y_i − y_j]`, so no specialisation of it can ever equal `3 − t²`, which means the mechanism
must involve genuine **cancellation**. It was in my own browse log from yesterday, cited zero times
by any of the four nulls.

**And something that should interest you directly:** `arXiv:1603.01815` — Wheeler–Zinn-Justin,
*Hall polynomials, inverse Kostka polynomials and puzzles*, which is in SEED.md's inventory — sits
at the intersection of the Puzzle, Integrable Lattice and Fock Space paths, and the object they
meet in is the **inverse Kostka matrix**. That is exactly `transfer_operators.py`'s discovery:
Kostka matrix inversion rather than hook-content evaluation. If the paper routes Hall polynomials
through inverse Kostka, **your code may already implement half the cylindric engine**, with only
the index set missing. I have graded that honestly as not-yet-first-hand and queued the read (Q437).

## Two faults in my boot prompt, both read-only to me

1. **`--files-dir` default inheritance.** `registry_validate.py --help` says `--files-dir` defaults
   to `--root`. My boot prompt passes `--root memory`, so every node's `proofs/...` path resolves
   to `memory/proofs/...`. Today it reported **56 problems for 56 nodes** — a total failure that
   reads as a data problem. `--files-dir .` → **0**. This is the **8th tool** hit by it, mechanism
   now read from source (L456/L299), and the faulty invocation is printed in the prompt I run
   verbatim.
2. **`gh api users/X/events --jq '.[0:8]'`** slices an **unordered** list. It silently dropped four
   real events of mine while showing older ones. `pushedAt` / the commits API is the authority on
   *is it published*.

I have not edited the prompt — it is read-only. Both corrections are one line each.

## Two things with deadlines that are not mine

- **Rick's FPSAC 2027 submission is finished and blocked only on you**: your yes, the
  acknowledgements, and the AI-declaration role. **Deadline 2026-11-15, FPSAC 2027 Galway** — not
  passed, but the window is five weeks. I have told him in writing that it sits with you.
- **Lyra wants an evalscience yes/no by about 10-18.**

No email from you since **10-05** and no GitHub activity in October. Everything of mine from the
last week is pushed and reachable (`clio-vega/tworow-d4-kernel` `39a2d61`, proofs `1f866d2`,
`clio-vega/rick-review` `d83f01a`), so none of it is waiting on you — these two are.

## One thing I got wrong today, for the record

A claim in `2026-10-11-c2-Q424-scope-and-domain.tex` line 551 was filed under *"Rests on
computation"* and **no computation backed it** — the script had crashed partway through and its
surviving output ended at a plausible place, with a 1,437-byte `.err` sitting unread beside it.
The mathematics was unaffected (the real argument is that one side is `t`-free and the other is
not), but **the grade was false**. I told Rick directly rather than quietly amending, and the
computation now exists. Every script I write now prints a sentinel as its last line, and I `wc -c`
the `.err` before reading the `.out`.
