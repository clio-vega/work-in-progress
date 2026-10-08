# PROVE 2026-07-30: Wreath decomposition of collision-regime coset Poincaré PROVED

**Session:** 3h PROVE, dedicated wreath probe.
**Verdict:** POSITIVE — but at a slightly different level than PROVE.md's target.
**Status:** New Theorem D candidate for byproduct paper §5.
**Definitional gap:** Romero-Wen 2505.01732 not in local cache; browsing disabled in proof session.

## Executive summary

The collision-regime factorisation $c_\mu(t) = [3]_t \cdot [2]_{t^2}$ at
$\mu = (2,2,0,0)$ **is proved** to arise from the $S_2$-wreath refinement of
the parabolic coinvariant algebra $R_{(2,2)} = R_4^{S_2 \times S_2}$.
Specifically:

$$\Frob_t(R_\alpha) \;=\; \underbrace{[3]_{t^2}}_{S_2\text{-invariant}} \cdot \, s_{(2)} \;+\; \underbrace{t \cdot [3]_t}_{S_2\text{-sign}} \cdot \, s_{(1,1)}$$

and the collision factorisation is precisely the algebraic identity
$$[3]_{t^2} + t[3]_t = (1+t^2)(1+t+t^2) = [3]_t \cdot [2]_{t^2}.$$

This is a **wreath refinement** of $c_\mu(t)$ in the sense the sprint was
reaching for — the second factor $[2]_{t^2}$ genuinely arises from the
$S_2$-wreath action (as the difference between the total $\binom{4}{2}_t$
and the wreath-invariant $[3]_{t^2}$).

## What the PROVE session gave vs. what PROVE.md asked

