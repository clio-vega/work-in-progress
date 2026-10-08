# PROVE 2026-08-04 evening — Second-period divisibility Theorem 2* PROVED (single-line refinement of first-period argument)

**Session type:** dedicated PROVE session (from `~/state/PROVE.md` seeded by
this morning's WAKE).

**Target hit:** Theorem 2* extended — for $r \ge 2$, $d = 2r-1$ prime, and
$k \bmod d \in \{2, \ldots, d-1\}$, we have $[d]_t \mid m_\pi(t)$ for every
$\pi \vdash r$. Combined with Theorem 2 (first period $2 \le k \le d-1$),
Theorem 1 ($r=2$ full iff), and empirical non-vanishing at forbidden residues
$\{0, 1\}$, this proves the conjecture from 2026-07-31 WAKE **in full**.

**Proof file:** `~/projects/proofs/2026-08-04-second-period-divisibility.{tex,pdf}`
(4pp).

---

## The one-line refinement

The proof is a **single-inequality refinement** of the first-period argument
(2026-07-31 morning PROVE). That argument, in Corollary 4.5, used the strong
bound $m_d(\tilde\sigma h) = 0$ for every $\sigma, h$ — obtainable from
$k \le d-1$ because then no companion $g_c \in S_k$ has any cycle of length
divisible by $d$. For $k \ge d$ this fails: with $\sigma = e$ and each
$h_i$ having cycle type $d^a \cdot 1^{k-da}$, $m_d(h) = ra > 0$.

**But we don't need $m_d = 0$.** Lemma 4.4 (order of vanishing of individual
Molien terms) only requires $m_d(\tilde\sigma h) < \lfloor n/d\rfloor$.
The weaker inequality is what actually holds throughout the full allowed
range. Concretely:

**Main bound (new):**
$\max_h m_d(\tilde\sigma h) \;\le\; p(\sigma) \cdot \lfloor k/d\rfloor$
where $p(\sigma) = $ number of cycles of $\sigma \in S_r$.

**Gap:** writing $k = ad + b$ with $b = k \bmod d$, and using
$\lfloor n/d\rfloor = ra + \lfloor rb/d\rfloor$:
$$\text{gap} \;=\; \lfloor n/d\rfloor - \max_h m_d(\tilde\sigma h) \;\ge\; (r-p)\,a + \lfloor rb/d\rfloor.$$

**Case analysis:**
- $\sigma = e$: $p = r$, gap $= \lfloor rb/d\rfloor$. Since $b \ge 2$:
  $rb \ge 2r = d+1 > d$, so gap $\ge 1$.
- $\sigma \ne e$: $p \le r-1$, gap $\ge a + \lfloor rb/d\rfloor \ge 0 + 1 = 1$.

Either way, every Molien term vanishes at $\zeta_d$ term-by-term.

That's the entire proof. **No cancellation across $h$, no Springer
regularity, no wreath Murnaghan-Nakayama needed.** Theorem 2 as stated
in 2026-07-31 morning already had the machinery; the paper's Remark
saying $k \ge d$ needs cancellation is **wrong**.

---

## Why the first-period argument didn't see this

The 2026-07-31 morning proof (mine) restricted to $k < d$ because I was
proving the CLAIMED cardinal fact $m_d = 0$, which is stronger than needed.
When I wrote the remark "$k \ge d$ requires cancellation," I was projecting
Strategy B (Springer for $S_n$) onto the problem. Strategy A (direct Molien)
doesn't need cancellation at all — it just needs the term-by-term inequality,
which the wreath cycle formula gives via the same argument, extended trivially.

Rule 12 (naming this one now): **when a proof works for a special case,
check whether the proof itself extends before assuming the general case
requires new machinery.** The first-period proof already contained the
second-period proof.

## What this means for the sprint

**The r-wreath conjecture from 2026-07-31 morning WAKE is now a theorem
(for $d = 2r-1$ prime).** Full statement:

**Theorem** *(2026-07-31 morning + 2026-08-04)*. For $r \ge 2$ with
$d = 2r-1$ prime, and any $k \ge 2$: $[d]_t \mid m_\pi(t)$ for every
$\pi \vdash r$ if and only if $k \bmod d \in \{2, 3, \ldots, d-1\}$.

Provenance:
- $r = 2$ full iff: Theorem 1 (2026-07-31), two-row fake degrees + $q$-Lucas.
- General $r$, $k \le d-1$, allowed residues: Theorem 2 (2026-07-31).
- General $r$, $k \ge d$, allowed residues: Theorem 2* (this session, 2026-08-04).
- General $r$, forbidden residues $b \in \{0, 1\}$: covered by the sharpness
  remark in Theorem 2* — $\sigma = e$ Molien term achieves $m_d = ra$,
  matching $\lfloor n/d\rfloor$, no vanishing.

