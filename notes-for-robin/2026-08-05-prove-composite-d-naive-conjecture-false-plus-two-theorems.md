# 2026-08-05 PROVE — Composite-$d$ naive conjecture is FALSE; Theorem A ($k=2$) and Theorem B ($(5,4)$, $\Phi_9$) proved

**Session:** PROVE (~3h), second session of container-day 2026-08-05. Structured by `/prove` skill. Sub-agents for computation only; proof thread mine.

## TL;DR

The composite-$d$ extension of Theorem 2 (as stated in `PROVE.md`) is **FALSE**. Empirical scan at $r=5, d=9$ (smallest composite-$d$) shows the strong divisibility fails at $k=3$ and $k=4$. Two positive theorems and one negative theorem land, in a single 6-page standalone `.tex` at `~/projects/proofs/2026-08-05-composite-d-k2-and-negative.pdf`:

- **Theorem A ($k=2$).** For every $r \ge 2$ and every divisor $e > 1$ of $d = 2r-1$: $\Phi_e(t) \mid m_\pi(t)$ for all $\pi \vdash r$. Hence $[d]_t \mid m_\pi(t)$. Clean parity-of-odd-multiplicity argument on $p_\lambda[h_2]$; special to $k = 2$.

- **Theorem B (unconditional at $(5,4), e=9$).** $\Phi_9(t) \mid m_\pi(t)$ for all $\pi \vdash 5$ at $k = 4$. Proof combines (a) computational structure theorem for $q_9$ (support on $\{p_{9,9,2}, p_{9,9,1,1}\}$, verified over all 627 partitions of 20) with (b) factorisation-count obstruction ($\lambda \vdash 5$ can't produce two 9's in $p_\lambda[h_4]$).

- **Theorem C (negative).** At $(5,3)$: $\Phi_3 \nmid m_\pi$ for any $\pi \vdash 5$; $\Phi_9 \mid m_\pi$ only for $\pi = (3,1,1)$. At $(5,4)$: $\Phi_3 \mid m_\pi$ only for $\pi = (3,1,1)$. At $(5,3)$ the $\Phi_3$-failure is structurally forced — the $q$-multinomial itself is not $\Phi_3$-divisible.

## The flip

The PROVE.md target was: "for composite $d$, same iff-on-residues as prime $d$." I started with the /prove protocol: compute first, prove second. The empirical scan at $(5, 3)$ took ~5 min via a fresh $m_\pi(t) \bmod \Phi_e$ script (avoiding full-polynomial expansion). Result: $\Phi_3 \nmid m_\pi$ for every $\pi \vdash 5$; $\Phi_9 \mid m_\pi$ only for $\pi = (3, 1, 1)$.

Sanity-checked against `verify_mpi.py`'s $\sum f^\pi m_\pi = q\text{-multinomial}$ identity — passes. So the failure is real.

Diagnosed the $\Phi_3$-failure at $(5, 3)$: the $q$-multinomial $\binom{15}{3^5}_t$ has $\Phi_3$-valuation $\lfloor 15/3\rfloor - 5\lfloor 3/3\rfloor = 5 - 5 = 0$. No cancellation across $\pi$ can rescue $\Phi_3$-divisibility of every $m_\pi$. **This is a structural obstruction that yesterday's WAKE-late conjecture missed.**

The prior empirical scan (2026-07-31) had only tested $(5, 2)$ for composite $d$ — the one case where the naive extension happens to work. Beyond that, "expensive plethysm" killed it at 33 min. The composite-$d$ extrapolation was in that gap.

## What Theorem A actually proves and why it matters

For $k = 2$: $p_j[h_2] = (p_j^2 + p_{2j})/2$. Every factor in $\prod_i p_{\lambda_i}[h_2]$ contributes either two copies of $\lambda_i$ or one copy of $2\lambda_i$. **Odd parts arise only in pairs.** So any $p_\nu$ appearing in the expansion of $s_\pi[h_2]$ has all odd values with even multiplicity.

For $e \mid d$ with $d = 2r-1$ odd: $e$ is odd, and $e \mid d = n-1$ where $n = 2r$, so Springer regular exists with cycle type $(e^{d/e}, 1)$. Springer + Theorem D + Frobenius:
$$m_\pi(\zeta_e) = \langle s_\pi[h_2], p_e^{d/e} p_1 \rangle.$$
The target has multiplicity 1 of the odd value 1 — odd count. Contradiction with parity, so the inner product vanishes. Hence $\Phi_e \mid m_\pi$ for every $\pi$.

This is orthogonal to (and stronger than) Theorem 2 in the following sense: Theorem 2 covers prime $d$ for $2 \le k < d$; Theorem A covers ALL $d$ (prime or composite) but only at $k = 2$. For $r = 5$ (smallest composite-$d$ case) at $k = 2$: the empirical scan of 2026-07-31 was confirmed, now with proof.

## What Theorem B is and why the mechanism generalises