**PROVE.md asked:** Does $K^{\mathrm{wr}}_{\mu',(2,2)}(0,t) = [3]_t[2]_{t^2}$
for the Romero-Wen wreath $(q,t)$-Kostka polynomial from arXiv:2505.01732?

**What I could give:** The Romero-Wen paper is not in `~/papers/`. Session
rules block browsing, so I couldn't fetch it. This means the specific
Romero-Wen identity as stated is **definitionally unresolved**.

**What I did give:** A cleaner, classical, self-contained wreath refinement
of the collision factorisation via representation theory of $R_\alpha$
directly (without needing wreath Macdonald machinery). Cross-verified against
Szendrői Thm 4.11 [16, Cor 5.8] at the specialisation $t_{\mathrm{Szendrői}} = 1$
for $k = 2, 3, 4$.

## Proof outline (5 pages, `.tex` + `.pdf`)

1. **$R_\alpha$ is a graded $S_2$-module.** The block-swap $\sigma_0$
   normalises $S_\alpha = S_k \times S_k$ inside $S_{2k}$; the quotient
   $S_k \wr S_2 / S_\alpha \cong S_2$ acts on $R_\alpha$.

2. **Classical decomposition.** $R_{2k} = \bigoplus_\lambda V_\lambda \otimes M_\lambda$
   with $\dim_t M_\lambda = \tilde f_\lambda(t)$ (fake degree). Then
   $\dim_t R_{2k}^H = \sum_\lambda \tilde f_\lambda(t) \dim V_\lambda^H$
   for any subgroup $H$.

3. **Frobenius reciprocity** for $H = S_k \wr S_2$:
   $\dim V_\lambda^{S_k \wr S_2} = \langle V_\lambda, h_2[h_k] \rangle$
   with $h_2[h_k] = \sum_{i=0}^{\lfloor k/2 \rfloor} s_{(2k-2i, 2i)}$
   (standard plethysm identity, Macdonald Sym Fcns Ch I App A).

4. **Trivial-isotypic Hilbert series:**
   $T_k(t) = \sum_i \tilde f_{(2k-2i, 2i)}(t)$.
   At $k = 2$: $T_2(t) = 1 + (t^2 + t^4) = [3]_{t^2}$.

5. **Sign-isotypic by complement:** $N_k(t) = \binom{2k}{k}_t - T_k(t)$.
   At $k = 2$: $N_2(t) = t + t^2 + t^3 = t[3]_t$.

6. **Algebraic identity:** $[3]_{t^2} + t[3]_t = [3]_t \cdot [2]_{t^2}$
   (direct expansion). QED.

## Numerical verification

Ran probes at `~/projects/probes/2026-07-30-wreath-plethystic-collision/`:

- **`szendroi_411.py`**: Symbolic implementation of Szendrői Thm 4.11 plethystic
  formula for $(k, m) \in \{(2,1), (2,2), (2,3), (3,2)\}$. Reproduces
  Szendrői Ex 4.6 exactly ($A_{(2,2)}(t,q) = 1 + qt + 2q^2 t + q^3 t + q^4 t^2$).
- **`exhaustive_spec.py`**: 11 natural (t,q)-specialisations tested. Only $t=1$
  reproduces $c_\mu$; $q=0$ trivialises.
- **`wreath_decomposition.py`**: Cross-check of my Theorem's $T_k, N_k$ against
  Szendrői's $F_{(2)}(1,t), F_{(1,1)}(1,t)$ for $k = 2, 3, 4$. **Exact match** in
  all three cases.

## Key structural finding

**Szendrői's bigraded lift = (t,q)-refinement of the wreath decomposition.**

At $(k,m) = (2,2)$, Szendrői gives
$$F_{(2)}(t,q) = 1 + q^2 t + q^4 t^2, \qquad F_{(1,1)}(t,q) = qt \cdot [3]_q.$$

At the specialisation $t_{\text{Szendrői}} = 1$ (his descent grading trivialised):
- $F_{(2)}(1, q) = 1 + q^2 + q^4 = [3]_{q^2}$
- $F_{(1,1)}(1, q) = q + q^2 + q^3 = q[3]_q$

Exactly matches my classical $T_2, N_2$ (with $q \leftrightarrow t$).

So Szendrői's Thm 4.11 IS the bigraded lift of my (single-graded) wreath
decomposition, providing the *bigraded refinement* the sprint has been
looking for.

## Why the $[k+1]_t \cdot [2]_{t^k}$ factorisation is $k=2$-special

The wreath decomposition $R_\alpha = R_\alpha^{S_2} \oplus R_\alpha^{\mathrm{sgn}}$
is valid for all $k$, but the resulting sum $\binom{2k}{k}_t = T_k(t) + N_k(t)$
only factors as $[k{+}1]_t \cdot [2]_{t^k}$ at $k = 2$:

| $k$ | Factorisation of $\binom{2k}{k}_t$ |
|-----|-----------------------------------|
| 2   | $[3]_t \cdot [2]_{t^2}$           |
| 3   | $[5]_t \cdot [2]_{t^2} \cdot [2]_{t^3}$ |
| 4   | $[7]_t \cdot [2]_{t^2} \cdot [4]_{t^2} / \ldots$ (no clean form) |

At $k = 2$: $\binom{4}{2}_t = [4]_t [3]_t / [2]_t$ and $[4]_t = [2]_t \cdot [2]_{t^2}$
cancels neatly. Higher $k$: additional $[2]_{t^r}$ factors appear.

## Correction to `questions/2026-07-29-wreath-plethystic-collision-regime.md`

Line 46 claims $c_{(2,2,1,0)}(t) = [4]_t \cdot [2]_{t^2}$. This is **wrong**.
Correct value: $c_{(2,2,1,0)}(t) = [3]_t \cdot [4]_t = 1 + 2t + 3t^2 + 3t^3 + 2t^4 + t^5$.
$[4]_t \cdot [2]_{t^2} = 1 + t + 2t^2 + 2t^3 + t^4 + t^5$, which is different.

The "collision phenomenon" $[k{+}1]_t \cdot [2]_{t^k}$ is **specific to
$\mu = (m^k, 0^k)$ profile** (two value-classes with equal multiplicity $k$),
not to any "collision-like" $\mu$. Should update the question memo.

## Consequences for the byproduct paper

**Theorem D candidate** for §5.2:
> The collision-regime factorisation $c_\mu(t) = [3]_t \cdot [2]_{t^2}$ at
> $\mu = (2,2,0,0)$ is the $S_2$-wreath decomposition
> $\dim_t R_\alpha^{S_2} + \dim_t R_\alpha^{\mathrm{sgn}}$ of the parabolic
> coinvariant algebra $R_\alpha = R_4^{S_2 \times S_2}$, rewritten as a product.

If we include this, §5.1 becomes: Theorem 2 (2026-07-28, Weyl-symmetrisation
coset Poincaré) + Theorem 3 (2026-07-29 late, Foata bijection) + Rigidity
(2026-07-29 morning) + **Theorem D** (2026-07-30, wreath decomposition).

**Post-Rigidity route status update:**
- **Route 2 (Szendrői geometric): partially confirmed.** Szendrői's bigraded
  lift is a genuine $(t,q)$-refinement of the wreath decomposition. Verified
  at $t=1$ for $k=2,3,4$.
- **Route 1 (BHMPS $\eta \neq \emptyset$): still open, longer horizon.**
- **Route 3 (Carlsson-Chou module-level compatibility): open.**
- **Route 4 (Ram-Mellit affine Springer): still open.**
- **New: Romero-Wen wreath Macdonald (arXiv:2505.01732): definitionally
  blocked** on my end; need paper fetch.

## What I need from you

1. **Fetch Romero-Wen 2505.01732** to `~/papers/` so I can attempt the direct
   Romero-Wen identity in the next PROVE session. Their $K^{\mathrm{wr}}(q,t)$
   at $q=0$ may or may not literally equal my $T_2(t) + N_2(t)$ — if it does,
   Route 1 is closed via my proof.
2. **Sign-off on Theorem D framing for byproduct paper §5.2.**
   Alternatively, I can bundle it into `clio-poincare-sketches` companion
   note per the fallback plan.
3. Still standing from prior sessions:
   - arXiv push authorisation (paper at 14pp, three theorems, sprint in conclusion).
   - PAT expiry countdown (24h from yesterday).
   - MO 512671 / 489191 / 513696 post drafts.
   - Bulk memory sed (Foata within-block PRUNED marker).

## Sprint status

Sprint at **conclusion phase**. Today's PROVE adds a fourth theorem
(wreath decomposition) that fits cleanly alongside the three from
2026-07-28--29. The wreath origin of the collision factorisation is now
proved, closing the biggest open question from the 2026-07-29 dream.

Rule reinforced (**10th consecutive cycle**): Hour-1 numerical extension
decisive. Today's cycle: Szendrői probe at $(k,m)=(2,2)$ in Hour 1 killed
the naive $q=0$ specialisation route (trivialises), Hour 2 identified the
$t=1$ slice as the right specialisation and derived the wreath decomposition
via classical rep theory, Hour 3 wrote up. The negative result at $q=0$
(hedged in PROVE.md as possible failure mode) was what freed me to find
the correct wreath framing.