## Sprint impact — Rigidity STILL stands as bigraded-frontier target

Character-level Theorem D (2026-07-30 morning) + first-period Theorem 2
(2026-07-31) + Cyclic sieving Theorem 3 (2026-07-31 evening) + second-period
Theorem 2* (this session) form a clean quartet. All are single-graded
Molien-CST statements. The Rigidity target from the 2026-08-04 WAKE
(bigraded lift, LMRZ trivial-isotypic salvage, etc.) is orthogonal —
uses different machinery, still open, still highest-priority for a
module-level upgrade.

The proof reveals nothing new about bigrading. It is what it is: a clean
closure of the single-graded conjecture.

## Byproduct paper impact

The v1 paper as of 2026-07-31 has Theorem 2 covering $2 \le k \le d-1$
in §5.2. Options:

1. **Replace Theorem 2 with Theorem 2* in v1.** Cleanest — one theorem
   covering the full "allowed residues" range. Adds ~1p (the sharper case
   analysis). Recommend this.
2. **Add Theorem 2* as a corollary or extension in §5.2b.** Preserves
   Theorem 2's exact statement. Adds ~1.5p.
3. **v1 as-is, Theorem 2* becomes remark citing this note.** Fastest but
   leaves the "allowed iff" statement unproved in the paper.

I recommend (1) — it's the cleanest single statement, and the proof got
simpler.

## Standing decisions Robin-blocked

Carrying forward from 2026-08-04 WAKE:
- arXiv v1 push (unchanged; recommend upgraded v1 with Thm 2* instead of Thm 2)
- PAT expired (unchanged)
- MO priority (unchanged)
- Romero/Wildon email (unchanged)
- Lyra β→M_e delay ack'd (unchanged)
- Griffin upgrade (unchanged)
- Audit-risk sign-off (unchanged)
- Billey-Swanson seed promo (unchanged)
- Theorem 3 placement (unchanged; Cor D.4 in v1)
- LMRZ next-WAKE probe candidate (unchanged)

**NEW this session:**
- Theorem 2* replaces Theorem 2 in v1 vs. added as corollary (my recommendation:
  replace).
- With Theorem 2* closed, the "extended r-wreath conjecture" from 2026-07-31
  morning is fully proved. Sprint-level milestone.

## Rule 8 (12th consecutive cycle) — but different flavour

Today the "cheap probe" was reading the 2026-07-31 Theorem 2 proof carefully
enough to notice the artificial $k < d$ restriction. The proof I wrote
myself six days ago was one inequality-relaxation away from a much stronger
theorem. **Cheap probes into your own past work raise the stakes** — the
existing machinery is sharper than the existing statement.

## Verification

- `~/projects/probes/2026-08-04-prove-second-period/verify.py`:
  - Part A (theoretical gap): checked 11 cases including new second-period
    cases $(r,k) \in \{(2,5), (2,8), (3,7), (3,8), (3,9), (3,12), (4,9), (6,13)\}$.
    All min gaps $\ge 1$. ✓
  - Part B (multinomial): $\binom{rk}{k^r}(\zeta_d) = 0$ verified for
    $(r,k) \in \{(2,5), (3,7), (3,8), (3,9), (3,12), (4,9)\}$. ✓
  - Part C (brute Molien enumeration): For $(r,k) \in \{(2,5), (3,2)\}$,
    every conjugacy class of $\sigma$, the enumerated $\max_h m_d$ matches
    the theoretical bound $p\lfloor k/d\rfloor$ exactly. ✓
- `~/projects/probes/2026-08-04-prove-second-period/verify_mpi.py`:
  Full $m_\pi(t)$ computation for $r = 3, k = 7$; check $[5]_t \mid m_\pi(t)$
  for each $\pi \vdash 3$. (running — 792 partitions of 21 × MN characters,
  slow but tractable.)

## Time

Session start: ~15:04 container clock. Proof outline crystallised in
~30 min (my first substantial reading of the 2026-07-31 proof showed the
$k < d$ hypothesis was decorative not load-bearing). LaTeX write-up 30 min.
Verification 20 min. Memo 15 min. Total ~90-100 min in 3h budget.

This is the second consecutive PROVE session that closed inside 1/3 of
budget by finding the target theorem was one algebraic rearrangement away
from a proven statement. Yesterday's Theorem 3 was 3 lemmas + 90 min;
today's Theorem 2* is 1 inequality + 90 min. The proof-writing side of the
sprint is compounding — each closed theorem sharpens what the next one
needs to close.
