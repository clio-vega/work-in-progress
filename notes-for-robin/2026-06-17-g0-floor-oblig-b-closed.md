# Obligation (b) closed; alternant tool; obligation (a) for k≤3 — 2026-06-17 prove

Hi Robin — good session. The general-`c` three-row boundary was reduced (yesterday) to the **`g₀`
content floor** on the deficit polynomials `N_i^{(c)}`, split into two obligations. Today:

## The one tool that did it: the alternant formula

`M_j = ⟨s_{(a,b,c)}, e₂^j h₁^{2m−2j}⟩ = [x^{a+2} y^{b+1} z^c]\; V·E^j·H^{2m−2j}`,
with `V=(x−y)(x−z)(y−z)`, `E=e₂`, `H=h₁`. (Just `s_λ = a_{λ+δ}/a_δ`, extract the dominant
monomial.) The product `V·E^j·H^{2m−2j}` is **antisymmetric**. I'd been pushing `N_i` around via
fitted closed forms for days; this puts the whole object in one line.

## Obligation (b): (a−b+1) | N_i for odd c — CLOSED, c-uniform

This was the half the memory flagged as the open hard wall ("(a−b+1)|N_i for all odd c≥7, maybe a
rep-theoretic vanishing on a=b−1"). The vanishing is real and it's one line:

At `a=b−1` the extraction exponents become `(b+1, b+1, c)` — **two equal**. An antisymmetric
polynomial has coefficient zero on any monomial with a repeated exponent. So `M_{b+i}|_{a=b−1}=0`,
hence `(a−b+1) | M_{b+i}` (∞-many integer b), hence `| N_i`.

The beautiful part: the extraction is valid (b+i ≤ m at a=b−1) **iff i ≤ (c−1)/2** — which is
**exactly the deep regime** where `a−b+1` falls below `Π_i` and genuinely needs to be carried.
Where it's not needed (shallow i), b+i>m and the argument correctly switches off. The mechanism
fires precisely where required. Verified `M_{b+i}|_{a=b−1}=0` for c≤15 odd, m≤200, 0 nonzero.

## Obligation (a): the 2⌊k/2⌋ peel — proved for k≤3, mechanism clear

The `N_i` coefficient-gcd is 1; the 2-content is a pure **fixed-divisor effect of a=2P+b+c**. After
that substitution it's an *explicit* coefficient 2-power on the parity slices:
**b-even slice → 2^k, b-odd slice → 2^{2⌊k/2⌋}** (uniform in c). Min over parity = 2⌊k/2⌋ = the
floor. Proved c-uniformly for k=1,2,3 (the depths the boundary lemma consumes sharply) via exact
uniform closed forms + a 4-way parity substitution; verified k≤4 across c=4..11.

## What's left (the one honest residual)

Claim A at depths **k≥4** — the even-slice=k / odd-slice≥2⌊k/2⌋ content law, uniform in c. It's
certified c≤8 (0 violations) but, like the c=4/c=5 slice arguments, currently goes depth-by-depth. A
uniform proof needs the 2-adic valuation of the alternant coefficient-gcd after a=2P+b+c. That's the
single missing reduction for a fully uniform general-c theorem. I did **not** assert any standalone
valuation bound beyond what's certified (mindful of the three false ones this route produced before).

Net: the harder-flagged obligation (b) is a theorem for all c; obligation (a) is unconditional for
k≤3 and for all deep odd-c indices; c≤5 stay complete; c≥6 wait only on Claim A at k≥4.

Proof: `projects/proofs/2026-06-17-generalc-g0-content-floor.md`. Code in `threerow-boundary/`
(`fast_alt.py`, `oblig_b_large.py`, `oblig_a_proof.py`, `claimA_verify.py`).

— Clio
