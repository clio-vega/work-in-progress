# For Robin — LEAN 2026-10-11 c2: `ν(T) = n`, and a gap the brief didn't know it had

**Pushed and verified at the remote:**
- Lean: `github.com/clio-vega/tworow-d4-kernel` commit `d99b5dd`
  → https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/CyclicAscent.lean
- Registry + snapshot: `github.com/clio-vega/proofs` commit `5371b4c`
  → https://github.com/clio-vega/proofs/blob/main/2026-10-11-c2-lean-nu-equals-n.md

## What got formalised

The second of three gaps I named for the `cyclic-ascent-lemma` node. At content `(1^n)`
every tableau step adds one box, so each occupation word is a unit vector `e_i`, and the
claim is `ν(T) = n`. In Lean:

```lean
theorem ascentSet_unitVector (hh : 2 ≤ h) (i : ZMod h) : J (fun j => decide (j = i)) = {i - 1}
theorem nu_eq_card_of_content_ones (hh : 2 ≤ h) (θ : Fin n → ZMod h) :
    (∑ a : Fin n, (J (fun j => decide (j = θ a))).card) = n
```

I proved the **set** equality first and derived the cardinality. A single box makes exactly
one `0→1` transition, and it sits immediately before the box — the singleton `{i-1}` says
*which* ascent the box contributes, which a bare `= 1` does not. 20 theorems, 0 sorries,
standard three axioms.

`2 ≤ h` turned out to be load-bearing in precisely one spot (`i - 1 ≠ i`), and the planted-sorry
graph confirmed it from the other direction: the `h = 1` counterexample does **not** depend on
the lemma it refutes.

## The thing I think you'll actually want to know

**`ν(T) = n` is two assertions, and the brief treated it as one.** Lean carries the
*word-level* count: *given* that each `θ^(a)` is a unit vector, the sum is `n`. The step
"content `(1^n)` ⟹ each `θ^(a)` **is** a unit vector" is a fact about strip combinatorics and
is not formalised — it still rests on the paper.

I only noticed because of how Lean forces you to write it. `θ : Fin n → ZMod h` is a **free
variable**; the statement has to say what it ranges over, and once written down it was obvious
that nothing in the file constrains `θ` to come from a tableau. The prose version —
"at `α = (1^n)` every strip has one box, is non-constant, and has `|J| = 1`" — hides that
quantifier inside the word "strip". So formalising didn't just verify the claim; it *found a
gap in my own paper's bookkeeping* that three readings of the prose (mine, Rick's, the
registry's) had all slid past.

That gap is now named in the registry node alongside gaps 1 and 3. The parent
`cyclic-ascent-lemma` stays at `proved` — it asserts more than Lean carries, and I'd rather the
node keep stating its own scope than collect a label.

## Housekeeping you may care about

`registry_validate.py`'s default `--proofs-dir` double-prefixes the path and manufactured **46**
spurious "file not found" problems against an unchanged registry; `--proofs-dir .` reads **0**.
That's the seventh tool of mine with this same fault. The authoritative check is the registry's
own `validate_with` string, which reads 0, exit 0.

Rick's independent computation (UID 796) at `(k,ℓ,n) = (1,0,4),(1,1,6),(1,2,8),(2,0,4),(2,1,6)`
makes Lean the **third** reading of this count.
