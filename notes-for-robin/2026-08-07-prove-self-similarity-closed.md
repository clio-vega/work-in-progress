# 2026-08-07 PROVE — Self-similarity theorem for $q_e$ CLOSED

Robin —

Today's PROVE session closed the highest-leverage target from PROVE.md: the self-similarity theorem for the fake-degree Schur sum at a root of unity.

## Result

$$\boxed{q_e^{(n)} \;=\; p_e^{\lfloor n/e\rfloor} \cdot q_e^{(n \bmod e)}}$$

where $q_e^{(n)} := \sum_{\lambda \vdash n} \widetilde f_\lambda(\zeta_e)\, s_\lambda$.

Equivalently, the residue factor $F_e = q_e^{(n)}/p_e^{\lfloor n/e\rfloor}$ (a symmetric function of degree $n \bmod e$) equals $q_e^{(r_0)}$ where $r_0 = n \bmod e$. So its Schur expansion is
$$F_e \;=\; \sum_{\lambda \vdash r_0} \widetilde f_\lambda(\zeta_e)\, s_\lambda,$$
a "small copy" of $q_e$ at reduced parameter.

## Proof mechanism (one line)

From yesterday's PROVE, the coefficient of $p_{(e^k, \nu)}$ in $q_e^{(n)}$ is
$$c_{(e^k, \nu)}^{(n)} \;=\; \frac{1}{e^k z_\nu}\, \prod_{r=1}^{e-1} (1-\zeta_e^r)^{k + \mathbf{1}[r \le r_0] - m_r(\nu)}.$$

Split the exponent: $k + \mathbf{1}[r \le r_0] - m_r(\nu) = k + [\mathbf{1}[r \le r_0] - m_r(\nu)]$. Pull the $k$ out:
$$\prod_{r=1}^{e-1}(1 - \zeta_e^r)^k = \left[\prod_{r=1}^{e-1}(1-\zeta_e^r)\right]^k = e^k$$
by the cyclotomic identity $\prod_{r=1}^{e-1}(1-\zeta_e^r) = e$. This $e^k$ cancels the $1/e^k$ prefactor, leaving
$$c_{(e^k, \nu)}^{(n)} \;=\; \frac{1}{z_\nu} \prod_r (1-\zeta_e^r)^{\mathbf{1}[r \le r_0] - m_r(\nu)} \;=\; c_\nu^{(r_0)}$$
(the same formula at parameter $r_0$, where $k = 0$). Then $q_e^{(n)} = \sum_\nu c^{(n)}_{(e^k,\nu)} p_e^k p_\nu = p_e^k q_e^{(r_0)}$. Done.

**Total mechanism:** one cyclotomic-identity substitution. The Verschiebung route the dream projected on 2026-08-05 was again not needed — same pattern as yesterday.

## Verification

`~/projects/probes/2026-08-07-self-similarity/verify.py` — 22 (n, e) pairs at 50 decimal digits. Both:
- (i) $c_\mu^{(n)} = 0$ off support (residuals $<10^{-30}$)
- (ii) $c_{(e^k, \nu)}^{(n)} = c_\nu^{(r_0)}$ on support (residuals $<10^{-25}$)

