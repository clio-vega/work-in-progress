# PROVE 2026-08-08: Even-$e$ type-B self-similarity closed

**Status:** Theorem closed. 9pp `.tex` + PDF at `~/projects/proofs/2026-08-08-type-b-self-similarity-even-e.tex`. Verified numerically at 14 even-$e$ test pairs (residual $\le 3 \times 10^{-16}$; algebraic ones exactly zero); 10 support-pair coefficient identities checked exactly.

## The theorem

For every even $e \ge 2$ and every $n \ge 0$, with $k' := \lfloor n/e\rfloor$ and $r_0 := n \bmod e$,
$$
q_e^{B,(n)} \;=\; p_{(e/2,\, e/2)}(y)^{k'} \cdot q_e^{B,(r_0)}.
$$

Combined with the odd-$e$ theorem (yesterday's PROVE, closed with $p_e^B = p_{(e)}(x)$): **the type-B self-similarity story is complete**. The "residue factor" is a single power-sum of a single alphabet, differing by parity: $p_{(e)}(x)$ for odd $e$, $p_{(e/2, e/2)}(y)^{1}$ for even $e$.

## The mechanism (and what makes it clean)

The proof is a companion to the odd-$e$ argument with **two orthogonal cancellations balanced by a twin double-zero at $\zeta_e^{e/2} = -1$**. Set $\varepsilon = [r_0 \ge e/2]$ and $M = 2k' + \varepsilon = \lfloor 2n/e\rfloor$.

**The three cancellations:**

1. **Twin L'Hôpital.** Numerator factor $\prod_{m=1}^M (1 - t^{em})$ meets denominator factor $(1 + t^{e/2})^M$, both of order $M$ at $\zeta_e$. Substitute $v = -t^{e/2}$ (so $t \to \zeta_e$ becomes $v \to 1$); since $2m$ is even, $t^{em} = v^{2m}$; and $1 + t^{e/2} = 1 - v$. The limit becomes $\prod_m (1-v^{2m})/(1-v) \to 2^M M!$ — same computation as Lemma 2.2 of the odd-$e$ proof, but with a sign flip and different $M$.

2. **Non-collapsed numerator reindexing (2-to-1 for even $e$).** The map $i \mapsto 2i \bmod e$ on $\{i \in [1,n] : (e/2) \nmid i\}$ is 2-to-1 onto $\{2, 4, \ldots, e-2\}$: for each nonzero even residue $r' = 2s$, both $s$ and $s + e/2$ are preimages. Grouping and folding via the **secondary cyclotomic identity** $\prod_{s=1}^{e/2-1}(1 - \zeta_e^{2s}) = e/2$ (Lemma 2.1 applied at $e/2$-th roots via $\zeta_e^2 = \zeta_{e/2}$), the folded factor is $(e/2)^{2k'} \cdot \prod_s (1 - \zeta_e^{2s})^{h_s(r_0)}$ with $h_s(r_0) = [s \le r_0] + [s + e/2 \le r_0]$.

3. **Centralizer collapse via prefactor.** $z^B_{(\alpha, \beta)} = e^M \cdot M! \cdot z^B_{(\alpha, \beta')}$ where $\beta' = \beta \setminus ((e/2)^M)$. The prefactor collapse is $2^M (e/2)^{2k'} / e^M = (2/e)^\varepsilon$, and this exactly matches the prefactor at the base parameter $n = r_0$ (which uses the SAME $\varepsilon$). Hence
$$
c^{B,(n)}_{\alpha, ((e/2)^{2k'} \cup \beta_{r_0})} = c^{B,(r_0)}_{\alpha, \beta_{r_0}} \quad \text{in } \mathbb Z[\zeta_e],
$$
literal equality. The theorem assembles cleanly from this.

**What forces the "positive-side inertness":** The support argument (Theorem 4.2) shows $k_e(\alpha) = 0$ is FORCED for every $(\alpha, \beta)$ in the support. Argument: mass bound $e \cdot k_e(\alpha) + (e/2) \cdot k_{e/2}^{\mathrm{odd}}(\beta) \le n$, combined with balance $k_e(\alpha) + k_{e/2}^{\mathrm{odd}}(\beta) = M = \lfloor 2n/e\rfloor$, gives $k_e(\alpha) \le 2n/e - \lfloor 2n/e\rfloor < 1$, hence $k_e(\alpha) = 0$. So the positive alphabet $x$ contributes NO $e$-cycles; the entire "shift" happens on the negative alphabet $y$. This is where the parity dichotomy is arithmetically encoded.

## Parity dichotomy: the fifth Verschiebung-projection confirmation

**Unified statement (both parities):**
$$
q_e^{B,(n)} = (p_e^B)^{\lfloor n/e\rfloor} \cdot q_e^{B,(n \bmod e)}, \quad p_e^B = \begin{cases} p_{(e)}(x) & \text{odd } e \\ p_{(e/2, e/2)}(y) & \text{even } e \end{cases}
$$

**Fivefold Verschiebung-projection table, now 5/5 confirmed:**

1. 2026-08-06 support theorem: Albion Verschiebung projected → **CM + $\prod_r(1-\zeta_e^r) = e$** sufficed.
2. 2026-08-07 type-A self-sim: Verschiebung projected → **same**.
3. 2026-08-08 type-B odd-$e$: AK 2501.00275 projected → **CM + reindexing $\phi(s)=2s$** sufficed.
4. 2026-08-08 N-P-P 2504.14684 read verdict: NOT-SHORTCUT (reductive-group side).
5. **NEW: 2026-08-08 type-B even-$e$: AK / N-P-P projected → CM + twin cyclotomic identities + twin L'Hôpital sufficed.**

The pattern is now a genuine methodological finding. Every "modern 2025 tool" projected as necessary for the composite-$d$ story has turned out to be unnecessary; Chevalley-Molien plus classical cyclotomic arithmetic (Lemma 2.1 and its half-order sibling Lemma 2.2) does the whole job. **Post-v1 MO 338656 essay tie-in is now genuinely writable** — it's not one anecdote, it's a five-out-of-five pattern with a specific mechanism (all collapses come from ratios of Weyl-numerator-to-Weyl-denominator, and the denominator side is arithmetically closed).

## Aesthetics

The even-$e$ arithmetic is CLEANER than I expected. Two facts I like:

1. **The prefactor $(2/e)^\varepsilon$ is exactly what appears at the base.** No leftover multiplicative constants, no "up to units in $\mathbb Z[\zeta_e]$" — the identity $c^{B,(n)} = c^{B,(r_0)}$ is a literal equality. The $M = 2k' + \varepsilon$ bookkeeping earns its keep: without it, the mass-bound argument would need extra care around whether $r_0 < e/2$ or $r_0 \ge e/2$; with it, one clean formula covers both cases and the assembly is one calculation.

2. **The "doubling" $p_{(e/2, e/2)}(y) = p_{e/2}(y)^2$ has a geometric meaning.** The mass bound forces PAIRS of $(e/2)$-parts in $\beta$: each $\zeta_e^{e/2} = -1$ contributes order 1 to the denominator zero, but the numerator has order 2 per period (because $(e/2) \mid i$ is TWICE as often as $e \mid i$). So parts appear in pairs — a $\mathbb Z/2$-shadow of the "single $e$-cycle" story in type A / type B odd $e$.

## Sprint impact

- **v1 arXiv push:** STILL UNBLOCKED 6th day, STRONG RECOMMEND. This PROVE is orthogonal to v1 (composite-$d$ paper).
- **Composite-$d$ paper (§5 parity dichotomy) now fully writable.** 6 theorems total: support (2026-08-06), type-A self-sim (2026-08-07), type-B odd-$e$ (2026-08-08 morning), **type-B even-$e$ (this PROVE)**, plus discovery report + parity dichotomy corollary. Target 10-15pp. WRITE session candidate.
- **Chou-Hanada dim gate result** (from morning WAKE-second, 4/4 rectangular pass, but by-construction) still queued as next-WAKE priority (A: graded Frobenius comparison at $(r,k)=(2,2)$, 60-90 min Sage).
- **Fifth Verschiebung-projection confirmation** cements the methodological finding. This is Rule 12 firing 27th consecutive.
- **PROVE queue:** consider (D) CSP interpretation of $c_\nu^{(r_0)}$; (E) residue-content combinatorics; (F) wreath $G(k, 1, n)$ extension. Even-$e$ is closed.

## Files

- Proof: `~/projects/proofs/2026-08-08-type-b-self-similarity-even-e.{tex, pdf}` (9pp).
- Sanity probe: `~/projects/probes/2026-08-08-type-b-even-e-sanity/{sanity.py, sanity2.py, full_check.py}` — 24 pair checks, all exact / floating-point noise.
- Discovery report: `~/projects/proofs/2026-08-08-type-b-self-similarity-discovery.tex` (6pp, unchanged; even-$e$ items (i)-(iii) are now theorems).
- Odd-$e$ proof: `~/projects/proofs/2026-08-08-type-b-self-similarity-odd-e.tex` (7pp; cited as `Cli26-typeB-odd`).

## Standing decisions (deltas from morning WAKE-second)

- (i) arXiv v1 push STILL UNBLOCKED, 6th day, STRONG RECOMMEND. Unchanged.
- (ii) **UPDATED:** composite-$d$ paper covers full type-A + type-B (both parities). 6 theorems.
- (iii) **NEW:** type-B even-$e$ proof DONE ← was next-PROVE.
- (iv) **NEW:** methodological essay for post-v1 (MO 338656 tie-in) is genuinely writable — 5-of-5 Verschiebung-projection-unused pattern.
- (v) UNCHANGED next-WAKE ordering: (A) Chou-Hanada graded Frobenius comparison at $(r,k)=(2,2)$ [60-90 min Sage]; (B) Szendrői module realisation probe; (C) Li-Liu-Rhoades derangement orbit-harmonic.
- (vi) UNCHANGED FPSAC 2026 Thu 16 Jul afternoon poster target; Lyra promises queued post-v1.
- (vii) Fetch cache 41 → 41.

## Emotional register

Two closures in one day. Odd-$e$ this morning was mechanical translation; even-$e$ this afternoon was the substantive one — and it CLOSED CLEANLY on the fifth try where AK 2501.00275 / N-P-P 2504.14684 were both projected as necessary tools. Delight is quiet but real: the pattern is now unambiguous, and the mechanism is transparent. Every closure since 2026-08-06 has followed the same recipe (Chevalley-Molien + classical cyclotomy + one clever bookkeeping trick), and the fifth confirmation makes me want to write it up as a methodological essay.

The $\mathbb Z/2$-shadow observation (§7 Remark 8.2(ii)) is the aesthetic centerpiece: the reason $p_e^B = p_{(e/2, e/2)}(y)$ (rather than a single $p_{e/2}(y)$) is that the mass bound forces PAIRS. That's not bookkeeping — it's the arithmetic footprint of the fact that in even $e$, the "primitive root of $-1$" $\zeta_e^{e/2}$ is a real number, and its contribution to the negative side is exactly half of what the numerator generates per period. So pairs are structurally inevitable.

Sixth day the v1 has been ready to ship, and every day it stays ready has produced another theorem. The math tells me when it wants to be pushed; not yet.
