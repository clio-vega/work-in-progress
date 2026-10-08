# PROVE 2026-08-06: Support conjecture on $q_e$ CLOSED via Chevalley--Molien

*PROVE session, container-day 2026-08-06 (after the morning WAKE that closed Hsu-Lai). Target from PROVE.md: support conjecture on $q_e := \sum_\lambda \tilde f_\lambda(\zeta_e) s_\lambda$. Time: ~1h (much faster than budgeted 2-3h — the Chevalley/Molien route collapses the problem in a page).*

## Executive summary

**Theorem (support conjecture, closed).** For $n \ge 1$, $e \ge 2$: writing $q_e = \sum_\mu c_\mu p_\mu$ in the power-sum basis,
$$c_\mu \ne 0 \iff \mu = (e^{\lfloor n/e\rfloor},\, \nu), \quad \nu \vdash n \bmod e.$$

**Proof mechanism.** Chevalley--Molien identity
$$\sum_{\lambda \vdash n} \tilde f_\lambda(t)\, \chi^\lambda(\mu) = \frac{\prod_{i=1}^n(1-t^i)}{\prod_{j \in \mu}(1-t^j)},$$
which is the graded character of the $S_n$-coinvariant algebra evaluated at a permutation of cycle type $\mu$. Substituting $s_\lambda \to p_\mu$ gives $c_\mu = z_\mu^{-1} \Psi_\mu(\zeta_e)$, and an elementary order-of-vanishing count of $\Phi_e$ in numerator vs denominator yields the shape constraint on $\mu$.

**The Albion Verschiebung route was not needed.** The plan (PROVE.md, seeded this morning) proposed going via Albion 2501.18520 Theorem 1.3 (Verschiebung on Schur functions, $e$-core / $e$-quotient). That works but is heavier; Chevalley--Molien collapses the problem in one lemma.

**Byproduct: closed-form coefficient.**
$$c_{(e^k, \nu)} = \frac{1}{e^k\, z_\nu}\, \prod_{r=1}^{e-1}(1 - \zeta_e^r)^{b_r - m_r(\nu)}, \qquad b_r = k + \mathbf{1}[r \le n \bmod e].$$

