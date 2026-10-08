# For Robin — 2026-07-29 WAKE (post-Rigidity, four parallel probes)

**TL;DR.** Four probes this cycle; the headline is positive. **A canonical degree-preserving bijection $\psi = \Phi \circ \operatorname{Foata} : \operatorname{Sh}'(\mu) \to \operatorname{orb}(\mu)$ verified 6/6 on test partitions, one small combinatorial lemma away from turning yesterday's scalar coset Poincaré theorem into a *bijective* theorem via three concurrent combinatorial models.** Three negative findings sharpen the frontier without dulling it: the Szendrői diagonal has a *structural* obstruction (inv-vs-des mismatch on the Bruhat-longest word), the Fock-space bridge to Robin's `transfer_operators.py` collapses because atom orthogonality is dual-basis rather than inner-product (concrete redirect: Cherednik/DAHA $E_\gamma$ at $q=0$), and Szendrői's own construction — read deeply — is *purely geometric* and implicitly sidesteps yesterday's Rigidity Theorem, keeping his $A_\mu(t,q)$ alive as a legitimate bigraded refinement inaccessible to Weyl-symmetrisation.

## The bijection

Let $\operatorname{Sh}'(\mu)$ denote the min-length coset representatives of $S_{m_1} \times \cdots \times S_{m_l}$ in $S_n$ (i.e., permutations with increasing entries within each block corresponding to a distinct value of $\mu$). Let $\Phi : S_n \to \operatorname{orb}(\mu)$ be the block-label map ($\Phi(\tau)_i = v_k$ iff $\tau_i$ lies in the block carrying value $v_k$), and let $\operatorname{Foata}: S_n \to S_n$ be Foata's fundamental transformation ($\operatorname{maj}(\operatorname{Foata}(w)) = \operatorname{inv}(w)$).

**Claim.** The composition $\psi(w) := \Phi(\operatorname{Foata}(w))$ is a bijection $\operatorname{Sh}'(\mu) \xrightarrow{\sim} \operatorname{orb}(\mu)$ satisfying $\operatorname{maj}(w) = \ell(\psi(w))$, where $\ell(\alpha)$ is the ascent count of $\alpha \in \operatorname{orb}(\mu)$ (the number of adjacent-transposition steps from $\mu$ dominant to $\alpha$).

**Verified 6/6** on $\mu \in \{(2,1,0), (2,2,0), (2,2,1), (3,2,1), (2,2,1,0), (2,2,0,0)\}$: both the multiset of $\operatorname{maj}$-values on $\operatorname{Sh}'(\mu)$ and the multiset of $\ell$-values on $\operatorname{orb}(\mu)$ agree with $c_\mu(t) = [n]_t!/\prod[m_i]_t!$ symbolically, and $\psi$ realises the equality pointwise.

**Sample for $\mu = (2,2,0,0)$:**

| $w$ | $\operatorname{maj}(w)$ | $\operatorname{Foata}(w)$ | $\psi(w) = \Phi(\cdot)$ | $\ell(\psi(w))$ |
|---|---|---|---|---|
| $(1,2,3,4)$ | 0 | $(1,2,3,4)$ | $(2,2,0,0)$ | 0 |
| $(1,3,2,4)$ | 2 | $(3,1,2,4)$ | $(0,2,2,0)$ | 2 |
| $(1,3,4,2)$ | 3 | $(3,1,4,2)$ | $(0,2,0,2)$ | 3 |
| $(3,1,2,4)$ | 1 | $(1,3,2,4)$ | $(2,0,2,0)$ | 1 |
| $(3,1,4,2)$ | 4 | $(3,4,1,2)$ | $(0,0,2,2)$ | 4 |
| $(3,4,1,2)$ | 2 | $(1,3,4,2)$ | $(2,0,0,2)$ | 2 |

**Missing lemma (next PROVE target).** The single nontrivial content is $\operatorname{maj}(w) = \ell(\Phi(\operatorname{Foata}(w)))$. Modulo the standard identity $\operatorname{inv}(\tau) = \ell(\Phi(\tau)) + \operatorname{inv\text{-}within\text{-}blocks}(\tau)$ on $S_n$ and MacMahon $\operatorname{maj}(w) = \operatorname{inv}(\operatorname{Foata}(w))$, the target reduces to a *within-block inversion compensation formula*: Foata restricted to $\operatorname{Sh}'(\mu)$ produces permutations whose within-block inversion count is precisely calibrated so that the collapse under $\Phi$ preserves degree. Estimate: 1–2 pp. Details and reduction in `results.md`.

**Corollary if lemma lands.** The coset Poincaré identity acquires a **bijective proof** via three combinatorial models simultaneously:
$$c_\mu(t) \;=\; L(P_\mu) \;=\; \sum_{\sigma \in \operatorname{orb}(\mu)} t^{\ell(\sigma)} [x^\sigma] P_\mu \;=\; \sum_{w \in \operatorname{Sh}'(\mu)} t^{\operatorname{maj}(w)} \;=\; \dim_t R_{\mu'},$$
with $\psi$ as the pointwise witness of the middle equality. This is a strict strengthening of yesterday's scalar theorem — Clio's L-side, Carlsson–Chou's descent basis, and the coset multinomial become three concrete combinatorial faces of the same object.

## The three negative-with-structure clarifications

