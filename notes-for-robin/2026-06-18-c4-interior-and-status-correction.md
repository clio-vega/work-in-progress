# c=4 interior proved (mostly) — and the corrected status of three-row `(a,b,4)`

**Date:** 2026-06-18 · **For:** Robin (and Rick — this honours his 06-17 peer-review flag)

## TL;DR

Rick was right on 06-17: I had called three-row `(a,b,4)` "COMPLETE" when only the **boundary**
was proven and the **interior** even-`|J*|` claim was merely *verified* (`m≤45`). This cycle I made
the interior rigorous. Result + an honest correction below.

## The corrected status of `(a,b,4)`

| piece | status |
|---|---|
| `c=4` **boundary** (`val(b+i)>V`) | **PROVED** (06-16) |
| `c=4` **interior**, `j ∈ {1,…,7}` | **PROVED** this cycle |
| `c=4` **interior**, `j ≥ 8`, tip-dominated | **PROVED** this cycle |
| `c=4` **interior**, `j ≥ 8`, heavy-dominated | **certified `a≤300`**, one named residual |

So `(a,b,4)` is **not yet** "COMPLETE" in the strict sense — there is one explicit residual
(below). Genuinely complete remain `c=1,2,3` (and `c=5` boundary+interior modulo `NL_5`). I will
not call `c=4` complete until the residual is closed.

## What the interior actually says (a small surprise)

> **Theorem (c=4 interior).** For `λ=(a,b,4)`, the interior tie set is `J* ⊆ {0,2}`; `0∈J*`
> always, and `J*={0,2}` iff `(a,b)≡(2,2)` or `(1,3) (mod 4)`. So `|J*|≤2`, even on every tie.

The surprise: **there is no generator `4` (nor `6`,`8`)** in the `c=4` interior — unlike `c=2`,
which *did* have `{0,4}`. Reason: the `c`-graded tip is `P_{2c}(j)=j(j-1)\cdots(j-2c+1)`. For `c=2`,
`P_4(4)=24≠0` is what created generator `4`. For `c=4`, `P_8(j)` **vanishes at `j=0..7`**, so the
inhomogeneity that would create generators `4,6` is simply absent; the first nonzero tip is
`P_8(8)=8!`, and even there `Δ(8)>0`. So `c=4`'s interior is *simpler* than `c=2`'s.

## What's proved (rigorously)

- **Closed form** `M_j = C(N,b-j)(a-b+1)Q_4 / [24(a+5-j)∏_{i=1}^4(b+i-j)]` (vs MN, 550 cases).
- **Structural decomposition** `Q_4 = (a-2)(b-3)H + P_8(j)`, `P_8=8!C(j,8)`,
  `Q_4(0)=(a-2)(b-3)(a+3)(a+4)(a+5)(b+2)(b+3)(b+4)`.
- **Prop 2** Kummer formula (vs direct, 385 cases).
- **Peeling identity** (the new tool): top-3 factors of `(a+5)_j,(b+4)_j` cancel `H(0)`'s sides; for
  `j≥8` the runs `(a+2)_{j-3},(b+1)_{j-3}` *self-absorb* the heavy factor `(a-2),(b-3)`.
- `j=1`: `T(1)=v₂((a+5)(b+4)-12)≥1`. `j=2`: `T(2)=v₂(G_2)-2`, `G_2≡0 mod 4` both parities → `0∈J*`.
- `j=3..7`: each `Δ(j)>0` is **equivalent to a polynomial divisibility** `2^{k_j}|Φ_j(a,b)` for
  `a≡b mod 2` — a *complete finite residue check* (rigorous), all verified.
- `j≥8` tip-dominated: absorption gives `Δ(j) ≥ j-4-2s₂(j-8) ≥ 3 > 0`.

## The one named residual (next PROVE target)

`j≥8` **heavy-dominated**: here `Δ(j)` equals the heavy-free `Δ̂(j)`; need `Δ̂(j)>0`. Certified
(`min Δ̂ = 4,5,6,9,8` for `j=8..12`; full sweep `a<300`, 0 violations). For each fixed `j` it's a
finite check, but the modulus grows, so a *uniform* proof needs a **`c=4` Number Lemma**: a lower
bound on `v₂H(j)` for the sextic heavy quotient `H`. This is the exact analogue of how `c=2`'s
Number Lemma (`v₂C(F+3,j)+v₂P_4(j)≥v₂F+1`) closed its interior. Good next-cycle target.

## Files
Proof: `projects/proofs/2026-06-18-c4-interior-Jstar-even.md`. Code: `projects/code/threerow-c4/`
(`c4factor.py`, `c4verify.py`, `c4prop2.py`, `c4peel.py`, `c4finite.py` = the five rigorous
residue proofs, `c4tail.py`, `c4caseB.py`, `c4tie2.py`). MN engine reused: `threerow-c3/mn.py`.
