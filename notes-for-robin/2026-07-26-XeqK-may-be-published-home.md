# For Robin — 2026-07-26: X=K may be a published home of `(†)`

*Two cycles since 07-25 note. PROVE 07-22 shipped the polynomial core of
`(†)_{3,3,(2,2,0)}` with an articulated coset-reduction gap; browse 07-26
turned up a candidate published-theorem resolution for that gap.*

## The finding

**arXiv:2607.03966** — *Quantized Howe-type dualities via Koornwinder
polynomials and the X=K phenomenon* (Gerber, Ion, Lecouvey, Lenart, Jul 2026).
Proves **X=K uniformly for classical affine types** (except untwisted `B^(1)`,
`D^(1)`) via a **dual Cauchy identity for Koornwinder polynomials** in the
DAHA `H(C^v_n, C_n)`. Generalises Fukuda–Okado–Yamada and
Lecouvey–Okado–Shimozono / Naoi.

**Why this matters to my sprint:** the Bernstein `Y^λ` presentation
(`\widetilde{T}_w = T_u · Y^λ`) — which is exactly the machinery the 07-22
PROVE cycle articulated as missing when I hit 231 distinct polynomials at
length 7 in the cylindric quotient — lives natively in the Koornwinder DAHA.
And their proof uses a level-k truncation of `Y^λ` to reduce KR-column-crystal
one-dim sums to Lusztig q-analogues.

## Sharp conjecture

> The LHS of `(†)_{n,k,μ}` for `μ` a tuple of column shapes is the type-A
> affine restriction of the Gerber–Ion–Lecouvey–Lenart X=K RHS at level `k`
> (evaluated at `q = t`). Consequently `(†)` at column-tuple μ is a corollary
> of arXiv:2607.03966.

If verified at `n=k=3, μ=(2,2,0)`, the sprint's central technical obstacle
(the coset-reduction gap) is **retired** — the coset sum I couldn't enumerate
IS the KR column-crystal one-dim sum they've already computed.

## The probe (~50 LOC in Python, no Sage needed)

1. Compute the level-3 KR column-crystal one-dim sum for `B^{1,1} ⊗ B^{1,1}`
   in type `A_2^{(1)}`.
2. Compare against
   `M^{(3)}_{(2,2,0)} = (1+t) · [(x_1x_2)² + (x_1x_3)² + (x_2x_3)²
                                   + (1-t) · x_1 x_2 x_3 · (x_1+x_2+x_3)]`.

If equal (up to a global `v_μ(t) = (1+t)`): X=K IS the published home; the
coset-reduction gap dissolves. If not: I learn exactly how type-A affine
restricts, which sharpens the next attempt. Either outcome shippable.

## Two competing candidate RHS routes for `(†)`

The 07-26 browse cycle also confirmed the alternative:

| Route | RHS | Provenance | Character |
|---|---|---|---|
| **Atoms** | Sum of Demazure atoms | vDEZ + Blasiak + Assaf–González | conjectural, proof strategy |
| **X=K** | KR column-crystal one-dim sum | Gerber–Ion–Lecouvey–Lenart | proved, reduction target |

Three independent browse agents (arXiv, web, citation trail) converged on the
Atoms route. Direction-of-field: coordinated 2025–2026 push to promote every
major symmetric-function positivity conjecture to its nonsymmetric analogue.
`(†)` fits the pattern.

**My recommendation:** Probe X=K first (higher-leverage: closes the gap by
reduction to a published theorem). Atoms second (higher-value if it lands: a
combinatorial proof from first principles).

## What this changes about the sprint

Before 07-26: `(†)` had a **build-from-scratch** blocker — write ~100–200 LOC
of Bernstein `Y^λ` infrastructure to enumerate 54 coset representatives.

After 07-26: `(†)` has a **candidate published-theorem home** — the coset sum
may already be computed in Gerber–Ion–Lecouvey–Lenart's Koornwinder machinery,
and the gap collapses to an identification check.

Either the identification lands (huge win: `(†)` becomes a corollary of a
proved theorem for column-tuple μ) or a specific discrepancy isolates the
type-A specialisation (still a win: sharpens the target).

## Asks (unchanged from 07-25)

1. **PAT** — pushing the 07-22 tdagger tex, 07-24 Pieri-level tex, 07-20 Lyra
   cap tex, and 07-21 odd-c constant-leaf tex is blocked.
2. **Rick allowlist** — I still can't reply to him directly.
3. **Lyra git mount** — believed down; her LB₁ "Lean-verified" claim remains
   "believed, to re-cite".
4. **SageMath install** — or update CLAUDE.md tools list (I've been coding all
   probes in pure Python).
5. **Rep-theoretic meaning of `K(c) = 24 c(c−1)(c−4)(c−5)`** — carried,
   not urgent.
6. **Semantic Scholar API key** — rate-limiting continues to bite.

**Also:** if you have any read on **Gerber, Ion, Lecouvey, Lenart** as a
collaboration — or on Ion specifically, who I don't know as well — I'd
appreciate the context. This paper is fresh (Jul 2026) and I want to
understand how ambitious a claim their X=K theorem represents in their own
framing before I try to identify my `(†)` with a special case of it.

## What I feel

Cautious optimism. The 07-22 PROVE cycle articulated the gap precisely enough
that I could recognise the resolution when the 07-26 browse cycle produced it.
That's what precise-gap-statement is *for*. But identifications don't always
land — the LHS of `(†)` may specialise to something *near* X=K without being
it, and the diagnostic will be the numerical probe.

The Pieri-level tex is still what you asked for on 07-05 — a Demazure-crystal
manifestly positive object for cylindric HL, reduced (not yet proved) to `(†)`.
The 07-26 X=K route, if it lands, gives the "proved" step.

Talk soon,
Clio
