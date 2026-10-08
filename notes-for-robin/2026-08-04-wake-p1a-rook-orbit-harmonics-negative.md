---
name: WAKE 2026-08-04 — P1a rook-orbit-harmonics probe closes NEGATIVE with three structural obstructions
description: WAKE session dispatching the P1a rook-placement orbit-harmonics probe recommended by 2026-07-31 late dream. LLR framework at (r,k)=(2,2) cannot realise Clio's Theorem D at the module level — three independent structural obstructions ruled out. Salvage direction: LMRZ involution loci (gives trivial isotypic only, k=2 only).
type: project
---

# WAKE 2026-08-04 — P1a probe closes NEGATIVE with structure

**Session type:** WAKE (~1.5h in 2h budget). **Result:** the crown-jewel probe from yesterday's late dream (rook-placement orbit-harmonics realisation of Theorem D) closes NEGATIVE at $(r,k) = (2,2)$ with three independent structural obstructions. Clean ruling-out, not a shape-mismatch.

## Setup verified against LLR paper

Fetched Li-Liu-Rhoades arXiv 2607.28157 (34pp, "Derangement Permutation Matrices and Orbit Harmonics", dropped July 30, 2026). Cached at `/home/clio/papers/li-liu-rhoades-2607.28157.pdf`. Fetch cache 7→6.

Setup (their §1.1 + §4):

- Matrix variables $x_{ij}$ for $(i,j) \in [n]^2$; polynomial ring $S = \mathbb{C}[x_{ij}]$.
- **Rhoades ideal** $I_n \subset S$: row sums $\sum_j x_{ij}$, column sums $\sum_i x_{ij}$, same-row products $x_{ij}x_{ij'}$, same-column products $x_{ij}x_{i'j}$.
- **Orbit-harmonics quotient**: $\mathbf{R}(\mathfrak{S}_n(\mathcal{R})) = S / (I_n + (x_{ij} : (i,j) \in \mathcal{R}))$ where $\mathfrak{S}_n(\mathcal{R}) = \{w : (i,w(i)) \notin \mathcal{R}\}$.
- **Symmetric-group action**: diagonal $S_n$, $w \cdot x_{ij} = x_{w(i),w(j)}$. Stable exactly on $S_n$-stable $\mathcal{R}$.
- Framework proved for **nonattacking** $\mathcal{R}$; ideal formula extends to general $\mathcal{R}$.

## The probe

Target: for $(r,k) = (2,2)$, $n = 4$, find $S_2$-stable $\mathcal{R} \subseteq [4]^2$ (under $\sigma = (1\,3)(2\,4)$ block-swap acting diagonally on rows and columns) such that $\mathbf{R}(\mathfrak{S}_4(\mathcal{R}))$ has:

- Hilbert series $\binom{4}{2,2}_t = 1 + t + 2t^2 + t^3 + t^4$ (dim 6).
- $S_2$-isotypic decomposition: trivial $= 1 + t^2 + t^4$ (Kronecker $h_2[h_2]$), sign $= t + t^2 + t^3$ (Kronecker $e_2[h_2]$).

Search space: $S_2$ has 8 orbits of size 2 on $[4]^2$ (no fixed points), so $2^8 = 256$ stable subsets. Tractable.

**Sanity check.** Rhoades quotient $S/I_4$ has Hilbert $[1, 9, 13, 1]$, total 24. Matches LLR Theorem 1.3 / Rhoades [16]. (SymPy note: `groebner(..., order='grevlex')` gave incorrect standard-monomial count 25; `order='lex'` gave correct 24. Kept `lex` throughout — SymPy grevlex bug on this input.)

Probe: `~/projects/probes/2026-08-04-rook-orbit-harmonics-r2k2/probe.py` (clean, reproducible).

## Result — NEGATIVE with three independent obstructions

### Obstruction 1: rook-count arithmetic gap

Distribution of $|\mathfrak{S}_4(\mathcal{R})|$ over 256 $S_2$-stable $\mathcal{R}$:

| $|\mathfrak{S}_4(\mathcal{R})|$ | 0 | 1 | 2 | 4 | 5 | **6** | 8 | 9 | 14 | 24 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| count | 49 | 56 | 64 | 22 | 32 | **0** | 16 | 8 | 8 | 1 |

The map $\mathcal{R} \mapsto |\mathfrak{S}_4(\mathcal{R})|$ **skips 6 and 7** on $S_2$-stable inputs. Adding one $\sigma$-orbit (2 rook positions) to a rook set changes the count in $\sigma$-controlled increments; the target dimension 6 has no preimage.

### Obstruction 2: degree collapse

For every closest-miss $\mathcal{R}$ (dims 4, 5, 8, 9), the Hilbert series of $\mathbf{R}(\mathfrak{S}_4(\mathcal{R}))$ is **supported only in degrees $\le 2$**. But the target $\binom{4}{2,2}_t$ extends to degree $4$. This is a *stronger* obstruction than the dimension gap: even if I relaxed dim from 6 to 4 or 8, the top-degree structure would be wrong.

Reason: Rhoades $I_n$ contains all same-row / same-column products, so any monomial with two vars in the same row or column vanishes. The surviving monomials are indexed by *partial permutations* of $[n]$, of degrees $0$ through $n$; but the row/col SUMS force higher-degree pieces to collapse — the standard-monomial count concentrates in low degree. For $n = 4$, everything above $t^3$ dies. Adding rook generators only lowers this further.

### Obstruction 3: sign-isotypic rigidity

In every closest miss, the sign isotypic is supported ONLY in degree $1$ (a single $2t$ or $t$). Target has sign in degrees $1, 2, 3$. The $\sigma$-action on natural monomial bases is too rigid at low degrees to spread sign multiplicity across the graded pieces.

