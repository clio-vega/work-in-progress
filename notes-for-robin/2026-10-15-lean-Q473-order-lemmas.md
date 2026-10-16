# Q473's two order lemmas are now machine-checked — and the lesion found a free hypothesis

**LEAN 2026-10-15.** Both targets sorry-free, in one module.

* Lean: `clio-vega/tworow-d4-kernel` @ `e1ba5af`,
  [`TworowD4Kernel/HalfspaceOrder.lean`](https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/HalfspaceOrder.lean)
* Writeup: [`2026-10-15-lean-Q473-order-lemmas.md`](https://github.com/clio-claude/proofs/blob/main/2026-10-15-lean-Q473-order-lemmas.md)
  (if that org is wrong, it is the `proofs` repo @ `6451de5`)
* Registry: two new children at `lean-verified` in `registry/halfspace-sixvertex-orthogonality.json`.
  That tree had **8 proved / 0 lean-verified** before today.

`lem:order` entire — `⪯` a partial order on strict partitions, least element `∅`, every
principal down-set finite, hence well-founded — **plus** the contrast, which is the half of
the Q473 headline no computation in the paper verified: `¬ WellFounded (· > ·)`, witnessed by
`(1) ≺ (2) ≺ (3) ≺ ⋯`. The choice of `⪯` over `⪰` is now machine-checked as *forced*.

`lem:match` both directions.

## Three things worth your time

**1. A hypothesis I was charging myself for and never spending.** I deleted the
strict-decrease field from the structure and rebuilt. **All 22 declarations still compile.**
So `lem:order` is true for *arbitrary lists of positive naturals*; strictness is free. My
paper proof does use decrease ("every element of `κ'` lies in `[κ_1]`") — the Lean route, an
injection of the down-set into `∀ i : Fin |κ|, Fin (κ_i + 1)`, needs only the pointwise bound.
Same for the length clause of the definition: positivity forces it, so `def:order`'s two
clauses are not independent.

**2. I did not prove the clause I most wanted to.** The paper's forward direction of
`lem:match` runs on *"pointwise domination is preserved by decreasing rearrangement"*, stated
in one clause and never proved. Lean would not let me assert it — so I replaced it with a
counting argument (`j+1` indices injecting into a hosting set of size `≤ j`). **The clause is
still unproved.** The lemma no longer needs it, which is a different and lesser thing than
having earned it.

**3. An instrument of mine returned a clean-looking zero over a domain it was blind to.** To
decide (1) I first scanned proof terms for the constant `SP.chain`: 0 users. It also reported
**0 users of `SP.pos`, which the proofs demonstrably spend** — structure projections are
`Expr.proj` nodes, not constant applications. Only the positivity control exposed it. That is
the "empty domain greps like a clean one" failure again, and the thing that caught it was
pointing the instrument at a fact I already knew.

## One for you to fix (read-only to me)

`code/registry_validate.py`'s `--proofs-dir` **defaults to the registry's parent** (`proofs/`),
but node `file` fields already carry the `proofs/` prefix — so the flagless form the LEAN skill
prescribes double-prefixes and prints **13 false "file not found" problems**, 11 of them on
nodes that predate today. There is no wrong flag to omit here; the default is the fault.
Correct form from `projects/`: `python3 code/registry_validate.py --proofs-dir . <registry>`
→ `OK ... is valid`, exit 0.

## Not carried

`thm:tri`, `thm:main`, `lem:phi`, and deliberately **not** `thm:top` — it rests on Hypothesis H,
the open analytic interchange, and grading it would have manufactured a `lean-verified` badge
for something unproved. `evaluation-triangularity` and `topological-independence` stay at
`proved`.
