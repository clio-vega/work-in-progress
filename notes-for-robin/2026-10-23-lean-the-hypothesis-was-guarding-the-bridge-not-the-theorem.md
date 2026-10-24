# 2026-10-23 LEAN — the hypothesis was guarding the bridge, not the theorem

**Sorry-free.** `TworowD4Kernel.RhoShiftVanishing`, 18 declarations, 0 sorry, standard
three axioms. Commit `21883d2` in `clio-vega/tworow-d4-kernel` (not pushed).
Artifact: `proofs/2026-10-23-lean-rho-shift-vanishing.md`.

## What I formalised

The forward ρ-shifted vanishing law from Wednesday's Q553 note — *if `θ_j − θ_k = k − j`
for some `j < k` then the alternant `det(x_i^{m_j})` vanishes*, where `m_j = θ_j + j − 1`.
Three declarations, deliberately not grouped: the index bridge (as an **iff**, which is
what this morning's Q559 converse actually consumes), the two-equal-columns determinant
step, and their composition with the paper's hypothesis verbatim.

**It does not reach `Ψ^C`.** The step from a vanishing alternant to a vanishing `Ψ^C` is
the alternant expansion `thm:alt`, which is unformalised, so the parent registry node
stays at `proved` and only the new determinant-layer child is `lean-verified`. A
Lean-verified summand is not a Lean-verified sum.

## The thing worth telling you

I pre-registered four lesions. Three came back as predicted. The fourth is the session.

I predicted that `x_i ≠ 0` would be **irremovable** for the Laurent (`zpow`) statement —
the one the paper actually claims — because negative exponents obviously demand units.
Lean proved the theorem over a bare field with **no hypothesis on `x` at all**, by the
identical four-line proof as the non-negative-exponent version. Two reasons, both of which
were sitting in front of me: Mathlib's `zpow` is *total* on a `GroupWithZero`, so
`0^(−1) = 0` and the entries exist regardless; and `det_zero_of_column_eq` asks only that
two columns be **equal**, which cannot tell whether the entries are invertible.

So where does the nonvanishing go? I went looking, and proved the one lemma that needs it:
`det_zpow_shift`, which says that shifting every exponent by a constant multiplies the
determinant by the monomial `∏ x_i^c`. *That* needs `x_i ≠ 0`, because `zpow_add₀` does.
And the vanishing law never calls it.

What I had done was reason about the statement by reasoning about the **route I imagined
taking to it**. I had in mind the argument "shift the exponents up until they're
non-negative, then it's an ordinary alternant" — and that argument needs units, so I filed
the hypothesis against the destination instead of against the bridge. The destination was
always reachable directly.

It is the same shape as the genericity hypothesis in October's type-B work, which belonged
to the theorem that *separates* rather than the characterisation it was attached to. I now
have two instances, which is enough to make it a habit rather than an anecdote: **when a
hypothesis feels necessary, name the lemma that consumes it before believing it is needed —
and if the only candidate is a step you have not taken, try the statement without it.**

## Smaller things

* The 1-indexed / 0-indexed worry evaporated for a structural reason I should have seen:
  the hypothesis only ever mentions the **difference** `k − j`, which is the same in both
  conventions, and the conclusion is invariant under a constant exponent shift. I proved
  this (`injective_add_const_iff`) for an arbitrary constant rather than just for the `−1`,
  so the whole family of conventions is covered at once.
* `r ≥ 2` is **absent**, not removable, and this time I located it properly: the
  existential `∃ j k : Fin r, j ≠ k` implies it, and I derived it (`rhoTie_forces_two_le`)
  rather than just observing a green build. An absent binder and a surviving lesion look
  identical from the build log.
* The planted-sorry control fired — **and the build still said `Build completed
  successfully`**, because a `sorry` is a warning, not an error. That success line carries
  no information about sorry-freeness, in either direction. Worth knowing if you ever read
  one of my build logs.
* The non-vacuity control is the one I care about: `θ = (0,0)` gives `det = 1/6 ≠ 0`.
  Confirming the vanishing arm forty times could never have established that.

## Still local, still not shipping

`/home/clio/projects` is not a git repository, so the artifact, the digest and the registry
exist only on my volume. The Lean module does ship (it has its own repo). This is the same
standing condition I flagged on the registry's peer references — not new today, but it
keeps being true, and I would rather name it every time than let a green file-existence
check stand in for reachability.
