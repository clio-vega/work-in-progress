# Sign-positivity for (3,2)/(4,1): structural reduction

**Date:** 2026-05-06 (afternoon prove session)
**Status:** Proved.
**Writeup:** `~/projects/proofs/2026-05-06-sign-positivity-structural.tex` (commit `2ae2d5a`, unpushed due to PAT block).

## What

The sign-positivity lemma underlying Theorem B's multiset form asserts:
$$M_{(4,1)} \le 2 M_{(3,2)} \quad \text{and} \quad M_{(3,2)} \le 2 M_{(4,1)} \quad \text{on } B_4.$$

I gave a **structural reduction** of this lemma to two single-component multiplicity bounds:
$$\boxed{m^{(3,2)}_2 \ge 2 \quad \text{and} \quad m^{(4,1)}_1 \ge 2.}$$

The reduction uses the canonical $B_4$-decomposition
$$M_{(3,2)} - M_{(4,1)} = (0, +2, -2),$$
which is the multiplicity-vector form of Theorem C: $A_{(3,2)} - A_{(4,1)} = 2q(q^2+q+1)$.

Then $\mathrm{atom}_{\mathrm{RTL}} = M_{(3,2)} + (0, +2, -2) = (m^{(3,2)}_0, m^{(3,2)}_1+2, m^{(3,2)}_2-2)$,
so non-negativity reduces to $m^{(3,2)}_2 \ge 2$. Symmetrically for $\mathrm{atom}_{\mathrm{LTR}}$.

Both bounds verified by enumeration: $m^{(3,2)}_2 = 3 \ge 2$ and $m^{(4,1)}_1 = 3 \ge 2$. Each has slack 1, matching $\mathrm{atom}_{\mathrm{RTL}}[2]$ and $\mathrm{atom}_{\mathrm{LTR}}[1]$ respectively.

## Why it's worth flagging

This is a **clean reformulation** of an inequality you might have read as just "checked numerically." Now we know:

1. The sign-positivity is reducible to **two** specific multiplicity inequalities, each on a **single component** of a **single** atom. No cross-comparison needed.
2. The slack of each atom-RTL/LTR is **localized**: the slack at a specific component equals the (slack-1) saturation of the corresponding bound. The other components have automatic slack.
3. The "(0, +2, -2)" structure of $M_{(3,2)} - M_{(4,1)}$ is the **canonical $B_4$-decomposition** of $2q(q^2+q+1)$ — a structural object — and this same vector recurs in both atom slacks (with sign flipped).

## What's still open

A **W-graph-natural lower bound** on $m^{(3,2)}_2$ and $m^{(4,1)}_1$ — i.e., proving these two inequalities WITHOUT enumerating all closed paths. The bounds are about path counts at a specific $\bar c$ in a specific cell. A spectral argument on the W-graph adjacency operator would presumably work but has not been done.

The other big open: a **canonical** path-level injection $\iota$. The new structural reduction gives a structural read of the slack but doesn't pin down which specific path is the "atom slack". (For atom_RTL = (1,7,1) the slack-1 components are at $\bar c \in \{0, 2\}$; for atom_LTR = (1,1,7) at $\bar c \in \{0, 1\}$.)

Branching observation included in the writeup: at $\bar c = 2$, all 5 V_(4,1)-paths start at a V_(3,1)-branching vertex, but V_(3,2) has only 2 V_(3,1)-branching paths at $\bar c = 2$ (i.e., 4 slots in two copies). One V_(4,1)-path **must** go to a V_(2,2)-branching slot. This is a lower bound on the non-branching content; doesn't single out the slack path.

## Where this fits

This is a small but real result that complements the existing Theorem B writeups (multiset and path-level). It addresses the PROVE.md backup target ("sign-positivity lemma") and gives a structural framing of the slack. The main path-level Theorem B remains open in its strong "canonical" form; this reduction is a step toward it but does not close it.

I'm flagging this because the **exact** form of the reduction (two specific bounds + the (0,+2,-2) decomposition) might be useful when you're thinking about whether the same machinery applies to other partition pairs $(\lambda, \mu)$ with simple $A_\lambda - A_\mu$ differences. If so, sign-positivity for those pairs might similarly reduce to a small number of single-component bounds.

— Clio
