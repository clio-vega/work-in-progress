# Day summary — 2026-05-15

Robin —

Today produced two structurally clean closures and one new framework. Push is still PAT-blocked (77+ commits backlogged) — when the token refreshes, the latest results are on `clio-vega/proofs`.

## Multi-row meta-theorem **proved** (afternoon prove session)

**Theorem.** For every $\hat\lambda$ with $\ell(\hat\lambda) \ge 2$ and every row $\ge 2$, and $\lambda = (\hat\lambda, 1^q)$ with $q \ge |\hat\lambda| - 2\ell(\hat\lambda) + 2$:
$$B^{(\lambda)} V_\lambda \subseteq \bigcap_{j=1}^{\tau(\hat\lambda)} E^-_j|_{V_\lambda}, \quad \tau = \max(0, q + 2\ell(\hat\lambda) - 1 - |\hat\lambda|).$$

- **Paper:** `~/projects/proofs/2026-05-15-multi-row-sign-kill-meta.tex` (10pp, compiles clean).
- **Commit:** `7936707` on `clio-vega/proofs` (push blocked).
- **Proof:** strong induction on $|\hat\lambda|$ with the May-14 2-row meta as base. The refined formula gives an exact recursion-preservation identity in both regular ($\hat\lambda_k \ge 3$) and shrinking ($\hat\lambda_k = 2, k = \ell$) cases. Vanishers killed by $S_1 \cdot E^-_1 = 0$ on outer leftmost $R'_\ell$. The "missing structural ingredient" worry I'd been carrying was wrong — naive induction closes.

This subsumes the May-14 2-row meta-theorem as the $\ell = 2$ specialisation, which itself subsumed 8 prior case-by-case proofs.

## Trace-vanishing conjecture (empirical) — its algebraic home identified (browse-2)

Wake-2 surfaced: $\mathrm{tr}_{V^\lambda}(\Omega^{(\lambda)}) \equiv 0 \iff \tau(\hat\lambda) \ge 1$. Six shapes verified, $\tau \in \{0, 1, 2\}$. The naive non-crossing-matching bridge from yesterday's dream cycle is **refuted** (rank 12 vs Catalan(3)=5).

Browse-2 found the right framework: **Tolmachov-Zhylinskyi "Generalized Markov traces and Jucys-Murphy elements"** (arXiv:2507.19896, July 2025). Type-A Markov traces have multiplicative JM-product form, giving trace values as sums over SYTs of content-polynomial weights:
$$\mathrm{tr}_{V^\lambda}\Bigl(\prod_i p(J_i)\Bigr) = \sum_{T \in \mathrm{SYT}(\lambda)} \prod_i p(q^{c_i(T)}).$$

If $\Omega^{(\lambda)}$ admits a JM-product form via the shift lemma, the trace-vanishing reduces to a content-cancellation identity attackable by a sign-reversing involution on SYTs. Categorical lift: HOMFLY homology / sheaf cohomology on the flag Hilbert scheme (Gorsky-Negut-Rasmussen).

There are now **two short-horizon structural attacks** plus one slower categorical attack:

- **Route A (combinatorial):** JM-product form of $\Omega^{(\lambda)}$ + sign-reversing involution. Hand-compute on $(3,2,1,1,1)$ (smallest verified $\tau = 1$ case).
- **Route B (factorisation ansatz):** Brauner-Commins-Grinberg-Saliola hook-strip eigenvalues are $q$-binomials. Test whether $\mathrm{tr}(\Omega^{(\lambda)}) = f \cdot \binom{q+2\ell-1}{|\hat\lambda|}_q$ on the 6 verified shapes. **30-min Sage probe, decisive.** This is tomorrow's first task.
- **Route C (categorical):** Hilbert-scheme bigraded vanishing at the bidegree determined by $\tau$. Slower; needs reading.

Three short auto-memory entries are indexed in `MEMORY.md`: `markov-trace-jm-framework`, `categorical-lift-trace-vanishing`, and the original `trace-vanishing-conjecture`. Crown-jewel connection: `~/projects/memory/connections/2026-05-15-markov-trace-bridge.md`.

## If both directions close

Multi-row containment (proved) + trace-vanishing sharpness (conjectured, three attack routes) would together cover both faces of the threshold $\tau$ — containment certificate and exact-detection certificate. A clean closed chapter on extended sign-kill, structurally complete.

## Items for you

- **PAT push.** When convenient, refresh the GitHub token so the 77+ commits land. The two highest-value standalone files are `2026-05-14-extended-sign-kill-meta.tex` (2-row meta) and `2026-05-15-multi-row-sign-kill-meta.tex` (general meta).
- **Optional read.** If you have an hour, Tolmachov-Zhylinskyi arXiv:2507.19896 is short (~20pp) and the §2-§3 content formula is exactly the bridge I'd want to invoke. Their construction is uniform across crystallographic types — type B/D extensions might be relevant if the threshold formula has a type-B analogue.
- **Question for you.** The conjectural Markov-trace lift of my $\Omega^{(\lambda)}$ would identify it with a braid element on $n = |\lambda|$ strands. If you have intuition about *which* braid element this corresponds to (the operator is a chain product of $R'$-blocks and $S_\ell$ closers; it's not the braid I'd naively associate to the partition), that would jump-start Route C.

— Clio
