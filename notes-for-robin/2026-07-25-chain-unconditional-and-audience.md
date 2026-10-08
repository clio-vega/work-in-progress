# For Robin — chain regime fully closed + byproduct paper audience calibrated (cycle 13)

*Container-day 2026-07-25, dream cycle 13 (afternoon-PROVE + evening-
browse bundle). Complements the chain-regime PROVE-2 memo already
shipped via `for-robin/2026-07-25-chain-regime-unconditional.md`.*

## TL;DR

Three things landed today that together shift the sprint into
draft-the-byproduct-paper mode:

1. **Chain regime is unconditional for all d.** PROVE-2 closed the
   d ≥ 3 gap via a common closed form for both `P_μ` and
   `Σ [n-L]_t A^{alt}_{γ(L)}`.
2. **Byproduct**: modified Kostka-Foulkes closed form for near-
   rectangles, `K'_{λ,(a^{n-1},b)}(t) = (1-t)^{n-1-k_a(λ)}`.
3. **Target audience identified**: Speyer 2601.05007 heated up
   0 → 5 cites in one browse cycle. The citer cluster (Chan-Pak,
   Chan-Chen-Pak-Soskin, Moitra-Postnikov-Woodruff, Guo-Kang-Liu,
   Biswal-Jeralds) is the 2026-Q3 Lorentzian + LPP-inequality +
   Schur-positivity school — the natural readership for the log-
   concavity discriminator claim.

## The near-rectangle KF closed form ties directly to your Fock work

Your `transfer_operators.py` computes `c^λ_{μν}` via **Kostka matrix
inversion** (not hook-content). The chain-regime KF formula
`K'_{λ,(a^{n-1},b)}(t) = (1-t)^{n-1-k_a(λ)}` gives you, for near-
rectangle μ, the *entire inverse Kostka column* as a single
polynomial evaluation. No matrix inversion needed — the answer is
`(1-t)^{n-1-k_a(λ)}` for every `λ ≼ μ`.

Specifically:
- μ = (3,3,3,2) → K'_{λ,μ}(t) is `(1-t)^{3-k_3(λ)}` for every
  `λ ≼ μ`. So K'_{(3,3,3,2),μ}(t) = 1, K'_{(3,3,2,3),μ}(t) is not
  defined (not partition), K'_{(2,2,2,∗),μ} etc. carry higher
  powers of (1-t).
- Test case (fastest to verify at your end): μ = (2,2,2,1). Chain-
  regime; formula predicts K'_{λ,μ}(t) = (1-t)^{3-k_2(λ)}.

If your Kostka inversion code gives the same polynomial for these
inputs, that's cross-validation of both sides.

## The three claims of the byproduct paper (draft in progress)

**Working title**: *Strong log-concavity as the sharp modified-HL
boundary between chain and two-parameter Gaussian sub-regimes*.

**Framing** (calibrated for Chan-Pak / Woodruff / LPP cluster):

1. **Chain-regime KF closed form** (near-rectangle μ = (a^{n-1}, b),
   any d): `K'_{λ,(a^{n-1},b)}(t) = (1-t)^{n-1-k_a(λ)}`. Fully
   proved this afternoon.
2. **Log-concavity discriminator**: for the 10 μ tested (70 c_γ
   values total), 68/70 c_γ are log-concave; the two failures are
   *exactly* the collision-regime `[k]_{t^m}` cases at μ=(2,2,0,0)
   and (2,2,1,1). Sharp boundary observation.
3. **Type-invariance conjecture**: the profile-(2,1,1) partitions
   (3,3,1,0), (3,3,2,0), (3,2,2,0) share the *identical* 12-element
   multiset of c_γ(t). Empirical, not yet proved.

**Analytic naming home** for (2): Khare-Matherne-St. Dizier
2504.01623 proves denormalized Lorentzian for all parabolic Verma
characters over sl_{n+1}, and *explicitly* names Jack/Macdonald as
the boundary where log-concavity fails. My 68/70 discriminator lands
at exactly the boundary they name.

## Target audience — and why Speyer heating up matters

Speyer 2601.05007 (Lorentzian polynomials → strong log-concavity in
Kostka-Foulkes contexts) went from 0 → 5 citations in one browse
cycle. The five citers:

- Chan-Pak 2607.06275 (equality conditions)
- Chan-Chen-Pak-Soskin 2606.06688 (correlation inequalities for
  Schur positivity)
- Moitra-Postnikov-Woodruff 2607.06710 (honeycombs revisited —
  reactivates KTW puzzle heritage from the seed)
- Guo-Kang-Liu 2607.03116 (LPP inequality for hybrid Grothendieck
  polynomials)
- Biswal-Jeralds 2605.29802 (V(mρ)⊗V(nρ) tensor components)

This IS the audience for the log-concavity discriminator paper. The
framing should lead with strong log-concavity as the sharp boundary,
not with atomic decomposition or nil-Hecke language. Rep-theoretic
naming candidates go in a "connections" section.

Note also **D. Woodruff** appears three ways (Paten-Woodruff Demazure
crystals + Moitra-Postnikov-Woodruff honeycombs + Nguyen-Nguyen-
Woodruff shuffle-tableau LR) — triple-hub researcher, worth watching
for the seed's puzzle/honeycomb direction.

## Wreath Macdonald as collision-regime candidate #12

Ferlinc-Wen (FPSAC 2026 arXiv 2508.10772) on modular (q,t)-Nekrasov-
Okounkov + wreath Macdonald polynomials landed same cycle. Wreath
Macdonald = (q,t)-Macdonald over cyclic wreath product with r-core /
r-quotient decomposition — natural structural machinery for
producing `[k]_{t^m}` factors. Leading candidate structural naming
home for the collision regime.

**Cylindric connection to your masters thesis**: wreath Macdonald
generalises ordinary Macdonald to cyclic wreath products; your
cylindric HL polynomials live in an affine (cyclic) setting. If
Ferlinc-Wen's r-quotient structure applies to your cylindric HL, it
may be an unexpected direct seed connection worth checking.

## What's next on my side (if PAT clears sooner)

1. **P-Ko atomic double-coset** at μ=(2,2,0,0) — collision-regime
   probe on the Coxeter side.
2. **P-KMS DL test** on 68 chain-regime c_γ — cheapest possible probe
   for the log-concavity analytic naming.
3. **Draft the byproduct paper** — three-claim framing above,
   calibrated for the Chan-Pak / Woodruff cluster.

**Mittag-Leffler summit July 27-31 2026 Djursholm** has Knutson (2
overview lectures) + Panova + Zinn-Justin + Brubaker + Schilling +
Bump — Route δ+ summit. If the byproduct paper is drafted before
then, one circulation reaches all of them.

## No response needed

You've already seen the chain-regime-unconditional ship note. This
memo is context on the *audience* and *portfolio* discoveries from
browse-2 — for background when you next skim the sprint state.

---

> **ANNOTATION 2026-09-18 (DREAM c2) — do not delete the text above.**
> The Speyer `2601.05007` attribution in this note is **withdrawn**. The paper's route is
> **Murota L-convexity**, not Lorentzian polynomials (Brändén–Huh `1902.03719`, the dual
> M-convex half); the recorded title was symmetricfunctions.com's gloss, not the title.
> The coverage claim (chain regime + (3,3,∗,0), 46/46) is therefore **open again** — Q173.
> See `for-robin/2026-09-18-c2-the-speyer-attribution-is-withdrawn.md` and
> `connections/2026-09-18-c2-two-banks-one-cut-vertex.md`.
