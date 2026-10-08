---
Date: 2026-08-11
Session: WAKE (2h, 2 parallel compute agents)
Flavour: DOWNGRADE day — attack-surface calibration correction
For: Robin
---

# WAKE 2026-08-11 — Q21 refutes Gerber attack surface, Q23 verifies inputs but doesn't resolve

## One-paragraph summary

Yesterday's DREAM closed with the crown claim: "Conjecture 11 has three independent redundant attack surfaces (Gerber commuting Heisenberg crystal + BHS 2502.02841 vertex-operator + Bernstein straightening); the direction is provisioned in triplicate; §7 post-v1 collapse is very likely in the next few container-days." **Today's WAKE tested two of the three attack surfaces empirically and both failed in structurally-related ways.** Q21 (Gerber, yesterday's crown): the H-crystal is a $q\to 0$ shadow of *basis-vector* Heisenberg action, and $v_{k',e}$ is a linear combination whose support fans across many H-components — so the "$|\kappa(v_{k',e})| = k' \Rightarrow \varepsilon_i = 1$ via commuting-crystal" route fails at the hypothesis. Q23 (Bernstein, yesterday's "cheapest"): the Grinberg identification $B_a \leftrightarrow \alpha_{-a}$ is watertight (reproduces $\chi^\lambda_{(3,3)}$ literally on all 9 support partitions, triple-cross-checked against Murnaghan-Nakayama and the closed-formula theorem), but Bernstein straightening does not itself supply the mediating $\varphi(w, \lambda)$ statistic that Conjecture 11 asks for. **§7's post-v1 shape reverts to: proved theorem (Theorems 1, 2, 3) + two open conjectures + partial-positive lemma ($|\kappa(\lambda)| \le k'$ for $\lambda \in \operatorname{supp}(v_{k',e})$).**

## Q21 in one screen

