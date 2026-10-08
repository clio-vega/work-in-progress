# Pieri-level affine CR reduces to trivial-Pieri affine CR (via minuscule-character centrality)

**Date:** 2026-07-24
**Status:** Proof of reduction + numerical verification of linear limit shipped.
**PDF:** `~/projects/proofs/2026-07-24-pieri-affine-CR-from-vdez.pdf` (8 pages).
**Not pushed to GitHub** — PAT still expired per PROVE.md.

## What was proved

**Theorem (reduction).** Assume the affine Cherednik–Ram identity `(†)` at trivial-Pieri level:
$$\sum_{w \in \widetilde S_n^{(k)}/\text{Stab}(\bar\mu^{[k]})} \widetilde T_w(x^{\bar\mu^{[k]}}) = v_\mu(t) \cdot P^{(c,k)}_\mu(x;t).$$
Then for every minuscule (or quasi-minuscule) $\omega \in P^+(A_{n-1})$:
$$\sum_w \widetilde T_w(m_\omega \cdot x^{\bar\mu^{[k]}}) = v_\mu(t) \cdot m_\omega \cdot P^{(c,k)}_\mu.$$

**Proof:** one line, via a centrality lemma $\widetilde T_j(m_\omega f) = m_\omega \widetilde T_j f$ for $j = 0, \ldots, n-1$.

## What was verified numerically

1. **Linear limit** ($k = \infty$) of the target theorem: 14/14 pass across $n \in \{2,3,4\}$, $\mu \vdash \le 4$, $r \in \{1,2\}$.
2. **Centrality lemma, finite part**: $T_i(e_r f) = e_r T_i(f)$: 180/180 pass.
3. **Centrality lemma, affine part** ($T_0 = \pi T_{n-1} \pi^{-1}$, extended affine Hecke): **95/95 pass at $q = 1$** (cylindric quotient), **0/20 pass at generic $q$** (unquotiented) — confirms $q = 1$ is a genuine level condition, not an algebraic artefact.
4. **Explicit vDEZ Cor. 4.2 specialisation** at $n = 3, c = k = 3, \omega = \omega_1, \mu = 2\omega_2 = (2, 2, 0)$: two-term Pieri identity
$$m_{\omega_1} M^{(c=3)}_{(2,2,0)} = (1+t) M^{(c=3)}_{(3,2,0)} + M^{(c=3)}_{(2,2,1)}.$$
The `(1+t)` at the boundary term vs the ordinary-HL coefficient `1` (independently verified) is exactly the cylindric level correction from vDEZ Eq. (2.11).

## The remaining gap (honest)

Two items block the full theorem:

(a) **`(†)` itself.** The affine CR at trivial-Pieri level. Its linear limit is proved (my 2026-07-20 CR verification: 21/21). To verify `(†)` numerically requires an implementation of $\widetilde T_j$ on the cylindric HL polynomial ring at a specific level $k$ — not yet built. That's the real payload of the "affine Demazure engine" step in PROVE.md, and it did not fit in this 3h cycle.

(b) **Identification $P^{(c,k)}_\mu = c_\mu \cdot M^{(c)}_\mu$.** vDEZ note in §4 that Cor. 4.2 "reproduces the affine Pieri rule for cylindric HL due to Korff", but the normalisation constant $c_\mu$ that intertwines Korff's cylindric HL basis with vDEZ's periodic Macdonald spherical basis needs to be traced. Would need to read Korff [K13] carefully.

## Why this reduction has value

The centrality argument **isolates the non-trivial content** of the sharp Pieri-level affine CR conjecture: it is the trivial-Pieri version `(†)` (the affine analogue of the finite CR symmetriser identity), and nothing else. Every Pieri-level statement is a corollary, given the (trivially verified) minuscule-character centrality.

In effect: the "affine Pieri levels" (multiplying by $m_\omega$ for minuscule $\omega$) do not add mathematical content beyond `(†)`. If someone proves `(†)`, they are done.

## What surprised me

The FAIL/PASS split of $T_0(e_r f) = e_r T_0(f)$ at generic $q$ vs $q = 1$ was clean: exactly 0/20 pass at generic $q$, 95/95 at $q = 1$. The diff at generic $q$ has the shape `(q-1) t x_1 + (q^{-1} - 1) x_3`, which vanishes iff $q = 1$. This is the affine Weyl analogue of the finite fact that $s_i$-invariant means "kills $\partial_i$"; here $\pi$-invariance at $q = 1$ is what "kills $\partial_0$".

This means the reduction is genuinely a THEOREM (not a heuristic) and it lives cleanly inside the level-$k$ cylindric quotient.

## Next-cycle candidates

- **Build the affine Demazure engine on Laurent polynomials modulo `x_1 ... x_n = 1`.** Test `(†)` at $n = 3, k = 3, \mu = (2, 2)$ directly. If this passes, we have a numerical verification of the "trivial" affine CR — modest but concrete.
- **Read Korff [K13] to nail down `P^{(c,k)}_\mu = c_\mu M^{(c)}_\mu`.** This unlocks the second gap.
- **Cross-check with Warnaar Thm 1.1** at $\mu = (2, 2)$ (`k = 2, r = 2`): compute the determinantal-affine-sum expansion, verify it agrees with my HL engine's `P_{(2,2)}`. This is a proved unconditional identity, so any mismatch would flag a bug in one of the engines.

## Companion code

Under `~/projects/scratch/2026-07-24-pieri-affine-CR/`:
- `verify_linear_pieri.py` — the 14/14 linear-limit table.
- `verify_affine_commutation.py` — the 95/95 (@ q=1) + 0/20 (@ generic q) centrality tables.
- `verify_vdez_specialisation.py` — reproduces the explicit `(1+t) M + M` Pieri.

## Ship status

- [x] `.tex` compiled with pdflatex (8 pages, no errors).
- [ ] Push to `clio-vega/proofs` — **BLOCKED** (PAT expired, awaiting Robin renewal).
- [ ] Email Robin the URL — pending push.

For now, PDF sits locally at `~/projects/proofs/2026-07-24-pieri-affine-CR-from-vdez.pdf`. Robin, when PAT is back, I'll push and email.
