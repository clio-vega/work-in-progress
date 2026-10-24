# PROVE 2026-10-21 — G5 core closed to `proved`, and the type-B branch of the paper has no proofs

**Artifact:** `proofs/2026-10-21-G5-core-c-equals-one.tex` / `.pdf`, 13 pp,
commit `97158d7` (hash filled in by `958a20a`), pushed.
`https://github.com/clio-vega/proofs/blob/main/2026-10-21-G5-core-c-equals-one.tex`
**Queued for Rick** in `state/OUTGOING-UNSENT.md` — this slot is barred email.

## The result

`T^1_{M,L} = delta_{M,L}` for all `M,L ⊆ [N]`: Motegi's `prop:allcard-Bhat-inverse`
(L4897) with the type factor stripped. With Theorem A of 10-20 this gives the
proposition in **both types and all N**, with no type-A input. The target gap was one
sentence of his, L5263 — *"every two-index factor has now been included either in some
`E_j` or in some `P_{eps_i eps_j}`"* — which is an assertion, and is now Lemma 4.

## What I think is actually worth your attention

### 1. P1 came back SPLIT, and the split is the content

I pre-registered "the pair → consumer map is a bijection". It is. But *"bijection"* is
one word covering two claims with **different load-bearing structure**:

- **Surjectivity** (nothing dropped) uses only the set partition `[N] = L ⊔ D ⊔ M^c`.
  Every order condition it meets is *satisfied, never needed*.
- **Injectivity** (nothing double-counted) is also pure partition logic on the mixed
  pairs — but on the `D`-pairs with `eps_i ≠ eps_j`, **two** products have the pair in
  range and the *only* thing separating them is the **total order on `[N]`**.

So `k<t` is **irremovable from injectivity and inert for surjectivity**, and that same
condition is why `P_01 ≠ P_10` — the asymmetry of the two off-diagonal shapes is the
shadow of an order relation, not of anything about `L` or `M`. The measurement that
caught it: lesion L1 (delete `k<t`) gives 110/240 mismatches **all of them "extra,
nothing missing"**; lesion L5 (drop `a<d_j`) gives 176/240 **all "missing, nothing
extra"**. The two lesions break *disjoint* halves. A single-arm pre-registration could
not have recorded this; a count of mismatches could not have either — only the
**direction** of the set difference.

This is the 10-19 lesson landing again, one level up: *a grouping asserts "one family,
one answer" and is cheaper to test than any theorem in it.* Here the grouping was a
single English word in my own pre-registration.

### 2. A second gap of the same shape, not on my agenda, found and closed

`lem:allcard-Bhat-product` (L4660) — the closed form for `Bhat^X` — is proved in the
paper by the words **"substituting these four expressions and simplifying"**. I had
recorded it as `computed` (240/240) in my own 10-20 note and moved on, because the brief
pointed me at the *other* gap. It is now seven exact cancellations, both types at once
(§3). The brief named one gap correctly; the cheapest second one was one lemma earlier,
and nothing in the brief would have found it. **Reading the proof region of the lemma I
was told to trust is what found it.**

### 3. The finding I did not expect: the whole type-B branch is stated without proof

Motegi **L3598**:

> *"The proofs of the type `B` statements below are parallel to the corresponding type
> `C` arguments, with the type `B` specialization and normalization factors in place of
> the type `C` ones, and are therefore omitted."*

So `eq:typeB-cross-sector-branching` (L3685) has no `\begin{proof}` anywhere in the
file, nor does anything else in §Type B. This is a legitimate move and he flags it. But
it means **every type-B statement upstream of my work is a declared parallelism, not a
demonstration** — and I had been treating the two types as symmetric inputs for days.

The good half: for the all-cardinality biorthogonality today's work **discharges** that
parallelism. Lemma 3 carries out both types explicitly from the raw definitions, and
Theorem A shows the one surviving difference is invisible to the identity. So "parallel"
is, *there*, a theorem now. Undischarged: the step from `WBtilde` to `Br^B`.

### 4. The B/C difference is the diagonal of a pair product

Sharpens **Q540**. The type is consulted at exactly one line of the whole development.
Type C writes `∏_{a≤b}` where type B writes `∏_{a<b}` plus `∏_a`; after the `M`-level
normalisation that *is* `c^C_t = (1-w_t^{-2})^{-1}` against `c^B_t = (1-w_t^{-1})^{-1}`,
ratio `1 + w_t^{-1}`. A diagonal `a=b` term of a two-variable product is a one-variable
quantity wearing two-variable clothes — which is what "boundary parameter rather than
bulk" ought to mean. New sharper falsifier for Q540 in §8 of the artifact.

## What I did NOT do, stated plainly

**G5 is not closed.** Two premises remain and are now **nodes**, not prose: the
cross-sector branching formulas, and `lem:allcard-Phihat-inverse` over the two RTV
statements. My `thm:S`/`thm:S'` and Rick's `q488-*` rest on those, not on the branch I
closed. §7 of the artifact says so in a table. Saying otherwise would be an over-claim
in my own favour, which has no natural objector.

**G3** (`(BD)` in type B) was the secondary target and was not reached — second day.

## Instrument notes

- **The trajectory emitter fragmented my session again** (2 files, and the second
  restarted IDs at `evt-0001`, so two events shared an ID). Merged by hand into
  `state/trajectory/clio-prove-G5-20261021.jsonl`, fragments retired as
  `.superseded-fragment`. `report` reads ONE file; I would have validated half a session.
- `registry_validate.py` flagged **4 real problems** — my new leaf nodes were missing the
  `children` key. Fixed; now `OK: valid`. I counted problem lines, not the exit code.
- A detector of mine gave a confident wrong answer again: my `/Count` regex read the PDF
  as having no pages (compressed page tree). The LaTeX log line *"Output written ... (13
  pages)"* is the positive control and was right.
- `git add` of a `.bak` silently broke an `&&` chain and the commit never ran — the
  `.gitignore` again. Caught because I printed `HEAD` afterwards instead of trusting the
  chain.
