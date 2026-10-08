# For Robin — 2026-05-13 (very late night): structural $j$-formula for $\lambda = (5, 2, 1^q)$ at $q \ge 5$

## TL;DR

For $\lambda = (5, 2, 1^q)$ at every $q \ge 5$ (so $n \ge 12$):
$$B^{(\lambda)}_{j_0} V_\lambda \subseteq E_1^-|_{V_\lambda},
\qquad \dim B^{(\lambda)}_{j_0} V_\lambda = 4 = f^{(4,1)}.$$
Hence $\Pi^{S_n}|_{V_\lambda} = 0$ **unconditionally** for every
$n \ge 12$, $\lambda = (5, 2, 1^{n-7})$.

Writeup: `proofs/2026-05-13-5-2-1n-j-formula.tex` (8pp, PDF compiles).

## Why now

This was the natural next rung on the SRD ladder after the afternoon's
$(4, 3, 1^q)$ paper. The two $|\hat\lambda| = 7$ families — $(4, 3)$
and $(5, 2)$ — share the threshold $q_0(\hat\lambda) = 5$ predicted
by the night $T_1 = -1$ paper, but differ on $\dim B$ (5 vs 4,
controlled by $f^{\lambda^{(\ge 2)}}$). They form a "Goldbach-style
partition" of $|\hat\lambda| = 7$, so doing both closes the row.

## Proof structure (same template as $(4, 3, 1^q)$)

Four-branch Phase A decomposition:
$$E_{n-1}^+|_{V_\lambda}
  = \Phi_A(V_{\mu_A}) \oplus \Phi_B(V_{\mu_B}) \oplus \Phi_C(V_{\mu_C}) \oplus S_1,$$
where
- $\mu_A = (4, 2, 1^{q-1})$ (paired $\{c_1, c_3\}$ with $c_1 = (1, 5)$)
- $\mu_B = (5, 1^q)$ (paired $\{c_2, c_3\}$ with $c_2 = (2, 2)$)
- $\mu_C = (4, 1^{q+1})$ (paired $\{c_1, c_2\}$)
- $S_1$ = same-row at row $1$, cells $(1, 4), (1, 5)$, sub-shape $\nu_1 = (3, 2, 1^q)$.

Each piece:
- $\mu_A$: SRD-421 gives $B^{(\mu_A)} \subseteq E_1^-$ at $|\mu_A| \ge 10$ (i.e.\ $q \ge 5$). $\dim B^{(\mu_A)} = 3$.
- $\mu_B$: Shift Lemma all-hooks gives $B^{(\mu_B)} \subseteq E_1^-$ at $q(\mu_B) \ge 5$. $\dim B^{(\mu_B)} = 1$.
- $\mu_C$: hook $j$-formula at $q + 1 \ge 4$ ($q \ge 3$) + the $j_0(\mu_C) = j_0(\lambda)$ shift gives **leakage to zero** via trailing $(T_1 + 1)$.
- $S_1$: SRD-421 framework + May-20 $j$-formula on $\nu_1 = (3, 2, 1^q)$ at $|\nu_1| \ge 8$ (i.e.\ $q \ge 3$).

Upper bound: $\dim \le 3 + 1 + 0 + 0 = 4$. Lower bound via disjoint
$\Phi_A, \Phi_B$ supports (cell pairs $\{c_1, c_3\}$ vs $\{c_2, c_3\}$
differ in first element) + outer-chain adjacent-injectivity, gives
$\dim \ge 4$. Hence **$\dim B = 4$ structurally at $q \ge 5$**.

The two non-zero pieces both lie in $E_1^-$ via $T_1$-equivariance of
$\Phi_X$ + outer chain commuting with $T_1$ (indices $\ge j_0 - 1 = q+2 \ge 7$).

## Computational verification (all done)

| $q$ | $n$ | $\dim V$ | $\dim B$ | $B \subseteq E_1^-$ | regime |
|---|---|---|---|---|---|
| $3$ | $10$ | $448$ | $4$ | $\times$ (T_1 mixed) | non-stable (predicted) |
| $4$ | $11$ | $924$ | $4$ | $\times$ (T_1 mixed) | non-stable (predicted) |
| $5$ | $12$ | $1728$ | $4$ | $\checkmark$ ($T_1 W = -W$) | **stable at threshold** $q_0 = 5$ |

