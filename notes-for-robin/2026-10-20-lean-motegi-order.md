# For Robin — 2026-10-20 LEAN: Motegi's order is Lean-verified, and the paper's quantifier range was a hypothesis

`lem:order` and `cor:order` of `proofs/2026-10-19-c2-sa-divisors-full-q.tex` are now
**sorry-free in Lean**, complete, with the standard three axioms.

- Module: `TworowD4Kernel/MotegiOrderTailCount.lean`
- Repo: https://github.com/clio-vega/tworow-d4-kernel (commit `002e639`)
- File: https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/MotegiOrderTailCount.lean
- Full record: `proofs/2026-10-20-lean-motegi-order-tail-count.md`

40 declarations enumerated from the environment, 0 sorries, axioms exactly
`[propext, Classical.choice, Quot.sound]`.

## What is verified

| | |
|---|---|
| **T1** `MLe_iff_tail` | `B ≤ A ↔ ∀ k, B_{≥k} ≤ A_{≥k}` |
| **T2** `MLe_refl/_trans/_antisymm` | `≤` is a partial order (+ a bundled `PartialOrder` instance) |
| **T3** `MLe_erase`, `downset_erase_closed` | `A ∖ {m} ≤ A`; down-sets closed under the boundary collision map |
| **T4** `MLe_iff_compl` | complementation in `range N` reverses the order (+ `motegiComplOrderIso`) |

The entry point is `MLe` from `MotegiOrder.lean`, which I committed on 10-17 in
**Motegi's own increasing enumeration** (arXiv:2610.15344 Thm 2.6(i), L625–L636),
before I had the tail-counting reading. So T1 is a genuinely falsifiable theorem
against a definition transcribed from the source, not a restatement of a convenient
form. It held exactly as the tex displays it.

## Three things you may want to change in the paper

**1. `lem:order` should name its ambient.** The tex quantifies `k ∈ [N]`. Over
`Finset ℕ` that restriction is **strictly weaker** and the lemma is false as stated:
`B = {0}`, `A = ∅` satisfies every tail inequality for `k ≥ 1` while `B ≰ A`
(`control_L1b_restrict_one_fails`). The tex is *correct in its own domain* — in
`[N] = {1,…,N}` nothing is below 1, so its `k = 1` instance **is** the cardinality
clause `r ≤ s`, exactly as the proof says at L272. But that means the clause `r ≤ s`
is not a second condition at all: it is the tail inequality at the smallest index the
ambient admits, and *which index that is* depends on the ambient. I would state
`lem:order` with the ambient named, or over all finite subsets of `ℤ_{≥0}` with
`∀ k ≥ 0`.

The sharp version: the same `N` is **absent** from `lem:order` and `cor:order`(2) —
they hold with no ambient bound whatever (`MLe {1000} {1000, 10⁹}`) — and
**irremovable** from `cor:order`(3), which cannot even be *stated* without it. One
symbol, opposite roles, three corollaries apart.

**2. `cor:order`(3) is stronger than "anti-automorphism."** Complementation inside a
*fixed* `range N` is an **order-reversing involution**, and I can exhibit it as a
bundled `OrderIso` onto the order dual:
`motegiComplOrderIso : MotegiBelow N ≃o (MotegiBelow N)ᵒᵈ`, where `MotegiBelow N` is
`{A // A ⊆ range N}` carrying `MLe`. "Anti-automorphism" records neither the
involutivity nor that the ambient is fixed — and `cor:order`(3) currently writes `Aᶜ`
without naming `N`.

**3. `cor:order`(2) is the one-element case of something free.** *Every* subset is
Motegi-below (`MLe_of_subset`), immediately from monotonicity of the tail count. The
paper's "deleting an element decreases every `A_{≥k}` by 0 or 1" is more careful than
needed — the amount never matters, only the sign. And `cor:order`(1)'s antisymmetry
does not need the counting function at all: `MLe B A` and `MLe A B` pin the two
increasing enumerations entrywise, so `B = A` directly (`MLe_antisymm_asc`). Both
routes are in the file.

## One structural remark

The paper proves `lem:order` by two index chases (L272–276 and L278–283). In Lean they
are the *same* biconditional applied at two different points:

> for a decreasingly sorted list and `i` in range, `k ≤ l[i] ↔ i < #{entries ≥ k}`
> — *the `(i+1)`-st largest entry is `≥ k` exactly when more than `i` entries are.*

(⇒) is that iff at `i = B_{≥k} − 1`; (⇐) is it at `k = ` the `(c+1)`-st largest of `B`.
Nothing else about sortedness is used anywhere in the formalisation. The two chases
are one argument read forwards and backwards — worth a sentence in the paper, since it
is also why `cor:order` falls out in four lines.

## Scope — what is NOT verified

Only the order theory. No `w`, no `q`, no field, no root system. In particular **not**
`lem:inverse`, `lem:gamma`, `lem:gnz`, `thm:S`, and not the *use* of `cor:order`(3)
that motivated the target — that the support of Motegi's inverse formula agrees with
the chain-expansion support of `lem:gamma`. T4 is the bridge; the two mechanisms it
bridges are not formalised. So `boundary-divisors-converse-full-q` stays
`in-progress` and `tail-counting-order` stays `proved`; the new `lean-verified` node
is a child.
