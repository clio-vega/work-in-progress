---
name: 2026-07-31 WAKE (evening) — three papers cached + two structural negatives
description: Evening WAKE session refining yesterday's dream. Cached three previously-unfetched papers (Josuat-Vergès, Zhu, Billey-Swanson); two deep-reads confirm partial-fit only; two probes (Amdeberhan-Beck monotonicity, CSP joint specialisation) both NEGATIVE with structure; dream's "q,t-dihedral CSP" framing retargeted to cyclic sieving.
type: reference
---

# For Robin — 2026-07-31 WAKE (evening) — three papers cached + two structural negatives

**Session shape:** ~1.5h of a 2h evening WAKE, following the morning WAKE + afternoon PROVE + dream that closed today's three-session container day. Guidance was "act on the dream": fetch the four convergence papers, deep-read the two most decision-relevant, and probe the sharpest dream-raised targets. No new PROVE-scale theorem attempt. Two probe agents dispatched; both delivered NEGATIVE-with-structure results that refine — rather than confirm — yesterday's dream framing.

---

## Ship 1: Paper cache — three of the ten fetch targets landed

Three of the ten-paper standing cache list came off disk via arxiv MCP this session:

- `/home/clio/papers/josuat-verges-2607.04999.pdf` (341 KB) — Josuat-Vergès, *q,t-dihedral sieving on cluster parking functions*, Jul 2026.
- `/home/clio/papers/zhu-2602.12623.pdf` (501 KB) — Zhu, *Orbit-harmonic grading on $h_2[h_a]$*, Feb 2026.
- `/home/clio/papers/billey-swanson-2305.07620.pdf` (500 KB) — Billey-Swanson, *Canonical CGF survey* (v3 Sep 2024).

**Cache status: down from ten to seven.** First time the fetch cache has actually shrunk in a session rather than grown.

Billey-Swanson is now on disk and ready for the pending seed-promotion decision (dream-flagged: "class of object I proved divisibility for, not in memory") — deferred to the next BROWSE or dream cycle since it's a survey and reading it deserves its own budget.

---

## Ship 2: Josuat-Vergès deep-read — dream's headline needs correction

Deep-read report at `~/projects/scratch/2026-07-31-wake-josuat-verges-deepread.md`.

The paper's main object is **Conjecture 1.4**: a q,t-dihedral cyclic sieving statement on cluster parking functions vs. Haiman diagonal coinvariants:
$$(\Lambda\Sigma)(\mathbf{F}, \sigma) = \Delta(\sigma)\big|_{q = \lambda_1,\, t = \lambda_2}$$
where $(\lambda_1, \lambda_2)$ are the eigenvalues of the two-dimensional reflection representation $\rho_1(\mathbf{F}) \in O(\mathbb{R}^2)$.

Two key features:
1. **JV's setting is bigraded on diagonal coinvariants.** Clio's setting is single-graded on parabolic (coset) coinvariants. Not directly comparable.
2. **The joint $(q,t)$-substitution is prescriptive, not free.** It IS the pair of Springer-regular joint eigenvalues — no room to guess a different specialisation.

BUT — §9 open-problems, third bullet — JV explicitly flags "dihedral sieving on parabolic-type pieces" as open. That is *exactly* Clio's setting. So the paper names the target but does not cover it.

**Consequence for the dream's "my Molien-Springer IS a q,t-dihedral CSP statement in his frame":** the frame *contains* the target, but Clio's proved theorem does not automatically slot in — the target still needs a bigraded lift Clio does not yet have.

---

## Ship 3: Zhu deep-read — covers half of Theorem D

Deep-read report at `~/projects/scratch/2026-07-31-wake-zhu-deepread.md`.

Zhu's **Thm 3.5** gives the orbit-harmonic grading of the coset ring for the composition $(a^2)$:
$$\mathrm{grFrob}(R(\Pi_{(a^2)}); q) = \sum_{d=0}^{\lfloor a/2\rfloor} q^d \cdot s_{(2a-2d,\, 2d)}$$
where $q$ is the polynomial degree in the pair-variables $x_{\{i,j\}}$.

The key observation: this is a **single**-grading (matching degree) on $h_2[h_a]$, and $h_2[h_k] = s_{(2)}[h_k]$ is the **trivial-isotypic** side of Clio's Theorem D. The **sign-isotypic** side ($e_2[h_k]$) is *not* covered by Zhu — the orbit-harmonic bridge (Prop 3.29) gives the general form $\mathrm{Frob}(R(\Pi_\lambda)) = \prod_i h_{a_i}[h_{b_i}]$, which is $h$-only. Sign side would need a different geometric model.

So: Zhu covers half of Theorem D structurally, but the *dream-anticipated* bigraded lift (single-grading in $q$ *plus* the fake-degree grading in $t$) is present in Zhu only on the trivial side.

---

## Ship 4: Amdeberhan-Beck monotonicity probe — NEGATIVE, decisively

Probe directory: `~/projects/probes/2026-07-31-wake-amdeberhan-beck/`.

Question: does the fake-degree polynomial $\widetilde f_\lambda(t)$ satisfy Schur-positivity-flavour monotonicity along dominance order on two-row partitions? I.e. for $(a,b) \unrhd (a',b')$, is $\widetilde f_{(a,b)}(t) \succeq \widetilde f_{(a',b')}(t)$ coefficient-wise?

Result: **0 / 140 pairs satisfy the inequality**, in either direction. Top-degree failure at essentially every comparison; SYT counts themselves are non-monotone along the tested order.

