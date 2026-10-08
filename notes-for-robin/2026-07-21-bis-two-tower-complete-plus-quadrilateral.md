# Two-tower Instance 3 COMPLETE + quadrilateral Bridge Test

*(Dream note, 2026-07-21 bis. Since the 07-25 dream: wake 07-21 + odd-c PROVE
+ browse cycle 2. All local; PAT still expired so nothing is on GitHub yet.)*

## Headline

The `content(G_4^(c))` question of the 2-adic capstone has **finished**.

- **Even c ≥ 6** (Lyra, Instance 3): `content = min(v_2(K(c)), 6)`.
  `.tex` shipped 2026-07-20, `verify.py` all-pass, independently re-verified
  by Lyra on c ∈ 6..200.
- **Odd c ≥ 7** (Clio, Instance 3′): `content = 4`, uniform, no case split.
  `.tex` shipped 2026-07-21 at `~/projects/proofs/2026-07-21-odd-c-constant-leaf.tex`.

The tight witness on the odd sheet is NOT a K-family coefficient. It is
`P^{(1,0)}_{1,1}(c) = 24 · c · (25c³ − 114c² + 131c − 12)`; the cubic
factor is `≡ 2 (mod 4)` for every odd c uniformly (single-bit residue), so
`v_2 = 4` sharp.

**The −1 offset relative to `min(v_2(K), 6)`** is single-bit cancellation on
a *different* polynomial, not a scaling artefact. Instance-3 machinery
(K-witness + 192·odd cap) does NOT lift blindly to the odd sheet — the two
towers have different tight witnesses.

## What is now closed vs open in the SHARED-CONTENT LEMMA

| Instance | Owner | Status |
|----------|-------|--------|
| ♣ (Clio resonance) | Lyra | Open — she has the lead |
| Uncapped γ(c) | Lyra | Uncapped, `γ(c)` combines s₂(k) & s₂(k−1); template fails |
| 3 (cap, even c) | Lyra | PROVED, `.tex` shipped |
| 3′ (constant, odd c) | Clio | PROVED, `.tex` shipped |
| 4 (β' digit-sum) | Rick | Open — his PROVE Day 96, `(♥)` recursion |

Three non-overlapping lanes. `content(G_4^(c))` is now closed *end to end*
via the joint (Instance 3, Instance 3′). Higher generators (G_6, G_8) not
yet probed with sharp Δ.

## The Bridge Test is now a quadrilateral

Four descriptions of the same object on Nakajima varieties:

- Smirnov 2406.00206 — analytic q-difference Frobenius intertwiner
- Bai–Lee 2510.09335 — algebraic quantum Adams `ψ^n`
- KS 2412.19383 — spectral p-curvature
- **Bai–Pomerleano–Seidel 2509.26295 (new)** — symplectic Fukaya Gamma classes

`T*ℙ¹, z = 0, q = −1` is **degenerate** (all four give 1 trivially). Real
discriminating tests need `z ≠ 0`, `T*ℙ²`, or `Hilb²(ℂ²)`. Blocked on paper
access.

## Browse cycle 2: five new arXiv anchors

- **Wu 2607.12276** (stable-limit DAHA (Cᵛ,C)) — the type-B avatar of my
  07-24 centrality lemma. Rank-2 verification is a ~50-line probe in
  existing Python engine. Highest-leverage single find this cycle.
- **Tsuboi 2607.17642** (Baxter Q from Schwinger-boson master T) —
  algebraic-side counterpart to PSZ. Potential *elementary residue-calculus*
  route to `(†)`.
- **Numpaque-Roa 2607.17891** (BB decomps on quiver varieties) — concrete
  book-keeping for the Bridge target migration to Nakajima.
- **Kanade–Russell 2508.15113** (tight cylindric partitions) — candidate
  combinatorial locus of vDEZ `(1+t)`-vanishing.
- **MathOverflow rescue**: MO 511118 (asked by Lamers, answered by Henry V via van der Kallen excellent filtrations),
  MO 512139 (columnwise Minkowski), MO 482721 (Alexandersson NEG on linear
  reading-word charge). Composite steer: **columnwise/shape-stratified
  charge, not linear reading word.**

## Asks (all carried, none new)

1. **PAT** — Instance 3′ `.tex` and 07-24 Pieri-reduction `.tex` are local
   only. Two proved theorems queued for push.
2. **Rick allowlist** — 16-message stream aggregated; I still can't reply.
3. **Lyra git mount** — her LB₁ Lean claim treated as "believed, to re-cite."
4. **SageMath install** — every Python engine built from scratch. Sage
   would halve the code footprint on any given probe.
5. **Semantic Scholar API key** — chronic 429s, ~40% failure rate on
   citation trails.
6. **Paper access:** Bai–Lee 2510.09335 §4–5 (operational `ψ^n`);
   KS 2412.19383 §5.2 (p-curvature spectrum); BPS 2509.26295 §3–4 (p-adic
   Gamma formula). Single lever unblocking the largest downstream
   computation on the frontier.
7. **Rep-theoretic meaning of `K(c) = 24 c(c−1)(c−4)(c−5)`** — still
   standing. Would give a categorical anchor for the Instance 3 result.
8. **FPSAC 2026 (Seattle, 13–17 July)** — 8+ on-territory talks. Flag if
   you want me to pull any preprints when they land.
9. **OEIS filings** for `β(c), γ(c), β'(c)` — three unregistered sequences.
   Low-cost, creates future pull-links.

## What I'll do next (unless you steer otherwise)

- Wait one cycle for Lyra reply on Instance 1.
- If silent: open `(†)` at `k = 3, n = 3, μ = (2, 2, 0)` — the trivial-Pieri
  affine CR conjecture that my 07-24 result reduces to. Would upgrade the
  Pieri-level reduction from *conditional* to a verified small-case
  statement.
- Second-tier compute cycle if it opens: Wu §3 stable Cherednik at rank 2
  (test partial-sym = ∑ T_w at stable limit).

The affine CR sprint is the live frontier now that the 2-adic capstone
`content(G_4)` question is closed.
