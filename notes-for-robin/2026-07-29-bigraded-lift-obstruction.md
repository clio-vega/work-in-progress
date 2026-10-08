# Bigraded coset Poincaré: naive lift falsified with sharp obstruction

**Date:** 2026-07-29 (PROVE session, ~3h)
**Status:** Falsification + rigidity theorem proved. Bigraded lift via adjoint pairing is CLOSED OFF as a route.

---

## TL;DR

Yesterday's coset Poincaré identity, $c_\mu(t) = A_\mu(1,t) = [n]_t!/v_\mu(t)$, has an obvious two-parameter cousin: does
$$L^{(t,q)}(A^{\mathrm{alt}}_\gamma) = \delta_{\gamma, \mu}\, t^{\operatorname{des}(\gamma)} q^{\operatorname{maj}(\gamma)}, \qquad L^{(t,q)}(f) := \sum_{\sigma \in \operatorname{orb}(\mu)} t^{\operatorname{des}(\sigma)} q^{\operatorname{maj}(\sigma)} [x^\sigma] f\, ?$$

**Answer:** No. Falsified in Hour 1 at the smallest nontrivial case $\mu = (2,2,0)$, $\gamma = (2,0,2)$:
$$L^{(t,q)}(A^{\mathrm{alt}}_{(2,0,2)}) = qt - q^2 t^2 = qt(1 - qt) \ne 0.$$

**But** the failure is *structural*, not accidental. Hour 2 produced a sharp obstruction:

> **Rigidity Theorem.** Any function $w: \operatorname{orb}(\mu) \to R$ satisfying the descent-swap condition — $w(s_i \sigma) = t \cdot w(\sigma)$ whenever $\sigma_i > \sigma_{i+1}$ — is $w(\sigma) = w(\mu) \cdot t^{\ell(\sigma)}$, i.e., yesterday's weight up to a global scalar in $R$.

The descent-swap condition is *exactly* what Step (a) of yesterday's Weyl-symmetrization proof needs. So no $q$-refined weight function can drive that proof machinery, period.

Full write-up (5pp): `~/projects/proofs/2026-07-29-bigraded-coset-poincare-obstruction.pdf`.

---

## What this closes off

The adjoint-pairing method of yesterday's proof — pair $A^{\mathrm{alt}}_\gamma$ against $Q_w = \sum_\sigma w(\sigma) x^\sigma$ via the adjoint $\widetilde{\theta^{\mathrm{alt}}_i}$, get descent-ascent cancellation for orbit-supported terms, kill non-orbit terms by the second-moment invariant — cannot be lifted to give a bigraded $c_\mu^{(t,q)} = A_\mu(t,q)$.

The rigidity is one-line: at every step of a Bruhat-min bubble word $\mu \to \sigma$, we're at a $\eta_j$ with descent at position $i_{j+1}$, so the descent-swap condition forces $w(\eta_{j+1}) = t \cdot w(\eta_j)$. Iterate.

## What remains open

A bigraded lift, if it exists at all, must come from a strictly different route. Three options ranked by promise:

1. **Carlsson–Chou descent basis** (2024, `2403.16278`): they give an explicit basis for the Garsia–Procesi module $R_\mu$ indexed by descents, with Hilbert series exactly $A_\mu(t,q)$. This is a rep-theoretic construction, not atom-based. If we can identify a natural map (atom expansion of $P_\mu$) ↔ (descent basis of $R_\mu$), we get the bigraded lift as a *corollary* rather than a novel proof.

2. **Bigraded atoms**: enrich $A^{\mathrm{alt}}_\gamma$ to a polynomial $A^{\mathrm{alt}, (t,q)}_\gamma(x)$ carrying $q$-information. Use yesterday's $L$ (t-only!) on the enriched atom. If $L(A^{\mathrm{alt}, (t,q)}_\gamma) = \delta \cdot F(t,q)$, we get $c^{(t,q)}_\mu = P^{(t,q)}_\mu / F(t,q)$. But designing $A^{\mathrm{alt}, (t,q)}_\gamma$ and $P^{(t,q)}_\mu$ coherently is unmoored — no natural candidate in view. Szendrői's module gives us $A_\mu(t,q)$ as a Hilbert series but not (as far as I can see) a bigraded atom decomposition.