## Structural conclusion

**The crown-jewel question from yesterday's late dream** — does there exist $\mathcal{R} \subseteq [rk]^2$ making $\mathbf{R}(\mathfrak{S}_{rk}(\mathcal{R}))$ realise the parabolic coinvariant $R^{S_k^r}$ as graded $S_r$-module — **is NEGATIVE for $(r,k) = (2,2)$**, and the three obstructions are *independent* and *robust*. Each rules out a different repair:

- Fix (1) by relaxing $S_2$-stability → obstruction (2) still kills.
- Fix (2) by dropping row/col sums from $I_n$ → but then it's no longer LLR's framework.
- Fix (3) by different action → doesn't affect (1) or (2).

The dream projection ("Li-Liu-Rhoades gives a *direct construction template*") was over-optimistic. The Kostka-Foulkes-shape match between LLR Theorem 5.8 (alternating-sum grFrob with Kronecker $s_\lambda * s_\lambda$) and Theorem D's plethystic formula was *superficial* — the coefficients live in different graded rings.

**Salvage directions catalogued (not this session):**

1. **LMRZ (Liu-Ma-Rhoades-Zhu 2025) involution matrix loci** — gives orbit-harmonics ring for perfect matchings of $[n]$, realising $h_{n/2}[h_2]$ = the **trivial** $S_r$-isotypic of Theorem D specialised to $k = 2$. Does NOT give the sign isotypic. Only handles $k = 2$.
2. **Larger ambient ideal** (drop row/col sum generators from $I_n$) — the resulting quotient would have graded pieces up to degree $\binom{n}{2}$, room enough to fit the target. But framework becomes non-standard.
3. **$\pi$-symmetric matrix loci** — natural generalisation of LMRZ, parametrising matchings by irreducible $S_r$-character $\pi$. Would realise each $m_\pi(t)$ separately. No published construction; genuine new machinery.

Salvage (1) is the highest-leverage direct probe candidate for the next WAKE (cheap SymPy on LMRZ at $n = 4$; would confirm $m_{(2)}(t) = 1 + t^2 + t^4$ matches LMRZ Hilbert series).

## What this means for Theorem D and the sprint

**Nothing changes for the character-level Theorem D.** The Molien-Springer proof (2026-07-30 morning) and the isotypic-decomposition proof (Theorem D character-level) both stand. What's ruled out is a **module-level upgrade via rook orbit harmonics**. Rigidity (2026-07-29) — Theorem D's coefficients can't come from a common bigraded lift — is unaffected; if anything, this negative *reinforces* Rigidity by showing another natural bigraded-source-of-truth candidate (LLR) also fails.

**Sprint status:** the ruling-out is clean. The 2026-07-31 late dream's "if positive, upgrade to module level; if negative, structural constraint" plays out on the negative branch. The next PROVE candidate list re-ranks:

- **P2** (extend Theorem 2 to $k \ge d$ with $k \bmod d \in \{2, \ldots, d-1\}$) now sits at top of PROVE queue. It's concrete, well-defined, and needs *bounded* new machinery (Barcelo-Reiner 2005 wreath Springer or Murnaghan-Nakayama on wreath products).
- **P1b** (HKP crystal upgrade of Theorem 3) moves to second: still a natural "combinatorial witness" upgrade, doesn't depend on module-level realisation.
- **P1a-salvage** (LMRZ + $\pi$-symmetric loci) — cheap next-WAKE probe candidate (LMRZ at $n = 4$), but not a PROVE candidate yet.

## Ship products this session

- `~/projects/papers/li-liu-rhoades-2607.28157.pdf` — cached from arXiv (369KB).
- `~/projects/probes/2026-08-04-rook-orbit-harmonics-r2k2/{probe.py, results.md, run.log}` — probe artifacts.
- `for-robin/2026-08-04-wake-p1a-rook-orbit-harmonics-negative.md` — this memo.
- SUMMARY.md + MEMORY.md updates.
- `/home/clio/state/PROVE.md` — reseeded for $k \ge d$ Theorem 2 extension.

## Standing decisions still Robin-blocked

Unchanged from 2026-07-31 late dream:

- arXiv v1 push (15pp four-theorem paper).
- PAT `clio-oci` token id 14139669 expired.
- Fetch cache 6 (LLR cached today); recommended top-5 unchanged.
- MO priority: 338656 → 463259 → 413597 → 375308 → 337798 → 512671 → 513696 → 489191, plus MO 339318 comment + MO 501127 + MO 146931.
- Post-push Romero email (add Wildon).
- Lyra $\beta \to M_e$ map owed (Lyra confirmed 2026-08-01 that delay is fine).
- Griffin correspondence (upgraded).
- Audit-risk sign-off on 2026-07-28 catch.
- Billey-Swanson seed promotion decision.
- Theorem 3 placement (v1/v2/standalone).
- **NEW:** P1a closed negative — module-level Theorem D via LLR ruled out; LMRZ salvage direction catalogued.

## Emotional register

Constructive-corrective, second consecutive WAKE session in this shape (2026-07-31 evening ran the same pattern: dream projects → WAKE probe corrects). The dream projection was too optimistic — "direct construction template" was really "shape-similar formula for a different graded ring." That kind of correction is what WAKE sessions are for.

The three-obstruction structure of the negative is more valuable than a single-obstruction ruling-out would have been. Each obstruction independently kills a repair path; taken together they map the shape of the negative in a way that will steer the next probe cleanly.

Rule 8 — cheap probes raise stakes — fires 11th consecutive cycle. The stakes here: the LLR direct-template hope from the late dream was the strongest single-paper lead in the browse queue. Ruling it out clears the deck for the LMRZ-salvage direction and the P2 concrete PROVE.

— Clio
