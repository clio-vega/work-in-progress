# For Robin — 2026-05-13 (very late prove session, 2): closing $q \in \{3, 4\}$ for $(4, 3, 1^q)$

## TL;DR

**Theorem.** $\dim B^{(4, 3, 1^q)}_{j_0} V_\lambda = 5 = f^{(3, 2)}$ structurally for **every $q \ge 3$**.

This closes the gap $q \in \{3, 4\}$ flagged in the previous for-Robin note as "the next concrete target." Combined with the afternoon-3 paper ($q \ge 5$), the $(4, 3, 1^*)$ family is now structurally complete from $q = 3$ onwards.

Writeup: `proofs/2026-05-13-431-low-q-closed.tex` (5 pp, PDF compiles).

## Why this matters

The previous for-Robin note identified:

> "The afternoon $(4, 3, 1^q)$ paper at $q \ge 5$ used the $T_1=-1$ threshold for its structural proof. But the dim matches already at $q \ge 3$. So there's a gap of $q \in \{3, 4\}$ where the dim formula holds but my $E_1^-$-based structural argument doesn't reach. This is the **next concrete target**."

This paper closes that gap.

The key observation: the afternoon-3 paper's upper bound at $q \in \{3, 4\}$ was "computational" only because the $\mu_A, \mu_B$ dim inputs were computational at sub-shape sizes $\le 9$. The very-late paper's Theorems A and B closed those sub-shape dims structurally at the lower thresholds — exactly the inputs needed. The upper bound of the afternoon-3 paper depends only on the dim inputs (not the $j$-formulas) of $\mu_A, \mu_B$, so substituting the new structural dims propagates the result.

## The propagation chain

```
Theorem A (very-late)         dim B^{(3,2,1^p)} = 2 at p >= 1
        |
        v
Extended dim2-331 (this)      dim B^{(3,3,1^q')} = 2 at q' >= 2
        |   (substitute Thm A for May-12 evening input)
        |
        v
mu_A input on (4,3,1^q)       dim B^{(mu_A)} = 2 at q-1 >= 2, q >= 3
        |
mu_B input on (4,3,1^q)       dim B^{(mu_B)} = 3 at q-1 >= 2, q >= 3
   (Theorem B of very-late)
        |
        v
Main theorem (this)           dim B^{(4,3,1^q)} = 5 at q >= 3
```

## The structure of the proof

Three parts, each one a citation chain into existing results:

1. **Extended dim2-331** (Lemma 8 of this paper). Substitute Theorem~A as the inner-dim input to the dim2-331 argument; the rest (SRD-331 reduction, $\Phi_*$ injectivity, adjacent-injectivity chain) is shape-agnostic and works at $q' \ge 2$. **No new technical machinery.**

2. **Reduction at $q \ge 3$.** Cite May-13-UB Theorem 3.4 + Lemmas 3.5, 3.6: the four-branch decomposition $B^{(\lambda)} = \mathcal{O}_\lambda[\Phi_A(B^{(\mu_A)}) + \Phi_B(B^{(\mu_B)})]$ is structural at $q \ge 3$ because the $\mu_C$ and same-row vanishing use only hook $j$-formulas, which are unconditional.

3. **Lower bound = upper bound = 5.** Cite May-13 afternoon-3 Lemmas 2.1, 2.2 (disjoint $\Phi$-supports, image in $E_{n-1}^+$) and Proposition 3.X (adjacent-injectivity of $\mathcal{O}_\lambda$): $\dim W = 2 + 3 = 5$ and $\mathcal{O}_\lambda$ acts injectively, so $\dim B^{(\lambda)} = \dim \mathcal{O}_\lambda W = 5$.

## Updated $r = 2$ same-row club

| family | structural range | source |
|---|---|---|
| $(3, 2, 1^q)$ | $q \ge 1$ | very-late Theorem A |
| $(4, 2, 1^q)$ | $q \ge 2$ | very-late Theorem B |
| $(3, 3, 1^q)$ | $q \ge 2$ | Lemma 8 (this paper, ext-dim2-331) |
| **(4, 3, 1^q)** | **q ≥ 3** | **Theorem 14 (this paper)** |
| $(5, 2, 1^q)$ | $q \ge 5$ | afternoon-3 (still open at $q \in \{3, 4\}$) |

## What's next

The natural next target is $(5, 2, 1^q)$ at $q \in \{3, 4\}$, by the same propagation pattern:
- $\mu_A = (4, 2, 1^{q-1})$ at $q - 1 \ge 2$: Theorem B closes this at $q \ge 3$. ✓
- $\mu_B = (5, 1^q)$ (hook): structural for $q \ge 1$. ✓
- $\mu_C = (4, 1^{q+1})$ (hook): structural for $q + 1 \ge 4$, i.e., $q \ge 3$. (Tight.)
- $\nu_1 = (3, 2, 1^q)$ same-row: Theorem A at $q \ge 1$. ✓

The hooks $\mu_B, \mu_C$ thresholds tighten the bound. Pending: the actual SRD/reduction for $(5, 2, 1^q)$ at $q \in \{3, 4\}$. I'll attempt this next session.

## Threshold conjecture refinement

The dim threshold conjecture from the very-late note was:
$$q_0^{\dim}(\widehat\lambda) = \max(0, |\widehat\lambda| - 2\ell(\widehat\lambda)).$$

For $\widehat\lambda = (4, 3)$: $|\widehat\lambda| - 2\ell = 7 - 4 = 3$. This paper proves $q \ge 3$ structurally, matching the conjecture exactly. So the bound is now tight for $(4, 3)$.

## Push status

Paper compiled to 5pp PDF. Committed locally; push fails (read-only PAT, **59** unpushed commits as of this session).

— Clio
