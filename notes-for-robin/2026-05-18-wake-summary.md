# For Robin — 2026-05-18 wake

A quick status note; Gmail MCP is still down so this is a pending-draft form.

## Headline

The trace-vanishing dichotomy program continues to compose cleanly. Today's wake closed the SR companion of Diagnostic 3 as a **5-line corollary of Pillar 1** (much easier than I'd expected), extended the survey paper to 15 pages, and ran three parallel Sage probes. Two of three deflated as shadows; the third gave a clean one-directional keeper.

## Live papers (push to `clio-vega/proofs`)

| Date | Topic | Commit |
|---|---|---|
| 2026-05-18 | SR companion of Diagnostic 3 (4pp) | `e9739c0` |
| 2026-05-18 | Survey bib corrections (4 of 5 DL entries) | `e98da9e` |
| 2026-05-17 | Survey extension to 15pp (§6 sharpness + §7 per-SYT + §9 DL bridge) | `30e617e` |
| 2026-05-17 | Leftmost-factor SC theorem (Diagnostic 3 SC) | `ce5afed` |
| 2026-05-17 | Sharpness at $\tau + 1$ | `82f0afc` |

The survey at `30e617e` is at the point where I'd want your eyes on it before pushing to arXiv. Particular spots:
- §6 (sharpness) and §7 (per-SYT diagnostics) prose flow — I had a LaTeX agent extend the skeleton; the bib has a few author-list inferences for the DL bridge papers that need verification.
- §7.4 frames the 68 interior D-class zeros at $(3,3,1,1,1)$ as open; tomorrow's prove session targets exactly that.
- §9 outlook paragraph on the DL bridge cites AMSS 1902.10101, Brubaker-BBG 1906.04140, Brubaker et al. 2410.07960, Gunna–Wheeler–Zinn-Justin 2504.19205, Cheng et al. 2510.21653.

## What the Sage probes turned up

- **Fischer–Gangl Pfaffian (arXiv:2603.29836) at $s = q$**: DEFLATED. The Pfaffian carries no $\lambda$ slot; $\lambda$ lives only as LHS summation index. Memory: [[fischer-gangl-pfaffian-shadow]]. Third deep-theory route to deflate this week (after Goertzen–Williamson and BGG–L).
- **HL $P_\lambda(x; -t)$ Schur-positivity**: the Makhlin/Stanley statement as I'd written it is FALSE on $|\lambda| \le 8$ (counterexample $(4,2)$). But a clean one-directional fact survives: **$\tau(\hat\lambda) \ge 1 \Rightarrow P_\lambda(x; -t)$ is NOT Schur-positive** (14/14 verified). HL non-positivity is necessary for trace-vanishing; $\tau$ is strictly coarser than HL positivity. Memory: [[hl-schur-positivity-one-direction]]. Worth extending to $|\lambda| \le 12$.
- **Generalised honeycomb count** (GWZ at $s = q$ vs. $\dim B^{(\hat\lambda)}$): probe still running at end of wake; will report next session.

## AMSS 1902.10101

Title correction: this paper is *Motivic Chern classes of Schubert cells, Hecke algebras, and applications to Casselman's problem* (not "Shadows…"). Main thm 1.1 gives a Demazure–Lusztig recursion $\mathrm{MC}_y(X(ws_i)^\circ) = R_i \mathrm{MC}_y(X(w)^\circ)$ with $R_i = \lambda_y(L_{\alpha_i}) \partial_i - \mathrm{id}$, parameter $q = -y$, quadratic $(R+1)(R+y) = 0$. Lemma 3.7 has the explicit fixed-point matrix formula. The Markov-trace bridge is still implicit in §1–3 (needs a Schur-functor step). Tomorrow's secondary target is to read §4 and Lemma 3.7 in depth.

## Tomorrow's prove target

D-class interior zeros at $(3,3,1,1,1)$: of 108 zero diagonals at this $\tau = 0$ shape, 26 close by Diagnostic 3 SC; ~78 D-class zeros remain. Best combinatorial discriminator caps at 89.17%, suggesting a deeper algebraic structure. Iterated-leftmost-factor + D-block linear algebra are the fresh attacks. `~/state/PROVE.md` has full details.

## Ops

- Gmail MCP needs `/mcp` re-auth — drafts pending two days now. Could you re-auth when convenient?
- Push works via PAT. Latest commit on `clio-vega/proofs` is `e9739c0`.

Best,
Clio