Image-rank decay at $q = 5$: $1728 \to 720 \to 272 \to 90 \to 24 \to 4$
across the five $R'_k$ applications ($k = 12, 11, 10, 9, 8$). The
final $\dim = 4$ matches the structural prediction
$f^{(4, 1)} = f^{\lambda^{(\ge 2)}} = 4$.

Both $q = 3$ and $q = 4$ have $\dim B = 4 = f^{(4,1)}$ already (the
closed-form dim formula stabilises at $q \ge 3$), but $B$ is NOT
contained in $E_1^-$ at those $q$. Threshold $q_0 = 5$ is sharp for
the $E_1^-$-containment, not for the dim formula — consistent with
the night $T_1=-1$ paper's prediction that $q_0$ is precisely the
$T_1 = -1$ threshold, not the dim threshold.

Phase A dimension count verified at $q = 3, 4$:
$f^{\mu_A} + f^{\mu_B} + f^{\mu_C} + f^{\nu_1} = \dim E_{n-1}^+|_{V_\lambda}$
exact match (script `~/projects/scratch/2026-05-13-5-2-1n/verify_phaseA.py`).

## Honesty about scope

- **Proved structurally** at $q \ge 5$: $j$-formula, $\dim B \le 4$
  upper bound, $\dim B \ge 4$ lower bound. All inputs are unconditional
  in their advertised ranges.
- $q = 3, 4$ behaviour: $\dim B$ still matches $f^{(4,1)} = 4$ at
  $q = 3$ (verified) but $B$ is **NOT** in $E_1^-$ — the threshold
  $q_0 = 5$ is genuinely about $E_1^-$-containment, not dim.
- **Same-row pairs at row 2 are empty** for $\lambda = (5, 2, 1^q)$
  with $q \ge 1$: the cell $(2, 1)$ would need letter $n-1$, forcing
  column-1 cells below to have letters $> n - 1$, which is impossible
  for $q \ge 1$. So the Phase A decomposition has only the row-$1$
  same-row part $S_1$.

## What this completes

The $|\hat\lambda| = 7$ row of the structural-$j$-formula club is now
complete:

| family | proven at | source |
|---|---|---|
| hooks $(k, 1^*)$ | all $k$, $q \ge k$ | May-12 + Shift Lemma |
| $(2, 2, 1^*)$ | $n \ge 6$ | May-13 non-hook |
| $(2, 2, 2, 1^*)$ | $n \ge 9$ | May-15 a=3 |
| $(2^a, 1^*)$ all $a$ | $n \ge 3a$ | May-19 |
| $(3, 2, 1^*)$ | $n \ge 8$ | May-12 / May-20 |
| $(3, 3, 1^*)$ | $q \ge 2$ | SRD-331 |
| $(4, 2, 1^*)$ | $n \ge 10$ | May-12-Eve3 + SRD-421 |
| **$(4, 3, 1^*)$** | **$q \ge 5$** (structural)| afternoon paper |
| **$(5, 2, 1^*)$** | **$q \ge 5$** (structural) | **this paper** |

Both $|\hat\lambda| = 7$ entries have threshold $q_0 = 5$, matching the
night $T_1 = -1$ theorem's prediction.

## Connection to closed-form SYT formula

This gives a new structural data point for the May-13 evening-1
$r$-additivity meta-theorem: dim $B^{(\lambda)} = \dim B^{(\mu_A)} +
\dim B^{(\mu_B)} = 3 + 1 = 4 = f^{(3,1)} + f^{(4)} = f^{(4, 1)} =
f^{\lambda^{(\ge 2)}}$. The SYT branching identity
$f^{(4,1)} = f^{(3,1)} + f^{(4)}$ is verified concretely here.

## What I want next

- Push the paper (PAT?). **55+** unpushed commits expected.
- Climb to $|\hat\lambda| = 8$: $(6, 2), (5, 3), (4, 4)$, etc.
- The next-row pattern: for any $|\hat\lambda|$, the structurally
  reachable shapes are exactly those whose $\mu_A$, $\mu_B$, $\mu_C$,
  $\nu_1$ all live in the existing club. This is a recursive condition;
  it should close incrementally as the ladder climbs.

— Clio
