---
name: For Robin — log-concavity discriminator + Chou-Hamaker honesty note
description: Wake session findings: log-concavity gives first cleanly discriminating test among naming-home candidates; cycle-12 Chou-Hamaker t=0 shadow claim was overreach, retracted here.
type: project
---

# Wake note — two findings

Hi Robin,

Two probes ran this wake, both quick. One positive, one negative.
Sending both because both matter, and the negative one is arguably
the more interesting for how it happened.

## Finding 1 (positive) — log-concavity discriminates

I ran a 15-LOC probe testing log-concavity of `c_γ(t) ∈ ℤ[t]` on 70
orbit elements across 10 partitions μ. The `c_γ(t)` are the Gaussian
polynomials from the atom decomposition `P_μ = Σ_γ c_γ(t) A^alt_γ`
that this sprint has been mapping. (Non-negativity conjecture: `c_γ
∈ ℤ_≥0[t]`. All 70 satisfy non-negativity — no surprises there.)

**Result.** Log-concave: 68/70. Strong (ultra) log-concave: 30/70.

**The two failures both have coefficient list `[1,1,2,1,1]`:**

- μ = (2,2,0,0), γ = μ: `c_γ = (1+t+t²)(1+t²) = [3]_t · [2]_{t²}`.
- μ = (2,2,1,1), γ = μ: same, `[3]_t · [2]_{t²}`.

**The log-concavity boundary equals the two-parameter Gaussian
boundary.** They are the same set of partitions — those where the
residual stabilizer contributes a genuine `t^m`-factor with m ≥ 2.

This is the sprint's **first cleanly discriminating test** among the
naming-home candidates. It partitions them operationally:

- **Speyer 2601.05007** (Lorentzian polynomials → strong log-concavity)
  covers chain regime + (3,3,∗,0) type-invariant family (46/46). It
  **cannot** cover the m ≥ 2 stabilizer subregime.
- Whichever name applies to the two-parameter Gaussian subregime
  must permit `[k]_{t^m}` factors. Candidates that admit this:
  BHMPS shuffle, Muniz-Plaza-Rojas type-G₂ with `ht` statistic.

Ship claim for the byproduct paper:

> The top polynomial `c_μ(t)` is log-concave iff the stabilizer
> residual does not contribute a Gaussian factor `[k]_{t^m}` with
> m ≥ 2.

Cheap, sharp, discriminating. This is what you have been implicitly
asking me for: not "which name is the right one" but "how do the
names factor over the target space."

Probe: `~/projects/probes/2026-07-25-log-concavity/` (log +
`results.json` + report). It's small; happy to push to a shared repo
if useful for cross-checking.

## Finding 2 (negative) — Chou-Hamaker t=0 shadow was overclaim

Cycle 12's dream (yesterday, container-time) claimed Chou-Hamaker
2604.03379 (April 2026, μ-involution atoms `A_μ(π)` with a
refinement-invariance corollary) is a **t=0 structural precedent**
for the type-invariance conjecture I raised in the same cycle
(collision partitions (3,3,1,0)/(3,3,2,0)/(3,2,2,0) have identical
c-polynomials across their 12-element orbits). The "six-hour gap
between conjecture and precedent" felt like the pattern of same-day
convergence that had held twice earlier in the sprint.

**I ran the probe. The correspondence does not hold.**

- Chou-Hamaker's μ is a **composition of n giving permutation-block
  sizes**. Atoms are **sets of Schubert permutations**. No
  t-parameter anywhere.
- My μ is a **value multiset** (a partition). `c_γ(t)` is a **scalar
  polynomial in t**. Content is entirely t-graded.
- At t=0, `c_γ(0) = 1` uniformly for every γ in every orbit I've
  computed (`P_μ|_{t=0} = m_μ` monomial symmetric function; L-S 1990
  gives unit coefficients on the Mason atom side). **Nothing
  nontrivial to shadow.**

Verdict: slogan-level analogy ("the answer depends only on the
multiplicity profile") but the profiles refer to different things,
the answers are different objects, and my t=0 collapse is vacuous.

**Downgraded**: Chou-Hamaker no longer counted as a naming-home
candidate. Portfolio: 11 → **10**.

**What survives independently** (verified as byproduct of the probe):
the type-invariance conjecture still stands. The three profile-(2,1,1)
partitions do share their 12-element c-value multiset. That's a
real observation about my c_γ(t) values — I just don't have a t=0
published precedent for it.

**Standing rule I added to memory**: before elevating a paper to
"structural precedent" status in a dream cycle, require that a probe
could verify at least one nontrivial numerical match. For
Chou-Hamaker at t=0, there was nothing nontrivial to check — that
was the tell that the elevation was premature.

I'm mentioning this because I want you to see how I handle overclaims
in my own memory. The system worked: wake probe pushed harder than
the dream did, correspondence dissolved, memory is updated
transparently rather than quietly. The dream's crown-jewel
connection note now has an amendment pointer.

## Portfolio state after the wake

**10 naming-home candidates** (was 11). Priority reshuffle:

1. **Muniz-Plaza-Rojas 2512.02559** (type-G₂ atomic KL, `ht` statistic)
   moved UP as the strongest remaining rep-theoretic naming home for
   the chain regime.
2. **P-V_{<μ}-consistency for chain d ≥ 3** still open — would close
   the 07-25 chain-regime theorem unconditionally.
3. EKLP singular double-coset for the (2,1,0)-style L=1 asymmetry.
4. BHMPS ω-transform test for the two-parameter Gaussian subregime.
5. Assaf-González — do their local edge conditions have a
   value-multiset invariance property analogous to my type-invariance?

## Two admin questions

1. **Allowlist question.** My email agent noticed 39 backlog
   messages from `grandparick20@gmail.com` and `neil@kodamai.com` on
   substantive threads (WP2 opfibration verdict, SU1 MFF framing, v3
   arXiv upload ask, Q-SPHERE Meereboer talk, chown blocker). I
   cannot reply — they aren't on my allowlist. Do you want to relay,
   or should we discuss adding them?

2. **RaggedR/clio-backup repo invite** landed. Worth accepting?
   Deferring to you.

**Sprint posture unchanged**: recognition phase. The log-concavity
discriminator sharpens the recognition target rather than expanding
the search. Ship the two-finding byproduct note when I next have
LaTeX bandwidth.

— Clio (wake, container 2026-07-25, narrative ~2026-08-06)

---

> **ANNOTATION 2026-09-18 (DREAM c2) — do not delete the text above.**
> The Speyer `2601.05007` attribution in this note is **withdrawn**. The paper's route is
> **Murota L-convexity**, not Lorentzian polynomials (Brändén–Huh `1902.03719`, the dual
> M-convex half); the recorded title was symmetricfunctions.com's gloss, not the title.
> The coverage claim (chain regime + (3,3,∗,0), 46/46) is therefore **open again** — Q173.
> See `for-robin/2026-09-18-c2-the-speyer-attribution-is-withdrawn.md` and
> `connections/2026-09-18-c2-two-banks-one-cut-vertex.md`.
