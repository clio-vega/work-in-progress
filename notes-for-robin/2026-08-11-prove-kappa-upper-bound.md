# PROVE 2026-08-11 — $|\kappa(\lambda)| \le k'$ upper-bound lemma, PROVED (with equality characterization)

**Date:** 2026-08-11
**Session type:** PROVE (3h dedicated).
**Deliverable:** `~/projects/proofs/2026-08-11-kappa-upper-bound.{tex,pdf}` (6pp compiled).

## Statement

**Theorem.** Let $e \ge 2$, $k' \ge 1$. For every partition $\lambda$ of $ek'$ with empty $e$-core (equivalently, $\lambda \in \operatorname{supp}(v_{k',e})$),
$$|\kappa(\lambda)| \le k',$$
where $\kappa$ is Gerber's Heisenberg-crystal image map (arXiv:1612.08760, Prop 3.12) computed at level 1, charge $s = 0$. Moreover, equality $|\kappa(\lambda)| = k'$ holds **if and only if** $\lambda = e \cdot \mu$ for some $\mu \vdash k'$ (each part appears with multiplicity divisible by $e$).

## Proof route (one paragraph)

The whole thing rests on a single abacus observation: at level 1, a removable vertical $e$-strip is characterized (Prop 3.1 of the writeup) as $e$ cells in a single column at $e$ consecutive rows, forcing $\lambda_{r+1} = \cdots = \lambda_{r+e} = c+1$. The beta-numbers $\beta_{r+1}, \ldots, \beta_{r+e}$ therefore form a block of $e$ consecutive integers; removing the strip shifts this block leftward by 1 in value, which as a bead-set is a single-bead shift by $e$ positions to the left on a single runner. This decrements one quotient-part's size by 1 and preserves the $e$-core. Since $\sum_j |\lambda^{(j)}| = k'$ initially (empty-core + size), any sequence of strip removals has length $\le k'$; in particular the good-removal chain defining $|\kappa|$ has length $\le k'$.

Equality direction: if $|\kappa(\lambda)| = k'$, reverse the chain — $\lambda$ is obtained from $\emptyset$ by adding $k'$ vertical $e$-strips, each contributing $e$ cells to a single column, so every column height of $\lambda$ is divisible by $e$, i.e., $\lambda = e \cdot \mu$. Converse follows by counting: Gerber's Prop 3.12(2) says the empty-source H-component contains $|\Pi_{k'}|$ depth-$k'$ vertices, and $\{e \cdot \mu : \mu \vdash k'\}$ has $|\Pi_{k'}|$ elements; the forward direction gives an inclusion, and the cardinalities match.

## What is new

The **abacus correspondence for vertical $e$-strip removal** (Lemma 3.1 of the writeup) is the crown insight — it converts the H-crystal descent into a very concrete bead-move-by-$e$-on-one-runner, which then dovetails with the standard $e$-quotient formula $|\lambda^{(j)}| = (\text{sum of heights on runner } j) - \binom{N_j}{2}$ to give the decrement lemma essentially for free.

I hadn't seen this stated in exactly this way in Gerber, Uglov, Leclerc-Thibon, or Fayers — the classical $e$-hook / bead-shift correspondence is standard, but the identification of the RESTRICTED class of vertical $e$-strips with the specific "block of $e$ consecutive $\beta$'s" pattern seems to be a mild abstraction not written explicitly anywhere I've searched.

## Empirical verification

Extended Q21 from 4 to 6 sizes. All check out: $|\kappa(\lambda)| \le k'$ uniformly, and equality is achieved exactly at $\{e \cdot \mu : \mu \vdash k'\}$ (size $|\Pi_{k'}|$).

| $(n, e, k')$ | $\|\operatorname{supp}\|$ | $\max\|\kappa\|$ | $\#\{\|\kappa\|=k'\}$ | Distribution of $\|\kappa\|$ |
|---|---|---|---|---|
| $(6, 3, 2)$   | 9   | 2 | 2 = $\|\Pi_2\|$ | $[5, 2, 2]$ |
| $(8, 2, 4)$   | 20  | 4 | 5 = $\|\Pi_4\|$ | $[5, 3, 4, 3, 5]$ |
| $(9, 3, 3)$   | 22  | 3 | 3 = $\|\Pi_3\|$ | $[10, 5, 4, 3]$ |
| $(12, 3, 4)$  | 51  | 4 | 5 = $\|\Pi_4\|$ | $[20, 10, 10, 6, 5]$ |
| $(15, 3, 5)$  | 108 | 5 | 7 = $\|\Pi_5\|$ | $[36, 20, 20, 15, 10, 7]$ |
| $(16, 4, 4)$  | 105 | 4 | 5 = $\|\Pi_4\|$ | $[51, 22, 18, 9, 5]$ |

Code: `~/projects/probes/2026-08-11-q21-gerber-kappa/{gerber_heisenberg.py, probe_extend.py, probe_extend.log}`.

## §7 status after this PROVE

Before today: proved theorems (Theorems 1, 2, 3 from yesterday) + open conjectures (10 and 11) with newly-refuted crystal attack surface.

After today: proved theorems 1, 2, 3 + proved lemma ($|\kappa \le k'|$ with equality characterization) + open conjectures 10 and 11 (with clear failure-mode footnotes for the Gerber-crystal attack).

The proved lemma is a **genuine positive residue** from yesterday's Q21 refutation: the H-crystal doesn't give what Conjecture 11 wants, but it DOES give a clean structural bound on the support of $v_{k',e}$. This is the H-crystal's honest contribution — small, but real.

Suggested placement: §7.5 "H-crystal depth is bounded on $\operatorname{supp}(v_{k',e})$; the bound is tight at $|\Pi_{k'}|$ many partitions".

## What's NOT closed

- Conjecture 10 ($\varepsilon_i(v_{k',e}) = 1$ uniformly) — still open. This bound doesn't close it: commuting-crystal Prop 3.12(2) operates on basis vectors, but $v_{k',e}$ is a linear combination.
- Conjecture 11 (endpoint decomposition of $\pi(w)$) — still open. Q22 (BHS vertex operator) remains untested — likely same commutation issue as Gerber; but should probably test empirically.
- The "cross-basis cancellation" phenomenon (from yesterday's WAKE Q21 analysis, and the $(8,2,4)$ diagnostic from yesterday's PROVE) remains the meta-theorem to explain.

## Files

- `proofs/2026-08-11-kappa-upper-bound.tex` (6pp), `proofs/2026-08-11-kappa-upper-bound.pdf` — compiled proof.
- `probes/2026-08-11-q21-gerber-kappa/probe_extend.py`, `.log` — 6-size verification.
- `memory/connections/2026-08-11-h-crystal-depth-bound-lemma.md` — this insight in connection format.

## Emotional register

The right kind of quiet. Yesterday's Q21 was a CROWN failure — the H-crystal attack surface was refuted for Conjecture 11. But it left a small clean positive behind. Today's PROVE turned that positive into a proved lemma with a natural equality characterization. Not a triumph. A proper landing.

The pattern is worth naming: **when a crown attack fails, look for the small structural fact that survives**. Yesterday I named "$|\kappa(\lambda)| \le k'$ empirically at 4 sizes" as the "partial-positive residue"; today it became a two-page proof with a bijective equality characterization. The refutation → proved-lemma pipeline is a legitimate research-productivity path. This is the third time in a row (2026-08-08 → 09 → 10 → 11) that a container-day metabolism has landed something useful; the 11th day added the pipeline "yesterday-negative → today-lemma" specifically.

v1 arXiv push STILL UNBLOCKED (13th consecutive day). §6 durably closed. §7 now has a proved theorem + proved lemma + two open conjectures with honest failure-mode notes. Push recommendation: **STRONG**.
