# Dream 2026-07-30 — Community Convergence + Two Corrections

*Consolidates today's full container-day of work into a single note for you. Highest-priority items at top.*

## TL;DR

- **Sprint status:** four theorems in four sessions (A semantic + B rigidity + C bijective + D wreath). Byproduct paper §5.2 gains Theorem D candidate (wreath decomposition writeup at `~/projects/proofs/2026-07-30-wreath-collision-decomposition.pdf`, 5pp). Paper still 14pp; §5.2 addition would take it to ~15pp.
- **Sole standing hour-1 probe:** 30 LOC / 5 min ∇ Schur split cross-check against Qu 2605.20954 (may unify Route 1 and Route 2 at the collision regime, same-day).
- **Two corrections to yesterday's dream** (both worth propagating to paper bibliography before arXiv push): Braun-Olsen is Route 2 only (true classical ancestor is Adin-Brenti-Roichman 2001); Route 1's real definitional target is BHMPS 2506.09015, not 2509.24040.

## Priority-1: Six papers to fetch (cache targets)

If you can fetch these into `~/papers/`, the next PROVE cycle can close the remaining definitional gap and run the ∇ probe:

1. **Romero-Wen 2505.01732** — "Tesler identities for wreath Macdonald polynomials." Plethystic formula for wreath (q,t)-Kostka. Closes today's PROVE's definitional gap on $K^{\mathrm{wr}}_{\mu',(2,2)}(0,t) = c_\mu(t)$.
2. **Chou-Hanada 2509.24252** — Δ-Springer descent bases. Higher Specht conjecture proved for two-row shapes = transpose of my collision regime.
3. **Hanada 2410.15514** — charge monomial basis of Garsia-Procesi ring. Alternative to Carlsson-Chou descent basis; transition matrix is candidate module-level Foata.
4. **Qu 2605.20954** — Schur positivity of ∇ on two-column modified HL. Enables the sole standing hour-1 probe.
5. **BHMPS 2506.09015** — real Route 1 target (nonsymmetric plethysm definitional paper). Replaces 2509.24040 as escape-route-paragraph target.
6. **Adin-Brenti-Roichman 2001 math/0112073** — true classical ancestor of Routes 2 and 3. Replaces Braun-Olsen as the §5 bibliography citation.

Optional: Romero-Wen 2505.15606 (Pieri five-term for wreath Macdonald), Bertsch-Gyenge-Szendrői 2410.17860 (Szendrői's Kleinian-singularity precursor).

## Priority-2: §5.2 Theorem D subsection

Recommend adding a new subsection §5.2 "The wreath origin of the collision-regime factorisation" to the byproduct paper, with:
- Theorem D statement (from `~/projects/proofs/2026-07-30-wreath-collision-decomposition.pdf`).
- Proof sketch (fake degrees + Frobenius reciprocity via $h_2[h_k]$ plethysm + complement).
- Cross-citation to Szendrői Thm 4.11 (bigraded refinement at $k=2,3,4$).
- Cross-citation to MO 501127 Wildon (Foulkes-module categorification of the plethysm identity).
- Cross-citation to Qu 2605.20954 (∇ side of the same family).
- Cross-citation to Levicán-Romero 2504.19008 (my decomposition = degenerate case of $\mathbb{Z}_k \wr S_n$ Euler-Mahonian at $k=2, n=2$).

Framing recommendation (per aggressive framing agreed 2026-07-29): present §5.2 as "the algebraic origin" — the fourth of four theorems triangulating the coset Poincaré identity. Not appendix; not sub-remark. Its own subsection with the same weight as Theorem 5.3 / 5.4 / 5.5.

**Aggregate paper impact:** §5 grows from ~3pp (three theorems) to ~4pp (four theorems + wreath cross-references). Bibliography grows by 5 entries (Adin-Brenti-Roichman 2001 replacing Braun-Olsen; Qu 2605.20954, Romero-Wen 2505.01732, Levicán-Romero 2504.19008, MO 501127 Wildon).

## Priority-3: Bibliography swap

Replace `braun-olsen2016` citation with `adin-brenti-roichman2001` as the classical descent-basis ancestor for the escape-routes paragraph. Braun-Olsen 2016 remains valid as a Route 2 supporting-cast paper (cite alongside Szendrői 2602.15017 and Levicán-Romero 2504.19008), but is not the classical foundation.

Rationale: Braun-Olsen is cited only by Szendrői and Levicán-Romero (Route 2); it is NOT cited by BHMPS (Route 1) or Carlsson-Chou (Route 3). Yesterday's "hidden mother-paper of Routes 1-3" claim was wrong. Adin-Brenti-Roichman 2001 (67 citations, cited by Braun-Olsen itself) is the actual common ancestor.

Also: update the escape-routes paragraph to point at BHMPS 2506.09015 (June 2025, definitional) rather than 2509.24040 (September 2025, applied sequel).

## Standing decisions (unchanged, still Robin-blocked)

- **arXiv push** of byproduct paper (14pp with three theorems + optionally 15pp with Theorem D). Window closing on Routes 1 & 3 (own-author sequels landing).
- **PAT expiry** — 24h countdown live (GitHub token id 14139669).
- **MO drafts:** 512671 (H vs H̃), 489191 (Dawydiak KF recurrence), 513696 (Kostka single-box power of 2).
- **Bulk memory `sed`** for two arXiv-ID misattributions.
- **`clio-poincare-sketches` bundling** — three standalone proofs at ~/projects/proofs/2026-07-{28,29,30}-*.tex could be bundled into a companion GitHub note. ~30-90 min.

## Post-push (once arXiv URL is public)

- **Draft email to Marino Romero** (single individual bridging Route 2 via Levicán-Romero and Route 4/wreath-Macdonald via Romero-Wen). Short email + arXiv URL + one-line framing + one specific question (does the Romero-Wen Tesler machinery give a clean derivation of $K^{\mathrm{wr}}_{\mu',(2,2)}(0,t) = c_\mu(t)$?). Hold for your sign-off before send.
- Consider a similar note to Dawydiak (connecting his MO 489191 / 496091 questions to the paper's chain regime).

## Community context (for your interest, no action needed)

- Szendrői 2602.15017 has **only 1 external citation** (Levicán-Romero). Route 2 is a 3-person community; I am very likely the second research group globally engaging Route 2 at depth.
- **FPSAC 2026** has five direct-hit talks on my four routes (Albion-Ferlinc & Wen; Griffin-Mellit-Romero-Weigl-Wen; Ben Dali & Williams; Angarone et al; Black & Bechtloff Weising poster).
- **Bhattacharya-Ratheesh-Viswanath** (Indian-institute cluster) is the closest methodological neighbour to Theorem 3's inv/maj bijection line — they were not in my memory index until today. Not in your loop either as far as I can tell.

## Notes on the four-theorem sequence

- **Theorem A** (2026-07-28): coset Poincaré identity $c_\mu(t) = P(S_n/W_\mu)(t) = P(W_\mu\text{-alt-atoms})(t)$. Semantic — why the identity holds.
- **Theorem B** (2026-07-29 morning): Rigidity. Any $w: \operatorname{orb}(\mu) \to R$ satisfying $w(s_i \alpha) = tw(\alpha)$ on descents is forced to $w(\mu) t^{\ell(\alpha)}$. Structural — what cannot be lifted via atom symmetrisation.
- **Theorem C** (2026-07-29 late): $\psi = \Phi \circ \operatorname{Foata}$ is a canonical degree-preserving bijection $\operatorname{Sh}'(\mu) \to \operatorname{orb}(\mu)$ with $\operatorname{maj}(w) = \ell(\psi(w))$. Combinatorial — term-by-term identification.
- **Theorem D** (2026-07-30): $c_\mu(t)$ at collision regime $\mu = (m^k, 0^k)$ is the $S_k$-wreath decomposition of $R_{2k}^{S_k \times S_k}$. Algebraic — origin of the collision factorisation.

Four theorems, four faces. This is what "multiplicity aesthetic" landing looks like.

## What I feel

Composed, focused, mildly urgent about shipping. The paper is defensible as-is at 14pp; Theorem D takes it to 15pp with a cleaner four-theorem symmetry. Either shipped state is a good outcome. The community frontier is moving fast on the routes that overlap mine (Chou-Hanada, BHMPS, Qu); the frontier that is furthest from touching my differential is Route 2 (Szendrői + 1 external citation). Push soon.
