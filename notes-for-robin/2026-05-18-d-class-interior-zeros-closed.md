# For Robin — 2026-05-18 prove session: D-class interior zeros closed

The PROVE session today targeted the D-class interior zeros at $(3,3,1,1,1)$
that the survey flagged in §7.4. They are closed.

## Headline

The 78 D-class zero diagonals at $(3,3,1,1,1)$ are now fully explained by a
**two-sided kernel dichotomy**:
$$
   p_T(q) \;=\; 0
   \;\Longleftrightarrow\;
   \Omega\, v_T = 0
   \;\;\text{or}\;\;
   \Omega^* v_T = 0,
$$
where $\Omega^* = L_n L_{n-1} \cdots L_{\ell+1}$ with $L_k = S_1 S_2 \cdots
S_{k-1}$ is the anti-involution image of $\Omega$ in $H_q(S_n)$.

The 78 D-class zeros split as:
- **76 in $\ker(\Omega)$** (column-zero — vanishes via iterated rightmost
  factor of $\Omega$, e.g., $\Omega = (\text{stuff}) \cdot R'_n$ killing
  descent-1 cases).
- **2 in $\ker(\Omega^*) \setminus \ker(\Omega)$** (row-zero only) — these
  are the "interior" cases that were flagged as open:
  - $T_a = ((1,2,3),(4,5,8),(6),(7),(9))$
  - $T_b = ((1,2,3),(4,6,8),(5),(7),(9))$.

## What's actually proved

1. **Sufficient direction** (Lemma~1 + Corollary~3 of the paper):
   if $\Omega v_T = 0$ or $\Omega^* v_T = 0$, then $p_T = 0$. The column
   case is trivial; the row case uses the standard b'=1 ↔ b=1 seminormal
   basis rescaling to identify "row T of $\Omega$ matrix is zero" with
   "$\Omega^* v_T = 0$". Both are clean Hecke-algebra facts.

2. **Computational verification on all 120 SYTs**: the dichotomy holds
   exactly. 0 violations. $|\ker \Omega| = 105$, $|\ker \Omega^*| = 48$,
   overlap $= 45$, union $= 108$. The remaining 12 basis vectors are the
   nonzero diagonals.

## Structural insight: dim B = 2

The image $B := \Omega V^\lambda$ has $\dim B = 2$ at $(3,3,1,1,1)$ — a
striking compression of the 120-dim Specht to a 2-dim image. This is what
makes the kernel structure so rigid: there's very little room for "subtle
interior cancellation" beyond row/column vanishing.

For the row-zero side, the universal containment $B \subseteq E^+_\ell$
(from the leftmost factor of $\Omega$) already gives row-zero for all 26
SC tableaux (Diagnostic 3). The additional 22 row-zero basis vectors at
$(3,3,1,1,1)$ come from a deeper iterated-leftmost-factor argument that
gives $B \subseteq R'_{\ell+1} V$ — a much smaller subspace than $E^+_\ell$
when $\dim B$ is as small as 2.

## What I conjectured but didn't prove

Two combinatorial characterisations are left open:

- **Conjecture 1 (Stratification of $\ker \Omega^*$):** $v_T \in \ker
  \Omega^*$ iff there exists $k \in \{\ell+1, \ldots, n\}$ such that the
  partial product $L_k L_{k-1} \cdots L_{\ell+1}$ applied to $v_T$ lies in
  $\ker L_{k+1}$.
- **Conjecture 2 (Stratification of $\ker \Omega$):** mirror of
  Conjecture 1 for the rightmost-factor chain $R'_{\ell+1} \cdots R'_n$.

Together these would give a fully combinatorial diagnostic for $p_T = 0$.

The non-trivial forward direction of the dichotomy itself (every $p_T$-zero
is one-sided) is also empirical only, but the rank-2 structure of $B$ makes
me think it generalises to all $\tau = 0$ shapes where $\dim B$ is small.

## Paper

`~/projects/proofs/2026-05-18-d-class-row-zero.tex`, commit `8d25cf9`,
pushed to `clio-vega/proofs`. 6 pages.

## Sequel implications for the survey

§7.4 of `2026-05-17-survey-trace-vanishing-dichotomy.tex` flags the 68
interior D-class zeros as open. **That count was wrong (the actual count is
2, not 68)** — the 68 figure conflated all D-class zeros with the interior
ones. Today's paper corrects this and closes them.

The survey's §7 (per-SYT diagnostics) can be extended with a fourth
diagnostic: the row-zero / anti-involution mirror of Diagnostic 3, which
catches the 22 + 2 = 24 deeper row-zero cases. I haven't drafted the
update yet; let me know if you'd like me to extend §7 or write it as a
standalone "Diagnostic 4" paper.

## Compute / scripts

Verification scripts in `~/projects/scratch/2026-05-18-d-class-zeros/`:
- `support_analysis.py` — the discovery that 76/78 D-class zeros have
  $\Omega v_T = 0$ outright.
- `kernel_structure.py` — computes rank$(\Omega) = 2$ and stratifies
  $\ker(\Omega)$ by depth from the right.
- `check_anti_involution.py` / `check_anti_numeric.py` — verifies
  $T_i$ self-adjointness fails in b'=1 (as expected) but the row-zero ↔
  $\Omega^* v_T = 0$ correspondence holds (via b=1 rescaling).
- `verify_dichotomy_all.py` — final all-120 verification: 0 violations.

## Ops

- Gmail MCP still needs `/mcp` re-auth; this note remains a pending draft.
- Push works; commits `8d25cf9` is on `clio-vega/proofs`.

Best,
Clio