At $(5, 4), e = 9$: no Springer regular of order 9 in $S_{20}$ (since $9 \nmid 20, 9 \nmid 19$). But: define $q_e := \sum_\lambda \fdeg_\lambda(\zeta_e) s_\lambda \in \Lambda_n \otimes \ZZ[\zeta_e]$; then $m_\pi(\zeta_e) = \langle s_\pi[h_k], q_e\rangle$ by Theorem D.

Computationally (over all 627 partitions of 20): $q_9$ is supported exactly on $\{p_{9,9,2}, p_{9,9,1,1}\}$. Coefficients $\frac{162(1-\zeta_9)}{z_{(9,9,2)}}$ and $\frac{162(1+\zeta_9)}{z_{(9,9,1,1)}}$.

Then the pairing $\langle s_\pi[h_4], p_{9,9,\nu}\rangle$ vanishes for all $\pi \vdash 5$ because: to produce two 9's in the power-sum expansion of $p_\lambda[h_4]$, need two indices $i$ with $\lambda_i = 3$ and $\alpha^{(i)}$ containing a 3 (only feasible factorisation of 9 given size constraints). But $\lambda \vdash 5$ has at most one 3.

Result: $\Phi_9 \mid m_\pi(t)$ for all $\pi \vdash 5$. Unconditional (given the computational $q_9$ result at $n = 20$).

**Generalisation hook:** if the support conjecture (Conjecture 4.4 in the .tex) is proved, this argument extends to any $(r, k, e)$ where the factorisation-count obstruction rules out $\lfloor rk/e\rfloor$ parts of size $e$ from $p_\lambda[h_k]$. The support conjecture is empirically confirmed for all tested $(n, e)$; a general proof presumably goes through Kraskiewicz-Weyman analysis of fake degrees at roots of unity via $e$-cores and $e$-quotients.

## Standing decisions and updates

**Robin-blocked queue (updated):**
1. **arXiv v1 push** — REMAINS UNBLOCKED. Today's content is orthogonal to the current byproduct paper's scope (prime-$d$ only). Recommend proceed unchanged (per 2026-08-05 morning-WAKE recommendation, augmented by Thm 2 → Thm 2* replacement).
2. **NEW:** Composite-$d$ extension IS NOT the "same statement, more divisors" hoped for on 2026-07-31 morning. Do NOT include naive Theorem 2** conjecture in v1 or v2. If composite-$d$ deserves a paper, it's a *separate* piece with (a) Theorem A (clean, $k=2$), (b) Theorem B (single case, $(5, 4)$), (c) support conjecture on $q_e$ as central open problem.
3. **NEW:** Support conjecture on $q_e := \sum_\lambda \fdeg_\lambda(\zeta_e) s_\lambda$ is well-worth investigating. Trivially true in Springer-regular cases; empirically true in tested irregular cases. If provable, unlocks a family of theorems in the shape of Theorem B.
4. Six-negatives salvage catalogue from morning WAKE — unchanged. Character-level quartet stands. Module-level upgrade unaffected.
5. Post-arXiv correspondence — unchanged (Douvropoulos, Josuat-Vergès, Bechtloff Weising per prior).

**No new Rule proposed today.** But Rule 12 fires positively: /prove protocol's "compute first" caught the false conjecture in ~5 min, saving weeks of proof-hunting for a false target. Rule 8 fires 16th consecutive cycle (cheap probes into own past assumptions keep raising stakes).

## Deliverables

- `~/projects/proofs/2026-08-05-composite-d-k2-and-negative.tex` — 6-page standalone proof of Theorems A, B, C.
- `~/projects/proofs/2026-08-05-composite-d-k2-and-negative.pdf` — compiled.
- `~/projects/probes/2026-08-05-composite-d/scan.py` — $m_\pi \bmod \Phi_e$ scan; reusable.
- `~/projects/probes/2026-08-05-composite-d/check_qe_support.py` — $q_e$-support verification.
- `~/projects/probes/2026-08-05-composite-d/qe_support.log` — $(n, e) = (20, 9)$ result.
- `~/projects/scratch/prove-2026-08-05-composite-d.md` — session notebook (false starts + insights).
- SUMMARY.md updated (this session at top).
- MEMORY.md pointer added (see below).

## For the dream cycle

- The support conjecture on $q_e$ is the correct next mathematical target. It's a symmetric-function-side result, provable from existing Kraskiewicz-Weyman machinery on $e$-cores and $e$-quotients. Not "invent new construction" — probably a 5-10 page paper if pursued.
- The factorisation-count obstruction (Lemma 4.5 in the .tex) generalises: for any $(r, k, e)$ with $e = e_1 e_2$ the only feasible factorisation with $e_1 \le r, e_2 \le k$, and $\lambda \vdash r$ having limited copies of $e_1$: same argument fires.
- The 2026-07-31 morning "extended r-wreath conjecture" was true for prime $d$ (via Theorem 2*) but false for composite $d$. Second-order lesson: extrapolation from prime to composite in wreath-cycle divisibility results is not safe — the multinomial obstruction at $\gcd(k, d) > 1$ is a real gate.
- Cylindric-path bridge unchanged. Sixth consecutive session where Robin's masters is load-bearing.
