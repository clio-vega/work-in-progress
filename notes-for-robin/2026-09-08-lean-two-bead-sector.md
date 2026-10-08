# The two-bead sector is machine-checked — and the case split was the mistake

**Repo:** https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/CrossRankTwoBead.lean
**Commit:** `clio-vega/tworow-d4-kernel@9843435`
**Write-up (local only):** `proofs/2026-09-08-lean-Q92-two-bead-sector.md`

## What landed

```lean
theorem twoBeadSector_commutator_eq_zero_of_mul_eq_one {R : Type*} [CommRing R] (t s : R)
    (hts : t * s = 1) (he : 0 < e) (hf : 0 < f) :
    twoBeadSector f e M M' s t - twoBeadSector e f M M' t s = 0
```

If `ts = 1`, the two-bead sector of `[R_e(t), R_f(s)]` vanishes — any `CommRing`, every `M`
and `M'`. 14 theorems, 0 sorries; `lake build` and `lake test` both exit 0; `#print axioms`
is the standard three, asserted as an equality.

## The part worth your time

I went in to hand a type checker a **correction to my own paper**. Q92 Thm 2.3(2) had said
"if `e = f` then the two-bead element is `0`". That is a *one-parameter* statement: at `e = f`
there are two legal assignments whose indices `k` are negatives of one another, and they cancel
only at `s = t`. With `t ≠ s` the sector is `(t-s)(1-st)`, not zero. A numerical sweep found
exactly 61 disagreements, all of them `e = f` two-bead entries.

The Lean proof needed **no case split at all**.

Reversing the order of the two moves is an involution on routes — `Prod.swap` is a bijection
`twoBeadRoutes e f M M' → twoBeadRoutes f e M M'` — and on `ts = 1` the two orderings carry
the *same monomial*, because the two heights sum to the same total either way (`P' + Q' = P + Q`,
in `ℕ`). So the two sums cancel termwise under the bijection. The classification of legal
assignments — one when `e ≠ f`, two when `e = f`, which is what the paper reads the factor
`1 - (ts)^k` off — is never used. The involution does not need to count its fixed points.

So the `e = f` case that the old clause got wrong is covered with no case split, which is a
better outcome than proving the classification would have been. The error was not in *which*
branch of the split was right; it was that there was a split.

## What I did NOT prove — please read this bit

Corollary 4.2(iii) is an **iff**: the sector vanishes identically *if and only if* `ts = 1`.
Only the **if** direction is a Lean theorem. The **only if** is witnessed solely by `#guard`s
exhibiting nonvanishing at `ts = 2`. So I left the registry node `Q96-ts-equals-one-locus`,
which states the iff, at `proved` and created a **new** node for exactly the half that is
verified. Also unformalised: the assignment classification, and the two-parameter one-bead
sector. `Q92-structural-divisibility` is untouched — different statement.

## One thing I want you to be sceptical about

Today's PROVE session closed Q99 on the locus `st = 1` from the vertex-operator side, where
the exchange relation degenerates to a *nonzero* multiplication operator. This session found
the two-bead commutator sector *vanishing* on the same locus. Same hyperbola, two banks.

I have **not** checked whether these are the same phenomenon, and I don't think the coincidence
of a locus is evidence that they are — they are statements about different objects (`H^t_m`
versus `R_e(t)`, a full commutator versus one sector). If you see me write "`st = 1` is the
degenerate locus" in a future digest as though it were one fact, that is a merge I have not
earned. It needs someone to read both definitions side by side.
