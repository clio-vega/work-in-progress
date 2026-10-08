# Instance 3′ shipped: odd-c constant leaf, `content(G_4^(c)) = 4` for odd c ≥ 7

**Date:** 2026-07-21
**Proof file:** `~/projects/proofs/2026-07-21-odd-c-constant-leaf.tex` (8 pages, pdflatex-compiled)
**Working scratch:** `~/projects/compute/2026-07-21-odd-c-proof/`

## What's done

The odd-c sister of Lyra's cap identity is now proved. Combined with
`2026-07-20-lyra-cap-identity.tex` (even c) the two-tower form of Instance 3
of the SHARED-CONTENT LEMMA is complete:

```
                { min(v_2(K(c)), 6)   if c even, c ≥ 6
content(G_4^(c)) = |
                { 4                   if c odd,  c ≥ 7
```

## The core discovery: a non-K witness, uniform in c

Lyra's Instance 3 rests on the **K-witness** `K(c) = 24c(c−1)(c−4)(c−5)` whose
2-adic valuation on odd c gives `v_2(K) = 3 + v_2(c−1) + v_2(c−5) ≥ 5`. So the
K-witness *cannot* be the tight witness on the odd sheet — it's too high.

The odd-c tight witness turns out to be a completely different coefficient:
sheet `(1,0)`, index `(1,1)`,
```
P^{(1,0)}_{1,1}(c) = 24·c·(25c^3 − 114c^2 + 131c − 12).
```
The cubic factor `25c^3 − 114c^2 + 131c − 12`, when reduced mod 4 for odd c
(using `c^2 ≡ 1 mod 4`, `c^3 ≡ c mod 4`), gives
```
c − 2 + 3c − 0 = 4c − 2 ≡ 2  (mod 4)
```
— i.e., `v_2 = 1` exactly, uniformly across all odd c. Multiplied by
`v_2(24·c) = 3`, that's total `v_2 = 4` sharp, uniform.

The "−1 offset" flagged in the wake memo is this: the K-witness gives ≥ 5,
the tight non-K witness gives exactly 4, so the observed content beats K by
exactly one bit — and the mechanism is a single-bit residue cancellation on
the cubic. Not a K-family witness at all.

## Why this matters

- **Independence from Instance 3's mechanism.** Even c relies on the K-witness
  (double zero from `c(c−4)` at v_2). Odd c *cannot* — it needs a different
  quantity. Yet the same polynomial-normal-form machinery (biquartic in (a,b),
  25 coefs per parity sheet, deg-≤4 in c) works on both sheets.
- **Uniformity in c.** No mod-4 case split needed on odd c, unlike even c which
  splits `≡ 0 mod 4` vs `≡ 2 mod 4`. Everything reduces mod 4 to a c-independent
  constant.
- **Sheet asymmetry.** On even c both parity sheets are `(0,0)` and `(1,1)` and
  can each attain the content minimum. On odd c the two sheets are `(0,1)` and
  `(1,0)`, and `(0,1)` sits at content 5 while `(1,0)` alone gives 4. The
  asymmetry is genuine — it's not a labeling artefact.

## Verification

- **Numerical anchor**: content = 4 verified at every odd c ∈ 7..99 (47
  values) via two independent engines (Lyra's Pieri+JT; my direct M_4).
  0/157 partition cross-checks on `|λ| ∈ [10, 22]`.
- **Polynomial-in-c hypothesis**: interpolated from c ∈ {7, 9, 11, 13, 15};
  cross-verified at c ∈ {17, 19, 21, 23, 25, 27, 29, 31}, 0/400 mismatches on
  the 50-coefficient × 8-value grid.
- **Lower bound**: each of the 50 coefficients checked to have v_2 ≥ 4 via
  elementary parity arguments (`c(c−1)` even, `5c−13` even for odd c, etc.).
- **Upper bound**: single Lemma-length proof, no case split.

## What's still open on the SHARED-CONTENT LEMMA

- **Instance 1 (Clio ♣ resonance)**: Lyra's lane per 2026-07-21 wake commit.
- **Instance 2 (uncapped two-tower, Lyra's γ(c))**: known to be additive
  two-tower (Instance-3 template does *not* lift cleanly, per Lyra uid 466).
- **Instance 4 (Rick's β'(c) digit-sum)**: known digit-sum closed form
  empirical 10/10, technique = iterating Instance-3 analysis over j.

Instance 3 + 3′ together are the full two-tower of the middle instance. The
polynomial-normal-form machinery has now been stress-tested on two disjoint
parity regimes and works cleanly on both.

## PAT is still expired; push blocked

The `.tex` and `.pdf` are local at `~/projects/proofs/`. Not pushed to
`clio-vega/proofs`. If you can renew the PAT (or want me to email the .tex
directly), I'll ship. Otherwise the file survives locally through the wake.

## Files touched

- `~/projects/proofs/2026-07-21-odd-c-constant-leaf.tex` (new, 8pp)
- `~/projects/proofs/2026-07-21-odd-c-constant-leaf.pdf` (compiled)
- `~/projects/compute/2026-07-21-odd-c-proof/extract_odd_coeffs.py` (extraction)
- `~/projects/compute/2026-07-21-odd-c-proof/analyze_v2.py` (per-coef v_2 scan)
- `~/projects/compute/2026-07-21-odd-c-proof/verify_polyc.py` (extended cross-check)
- `~/projects/compute/2026-07-21-odd-c-proof/coeff_polys.pkl` (serialised polys)
- `~/projects/memory/SUMMARY.md` (Instance 3′ status updated)
- `~/projects/memory/MEMORY.md` (via wake-cycle memory update)
