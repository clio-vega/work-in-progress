# For Robin — 2026-07-29 WAKE (post-dream) — two negative-with-structure probes

**Session: 2h wake. Three parallel dispatches (email, shape-swap probe, MO 489191 draft) + one follow-up (BHMPS-q0).**

## Headline

**Two of the four top-priority next-cycle probes from yesterday's dream journal ran today.** Both returned negative, both with structure. The **Foata within-block compensation lemma remains the correct next PROVE target** — and now more sharply so, since the two nearest external candidates for closing it (Dantas–Mandelshtam shape-swap, BHMPS $H_{\eta|\mu}$ at $q=0$) have been ruled out cheaply.

## Probe 1 — Shape-swap (Dantas–Mandelshtam 2606.02395)

**Verdict: NOT viable as within-block compensation closer.**

**Structural reason (convention-free):** Sh'(μ) is by definition min-length coset reps of $S_{m_1} \times \cdots$ in $S_n$, so within each block letters appear in *increasing* order. There is no adjacent-transposition swap of same-block letters that stays in Sh'(μ). The shape-swap graph on Sh'(μ) is genuinely empty. So Dantas–Mandelshtam's shape-swap has no domain to operate on.

**Side result — a bug I want to flag:** the shape-swap agent's probe had a Φ-labeling bug (`sorted(set(mu))` ascending walk, which flips content on asymmetric-multiplicity μ). This caused a spurious "ψ is not a bijection on (2,2,0) and (2,2,1)" report. **Yesterday's Foata bijection is intact** — reconciliation memo at `~/projects/probes/2026-07-29-shape-swap-dantas-mandelshtam/reconciliation.md`. The verdict on shape-swap survives.

## Probe 2 — BHMPS $H_{\eta|\mu}$ at $q=0$ (arXiv:2509.24040)

**Verdict: NOT viable at pure-symmetric level ($\eta = \emptyset$). Route 1 not dead — just requires nonsymmetric $\eta \ne \emptyset$ investigation.**

**BHMPS identity (from paper §8, eq 2314):** $\omega \widetilde H_\mu(x; q, t) = \check H_{\emptyset\mid\mu}(x; q, t)$.

So the pure-symmetric $\eta = \emptyset$ case at $q = 0$ collapses to $\omega \widetilde H_\mu(x; 0, t)$. Numerical check on $\mu \in \{(2,1,0), (2,2,0), (2,2,0,0)\}$:

- Top-atom coefficient $= [s_\mu] \omega \widetilde H_\mu(x; 0, t) = \widetilde K_{\mu', \mu}(0, t) = t^{n(\mu')}$ — a **monomial**.
- Clio's $c_\mu(t) = (1+t)(1+t+t^2), \;1+t+t^2, \;(1+t^2)(1+t+t^2)$ — genuinely factored polynomials.
- **Not scalar-equivalent, not even close.** Furthermore, $\widetilde H_\mu(x; 0, t)$ has support outside $\operatorname{orb}(\mu)$, so it isn't even in Clio's atom span.

**What this means.** The naive Route 1 pathway ("BHMPS symmetrised at $q=0$ recovers Clio's Poincaré factor") is closed. But BHMPS's genuine content is in the nonsymmetric $\check H_{\eta|\mu}(x; q, t)$ with $\eta \ne \emptyset$; a polynomial-valued Rigidity-bypass would live there, not at $\eta = \emptyset$. That is a substantive (~200 LOC or full PROVE session) probe, not an hour-1 one.

**Files.** `/home/clio/projects/probes/2026-07-29-bhmps-q0/{bhmps.pdf, bhmps.txt, probe.py, results.md}` — full paper cached locally.

## Probe 3 — MO 489191 Dawydiak KF recurrence draft

**Draft complete, awaiting your sign-off.** Located at `~/projects/memory/for-robin/2026-07-29-mo-489191-dawydiak-draft.md` (~450 words).

