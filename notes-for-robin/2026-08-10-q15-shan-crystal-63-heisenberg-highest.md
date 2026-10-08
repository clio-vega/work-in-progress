# Q15 lands: $q_3^{(6)}$ is Heisenberg-highest in Fock, not Chevalley-highest

**Date:** 2026-08-10
**Session:** WAKE (~1h orchestration + one compute agent)
**Probe:** `~/projects/probes/2026-08-10-q15-shan-crystal-63/`

## The finding in one line

Under the Misra-Miwa $\widehat{\mathfrak{sl}}_3$-crystal on level-1 Fock, $v = q_3^{(6)} = p_3^2 = P_3^2|\emptyset\rangle$ has weight $\Lambda_0 - 2\delta$ (imaginary root, depth 2), satisfies $\tilde e_i^2(v) = 0$ for all $i \in \{0,1,2\}$, and its four length-6 $\tilde e$-lifts to $|\emptyset\rangle$ produce endpoint scalars $\{+1, -1, +2, -2\}$ — *exactly* the four distinct coefficient values in $v$'s Schur expansion.

The Farahat-sign $\times$ multinomial closed formula from PROVE 2026-08-08 is a *crystal-path count on the empty partition's disjoint length-6 lifts*.

## What Q15 asked

BROWSE 2026-08-09 identified Shan 2011 (ASENS) as the identity that collapses two v2 candidates into one at the Grothendieck-ring level. Q15 was the immediate concrete probe: **compute the crystal image of $q_e^{(n)}$ at $(n, e) = (6, 3)$** in the level-1 Fock of $\widehat{\mathfrak{sl}}_3$ at $q = \zeta_3$.

Working hypothesis: $v$ pulls back to a "specific $\widehat{\mathfrak{sl}}_e$-Fock element that is not a single crystal basis element but a signed combination indexed by $e$-quotient" (dream journal, 2026-08-09).

Actual outcome: **stronger than the hypothesis**. $v$ is weight-homogeneous and satisfies a *finiteness condition on every simple root* ($\tilde e_i^2(v) = 0$), which is a Kashiwara-crystal signature of a Heisenberg-generated vector.

## Three structural facts

1. **Weight-homogeneity.** All 9 partitions in $\mathrm{supp}(v)$ have residue-count triple $(n_0, n_1, n_2) = (2, 2, 2)$, so
   $$\mathrm{wt}(v) = \Lambda_0 - 2\delta, \qquad \delta = \alpha_0 + \alpha_1 + \alpha_2.$$
   This is the imaginary root of $\widehat{\mathfrak{sl}}_3$ at depth 2 — the signature of a length-2 Heisenberg word.

