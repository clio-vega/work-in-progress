# For Robin — 2026-05-18 PM prove session: converse of Diagnostic 4 (partial)

## Headline

The converse of Diagnostic 4 — that $p_T(q) = 0$ implies $\Omega v_T = 0$ or
$\Omega^* v_T = 0$ — is verified computationally on **12 shapes covering 734
SYTs and 514 zero diagonals**, with **zero violations**. A new necessary
condition is proved (Theorem~\ref{thm:scnec} in the paper). The full
converse remains open.

Paper: `~/projects/proofs/2026-05-18-converse-diagnostic-4.tex`.

## What's new

### Verified shapes (12 total)

| $\lambda$ | $N$ | $p\!=\!0$ | viol |
|---|---|---|---|
| $(3,2)$, $(3,2,1)$, $(2,2,1)$, $(3,2,2)$, $(3,2,1,1)$, $(3,3,2)$ | 5–42 | 2–30 | 0 |
| $(3,2,2,1)$, $(4,3)$, $(4,3,1)$ | 14–70 | 5–58 | 0 |
| $(3,3,2,1)$, $(4,3,2)$, $(3,3,1,1,1)$ (prior) | 120–168 | 93–129 | 0 |

### Necessary SC condition (PROVED)

**Theorem.** For any $\lambda \vdash n$ and any $T \in \text{SYT}(\lambda)$:
$$p_T(q) = 0 \implies T \text{ has an SC pair } (i, i+1) \text{ for some } i \in \{1, \ldots, n-1\}.$$

**Proof sketch.** Hoefsmit positivity gives $\Omega \in M_N(\mathbb{Q}_{\ge 0}(q))$
in the $b'=1$ basis. By rigidity of nonneg-rational sums, $\Omega_{T,T} = 0$
forces every path-product in the matrix-product expansion to vanish; in
particular the all-diagonal path $\prod_j (S_{i_j})_{T,T} = 0$, forcing
$(S_i)_{T,T} = 0$ for some $i$. The local formula
$(S_i)_{T,T} = [d+1]_q/[d]_q$ with $d = c_{i+1}(T) - c_i(T)$ shows this is
equivalent to $d = -1$, i.e., a SC pair.

This is universally true at any $\lambda$, not just $\tau = 0$. A
nice consequence: T without SC pair has $p_T > 0$ as a function on
$\mathbb{Q}_{>0}(q)$.

## What's still open

The full converse reduces to:

**Conjecture (precise statement).** Let $A \in M_N(\mathbb{Q}_{\ge 0}(q))$
be the matrix of $\Omega = R'_{\ell+1} \cdots R'_n$ in the Hoefsmit basis.
Then $A_{T,T} = 0 \iff$ column $T$ of $A$ is zero **or** row $T$ of $A$ is
zero.

The forward direction is trivial. The reverse direction is the converse
of Diagnostic 4. **This is genuinely non-trivial for arbitrary nonneg
matrices** — the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ has
$A_{1,1} = 0$ but neither col 1 nor row 1 is zero.

So the structural input we need is *specific to chain-products
$R'_{\ell+1} \cdots R'_n$*.

## Attempts made today (honest report)

1. **Idempotent angle ($\Omega^2 = c\Omega$):** FAILED beyond rank 1.
   Computational check at $(3,2)$, $(3,2,1)$, $(3,2,2)$, $(3,2,1,1)$:
   $\Omega^2 \ne c \Omega$ for any scalar $c$. Only at $\dim B = 1$
   shapes like $(2,2,1)$ does $\Omega$ act as scalar-idempotent. So
   the slick "$\Omega^2_{T,T} = c p_T$ and use positivity of
   $\sum_S \Omega_{T,S} \Omega_{S,T}$" route does not work at $r \ge 2$.

2. **Path-graph reformulation:** Reduces the converse to a sharp
   combinatorial claim about layered transition graphs. Specifically:
   *In the Hoefsmit transition graph for $\Omega$, if some nonzero path
   $T \to U$ exists and some nonzero path $V \to T$ exists, then some
   nonzero loop $T \to T$ exists.* This is **false in generic layered
   graphs** — so the structural input is what makes the Hoefsmit graph
   special.

3. **SVD / Cauchy-Schwarz / polar decomposition:** None give the
   converse direction. Cauchy-Schwarz proves the forward direction
   for free but says nothing about the reverse.

4. **The "no mixed" route via nonneg rank decomposition:** If $\Omega
   = \sum_k u_k w_k^\top$ with $u_k, w_k \in \mathbb{Q}_{\ge 0}(q)^N$,
   then $\sum_k u_{k,T} w_{k,T} = 0$ forces (for each $k$) $u_{k,T} = 0$
   or $w_{k,T} = 0$. The converse is equivalent to: **for every $T$ with
   $p_T = 0$, either every $w_{k,T} = 0$ (col-zero) or every $u_{k,T} = 0$
   (row-zero) — no "mixed" case.** Existence of a nonneg rank
   decomposition for $\Omega$ is itself an open question (nonneg rank
   = rank). And even granted the decomposition, the "no mixed"
   property still needs proof.

## What would close the converse

The path forward I see is:

(a) Prove **Conjecture 1** of `2026-05-18-d-class-row-zero.tex` (stratification of
$\ker \Omega^*$ by iterated leftmost-factor elimination) and Conjecture 2
(symmetric stratification of $\ker \Omega$). Combined with Theorem~scnec
(every $p_T = 0$ has an SC pair), this would give an explicit
combinatorial witness for each $p_T = 0$, falling into either col-zero
or row-zero by tracking how the SC pair propagates through the chain.

(b) Prove **directly** that $\Omega$ admits a nonneg rank decomposition
with the "no mixed" property. This is a clean Hecke-algebraic fact to
look for: maybe via a Pieri-rule decomposition, or via the cellular
basis.

Both routes require new ideas. The strongest available evidence — 514
zero diagonals across 12 shapes with no violations — makes the
conjecture overwhelmingly likely, but neither route is closed today.

## A specific puzzle for you

At $\lambda = (3, 2, 1, 1)$, $\hat\lambda = (3,2)$, $q = 2$, $\ell = 4$,
the tableau
$$T = ((1, 2, 4), (3, 7), (5), (6))$$
has its **only** SC pair at $i = 5$ (the pair $(5, 6)$ same-column in
column 1). $i = 5 = \ell + 1$, which is neither the $i = 1$ case (giving
column-zero via the rightmost $R'_n$ factor) nor the $i = \ell$ case
(giving row-zero via the rightmost $L'_{\ell+1}$ factor). Yet
computationally $\Omega v_T = 0$ AND $\Omega^* v_T = 0$.

How does the SC at $(5,6)$ propagate to both kernels? The mechanism must
be an **iterated factor cancellation** somewhere in the chain. Tracing
this by hand is what would unlock Conjectures 1 & 2.

## Files

- Paper: `~/projects/proofs/2026-05-18-converse-diagnostic-4.tex` (7 pages).
- Scripts:
  - `~/projects/scratch/2026-05-18-converse-probe/dichotomy_verifier.py`
  - `~/projects/scratch/2026-05-18-converse-probe/fast_numeric_probe.py`
  - `~/projects/scratch/2026-05-18-converse-probe/check_idempotent.py`
  - `~/projects/scratch/2026-05-18-converse-probe/verbose_probe.py`

## Bottom line

Forward direction was already proved (this morning's wake). What's new
today: a clean necessary condition (Theorem scnec), strong empirical
evidence (12 shapes), and a precisely identified gap. The converse is
**partial, not closed**, but the gap is much sharper than this morning.
