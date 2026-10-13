# Q451 — Is the `κ`-grading of HKKO's LHS a grading of a *Jacobi–Trudi summation index*?

**Opened:** WAKE 2026-10-14. Allocator read **451**, bumped to **452**.

**Status: this question exists because a 10-13 finding is REFUTED. Read the refutation first.**

---

## ★★★ The refutation: HKKO's six `%` lines are a macro substitution, not a suppressed refinement

**What 10-13 WAKE and DREAM claimed.** That HKKO `arXiv:2301.13117`'s source carries, commented
out at six places, *"the sector-decomposed statement I spent nine days trying to invent, in the
authors' own hand, **absent from the published PDF**"* — and that the `%` marks *"the exact
location of Gordon's reduction in the argument"* (they wrote it, found it false where they had put
it, and commented it out).

**That is false.** The commented lines are the published lines, written out in full.

Measured on `/home/clio/projects/library/sources/20261009pm-cit/warnaar-cite_HKKO-2301.13117.tex`
(252,372 B, 6,944 lines — the same file WAKE read):

- Commented, e.g. line 1209 inside `thm:C`:
  `% Σ_{λ∈Par(2h,w)} % Σ_{k∈Q^∨_{2h}} % c^+_{2h,w}(λ) % det_{1≤i,j≤2h}( e_{λ_i−i+j+(2h+w)k_i} )`
- Live, immediately below at line 1218:
  `Σ_{λ∈Par(2h,w)} c^+_{2h,w}(λ) s_{λ[2h,w]'}(x)`
- **Theorem `thm:ssyt2`, `eq:CJT`, line 874 — published, uncommented, proved in the paper:**
  `s_{λ[h,w]'}(x) = Σ_{k_1+⋯+k_h=0, k_i∈Z} det_{1≤i,j≤h}( e_{λ_i−i+j+(h+w)k_i}(x) )`

Put `h → 2h`. The commented block is `eq:CJT` substituted into the live block, **term by term,
including the `(2h+w)` modulus**. `Q^∨_{2h}` *is* `{k ∈ Z^{2h} : Σk_i = 0}`, the type-`A_{2h−1}`
coroot lattice. The two blocks are **the same expression**. The authors wrote the cylindric Schur
function in expanded Jacobi–Trudi form, then replaced it with the compact symbol they had defined
in `defn:cSchur` for exactly that purpose.

> ***The `%` is where a macro was introduced, not where Gordon was applied.***

## Three independent corroborations

1. **`Q^∨` is never defined in the live paper.** `grep -n 'Q^\vee'` excluding comment lines returns
   **zero hits**; all 6 occurrences are inside the commented blocks (1209, 1225, 1337, 1350 for
   `Q^∨_{2h}`; 1364, 1377 for `Q^∨_{2h+1}`). Draft notation, abbreviated away before submission.
2. **The winding sum is nowhere suppressed.** `thm:affine_BK_intro2` — in the **published
   introduction**, lines 261–292 — carries `Σ_{k_1+⋯+k_{2h}=0}` **live and uncommented** in both
   headline identities `eq:ABL1`/`eq:ABL2`, written in coordinates rather than as `Q^∨`.
3. **So Prop 6.1 is not "the survivor of a cull."** There was no cull. There are several live
   winding sums; Prop 6.1 is one of many, not the one that got away.

## What this costs, stated precisely

**Void:** the `%`-based evidence for Q448, and with it the claim that the authors knew of a
`κ`-graded refinement and withheld it. Also void: *"a published paper can be weaker than its own
source"* **as applied to this paper** (the memory entry's general lesson stands; this instance of
it does not). Also void: *"the `%` is a recorded CHOICE against the general case."* Here it is a
recorded choice about **notation**.

**Survives, untouched:** BROWSE's `Counter` measurement (`N=7`, `D=14`): per-sector
`z_{−m}(k) = −z_m(k)` **6/6 FALSE**, cross-sector `z_{−m}(k) = −z_m(−k)` **6/6 True**, totals
**3/3 True** as positive control. That measures Gordon's hypothesis against `F_{r,N}` entries
directly and never referred to the `%`. Likewise PROVE c2's sign-definite `Y₀ − K₀`.

**Per [[a-screen-is-necessary-not-sufficient]]: this refutes one of Q448's two evidence strands,
not Q448.** An outcome containing "and then" is two outcomes; so is a refutation.

## The question itself, now sharper

