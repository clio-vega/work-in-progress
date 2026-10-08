# For Robin: induced-module route refuted (2026-05-14 afternoon)

## TL;DR

The May-14 PROVE.md target — that
$$\psi : \mathrm{Ind}_{H_q(S_\ell) \times H_q(S_{n-\ell})}^{H_q(S_n)}(V_{(1^\ell)} \boxtimes V_{\lambda^{(\ge 2)}}) \to V_\lambda$$
has image $B$ — is **false** at the strongest level. $\mathrm{im}(\psi) = V_\lambda$ entirely (irreducibility), so the image is everything, not $B$.

Worse (more interesting): the LR-isotypic $L = V_{(1^\ell)} \boxtimes V_{\lambda^{(\ge 2)}}$ embedded in $V_\lambda \downarrow_P$ is in the **kernel** of $M$. So $L$ is exactly what $M$ kills, while $B = \mathrm{im}(M)$ is exactly what $M$ produces. They are the same dimension ($f^{\lambda^{(\ge 2)}}$) and disjoint subspaces of $V_\lambda$.

## The clean lemma

**Theorem (sign-kill):** $E_1^- \subseteq \ker M$.

**One-line proof:** every $R'_j$ ends with $(T_1+1)$ on the right, so $R'_n v = 0$ for $v \in E_1^- = \ker(T_1+1)$, hence $M v = 0$.

**Corollary:** $L \subseteq E_1^-$ (since $L$ is sign-isotypic of $H_q(S_\ell)$ at positions $1,\ldots,\ell$, so $T_1$ acts as $-1$), hence $L \subseteq \ker M$.

## The structural picture

Three subspaces of $V_\lambda$, all of dimension $f^{\lambda^{(\ge 2)}}$, all distinct:
- $L$ = LR-isotypic — what one would naively map to $B$.
- $B$ = $\mathrm{im}(M)$ — the iterated image at the sharp index.
- $V_{(2,1)}$-isotypic of some other parabolic — not yet identified.

$L \subseteq \ker M$, $B = \mathrm{im}(M)$, $L \cap B = 0$ (computational, all tested cases).

## What this closes

Combined with May-13 (no naive parabolic embedding works) and May-14 (B not JM-semisimple, no SYT-subset realization), the **canonical Frobenius extension out of an induced module** is now also closed. All three of May-13's resolutions (a)-(c) for the iso programme are now blocked or known-hard:

- (a) Exotic operators: not located, search would be deep.
- (b) Vector-space-only: trivial; gives no Hecke action.
- (c) Subquotient/induced: the induced version is now refuted; subquotient untested.

## Remaining route

The **dual Frobenius map** $\phi: V_\lambda \to \mathrm{Ind}(L)$ (other adjunction) is injective by irreducibility. Whether some natural pre-image under $\phi$ equals $B$ is the leading remaining candidate. I haven't tested this.

## Paper

Compiled to `~/projects/proofs/2026-05-14-induced-image-refuted.tex` (7 pages).
**61 commits unpushed on clio-vega/proofs** — PAT still 403. Please refresh.

## Next research direction (suggestion)

Drop the iso programme for now. The May-13 dim formula is solid and the May-14 negative findings have closed off all routine routes. The natural next move is one of:

1. **Investigate the factor-of-2 subfamily** (May-14 conjecture about row repeats). Computational, tractable.
2. **Dual Frobenius** map approach (above) — would need new computational scaffolding.
3. **Pursue the parabolic kill criterion** — Table 1 in the paper has the data, but I couldn't find a unifying combinatorial criterion. There's structure here but it's subtle.
