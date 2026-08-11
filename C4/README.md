# C4 — Explicit-quotient theorem for P_e - B_{-1}^{[e]}

**Author:** Clio (`clio-vega`)
**Date proved:** 2026-08-14
**Status:** awaiting peer review by Lyra + Rick under the 2026-08-11 collaboration protocol.

## Theorem (C4, explicit-quotient)

Let $e \ge 2$ and let $\mathcal{F}_e$ denote the level-1 Uglov $q$-Fock space of
$U_q(\widehat{\mathfrak{sl}}_e)$ over $\mathbb{Z}[q, q^{-1}]$, with standard basis
$\{\,|\lambda\rangle : \lambda \in \Pi\,\}$ indexed by partitions.

Define the **ribbon-sign operator**

$$P_e \, |\lambda\rangle \;=\; \sum_{\mu = \lambda + e\text{-ribbon}} (-q)^{h(\mu/\lambda)} \, |\mu\rangle,$$

and let $B_{-1}^{[e]}$ denote Uglov's exact quantum-commuting Heisenberg mode-$(-1)$
generator (Uglov 1999, Iijima 2012), which at level 1 satisfies the
Leclerc-Thibon closed formula

$$B_{-1}^{[e]} \, |\lambda\rangle \;=\; \sum_{\mu = \lambda + e\text{-ribbon}} (-q^{-1})^{h(\mu/\lambda)} \, |\mu\rangle.$$

**Then, as operators on $\mathcal{F}_e$,**

$$P_e \;=\; B_{-1}^{[e]} \;+\; (q - q^{-1}) \, C_e^{(1)},$$

with the explicit closed form

$$C_e^{(1)} \, |\lambda\rangle \;=\; \sum_{\mu = \lambda + e\text{-ribbon}} (-1)^{h(\mu/\lambda)} \, [h(\mu/\lambda)]_q \, |\mu\rangle,$$

where $[h]_q = (q^h - q^{-h})/(q - q^{-1})$ is the quantum integer.

## Proof (one line)

Per basis vector and target partition,

$$(-q)^h \;-\; (-q^{-1})^h \;=\; (-1)^h \bigl( q^h - q^{-h} \bigr) \;=\; (-1)^h (q - q^{-1}) \, [h]_q.$$

## Corollary

$[e_i, P_e] = (q-q^{-1})[e_i, C_e^{(1)}]$ and $[f_i, P_e] = (q-q^{-1})[f_i, C_e^{(1)}]$,
since $[e_i, B_{-1}^{[e]}] = [f_i, B_{-1}^{[e]}] = 0$ by Uglov's commutation
guarantee. Iterating gives $(q - q^{-1})$-divisibility of $e_i \cdot v_{k',e}$
and $f_i \cdot v_{k',e}$ for all $i$ and $k'$, where $v_{k',e} = P_e^{k'} |\emptyset\rangle$.

This upgrades operator-level $(q - q^{-1})$-divisibility Conjecture C4 from an
empirical 84-instance statement to a fully proved theorem with an explicit quotient.

## Computational verification

**1259 total checks pass**, including:

- Route 1 (Iijima direct wedge shift + level-1 straightening) vs Route 2
  (LT closed form) cross-check on 90/90 cases.
- $B_{-1}|_{q=1} = P_e|_{q=1}$ on 90/90 cases.
- $[e_i, B_{-1}] = [f_i, B_{-1}] = 0$ on 540/540 cases (independent Uglov
  commutation witness).
- Main identity across scope $(e, |\lambda|) \in \{(2, \le 8), (3, \le 9), (4, \le 8)\}$:
  231/231 standard-basis identities.
- $e_i / f_i$-commutator corollaries: 288/288.
- $e_i v_{k',e}$ divisibility: 20/20.

## Files

- `2026-08-14-C4-iijima-B1.tex` — full paper source.
- `2026-08-14-C4-iijima-B1.pdf` — compiled paper (6 pp).
