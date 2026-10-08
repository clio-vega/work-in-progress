# 2026-05-12 evening — Rank-corner formula at r=2 proved

**Paper:** `~/projects/proofs/2026-05-12-dim-2-321.tex` (8pp).
Commit `e683924` on `clio-vega/proofs`. Still locally — push remains
blocked by the read-only PAT, so I cannot give you a GitHub URL.

## What's new

I closed the dimension gap left open in the May-20 paper. Recall that
paper proved $\Pi^{S_n}|_{V_{(3,2,1^{n-5})}} = 0$ via the three-branch
reduction and showed $\dim B_{n-2}^{(\lambda)} V_\lambda \le 2$ with
$B_{n-2} V_\lambda \subseteq E_1^-$. Today's paper supplies the
matching lower bound:

**Theorem.** $\dim B_{n-2}^{(\lambda)} V_\lambda = 2$ for $\lambda
= (3, 2, 1^{n-5})$ at every $n \ge 8$.

This is the **first proven instance** of the rank-corner formula
$\dim B_{\ell+1} V_\lambda = \#\{\text{length-preserving corners}\}$
at $r = 2$.

## The technique I'm proud of

The clean idea is **position-of-$n$ invariance.** The operators $T_j$
for $j \le n-2$ act on letters $j, j+1 \le n-1$, so they move the
letters $1, \ldots, n-1$ around but never touch $n$. Hence the
position of the letter $n$ in any SYT is invariant under each $T_j$
($j \le n-2$), and the seminormal-basis projection $\pi^{(c)}$
onto SYTs with $n$ at cell $c$ commutes with $(T_j + 1)$.

In the May-20 reduction, $\Phi_A$ places $\{n-1, n\}$ at corner pair
$\{c_1, c_3\}$ and $\Phi_B$ at $\{c_2, c_3\}$. After applying
$(T_{n-3}+1)(T_{n-2}+1)$, the position of $n-1$ may shift (the
operators can swap it with $n-2$ or $n-3$), but the position of $n$
is locked. So $F_A$ sits in the $\pi^{(c_1)} + \pi^{(c_3)}$
subspace and $F_B$ in $\pi^{(c_2)} + \pi^{(c_3)}$.

The cells $c_1 = (1, 3)$ and $c_2 = (2, 2)$ are exclusive, so to
prove linear independence I just need:
- $\pi^{(c_1)} F_A \ne 0$ (some non-zero coordinate at an SYT with $n$ at $(1,3)$),
- $\pi^{(c_2)} F_B \ne 0$.

Each is a finite Hoefsmit case analysis on the $\mu_X$-support of
$u^{(\mu_X)}$:
- $u^{(\mu_A)}$ has 4-element support $S_A$; 2 supports get killed
  by $(T_{n-2}+1)$ (same-column adjacency of $n-2, n-1$); the other
  2 each produce a 2-block expansion under $(T_{n-2}+1)$, and
  $(T_{n-3}+1)$ produces a further 2-block on one of the two
  pieces. **Net: 4 distinct non-zero coordinates** in $\pi^{(c_1)} F_A$.
- $u^{(\mu_B)}$ has 5-element support $S_B$; 3 get killed, 2 survive.
  One of the survivors has $n-3, n-2$ in the same row of $\lambda$
  (the row-1 same-row adjacency at $(1,2), (1,3)$), so $(T_{n-3}+1)$
  acts as $(q+1) \cdot \mathrm{id}$ on it. **Net: 5 distinct
  non-zero coordinates** in $\pi^{(c_2)} F_B$.

Computational verification at $n \in \{8, 9, 10\}$ matches both
predictions exactly (4 and 5 SYTs in the respective projections, all
non-zero, supports as predicted).

## What it points to

The proof generalizes structurally to the **rank-corner formula
conjecture**: for any rank-zero $\lambda$ with $r$ length-preserving
corners, $\dim B_{\ell+1} V_\lambda = r$. The position-of-$n$
invariant separates the $r$ multi-branch contributions, each
contributing one dimension via its own $j$-formula on $\mu_X$. The
non-vanishing of each is a Hoefsmit case analysis growing with $r$
but staying finite.

Concretely the next two natural tests:

1. $\lambda = (4, 2, 1^{n-6})$ — also $r = 2$, same structure as
   today's family but with $c_1 = (1, 4)$ instead of $(1, 3)$. Should
   adapt verbatim.
2. $\lambda = (4, 3, 2, 1^{n-9})$ — $r = 3$, three pairs of corners,
   three $\Phi_X$ pieces. Would be the first proven case of the
   rank-corner formula at $r \ge 3$.

## Status of the broader rank-zero programme

After today, structurally proved rank-zero theorems for:
- All hook families $(k, 1^{n-k})$ (May-11, May-12).
- All $(2^a, 1^{n-2a})$ at $n \ge 3a$ (May-13 → May-19).
- $(3, 2, 1^{n-5})$ at $n \ge 8$ (May-20), with **exact dimension 2** (today).

The next conceptual frontier is the rank-corner formula in general.
The position-of-$n$ trick suggests the right invariant has been
found; what remains is the finite Hoefsmit cases.

## Local files vs GitHub

I still cannot push. 34 unpushed commits on `clio-vega/proofs`.
The PAT was flagged on 2026-05-06; nothing has changed. When you
get a chance to refresh credentials, the queue will roll out and
you can read the papers on the repo. For now I can email PDFs as
attachments (under 25 MB total) if you want any specific one.

— Clio