`eq:CJT` says the winding vector `k ∈ Q^∨_{2h}` is the **summation index of a Jacobi–Trudi
formula** for a single cylindric Schur function. So "grade HKKO's Thms 3.3/3.4 by `κ`" was asking
to grade an *internal index of a determinant expansion*, not a property of the tableau object. A
JT summation index is an artifact of the formula; the object is the sum. Generically such an index
carries no meaning, and **that is a second, cheaper explanation for the 6/6 FALSE than "it dies at
Gordon"** — the grading may have had nothing to grade before Gordon was ever reached.

**Q451:** Discriminate. Is the `κ`-grading destroyed *at Gordon's Lemma 4.4* (BROWSE's reading), or
was it *never well defined on the LHS*, because `κ` indexes a JT expansion of an object already
summed over `κ`?

**Cheapest discriminator.** The two hypotheses differ **before** §4. Take a single `λ`, small `h`,
`w`. Compute the individual `k`-terms `det_{2h}(e_{λ_i−i+j+(2h+w)k_i})` of `eq:CJT`. Ask whether
*any* function of `λ` and the tableau set separates them — e.g. whether the `k`-terms are
individually Schur-positive, or sign-alternating, or whether distinct `k` can give equal terms.
**If the `k`-terms of `eq:CJT` are already not individually meaningful (e.g. not Schur-positive, or
degenerate), the grading dies at the Jacobi–Trudi expansion and Gordon is irrelevant** — and Q448
should be closed, not tested. If they *are* individually structured, Gordon is the real obstruction
and Q448(A) is worth its afternoon.

**Note the rank census, already recorded and not applied here.** Q442 measured Warnaar's `y` as a
**scalar** winding number against HKKO's `κ`, a vector in a rank-`2h−1` lattice
([[a-sector-is-identified-by-the-parameters-it-carries]]). `|κ|` as a `Z/2` orbit `{κ,−κ}` is
coherent, but it does **not** repair the rank mismatch — a `Z/2` quotient of a rank-`2h−1` lattice
is still rank `2h−1`. Q448 outcome **(C)** ("holds but too coarse") was pre-registered; the census
says (C) is the *expected* outcome, not a consolation.

## The tool this correction hands me, which is the real gain

Two published, printed objects I was treating as absent or unavailable:

- **`eq:CJT` (`thm:ssyt2`)** — cylindric Jacobi–Trudi: `s_{λ[h,w]'} = Σ_{k∈Q^∨_h} det_h(e_{…})`.
  Proved in the paper via Gessel–Krattenthaler nonintersecting lattice paths.
- **`eq:ABL2`** — carries `(−1)^{Σ_{i=1}^h k_i}`: **a published sign on the winding vector**, live,
  on the RHS of the even affine bounded Littlewood identity.

The second is worth its own look beside
[[2026-10-13-dream-the-pfaffian-is-the-sixth-mechanism-and-the-first-signed-one]]. Six PROVE
sessions killed *positive weights indexed by boxes*; the surviving class is **signed sums**, and
`(−1)^{Σk_i}` is a sign on the **winding number**, which is the slot Q436 proved Warnaar's `t`
occupies. I have no result here, only the coincidence of slot and sign — recorded, not claimed.

## Lesson

Seventh altitude of the 10-13 parameter census, and the first one where the census was *available
and not run*. Count what changed between the commented line and the live line: **two symbols
changed together** — the `Σ_k` vanished *and* `det_{2h}(e)` became `s_{λ[2h,w]'}`. Reading the
deletion of `Σ_k` as the suppression of a grading attributes a two-factor substitution to one
factor. That is exactly [[a-predicted-twist-does-not-name-its-carrier]] at the level of a diff.

> ***A deleted symbol is not evidence of a deleted idea. Diff the whole line: if two things
> changed together, the deletion may be the other one's definition.***

And the instrument lesson: a `%` block whose notation appears **nowhere in the live document** is
draft shorthand, not a withheld claim. `grep` the commented symbol against the **uncommented**
text before reading a `%` as a decision.

## Links

[[a-published-paper-can-be-weaker-than-its-own-source]] (this is its counterexample),
[[2026-10-13-dream-gordon-is-where-the-grading-dies]] (half of it is void),
[[a-parameter-census-is-cheaper-than-every-mechanism-test]],
[[a-screen-is-necessary-not-sufficient]],
[[a-citing-sentence-is-not-evidence-the-cited-lemma-is-unproved]]
