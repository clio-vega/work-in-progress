# The cyclic/open ascent dichotomy is Lean-verified — 2026-10-11

Robin — this is **on GitHub**, both halves:

- Code: https://github.com/clio-vega/tworow-d4-kernel/blob/d37a524/TworowD4Kernel/CyclicAscent.lean
- Repo note: https://github.com/clio-vega/tworow-d4-kernel/blob/d37a524/NOTES-2026-10-11-cyclic-ascent.md
- Snapshot + controls: `proofs/2026-10-11-lean-cyclic-ascent.md` at `proofs` commit `5227716`
- Registry: `cylindric-statistic.json`, new child `cyclic-open-dichotomy-formalised`

**15 declarations, 0 sorries, standard three axioms only** (the rigidity core is even
choice-free: `[propext, Quot.sound]`).

The result, in one table — a binary word of length `h`, "ascent" = reads `false` then `true`:

| successor | ascent-free words are | how many |
|---|---|---|
| cyclic (`ZMod h`) | **constant** | **2**, every `h ≥ 1` |
| open (`Fin h`) | antitone, i.e. `1^a 0^{h-a}` | **h + 1** |

and `card_ascentFree_lt`: strictly more open than cyclic, every `h ≥ 2`. The cyclic locus does
not grow with `h` at all. That rigidity is exactly why Korff's cyclic `ψ`-grading can carry so
little, and the gap is the Q410/Q417 story in one integer.

**Three things worth your eye:**

1. **The brief's hard case was the easy one, for a reason I want to remember.** It predicted a
   `Nat.find` walk — "from a `false`, step forward to the first `true`, its predecessor is the
   ascent." I never wrote that walk. Proving the *stronger* conclusion (constant, not merely
   "has an ascent") makes it eight lines: no-ascent is the one-step inequality `θ(i+1) ≤ θ i`,
   iterating gives `θ(i+n) ≤ θ i` for natural `n`, and in `ZMod h` the element `1` **generates**,
   so that inequality holds between every ordered pair *in both directions* and antisymmetry
   collapses the word. Strengthening the conclusion deleted the search. The existential form was
   hiding a one-liner behind a pigeonhole.

2. **I declined the promotion the brief ordered.** It said set `cyclic-ascent-lemma` to
   `lean-verified`. That node asserts four things and Lean carries one — the `ord_{t=1} Ψ_T =
   ν(T)` identity, `ν(T) = n` at `α = (1^n)`, and the region condition are all still paper-only.
   So the parent stays `proved` and I added a child node that states the formalised scope and
   names the three unformalised assertions. The label would have been arithmetically fine and
   denotationally false.

3. **Both validators grade a fabricated declaration name as `OK`.** I planted
   `ZMod.this_does_not_exist` in the node's `lean` field: `registry_validate.py` → `OK`,
   `trustcheck.py` → `OK`, 0 problems. A bogus *trust enum* fires (2 problems) — so they are
   alive on tree shape, blind on the leaf. **Every `lean-verified` grade in the registry rests on
   my own `#print axioms` run.** If you ever want that automated, the hook is
   `registry/registry_lean_resolve.py`, which already exists but is not wired into either
   validator.

Also: `registry_validate.py`'s default `--proofs-dir` double-prefixes the node `file` paths —
**40 false "not found" problems**, 0 with `--proofs-dir /home/clio/projects`. Fifth tool in this
family. The `proofs/` prefix in the JSON and the tool's default root are redundant with each
other and nothing warns.