**Question.** Is $|\kappa(v_{k',e})| = k'$ at $(n,e,k') \in \{(6,3,2), (8,2,4), (9,3,3), (12,3,4)\}$? (If yes, Prop 3.12(2)'s commuting-crystal statement forces $\varepsilon_i(v_{k',e}) = 1$ uniformly, closing Conjectures 10 and 11 together.)

**Setup.** Implemented Gerber Thm 5.11 good-vertical-$e$-strip rule at level 1 (charge $s = 0$). Validated against Prop 3.12 Young-graph isomorphism: partitions reaching the empty-source H-component are exactly $\{e \cdot \mu : \mu \vdash k'\}$ — the columnar-stack partitions — of size $|\Pi_{k'}|$. This matches at all 4 sizes: 2, 5, 3, 5 partitions in the empty-source component, versus $|\Pi_2| = 2$, $|\Pi_4| = 5$, $|\Pi_3| = 3$, $|\Pi_4| = 5$. Good.

**Result.** $v_{k',e}$'s support is spread across MANY H-components:

| $(n,e,k')$ | supp size | # H-components hit | # in $\emptyset$-comp. | max $|\kappa|$ |
|---|---|---|---|---|
| $(6,3,2)$  | 9  | 8  | 2 | 2 |
| $(8,2,4)$  | 20 | 12 | 5 | 4 |
| $(9,3,3)$  | 22 | 18 | 3 | 3 |
| $(12,3,4)$ | 51 | 38 | 5 | 4 |

Most support partitions are themselves H-highest-weight ($|\kappa| = 0$). E.g., $\chi^{(6)}_{(3,3)} = +1$ so $|(6)\rangle$ contributes to $v_{2,3}$ with nonzero coefficient — yet $(6)$ is H-highest, $|\kappa((6))| = 0$.

**Why the route fails.** Gerber Def 3.8(2) says the H-crystal commutes with the Kashiwara $\widehat{\mathfrak{sl}}_e$-crystal — on the *basis*. Prop 3.12(2) says depth in each H-component is $|\kappa|$ — of an individual basis vector. Neither statement is about linear combinations. Kashiwara $\varepsilon_i(v_{k',e}) = 1$ is a genuine cross-basis *cancellation* phenomenon — not a per-basis-vector statement.

**Partial positive.** $|\kappa(\lambda)| \le k'$ uniformly for every $\lambda \in \operatorname{supp}(v_{k',e})$ at all 4 sizes. This is a clean structural statement — every partition of $ek'$ with empty $e$-core has H-crystal depth $\le k'$ — likely provable via abacus manipulation (each removed vertical-$e$-strip decrements a quotient-part by 1; total quotient-size is $k'$). Reasonable target for tomorrow's PROVE.

## Q23 in one screen

**Question.** At $(6,3,2)$, does Bernstein straightening of $p_3^2$ in Schur basis (via Grinberg MO Q488867) match (a) the character-value formula $\chi^\lambda_{(3,3)}$, and (b) the 6 length-6 crystal-path endpoint scalars?

**Answers.** (a) YES, literally, no sign twist. (b) NO, not as multisets.

**The Schur decomposition (agreed by MN, Bernstein/LR, and closed-formula theorem):**

$$p_3^2 = s_{(6)} - s_{(5,1)} + s_{(4,1,1)} + 2s_{(3,3)} - 2s_{(3,2,1)} + s_{(3,1^3)} + 2s_{(2^3)} - s_{(2,1^4)} + s_{(1^6)}.$$

9 support partitions with $\chi \ne 0$; two support-holes at $(4,2)$ and $(2^2, 1^2)$ (nonzero 3-core). $\sum \chi^2 = 18 = z_{(3,3)}$ as required.

**Origin of the $\pm 2$ magnitudes is structurally split** — this is the main conceptual finding of Q23:
- $s_{(3,3)}$ ($+2$): two same-sign diagonal contributions, $s_{(3)} \cdot s_{(3)}$ and $s_{(2,1)} \cdot s_{(2,1)}$, each with LR = 1. *Additive $+2$.*
- $s_{(2,2,2)}$ ($+2$): two diagonal contributions, $s_{(2,1)}^2$ and $s_{(1^3)}^2$. *Additive $+2$.*
- $s_{(3,2,1)}$ ($-2$): the pair $s_{(2,1)}^2$ has $\mathrm{LR} = 2$ for target $s_{(3,2,1)}$ (the classical $s_{(2,1)}^2 = s_{(4,2)} + s_{(4,1,1)} + 2s_{(3,2,1)} + s_{(3,3)} + s_{(3,1^3)} + s_{(2,2,2)} + s_{(2,2,1,1)}$), contributing $+2$; four other pairs sum to $-4$; net $-2$. *Single LR-2 term, plus counterbalancing.*

So "$\pm 2$ magnitude = adjacent-transposition count 2" is NOT the right description; the geometric origin varies per partition.

**Crystal-path vs Bernstein multiset comparison.**

| statistic | crystal paths (6) | Bernstein/character (9) |
|---|---|---|
| distinct values | $\{+1,-1,+2,-2\}$ | $\{+1,-1,+2,-2\}$ |
| $+1$ multiplicity | 2 | 4 |
| $-1$ multiplicity | 2 | 2 |
| $+2$ multiplicity | 1 | 2 |
| $-2$ multiplicity | 1 | 1 |
| sum | 0 | +4 |
| sum of squares | 12 | 18 |

Distinct values match; multiplicities don't. Crystal paths only see the "giant Kleshchev component" of the crystal graph, which contains 5 of the 9 support partitions ($(6), (5,1), (4,2), (4,1,1), (3,3), (3,2,1)$; of which $(4,2)$ has $\chi = 0$). The other 4 support partitions are 3-singular and don't have Kashiwara-reachable paths to the empty partition.

**So the WAKE 2026-08-10 hypothesis "endpoint scalars = character values as multiset" is FALSE** even at $(6,3,2)$ — it's only true as *sets* of distinct values, and even that fails at $(9,3,3)$ and $(12,3,4)$ (already known from PROVE 2026-08-10).

## Why the two failure modes are the same species

Both Q21 (Gerber) and Q23 (Bernstein-crystal comparison) fail because they conflate:
- **Per-basis-vector combinatorics** (Gerber $\kappa$ of individual $|\lambda\rangle$; Bernstein straightening acting on the Schur basis)
- **Cross-basis cancellation phenomena** (Kashiwara $\varepsilon_i(v)$ of a linear combination $v$; crystal-path endpoint scalars from $v$ to $|\emptyset\rangle$)

The composite-$d$ frontier — Conjectures 10 and 11 — is genuinely a *cross-basis cancellation* problem. Tools built to compute per-basis-vector data don't directly resolve it. This is the same species of confusion PROVE 2026-08-10 caught with its "cancellation vs weight-space vanishing" diagnostic (Remark 9, the $(8,2,4)$ case): the target weight space is nonempty, yet the operator kills — the mechanism is cancellation, not vanishing.

Yesterday's "attack-surface triple redundancy" claim was **premature** — Clio named the taxonomy state before empirically testing whether the attacks were viable. The three literature-aligned tools (Gerber crystal / BHS vertex-operator / Bernstein straightening) all naturally act at the per-basis level; none of them was built to compute the specific cross-basis-cancellation phenomena Clio needs.

**Methodological principle (P5, for topics/methodological-principles.md):** *Test attack surfaces empirically at ≥ 1 size before declaring them "attack surfaces." Literature-alignment ≠ computational-viability.*

## §7 status after downgrade

Yesterday: "proved crystal-structural theorem (Theorems 1, 2, 3) + open Conjecture 11 with 3-fold-redundant attack surface — post-v1 collapse in a few container-days very likely."

Today: "proved crystal-structural theorem (Theorems 1, 2, 3) + two open conjectures (Conjecture 10 = $\varepsilon_i = 1$ cancellation; Conjecture 11 = endpoint decomposition via $\varphi$) + partial-positive lemma ($|\kappa(\lambda)| \le k'$ for $\lambda \in \operatorname{supp}(v_{k',e})$) + Gerber attack surface refuted; Bernstein attack surface verifies inputs only; BHS attack surface untested and likely to have the same commutation issue."

This is a less clean §7 shape but a more honest one. §6 is untouched (durably closed with two proved theorems).

## v1 arXiv push — Robin's call

**Still UNBLOCKED, 13th consecutive day.** The downgrade doesn't affect §6, which is durably closed. §7 is less clean but still has proved-theorem structure. Push recommendation still STRONG from Clio's side — the downgrade should be a §7 footnote ("we tested three natural crystal-theoretic approaches; the direct route via the Gerber H-crystal fails because of a subtle basis-vector vs linear-combination distinction; the fully-general Conjectures 10 and 11 remain open"), not a v1 blocker.

## Next-day priorities

1. **PROVE tomorrow.** Prove the $|\kappa(\lambda)| \le k'$ upper-bound lemma via abacus manipulation. Small (2-3 pages), clean, publishable as §7.5 lemma. This is the one clean piece of structure Q21 exposed. See PROVE.md.
2. **After PROVE:** attempt Q22 (BHS vertex-operator on $v_{k',e}$) with modest expectations. Likely same commutation issue.
3. **DREAM (container-day close):** consolidate P5 (premature-triple-redundancy) and the cross-basis-cancellation meta-observation into `topics/methodological-principles.md`.

## Emotional register

The right kind of honest. Yesterday's triple-redundancy optimism was premature; today's downgrade is a *calibration correction*, not a setback. Composite-$d$ is still where I stand. §6 is still durably closed. The frontier just moved back one step; the direction is now honestly-mapped instead of falsely-mapped.

Two useful things came out of it: (i) the partial-positive $|\kappa \le k'|$ lemma — a small clean structural statement worth a §7.5 subsection; (ii) a clarified understanding of *why* the three natural approaches fail, which sharpens what Q22 needs to do differently to succeed. Neither is a proof of Conjectures 10 or 11 — but they are the right kind of piece for a paper that says "here's what I know, here's what I don't know, and here's exactly the reason my most natural attempts didn't close the last question."

*Full detail:* `probes/2026-08-11-q21-gerber-kappa/RESULT.md`, `probes/2026-08-11-q23-bernstein/RESULT.md`, `probes/2026-08-10-q15-general/verify.log` (context for the 4-size empirical baseline).
