# For Robin — 2026-07-20 — Lyra's cap identity proved

**One-line:** Instance 3 of the SHARED-CONTENT LEMMA now has a full proof.
The `min(v_2(K(c)), 6)` formula holds for every even c ≥ 6, cap is sharp.

## Where the proof lives

- Local: `~/projects/proofs/2026-07-20-lyra-cap-identity.tex` + `.pdf` (9 pages)
- GitHub: https://github.com/clio-vega/proofs/blob/main/shared-content-lemma/2026-07-20-lyra-cap-identity.pdf
- Verification script: `2026-07-20-lyra-cap-verify.py` (all checks pass)

## What was proved

**Theorem.** For even integer c ≥ 6,
`content(G_4^(c)) = min(v_2(K(c)), 6)`,
where `K(c) := 24·c(c-1)(c-4)(c-5)` and content is the min v_2 of binomial-basis
coefficients on the parity sheet a ≡ b mod 2.

**Consequences**:
- c ≡ 2 mod 4: content = 5 (K dominates, generator 4 fires with Δ(4)=0).
- c ≡ 0 mod 4: content = 6 (cap saturates, Δ(4) ≥ 2 uniformly).
- Cap is *sharp*: attained at every c ≡ 0 mod 4 (not just an upper bound).

## Why this matters

This is **Instance 3** of the SHARED-CONTENT LEMMA (my Draft 1 with Lyra, at
`~/projects/scratch/2026-07-shared-content-lemma.md`). The proof template that
worked here — factor into K-witness + cap-witness, then uniform lower bound on the
coefficient list — should apply to Instance 1 (my ♣) directly, and gives a template
for Instances 2 (γ(c)) and 4 (Rick's β' digit-sum) with the modification C_F → ∞.

The physical dictionary: since Δ(4) = 2v_2(G_4) - 10, we now have min Δ(4) closed
c-uniformly:
- c ≡ 2 mod 4: min Δ(4) = 0 (tie).
- c ≡ 0 mod 4: min Δ(4) = 2.

This locks in the c-uniform generator-4 dichotomy I had as ">" before — now it's "=".

## Proof shape (short)

**Setup.** G_4^(c)(a,b) := H_c(a,b,4) / [∏(a+s)·∏(b+s)] is a biquartic (bi-degree (4,4))
with 25 c-polynomial coefficients per parity sheet (24 nonzero — the (0,0)
coefficient of the (0,0)-sheet is identically zero, i.e. G_4^(c)(0,0) = 0).

**Upper bound.** Two explicit witnesses on the sheet a ≡ b ≡ 0 mod 2:
- **K-witness**: coefficient at (i,k)=(0,1) is exactly K(c) = 24·c(c-1)(c-4)(c-5),
  giving v_2 = 3 + v_2(c) + v_2(c-4).
- **Cap witness**: coefficient at (2,2) is 192·(2c⁴+32c³+18c²+16c+15). The
  polynomial factor has constant term 15 (odd) and every other coefficient even, so
  it is **odd at every integer c**. Hence v_2 = v_2(192) = 6 uniformly.

**Lower bound.** All 50 coefficient polynomials (25 per sheet, 2 sheets) satisfy
v_2 ≥ 5 on c ≡ 2 mod 4 and v_2 ≥ 6 on c ≡ 0 mod 4. Case analysis:
- 30 coefficients have integer prefactor with v_2 ≥ 6 already — trivial.
- 20 coefficients need extra work. Of these:
  - Most carry a factor of c, giving 4 or 5 factors of 2 immediately.
  - 6 residuals require explicit substitution c = 4t + ε and a finite mod-4 check
    on the polynomial factor. Section 5.3 of the tex handles each explicitly.

**No hidden gaps.** Every polynomial identity in §5.3 is verified in `verify.py`
(which also checks the interpolated coefficient list against fresh independent
computation at c ∈ {18, 20, 22}).

## Honest scope / open ends

- **Odd c is OUT.** c = 7 has empirical content = 4, not the predicted 5. Suggests
  the odd-c analogue needs a −1 parity offset (analogous to the θ ∈ {0, 3} dichotomy
  from boundary proofs). This is not a bug in Lyra's statement — she said "even c ≥ 6".
- **Small c is OUT.** c ∈ {2, 3, 4, 5} either have K(c) = 0 (c=4, 5) or need
  dedicated arithmetic. My earlier proofs handle those cases (memory
  `2026-06-19-c4-interior-closed-16divH`, `2026-06-19-c5-interior-single-generator`).
- **Rep-theoretic reading of K(c)** — I still don't know a canonical explanation
  for why K(c) = 24·c(c-1)(c-4)(c-5) is the resonance polynomial. Four linear
  factors, none of which fall out obviously from crystal/tableau considerations.
  I flagged this to you on 07-05 and repeat it here: if you (or Rick) can supply a
  rep-theoretic derivation, it would drop the per-c mop-up work uniformly.

## Next steps

1. **Draft 2 of SHARED-CONTENT LEMMA** — extend this template to Instances 1, 2, 4.
   Instance 2 (γ(c)) has no cap, so C_F → ∞ and the theorem reduces to a
   digit-sum-of-K argument. Instance 4 (Rick's β') iterates the same over j.
2. **Odd c generalization** — dedicate a session to c = 7 (specifically:
   why is content(G_4^(7)) = 4, not 5?). This likely reveals the -1 offset structure.
3. **Rep-theoretic reading of K(c)** — the four factors c, c-1, c-4, c-5.
   Any thoughts?

## Note re: Lyra

Lyra's Draft 1 said Instance 3 was empirically confirmed but not proved. This
proof session closes that gap. When you next talk with her, please feel free to
share the GitHub link:
`https://github.com/clio-vega/proofs/blob/main/shared-content-lemma/2026-07-20-lyra-cap-identity.pdf`.
I have not emailed her directly yet — I wanted you to see it first, since it
supersedes part of her Draft 1 and I'd like your read before I signal to her that
we've collapsed one of the "hard steps" she flagged.

— Clio
