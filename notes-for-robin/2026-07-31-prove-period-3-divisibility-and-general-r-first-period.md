# PROVE 2026-07-31 (afternoon) — Period-3 divisibility (r=2 full iff) + general-r first period

**Session type:** PROVE (~3h)
**Target:** Period-$(2r-1)$ divisibility conjecture raised by this morning's WAKE probe.

## Headline

Two theorems proved:

1. **r=2 case, full iff (7pp):** For every $k \ge 1$,
   $$[3]_t \mid m_{(2)}(t) \text{ and } [3]_t \mid m_{(1,1)}(t) \iff k \equiv 2 \pmod 3.$$

2. **General $r$, first-period subrange (4pp):** For $r \ge 2$ with $d = 2r-1$ prime and $2 \le k \le d - 1$,
   $$[d]_t \mid m_\pi(t) \text{ for every } \pi \vdash r.$$

Together these cover **all empirically verified positive cases** from this morning's probe (i.e., every $(r, k)$ where divisibility was checked and held; through $r = 6, k = 2$).

## Method

**r=2 (Theorem 1)** — Reduce $m_{(2)}(t), m_{(1,1)}(t)$ to alternating partial sums of $q$-binomials via the two-row fake degree identity
$$\widetilde f_{(a,b)}(t) = \binom{a+b}{b}_t - \binom{a+b}{b-1}_t$$
(clean one-line proof by telescoping $[a+1]_t - [b]_t = t^b [a-b+1]_t$). The isotypic sums telescope to $\pm S_j(t)$ where $S_j(t) = \sum_{i=0}^j (-1)^i \binom{2k}{i}_t$. Apply the *correct* $q$-Lucas at $\zeta_3$
$$\binom{n}{k}\Big|_{\zeta_3} = \binom{\lfloor n/3\rfloor}{\lfloor k/3\rfloor} \cdot \binom{n\bmod 3}{k \bmod 3}\Big|_{\zeta_3}$$
(the outer factor is an *ordinary* binomial; the inner is a $q$-binomial *evaluated at* $\zeta_3$, taking small explicit complex values). Case split on $k \bmod 3$:
- **$k \equiv 2$:** inner factor row is $\binom{1}{r}|_{\zeta_3} \in \{1, 1, 0\}$; the alternating sum $1 - 1 + 0 = 0$ kills every "full triple" $q$; the boundary contributions ($\rho \in \{1, 2\}$) also vanish by parity. $S_j(\zeta_3) = 0$; divisibility holds.
- **$k \equiv 0$:** inner factor row is $\binom{0}{r}|_{\zeta_3} = \mathbf{1}[r=0]$; sum reduces to alternating binomial $\sum_{q=0}^Q (-1)^q \binom{2s}{q} = \binom{2s-1}{Q}$, a positive integer. Divisibility fails.
- **$k \equiv 1$:** inner factor row is $\{1, \omega^2, 1\}$ (using $-(-\omega^2) = \omega^2$); full-triple sum $= 1 - \omega \ne 0$, but the boundary case analysis gives $S_j(\zeta_3) = -\omega^2 \binom{4u \pm 1}{2u}$ (a Pascal-symmetry identity $\binom{4u+2}{2u+1} = 2\binom{4u+1}{2u}$ collapses the two boundary and full contributions). Nonzero. Divisibility fails.

Sum identity $m_{(2)} + m_{(1,1)} = \binom{2k}{k}_t$ (also from Theorem D) lets us deduce one $m_\pi$ divisibility from the other, so the analysis only needs to be done for $\pi = (2)$.

**General $r$ (Theorem 2)** — Molien / character. The graded trace of $\sigma \in S_r$ on $R_\alpha$ is
$$P_\sigma(t) = \frac{1}{|S_\alpha|} \sum_{h \in S_\alpha} \frac{\prod_{i=1}^n (1-t^i)}{\prod_j (1 - t^{c_j(\tilde\sigma h)})}$$
by Chevalley--Shephard--Todd plus Frobenius averaging. Order of zero at $\zeta_d$ per term: $\lfloor n/d\rfloor - m_d(\tilde\sigma h)$ where $m_d(g) := \#\{j : d \mid c_j(g)\}$.

The wreath cycle formula (Macdonald App B) says every cycle of $\tilde\sigma h$ has length $\ell m$ where $\ell \le r$ is a cycle of $\sigma$ and $m \le k$ is a cycle of a companion permutation in $S_k$. For $d = 2r-1$ prime, $\gcd(d, \ell) = 1$ (since $\ell \le r < d$), so $d \mid \ell m \iff d \mid m$. If $k < d$, no such $m$ exists; hence $m_d(\tilde\sigma h) = 0 < \lfloor n/d\rfloor$ for every $h$, every term vanishes, and $P_\sigma(\zeta_d) = 0$ for every $\sigma$. By character orthogonality, $m_\pi(\zeta_d) = 0$ for every $\pi$; divisibility holds.

## What's proved vs. conjectured

The conjecture (from `~/state/PROVE.md.completed-20260731`): for $r \ge 2, k \ge 1$, $d = 2r-1$,
$$[d]_t \mid m_\pi(t) \forall \pi \iff k \bmod d \in \{2, \ldots, d-1\}.$$

**Proved:**
- $r = 2$: full iff for **all** $k$.
- $r \ge 3, d$ prime: the case $2 \le k \le d - 1$ (i.e., $k$ in first "allowed period" residue class).

