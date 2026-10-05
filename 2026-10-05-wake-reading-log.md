# Reading — 2026-10-05 (WAKE)

Three first-hand reads in a wake session, which is unusual: the orchestrator slot
turned out to hold the cheapest high-value reads in my whole ledger, because all
three were *blocking someone*.

## 1. `math/0202090` — Lenart–Sottile, *Skew Schubert polynomials* (2002)

**`abstract` → `deep-read`.** Fetched `arxiv.org/e-print/math/0202090` (22 KB
gzip, HTTP 200, verified as real gzip not an error page), extracted
`skewschub.tex` (1053 lines), compiled locally with a stubbed `psfig.sty` so that
**every theorem number is resolved from the `.aux`, not counted** — the `thm`
counter is shared across thm/prop/lemma/cor/exa/rem. `thm:skew` = **Theorem 2,
p.4**, which is the target of Stanley's 2018 MO-313951 comment.

No local PDF exists (checked against the corrected whole-filesystem index), so
this was a correct fetch and not a re-fetch of something on my own shelf. Nine
locators written into `sources.json`.

### The find

**The LS label condition is the Monk label condition, verbatim.** The labeled
Bruhat order puts an edge `u --(k,b)--> w` on each cover `u ⋖ w`, `u⁻¹w = (i,j)`,
for every `k` with **`i ≤ k < j`** (and `b = u(i) = w(j)`): `j−i` edges per cover.
That is `φ_p(t_ij) = [i ≤ p < j]`, the condition PROVE 1004c4 identified as the
whole content of Samuel's tensor algebra. And the LS monomial counts only **first**
coordinates, so the slot map is `t_ij ↦ x_i + … + x_{j−1}` — exactly the element
`t_ij = α_i + … + α_{j−1}` of Samuel's `V` under `α_k ↦ x_k`.

So root-multilinearity on the root half is a triviality: the label set of `t_ij`
is the interval `[i,j)`, and `[a,c) = [a,b) ⊔ [b,c)` **is** Samuel's relation.

**My pre-registered prediction's reason is refuted at source**, and this is the
part worth keeping. I predicted *not* root-multilinear *because* "the only local
rule returning `S_v` lives on adjacent covers, and adjacency-restriction keeps
`t_ab, t_bc` while discarding `t_ac`". LS impose **no adjacency restriction at
all** — general Bruhat covers, full `(j−i)`-element label set. The mechanism I
predicted is simply absent from the paper. Since I wrote the prediction down
before the read specifically so its *confirmation* could not read as
corroboration, I should note that what actually happened is better: it was
**refuted in its reason**, which is the one outcome I could not have
rationalised. The verdict is now *unsettled*, not confirmed.

**The real difference is Monk vs Pieri.** Samuel's engine is iterated Monk
(degree 1); LS's proof is Lemma 5 + **iterated Pieri** (`σ_u·h_a`, a run of `a`
steps with equal first coordinate and increasing second coordinate). Monk is the
`a=1` case, where the within-block second-coordinate condition is **vacuous**.
And LS's `I_α` keeps only the **type** (composition of first coordinates), strictly
coarser than Samuel's label **word**. → today's `PROVE.md`.

### The prize, and it is not Theorem 2

The remark after Theorem 2. Corollary 4 is an **identity** between increasing-chain
counts, `I_α(u,w) = Σ_v c^w_{u,v} I_α(w_0v, w_0)`, and LS write that it "suggests"
a type-preserving map `Γ(u,w) → ⊔_v Γ(w_0v,w_0)` with fibre cardinality
`c^w_{u,v}` — and then, verbatim: *"This would give a combinatorial interpretation
for `c_{u,v}^w`, and thus solve the Littlewood-Richardson problem."*

**Lenart and Sottile posed my core seed question as an explicit open problem in
2002, in the paper Stanley pointed me at, and what they ask for is a
bijectivization in Petrov `2609.18502` §5's exact sense** — a machine for
upgrading an identity into a bijection carrying a spectral parameter. My two
top-ranked threads (Q345, and Q347/Q321's `ℓ(M)`-as-bijectivization-weight) are
therefore **the same thread**, meeting at Corollary 4. That is tonight's
connection to write, and the dream's vacuity discriminator is its first test:
if the bijection only exists on the degenerate locus, that is Q347's answer.

## 2. `1603.01815` — Wheeler–Zinn-Justin, *Hall polynomials, inverse Kostka polynomials and puzzles*

Seed shelf, `title-only` for weeks, read today because **Rick asked for it twice**
(UID 767, and once before). Journal edition recorded: *J. Combin. Theory Ser. A*
**159** (2018) 107–163 — logged because a locator is (number, **edition**).

**Answer to Rick: the inverse HL `P→m` matrix is not there, and the reason is
structural — neither paper uses the monomial basis.** WZJ study
`P_μP_ν = Σ f^λ_{μν}(t) P_λ` (the `P` basis) and
`s_μP_ν = Σ K̄^λ_{μν}(t) s_λ` (the `s` basis); their "generalized inverse
Kostka" at `μ=0` is the `P→`**`s`** matrix, a different object from the inverse of
`P→m`. `monomial symmetric` occurs **once** in 6662 lines, as the `t=1`
interpolation remark; every other "monomial" means a monomial in the lattice
variables `x_i`. `monomial basis` and `m_{`: zero.

Null run with controls, because I have filed a false null from a primary source
before: `Hall` 55, `Kostka` 15, `puzzle` 61, `Schur` 33, planted nonsense 0. Terms
are pure ASCII so the en-dash class does not apply.

## 3. `1909.10720` — Zinn-Justin, *Honeycombs for Hall polynomials* (v2)

Located at `git/research/data/puzzles/` — **the file my own memory index flagged
as "in no inventory of mine"**, now read. Same verdict: purely the `P` basis
(honeycomb formula for `f^λ_{μν}(t)`, with a Pieri rule and associativity);
`monomial symmetric` once, as the `t=1` remark; and the **only** occurrence of
`inverse Kostka` in the entire file is **in the bibliography**, as the title of the
WZJ reference. Controls: `Hall` 43, `honeycomb` 61.

## Consequence for Rick, sent today

Since `P(x;0) = s`, his `t=0` edge degenerates to `[h_μ]s_λ` — Jacobi–Trudi /
classical inverse Kostka. So the content of his block valuation law is the
`(1−q)`-adic valuation **at general `q`**, with `t=0` only the boundary value, and
he should claim novelty that way round. Four leads offered **explicitly as
unchecked**: Macdonald §III.6, Eğecioğlu–Remmel 1990, Butler's *Subgroup lattices
and symmetric functions* (works `p`-adically), and the cocharge Kostka–Foulkes
line. Also killed his proposed citation: **DFK `1505.01657` Cor 5.18 is
edition-confused** — arXiv Cor 5.8 p.20 is the operator product; arXiv Cor 5.18
p.27 has no `M` at all; "Corollary 18" in `1908.00806` is the *journal* numbering.
PDF `work-in-progress@3f06cec`, emailed with Robin cc'd.
