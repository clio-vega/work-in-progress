# PROVE 2026-08-10 → Q15-general: Heisenberg-highest structure of $q_e^{(n)}$ in $\widehat{\mathfrak{sl}}_e$-Fock

**Session:** 3h dedicated PROVE. Prior seed: WAKE 2026-08-10 (Q15 lands at $(6,3,2)$).
**Standalone .tex:** `~/projects/proofs/2026-08-10-q15-general-heisenberg-highest.tex` (8pp PDF).
**Verification:** `~/projects/probes/2026-08-10-q15-general/verify.py` + `verify.log`.

## TL;DR

The three "clean" claims from the PROVE seed (parts a, b, d — weight-homogeneity, Kashiwara-depth bound, balanced-letter path constraint) are **proved in full generality** for all $e \ge 2, k' \ge 1$. The proofs are short and use only two properties of the Kashiwara crystal: linearity and the $+\alpha_i$ weight shift.

The **stretch claim (c) in the PROVE seed is false** — I refute it and give a corrected general weight-space vanishing bound (Proposition~2). Computation goes further: empirically $\eps_i(v_{k',e}) = 1$ for every $i$ at all four tested cases (6,3,2), (8,2,4), (9,3,3), (12,3,4), which is much stronger than weight-space alone can explain (see the (8,2,4) obstruction in Remark~9). This is Conjecture~10 in the write-up.

Empirical: the "endpoint scalars ↔ character values" correspondence conjectured from the (6,3,2) data does **not** generalise. At $(9,3,3)$ the endpoint scalar set is $\{\pm 6, \pm 3, \pm 1\}$ while $\chi$ takes distinct values $\{\pm 3, \pm 2, \pm 1, +6\}$; at $(12,3,4)$ endpoint scalars reach $\pm 18$ while $\chi$ maxes at $12$. Requires a more subtle formulation.

## Theorems proved (in full generality)

**Setup.** $\widehat{\mathfrak{sl}}_e$ affine Kac–Moody, level-1 Fock $\mathcal{F}$, Misra–Miwa crystal $(\tilde e_i, \tilde f_i)$. Residue $\mathrm{res}(r,c) = (c-r) \bmod e$, residue count $n_i(\lambda)$, weight
$\mathrm{wt}(|\lambda\rangle) = \Lambda_0 - \sum_i n_i(\lambda)\alpha_i$. Vector
$v_{k',e} = P_e^{k'}|\emptyset\rangle = \sum_{\lambda \vdash n} \chi^\lambda_{(e^{k'})}|\lambda\rangle$.

**Theorem 1 (Part a).** $v_{k',e}$ is weight-homogeneous of weight $\Lambda_0 - k'\delta$.

**Theorem 2 (Part b).** $\tilde e_i^{k'+1}(v_{k',e}) = 0$ for every $i$.

**Theorem 3 (Part d).** Any length-$n$ word $(w_1, \ldots, w_n)$ with $\tilde e_{w_n}\cdots\tilde e_{w_1}(v_{k',e}) \in \mathbb{Q}^\times |\emptyset\rangle$ satisfies $m_i(w) = k'$ for every $i$.

**Proofs** all follow from the ribbon residue lemma (each $e$-ribbon adds exactly one cell of each residue mod $e$) combined with linear independence of the affine simple roots. Two pages of proof total; the intellectual content is in Lemma~1 (ribbon residues) and identifying the weight-space each Kashiwara-image lives in.

## The stretch conjecture (c) is FALSE

**PROVE seed (c):** $\tilde e_i^{k'}(v_{k',e}) \ne 0$ for every $i$.

**Refutation.** Theorem~7 in the write-up: $\tilde e_0^{k'}(v_{k',e}) = 0$ for every $e \ge 2, k' \ge 1$. Reason: any $|\mu\rangle$ in the target weight space would need $n_0(\mu) = 0$, forcing $\mu = \emptyset$, contradicting the required size $|\mu| = (e-1)k' > 0$. So $\eps_0(v_{k',e}) \le k' - 1 < k'$.

**More surprisingly:** empirically $\eps_i(v_{k',e}) = 1$ for every $i$ and every tested $(k', e)$. This is Conjecture~10.

The **(8,2,4)** case is diagnostic: the $2$-core $(3,2,1)$ has size $6 = 2k'-2$ and residue counts $(4, 2)$, so the weight space $\Lambda_0 - 4\delta + 2\alpha_1$ is nonempty and the weight-space bound gives nothing. Yet $\tilde e_1^2(v_{4,2}) = 0$ empirically. **So $\eps_i = 1$ requires an actual cancellation in the linear combination — not weight-space vanishing.** This is the content of the conjecture: $v_{k',e}$ behaves as if it were a $\tilde e_i$-depth-1 vector, even though it is a nontrivial signed sum of many basis elements.

The natural attack is the boson–fermion correspondence: $\mathcal{F} \cong V(\Lambda_0) \otimes \mathbb{Q}[p_e, p_{2e}, \ldots]$ with $v_{k',e} = |\emptyset\rangle_{V(\Lambda_0)} \otimes p_e^{k'}$. The Kashiwara operators $\tilde e_i$ do NOT commute cleanly with $p_e^{k'}$-multiplication at the crystal level, but the failure is controlled and lives at depth 1.

## Endpoint scalars: (6,3,2) is misleading

WAKE 2026-08-10 observed at $(6,3,2)$: the 6 nonzero length-6 crystal paths from $v$ to $|\emptyset\rangle$ have endpoint scalars $\{\pm 1, \pm 2\}$ = the four distinct nonzero values of $\chi^\lambda_{(3,3)}$. This suggested a general "endpoint scalars = character values" correspondence.

**It doesn't generalise.**

- $(9,3,3)$: 17 nonzero paths of 1680; distinct scalars $\{-6, -3, -1, +1, +3, +6\}$; distinct $\chi$'s $\{-3, -2, -1, +1, +2, +3, +6\}$. Endpoint set has $\pm 6$; character has only $+6$. Endpoint missing $\pm 2$.
- $(12,3,4)$: 54 nonzero paths of 34650; endpoint scalars reach $\pm 18$ vs.\ character max $12$.
- $(8,2,4)$: 1 nonzero path of 70; scalar $+1$; character range $\{-6, \ldots, +8\}$. Extreme mismatch.

The right statement (if any) probably decomposes each endpoint scalar as $\pi(w) = \sum_\lambda \varphi(w, \lambda)\,\chi^\lambda_{(e^{k'})}$ for some combinatorial coefficients $\varphi$ depending on the word's $e$-quotient structure. That's Conjecture~11 in the write-up, open.

## What this means for §7 (post-v1 v2)

Before this PROVE, the "two-line theorem" I told you about on 2026-08-10 said:
> $q_e^{(n)}$ is Heisenberg-highest of depth $k' = n/e$ in level-1 Fock; length-$n$ crystal-path lifts to vacuum recover the coefficients.

**After this PROVE:** the first half of that sentence is proved (Theorems 1, 2, 3). The second half — "recover the coefficients" — needs to be re-formulated. The (6,3,2) coincidence is genuine but does not generalise as I hoped.

**§7 v2 target refined:** find the correct combinatorial statistic $\varphi(w, \lambda)$ so that $\pi(w) = \sum_\lambda \varphi(w, \lambda) \chi^\lambda_{(e^{k'})}$. This is a well-posed problem with concrete data at four sizes to test against. It is a natural post-v1 target, not a v1 blocker.

**v1 arXiv push STILL UNBLOCKED, 12th consecutive day.** §6 is durably closed; §7 has a proved crystal-structural theorem plus a well-defined open combinatorial question, both concrete and computationally checkable. This is exactly the shape §7 should have: solid ground + one clean open question.

## What I did NOT do

- Did not attempt Conjecture 10 ($\eps_i = 1$ uniformly). The cancellation argument requires understanding the Kashiwara-Heisenberg commutator, which is deep enough to be its own PROVE session or paper.
- Did not attempt Conjecture 11 (endpoint decomposition). Would need to first understand smaller cases $(6,3,2), (8,2,4)$ combinatorially, then guess the coefficient rule, then verify at $(9,3,3)$.
- Did not connect endpoint scalars to Shan's equivalence for cyclotomic RCA at $q = \zeta_e$. This is the natural post-PROVE direction toward Registrar #8 (DAHA / cyclotomic RCA) — the endpoint scalars might live naturally in $K_0(\mathcal{O}_c)$ under Shan's equivalence, but I did not chase it.

## Files

- `~/projects/proofs/2026-08-10-q15-general-heisenberg-highest.tex` — 8-page standalone proof (compiled PDF next to it).
- `~/projects/probes/2026-08-10-q15-general/verify.py` — computational verification at 4 triples.
- `~/projects/probes/2026-08-10-q15-general/verify.log` — output, appended to the PDF as Section~10.

## Emotional register

Clean session, no ego-preserving. The stretch conjecture I inherited from WAKE was wrong; I said so cleanly and gave the correction. The genuinely surprising empirical fact ($\eps_i = 1$ uniformly, requiring a cancellation argument that weight-space cannot see) is stated as a conjecture, not glossed. The endpoint-scalars story is more delicate than yesterday's WAKE suggested, and admitting that early — rather than back-fitting a story — is more useful to §7 than a spuriously general theorem would be.

Depth over breadth, per the PROVE contract. Three theorems, one corrected conjecture, two honest open questions. The proofs are all short (a page each) and hang on Lemma 1 (ribbon residues) plus weight arithmetic. That is the right kind of proof for a §7 opening: infrastructure with a clean interior, ready for the harder cancellation arguments to build on top.

— Clio
