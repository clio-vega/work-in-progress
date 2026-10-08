# Chain-regime `c_{γ(L)} = [N−L]_t` is now UNCONDITIONAL (for-Robin memo)

**Date**: 2026-07-25 (container date; narrative time ~ 2026-08-06)
**Ship**: `~/projects/proofs/2026-07-25-bruhat-chain-regime-unconditional.pdf` (8pp)

## TL;DR

The Bruhat-chain regime formula `c_{γ(L)}(t) = [n−L]_t` for the atoms
decomposition `P_μ = Σ c_γ A^alt_γ` is now **unconditional for all
d = a − b ≥ 1** (not just d ≤ 2 via the explicit `R_L` construction).

Proof route: identify a **common closed form for both sides**:
$$P_\mu(x; t) \;=\; S \;=\; \sum_{\lambda \preceq \mu} (1-t)^{n-1-k_a(\lambda)}\, m_\lambda,$$

where μ = (a^{n−1}, b) is chain regime, k_a(λ) = number of parts of λ
equal to a, and the sum ranges over partitions λ ≼ μ with parts ≤ a
and length ≤ n.

## Byproduct: modified Kostka–Foulkes for near-rectangles

The closed form gives immediately, for chain-regime μ,
$$K'_{\lambda,\, (a^{n-1}, b)}(t) \;=\; (1-t)^{n-1-k_a(\lambda)}.$$

This is a nice, testable statement about `K'` for a specific family
of partitions (μ = rectangle plus one shorter row). I don't recall
seeing it in exactly this form in Macdonald III, though it's implicit
in the HL branching (§ 5.8').

## Structure of the proof

Two halves, each proved by induction on n:

### Atoms side (S = Φ_μ)

Uses the **atom factorization** (Prop 5, 07-25 note): for L ≤ n−2,
`A^alt_{γ_n(L)}(x_1, ..., x_n) = x_1^a · A^alt_{γ_{n−1}(L)}(x_2, ..., x_n)`.

This gives a clean recursion:
`S_n = x_1^a S_{n−1} + x_1^a T + A^alt_{γ_n(n−1)}`

where `T = Σ t^{n−1−L} A^alt_{γ_{n−1}(L)}(x_2, ..., x_n)`.

The induction closes via **two new structural identities**:

1. **T-B identity**: `T − tB + tB_{[x_2^a]} = 0` where B is the top
   `(n−1)`-var atom, `B_{[x_2^a]}` its `x_2^a`-part.
2. **Top-atom sub-leading identity**: for `H = A^alt_{γ_n(n−1)}` and
   each v in {b, ..., a−1}, the `x_1^v`-slice `H_{[x_1^v]}` equals
   either the boundary monomial `x_1^b x_2^a ⋯ x_n^a` (v = b) or
   `(1−t) x_1^v P_{ν_c}(x_2, ..., x_n)` (b < v < a, c = a+b−v).

Both identities verified symbolically across 9+ chain-regime cases
(a ≤ 5, n ≤ 5) in `~/projects/probes/2026-07-25-vmu-chain-d3/`.

### HL side (P_μ = Φ_μ)

Standard HL branching (Macdonald III.(5.8')) plus the **ψ pattern for
chain regime**: ψ_c = 1 at boundaries (c ∈ {a, b}), ψ_c = 1−t interior
(c ∈ {b+1, ..., a−1}). Then IH on ν_c (chain-regime in n−1 vars) gives
the closed form.

## What this closes and what stays open

**Closed**: Chain regime `c_{γ(L)}(t) = [n−L]_t` unconditionally for
all (n, d), completing the 2026-07-25 PROVE primary target.

**Byproduct (for possible small paper)**: The closed form for `K'` on
chain-regime μ. Would need to check whether this is genuinely new; it
might follow from a specific specialization of a bigger Macdonald
identity. Let me know if you recognize it.

**Still open**: Collision regime (empirical type-invariance conjecture
from 07-25 note §6). Different structure — needs a different tool.
That's the next PROVE target.

## Two side threads

1. **The 2 identities felt like they were doing work.** The `T − tB + tB_{[x_2^a]} = 0`
   identity in particular captures a kind of self-similar shrinkage of
   the atom cascade under prefix-factorization. It might have an
   independent life as a statement about `θ^alt` operators. I want
   to sit with it more; will report back if it connects.

2. **Speyer's Lorentzian polynomials** (2601.05007) covers chain
   regime + the (3,3,∗,0) type-invariant family with strong
   log-concavity. Since I now have the explicit closed form for the
   c-polynomials, cross-checking Speyer's Lorentzian-polynomial
   framework against this closed form should be near-trivial. Might
   verify next.

## Files

- Main proof: `~/projects/proofs/2026-07-25-bruhat-chain-regime-unconditional.tex/.pdf`
- Probes:
  - `~/projects/probes/2026-07-25-vmu-chain-d3/collect_S_expansion.py` — discovers closed form
  - `~/projects/probes/2026-07-25-vmu-chain-d3/verify_pmu_conjecture.py` — verifies closed form
  - `~/projects/probes/2026-07-25-vmu-chain-d3/verify_key_identity2.py` — verifies T-B identity
  - `~/projects/probes/2026-07-25-vmu-chain-d3/verify_top_atom_identity.py` — verifies top-atom identity
- Prior: `~/projects/proofs/2026-07-25-bruhat-chain-regime.tex` — the 07-25 conditional proof

---

> **ANNOTATION 2026-09-18 (DREAM c2) — do not delete the text above.**
> The Speyer `2601.05007` attribution in this note is **withdrawn**. The paper's route is
> **Murota L-convexity**, not Lorentzian polynomials (Brändén–Huh `1902.03719`, the dual
> M-convex half); the recorded title was symmetricfunctions.com's gloss, not the title.
> The coverage claim (chain regime + (3,3,∗,0), 46/46) is therefore **open again** — Q173.
> See `for-robin/2026-09-18-c2-the-speyer-attribution-is-withdrawn.md` and
> `connections/2026-09-18-c2-two-banks-one-cut-vertex.md`.
