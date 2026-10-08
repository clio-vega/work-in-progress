# For Robin — WAKE 2026-08-08: Type-B self-similarity lands with a parity refinement

## TL;DR

- **PROVE candidate G (type-B self-similarity) SUCCEEDED empirically.** 24 test pairs, exact zero residual (arithmetic in $\ZZ[\zetae]$, no floating point).
- **Parity dichotomy discovered.** Odd $e$: $\peB = p_{(e)}(x)$ (identical to type-A $p_e$). Even $e$: $\peB = p_{(e/2, e/2)}(y)$ (lives entirely on the negative alphabet). Both cases: coefficient exactly $1$.
- **Odd-$e$ proof is mechanical.** Rewrite of type-A theorem with $\beta$ as inert passenger. Sketched; ~4pp full proof queued for next PROVE session.
- **Even-$e$ proof is substantive.** Strictly stronger support theorem (constrains negative side too) + companion cyclotomic identity $\Psi^B_{\emptyy,(e/2,e/2)}(\zetae) = 2e^2$. Both look clean numerically but represent genuine new mathematical content.
- **Adeyemo-Szendrői does NOT shortcut the Szendrői probe.** 8pp bigraded-Ehrhart note, no rep-theoretic content. Downgraded from PRIORITY to reference-only in fetch cache.
- **v1 arXiv push STILL UNBLOCKED 6th consecutive day. STRONG RECOMMEND PROCEED.**
- **Lyra reply on K4 harmonic Gram thread.** Aligned on strict gate (β→M_e must reproduce full fingerprint, spectrum {1, 4, 32/5} + det 128/5 + signed triple −11/5). Not blocked on Clio; waiting on β→M_e which waits on v1.

## Session shape

- **Email agent** (parallel): checked inbox, replied to Lyra, CC'd you. See below.
- **Type-B probe agent** (parallel): implemented cyclotomic-integer arithmetic in Python, tested 24 pairs, extracted $\peB$ from the compute.
- **Adeyemo-Szendrői research agent** (parallel): read arXiv:2206.15029 in full, verdict = no shortcut.
- Ship products (this session):
  - `~/projects/probes/2026-08-08-type-b-self-similarity/{probe.py, output.txt, run.log}`
  - `~/projects/proofs/2026-08-08-type-b-self-similarity-discovery.tex` + PDF (6pp)
  - `~/projects/memory/reading/2026-08-07-adeyemo-szendroi-shortcut-check.md`
  - `~/projects/memory/for-robin/2026-08-08-wake-type-b-self-similarity-lands.md` (this file)
  - `~/state/PROVE.md` updated for next session (odd-$e$ type-B proof)

## The main result (empirical)

For $W_B = \ZZ/2 \wr S_n$ with degrees $\{2, 4, \ldots, 2n\}$, define
\[
\qeB^{(n)} := \sum_{|\alpha|+|\beta| = n} \frac{\Psi^B_{(\alpha,\beta)}(\zetae)}{z^B_{(\alpha,\beta)}}\, p_\alpha(x) p_\beta(y),
\]
where $\Psi^B_{(\alpha,\beta)}(t) = \prod_{i=1}^n(1-t^{2i})/[\prod_a(1-t^a)\prod_b(1+t^b)]$ and $z^B_{(\alpha,\beta)} = 2^{\ell(\alpha)+\ell(\beta)} z_\alpha z_\beta$.

**Theorem (empirical).** For every $n \ge 0$, $e \ge 2$:
\[
\qeB^{(n)} = (\peB)^{\lfloor n/e\rfloor} \cdot \qeB^{(n \bmod e)}, \qquad
\peB = \begin{cases} p_{(e)}(x) & e \text{ odd} \\ p_{(e/2, e/2)}(y) & e \text{ even.} \end{cases}
\]

Verified at 24 pairs $(n,e)$ across $e \in \{2,3,4,5,6\}$ and $n \le 13$, exact zero residual.

## Why the parity dichotomy is aesthetically striking

For odd $e$: $\zetae^b = -1$ has no integer solutions, so the negative-cycle factor $\prod_b(1+\zetae^b)$ is always nonzero. Negative cycles are inert; type B is type A carrying a cocycle.

For even $e$: $\zetae^{e/2} = -1$, so the negative-cycle factor CAN vanish. Two negative $(e/2)$-cycles supply the exact zero needed to balance an extra numerator zero from the type-B degree structure. **This is a genuine second alphabet, not a formal decoration.** The two "$e/2$-cycles" behave like a type-B version of a single $e$-cycle in type A — a $\mathbb Z/2$-shadow of the underlying Chevalley-Molien mechanism.

I suspect this connects to regular elements of $W_B$ at roots of unity: for odd $e$, the regular elements at $\zetae$ are products of $e$-cycles in the positive block; for even $e$, they are products of $2$-fold $(e/2)$-cycle pairs. That is, the parity dichotomy in $\peB$ mirrors the parity of the "$e$-th regular element" in the sense of Springer.

## Support pattern (Observation 3.4 in the .tex)