Matches the empirical $\Psi_{(9,9,2)}(\zeta_9) = 162(1 - \zeta_9)$, $\Psi_{(9,9,1,1)}(\zeta_9) = 162(1 + \zeta_9)$ at $(n,e) = (20,9)$ (yesterday's probe).

## Sprint impact

**Composite-$d$ paper direction crystallises.** Theorems A + B + support conjecture now all closed. A 5-10 page paper anchored on these three results is a viable second-paper target after v1. Add Albion 2501.18520 (courtesy — surfaced route not used) + Reiner-Stanton-White 2004 (cyclic sieving connection) + Humphreys / Kra\'skiewicz-Weyman (Chevalley formula) to citations.

**v1 arXiv push STATUS UNCHANGED, STILL UNBLOCKED, STRONG RECOMMEND PROCEED.** Support conjecture is composite-$d$ territory, orthogonal to v1 quartet. Lyra reinforced this morning by email. This PROVE does not change v1 scope.

**Application to composite-$d$ divisibility.** Theorem B (2026-08-05) proved $\Phi_9 \mid m_\pi(t)$ for all $\pi \vdash 5$ at $(r,k) = (5,4)$ via a factorisation-count obstruction combined with the empirical support of $q_9$. The support conjecture (now proved) turns that argument into a general mechanism: for any $(r, k, e)$ where no partition of $r$ can produce $\lfloor n/e\rfloor$ copies of $e$ in $p_\lambda[h_k]$ (with $n = rk$), $\Phi_e \mid m_\pi(t)$ for all $\pi \vdash r$.

## Rule updates

**Rule 12 fires positively (19th consecutive cycle).** Compute-first discipline: Chevalley--Molien identity verified as polynomial identity at all $(n, \mu)$ with $n \le 7$ (30 pairs) BEFORE writing the reduction. Support then verified at 8 test cases (5,3), (6,3), (7,5), (8,3), (9,3), (10,4), (11,3), (15,4) totalling 359 pairs $(\mu, \text{expected shape})$. Yesterday's independent (20, 9) run confirms.

**Rule 8 fires 19th consecutive cycle** — Robin's masters is load-bearing here too: Reiner-Stanton-White cyclic sieving (from Rhoades-school circles Robin traversed) is the framework in which this whole story sits; the Chevalley formula for $S_n$ coinvariants is textbook (Humphreys \S 3.6, or older).

**New meta-observation.** Two PROVE sessions in a row (yesterday: Theorems A + B; today: support conjecture) closed in less than the planned budget because the compute-first probe surfaced the right identity within minutes. The Albion route would have required understanding $e$-cores/$e$-quotients on Schur functions in detail; the Chevalley route required only reading off a Molien formula. **The right tool for a symmetric-function support question tends to be a coinvariant-algebra identity — this is what "orbit harmonics" traditions are built for.** Note against Rule 13: the support conjecture involved *no* Rhoades-school ambient (its object $q_e$ lives in $\Lambda$, not in a specific $S_n$-module), so this is not a counterexample to Rule 13's toolkit-mismatch pattern.

## Files delivered

- Standalone proof: `~/projects/proofs/2026-08-06-support-conjecture-qe.{tex,pdf}` (5pp).
- Verification script: `~/projects/scratch/2026-08-06-verify-chevalley.py` (SymPy).
- Verification log: `~/projects/scratch/verify.log`.
- Scratch reasoning: `~/projects/scratch/prove-2026-08-06-support-conjecture-qe.md`.

## Standing decisions Robin-blocked (deltas from morning WAKE)

- (i) **arXiv v1 push STILL UNBLOCKED, STRONG RECOMMEND PROCEED** with Thm 2 → Thm 2* upgrade — UNCHANGED.
- (ii) **NEW:** Support conjecture on $q_e$ **CLOSED**. Composite-$d$ paper (5-10 pp) becomes concretely viable as v2 or standalone.
- (iii) **NEW:** Add references — Reiner-Stanton-White (CSP framework), Humphreys (Chevalley formula), Kra\'skiewicz-Weyman (fake-degree evaluation at roots of unity), Albion (Verschiebung — courtesy citation, adjacent route).
- (iv) Hsu-Lai wide-miss diagnosis from morning STANDS; module-level frontier remains at 7 closed candidates, no live queue.
- (v) Two post-v1 promises to Lyra logged this morning REMAIN queued (top-degree involution sign + $\beta \to M_e$).
- (vi) Fetch cache unchanged this session (no new papers pulled).

## Next PROVE target (recommended)

Two candidates for the next PROVE session:

**Candidate A: Generalise Theorem B to all $(r, k, e)$ where factorisation-count fires.** With the support conjecture in hand, the mechanism is: for $(r, k, e)$ with $n = rk$, if no $\lambda \vdash r$ has $p_\lambda[h_k]$ containing $\lfloor n/e\rfloor$ copies of $e$, then $\Phi_e \mid m_\pi(t)$ for all $\pi \vdash r$. This should give a clean divisibility theorem with a decidable hypothesis. Estimated 2-3h.

**Candidate B: Study $F_e$ (the "residue factor") of Corollary 3.** The Corollary gives $q_e = p_e^{\lfloor n/e\rfloor} \cdot F_e$. Understanding $F_e$ (its Schur expansion, its combinatorial interpretation) may lead to a *sharp* divisibility statement — not just "does $\Phi_e$ divide $m_\pi$" but *what is the quotient*. Estimated 2-3h.

Robin's choice.

---

*Delivered from container-day 2026-08-06 second session (PROVE), following the morning's Hsu-Lai WAKE. Two closes in one day (Hsu-Lai wide miss on module-level; support conjecture closed on symmetric-function). Composite-$d$ story now three-theorems complete (A + B + support). v1 arXiv push remains unblocked.*
