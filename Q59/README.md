# Q59 — closed form for the Chevalley commutator with $R_e(t)$

`2026-08-31-Q59-commutator-rigidity.tex`. Every matrix entry of $[x_i, R_e(t)]$ on
level-1 $q$-Fock space, $x \in \{e_i, f_i\}$, equals $\varepsilon q^k t^b (1+qt)$ with
$\varepsilon, k, b$ given explicitly by three bead statistics of the abacus. The question
asked whether the entries were *constrained* to that shape; the answer *determines* them.

**Mechanism:** two bead moves compose to a net one-bead displacement in exactly two ways,
at consecutive ribbon heights $s$ and $s+1$. That is the $(1+qt)$. Four-line case check,
no induction, no case analysis over ribbon shapes.

Corollaries: a new proof that $B^{[e]}_{-1} = R_e(-q^{-1})$ commutes with
$U_q(\widehat{\mathfrak{sl}}_e)$; (P1), (P2) and the $(q-q^{-1})$-divisibility of
$[x_i,P_e]$ entries promoted `computed` → `proved`.

Verification: 7328 nonzero entries, $2\le e\le 9$, $|\lambda|\le 14$, 0 mismatches,
two-sided by construction (union of predicted and computed supports, so a missing entry
fails exactly like a spurious one); plus a per-type row-by-row check, 25874 checks, 0
failures, designed to catch compensating errors.

**Two negative results, recorded with reasons.** The brief's ranked attack 1 (rank-1
dimension argument) is not the mechanism. Attack 2 (functional-equation degree bound) is
impossible *in principle*: the functional equation is a symmetry of the family of
instances, so it cannot bound a single instance — it is an antipode, and
anti-automorphisms permute structure constants rather than bounding them. Repurposed as
an independent check (858 instances, 0 failures).

**Not claimed as new:** $R_e(t)$ is the LLT spin-graded ribbon Pieri operator. The closed
form and the bead-move reformulation are what is claimed.

Open successor: does this survive to Uglov level $\ell \ge 2$ (Q63)?
