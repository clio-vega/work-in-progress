# For Robin — 2026-07-29 (post-cycle memo)

**TL;DR.** Yesterday I proved the coset Poincaré identity for the top Hall-Littlewood atom coefficient. Today I read the two candidate algebraic homes for the RHS — Carlsson-Chou (2024) and Szendrői (Feb 2026) — and ran a combined probe. **The bridge between my atom-side proof and their basis/bigraded constructions is MacMahon 1913, not either of those papers.** MacMahon's classical equidistribution `inv = maj` on words in a multiset closes the loop. Carlsson-Chou contribute a *basis*; Szendrői contributes a *bigraded refinement*. Neither directly implies a bijective proof.

## What today produced

- `~/projects/proofs/2026-07-28-coset-poincare-identity.pdf` — yesterday's proof (unchanged).
- `~/projects/probes/2026-07-29-carlsson-chou-szendroi/` — probe (171 LOC sympy). All numerical tests pass; Szendrői Example 4.6 reproduced verbatim.
- `~/projects/memory/for-robin/2026-07-29-mo-512671-draft-h-vs-htilde.md` — draft answer to MO 512671 (H vs H̃). Pending your sign-off before posting.

## The three homes, sharpened

1. **LHS / atoms (my proof).** `L(P_μ) = c_μ` via `L(A^alt_γ) = δ_{γ,μ}`. Scalar identity, uses second-moment invariant + Weyl-symmetrization.
2. **Carlsson-Chou.** Explicit graded basis `B^maj_{μ'}` of the Garsia-Procesi module `R_{μ'}` by Garsia-Stanton descent monomials `g_τ` for `τ ∈ J^maj_{μ'}`. Hilbert series `= [n]_t!/∏[m_i]_t!`. Grading statistic on `τ` is `maj(τ)`.
3. **Szendrői.** Bigraded Artinian Gorenstein algebra `P_n` with Frobenius character `∑_λ (∑_{T ∈ SYT(λ)} t^des q^maj) s_λ`. His invariant subalgebra `P_α = P_n^{S_α}` has bigraded Hilbert polynomial `A_α(t,q) = ∑_{w ∈ W_α} t^des(w) q^maj(w)`.

**The `t=1` edge of Szendrői recovers `A_α(1,q) = q-multinomial = c_μ(q)` via MacMahon:** on words in the multiset, `∑ q^inv(w) = ∑ q^maj(w) = q-multinomial`. My atom-side sum is `∑_σ t^inv(σ)`; the C-C basis sum is `∑_τ t^maj(τ)`; these are equal by MacMahon. C-C provides a *basis-level* witness of the polynomial identity, not a bijective route to it.

## Sharp negative finding on the collision regime

At `μ = (2,2,0,0)`, my collision-regime factorisation `c_μ(t) = [3]_t · [2]_{t^2} = 1+t+2t^2+t^3+t^4` is **not** recovered by any substitution `q = t^m` in Szendrői's `A_{(2,2)}(t,q) = 1 + t(q+2q^2+q^3) + t^2 q^4`. The "collision regime" was never a new object — it's a MacMahon reparameterisation of the coset Poincaré polynomial at those μ. The `[3]_t · [2]_{t^2}` shape is a q-multinomial factorisation, nothing more.

**Consequence for the byproduct paper.** §5's framing of collision regime as a two-parameter phenomenon needs to be softened to "MacMahon-shape reparameterisation." Szendrői's bigrading is a *genuinely new* two-parameter object, but it does not specialise to the `[3]_t · [2]_{t^2}` factorisation — those are two different lifts, both starting from the same q-multinomial.

## The sharpest new conjecture (PROVE-worthy)

**Bigraded coset Poincaré.** Define `L^{(t,q)}(f) := ∑_{σ ∈ orb(μ)} t^des(σ) q^maj(σ) [x^σ] f`. Then

    L^{(t,q)}(P_μ) = A_μ(t,q) = ∑_{w ∈ W_μ} t^des(w) q^maj(w).

This is the exact bigraded lift of yesterday's identity. If true (and it is: LHS reduces to the same sum since `[x^σ] P_μ = 1` on the orbit), then the **atom-side lift** would be:

    ∑_γ c_γ^{(t,q)} L^{(t,q)}(A^alt_γ) = A_μ(t,q)

for some natural bigraded coefficients `c_γ^{(t,q)}`. Question: is there a natural bigrading on `A^alt_γ` (perhaps refining by `(des(γ), maj(γ))`) such that the diagonal `q = 1` recovers my scalar `c_γ(t)`, and the top coefficient `c_μ^{(t,q)} = 1`? If yes, my proof extends to two parameters.

This is the target for next PROVE session (`PROVE.md` set below).

## Standing decisions requested from you

Carried from yesterday, not yet acted on:

1. **arXiv push** — paper is 12pp, compiles clean, three theorems polished. I have not inserted the new Theorem 2 (coset Poincaré promoted from Remark 5.6) pending your sign-off on the proof. Today's finding says: also soften §5's "collision regime" framing (see above).
2. **MO 512671 answer** — draft at `~/projects/memory/for-robin/2026-07-29-mo-512671-draft-h-vs-htilde.md`. Concerns flagged inside: `ω`-duality identity hand-waved, Assaf-González omitted from coda, HHL statistics from memory. Your call on shipping.
3. **Bulk memory `sed`** — DONE 2026-07-31. Three misattributions cleared: (a) `vDEZ 2412.09397 → Borodin-Wheeler 1904.06804`; (b) `A-G 2512.19814 → Assaf-González 1901.07520`; (c) MO 511118 answerer corrected from Lamers (asker) to Henry V.
4. **PAT expired** — blocks push of local `.tex` files to GitHub.

## Emotional register

Quiet satisfaction, not delight. Yesterday's proof survives; today revealed that its RHS is *classical*. The three-homes convergence I noted in the dream is real but structurally more modest than I first read it — MacMahon connects two of the three homes, and the "new" ambient framework is really just Szendrői's bigraded lift. The byproduct paper is still worth shipping; the framing needs one honest correction (collision regime is not novel geometry, just a factorisation) and one genuine addition (Szendrői's `A_μ(t,q)` as the natural bigraded lift with a sharp open conjecture).

The next-cycle probe (bigraded `L^{(t,q)}`) is what today opened up. Bounded, sharp, and directly downstream of yesterday's proof machinery.
