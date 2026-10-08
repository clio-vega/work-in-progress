# For Robin — 2026-05-19 wake-2

## The Dai-Zhang cell hypothesis is refuted; a sharper arithmetic
## discriminator appeared in its place.

### TL;DR

The dream's "highest leverage of the next week" — the Gelfand W-graph
cell hypothesis on the SR-at-1 residual — failed at $(3,3,1,1,1)$.
But the same probe surfaced a **clean arithmetic discriminator with
zero errors over 50 cases**, finer than any natural cell decomposition.
The residual problem now has a concrete combinatorial witness, not a
categorical-machinery dependency.

### What was tested

For $\lambda = (3,3,1,1,1)$ (so $\hat\lambda = (3,3)$, $q = 3$, $\tau = 0$,
$n = 9$), I computed the diagonal probe $p_T(q) = \langle v_T, \Omega v_T\rangle$
for all 120 SYTs in the Hoefsmit basis. There are 50 SR-at-1 SYTs (entries
1,2 in row 1); 35 of these have $p_T = 0$.

The W-graph cell hypothesis (Dai-Zhang Gelfand framework): the
SR-residual should be a union of cells in the Hoefsmit/Murphy
$W$-graph. **Refuted by explicit counterexample**:

$$T_{11} = \begin{matrix} 1 & 2 & 4 \\ 3 & 5 & 7 \\ 6 \\ 8 \\ 9 \end{matrix} \quad
T_{27} = \begin{matrix} 1 & 2 & 7 \\ 3 & 4 & 8 \\ 5 \\ 6 \\ 9 \end{matrix}$$

Both have descent set $D = \{2,4,5,7,8\}$ (and lie in the same
descent class, the finest natural cell coarsening; the Hoefsmit
Murphy graph is strongly-connected, so SCCs are trivial). But
$p_{T_{11}}(q) \ne 0$ while $p_{T_{27}}(q) \equiv 0$. So the residual
is finer than any natural W-graph cell.

### The replacement discriminator

For $T \in \mathrm{SYT}(3,3,1,1,1)$ with SR-at-1, $p_T = 0$ iff
$T$ has a "flush" SC pair in column 1 at one of:

- (α) index $3$ — entries 3,4 in cells (2,1),(3,1): 20 cases.
- (β) index $5$ — entries 5,6 in cells (3,1),(4,1) with 3 in (2,1):
  9 cases.
- (γ) index $7$ — entries 7,8 in cells (4,1),(5,1) with 9 NOT in
  column 1: 6 cases.

Total: 35, matching the empirical count. Zero errors.

**Arithmetic:** $\{3,5,7\} = \{q, q+2, q+4\}$ for $q = 3$. This is
a strikingly clean pattern — the discriminating SC-pair locations
in column 1 form an arithmetic progression with spacing 2 starting
at $q_{\hat\lambda}$.

**First-vanish-stage stratification:** (α) is killed first by $R'_8$,
(β) by $R'_7$, (γ) by $R'_6$. The "killing factor" in the chain
moves left as the SC pair moves down column 1, matching the
position-of-letter dynamics in the chain product.

### What I'm running now (background)

Two agents:

1. **Discriminator generalisation test** on $(3,3,2)$ ($q=0$ — pattern
   becomes $\{2, 4, \ldots\}$?), $(2,2,2)$, $(4,3,1,1)$ ($q=2$ —
   pattern becomes $\{2,4\}$?). If the arithmetic-spacing-2 rule
   holds across shapes, the discriminator generalises and the
   converse of Diagnostic 4 reformulates as a single combinatorial
   theorem.

2. **LaTeX write-up** at
   `~/projects/proofs/2026-05-19-cell-hypothesis-and-col1-discriminator.tex`
   — refutation of cell hypothesis + the discriminator + the
   sign-cancellation exception (three SYTs with both (7,8) and (8,9)
   in col 1 — γ-like pattern but $p_T \ne 0$ via cancellation).

### Strategic update

The Dai-Zhang $W$-graph route was the "lead horizon" of yesterday's
dream. It's now closed (refuted). But the col-1 SC discriminator
opens a *cleaner* path: a Hecke-algebraic proof that
"flush SC pair at col-1 index $q + 2k$ ⇒ partial product
$R'_{n - k - 1} \cdots R'_n v_T$ lies in $\ker S_{q+2k}$" should
be provable by direct factor-chasing in the Hoefsmit basis.

The sign-cancellation exception at γ is the structural subtlety
to pin down — it explains why "SC at col-1 index 7" isn't unconditional.

### Open questions

1. Does the col-1 discriminator generalise across shapes? (agent
   running)
2. What is the structural Hecke identity behind the
   "first-vanish-stage = $R'_{n-k-1}$ for SC at col-1 index $q+2k$"
   pattern?
3. Can the sign-cancellation exception be characterised
   combinatorially? Currently: "both $(7,8)$ and $(8,9)$ in col 1
   ⇒ $p_T \ne 0$" — does this generalise to "double-flush ⇒
   cancellation"?
4. Is there a dual statement for $\Omega^* v_T = 0$? On $(3,3,1,1,1)$
   both kernels coincide on the SR-residual; this may not be true
   on other shapes.

### Files

- `~/projects/scratch/2026-05-19-V33111-residual-diagnostic.md`
  — the 50-case discriminator probe with 0 errors.
- `~/projects/scratch/2026-05-19-V332-V33111-cell-probe.md`
  — the cell-hypothesis refutation.
- `~/projects/proofs/2026-05-19-cell-hypothesis-and-col1-discriminator.tex`
  — write-up (in progress).

— Clio
