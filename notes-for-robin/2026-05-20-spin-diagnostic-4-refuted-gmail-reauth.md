# Notes for Robin — 2026-05-20 wake

## Two items

### 1. Gmail MCP needs re-auth (again)

The Gmail tools are unavailable this session — only `authenticate` and
`complete_authentication` are exposed. This is the same failure mode that
hit yesterday morning's session ("4 sessions running" theory). If you
have a moment to re-auth, the inbox is unchecked since 2026-05-19 PM.

Not blocking — I'll check after re-auth.

### 2. Spin-Diagnostic-4 from last night's dream-2: **refuted at the
seminormal-basis level**

Last night's dream-2 conjectured a *Frobenius-super universal* form of
the per-diagonal trace-vanishing dichotomy:

> For every Frobenius superalgebra $A$, in the $\mathcal{W}_n^{(1)}(A)$-module:
> $p_T^c = 0 \iff \Omega^c v_T = 0 \lor (\Omega^c)^* v_T = 0$.

I tested the most natural lift at $A = \text{Cl}_1$ (the Hecke-Clifford
case) using the Chen-Wan seminormal form (arXiv:2605.11778). Across 8
strict partitions and ~5,500 basis vectors, **no diagonal entry ever
vanishes**.

**Structural diagnosis (the meat).** Shifted contents $c - r \ge 0$,
always. So the JM ratios $X_k X_{k+1}^{-1}$ on a completely-splittable
irreducible are pure positive $q$-powers — never cyclotomic poles. The
type-A trace-vanishing mechanism *requires* negative-content cells (the
$1^q$ tail of $\lambda = (\hat\lambda, 1^q)$), which strict-partition
shapes cannot host.

This is the **eighth methodological shadow** of the month. The pattern is
becoming a §10 chapter of the dichotomy survey: cheap probe (one
afternoon) → refutation → structural diagnosis → recovery of the
categorical layer where the lift *might* still survive.

What survives:
1. The whole-module supertrace question is open. (Not refuted by this
   probe — the per-basis check doesn't touch it.)
2. The HOMFLY-Hilb bidegree lift remains structurally plausible.
3. The right "spin tail" structure (no $1^q$ analog in strict
   partitions) is unidentified.

What this does to the chapter:
- Removes the "Frobenius-super universalisation chapter" from the
  expansion menu in its naïve form.
- Confirms the Hecke side is where the proof technology lives; reorients
  attention back to the SL_γ structural proof at $(3,3,1,1,1)$.

Paper: `proofs/2026-05-20-spin-diagnostic-4-refuted.tex` (commit
`ffd1d24`, 6 pp, pushed). Script:
`scratch/2026-05-20-spin-diagnostic-4.py`.

## Next prove session target

SL_γ structurally at $(3,3,1,1,1)$ — finish the col-1 SC discriminator's
last lemma using the $V_+/V_-$ template. This is the concrete piece I
was set to do today before the spin probe surfaced as higher-leverage;
now back on the active queue.

— Clio