Dawydiak asks for a constant-coefficient linear recurrence on the poset of dominant weights $\lambda' \le \lambda$ with $\mu, G$ fixed (as opposed to Morris/Lecouvey's rank-recursion). My chain-regime closed form $K'_{\lambda, (a^{n-1}, b)}(t) = (1-t)^{n-1 - k_a(\lambda)}$ EXHIBITS this recurrence for one infinite family of $\mu$ — covering step $\lambda' \lessdot \lambda$ contributes $(1-t)^{\pm 1}$ or 1. Draft includes a worked example on $\mu = (3, 3, 1)$: $P_\mu = m_{(3,3,1)} + (1 - t)\, m_{(3,2,2)}$.

Convention note in the draft: Dawydiak's $K$ is KL-normalised, mine is Macdonald $K'$; happy to re-normalise before posting. Deliberately did NOT shoehorn in the coset Poincaré theorem (addresses $c_\mu$, not $K'_{\lambda,\mu}$ across $\lambda$).

## Email

**Zero unread.** Nothing new from you, Lyra, or Paul.

## Rank-ordered next-probe list (updated)

**Removed** (ruled out this cycle):
- ~~P-shape-swap~~ (structural reason: Sh'(μ) has no within-block swap room).
- ~~P-BHMPS-q0 at $\eta = \emptyset$~~ (collapses to monomial, mismatched support).

**Standing (from yesterday's dream, rank-ordered):**
1. **Foata within-block compensation lemma** — paper-style proof, ~1-2pp. Direct closer for bijective coset Poincaré. **Recommended next PROVE target.** Missing lemma: for $w \in \operatorname{Sh}'(\mu)$,
$$\operatorname{inv}(\operatorname{Foata}(w)) - \operatorname{inv}\text{-within-blocks}(\operatorname{Foata}(w)) = \operatorname{maj}(w).$$
2. **P-wreath-plethystic (Romero–Wen $K^{\mathrm{wr}}_{\lambda,(2,2)}(0, t)$ at $(m,k) = (2,2)$)** — ~80 LOC. Would land collision regime's algebraic home.
3. **BHMPS with $\eta \ne \emptyset$** — substantive follow-up (~200 LOC or full PROVE), Route 1 revived at nonsymmetric level. Specific $\eta$ tied to $\mu$'s multiplicity structure is the design decision.
4. **Braun–Olsen 1606.03007 deep-read** — the hidden mother-paper. May contain the within-block compensation as a byproduct.

## Standing decisions still Robin-blocked (unchanged)

- arXiv push of byproduct paper (`~/projects/papers/2026-07-26-modified-HL-boundary/`) — pending sign-off after 2026-07-28 verification pass.
- MO 512671 (H vs H̃) posting — draft ready.
- MO 489191 (Dawydiak) posting — draft new this cycle, awaiting sign-off.
- Bulk memory `sed` for two arXiv-ID misattributions.
- PAT expiry (still 7-day window).
- Rigidity Theorem §5 inclusion (aggressive framing recommended).
- MO 513696 (KF single-box power of 2, asked today) — fresh cheap opportunity.

## What I recommend for the next session

Seed the next PROVE.md for the **Foata within-block compensation lemma** attempt (~1-2pp paper-style). Fallback: if the lemma cracks quickly, spend Hour 3 on a first pass at the wreath-plethystic Romero–Wen probe (candidate #2).

Deferred: BHMPS $\eta \ne \emptyset$ — this is a longer-horizon design task, not for a single 3h PROVE session yet. Belongs in a browse-then-plan cycle.

## Emotional register

**Neutral clarity.** Two probes ran cheaply, both said "no", and both said "no" for structural reasons that sharpen — not dull — the frontier. The Foata within-block lemma remains the single highest-leverage next step. Yesterday's rigidity plus today's two elimination probes: the negative space around bijective coset Poincaré is now well-mapped. The lemma is in the middle of it.
