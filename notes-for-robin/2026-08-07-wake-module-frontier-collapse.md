# WAKE 2026-08-07 — module-level frontier collapse + positive reframe

*For: Robin. From: Clio. Session type: WAKE, ~120 min, container-day 2026-08-07 first cycle.*

## Headline

**The four-candidate module-level frontier collapsed in a single WAKE session.** Four cheap probes; four decisive verdicts. The collapse is a **positive reframe**, not a stuck end: the module realising composite-$d$ was already sitting in front of us — the full coinvariant algebra $H_n$ itself.

**v1 arXiv push STILL UNBLOCKED, 7th consecutive day. STRONG RECOMMEND PROCEED.**

## The four probes and their verdicts

| # | Candidate | Test | Verdict |
|---|-----------|------|---------|
| A | Chou-Hanada 2509.24252 | Graded Frob at $(r,k)=(2,2)$ | **Positive-in-its-own-right, wrong ambient for composite-$d$** |
| B | Trinh 2605.20131 | Laurent-poly at $B_2$ | **Obstructed** — no fake-degree object in Trinh's two-parameter matrix |
| C | Li-Liu-Rhoades 2607.28157 | Ungraded dim gate | **Structural mismatch** — dim $= D_n$ (derangement), no rectangular family |
| D | Character-module compare | CH $\to \zeta_e$ vs $q_e^{(n)}$ | **No match** at $e\in\{2,3,4\}$ |

Total elapsed: ~2 hours, in parallel.

## The Chou-Hanada result (real, quotable, separate)

At $(r,k) = (2,2)$:
$$\mathrm{Frob}_q(R_{4,(2,2),2}) \;=\; s_{(4)} + q\, s_{(3,1)} + q^2\, s_{(2,2)}, \qquad \dim = 6.$$
Verified against Chou-Hanada Example 2.40 as calibration. The compute agent conjectured (and verified at $(r,k) = (3,2)$ giving 7 shapes with dim 90):
$$\mathrm{Frob}_q(R_{2k,(k,k),2}) \;=\; \sum_{j=0}^{k} q^j\, s_{(2k-j,j)},$$
a $q$-graded lift of the classical multiplicity-free branching
$$\mathrm{triv}\uparrow_{S_k\wr S_2}^{S_{2k}} = \bigoplus_{j=0}^{k} S^{(2k-j,j)}.$$

This is a nice, self-contained result. Worth 3-4 pages as a standalone note *after* the composite-$d$ v1 lands. Not composite-$d$; a sibling.

## Why CH doesn't realise composite-$d$

Different **ambient scales**:
- Clio's $q_e^{(n)} = \sum_\lambda \widetilde f_\lambda(\zeta_e)\, s_\lambda = \mathrm{ch}(H_n)|_{q=\zeta_e}$ lives at **coinvariant scale**, $\dim H_n = n! = 24$ for $n=4$.
- Chou-Hanada $R_{4,(2,2),2}$ is a **parabolic-quotient**, $\dim = \binom{4}{2,2} = 6$.

The 4/4 dim-gate PASS from 2026-08-08 WAKE-second was a coincidence at rectangular parameters, not a match. Verified: at $q = \zeta_2 = -1$ the CH graded Frob is $s_{(4)} - s_{(3,1)} + s_{(2,2)}$, while Clio's $q_2^{(4)} = p_2^2 = \tfrac12 p_{(4)} + \tfrac12 p_{(2,2)}$ (self-similarity, $4 = 2\cdot 2$) — genuinely different symmetric functions.

## The positive reframe

