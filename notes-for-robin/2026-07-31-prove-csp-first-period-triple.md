---
name: 2026-07-31 PROVE — CSP triple for first-period Molien-Springer vanishing
description: PROVE session upgrading Theorem 2 to a Reiner-Stanton-White cyclic sieving triple; explicit X, action, and 3-ingredient proof
type: project
---

# PROVE — Cyclic sieving triple for the period-(2r−1) Molien-Springer vanishing (first period)

**Date:** 2026-07-31 (PROVE session; ~90 min from PROVE.md-read to theorem-closed).

## Headline

**Theorem 3 (Cyclic sieving, first period).** Fix $r \ge 2$ with $d = 2r-1$ prime and $2 \le k \le d-1$. Let $H = S_k \wr S_r \le S_n$ ($n = rk$), and let $\rho \in S_n$ be any $d$-cycle. For every $\pi \vdash r$, the triple
$$
\bigl(X_{\pi,k},\ C,\ m_\pi(q)\bigr)
\quad\text{with}\quad
X_{\pi,k} = (S_n/H) \times \mathrm{SYT}(\pi),\ \ C = \langle \rho\rangle \cong \mathbb{Z}/d,
$$
and $C$ acting by translation on the coset factor and trivially on the tableau factor, is a **Reiner-Stanton-White cyclic sieving triple**.

This is the exact PROVE.md target of this morning's re-seed after the two negative probes (Amdeberhan-Beck coefficient inequality, joint $(\zeta_3, \zeta_3^{-1})$ CSP specialisation) established that Clio's proved fact is *cyclic* not *dihedral* sieving.

## The 3-ingredient proof

Three cheap lemmas closing the proof in 6pp:

1. **Cardinality lemma** (2026-07-31 PROVE): $m_\pi(1) = f^\pi \cdot [S_n:H]$ for every $r, k \ge 1$ and every $\pi \vdash r$. Proof: substitute $t=1$ in Theorem D, use $\sum_\lambda f^\lambda s_\lambda = h_1^n$, then Frobenius reciprocity + $\dim \mathrm{Ind}_H^{S_n}(V) = [S_n:H] \cdot \dim V$. **This gives $|X_{\pi,k}| = m_\pi(1)$.**

2. **Freeness lemma** (this session; cousin of the wreath cycle bound of Theorem 2): $H = S_k \wr S_r$ contains no element of order divisible by $d$ when $k < d$. Direct from cycle-length lemma: cycles of $\tilde\sigma h$ have length $\ell m$ with $\ell \le r < d, m \le k < d$; $d$ prime forces $d \nmid \ell m$. Therefore no fixed cosets of $\rho^j$ on $S_n/H$ for $j \ne 0$.

3. **Vanishing lemma** (Clio Theorem 2, proved earlier today): $[d]_t \mid m_\pi(t)$, hence $m_\pi(\zeta_d^j) = 0$ for $j \not\equiv 0 \pmod d$.

Combining: at $j = 0$, both sides of the CSP identity equal $|X_{\pi,k}| = m_\pi(1)$ (Lemma 1). At $j \ne 0$, both sides equal 0 (Lemmas 2, 3). Done.

Full write-up: `~/projects/proofs/2026-07-31-cyclic-sieving-first-period.pdf` (6pp).

## Structural remarks

**On the "content" of the CSP identity.** At $j \ne 0$, both sides of the CSP identity are 0. This makes the CSP identity look tautological. What Theorem 3 actually packages is: (i) the polynomial $m_\pi(q)$ has zeros at all nontrivial $d$-th roots of unity (this is Theorem 2, the mathematically hard part); (ii) the *natural* coset set $S_n/H$ has size $[S_n:H]$ dividing $m_\pi(1)$ in a way compatible with a free $\mathbb{Z}/d$-action. Together they place the vanishing into the RSW framework alongside Rhoades' promotion-CSP for SYT and Springer's regular-element theory.

**On the $\mathrm{SYT}(\pi)$ factor.** The second factor $\mathrm{SYT}(\pi)$ is a "silent" factor: $C$ acts trivially on it. It's needed for the count to hit $m_\pi(1) = f^\pi \cdot [S_n:H]$. Cleaner (basis-free) reformulation: $\mathbb{C}[X_{\pi,k}]$ is a permutation model for the induced module $\mathrm{Ind}_H^{S_n}(\mathrm{triv} \boxtimes S^\pi)$ *restricted to $\langle\rho\rangle$*. SYT$(\pi)$ is a natural index set for a basis of $S^\pi$ via Young's seminormal, giving a natural (rather than arbitrary) index set for the induced module.

**On alternative Springer proof at $k = 2$.** For $k = 2$, $n = 2r$, and $d = 2r-1$: $d \mid n-1$ so a $d$-cycle in $S_n$ is a Springer regular element of order $d$. In that case one can prove Theorem 3 via Springer's theorem $\widetilde f_\lambda(\zeta_d) = \chi^\lambda(\rho)$ combined with the empty-summation formula for induced characters. For $k \ge 3$, $S_n$ has no Springer regular element of order $d$, and the Molien proof (Theorem 2) is essential.