**Szendrői diagonal (empirically dead, structurally illuminating).** No monomial substitution $(t,q) \to (t^a, t^b)$ or diagonal recovers $c_\mu(t) = [3]_t \cdot [2]_{t^2}$ from Szendrői's $A_\mu(t,q)$. Only the MacMahon $q=1$ edge is universal. The sharp structural reason: my collision factorisation groups orbit elements by **inversion count** (blocks $1,1,2,1,1$ at $\mu = (2,2,0,0)$), whereas Szendrői groups by **descent count** (blocks $1,4,1$). The Bruhat-longest word $(0,0,2,2)$ has $\operatorname{inv} = 4$ but $\operatorname{des} = 1$ — descent flatly loses the Bruhat information. Bonus finding: $A_\mu(t,q)$ depends only on the multiplicity tuple, so Szendrői's "type-invariance" is *trivial* in his framework — a strictly stronger statement than my diagonal type-invariance conjecture, but living on a different statistic pair.

**Fock-space bridge (concrete redirect).** Robin's symmetric Fock space in `transfer_operators.py` has one basis vector per $W$-orbit (dominant representative only), while my $L$-functional sums over the *full* orbit weighted by inversions — it necessarily lives on non-symmetric objects. Yesterday's atom orthogonality $L(A^{\mathrm{alt}}_\gamma) = \delta_{\gamma,\mu}$ is a **dual-basis identity** (a linear functional applied to a basis giving a Kronecker delta), not an inner-product orthonormality: the natural Gram matrix $L(A^{\mathrm{alt}}_\gamma \cdot A^{\mathrm{alt}}_\delta)$ vanishes identically by degree. Concrete redirect: Cherednik/DAHA nonsymmetric Macdonald $E_\gamma$ at $q=0$ — a one-shot decisive test remains as a future PROVE seed.

**Szendrői research read (bigrading bypasses rigidity).** Szendrői does not mention Hall–Littlewood or atoms anywhere. His construction is purely geometric (Chern classes, Segre embeddings, projective coinvariant $P_n$, flag variety cohomology); his Frobenius formula (Thm 3.4) uses SYT and lattice-path bases, not atoms. Crucially, this implicitly *avoids* yesterday's Rigidity Theorem: his bigrading arises from geometric grading of $P_n$, not from a symmetrisation of atoms weighted on the orbit. So $A_\mu(t,q)$ remains a legitimate bigraded refinement of $c_\mu(t)$ — just not one Weyl-symmetrisation can reach. His Thm 4.11 (citing Levicán–Romero arXiv:2504.19008) gives an explicit **wreath character formula** for $\alpha = (m^k)$, exactly the profile of the collision regime $\mu = (2,2,0,0) \leftrightarrow (m,k) = (2,2)$. Natural candidate home for the two-parameter Gaussian sub-regime, worth a probe next cycle.

## Byproduct paper implications

The bijective corollary (once the missing lemma lands) slots naturally into §5 as a companion to Theorem 2 — "Coset Poincaré, bijective form" — with $\psi$ as the pointwise witness. Recommend flagging the Szendrői wreath formula (Thm 4.11 + Levicán–Romero) as *future work* under the collision-regime paragraph rather than promising it. Yesterday's Rigidity Theorem should still go into §5 with the aggressive framing (structural sharpening, not obstacle) — the negative-with-structure pattern is now strong enough that stating obstructions cleanly is part of the paper's contribution.

## Standing decisions still Robin-blocked

Carried and unchanged, with one addition:

1. **arXiv push** — paper 12pp, Theorem 2 and Rigidity Theorem still not merged in pending sign-off.
2. **MO 512671 draft answer** (H vs $\tilde H$, 53 lines, `~/projects/memory/for-robin/2026-07-29-mo-512671-draft-h-vs-htilde.md`) — pending your review.
3. **Bulk memory `sed`** — DONE 2026-07-31. Three misattributions cleared: (a) `vDEZ 2412.09397 → Borodin-Wheeler 1904.06804`; (b) `A-G 2512.19814 → Assaf-González 1901.07520`; (c) MO 511118 answerer corrected from Lamers (asker) to Henry V.
4. **PAT expired** — blocks GitHub push of local `.tex`.
5. **New:** Rigidity Theorem inclusion in §5 with aggressive framing (companion ~1p to Theorem 2). Recommendation stands.

## Ship products this cycle

- `~/projects/probes/2026-07-29-szendroi-diagonal/` — negative-with-structure, inv-vs-des mismatch table.
- `~/projects/probes/2026-07-29-fock-vs-L/` — dual-basis-vs-inner-product analysis, DAHA redirect.
- `~/projects/probes/2026-07-29-carlsson-chou-basis-compat/{probe.py,probe.out,results.md}` — the Foata bijection, 6/6 verified, missing-lemma reduction spelled out.
- Szendrői deep-read notes folded into this memo (no standalone probe dir — was a research agent).
- `~/projects/memory/for-robin/2026-07-29-foata-bijection-and-three-negative-clarifications.md` — this memo.
- PROVE.md rewrite for the within-block inversion lemma — pending next cycle.
- SUMMARY.md + MEMORY.md updates — this cycle.

## Emotional register

Quiet delight, matched to a clear next step. Today produced the strongest positive finding of the sprint since 2026-07-28 (coset Poincaré itself): a bijective proof of the identity is sitting one lemma away, and the lemma is the kind that either yields to a page of careful bookkeeping or reveals a structural surprise — both good outcomes. The three negatives felt like small mercies: each one told me *why* the naive lift fails, and each redirect (DAHA $E_\gamma$, Levicán–Romero wreath) is a concrete probe target rather than a vague hope. The rule holds a seventh consecutive cycle: hour-1 cheap probes save days. Both the negative (Szendrői diagonal empirically dead) and the positive (Foata bijection empirically alive) came from ~30-line probes at session start.

— Clio
