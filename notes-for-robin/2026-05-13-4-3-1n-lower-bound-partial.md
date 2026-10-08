# Partial progress on (4, 3, 1^q) structural lower bound

**Date:** 2026-05-13 afternoon prove session
**Paper:** `2026-05-13-4-3-1n-lower-bound-analysis.tex` (9 pp, commit `7be30b7`, unpushed — PAT still read-only as of session start)
**Status:** Honest partial. A vs B decoupling fully structural. Within-class linear independences left as two finite Hoefsmit tracer computations.

## What I set out to do

The morning's `2026-05-13-4-3-1n-upper-bound.tex` proved $\dim B^{(\lambda)}_{j_0} V_\lambda \le 5$ structurally at $q \ge 5$ for $\lambda = (4, 3, 1^q)$, with computational verification dim $= 5$ at $q \in \{3, 4\}$. The structural lower bound $\ge 5$ was the natural next step.

## What I did

Wrote the explicit five-vector construction via two layers of lifting and proved cleanly that the A vs B coupling is broken by the position-of-$n$ projection alone, reducing the full $5$-vector independence to two within-class projection independences.

**Theorem 3.2 (clean structural statement):** Suppose
- (a) $\{\pi^{(c_1)}_n F_A^i\}_{i=1}^2$ are linearly independent.
- (b) $\{\pi^{(c_2)}_n F_B^j\}_{j=1}^3$ are linearly independent.

Then $\dim B^{(\lambda)}_{j_0} V_\lambda \ge 5$.

The proof uses only position-of-$n$ via the exclusive cells $c_1 = (1, 4)$ (A-only) and $c_2 = (2, 3)$ (B-only). No analysis of the $c_3$-direction is needed (Remark 5.6). This is cleaner than the May-12-Eve3 statement, which conflated the decoupling with a $c_3$-noncancellation claim.

## What I found out

Tried to prove (a) and (b) by lifting the May-12-Eve3 / May-12-dim-2-321 position-of-letter separators through the outer chain. **The natural separator gets contaminated by the chain of $T_j$ moves.**

Specifically: the $(4, 3, 1^q)$ shape requires **three layers of recursion** ($\mu_1^A = (3, 2, 1^{q-2}) \to \mu_A = (3, 3, 1^{q-1}) \to \lambda$), with a total of $9$ $(T_j+1)$ factors in the cumulative chain. The 9-step orbit of position-of-letter for the natural separator includes the originally-exclusive cell of the *other* inner basis vector.

This is a structural fact, not a defect of the proof method.

**Heuristic rule (Remark 6.4):** position-of-letter techniques exhaust at recursion depth $\le 2$. For depth $3+$ shapes, finer tools are needed.

## What's next

The right tool, per the session's `tracer-pair-technique` memory note, is to compute explicit $5 \times 5$ tracer matrix entries via Hoefsmit factors. By the A vs B decoupling, this reduces to:

1. A $2 \times 2$ tracer for $\{F_A^1, F_A^2\}$. Five nested Hoefsmit factors per entry. Structural at large $q$ (cited from May-12-dim-2-321 + SRD-331 inner inputs); computational at $q \in \{3, 4\}$.
2. A $3 \times 3$ tracer for $\{F_B^1, F_B^2, F_B^3\}$. Lifts May-12-Eve3's position-of-$(n-1)$ analysis plus the outer factor $(T_{n-5}+1)$ specific to $(4, 3, 1^q)$.

Each entry is finite and computable. The total work is parallel to May-12-Eve3 \S5-7, scaled up roughly $5\times$ in case count.

## Honest reflection

I tried to bull-rush this and produce a full structural proof. The contamination phenomenon stopped me — I kept hoping a clever position separator would survive, and it didn't, at any depth. The right move is to put down the position-of-letter hammer and pick up the Hoefsmit tracer. That's the structural lesson of this session.

A separate cleaner target for a future session: the structural $\dim \ge 2$ for $(3, 3, 1^q)$, which is also open (SRD-331 Remark 3.4) and a prerequisite for the $(4, 3, 1^q)$ proof. The recursion depth there is only 2 ($\mu_1^A \to \mu_A$), so position-of-letter might still work — I should try the cleaner case first.

## What I want next

- Push the paper (PAT still read-only — Robin, can you fix? **36 unpushed commits + this one = 37 unpushed** on `clio-vega/proofs`).
- Decide: should I attempt $(3, 3, 1^q)$ lower bound (depth 2) before $(4, 3, 1^q)$ (depth 3)? The smaller target is a clean prerequisite and uses the same machinery.

— Clio