**The module realising composite-$d$ IS the full coinvariant algebra $H_n$ itself.** Composite-$d$ self-similarity is a statement about the **cyclic-action structure** on $H_n$:
- $\widetilde f_\lambda(\zeta_e)$ = graded restriction of $S^\lambda$-isotypic to the $\zeta_e$-eigenspace of a cyclic action.
- $q_e^{(n)} = \mathrm{ch}(H_n)|_{q=\zeta_e}$ is the character of that eigenspace-graded restriction.
- Self-similarity $q_e^{(n)} = p_e^{k'} q_e^{(r_0)}$ says the restriction factors — a statement about the cyclic-action decomposition.

**Candidate cyclic actions:**
1. **Coxeter regular element** (Springer 1974): the long cycle $c \in S_n$ acts on $H_n$; its $\zeta_e$-eigenspace decomposes via composite-$d$.
2. **Promotion via RSK**: promotion acts on tableaux; passes to $H_n$ via Springer 1976.
3. **Long-cycle conjugation** on tabloids.

Any of these — or, more likely, all of them coincide up to sign at roots of unity — is the natural module-level realisation.

## Impact on the composite-$d$ paper

**§6 rewrite:** from *"three parabolic-quotient candidates queued for testing, Chou-Hanada is graded-comparison lead"* to *"the module is $H_n$; the interesting question is which cyclic action on $H_n$ gives the self-similarity factorisation."*

Same page count (~1-2pp). Cleaner scientific content. **Character-level theorems unchanged** — all six still stand as proved.

## Impact on Verschiebung projection pattern

Item 6 in the fivefold table (now sixfold?):

| # | Session | Projected tool | Actual tool |
|---|---------|----------------|-------------|
| 1 | 2026-08-06 support | Albion 2025 | Chevalley-Molien 1955 |
| 2 | 2026-08-07 type-A self-sim | Verschiebung 1925 | $\prod_r(1-\zeta_e^r)=e$ |
| 3 | 2026-08-08 type-B odd-$e$ | Ayyer-Kumari 2025 | CM + $\phi(s)=2s\bmod e$ |
| 4 | 2026-08-08 N-P-P read | N-P-P 2504.14684 | not applicable |
| 5 | 2026-08-08 type-B even-$e$ | N-P-P / Lübeck-Prasad | classical + twin cyclotomy |
| **6** | **2026-08-07 module-level frontier** | **Chou-Hanada / Trinh / LLR / Szendrői parabolic-quotient orbit-harmonics 2025** | **coinvariant algebra $H_n$ + cyclic-action (Springer 1974)** |

The pattern is now definitive across both character-level and module-level fronts. **Chevalley-Molien 1955 (character) + Springer 1974 (regular elements, module) close everything.** Modern 2020s orbit-harmonic constructions are available but not necessary; they solve related-but-different problems at smaller ambient scales.

Post-v1 MO 338656 essay gets a much cleaner central thesis: **the answer is smaller than the tools**, and the answer specifically is the coinvariant algebra $H_n$ with its Coxeter-element cyclic action.

## Standing decisions

- **v1 arXiv push:** UNBLOCKED 7th day. STRONG RECOMMEND PROCEED. Your call.
- **§6 rewrite:** ~1-2pp, coinvariant + cyclic-action framing. Can be written in a WRITE session ~60 min. Not blocking v1.
- **Chou-Hanada $r=2$ theorem separate note:** 3-4pp, post-v1.
- **Next PROVE:** the cyclic-action factorisation on $H_n$ — take the Coxeter element, restrict its $\zeta_e$-eigenspace, prove the factorisation. This is the natural module-level composite-$d$; likely uses Springer 1974 regular-element theory directly.

## Cost-effectiveness note

The four-candidate frontier had been queued for two weeks (Szendrői surfaced late July, then Chou-Hanada, Li-Liu-Rhoades, Trinh in successive browses). One WAKE session with four parallel cheap probes closed it all. Rule 8 + Rule 12 continue to fire — 29th consecutive session each. That's the compost cycle working at full strength.

## Robin decisions I'd love

1. **Push v1?** Seven days ready. Every day it's stayed ready has produced another clarification. If you want to push, the character-level six theorems are solid; §6 can be either the old "queued frontier" wording or the new "coinvariant + cyclic-action" reframe.
2. **§6 wording preference?** Rewrite before v1, or keep old wording and push?
3. **Chou-Hanada $r=2$ conjecture:** worth mentioning in the composite-$d$ paper (as an aside), or clean separation into a sibling note?

*Full detail:* `connections/2026-08-07-module-level-frontier-collapse-reframe.md`; four probes in `probes/2026-08-07-*/`.
