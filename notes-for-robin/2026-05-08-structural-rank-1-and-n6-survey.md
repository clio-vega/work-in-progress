# Structural rank-1 proof + n=6 rank survey (2026-05-08 wake)

## TL;DR

Two new things this session:

1. **Theorem A and B (structural)**: $\Pi^{S_5}$ has rank exactly 1 on
   $V_{(2,2,1)}$ and $V_{(3,1,1)}$, proven by tracking image dimensions
   through each $(T_i+1)$ factor in the seminormal basis. The May-7
   "rank-1 lemma" (verified by Lagrange interpolation) is now a
   structural theorem.

2. **Refutation of the atom-count conjecture**: The May-7 conjecture
   $\mathrm{rank}(\Pi) = \lceil k_\lambda / 2 \rceil$ FAILS at $n=6$:
   - $V_{(4,1,1)}$ at $n=6$: 4 atoms, rank 1.
   - $V_{(3,3)}$ at $n=6$: 4 atoms (same poly!), rank 1.
   The conjecture would predict rank 2 for both. So the original
   atom-count formula doesn't extend to $n=6$. (One-sided upper
   bound $\leq \lceil k/2 \rceil$ still holds across all data.)

## Proof writeup

`~/projects/proofs/2026-05-08-rank-Pi-structural.tex` (.pdf 9 pages,
284 KB). Now in **commit 97159cd** — the **11th** unpushed commit on
local main. PAT still read-only.

Robin: when you fix the PAT, please push. I have:

```
97159cd Structural rank-1 proof for Π^{S_5} on V_(2,2,1) and V_(3,1,1)
308ef06 Rank-one Π^{S_5} on V_(2,2,1) and V_(3,1,1): proves branching factorization
e4582a8 2026-05-06 (evening): isolate the q-integer [3]_q in Theorem B
c8ef671 Trace identity: 3-cross-trace restatement + S_4-DB framework
5c81ba7 2026-05-07: Trace identity D = cross_(3,1,1)→(3,2) — residual reduction
524ae5f Prove fourth cross-trace vanishing cross_(2,2,1)→(3,1,1) = 0
2ae2d5a 2026-05-06 (afternoon): Sign-positivity structural reduction
ea73b68 Q3 refuted, explicit n=5 ι, surprising D = cross identity
c4276ee 2026-05-06: Path-level Theorem B — existence of bigrading-preserving injection
5713857 2026-05-06: Theorem B at multiset level — atom_RTL is a hidden σ_1-G1 atom
94197a6 2026-05-06: Twin identity lifted to multiset-tensor-product structure
```

## Mathematical highlights

### The rank-collapse mechanism

For the staircase reduced word, the second $(T_1+1)$ factor (Step 5,
applied right-to-left) is where rank collapses. Specifically:

- $\mathrm{Im}_4$ lies in $(+q\text{-eig}(T_1)) \oplus (-1\text{-eig}(T_1))$.
- $(T_1+1)$ kills the $-1$-eigenspace components.
- For $V_{(2,2,1)}$: the $+q$-eig component is in span(v_1, v_2),
  and Im_4 has only a 1-dim slice there. So Im_5 is 1-dim.
- For $V_{(3,1,1)}$: the $+q$-eig component is in span($\alpha_4 v_2 +
  \beta_4 v_3$), a single 1-dim line. So Im_5 is 1-dim.
- For $V_{(3,2)}$ (rank 2): the $+q$-eig component is 2-dim
  (span($v_3$, ...)). Step 5 doesn't fully collapse.

The structural distinction between rank 1 and rank 2 at $n=5$ is:
**does $T_3$ kill an extra direction at Step 3?** For $V_{(2,2,1)}$
and $V_{(3,1,1)}$, yes (because of the partition's column structure).
For $V_{(3,2)}$ and $V_{(4,1)}$, no.

### The σ_1 coincidence at n=6

Surprising new datum: **$\sigma_1(V_{(4,1,1)}) = \sigma_1(V_{(3,3)})$**
at $n=6$. Both equal
$q^3 + 15q^4 + 91q^5 + 281q^6 + 484q^7 + 484q^8 + 281q^9 + 91q^{10} + 15q^{11} + q^{12}$.

Both have rank 1, but $\dim V_{(4,1,1)} = 10$ and $\dim V_{(3,3)} = 5$,
so they're certainly distinct reps.

This is unique among $n \leq 6$. At $n \leq 5$ all $\sigma_1$ values
are distinct.

### Sub-family rank formulas (still conjectural beyond n ≤ 6)

- $\mathrm{rank}\,\Pi^{S_n}|_{V_{(n-1, 1)}} = \lceil (n-2)/2 \rceil$
  (verified $n \in \{3,4,5,6\}$).
- $\mathrm{rank}\,\Pi^{S_n}|_{V_{(n-2, 2)}} = n - 3$
  (verified $n \in \{4,5,6\}$).

## Computational verification

`~/projects/scratch/2026-05-08-rank-Pi/verify_seminormal.py` runs
the iterative image computation in sympy at $q = 7$ rational. It
confirms:

```
V_(2,2,1):  image dim sequence (2, 2, 2, 2, 1, 1, 1, 1, 1, 1)
V_(3,1,1):  image dim sequence (3, 3, 3, 3, 1, 1, 1, 1, 1, 1)
V_(3,2):    image dim sequence (3, 3, 3, 3, 2, 2, 2, 2, 2, 2)
```

The drop happens at Step 5, exactly where my proof predicts.

## Open questions

The general rank-characterization problem is still open. Possible
candidates I haven't ruled out:
- A multi-step sub-family analysis where rank is determined by
  $\lambda$'s "first-column structure" interacting with the staircase
  word at each step.
- Maybe rank counts something dual to the σ_1-atom count: the
  number of "generic" SYTs minus the number of "constrained" SYTs.

Empirically: at $n=6$, rank ranges 0 to 3, with rank 3 only for
$V_{(4,2)}$. So there's still a clean stratification by rank.

## Context

The May-7 work on the trace identity $D = \mathrm{cross}_{(3,1,1) \to (3,2)}$
reduced to the rank-1 lemma for $V_{(2,2,1)}$ and $V_{(3,1,1)}$.
That lemma is now a **structural theorem** (Theorem A, Theorem B
in the new writeup). So the branching factorization conjecture
of `2026-05-06-D-cross-T-A-factorization.tex` (Conjecture 5.1) is
**fully proven** — no longer "modulo a structural lemma."

The remaining structural questions on the trace identity are about
the cross-flow into $V_{(3,2)}$ — the LHS of the refined residual
identity in `2026-05-07-rank-one-Pi.tex` Corollary 5.4. That cross-
flow does NOT have a rank-1 collapse (since $V_{(3,2)}$ has rank 2),
so it requires different machinery.

## Email

Cannot send email this session — Gmail MCP unauthenticated.
This file in `for-robin/` is the deliverable.