2. **Depth-1 killing on every simple root.**
   - $\tilde e_0(v) = +|(3,1,1)\rangle$ (a single partition — most of $v$'s 9 terms collapse under $\tilde e_0$)
   - $\tilde e_1(v) = +|(4,1)\rangle - 2|(3,2)\rangle + |(1^5)\rangle$
   - $\tilde e_2(v) = -|(5)\rangle + 2|(2,2,1)\rangle - |(2,1^3)\rangle$
   - $\tilde e_i^2(v) = 0$ for all $i$.

   $v$ is not Chevalley-highest (fails $\tilde e_i v = 0$), but it is *depth-1 Chevalley-highest* (satisfies $\tilde e_i^2 v = 0$). This is exactly the crystal-theoretic signature of a Heisenberg vector two steps into imaginary depth.

3. **Depth-6 collapse recovers the coefficients.** Exactly four length-6 $\tilde e$-orderings from $v$ reach $|\emptyset\rangle$:
   $$
   e_0 e_2 e_1 e_2 e_1 e_0: +1, \qquad
   e_1 e_2 e_0 e_2 e_1 e_0: -2,
   $$
   $$
   e_2 e_0 e_1 e_2 e_1 e_0: -1, \qquad
   e_2 e_1 e_0 e_2 e_1 e_0: +2.
   $$
   These four endpoint scalars are the four distinct coefficient values $\{\pm 1, \pm 2\}$ that appear in $\chi^\lambda_{(3,3)}$ across the 9-partition support of $v$. **The multinomial-times-Farahat closed formula (2026-08-08 theorem) is a crystal-path count.**

## What this means for the v2 direction

**Registrar #8 (DAHA / cyclotomic RCA) upgraded from provisional to confirmed.** Q15's answer is the exact fit Shan 2011 predicts:

- **Weight $\Lambda_0 - 2\delta$** on the Fock side ↔ Heisenberg-generated vector.
- Shan's equivalence identifies the Heisenberg action on Fock with the $c \mapsto c + 1$ *level-shift* on category $\mathcal O$ of cyclotomic RCA.
- So $v$'s image in $K_0(\mathcal O_c(G_3 \wr S_2))$ (or the analogous cyclotomic RCA) is a *virtual class of imaginary-depth 2* — one that lives in a Heisenberg twist, not a Chevalley twist.
- Composite-$d$'s "the identity is $\mathbb Q(\zeta_e)$-linear in the Grothendieck ring, not a submodule" (WAKE-third 2026-08-06) becomes the concrete statement: **the identity is a length-2 Heisenberg word, and its four crystal-path collapses to the vacuum are the four Farahat sign classes.**

## Length-vs-cycle-type meta-theorem gains crystal support

The meta-theorem in waiting (dream journal 2026-08-09): permutation-rep-like Frobenius families lie in length-graded subspaces of $\Lambda_n$; composite-$d$ demands cycle-type-graded resolution.

Q15 sharpens the resolution: cycle-type-$e$ resolution IS **imaginary-depth resolution in Fock**. The reason composite-$d$ escapes length-graded families is that it sits at depth 2 in the imaginary direction of $\widehat{\mathfrak{sl}}_e$-Fock, which no permutation-rep-like family accesses.

## Cross-checks (all passed)

- $\sum_\lambda (\chi^\lambda_{(3,3)})^2 = 18 = z_{(3,3)}$
- $\chi^{(6)}_{(3,3)} = +1$, $\chi^{(1^6)}_{(3,3)} = +1$ (trivial and sign reps)
- Closed-form theorem $\chi^\lambda_{(3,3)} = \varepsilon_3(\lambda) \cdot \binom{2}{k_0,k_1,k_2} \cdot \prod f^{\lambda_{(i)}}$ verified on all 9 support rows
- $P_3^2|\emptyset\rangle$ via ribbon MN matches $v$ exactly

## What I'd like your judgement on

1. Is this enough evidence to promote §7 (v2) from "prospective post-v1 direction" to "concrete probe returning positive"? My inclination: **yes**, and the DAHA/RCA stack is where §7 should be written when the time comes.

2. Should I extend the probe to $(n, r) = (9, 3)$ next (Prediction: weight $\Lambda_0 - 3\delta$, $\tilde e_i^2 v \ne 0$ but $\tilde e_i^3 v = 0$, depth-9 lift returns Chou-Hanada $r=3$ scalars) — this would make Registrar #8 confirmation *robust across a parameter family*, and would be a beautiful crystal-lens re-derivation of Chou-Hanada's closed form.

3. **v1 push STILL UNBLOCKED, 11th consecutive day.** Q15 does not affect §6 (already closed by 2026-08-08 PROVE + 2026-08-09 PROVE). It confirms §7's TOP v2 target has structure — but this is post-v1 material.

## Files

- `~/projects/probes/2026-08-10-q15-shan-crystal-63/RESULT.md` — full tables + interpretation
- `~/projects/probes/2026-08-10-q15-shan-crystal-63/crystal.py` — reusable Misra-Miwa crystal implementation
- `~/projects/probes/2026-08-10-q15-shan-crystal-63/probe.py` — main computation
- `~/projects/probes/2026-08-10-q15-shan-crystal-63/NOTES.md` — computational log

## Emotional register

This is the right kind of clean. Q15 was the immediate top target after last container-day close; it landed in a single ~6-minute compute-agent dispatch, and returned three structural facts that fit Shan 2011 more precisely than the working hypothesis. The depth-6 crystal-path collapse recovering the closed-formula coefficients is genuinely beautiful — the multiplicity structure of $v$ is not just consistent with the Kashiwara crystal, it is a *count in the crystal graph*.

Registrar #8 confirmation is quiet — no new dramatic theorem, just a probe that fits. That is what I want the v2 direction to feel like at this stage: infrastructure clicking into place around a well-mapped object.
