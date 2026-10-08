# PROVE 2026-08-08 — Odd-$e$ Type-B Self-Similarity Closed

## TL;DR

Type-B self-similarity for **odd $e$** is proved end-to-end:
$$\boxed{\ q_e^{B,(n)} \;=\; p_e(x)^{k} \cdot q_e^{B,(r_0)}, \quad e \text{ odd}, \; k = \lfloor n/e \rfloor, \; r_0 = n \bmod e.\ }$$

The proof is `~/projects/proofs/2026-08-08-type-b-self-similarity-odd-e.{tex,pdf}` (7 pages). It is a mechanical translation of the type-A self-similarity theorem (2026-08-07) exactly as the discovery report predicted, but the arithmetic is cleaner than expected. The coefficient identity
$$c^{B,(n)}_{(e^k, \alpha'), \beta} \;=\; c^{B, (r_0)}_{\alpha', \beta}$$
holds as **literal equality in $\mathbb Z[\zeta_e]$**, not merely up to units.

## The mechanism

Three orthogonal cancellations, one classical cyclotomic collapse:

1. **$e$-cycle numerator zeros ↔ $(1-t^e)^k$ denominator zeros.** By L'Hôpital on $u = t^e$:
   $$\lim_{t \to \zeta_e} \prod_{m=1}^k \frac{1 - t^{2em}}{1 - t^e} = \prod_{m=1}^k 2m = 2^k \cdot k!.$$

2. **The $2^k k! e^k$ prefactor from $z^B_{(\alpha, \beta)} = 2^k k! e^k \cdot z^B_{(\alpha', \beta)}$** absorbs the $2^k k! e^k$ arising from (1) together with the extra full-cycle factor.

3. **Non-$e$-cycle numerator factors** decompose as $e^k \cdot \prod_{s=1}^{r_0}(1-\zeta_e^{2s})$ via the reindexing $\phi(s) = 2s \bmod e$ (a bijection on $\{1, \ldots, e-1\}$ for odd $e$). The $e^k$ is $\prod_{r=1}^{e-1}(1-\zeta_e^r)^k$ by Lemma 2.1 (classical $\prod_r \alpha_r = e$).

The remainder is literally the parameter-$r_0$ coefficient formula.

## Why the negative side is inert

For odd $e$: $\zeta_e^b = -1$ has **no integer solution $b$** (since $-1 = \zeta_e^{e/2}$ requires $e$ even). Hence $\prod_{b \in \beta}(1 + \zeta_e^b)$ is a nonzero element of $\mathbb Z[\zeta_e]$ for every $\beta$; the negative bipartition $\beta$ enters every coefficient as a benign multiplicative constant, appearing identically on both sides of the theorem.

## Sanity check (Section 8 of the proof)

At $(n, e) = (5, 3)$, so $k = 1$, $r_0 = 2$; take $(\alpha, \beta) = ((3, 2), \emptyset)$:

- **Direct** $\Psi^B_{(3,2), \emptyset}(\zeta_3)/z^B$: numerator has zeros at $i=3$ ($t^6$) and denominator at the $3$-cycle ($t^3$); L'Hôpital gives $\Psi^B = 2\alpha_1^2 \alpha_2$, dividing by $z^B = 24$ and using $\alpha_1 \alpha_2 = 3$: coefficient $= \alpha_1/4$.
- **Closed form (Prop 4.1):** $\alpha_1^{g_1(2) - 0}\alpha_2^{g_2(2) - 1}/z^B_{(2), \emptyset} = \alpha_1/4$ (using $g_1(2) = g_2(2) = 1$, $z^B_{(2), \emptyset} = 4$).
- **Comparison target** $c^{B, (2)}_{(2), \emptyset} = (1-\zeta_3^4)/4 = \alpha_1/4$.

All three give $(1-\zeta_3)/4$ exactly. **Verified computationally with $\mathbb Z[\zeta_3]$ arithmetic** (see below).

```
prod_{r=1,2} (1 - zeta_3^r) = 3         (Lemma 2.1)
c^{B,(5)}_{(3,2),emp} direct = [1/4, -1/4]   # = 1/4 - zeta/4
c^{B,(5)}_{(3,2),emp} closed = [1/4, -1/4]
c^{B,(2)}_{(2),emp}         = [1/4, -1/4]
Match: True
```

## The five theorems of the character-level composite-$d$ story (as of 2026-08-08)

| # | Session       | Result                                                           |
|---|---------------|------------------------------------------------------------------|
| 1 | 2026-08-05    | Theorem A: composite-$d$ closure ($k=2$)                        |
| 2 | 2026-08-05    | Theorem B: $\Phi_9$ unconditional at $(r, k, e) = (5, 4, 9)$    |
| 3 | 2026-08-06 AM | Support theorem on $q_e$ (type A)                               |
| 4 | 2026-08-07    | Type-A self-similarity $q_e^{(n)} = p_e^k q_e^{(r_0)}$          |
| 5 | 2026-08-08 PM | **Type-B odd-$e$ self-similarity** $q_e^{B,(n)} = p_e^k q_e^{B,(r_0)}$ |

Follow-up: type-B even-$e$ self-similarity (substantive; needs strictly stronger support theorem + $\Psi^B_{\emptyset,(e/2,e/2)}(\zeta_e) = 2e^2$ identity; deferred).

## Verschiebung projected 3×, needed 0× — again

The 2026-08-06 dream projected Ayyer–Kumari 2501.00275 (odd-power-of-even-root factorisation, the type-B/C/D analogue of Albion's Verschiebung) as the tool for type-B self-similarity. The odd-$e$ proof bypasses it entirely: Chevalley–Molien + one line of classical cyclotomy again suffices. This is now the **third consecutive instance** in the 2026-08 sprint where a projected 2025 tool was undercut by a 1955-era mechanism:

- Support conjecture (2026-08-06 morning): Chevalley–Molien beats Verschiebung.
- Type-A self-similarity (2026-08-07): $\prod_r \alpha_r = e$ beats Verschiebung.
- Type-B odd-$e$ self-similarity (this session): Chevalley–Molien + reindexing $i \mapsto 2i$ beats Ayyer–Kumari.

Even-$e$ may still need Ayyer–Kumari machinery (the negative side is no longer inert, and the reindexing is $2$-to-$1$); TBD.

## Standing decisions (Robin-blocked; deltas from this morning's WAKE)

- **arXiv v1 push** — STILL UNBLOCKED, 6th consecutive day. **STRONG RECOMMEND PROCEED.**
- **UPDATED: Composite-$d$ paper** now spans type A + type B odd $e$ (5 theorems). Type-B even-$e$ deferred.
  - Recommend standalone at FPSAC 2026 (submission deadline research needed).
- **NEW: Type-B odd-$e$ proof DONE** ← was the top of the next-PROVE queue.
- **NEW: Type-B even-$e$ proof** = next-PROVE candidate (~6-10pp, substantive; needs items (i)-(iii) from discovery report §4).
- **UNCHANGED: Next-WAKE ordering** — (B) Chou–Hanada 30-min dim probe → (D) Szendrői 60-90 min. Item (A) [odd-$e$ type-B PROVE] ← DONE this session.
- **UNCHANGED:** Hopkins MO 338656 essay (post-v1), two Lyra promises queued post-v1, correspondence queue.
- **Fetch cache 34 → 34** (no additions).

## Aesthetic note

The type-A proof at $(2026-08-07)$ needed a genuine cancellation step: the byproduct formula had a $k + \mathbf 1[r \le r_0] - m_r(\nu)$ exponent that split as $k + [\text{rest}]$, requiring $\prod_r \alpha_r^k = e^k$ to be pulled out and cancelled against the $e^k$ in $z_\mu = e^k k! z_\nu$. In type B odd $e$, **the analogous split happens inside the numerator itself**: the "extra full-cycle residues" from $i = 1, \ldots, ke$ (excluding multiples of $e$) automatically give exactly $\prod_r \alpha_r^k = e^k$, which then cancels the $e^k$ in $z^B_\alpha = e^k k! \cdot 2^k \cdot z^B_{\alpha'}$. The cancellation isn't between the byproduct formula and a cyclotomic identity — it's between the geometry of the residue orbits and the type-B centraliser structure. Cleaner.

The $\phi(s) = 2s \bmod e$ reindexing is where the "type-B degrees are twice type-A degrees" fact enters. For odd $e$, it's a bijection (so nothing changes at the multiset level). For even $e$, it's $2$-to-$1$ and everything reshuffles — which is exactly why the even-$e$ story is substantively different.

## Files

- `~/projects/proofs/2026-08-08-type-b-self-similarity-odd-e.tex` — full proof, 7pp
- `~/projects/proofs/2026-08-08-type-b-self-similarity-odd-e.pdf` — compiled PDF
- `~/projects/proofs/2026-08-08-type-b-self-similarity-discovery.tex` — discovery report from this morning (context)
- `~/projects/probes/2026-08-08-type-b-self-similarity/` — the 24-pair compute

## Time budget

~60 min (PROVE session with 90-min budget). ~30 min for the proof draft, ~30 min for LaTeX compilation + computational sanity check + this memo. The theorem was indeed mechanical, as the WAKE session predicted.
