# For Robin — LEAN 2026-10-13: the last word-level obstruction is closed

**Everything here is on GitHub.** Repo `clio-vega/tworow-d4-kernel`, branch `main`.

- Module: https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/TableauReduction.lean
- Session note: https://github.com/clio-vega/tworow-d4-kernel/blob/main/NOTES-2026-10-13-tableau-reduction.md
- `#print axioms` evidence: https://github.com/clio-vega/tworow-d4-kernel/blob/main/AXIOMS-2026-10-13-tableau-reduction.txt
- Commits: `551f257` (module), `0323235` (evidence), `bd536d5` (close-of-session verification). Remote `main` verified at `bd536d5`.

## What it is

`ord_{t=1} Ψ_T = ν(T) = n` for Korff's cylindric weight at content `(1ⁿ)`, `h ≥ 2`, is now one
sorry-free Lean declaration (`Tableau.rootMultiplicity_Psi_eq_nuT`), assembled from the four
pieces earlier sessions built: gap 1 (the polynomial engine), gap 2 (the word count), gap 3 (the
region condition), and the index-model bridge.

## What the gap actually was, because the name was misleading

I had been calling it "the tableau-to-word reduction," which made it sound like tableau theory.
It was a **set equality I had been reading as a notation choice**. `CyclicAscent`'s count was
stated for words *already written* as `fun j => decide (j = p a)`. The paper's Lemma `lem:nu`
quantifies over whatever words a path produces, and its first sentence is

> "Each step has `Σ_i θ^{(a)}_i = 1`, so `θ^{(a)}` has a single `1`, at some position `p_a`."

Lean's domain was `{words of the form e_p}`. The paper's was `{words whose letters sum to 1}`.
Those are the same set — and *that they are* is a theorem, three lines via
`Finset.card_eq_one`, which nobody had written down because in English the noun "strip" hides the
quantifier. A typed binder cannot hide it. That is the second time this project's formalisation
has worked as a **scope audit of the prose** rather than a transcription of it.

## The part you should push back on if you disagree

**I did not claim the obstruction count went `1 → 0`, and I think that is right.** The brief's
framing — "content `(1ⁿ)` forces each `θ^(a)` to *be* a unit vector" — bundles two statements:

- **(a)** content `α` ⇒ the `a`-th step has `Σ_i θ^{(a)}_i = α_a`. This is `prop:dict` (the
  semistandard/row-strict transpose dictionary + Korff's Lemma 5.4 relation). It is definitional
  *inside the path model* and says nothing until you have the dictionary.
- **(b)** `Σ_i θ_i = 1` ⇒ `θ = e_p`. The real combinatorial content.

I closed **(b)**. **(a)** is a hypothesis *field* of my `Tableau` structure
(`boxCount_eq_one`), not a theorem — and I defined `boxCount` as `Σ_i θ_i` specifically so that
the field reads verbatim as `α = (1ⁿ)` and cannot be mistaken for a different statistic. So the
word-level half is closed and `prop:dict` remains, as a dictionary between two combinatorial
models rather than a step of `lem:nu`. A bundled obstruction reports as closed when either half
closes, which is why I am spelling the halves out.

## Grading

`q410-no-cyclic-psi-weight` **declined a sixth time.** It asserts 4 things; Lean carries 1.
`cyclic-ascent-lemma` asserts 5; Lean carries 3 (the dichotomy, the region condition, and the
*equality* half of `ord = ν` at `α = (1ⁿ)`). Not carried: `ν(T) ≥ #{non-constant strips}` at
general content, the `prop:dict` clause, and `Ψ_T(0) = 1`. The grade went to a scope-stated
child, `tableau-to-word-reduction-formalised`. `lean-verified` is now 6 nodes, each with its
boundary written into it rather than one node overclaiming.

## Controls, as integers

25 declarations, 0 sorries, 25 `#print axioms` records (the file is **34 lines** — three records
wrap, so a line count is wrong here), 0 non-standard axioms. Two fabricated-name plants fired,
one deliberately armed inside the non-vacuity control's own family. A `sorry` at the dependency
root contaminated **8 of 25 including `wit_rootMultiplicity`** — last session's plant spared the
control, and this one did not. It spared `wit_nuT` and `wit_Psi`, which are kernel computations
(`decide`, `norm_num`) that never touch the reduction: independent corroboration of `ν = 1` and
`Ψ = 1 − X²`.

Non-vacuity is **computed, not asserted**: `wit : Tableau 2 1 2` is one box on the all-zero
state, `wit_Psi` proves `Ψ = 1 − X²` outright (not `1`, not a unit), and `wit_natJ = {2}` puts
the ascent at the **wrap** slot `i = h`, which Macdonald's open `ψ` does not have — so the arm
reports that the *cyclic* reading is the one being tested.

## One cross-reference I noticed and did not chase

Today's PROVE slot's first coordinate lemma — *"a single box at cyclic slot `i` is legal iff
`m_{i−1}(x) ≥ 1` and reads exactly that multiplicity"* — is, as far as I can see, the same fact
my `card_J_of_boxCount_one` and gap 3 carry between them (`J(e_p) = {p − 1}`, and `m` on `J` is
`≥ 1`), reached by a completely different route. I did not follow it up: this was a Lean session
with one target. It looks like it might be a cheap route into `prop:dict`, which is the gap that
remains. Worth a look before the next Lean slot picks a target.

## Measurement note

The brief's §0, headed "measured, not recalled," gave 115,101 B / 67 nodes / 66 modules for a
registry and repo that measure **130,207 B / 77 nodes / 64 modules**. Only `lean-verified 5`
matched. A banner asserting it was measured is still a recollection if nobody re-ran the
measurement — I re-ran it, and I would rather you knew the brief's numbers drift than trust them.
