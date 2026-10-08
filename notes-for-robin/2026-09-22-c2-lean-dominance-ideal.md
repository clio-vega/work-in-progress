# `prop:ideal`'s order-theoretic core is machine-checked

**2026-09-22 c2 (Day 200), LEAN session.** Sorry-free.

Declaration: `RobinHood.dominance_ideal`
File: https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/DominanceIdeal.lean
Commit: `clio-vega/tworow-d4-kernel@e5a80df`
Write-up: https://github.com/clio-vega/proofs/blob/main/2026-09-22-c2-lean-dominance-ideal.md

This is Proposition `prop:ideal` of the cylindric M-convexity paper — `P(W_ℓ(λ/μ))` is a
dominance order ideal — with its two combinatorial inputs (`cor:bk`, the cylindric
Bender–Knuth involution; `cor:exchange`, a bead sliding one site) as **explicit
hypotheses rather than sorries**. The bead-chain model is not formalised and I am not
claiming it is. The Lean file *says* it assumes them, and the registry parent node
`root/dominance-ideal` deliberately stays `proved`, not `lean-verified`.

`lake build` green, 2987 jobs. All seven new declarations: axioms exactly
`[propext, Classical.choice, Quot.sound]`.

## Four things Lean extracted that the paper does not contain

**1. The measure.** The paper's proof is four lines and its only gap is the phrase
"by induction on the (finite) number of steps" — the terminating measure is never named.
It is

  `gap ℓ σ ν = ∑_{r<ℓ} (psum ν r − psum σ r)`,

the area between the two partial-sum profiles. It is `≥ 0` exactly when `σ ⊴ ν`, and a
Robin Hood step drops it strictly because the profile falls by one unit on the window
`(a, b]`. I think this is worth a sentence in the paper regardless of the formalisation
— it turns a hand-wave into a one-line justification.

**2. A side condition the paper never states.** `gap` sums over `r < ℓ`, so the strict
drop needs its witness inside that range: `b < ℓ`. That is **not** a conclusion of
`robin_hood_step` (Lemma `lem:hlp`). It has to be recovered — `a < ℓ` because
`ν_a ≥ ν_b + 2 ≥ 2 > 0`, and then the size equation forces `b < ℓ`. Without it the
induction has no measure. This is the kind of thing only a type-checker asks for.

**3. The sorting bridge is one identity.** The paper appeals to `S_ℓ`-stability plus
sorting. Constructing `sort` in Lean would have eaten the session. It is unnecessary:
with `π = swap(a+1, b)`,

  `ex a (a+1) (ν ∘ π) = (ex a b ν) ∘ π`

— *the near exchange applied to the twisted vector is the far exchange, twisted*. `π` is
an involution, so one more application of `S_ℓ`-stability untwists it. The whole bridge
is 25 lines. I like this one; it is the statement I would have wanted in the paper.

**4. One hypothesis I had listed is not consumed.** I had expected to need "every
`β ∈ W` has `∑β = d` and `β ≥ 0`". The proof does not use it — the instances that are
needed are already carried by `IsPart` and by the theorem's own equal-size hypothesis.
So it is not assumed, and the theorem is correspondingly stronger.

## The control worth looking at

An abstracted theorem with two assumed hypotheses can be true for the wrong reason, so
I added `hexch_load_bearing`: the `S_2`-orbit `W₀ = {(3,1), (1,3)}` satisfies **every**
hypothesis except `hexch` — transposition-stable, contains the partition `ν = (3,1)`,
and `σ = (2,2)` is a partition of the same size with `σ ⊴ ν` — yet `σ ∉ W₀`. So the
result genuinely consumes `cor:exchange`; it is *not* an order-theoretic fact about
`S_ℓ`-stable sets. That was the shape of error the abstraction invited, and it is now
closed by a machine-checked counterexample rather than by my confidence.

## Still open

Both combinatorial inputs, i.e. the whole periodic-Maya bead-chain model. `cor:bk` is
the harder one (cylindric shapes, horizontal strips, well-definedness of the
involution) and is a multi-session project on its own. Neither is blocked; both are
large. The order-theoretic scaffolding above them is now checked end to end.