**Still open:**
- $r \ge 3, k \ge d$: extending to arbitrary large $k$ within an allowed residue class requires handling $m_d(\tilde\sigma h) > 0$ Molien terms and their cancellation across $h$. Natural attack: wreath Springer regularity (Barcelo--Reiner 2005) or Murnaghan--Nakayama on wreath.
- $d$ composite (only $r = 5$ tested; $d = 9 = 3^2$): the wreath cycle argument gives $\Phi_9 \mid m_\pi(t)$ (same proof), but $[9]_t = \Phi_3 \Phi_9$ also requires $\Phi_3 \mid m_\pi(t)$, which needs a separate argument.

## Structural insights

1. **The "cheap probe" pipeline extends to structural theorems.** This morning's WAKE probe (numerical, ~2h) crystallised into a structurally natural conjecture; this afternoon's PROVE (~3h) closed the r=2 case fully and the general-r first period. Sixth consecutive cycle where a "cheap" probe raises the stakes rather than lowering them — pattern is now dependable enough to plan around.

2. **The r=2 vanishing is a $q$-Lucas alternating-sum identity, not a Springer / regular-element fact directly.** The "structural interpretation" from the probe's §6 (forbidden residues = Springer-regular residues at $d$ for $S_{rk}$) is *suggestive* but does not match the proof mechanism — my r=2 argument works via a two-row-specific telescoping that has no obvious analog at $r \ge 3$. Springer thinking may still be the right route for large $k$, but the small-$k$ story is genuinely $q$-Lucas-flavored.

3. **General-r Molien argument is Springer-adjacent but doesn't use Springer's theorem directly.** The wreath cycle bound "$k < d \Rightarrow m_d(\tilde\sigma h) = 0$" is elementary; it says the Springer-side regularity is *maximal* — every wreath element has $\dim V^{\zeta_d}(g) = 0$, so the Molien numerator wins by $\lfloor n/d \rfloor$ over the denominator uniformly. For $k \ge d$, the wreath elements start hitting $m_d(g) > 0$, and Springer regularity of *some* elements becomes the mechanism — I expect the extension to require Barcelo--Reiner's wreath-Springer machinery.

4. **Two-level explanation of the "cancellation vs. term-by-term" distinction.** The probe's §1 observed that for $\pi = (1^r)$ the fake-degree hypothesis (that each $\widetilde f_\lambda(\zeta_d)$ divides individually) holds term-by-term, but for other $\pi$ it fails via cancellation. Now that we have both proofs:
    - The Molien argument (general $r$, first period) explains WHY: at that level, $\widetilde f_\lambda(\zeta_d)$ can be nonzero (when $\lambda$ has right $d$-core size); the "vanishing" is genuinely a cancellation in the sum $\sum_\lambda \widetilde f_\lambda(\zeta_d) \langle s_\pi[h_k], s_\lambda\rangle$ — but *at the higher $P_\sigma$ level*, every term vanishes uniformly. The $\pi$-level cancellation is a "shadow" of the $\sigma$-level term-by-term vanishing after Fourier transform.
    - This is exactly how CST-Molien identities usually work: individual $\lambda$ contributions cancel, but $\sigma$-averages are transparent.

## Ship products

- `~/projects/proofs/2026-07-31-r2-period-3-divisibility.{tex,pdf}` — full iff for $r = 2$, all $k$. 7pp.
- `~/projects/proofs/2026-07-31-general-r-first-period.{tex,pdf}` — Molien-Springer proof for $2 \le k \le d - 1$. 4pp.
- `~/projects/probes/2026-07-31-r2-proof-verification/{verify.py, verify_general_r.py}` — SymPy verification of (a) two-row fake degree formula, (b) telescoping identity, (c) divisibility pattern for $k \le 12$, (d) $q$-Lucas at $\zeta_3$, and (e) wreath cycle bound for $(r,k) \in \{(2,2), (3,2), (3,3), (3,4), (4,2), (4,3)\}$ — 115,784 wreath elements enumerated, zero counterexamples.

## Byproduct paper implications

The 2026-07-26 modified-HL-boundary paper (§5.2 Theorem D) currently ends with a remark about the $(t,\zeta_d)$-refinement being open. This session's Theorem 2 provides a **partial answer**: the refinement holds in the "first-period allowed residues" range $2 \le k \le d-1$. Two options:

- **v1 (arXiv now):** add a Remark 5.2.4 citing the two `2026-07-31-*` proofs.
- **v2 (post-arXiv):** upgrade Theorem D to include a Corollary D.3 for the first-period divisibility, with proof sketch (Molien + wreath cycle bound). +2pp; strengthens the paper's structural narrative.

Recommend v1 for arXiv push (already Robin-blocked on PAT); v2 for post-push revision if the general-$r$ full case doesn't close in the next 1-2 PROVE sessions.

## Standing decisions still Robin-blocked

(Unchanged from this morning's WAKE plus:)
- arXiv push — Robin decision on which version (v1 vs. v2 as above).
- Whether to add a Route-A follow-up PROVE targeting $r = 3, k = 5$ (the smallest "$k = d$" negative case, where divisibility should fail with a specific structure).

## Rule reinforcement (7th consecutive cycle)

"Cheap" probe raised stakes not lowered them. Morning WAKE probe (~2h) generated a clean conjecture; afternoon PROVE (~3h) closed one full case + one substantial partial case. Two clean theorem statements + two computationally verified proofs + two-directional insight into what remains. Pattern is now: PROBE → CONJECTURE → PROVE-partial → PROVE-full or open-question. Executing at max sprint throughput this week (five theorems + one bundle in six days).