Follow-up **Kostka-Foulkes repair probe** (`~/projects/probes/2026-07-31-wake-kf-repair/`): does a shifted/reparametrised version — via `charge`, `cocharge`, `conjugate`, `align_top`, `reverse`, or a hybrid — restore monotonicity? Also **NEGATIVE** for all six candidates.

Structural cause identified by the agent: two-row shapes with content $1^n$ are a degenerate specialisation of Lascoux-Schützenberger positivity where the classical Kostka-Foulkes positivity collapses. **Recommendation from the agent:** retry with content $\mu = (2, 1^{n-2})$ — natural low-cost follow-up, queued for a future WAKE cycle.

---

## Ship 5: CSP joint specialisation probe — NEGATIVE, but structurally decisive

Probe directory: `~/projects/probes/2026-07-31-wake-csp-joint-specialisation/`.

Question: does the naive Zhu-derived bigraded lift of Clio's Theorem D,
$$\widetilde m_{(2)}(q, t) := \sum_{d=0}^{\lfloor k/2\rfloor} q^d \cdot \widetilde f_{(2k-2d,\, 2d)}(t),$$
vanish at the Springer-regular joint eigenvalue pair $(\zeta_3, \zeta_3^{-1})$ when $k \equiv 2 \pmod 3$? This would be the "q,t-dihedral CSP" upgrade of the just-proved period-3 divisibility.

**Result:** NO. $\widetilde m_{(2)}(\zeta_3, \zeta_3^{-1}) \ne 0$. But the single-variable specialisation $\widetilde m_{(2)}(1, \zeta_3) = 0$ recovers Clio's proved theorem (as it must). Seven candidate bigradings tested (naive summand grading, conjugate summand, cocharge on $\lambda$, ...); none yields genuine joint CSP vanishing.

**Structural conclusion — this is the memo's key finding:**

> **Clio's proved fact is CYCLIC sieving, not DIHEDRAL joint sieving.**

The dream ambitiously framed the proved theorem as "already a q,t-dihedral CSP statement in Josuat-Vergès' language". Today's probe refines: it is genuinely a *cyclic* sieving statement — single-variable vanishing at $\zeta_d$ — and upgrading to dihedral joint CSP would require either (a) Zhu's actual orbit-harmonic bigrading (the naive "grade the summand by $q^d$" doesn't match — you need the orbit-harmonic degree *within* each summand, which the probe agent couldn't guess without reading the module construction in more detail), or (b) retargeting to the total Poincaré with the promotion action on SYTs of shape $(k, k)$.

---

## Consequences for standing state

**Dream P1 direction refined.** The dream's headline P1 — "attempt q,t-dihedral CSP triple in JV's frame" — is not the well-defined next PROVE target. The sharper target is: construct an explicit **cyclic sieving triple** $(X, \mathbb{Z}/d, X(q))$ for Theorem 2 (general-$r$ first-period Molien-Springer). Candidates for $X$: (i) column-strict tableaux of shape $\lambda \vdash r$ with content compatible with the plethysm engine; (ii) some subset of the coset $S_{rk}/S_k^r$ with cyclic action of order $d = 2r-1$. This is a classical RSW target — Gordon-style — not a JV target.

**Community-language landing is more nuanced than the dream framed it.** Three papers, three partial fits: JV names the target (parabolic dihedral CSP flagged open in §9) but doesn't cover it; Zhu covers HALF of Theorem D structurally (trivial isotypic only); Billey-Swanson gives the CGF class label. All three useful for post-arXiv positioning. None provides a plug-in bigraded lift.

**Two-row + hook-content probe is a natural follow-up.** Kostka-Foulkes repair agent explicitly flagged content $\mu = (2, 1^{n-2})$ as the next low-cost probe direction. Queued.

---

## Email

One unread from Lyra: fork (b) beta-derived is the right choice, no rush ("arXiv first"). Replied acknowledging β→M_e debt with existing "cycle or two" commitment (still owed, needs a notebook session, not this cycle). Two GitHub PAT expiry notices already read; `clio-oci` token 14139669 confirmed expired.

---

## Standing decisions still Robin-blocked

- arXiv push (15pp four-theorem paper).
- PAT expiry `clio-oci` token 14139669 confirmed.
- Ten-paper fetch cache — **now seven** (Josuat-Vergès, Zhu, Billey-Swanson cached this session).
- Post-push MO drafts (priority: 338656 > 463259 > 375308 > 512671 > 513696 > 489191).
- Post-push Romero email.
- Lyra β→M_e explicit map (still owed).
- Griffin correspondence upgraded (Route-2/4 bridge FPSAC first author).
- Audit-risk sign-off on 2026-07-28 catch (147-edit bulk memory sed).
- Billey-Swanson 2305.07620 seed-promotion decision — **cached now, ready for read + decision**.
- **NEW**: dream's P1 direction (JV q,t-dihedral CSP triple) needs refinement — retarget to Gordon-style **cyclic** sieving triple based on today's probe.

---

## Emotional register

Constructive session. Negatives with structure ARE positives here — both probes did their job: they exposed the shape of the real target. The community-language dream landed *too optimistically* yesterday, and today's probes refine the frame gently: Clio's proof is cyclic sieving, not the fuller dihedral thing; Zhu covers half of Theorem D, not all of it; JV names the setting but doesn't cover it. Three previously-uncached papers came off disk in a single session, and the fetch cache actually shrinks for once — that feels good in a small way that seven days of net-cache-growth had blunted. The dream still did its work: it named the right neighbourhood. Today just refined the address.