## Computational verification

Verified all three ingredients for $(r,k) \in \{(2,2),(3,2),(3,3),(3,4)\}$, all $\pi \vdash r$ (12 total $(r,k,\pi)$-triples). Sample:
- $(r,k,\pi) = (2,2,(2))$: $m_\pi(t) = 1+t^2+t^4 = [3]_t(1-t+t^2)$; $m_\pi(1) = 3 = 1 \cdot 3 = f^\pi \cdot [S_n:H]$. ✓
- $(r,k,\pi) = (3,2,(2,1))$: $m_\pi(t)$ degree 11, $m_\pi(1) = 30 = 2 \cdot 15$. ✓
- $(r,k,\pi) = (3,4,(2,1))$: $m_\pi(t)$ degree 47, $m_\pi(1) = 11550 = 2 \cdot 5775$. ✓

Script: `~/projects/probes/2026-07-31-prove-csp-verify/verify.py` (SymPy-only: fake degrees, plethysm via power-sum, Murnaghan-Nakayama). Every case passes the algebraic $[d]_t | m_\pi(t)$ divisibility test.

## What remains (out of scope for this PROVE)

1. **$k \bmod d \in \{2,\ldots,d-1\}$ with $k \ge d$.** The conjectured full period-$(2r-1)$ divisibility (Wake 2026-07-31 conjecture) extends beyond first period; Theorem 2 (and hence Theorem 3) only covers $k \le d-1$. For $k \ge d$, the freeness lemma fails ($H$ acquires $d$-torsion), so the coset-space CSP construction breaks — a genuinely new CSP set is needed.

2. **Composite $d$.** When $d = 2r-1$ is not prime (e.g., $r = 5$, $d = 9$), $[d]_t = \prod_{e | d, e > 1} \Phi_e$, and one must control vanishing at each primitive $e$-th root separately. Theorem 3's cyclic action $C = \mathbb{Z}/d$ is not the natural structure here (should be $\mathbb{Z}/e$ separately for each prime power $e | d$).

3. **Bigraded / dihedral upgrade.** Today's negative probes (`~/projects/probes/2026-07-31-wake-csp-joint-specialisation/`) ruled out the naive Zhu bigrading as a joint $(\zeta_d, \zeta_d^{-1})$-sieving. Whether a genuine bigraded refinement exists (Josuat-Vergès q,t-dihedral machinery, Zhu's orbit-harmonic bigrading) remains open. Would upgrade Theorem 3 from a "trivial-value" CSP to one where both sides carry more content.

## Byproduct paper impact

`~/projects/papers/2026-07-26-modified-HL-boundary/paper.pdf` (currently 15pp, four theorems):
- **§5.2 Theorem D and Corollary D.3** (the period-$(2r-1)$ divisibility) already stated.
- **Upgrade path**: add Theorem 3 as **Corollary D.4** or standalone Theorem E in §5.3. Additional length: ~1 page (statement + 3-ingredient proof reducing to Corollary D.3 + Lemma above). Would strengthen §5 from *divisibility of coefficients* to *cyclic sieving on natural combinatorial data*, matching Rhoades/Springer language.

Or defer as v2 material and land Theorem 3 as standalone note (current PDF). Recommend: keep standalone for now (aligned with Robin's "arXiv push v1 recommended" standing decision), cite as reference in v2 if paper grows.

## Rule 8 update

**8th consecutive cycle at Rule 8** ("cheap probes raise stakes"): today's WAKE-morning conjecture + PROVE-afternoon Theorem 2 + BROWSE-evening 4 convergences + WAKE-evening 2 corrective negatives + PROVE-evening Theorem 3 — full cycle in one container day. Cheap probes (Amdeberhan-Beck, CSP joint specialisation) corrected the frame from *dihedral* to *cyclic*, which then made the RSW target explicit, which then made the 3-lemma proof appear in 90 minutes.

The pattern is entrenched: every PROVE-scale theorem in the last 8 cycles has been preceded by a cheap negative or a cheap conjecture-crystallisation. Never bypass the cheap probe.

## Session summary

- **Time**: ~90 min from PROVE.md-read to theorem-closed. (Total 3h budget; ~90 min remaining, used for computational verification + write-up.)
- **Ships**: 1 proof PDF (6pp) + 1 verification script + 1 memo (this).
- **Estimated probability of clean theorem in 3h** (from PROVE.md): 55%. **Actual**: closed within 90 min. The structural bet in PROVE.md ("Once $X$ named, proof is 2-3pp") was accurate; the 3-lemma decomposition matched the "character orthogonality" intuition.
- **Standing decisions for Robin unchanged** (arXiv push still Robin-blocked, PAT still expired, MO drafts unchanged, ...). **NEW: recommend Theorem 3 land as v2 addition or standalone corollary**, not v1 blocker.

---

*Files:*
- Proof: `~/projects/proofs/2026-07-31-cyclic-sieving-first-period.{tex,pdf}` (6pp)
- Verification: `~/projects/probes/2026-07-31-prove-csp-verify/verify.py`
- This memo: `~/projects/memory/for-robin/2026-07-31-prove-csp-first-period-triple.md`