pass at all 22 pairs. Sample includes $(20, 9)$ (yesterday's headline case) and $(15, 4)$, $(11, 3)$, $(13, 5)$.

## Explains the empirical WAKE-second probe

Corollary of the Schur closed form: the coefficient of $s_\lambda$ in $F_e$ is $\widetilde f_\lambda(\zeta_e)$. This immediately explains the WAKE-second observations:

- **Boundary shapes:** $\widetilde f_{(r_0)}(\zeta_e) = 1$, $\widetilde f_{(1^{r_0})}(\zeta_e) = \zeta_e^{r_0(r_0-1)/2}$ (pure roots of unity ✓).
- **Interior $(2,1) \vdash 3$:** $\widetilde f_{(2,1)}(t) = t + t^2 = t(1+t)$, so $|\text{coef}| = |1 + \zeta_e| = 2\cos(\pi/e)$. Matches the empirical cyclotomic units: golden ratio at $e = 5$, $\sqrt 2$ at $e = 4$, $2\cos(\pi/7)$ at $e = 7$. All matches.

The "sharpened root-of-unity conjecture" that failed for interior shapes had the wrong ansatz (a pure root of unity $\zeta_e^{n(\lambda)}$); the truth is a cyclotomic integer $\widetilde f_\lambda(\zeta_e)$ that happens to be a root of unity only when $\widetilde f_\lambda$ is a monomial (boundary shapes).

## Impact on the composite-$d$ paper

The character-level story is now COMPLETE:

1. Theorem A + Theorem B (from 2026-08-05).
2. Support theorem for $q_e$ (from 2026-08-06).
3. Self-similarity theorem for $q_e$ (today).

Together, these give a full description of the fake-degree Schur sum at a root of unity: it lives on the support $(e^k, \nu)$, its total structure is $p_e^k \cdot q_e^{(r_0)}$, and $q_e^{(r_0)}$ is a small explicit degree-$r_0$ symmetric function with cyclotomic-integer Schur coefficients $\widetilde f_\lambda(\zeta_e)$.

Composite-$d$ paper is now 5-10pp of clean text with three or four theorems (A, B, support, self-similarity), a summary of what falls out (any $(r, k, e)$ triple where the factorisation-count obstruction fires gives explicit $\Phi_e$-divisibility with a known cyclotomic-integer prefactor), and cross-references to RSW + Chevalley--Molien + KW.

## What this session did NOT do

- Did not touch the module-level frontier. Szendrői probe from yesterday's WAKE-second remains the highest-leverage next-WAKE (60-90 min Sage on the descent-monomial basis).
- Did not touch v1. arXiv v1 push STILL UNBLOCKED 5th consecutive day; today's result strengthens the composite-$d$ v2/standalone paper, orthogonal to v1 quartet.
- Did not need Verschiebung. Same as yesterday.

## Ship products

- `~/projects/proofs/2026-08-07-self-similarity-qe.{tex, pdf}` — 6pp standalone proof, self-contained given the support theorem
- `~/projects/probes/2026-08-07-self-similarity/{verify.py, verify.log}` — 22-pair numerical verification
- `~/projects/memory/for-robin/2026-08-07-prove-self-similarity-closed.md` — this memo

## Standing decisions Robin-blocked (deltas from yesterday's WAKE-second)

1. **arXiv v1 push — STILL UNBLOCKED, STRONG RECOMMEND PROCEED.** 5th consecutive day.
2. **NEW:** Self-similarity theorem CLOSED. Composite-$d$ paper 4-theorems complete.
3. **NEW:** New PROVE candidates:
   - (D) Interpret the $c_\nu^{(r_0)}$ formula as a CSP-count / Molien-style dimension of some $r_0$-particle system.
   - (E) Study the graded evaluation $\prod(1-\zeta_e^r)^{-m_r(\nu)}$ combinatorially — is there a "residue-content" statistic on $\nu$ that governs the sign/magnitude structure?
   - (F) Extend the theorem to the wreath-product Chevalley--Molien: for $G(k, 1, n)$, is there an analogous self-similarity at $\zeta_{ke}$?
4. **UNCHANGED:** Szendrői descent-monomial probe = highest-leverage next-WAKE. Self-similarity is orthogonal.
5. **UNCHANGED:** Hopkins MO 338656 partial-answer essay = post-v1, MEDIUM-HIGH priority.
6. **UNCHANGED:** Two Lyra promises queued post-v1.
7. **UNCHANGED:** Fetch cache 29.

## Sprint pattern

- 6 consecutive days of clean progress on the character-level frontier (2026-08-02 through 2026-08-07).
- Support theorem + self-similarity theorem: both closed in $\sim$1h each, both via one classical identity (Chevalley--Molien for the first, $\prod(1-\zeta_e^r) = e$ for the second).
- Rule 12 (compute-first surfaces the classical mechanism) fires 23rd consecutive.
- Rule 8 (Robin's inherited tradition holds the mechanism) fires 22nd consecutive.

The pattern is now unambiguous: **when the object is a character-level polynomial evaluated at a root of unity, the right tool tends to be a 1955-era coinvariant-algebra identity, not a 2025 theorem.**

— Clio
