# For Robin: factor-of-two conjecture refuted (2026-05-14 evening prove session)

## TL;DR

The PROVE.md side question conjectured: for $\lambda$ with a row-repeat at non-trivial level ($\lambda_i = \lambda_{i+1} \ge 2$), $\dim B_{\ell+1}^{(\lambda)} V_\lambda = 2 \cdot f^{\lambda^{(\ge 2)}}$. The two cited examples $(4,2,2,1)$ and $(4,4,1,1)$ check out.

**The generalisation is false.** Four explicit counter-examples:

| $\lambda$ | $n$ | $f^{\lambda^{(\ge 2)}}$ | actual $\dim B$ | factor |
|-----------|-----|--------------------------|------------------|--------|
| $(6,2,1)$ | $9$ | $5$ | $\mathbf{17}$ | $3.4$ (not even integer!) |
| $(3,3,1)$ | $7$ | $2$ | $\mathbf{3}$ | $1.5$ |
| $(4,3,1,1)$ | $9$ | $5$ | $\mathbf{12}$ | $2.4$ |
| $(4,4,1,1,1)$ | $11$ | $5$ | $\mathbf{15}$ | $3$ |

The last case is striking: same row-repeat as the cited $(4,4,1,1)=2{\cdot}5$ example, but factor $3$ at $q{=}3$ rather than $2$ at $q{=}2$.

Paper: `2026-05-14-factor-of-two-refuted.tex` (7pp).

## What's actually happening

The right framework is a **shape-dependent stability threshold** $q_0(\widehat\lambda)$:

- For $q \ge q_0(\widehat\lambda)$: $\dim B = f^{\lambda^{(\ge 2)}}$ (the May-13 closed form).
- For $q < q_0(\widehat\lambda)$: $\dim B$ is a finer invariant.

The data places $q_0$ in a non-trivial pattern:
- $q_0((3, 2)) = 1$, $q_0((4, 2)) = 2$, $q_0((5, 2)) = 3$, $q_0((6, 2)) \ge 3$.
- $q_0((3, 3)) = 2$, $q_0((4, 3)) = 3$.

The candidate $q_0 = \widehat\lambda_1 - 2$ fails at $(2,2)$, $(3,3)$, $(4,3)$, so no closed form is known yet.

## The cleanest non-stable family: $(5, 2, 1^q)$

A particularly clean phenomenon:

| $q$ | $0$ | $1$ | $2$ | $3$ |
|-----|-----|-----|-----|-----|
| $\dim B$ | $5$ | $8$ | $12$ | $4$ (stable) |

The non-stable values $5, 8, 12$ have no closed form as multiples of $f^{(4,1)} = 4$, but the differences $+3, +4$ suggest a structural contribution from non-stable $\mu_i$ inside the recursion. The jump from $12$ at $q{=}2$ to $4$ at $q{=}3$ is a sharp **phase transition**.

## Why the May-13 recursion fails non-stably

Naive recursion test on $\lambda = (4, 2, 2, 1)$ at $n=9$, $\dim B = 12$:
- Good pairs: $\mu_1 = (3,2,2)$ contributes $\dim B^{(\mu_1)}_{\text{sharp}} = 3$.
                $\mu_2 = (4,2,1)$ contributes $\dim B^{(\mu_2)}_{\text{sharp}} = 6$.
                Sum: $9$.
- All pairs: also include bad pair $\mu_{1,2} = (3,2,1,1)$ with $\dim B^{(\mu_{1,2})}_{\text{sharp}} = 2$. All-pair sum: $11$.

Neither sum equals $12$. The recursion's defect of $3$ (or $1$) is not a clean $f^\mu$ count, suggesting the structure is more subtle than the May-13 paper's stable-regime argument.

## Honest scope

**Established:**
- The May-13 closed form $\dim B = f^{\lambda^{(\ge 2)}}$ is correct in the stable regime (consistent with $11+$ tested shapes).
- The factor-of-two side conjecture is false; counter-examples exhibited.
- Shape-dependent stability threshold $q_0(\widehat\lambda)$ is a real phenomenon with values from $0$ to $\ge 3$.

**Not established:**
- Closed form for $q_0(\widehat\lambda)$.
- Closed form for non-stable $\dim B$.
- Structural mechanism for the phase transition at $q = q_0$.

## What I'd suggest as the next concrete target

The non-stable family $(5, 2, 1^q)$ at $q \in \{1, 2\}$ is small enough to dissect by hand: $\dim V_\lambda = 35, 90$. The branching-decomposition computation should reveal *which* terms in the May-13 reduction fail to vanish or split, and that would pinpoint the precise structural obstruction. From there, the right correction formula should emerge.

Alternatively: pin down $q_0(\widehat\lambda)$ empirically for $\widehat\lambda_1 \in \{3, 4, 5, 6\}$ by completing the data table — a $1{-}2$ hour compute job for $n \le 11$.

## Bonus finding: $E_1^+$/$E_1^-$ flip at $(3, 2, 1)$ boundary

Late in the session, while dissecting $(5, 2, 1)$'s 4-piece decomposition, I needed to check whether $B^{(3, 2, 1)}_4 V_{(3, 2, 1)} \subseteq E_1^-$ at $n = 6$ (the borderline case). Directly computing $(T_1{+}1) \cdot B^{(3, 2, 1)}_4 V_{(3, 2, 1)}$ shows:

- $\dim B^{(3, 2, 1)}_4 V = 2$
- $(T_1{+}1)$ is **injective** on this image (rank 2 in, rank 2 out)
- So $B^{(3, 2, 1)}_4 V \subseteq E_1^+$ at $n = 6$ — **opposite eigenspace** from the $n \ge 8$ result of the May-20 paper.

This is the first time we've observed the $(3, 2, 1^*)$ family's structural picture **flipping** at the boundary $n = 6$. The May-20 rank-zero theorem (with $n \ge 8$ hypothesis) was sharp: at $n = 6$, the entire structural mechanism (image in $E_1^-$, killed by trailing $T_1{+}1$) breaks. The dim still equals $f^{(2, 1)} = 2$, so the *closed form* extends to $n = 6$, but via a structurally different path.

This is a small but interesting refinement of the existing $(3, 2, 1^*)$ structural club. It explains why the family's non-vanishing dim at $n = 6$ doesn't violate any expectation — and it suggests the right framework for non-stable shapes is **eigenspace-tracking** rather than just dim-counting.

## Status

Conjectural refutation paper, now refined with two structural contributions:
1. Refutation of the factor-of-2 conjecture (4 counter-examples).
2. Boundary $E_1^+$/$E_1^-$ flip at $(3, 2, 1)$, $n = 6$.

Both are honest computational findings with implications for the structural programme.

## Status

Conjectural refutation paper. The two cited examples confirm; the conjecture as a whole is false; no replacement closed form is offered. This closes a misleading entry on the PROVE.md side track and refines what to ask next.

## Push status

**62 unpushed commits** (was 61). PAT issue from May 6 persists.

## Files

- Paper: `~/projects/proofs/2026-05-14-factor-of-two-refuted.tex` + `.pdf`
- Scripts: `~/projects/scratch/2026-05-14-row-repeat/`
  - `test_base.py` — verifies the two cited examples
  - `scan_focused.py` — 20-shape scan
  - `test_k21.py` — $(k,2,1)$, $(k,k,1)$, $(4,3,1^q)$ families
  - `test_extras.py`, `test_52_family.py` — additional shape probes
  - `verify_621.py` — confirms $\dim B^{(6,2,1)} = 17$ across $Q \in \{11, 13, 17, 23\}$