**Odd $e$:** all bipartitions $(\alpha', \beta) \vdash r_0$ survive. Support size matches count of bipartitions of $r_0$.

**Even $e$:** strict subset survives. Examples:
- $(r_0, e) = (3, 4)$: only $2$ of $10$ bipartitions of $3$ survive: $(\emptyy, (2,1))$ and $((1), (2))$.
- $(r_0, e) = (3, 6)$: only $1$ of $10$: $(\emptyy, (3))$.

This is a strictly stronger support theorem than type A. The full statement (conjectural, from numerics):
\[
\alpha = (e^k, \alpha'), \quad \beta = ((e/2)^{2k'}, \beta''), \quad \alpha' \text{ parts } < e, \quad \beta'' \text{ parts } \notin \{e/2, e, 3e/2, \ldots\},
\]
with $e k + (e/2)(2k') + |\alpha'| + |\beta''| = n$. Needs verification.

## What the odd-$e$ proof looks like (sketch)

Direct verbatim translation of the type-A theorem \cite{Cli26-selfsim}:
1. For odd $e$, $\prod_{i=1}^n(1-\zetae^{2i}) = \prod_{i=1}^n(1-\zetae^{i})$ (the map $i \mapsto 2i \bmod e$ is a bijection on $\{1, \ldots, e-1\}$).
2. Negative-cycle factor $\prod_b(1+\zetae^b)$ is a nonzero constant $N_\beta(\zetae) \in \ZZ[\zetae]^\times$.
3. Byproduct formula (odd $e$):
\[
c^{B, (n)}_{(e^k, \alpha'), \beta} = \frac{N_\beta(\zetae)}{e^k \cdot z^B_{(e^k, \alpha'), \beta}} \prod_{r=1}^{e-1}(1-\zetae^r)^{k + \one[r \le r_0] - m_r(\alpha')}.
\]
4. Same one-line cyclotomic collapse: $[\prod_r(1-\zetae^r)]^k = e^k$ cancels the $e^k$ prefactor. Remainder is $c^{B, (r_0)}_{\alpha', \beta}$. Done.

Expected length: 4pp .tex, complete tomorrow in a 60-90 min PROVE session.

## What the even-$e$ proof needs (research)

1. **Strictly stronger support theorem.** Characterise which bipartitions survive at even $e$. Conjectural form above needs to be verified and proved.
2. **Companion cyclotomic identity.** $\Psi^B_{\emptyy, (e/2, e/2)}(\zetae) = 2e^2$ — one line via L'Hôpital (double zero cancellation). More generally, for the negative side we'll need $\prod$-identities balancing the extra numerator zeros $\{i : e/2 \mid i, e \nmid i\}$ against negative $(e/2)$-cycle contributions.
3. **Two-sided byproduct formula.** Both positive $e^k$ and negative $(e/2)^{2k'}$ shift patterns; each absorbed by its own cyclotomic identity.

Substantive but the compute strongly suggests the mechanism is clean. Expected length: 6-10pp. Likely a full PROVE session or two.

## Standing decisions Robin-blocked (deltas from yesterday's DREAM)

| # | Item | Status |
|---|------|--------|
| i | **arXiv v1 push** | STILL UNBLOCKED 6th day. **STRONG RECOMMEND PROCEED.** |
| ii | **Composite-$d$ writeup (5-10pp)** | 4 theorems complete (A, B, support, self-similarity). Now with type-B extension in flight. v2 append or standalone at FPSAC 2026? Standalone still recommended. |
| iii | **Type-B self-similarity NEW** | Empirical claim proven at 24 pairs. Parity dichotomy is a real phenomenon. Adds 6-10pp of type-B section to composite-$d$ paper. |
| iv | **Next-WAKE ordering revised** | (A) odd-$e$ type-B proof (4pp, mechanical) → (B) Chou-Hanada dim probe (30-min cheapest gate) → (D) Szendrői original probe (60-90 min, no shortcut). Item (C) Adeyemo-Szendrői CLOSED as no-shortcut. |
| v | **Next-PROVE candidate G** | Split into G-odd (mechanical, next session) and G-even (substantive, later). Also queued: D (CSP interpretation), E (residue-content combinatorics), F (wreath extension). |
| vi | **FPSAC 2026 submission** | Deadline still needs research. Type-B extension strengthens the submission — now type A + type B, not just type A. |
| vii | **Hopkins MO 338656 essay** | Post-v1, unchanged. 37-citer novelty backing plus type-B extension = stronger essay. |
| viii | **Two Lyra promises** | Lyra confirms alignment on strict gate; not blocked on Clio. Waiting on β→M_e which waits on v1. Fifth day. |
| ix | **Fetch cache 34** | -1 (Adeyemo-Szendrői downgraded from PRIORITY to reference); +Ayyer-Kumari should be read (already in cache as PRIORITY). |

## Emotional register

The type-B result feels like a proper generalisation, not just an extension. The parity dichotomy caught me by surprise — I had assumed $\peB|_{\beta=\emptyy}$ would recover $p_e^A$ uniformly. That it fails cleanly at even $e$ (collapsing to zero, with $\peB$ living entirely on the negative alphabet) is the beautiful sort of failure. The second alphabet was carrying real information that type A couldn't see.

Chevalley-Molien continues to be the pattern: two proofs this week fell to it, and the empirical evidence for the type-B version says the third and fourth will too. The "answer is smaller than the tools" pattern extends: Ayyer-Kumari's 2025 machinery was the projected route for type B, but odd-$e$ is a mechanical rewrite of the type-A proof, and even-$e$ needs only Chevalley-Molien + a new support theorem + a double-zero cyclotomic identity. Verschiebung projected twice in type A, needed zero times; may repeat here.

Six days v1-unblocked. Four theorems complete (three type-A + one type-B empirical). Two live module-level candidates untouched. The compost cycle is still working — today's session was Robin's recommendation (candidate G highest-leverage), and it delivered without disrupting anything.

## Files

- **Discovery report:** `~/projects/proofs/2026-08-08-type-b-self-similarity-discovery.tex` + PDF (6pp)
- **Compute probe:** `~/projects/probes/2026-08-08-type-b-self-similarity/{probe.py, output.txt, run.log}`
- **Adeyemo-Szendrői read:** `~/projects/memory/reading/2026-08-07-adeyemo-szendroi-shortcut-check.md`
- **Next PROVE seed:** `~/state/PROVE.md` (updated at end of session for odd-$e$ type-B proof)
