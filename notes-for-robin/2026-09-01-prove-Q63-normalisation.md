# PROVE 2026-09-01 — Q63 gap 3: the q-power we were hunting did not exist, and the one that does has a closed form

**Paper:** `proofs/2026-09-01-Q63-wedge-fock-normalisation.tex` (9pp, compiles).
**Registry:** `proofs/registry/fock-ribbon-sign-operator.json`, validates clean.

## The short version

Yesterday's paper's blocking gap was: the wedge/Fock identification
`u_k <-> |lambda,s>` "carries an unidentified q-power" — `[e_i, B_{-1}]` was nonzero on
13 of 126 test cases. The brief asked me to test hypothesis (H4), that the power is the
cross-runner tie term, against one named rival.

**There is no power.** Uglov says so in the paper we have had on disk since 30 August. Having
written the wedge action in the multipartition indexation he writes that those actions "are
identical with those defined on the combinatorial Fock space", and two pages later that the
quantum affine algebra and the Heisenberg "are pairwise mutually commutative". So the
normalisation is 1 and `[e_i,B_{-1}] = 0` exactly.

The 13/126 was **our bug**. Six lines of straightening code discarded any wedge with a
repeated index *anywhere*; Uglov's rule (R1) licenses that only for an *adjacent* repeat.
At level 1 it is harmless (only two of the four ordering rules can fire, and both are
antisymmetric at leading order); at level ≥2 rule (R4) has leading coefficient **+1** and
the shortcut destroys real terms. After the repair: `[e_i,B_{-1}] = 0` on **523/523**,
`[f_i,B_{-1}] = 0` on 523/523 (8 apparent failures are truncation, all clear at depth ≥ 9).

## What made it findable

The level-1 validation was strong — 201 blocks, 818 coefficients against Lyra's
independently generated answer key, zero mismatches — and **could not see this bug**,
because level 1 never executes rules (R3) or (R4). The check that found it is internal and
untuned: **`[B_{-1}, B_{-2}] = 0`**, which Uglov proves. Before the repair: 7 of 8
configurations had a nonzero commutator at level ≥ 2, 0 of 8 at level 1. After: 0 of 8.
Confluence (straighten resolving the first inversion vs. the last) passed **both before and
after**, so that check would not have caught it either.

The generalisable form, and I think it is the useful sentence: **a validation suite
inherited from a special case certifies only the code paths that special case executes.**
Level 1 runs half the ordering rules.

## The result that survives

Gap 3 also recorded a *measurement*: on single-component entries the ratio of `B_{-1}` to
the naive per-runner ribbon operator was always `q^a` with `0 ≤ a ≤ ℓ-1`, "not constant on
a runner". That survives the repair, and it now has a proof:

> **Theorem.** For ν and λ differing in one component d, by the e-ribbon move κ → κ+e on
> runner d,
>
> `<ν|B_{-1}|λ> = (-q^{-1})^h · q^a`,   h = #(M_d ∩ (κ, κ+e)),
>
> `a = #{d' > d : κ ∈ M_{d'}} + #{d' < d : κ+e ∈ M_{d'}}`.

Verified 913/913. The proof is a **locality lemma**: straightening the term `k_j → k_j + N`
never disturbs a bead outside the closed window `[k_j, k_j+N]`, and that window has length
exactly N — so the only single-bead-move target it can reach is its own. Plus `Σk²`
strictly decreases at every correction term, so that target is reached by transposition
terms only, and their leading coefficients are `-q^{-1}`, `q`, `1` by inspection of
(R2),(R3),(R4). The bound `a ≤ ℓ-1` then falls out: each label occurs exactly once in a
window of length N.

Two claims of yesterday's paper are **promoted from `computed` to `proved`** by the same
lemma: every entry of `B_{-1}` changing two or more components is divisible by `(q - q^{-1})`,
and `B_{-1}` at `q=1` **is** the naive per-runner ribbon operator exactly.

I measured the dichotomy directly as a check on the lemma: single-component entries got 697
transposition-only contributions and **0** correction contributions; two-component entries
got **0** and 118. No cancellation — disjoint targets, exactly as predicted.

## (H4): refuted, and honestly

(H4) and its named rival are both refuted, and the discriminating test the brief designed
was never reached, because the object both hypotheses were about did not exist. But (H4) was
not a bad guess: the q-power **is** a cross-runner tie count, bounded by ℓ-1, vanishing at
ℓ=1 — every property (H4) predicted. It has the right species and the wrong home. It belongs
to the operator, not to the basis.

Worth noting which of the brief's four supporting coincidences held up. The brief rated
"both are not constant on a runner" as the only one with force, and that is exactly the one
that survives — it is now a corollary, for the cross-runner reason (H4) guessed. The three
free ones (matching range, both vanish at ℓ=1, would unify two gaps) were all true and all
pointed at the wrong object.

## Corrections to the 31 August paper

1. Gaps item 3 ("the wedge/Fock normalisation is unresolved") — **withdrawn**.
2. Remark 1.4 said the tie-break and the side "were fixed by requiring that the ℓ=1
   specialisation reproduce the proved Q59 theorem". True of the side; **false of the
   tie-break** — at ℓ=1 no two components compete for a shifted content, so it is invisible
   there. It was pinned by nothing. It is now pinned by Uglov's Theorem 2.1 and,
   independently, by `[e_i,B_{-1}]=0` (the mirror tie-break gives 20/96).
   Related: the `sl_2` relation `[e_i,f_i] = [N_i]_q` holds for **both** tie-breaks and both
   sides, 534/534 each. A relation satisfied by every convention is not a convention check.
3. Proposition 4.1 **stands**, recomputed after the repair (55 two-component entries in the
   narrow sweep, 118 in the wide one, all `(q-q^{-1})`-divisible, q=1 agreement 487/487).
4. Theorems 2.3, 3.1, Corollary 2.4, Conjecture 3.3 **unaffected** — none uses the wedge
   realisation or the straightening.

The bug is patched at source in `probes/2026-08-31-route1-diff/route3_uglov.py`, with a
comment explaining why level 1 could not see it. I checked the patch changes **nothing** at
level 1 (171 configurations, 0 changed), so Lyra's answer-key match is preserved.

## Two things for you

- **`trustcheck` misinvocation, sixth firing.** Running without `--root memory --sources
  memory/reading/sources.json` reports **159 "read file missing"** problems that do not
  exist. With the canonical flags the registry is clean. This has now cost time in six
  separate sessions. It is a defect in the boot prompt's recorded invocation, not in the
  tool — worth fixing at the prompt.
- **Not done:** step 2 of the brief (Conjecture `conj:j`, the entry-by-entry check over the
  1248 form-(i) entries). The session went entirely into gap 3. `conj:j` is undamaged by any
  of this — it concerns `[e_i, R^{(ℓ)}(t)]`, which uses neither the wedge nor the
  straightening — and it is still the cheapest next step.
