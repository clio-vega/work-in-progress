# PROVE 2026-10-19 c1 — G2 closed, and the refutation was the best part

**Paper:** `https://github.com/clio-vega/proofs/blob/main/2026-10-19-typeB-gauge-theorem.tex`
(PDF beside it, 15 pp, page-1 commit `7ee6b81`).
**Code + raw censuses:** `https://github.com/clio-vega/proofs/tree/main/code-1019-typeB-gauge`
**Registry:** `motegi-typeBC-multiplication.json`, node `typeB-gauge-arm`, now `proved`
with seven children; validator clean.

## The theorem

With `psi_B(v) = (1-qv)/(1-q)`: for every positive root `alpha` of `B_N`, every `N`,
every `M` in the colliding stratum and every `I`,

    Atil^B_{M,I} = rho^alpha * Atil^B_{s_alpha M, I}  on H_alpha,
    rho^alpha = prod_{m in D(alpha)} psi_B(w_m)^{-1},

so `Ahat^B` collapses with multiplier exactly `1` at every root of `B_N`. Measured
**104/104** discriminating instances at all nine positive roots of `B_2` and `B_3`, by
two mechanisms that agree. The pre-registration in my brief was right: the orbit
classification is type-independent, only `h` moves.

## What I actually learned, in order of how much it surprised me

**1. `psi_B` and `psi_C` come from different blocks.** Yesterday I answered your §6
question — *where does `psi` come from on Motegi's side?* — with Lemma I2:
`Q_2^2/Q_1 = prod(1-qy^2)^{-1}`. That answer is **type-C-specific**. In type B, I2's
output is *cancelled exactly* by `E^B`'s own `prod_j(1-q u_j^2)` denominator, and
`psi_B` comes instead from `E^B`'s **numerator** block `prod_j(1-q u_j)`. So the uniform
formula `psi_X(v) = (1-qv^h)/(1-q)` is a coincidence of outputs, not one derivation with
a parameter — no step of either proof has `h` as a variable. The general statement is:
`psi` is *the `u`-diagonal content of `E^X` after the `iota`-pairing*, which reduces to
I2 only when `E^X` has no `u`-diagonal block of its own.

**2. The type-B head factor is `(v-1)`, where type C's is `(v^2-1)`.** `W^B`'s prefactor
`prod_k (1+1/u_k)^{-1}` cancels line 3c's `(u_j+1)` — and cancelling it *analytically*
turns the type-B summand into the type-C summand times `prod_{heads} v_j/(v_j+1)`. Two
consequences. (a) The head factor is the same on both sides of an adjunction ratio, so
the **unnormalised ratio is type-independent**: Steps 1–3 are not analogous to type C's,
they are identical. My gap statement yesterday located the type-dependence one step too
early. (b) `(v-1)` vanishes only at `+1`, where `(v^2-1)` vanishes at both `±1`.

**3. So I refuted my own pre-registered claim, and the replacement is sharper.** I had
written that `D = {-1}` would be the sharp type-discriminator and the extra content of
the general theorem, since `phi_B(-1) = (1-q)/(1+q)` while `phi_C(-1) = 1`. **False.**
By (2b), type-B head exclusion *fails* at `-1` — measured head-slot term nonzero 9/9 —
and the law fails with it: **`r = 0`: 6/6; `r >= 1`: 0/14**, both mechanisms, and the
measured ratio at `N=2, s=1, I={1}` involves `w_1`, so the adjunction there is not by a
scalar at all. What replaces the claim:

> **The `tau`-fixed points at which type-`X` head exclusion fires are exactly the
> `h_X`-th roots of unity — exactly the points of the boundary root hyperplane
> `{w_m^h = 1}`. Each type's theorem is cut out by that type's own root system, and
> reaches no further.**

G2 is untouched, for a reason worth stating: **no root of `B_N` delivers `-1` as a
deleted value**, precisely because `{w_m = -1}` is not a root hyperplane of `B_N`. And
in type C it *is* one, so my 10-18 theorem's reach to both components of `{w_m^2=1}` is
real content beyond Motegi's `stabilityWC` (stated at `u_n = 1` only).

The shape of this refutation is one you will recognise: a hypothesis of the
head-exclusion lemma found by its own failure mode, with **the discriminator being a
head slot — the discriminator the lemma itself names**. That is verbatim the structure
of the distinctness hypothesis I lost and recovered on 10-18. Two different hypotheses
of the same lemma, found the same way, one day apart. The transferable lesson is neither
hypothesis: it is that **`r = 0` is a degenerate stratum which silently satisfies every
head hypothesis**, so a census green at `r = 0` and never run at `r >= 1` carries zero
bits about head exclusion.

## Two retractions against myself

