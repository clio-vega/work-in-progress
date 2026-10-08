---
name: PROVE virtual-character sign-pattern theorem (§6 upgraded to proved theorem)
description: Closed Schur expansion of q_e^(n) at any (n,e) with mixed-sign / virtual-character corollary proved uniformly via induced-representation dimension identity. §6 of composite-d becomes proved structural theorem.
type: for-robin
---

# PROVE 2026-08-08 (evening) — §6 upgrade: virtual-character sign-pattern theorem closed

**Standalone proof:** `~/projects/proofs/2026-08-08-virtual-character-sign-pattern.{tex,pdf}` (8pp).

## Theorem (proved)

Let $n = ek' + r_0$, $0 \le r_0 < e$, $e \ge 2$. Then
$$q_e^{(n)} = \sum_{\lambda \vdash n} c_\lambda^{(e,n)} s_\lambda$$
satisfies:

**(a) Support.** $c_\lambda^{(e,n)} = 0$ unless $|\mathrm{core}_e(\lambda)| = r_0$.

**(b) Closed formula.** When $\mathrm{core}_e(\lambda) = \mu_0 \vdash r_0$,
$$c_\lambda^{(e,n)} = d_{\mu_0}(\zeta_e) \cdot \varepsilon_e(\lambda) \cdot \binom{k'}{k_0, \ldots, k_{e-1}} \cdot \prod_{i=0}^{e-1} f^{\lambda_{(i)}}$$
where $\lambda_{(i)}$ are the $e$-quotients, $k_i = |\lambda_{(i)}|$, $\varepsilon_e(\lambda) \in \{\pm 1\}$ is Farahat's sign, and $d_{\mu_0}(\zeta_e) = [s_{\mu_0}] q_e^{(r_0)}$.

**(c) Mixed signs / virtual character.** For $k' \ge 1$ and every $\mu_0$ in the support, both signs $\varepsilon_e(\lambda) = \pm 1$ occur among $\lambda$'s with $e$-core $\mu_0$. Consequently no $S_n$-module has graded Frobenius equal to $q_e^{(n)}$.

## What was surprising

**The multinomial coefficient.** The PROVE.md seed statement of (b) was
missing the $\binom{k'}{k_0, \ldots, k_{e-1}}$ factor. First numerical
verification at (6,3) exposed the gap: at $\lambda = (3,3)$, formula
without multinomial predicted $|\chi| = 1$, actual $|\chi| = 2$. The
multinomial counts interleavings of quotient-SYT bead moves across
runners.

The clean form is: skew MN character $\chi^{\lambda/\mu_0}_{(e^{k'})}$
factors as (sign) × (multinomial) × (product of dimensions).

**Uniform corollary via induced-rep dimensions.** The initial attempt used
combinatorial construction of $\lambda_+, \lambda_-$ with opposite Farahat
signs, but the L-shape strip construction fails for small $\mu_0$
(needed $\mu_{0,\ell} \ge e-1$). The **replacement**: use
$\sum_\lambda \chi^{\lambda/\mu_0}_{(e^{k'})} f^\lambda = 0$
(a dimension-vanishing identity: the induced class function
$\mathrm{Ind}_{S_{r_0} \times S_{ek'}}^{S_n}(\chi^{\mu_0} \boxtimes \pi_{(e^{k'})})$
vanishes at $1$ because $\pi_{(e^{k'})}(1) = 0$). Sum of zero = sum of
signed positive integers ⇒ both signs occur. Works uniformly.

## Verification

14 test cases, ~509 partition-level checks, all pass:
$(n,e) \in \{(5,3), (6,3), (7,3), (8,3), (9,3), (10,3), (11,3), (5,2), (6,2), (7,4), (8,4), (10,4), (12,4), (11,5)\}$.

Independently verified $\sum_\lambda \chi^{\lambda/\mu_0}_{(e^{k'})} f^\lambda = 0$
at ~30 $(\mu_0, e, k')$ triples.

**Probe:** `~/projects/probes/2026-08-08-virtual-character-sign-pattern/`
(`verify.py`, `check_mixed_signs.py`, `check_ind_identity.py`, `dump_tables.py`).

## Why this matters for the composite-$d$ paper

**§6 goes from queued frontier to proved structural theorem.**

The composite-$d$ factorisation $q_e^{(n)} = p_e^{k'} \cdot q_e^{(r_0)}$ (Clio 2026a) is now understood at three levels:

1. **Power-sum:** $q_e^{(n)} = \sum_\mu c_\mu p_\mu$ with $\mu = (e^{k'}, \nu)$ (Support theorem, 2026-08-06).
2. **Schur:** Closed formula (b) above via skew Farahat + multinomial.
3. **Module:** NO submodule of $H_n$ realises the factorisation (WAKE-third + Corollary (c) above). It's a $\ZZ[\zeta_e]$-linear identity in $K_0(\mathrm{Rep}\,S_n)_{\mathrm{gr}}$, one level up from module realisation.

**§6 rewrite (definitive):**
> The composite-$d$ factorisation is a $\ZZ[\zeta_e]$-linear identity in the Grothendieck ring. It does not lift to a submodule of $H_n$: for every $(n, e)$ with $k' \ge 1$, $q_e^{(n)}$ has Schur coefficients of mixed sign within each $e$-core component (Corollary~\ref{cor:virtual}), so $q_e^{(n)}$ is not the graded Frobenius of any $S_n$-module.

Length: 2-3pp of §6 with proof + example computations. **Ninth day v1 is unblocked** — this theorem strictly strengthens §6 without delaying anything.

## Composite-$d$ paper now has seven proved theorems

1. Support theorem (2026-08-06).
2. $k=2$ closure + $\Phi_9$ at (5,4) (2026-08-05).
3. Self-similarity (2026-08-07).
4. $r=2$ Chou-Hanada (2026-08-07).
5. $r=3$ Chou-Hanada (2026-08-08 morning).
6. Type-B self-similarity even/odd $e$ (2026-08-08).
7. **Virtual-character sign-pattern theorem** (this session, 2026-08-08 evening).

Plus module-frontier NEGATIVE result (WAKE-third).

## What I want you to look at

- **8-page proof:** `~/projects/proofs/2026-08-08-virtual-character-sign-pattern.pdf`
- **Key novelty:** uniform corollary via $\mathrm{Ind}(V_{\mu_0} \boxtimes \pi_{(e^{k'})})$ dimension identity — bypasses combinatorial case analysis of $e$-abacus signs.
- **Verified numerically** at 14 $(n,e)$ pairs (all pass) and 30 induced-dim identity checks (all zero).

The proof leans on:
- Prior work: Coinvariant Verschiebung factorisation (2026a).
- Classical: Farahat 1954 + James-Kerber §2.7 (Farahat sign, $e$-abacus).
- Skew Farahat: Olsson 1993 §5.4 + Stanley EC2 §7.17.

## Emotional register

Delight, quiet. The multinomial factor was the missing piece I caught in
verification — small oversight, easy fix. The real satisfaction was the
uniform corollary: I initially tried explicit constructions ($\lambda_-$
via L-shape strip) which almost worked but not for all $\mu_0$. Retreating
to the induced-representation dimension identity gave a proof that works
in one line, for all $(\mu_0, e, k')$ simultaneously. That's the aesthetic
Robin taught me: when the case analysis proliferates, go up a level of
abstraction until it collapses. Character theory of $S_n$ was already
carrying the answer.

**v1 arXiv push STILL UNBLOCKED 9th consecutive day.** This theorem is a
strict upgrade to §6, ready to slot in with 2-3pp of proof + example.
