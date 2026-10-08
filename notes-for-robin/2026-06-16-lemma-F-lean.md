# Lemma F (and the two-factor F2) — machine-checked

**2026-06-16 lean session.** Robin — the uniform boundary engine is now formalised. Both the
single-factor **Lemma F** and the two-factor **Lemma F2** are named Lean declarations in
`tworow_d4_kernel`, **zero `sorry`, zero warnings, only the 3 standard axioms**
(`propext`, `Classical.choice`, `Quot.sound`).

File: `TworowD4Kernel/LemmaF.lean` (snapshot in `proofs/2026-06-16-lean-lemma-F/`).

## What got proved

```lean
theorem lemma_F {R Q t₀ : ℕ} (hQ : 4 ≤ Q) (ht₀ : t₀ ∈ Finset.Icc 1 Q) :
    padicValNat 2 (R + t₀) + 1 ≤ padicValNat 2 (∏ t ∈ Finset.Icc 1 Q, (R + t))

theorem lemma_F2 {R Q t₁ t₂ : ℕ} (hQ : 6 ≤ Q) (ht₁ : t₁ ∈ Finset.Icc 1 Q)
    (ht₂ : t₂ ∈ Finset.Icc 1 Q) (hne : t₁ ≠ t₂) :
    padicValNat 2 (R + t₁) + padicValNat 2 (R + t₂) + 1
      ≤ padicValNat 2 (∏ t ∈ Finset.Icc 1 Q, (R + t))
```

The proof is exactly the informal one: split the consecutive product `∏_{t=1}^{Q}(R+t)` with
`Finset.mul_prod_erase` to peel off the distinguished factor(s); among the first `4` (resp. `6`)
consecutive integers there are `2` (resp. `3`) even ones, so an even factor *survives* the
deletion(s); `2 ∣ rest`, hence `v₂(rest) ≥ 1`; finish with `padicValNat.mul` additivity. No new
mathematics — it's the elementary primitive the `c=1`/`c=2` boundary lemmas were waiting on.

## Honesty flag — the F2 hypothesis in LEAN.md is one notch too generous (corrected)

The LEAN brief asked for the stretch goal as:

> Among `Q ≥ 5` consecutive integers, for any TWO distinguished factors `R+t₁, R+t₂`,
> `v₂(∏) − v₂(R+t₁) − v₂(R+t₂) ≥ 0`.

That statement is **true but vacuous**: for distinct `t₁ ≠ t₂` the product *contains* both factors,
so `v₂(∏) = v₂(R+t₁) + v₂(R+t₂) + v₂(rest) ≥ v₂(R+t₁) + v₂(R+t₂)` for **any** `Q ≥ 2` — the
remaining factors can never make the valuation drop below the sum. The `Q ≥ 5` and the "≥3 evens,
one ≡0 mod4" reasoning carry no weight for the `≥ 0` claim.

The version with actual content — and the one the `c=3` `a`-odd top genuinely needs (the **F2** you
named in the 06-16 prove note) — is the **surplus** form:

> Among `Q ≥ 6` consecutive integers, two distinct deleted factors still leave the product **even**:
> `v₂(∏) − v₂(R+t₁) − v₂(R+t₂) ≥ 1`.

I verified the thresholds numerically before formalising (`R < 500`, `t₁ ≠ t₂`):

| claim | range | result |
|---|---|---|
| `Q ≥ 5`, surplus `≥ 0` (LEAN.md) | `Q ∈ [5,40]` | 0 fail (vacuously true) |
| `Q ≥ 6`, surplus `≥ 1` (F2) | `Q ∈ [6,40]` | **0 fail** |
| `Q = 5`, surplus `≥ 1` | `R < 500` | **500 fail** — `Q ≥ 6` is SHARP |

So I formalised the **true keystone**: `Q ≥ 6`, surplus `≥ 1`. The `Q = 5` failures are exactly the
`R`-even starts whose only two even factors are `R+2, R+4` — delete both and the rest is odd. This
matches your 06-16 prove note ("`Q ≥ 6` SHARP"); it's the LEAN.md wording (drawn from the 06-15 note)
that was the loose one. Single-factor Lemma F is unchanged: `Q ≥ 4`, surplus `≥ 1`, and `Q = 3`
genuinely fails (100/600 in a small sweep), matching §1.3.

## How close is a fully machine-checked `c = 1` boundary lemma?

Close, but not one step away. With Lemma F now formalised, the **arithmetic primitives** for the
`c=1` boundary are all in Lean (Lemma F here; the hook Kummer lemmas K/K′, the central-binomial and
choose-valuation helpers in `HookKummerLemmas.lean`). What is **not** yet formalised, and stands
between us and an end-to-end `c=1` boundary statement, is the *bridge layer*:

1. the **3-row hook formula** `f^{(a,b,c)} = (2m)!(a−c+2)(a−b+1)(b−c+1) / [(a+2)!(b+1)!c!]`
   as a `Nat`/`Int` identity (pure factorial algebra — Mathlib-reachable, a real but finite job);
2. the **Kummer carry-expansion** turning `Δ(b+i)` into *(positive linear in `b`) + 2·carries −
   2·v₂(factor)* — this is where Lemma F plugs in; needs `padicValNat` of the hook ratio via
   Legendre, which we have the pieces for;
3. the assembly `val(b+i) > V ⟺ Δ(b+i) ≥ 2 − θ` and the `c=1` clean form
   `Δ(b+1) = (b−3) + 2v₂(a+2) + 2(s₂(m−b) − s₂(a))`.

None of these needs the symmetric-function content (`G_λ`, `M_j` as a Jacobi–Trudi determinant) —
those stay out of Mathlib reach, as in every prior session. So a machine-checked `c=1` boundary
lemma is a **bounded factorial-algebra + Legendre formalisation away**, with the hard 2-adic core
(Lemma F + K/K′) already done. I'd estimate one focused lean session for the hook-formula identity
and a second to wire the `Δ(b+1)` assembly. Flagging it as the natural next lean target.

— Clio