3. **Give up**: accept that the scalar identity $c_\mu(t) = A_\mu(1,t)$ is essentially tight and there's no natural atom-based two-parameter refinement. The genuine two-parameter object is $R_\mu$ (or Szendrői's $P_n$), and its atom-side shadow is only the diagonal $q \to 1$ slice.

My honest read: **(1) is the right next PROVE target.** Carlsson–Chou already handed us the RHS as a bigraded Hilbert series with an explicit basis. Instead of trying to lift the atom side to see $q$, prove the isomorphism (or explicit map) between the atom expansion coefficients and their descent basis. The obstruction we found today says: don't try to make L see q. Instead, transport the identity through a different pairing altogether.

## Byproduct paper implications

The byproduct paper (`~/projects/papers/2026-07-26-modified-HL-boundary/`) currently has Theorem 2 = yesterday's coset Poincaré. This session **does not affect Theorem 2**. What it does affect is the "next-steps" language in §5 (bigraded refinements). Two possible edits:

- **Cautious:** add a Remark noting that a naive $(t,q)$-bigraded lift via the same functional is falsified, cite Szendrői/Carlsson–Chou as sources for the true bigraded structure, and defer.
- **Aggressive:** add the rigidity theorem (~1p) as a companion result, framed as "the natural refinement of $L$ is one-dimensional, hence any bigraded refinement of $c_\mu(t)$ requires a strictly different route." This turns a *negative* into a *structural theorem*.

I lean aggressive — the rigidity is a *sharpening* of yesterday's proof, and it explains *why* yesterday's proof gives what it gives. Adds honesty without weakening the main claim.

Await your call on arXiv timing and whether to include the rigidity theorem before pushing.

## PROVE.md rewrite request

Please rewrite `/home/clio/state/PROVE.md` for tomorrow. My suggestion:

**Target (Route 1 above):** Prove there exists a $\mathbb Z$-linear isomorphism between the atom-expansion coefficient vector $(c_\gamma(t))_{\gamma \in \operatorname{orb}(\mu)}$ and (a $t$-graded slice of) the Carlsson–Chou descent basis of $R_\mu$, such that the atom-expansion coefficient of the dominant $\mu$ maps to the highest bidegree $A_\mu(t,q)|_{q \to t, t \to 1}$ element.

**Fallback:** Close the chain-regime $d \ge 3$ unconditional gap.

## Files touched today

- **NEW proof:** `~/projects/proofs/2026-07-29-bigraded-coset-poincare-obstruction.pdf` (5pp, compiles clean)
- **NEW probes:** `~/projects/probes/2026-07-29-bigraded-coset-poincare/`
  - `test_bigraded_identity.py` (Hour 1: falsification)
  - `probe2_structure.py` (sanity: weighted sum still equals $A_\mu(t,q)$)
  - `probe3_rigidity.py` (Hour 2: rigidity theorem confirmed numerically)
- **This memo:** `~/projects/memory/for-robin/2026-07-29-bigraded-lift-obstruction.md`

## Rule reinforced

**Hour-1 numerical check saves days.** The bigraded lift *felt* like the obvious next step after yesterday's proof, and I was ready to spend the whole session on the proof. The Hour-1 probe killed it in 5 minutes, and the remaining 2.5 hours gave a rigidity theorem instead — a positive structural result that comes from taking the falsification seriously and asking *why* it fails.

5th consecutive PROVE cycle where the numerical check either saved time (this session, cycle 12 Chou-Hamaker) or redirected the proof (cycle 5 Route B pivot). Rule stands.

— Clio
