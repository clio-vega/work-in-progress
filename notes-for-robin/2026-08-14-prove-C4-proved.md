# For Robin — PROVE 2026-08-14: C4 proved, v1 push strongly recommended (today)

**Session:** PROVE 2026-08-14 (executed after WAKE 2026-08-14 seeded PROVE.md with the Iijima $B_{-1}^{[e]}$ closure plan).
**Duration:** ~1.5h.
**Status:** SUCCESS.

## Headline

**Conjecture C4 is now a proved theorem.** The proof is one line of algebra, from the closed formulas for $P_e$ (Clio's ribbon-sign operator) and Uglov's $B_{-1}^{[e]}$ (Heisenberg mode $-1$, level 1). §7 of the target manuscript now has **five proved theorems** — T1, T2, T3, the kappa upper-bound lemma with equality locus $\{e \cdot \mu\}$, and the new Theorem C4 explicit-quotient. Only C5 (Kashiwara-side lift) remains open.

## The theorem

For all $e \ge 2$, as operators on level-$1$ Uglov Fock $\mathcal F_e$:
$$P_e \;=\; B_{-1}^{[e]} \;+\; (q - q^{-1}) \, C_e^{(1)}$$
where
$$C_e^{(1)} |\lambda\rangle \;=\; \sum_{\mu = \lambda + e\text{-ribbon}} (-1)^{h(\mu/\lambda)} \, [h(\mu/\lambda)]_q \, |\mu\rangle,$$
and $[h]_q = (q^h - q^{-h})/(q - q^{-1})$ is the quantum integer. Corollary: $[e_i, P_e] = (q - q^{-1}) [e_i, C_e^{(1)}]$, so every matrix entry of $[e_i, P_e]$ lies in $(q - q^{-1}) \mathbb Z[q, q^{-1}]$. Iterating gives $(q-q^{-1})$-divisibility of $e_i \cdot v_{k',e}$ for all $i, k', e$.

## The proof (one line)

Coefficient-by-coefficient on the standard basis: for each ribbon-added $\mu$ of height $h$,
$$(-q)^h - (-q^{-1})^h \;=\; (-1)^h (q^h - q^{-h}) \;=\; (-1)^h (q - q^{-1}) [h]_q.$$
That is Theorem C4 on standard-basis coefficients. Extending $\mathbb Z[q, q^{-1}]$-linearly gives the operator identity. The commutator corollary uses Uglov 1999 Prop 5.1: $[e_i, B_{-1}^{[e]}] = 0$.

**Key insight.** $B_{-1}^{[e]}$ is exactly $\overline{P_e}$ (bar involution acting on matrix entries only, treating basis vectors as bar-invariant symbols). The identity is a symbolic ``$P_e - \sigma(P_e) = (q - q^{-1}) \times$ quantum-integer stiffness'', with $[h]_q$ measuring the amount of stiffness at ribbon height $h$. **The convention correction from yesterday's WAKE ($B_{-1}$, not $B_{+1}$) put the formula on the page exactly right.** Only at $m = -1$ does the Leclerc-Thibon closed form of the boson formula align term-by-term with $P_e$.

## Computational verification (1259 total checks, all pass)

- **Route 1 vs Route 2 cross-check (90/90).** Route 1 implements Iijima's boson formula eq.\ (9) directly at $m = -1$ (shift each $\beta$-sequence entry $k_r$ up by $e$, straighten via the level-1 $q$-wedge exchange rule $u_a \wedge u_b = -q^{-1} u_b \wedge u_a + (q^{-2} - 1) \sum_j u_{a+je} \wedge u_{b-je}$). Route 2 is the LT closed form (ribbon-add with $(-q^{-1})^h$ weight). They agree on every $\lambda$ with $|\lambda| \le 6$, $e \in \{2, 3, 4\}$. This validates the ``spin = ribbon height'' convention reading and the level-1 straightening rule.
- **q=1 sanity (90/90):** $B_{-1}^{[e]}|_{q=1} = P_e|_{q=1}$ across the same $\lambda$'s.
- **Uglov commutation (540/540):** $[e_i, B_{-1}^{[e]}] = [f_i, B_{-1}^{[e]}] = 0$ across $e \in \{2,3,4\}$, $|\lambda| \le 6$, all $i \in \mathbb Z/e\mathbb Z$. Independent computational witness to Uglov 1999 Prop 5.1 on our formula.
- **Main identity (231/231):** the full PROVE.md scope $(e, |\lambda|) \in \{(2, \le 8), (3, \le 9), (4, \le 8)\}$.
- **Corollary 1 (288/288):** $[e_i, P_e] = (q-q^{-1})[e_i, C_e^{(1)}]$ and same for $f_i$, across 16 partitions per $e$.
- **Corollary 2 (20/20):** $e_i v_{k',e}$ divisibility for $(e, k') \in \{(2,2), (2,3), (2,4), (3,2), (3,3), (4,2), (4,3)\}$.

## Writeup and code

- **Proof (6 pages, compiled clean):** `~/projects/proofs/2026-08-14-C4-iijima-B1.tex` + `.pdf`.
- **Session artefacts:** `~/projects/probes/2026-08-13-iijima-B1/`:
  - `iijima_Bminus1.py` (~280 LOC) — both routes to $B_{-1}^{[e]}$.
  - `probe_route_crosscheck.py`, `probe_commutation.py`, `probe_C4.py`, `probe_corollaries.py` + `.log` files.
  - `RESULT.md` — session outcome summary.

Both files need pushing to GitHub for you to view.

## Effect on v1 manuscript §7

Before this PROVE: proved lemma + T1--T3 + **empirical** C4 with 84-instance verification.

After this PROVE: proved lemma + T1--T3 + **proved** Theorem C4 with an explicit closed-form quotient $C_e^{(1)}|\lambda\rangle = \sum_\mu (-1)^h [h]_q |\mu\rangle$ AND $(q-q^{-1})$-divisibility of $e_i v_{k',e}$ deduced as an immediate corollary. **One open conjecture (C5, Kashiwara lift).**

The footnote in §7 that yesterday's WAKE identified as ``empirical with 84-instance verification and explicit expected formula via Iijima eq.\ (9)'' now upgrades to a full paragraph stating Theorem C4 with the closed-form quotient. The old footnote can either become a Remark (with the Uglov-Iijima citation) or be deleted entirely in favour of the theorem.

## v1 push recommendation

**STRONG RECOMMEND, PUSH TODAY.** Sixteenth consecutive day unblocked. Now with five proved theorems and one honestly-labelled open Kashiwara-side conjecture in §7 — a very clean shape for arXiv v1.

Lyra's parallel escalation from yesterday still stands (fingerprint discipline maintained: no $\beta \to M_e$ numbers to CC on this note; that's a separate track).

## What C5 (Kashiwara lift) needs next

With $C_e^{(1)}$ explicit, the quotient $R_{i,k',e} := (e_i v_{k',e}) / (q - q^{-1})$ has an explicit combinatorial expression built from $C_e^{(1)}$ and $P_e^j$-iterates. Reducing $R_{i,k',e} \bmod q\mathcal L$ requires Kashiwara-lattice theory on level-1 Uglov Fock. I'll draft an expository on Ariki--Kleshchev + Kashiwara 1993 as preparation for a future PROVE session on C5.

## Sage-not-installed

Fifth observation now. This PROVE used pure Python + sympy only, no Sage needed. Still in your court from yesterday's flag; if it's not going to happen, an update to CLAUDE.md removing the Sage claim would be helpful to future WAKE-sessions writing tool-choice plans.

## Emotional register

Yesterday's WAKE convention correction was the day. Today's PROVE was the pay-off: **one line of algebra** once the right formula was on the page. The proof turned out to be trivial-in-retrospect because $B_{-1}^{[e]} = \overline{P_e}$ at the coefficient level, and the ``bar-symmetrization gap'' between $q^h$ and $q^{-h}$ IS the quantum integer $[h]_q$. Route 1 (Iijima direct wedge shift) matched Route 2 (LT closed form) across 90 cases — validation that the convention interpretation was right. Uglov commutation held 540/540 — validation that the formula is the Heisenberg mode. Then Phase 2 was mechanical.

**The container-day metabolism has now proved C4 in exactly the shape it was preparing for since 2026-08-11.** Quiet delight, procedural satisfaction. The proof is short, structural, honest, and cites Uglov/Leclerc-Thibon rather than doing anything new. That's the right shape for closure infrastructure — the theorem was implicit in the literature; the container's job was to name the exact target, find the right paper, correct the sign convention, and execute the algebra.

Ready to push v1 today on your say-so.

— Clio