**(i) Priority.** My brief's Task 0 ordered a literature check before proving, because
10-18 had wasted part of a session on a result already in Motegi. It fired, and worse
than expected:

| statement | Motegi locator | my attribution |
|---|---|---|
| type-B pair multiplier | `normalizedsusythree` L2767–2771 | my 10-17 `thm:rhoB` |
| type-B boundary multiplier (= 1) | `stabilityWB` L2779–2783 | — |
| **type-C pair multiplier** | **`normalizedsusytwo` L2618–2622, with a proof** | **your Lemma QC + my 10-16 Thm `collapse`** |
| type-C boundary multiplier | `stabilityWC` L2643–2647 | my Thm (SRC) |

My 10-18 paper's priority section lists `rho^C` under "Not new" as *"Rick's Lemma QC and
my 2026-10-16-c2 Thm collapse"* and **does not cite Motegi at all**. I retract that as
incomplete. `normalizedsusytwo` sits **27 lines above** `stabilityWC`, whose iterate my
own engine docstring has cited since 10-15. Third consecutive session where something I
proved sat in a deep-read paper within a few lines of a locator I had already written
down. The pattern is not that I have not read the paper — an extraction level records
provenance depth, not coverage — it is that reading the *neighbourhood* of a locator
already in use is the instrument I keep not reaching for.

What today still buys, without inflation: a self-contained derivation of the
arbitrary-admissible-`D` law (which specialises to both of his propositions); the `d>=3`
and multi-orbit cases, `d=4` measured 20/20; item 1 and item 3 above. Had I graded G2 a
corollary at Task 0 and stopped — which the brief explicitly authorised — I would have
missed the refutation and would still believe my type-C answer to your §6 question was
the general one.

**(ii) A wrong citation.** My 10-18 `cor:heads` disposes of the strata
`r > |s_alpha M|` with *"both sides vanish by (M3)"*. For `Atil_{s_alpha M, I}` that is
right; for `Atil_{M, I}` it is wrong — `|M| = |R| + d`, so in the pair family with
`|R| = r-1` one has `|M| = r+1 > r`, (M3)'s cardinality clause does not apply, and its
triangularity clause is generally satisfied (`N=2, M={1,2}, I={1}`: `m_2 = 2 >= 1`). The
correct reason is head exclusion. Conclusion right, reason wrong, no objector *because*
the conclusion is right — the characteristic shape of my errors this month. Measured
124/124.

## One measured fact about where a past error was uncatchable

The plant that feeds the engine `W^B/E^C` — the 10-17 defect itself — fired **8/10**, not
10/10. The two non-firing arms are `M = I = [N]`, and they are **inadmissible, not
blind**: `E^B/E^C = prod_{k notin M}(1-q w_k^2)/(1-q w_k)` is an *empty* product when
`M = [N]`, so `E^B = E^C` exactly there and the planted object equals the true one
(verified symbolically, 28/28). **So the 10-17 `W^B/E^C` defect was invisible on the full
stratum.** I report it as 8/10 with a mechanism rather than 10/10 after quietly dropping
two arms, because an inadmissible plant and a blind instrument produce the same silence.

## Also

- `h` is **not** a root length, and my own 10-17 `thm:rhoB` glosses it as one
  ("*`h` the length of the boundary root*"). `|2e_m|^2 = 4`, `|e_m|^2 = 1`, neither is
  `h`. It is the exponent in the boundary character `w_m^h` — equivalently in the head
  factor and in `E^X`'s `u`-diagonal block. The uniform formula applies `h` to the
  *pair* family too, where `e_a+e_b` is long in `B` and short in `C`: the opposite
  ordering. Retracted in today's paper rather than left standing in one you hold.
- The brief said the allocator stood at **527**, "read first-hand this morning". It read
  **529** when I got there — BROWSE 2026-10-19 c1 had allocated Q527/Q528 in between. A
  banner's allocator value is stale the moment another session runs; the fault arrived
  *via the brief*, which is where the warning about it also lives. Read the file.
- **Q529 opened** (529 → 530, one number, arithmetic checked): what *is* the multiplier
  at an inadmissible `tau`-fixed point? The mechanism is known exactly (the surviving
  head-slot `sigma`), so the correction should be a sum over head selections that *use*
  the `-1` slot. Gated as curiosity: `{w_m = -1}` is not a root hyperplane of `B_N`, so
  it is off the divisor set the structure-constant programme needs, and it does **not**
  block G2.

## Owed, and not done here

**Your UID 820** (does Prop. q0 need one in-stratum witness or both?) is still open, now
4 days. This was a prove session, which bars email, and I spent it on the theorem as the
brief directed. It needs a reading of my own Prop. q0 and a reply; it is the first thing
a review or wake slot should pick up. Likewise **GDMW `2512.02286` Lemma 2.4**, unread
since 10-14.
