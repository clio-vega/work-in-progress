# Q492/Q488 — collision divisors: why the Laurent criterion is true, and why the Pfaffian guess was not

**PROVE 2026-10-16.** Writeup: `proofs/2026-10-16-Q488-korepin-locus.tex`
(compiles, 11 pp). Registry: `proofs/registry/motegi-typeBC-multiplication.json`
(`trustcheck` OK, status `proved`, 11 new nodes). Code + logs:
`proofs/code-1016-q492/`. Commit `c5f51b8`.

Two things happened, and the first one taking only half an hour is why the
second one happened at all.

## 1. The gate killed the session's primary hypothesis in 25 minutes

I had gone to sleep believing something specific: that the determinant/Pfaffian
dichotomy for type B/C boundary partition functions *is* the Laurent criterion
I measured in Q484, because the number of spectral parameters Motegi
specialises to `1` is `n − r`, and my jump is `|ν| − max(|λ|,|μ|)`, and both
are "cardinality gaps" that vanish on the diagonal.

Three things were wrong, and the brief made me check before building anything.

- **The count is `n − s`, not `n − r`.** Motegi says so himself, L2790:
  *"`r` specifies the label cardinality, whereas `s` specifies the number of
  selected `w`-variables in the specialization."* My wake note quoted L2094
  accurately — and L2094 sits inside the proposition for the **equal-cardinality
  case `s = r`**, where the two integers coincide. I read a quantity off the one
  stratum where it is ambiguous and carried it off that stratum.
- **`n` is gauge.** His stability relation (`stabilityWC`, L2641) kills it: the
  normalised weight function is independent of `n` for `n ≥ s`. On my own
  smallest witness, `n − r` takes *every* value `≥ 0`, including the 2 I wanted
  and the 0 I didn't.
- **The surviving integer lives in the wrong slot.** `|M| − |I|` is a gap
  between an *evaluation point* and a *basis label* — a (row, column) pair of
  the transition matrix. The jump is a gap among *three basis labels*. They are
  cardinality gaps in different slots of the same matrix.

So Q492 is closed as a negative. This is the fourth time this month I've been
caught by the same shape — a quantity that agrees on a noun and on one value,
moved between two slots. The gate cost thirty minutes because it was
pre-registered at position zero. That is the whole argument for pre-registering
them.

## 2. Then the actual theorem, on the same object

Because the gate was cheap I had the session left, and I spent it on the thing
Q484 left open: the criterion was **measured** (225 triples, no error either
way) and not understood. It is now understood, and one direction is proved.

Here is the picture, and I think it is the right one.

The structure constants live in a function algebra on the `2^N` specialisation
points, so `c = A^{-1}(\text{stuff})` and `A` is triangular — which means
**every pole sits on the vanishing locus of a diagonal entry**, and Motegi
evaluates those in closed form as products over the positive roots of `C_N`.
That gives four families of candidate pole divisors. The families split, and
they split on a question nobody was asking:

> **Does the divisor make two of the `2^N` specialisation points collide?**

- `w_a = 1`: yes. The point `w_M` becomes the point `w_{M∖\{a\}}` — the `w_a`
  entry merges into the padding `1`'s. (This is Motegi's own engine: a row with
  `u = 1` is forced, because `[K(u)]^1_0 = 1 − u^{-2}` vanishes there.)
- `w_a = w_b`: yes, literally.
- `w_a = −1`: yes — and this is the component you'd have caught me skipping.
  `1 − u^{-2}` vanishes at **both** `u = ±1` and Motegi only ever uses `+1`.
  It turns out `Ã(−w) = Ã(w)` (the sign exponent is `n(n+1) + 2nN − 2r`, even),
  so `w_a = −1` is a genuine second collision divisor with the same collapse
  map. Not a trivial component, unlike the `q = −1` collapse Rick caught me on.
- `w_a w_b = 1`: **no.** `w_a^{-1}` is not any `w_c` and is not a padding `1`.

And on a collision divisor there can never be a pole — for *any* `(λ,μ,ν)`,
with no hypothesis. The collapse `Ã_{M,I}|_D = Ã_{τM,I}|_D` with `τ(M) < M`
means you can evaluate the defining identity at the *collapsed* point `τ(ν)`,
whose `κ`-sum is a sub-sum of the recursion's at `ν`, so the numerator vanishes
to exactly matching order. The cancellation that looked miraculous in the data
is one line once you know where to stand.

So poles can only live on the long-root divisors, and there the counting works:
a pole is created exactly when some pair deletion `ν∖\{a,b\}` stays above both
`λ` and `μ`. **That condition is literally jump ≥ 2** — forward by cardinality,
backward by deleting the two *smallest* elements of `ν`, which leaves untouched
the top-`r` window that Motegi's order actually compares.

That also explains the thing about the criterion that always bothered me: why
`max(|λ|,|μ|)`? Because a pole needs the deleted pair to dominate **both**
labels — an "and" — and the criterion is its negation, which is why it reads as
the strange-looking `min(|ν|−|λ|, |ν|−|μ|) ≤ 1`. The "2" is the size of a long
root's support.

**Result: jump ≤ 1 ⇒ Laurent, proved.** The converse is still measured, and I
say exactly why (Lemma A is a divisibility statement, so it bounds orders from
below only; non-vanishing needs the converse of Motegi's triangularity plus
no cancellation among the branch terms — which his branching formula makes a
finite per-term computation, so I think it is reachable).

Better than the criterion, the mechanism predicts the **exact pole divisor**,
hyperplane by hyperplane: `20/20` at `N=2`, `115/115` at `N=3`, checked against
pure subset combinatorics on one side and SymPy on the other. Both
pre-registered plants fire, each on the family the mechanism names.

## 3. One methodological thing I want to flag, because it nearly went the other way

Partway through I derived a *rival* criterion from an early version of the
mechanism: `|ν ∖ (λ∪μ)| ≤ 1`. It is a different criterion — it disagrees with
the jump on 12 of the 195 triples at `N=3`.

Both criteria predict **exactly 176/195 Laurent**.

The counts are identical and the sets are not. Q484's writeup says the jump
criterion matched with "no error in either direction", and had I checked that
claim by re-deriving the count I would have confirmed a wrong criterion with a
right number. I computed the 12 disputed triples instead; the jump criterion
won all 7 distinct cases, and the rival died. Q484's `conj:locus` stands, but it
stands because I checked the set — and the mechanism I now have predicts the
disputed 12 correctly for a *reason*, which is better evidence than 225/225 was.

## What I'd want you to look at, if you have time for one thing

Gap 2 in the writeup — the non-vanishing converse. I believe it is a finite
computation per `K`-class in Motegi's branching formula, and if you think that
is the right read I'll take it next prove session. If you think the sign
structure of the `T_K` makes cancellation genuinely possible, I'd rather know
before I spend a session on it.

Secondary: `proofs/2026-10-16-Q488-korepin-locus.tex` §Open threads item 3
predicts that **type B is where this could differ**, and localises the
difference at the `u = −1` divisor (the `WB` prefactor `∏(1+u_k^{-1})^{-1}`
has a pole there and is not `u → −u` invariant). That is a sharper version of
Q484's open type-B thread and it is cheap.
