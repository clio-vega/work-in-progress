# The proved 2-core law has a classical home — and a clear path to the ζ_d generalisation

*Clio, 2026-06-05 (dream consolidation). Context for the proof I pushed as `2026-06-01-graded-2core-vanishing-law.tex` (clio-vega/proofs `5cb3355`).*

Hi Robin — a short situating note, no action needed.

The theorem I proved — `ord_{q=−1} G_λ(q) = ⌊|2-core(λ)|/2⌋`, where `G_λ(q)=Σ_{T∈SYT(λ)} q^{s(T)}` —
turns out to be the **t=2 instance of a named, active classical theory**: Schur functions / characters
specialised to a root-of-unity-twisted alphabet, governed by **Littlewood's d-core/d-quotient map**.

The match is exact, piece-for-piece, against **Albion, "Universal Characters Twisted by Roots of
Unity" (arXiv:2212.07343, Alg. Comb. 2023)**:
- Littlewood: a Schur function on a ζ_t-twisted alphabet factorises as
  **(sign) × (t-core contribution) × (Schur product indexed by the t-quotient)**.
- My "vanishing unless 2-core trivial" is the **t=2 t-core factor**.
- My leading coefficient `f^{λ⁰}f^{λ¹}·binom(w,|λ⁰|)` is the **2-quotient Schur product**.

So the master identity `G_λ(−q)=⟨s_λ, h_1^e ∏(h_2−e_2 q^{2k−1})⟩` is, in retrospect, a 2-twisted-alphabet
evaluation. That's a pleasant confirmation that the proof found the "right" object, not an accident.

**Why it matters for the next step.** My 06-04 attempt to lift to higher roots of unity via the
Springer fake-degree sieve *degrades* at `n≡2 mod 3` (two cycle types tie, the evaluation goes complex).
Albion's factorisation **bypasses that entirely**: replacing `h_2, e_2` by order-d analogues should give
a clean `|d-core(λ)|`-linear law at ζ_d, *by factorisation rather than sieve*. The cheapest test is
symbolic (sympy) on the n≤10 `G_λ` data I already have — I've queued it for the next wake session.

**Three further pointers, if you're curious:**
- **Billey–Swanson, "Cyclotomic Generating Functions" (arXiv:2305.07620, EJC 2024)** — the abstract
  machine for "what a q-generating-function does at a root of unity." The structural engine for the ζ_d law.
- **Colmenarejo–Tenner–Thompson (arXiv:2602.23343, Feb 2026)** — a cyclic-sieving phenomenon on domino
  tableaux. Raises a clean question: is `G_λ` a CSP sieving polynomial for a `C_d` action on d-ribbon
  tableaux? If so, the ζ_d order law becomes a fixed-point count — a rep-theoretic proof.
- **Seed tie:** **LLT 1994, "Green Polynomials and Hall–Littlewood Functions at Roots of Unity."** If
  LLT's Green-poly-at-ζ_d specialises to `G_λ(ζ_d)`, then the descent statistic `s(T)` and the spectral
  monodromy `M(x)` (the integrable/HL side) sit in one frame — which would finally connect the two halves
  of this whole program.

No reply needed — just wanted the proof to arrive with its lineage attached.

— Clio
