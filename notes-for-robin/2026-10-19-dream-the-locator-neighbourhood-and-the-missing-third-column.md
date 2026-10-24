# For Robin — 2026-10-19 DREAM

Two findings about how I work that I think are worth your time, and one request.

---

## 1. The highest-yield unread region in my corpus is the neighbourhood of a locator I am already using

Four consecutive sessions, four different lanes, one shape: **the thing I needed was inside a
document I already held, tens of lines from a line number already written in my own notes.**

| session | distance | what was sitting there |
|---|---|---|
| PROVE 10-18 c2 | 4 lines | `normalizationWB` — closed Q514 *in the session that posed it* |
| PROVE 10-19 | 27 lines | `normalizedsusytwo`, `arXiv:2610.15344` L2618–2622 — Motegi owns the headline multiplier of my 10-18 paper, **with a proof**. Retracted. |
| REVIEW 10-19 | 59 lines | `lem:allcard-Phihat-inverse` L4424 — an exact **type-A** dual basis at complements, all cardinalities. A tool I did not have. |
| BROWSE 10-19 | same document | the machinery for an open question, inside my own seed paper `1811.07581`, held at `deep-read` |

The reason I think this is a real effect and not four unlucky days: **the sign of the outcome
carries no information.** The same move gave me a tool and took a theorem, from the same e-print,
within sixty lines of each other, on the same day. What is constant is the information density,
not whether I come out ahead.

Why that region in particular is rich: a locator I am *actively citing* is simultaneous evidence
that (a) the document answers questions of exactly my shape — I proved that by citing it, (b) the
author wrote the surrounding pages in one sitting about one object, and (c) the read is free, since
the brief hands me the line numbers and there is no network involved. My habitual first moves — an
arXiv keyword search, a new deep-read — are both *bets*. This one isn't.

**The rule I have adopted: ±50 lines around every locator the brief cites, before proving
anything.** Four locators is about 400 lines of `sed`, under five minutes. I have recorded a
falsifier: if three consecutive briefs turn up nothing new, it is cargo cult and I will say so.

The related finding, which BROWSE reached independently and phrased better than I did: **a
`deep-read` grade records that I read the document, not that I asked it my current question.** My
extraction ladder measures provenance depth and I have been reading it as coverage. It has no
column for the second, and the two are *anti*-correlated — a paper earns `deep-read` by answering
one question, and then the grade reports as though it had answered all of them.

## 2. Three of my registers have the same structural defect: no third column

Today I pre-registered three binary predictions. **All three came back with an answer that was not
on the ballot.**

- Lean predicted a hypothesis **irremovable**; it was **absent** — the binder lives one lemma
  upstream. "Removable" and "irremovable" both presuppose the binder was in scope.
- A proof predicted a corollary true at `v = −1`; the point is **outside the domain** — the
  prefactor has a pole exactly where the other factor has a zero, so the literal substitution
  returns `nan` and the `0/18` I nearly reported as a refutation meant *undefined*.
- Browse asked a yes/no question about symplectic bumpless pipe dreams; the question was
  **mis-posed** — those objects are orbit closures in the complete flag variety, not Schubert
  varieties in the Lagrangian Grassmannian. No domain as posed.

In each case the ballot presupposed a fact I had never separately checked, and **the presupposition
was the load-bearing claim while the ballot was decoration.** That is not three mistakes; it is one
missing column, and it recurs across unrelated registers — lesion verdicts (removable/irremovable),
pole censuses (zero/nonzero), token liveness (live/dead, when a token turned out to be dead on one
endpoint and alive on another).

My conclusion, which I think generalises past my own notebooks: ***when an instrument keeps
returning an answer the schema cannot hold, the defect is in the schema, not the instrument.*** The
fix is one line per pre-registration — a "not-well-posed" arm plus a named detector that would fire
if the presupposition fails. Today's yield would have been three for three, and in all three the
third arm is where the actual content turned out to be. The out-of-domain one is the nicest:
cancelling analytically didn't just save me from a false refutation, it revealed the real
phenomenon at the same point.

## 3. The mathematics, briefly

Type B is now closed — the collapse multiplier is exactly `1` at every root of `B_N`, 104/104 by
two mechanisms (`proofs/2026-10-19-typeB-gauge-theorem.tex`, commit `7ee6b81`). With type A closed
on 10-18, **type C is the only direction where the multiplier is nontrivial**, which is the third
independent confirmation this week that type C is the odd one out. The exception is the programme.

And the "uniform formula in `h`" that I thought bridged the types is a coincidence of outputs: no
step of either derivation has `h` as a variable. That is a grep over the proofs, not an impression
of them. What replaces it is better — each type's theorem is cut out by that type's own root
system and reaches no further, which is why `G2` survives (the bad point isn't a root hyperplane
of `B_N`). The theorem explains its own exceptions, which is the shape I always hope for.

## The request, restated

The wake session escalated this to you and I am repeating it rather than deciding it myself:
**73 registry references point into `projects/peers/`, which is not a git repository.** Those nodes
are canonical for me and invisible to everyone else. Making it a repo versus re-pointing the
references changes what my registry *means* to a reader, and that is a call about the artifact's
audience rather than its contents.

Nothing is blocked on it. It just gets more expensive the longer it sits.
