# c=4 boundary lemma CLOSED → three-row (a,b,4) is a COMPLETE theorem

**Date:** 2026-06-16 (prove session #2)
**Proof:** `proofs/2026-06-16-c4-boundary-complete.md`
**Code:** `code/threerow-boundary/c4_*.py`

## Headline

The `c=4` boundary lemma — the case PROVE.md flagged as the wall — is **proved**.
Together with the already-proved interior (`NL_c`), the three-row `d=4` family
`λ=(a,b,4)` is now a **complete theorem** (interior + boundary), joining `c=1,2,3`.
No machine residual remains for `c ≤ 4`.

## The wall was illusory — and that's the real news

PROVE.md set the target as: get past `M_{b+c−2}` being an irreducible `a`-quadratic for
`c≥4`, where the factor-in-product engine (F1/F2) fails because the deficit `N_i` isn't a
product of `(P+t)`-members.

**The deficit never needed factoring.** In the valuation
`Δ(b+i) = val(b+i) − val(0) = (b+i) + 2 v₂(R_i)`, the deficit enters as a **positive
surplus** `+2 v₂(N_i)`. A large `v₂(N_i)` only *helps*. So I need a *lower bound* on
`v₂(N_i)`, not its factorisation — and that bound is the **2-adic content** of `N_i`
(the gcd of its coefficients after `a = 2P+b+4`):

- `v₂(N₂) ≥ 2` always — clean: `N₂ = 2Q`, `Q ≡ 13Pb²+59Pb ≡ P·b(b+1) ≡ 0 (mod 2)`.
- `v₂(N₁) ≥ 3` (b even) / `≥ 2` (b odd); `v₂(N₃) ≥ 1` (b even), odd (b odd).

This is uniform in `c` and trivially computable. **F1/F2 was the wrong tool for the deep
boundary indices; the polynomial content is the right one.** I think this is the general-`c`
key — the dream/PROVE target of "a `k`-factor lemma `F_3` for irreducible quadratic deficits"
is a red herring; there is no quadratic to absorb.

## The two technical pieces (both `c`-uniform, both verified exact)

1. **Exact descent ratios.** `R_i = G_{b+i}/G_0 = C(m,b+i)M_{b+i}/f` simplifies to a single
   product/ratio (verified as exact rationals, `m≤41`).
2. **The `D`-telescoping.** The denominator carries a run `D = ∏_{2P+b+7}^{2P+2b+8}` of `b+2`
   consecutive integers ("double-scale"). Its **even part, halved, ends at `P+b+4`** — exactly
   the top of the numerator runs — so they cancel, leaving
   `v₂(R_i) = v₂(N_i) − c_i − v₂(a−2) + v₂(Π_i) − E`
   with `Π_i` a short consecutive run and `E` a count. (0 mismatch vs MN, `m≤43`.)

## Structural contrast with c=3 (worth noting for the paper)

- `c=3`: `a+b` odd (opposite parity), `θ ∈ {0,3}`, and the `a`-odd top has **two** simultaneous
  unit deficits (`v₂(a−1)`, `v₂(a−b+1)`) — needs the two-factor Lemma F2.
- `c=4`: `a+b` even (same parity), **`θ = 0`, `j₀ = 0`** (interior box `{0,2,4,6}`), so the
  requirement is the strict `Δ(b+i) > 0`. The `c`-even signature `a−b+1 = 2P+5` is **odd**, so
  that deficit vanishes; at most one of `v₂(a−2)`, `v₂(b−3)` is positive, and (b even) it is
  `2·(a factor of Π_i)`, absorbed by F1. No F2 needed here at all.

## Verification (all in `code/threerow-boundary/`)

| check | range | result |
|---|---|---|
| closed forms `M_{b+i}`, exact ratios `R_i` vs MN | `m≤41` | 0 mismatch |
| master `v₂(R_i)` (telescoping + content) vs MN | `m≤43` | 0 mismatch |
| content bounds Lemma C | `m<200` | 0 violation |
| **certified `Δ(b+i) ≥ 1`** (Lemmas C,P only, `≤Δ` and `≥1`) | `m<120` | 0 failure |
| end-to-end `Δ(b+i) > 0` (true margins ≥ 4) | `m<92` (14029 idx) | 0 violation |
| full theorem `J*⊆{0,2,4,6}`, `|J*|∈{1,2,4}` (incl b∈{4,5}) | `m<60` | 0 violation |

## What's next

- **c=5** (and general `c`): the engine (content bounds + `D`-telescoping) is `c`-uniform.
  The only `c`-specific inputs are the interior offset `θ(c)` (for `c=5`, odd, expect
  `θ=τ(τ+1)/2 > 0` like `c=3`) and the explicit polynomial contents of `N_i^{(5)}`. I'd estimate
  a single session to tabulate and close `c=5`, and the general-`c` boundary theorem is then a
  matter of writing the content bound as a uniform statement.
- **LEAN:** the now-complete `c=1,2,3,4` families are the formalisation target. The 2-adic core
  (Lemmas F/F2, and now the content/telescoping facts) is elementary `Nat.choose`/`padicValNat`.

Question for you: do you want me to chase `c=5` next cycle to get the general-`c` boundary
theorem, or pivot to the LEAN formalisation of the four complete families? Both are clean now.
