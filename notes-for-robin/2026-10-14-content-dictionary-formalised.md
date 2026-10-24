# The content half of `prop:dict` is in Lean — and its domain is bigger than the paper's

2026-10-14, LEAN session. Robin — the short version and then the one thing worth your time.

**Short version.** `Tableau.boxCount_eq_one` was the last hypothesis field standing between
the Lean chain and an unconditional `ord_{t=1} Ψ_T = ν(T) = n`. It is now a theorem.
26 declarations, sorry-free, 27 `#print axioms` records, 0 non-standard, whole project
builds (3464 jobs, exit 0).

* Module: https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/ContentDictionary.lean
* Writeup: https://github.com/clio-vega/proofs/blob/main/2026-10-14-lean-content-dictionary.md
* Axioms evidence: https://github.com/clio-vega/proofs/blob/main/2026-10-14-lean-content-dictionary-axioms.txt

**The thing worth your time.** I was told to write down the domain of the paper's `prop:dict`
and the domain of my Lean version side by side before writing the statement. They are not the
same set, and the difference is the result.

The paper's proposition quantifies over cylindric row-strict tableaux of `λ ∈ Par(h,w)`:
rows strictly increasing, columns weakly increasing, the cylindric identification
`T(i,j) = T(i+k, j−n)`, entries bounded. The content sentence — `Σ_i θ^{(a)}_i = α_a` — needs
**row-strictness and nothing else**. Not the columns, not the cylinder, not the partition
condition, not the bound. My `Filling` imposes only row-strictness, over arbitrary row lengths,
and D1 and D2 go through.

So the statement is *stronger* than the paper's, and the three dropped conditions turn out to
be spent entirely on the region condition — which is a different proposition (HKKO Prop. 2.7)
and is still a hypothesis. `prop:dict` splits three ways, not the two I had predicted, and the
half I guessed would be tractable (Korff's Lemma 5.4 relation) turned out not to be needed at
all: it is a statement about `m`, and `boxCount_eq_one` never mentions `m`.

The cylindricity was riding along because the English sentence travelled inside a paragraph
about cylindric tableaux. Third session running that a noun hid a quantifier a typed binder
had to declare — "strip", then "the index map", now the package `prop:dict` was stated in.

**Honest accounting.** The obstruction count goes **1 → 1**, not 1 → 0. `Tableau.mem` was
already a field; `toTableau` takes exactly that hypothesis and nothing else. What changed is
*which* statement is assumed — geometric now, with a named external source, rather than a
bundled combinatorial one. `q410-no-cyclic-psi-weight` is declined for promotion a seventh
time; the grade went to a scope-stated child, `content-dictionary-formalised`.

**One control that reported against me.** I planted a `sorry` at the dependency root. On
10-13 the equivalent plant spared the non-vacuity controls, which is what made them a second
mechanism. This time it reached all six of them — because they are built *by* `toTableau`,
the very thing under test. A `Tableau`-level non-vacuity control cannot be independent of a
theorem that constructs the `Tableau`. The genuinely independent survivors are the two
kernel computations on the raw filling (`witF_content`, `witF_mem`). I'd rather record that
than quietly keep calling the `witT_*` family corroboration.
