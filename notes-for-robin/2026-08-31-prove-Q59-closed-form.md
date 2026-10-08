# For Robin — PROVE 2026-08-31: Q59 closed, and the interesting part is *why the plan was wrong*

## The result

Level-1 $q$-deformed Fock space, $R_e(t)=\sum_h t^h N_e^{(h)}$ the $e$-ribbon addition
operator graded by ribbon height. For every Chevalley generator and every pair of
partitions I now have the commutator entry in closed form:

$$[e_i,R_e(t)]_{\nu\lambda}=(\alpha-\beta)\,q^{-\phi-\alpha}\,t^{s}\,(1+qt),
\qquad
[f_i,R_e(t)]_{\nu\lambda}=(\alpha'-\beta')\,q^{\psi-1}\,t^{s}\,(1+qt).$$

It is zero unless $\nu/\lambda$ is an $(e-1)$-ribbon (resp. $(e+1)$-ribbon), and all
four statistics are single reads off the abacus of $\lambda$. Write $M=\{\lambda_j-j\}$
and $m=\mathbf 1_M$; if the ribbon corresponds to the bead move $a\mapsto a+e-1$ then
$\alpha=m(a-1)$, $\beta=m(a+e)$, $s=\#(M\cap[a+1,a+e-2])$, and $\phi$ is a
step-$e$ alternating bead sum below $a$.

Q59 asked only whether the *shape* $\varepsilon q^kt^b(1+qt)$ held. This names
$\varepsilon$, $k$, $b$, and the vanishing locus: **the commutator is nonzero exactly
when precisely one of the two positions $a-1$, $a+e$ carries a bead.** Asymmetric bead
configurations, nothing else.

Paper: `proofs/2026-08-31-Q59-commutator-rigidity.tex` (+pdf), pushed to
`work-in-progress`. Registry `fock-ribbon-sign-operator.json` updated and validating.

## Why I'm writing rather than just filing it

The session brief (my own, written yesterday) proposed two attacks and ranked them
"cheapest first." **Both were wrong, and the second is wrong in principle** — which is
a more useful thing to have learned than the theorem.

1. *"Rigidity wants a dimension argument — exhibit a rank-1 space the commutator must
   lie in."* No. The rigidity is a **cancellation between two length-two paths**. There
   is no one-dimensional operator space; there is a counting fact about how two moves
   can overlap.

2. *"The functional equation $\Omega R_e(t)\Omega=t^{e-1}R_e(1/t)$ may alone force
   $\deg\le b+1$."* This one I can now say **cannot** work. Since $R_e(t)$ commutes with
   every $K_j$ (an $e$-ribbon contains exactly one cell of each residue, so it does not
   move the $\widehat{\mathfrak{sl}}_e$-weight), the equation relates
   $\Phi^{i}_{\nu'\lambda'}(t)$ to $t^{e-1}\overline{\Phi^{-i}_{\nu\lambda}(1/t)}$. It
   maps the instance $(\nu,\lambda,i,b)$ to $(\nu',\lambda',-i,e-2-b)$. That is a
   **symmetry of the family of instances**, not a constraint on any single instance. It
   can halve your work; it cannot bound a degree. I've recorded both as `dead-end` with
   reasons rather than quietly dropping them.

What did work was a change of language, not a change of strategy. The Chevalley weight
exponent is defined by a *geometric* condition — count addable minus removable $i$-nodes
*strictly below* a given node. On the abacus that becomes

$$N^{\downarrow}_i(\pi,\gamma_c)=\sum_{k\ge1}\big(m(c-ke-1)-m(c-ke)\big),$$

an alternating bead sum along an **arithmetic progression of step $e$** — the same step
the ribbon move uses. That is the whole trick. Once the two ingredients are written in
the same units, the proof is: two bead moves compose to a net one-bead displacement in
exactly two ways, giving four formal path types of which exactly two are ever legal,
with heights $s$ and $s+1$. Four lines of case check. No induction, no case analysis
over ribbon shapes.

A thing I want to flag because it is a *methodological* result and not just a
mathematical one: the brief's throwaway "structural hint" — *expect the paths to cancel
in pairs* — was correct, while both of its ranked strategies were wrong. The hint knew
more than the plan did. I don't yet know what to do with that beyond noticing it.

## Corollaries worth knowing

- $[x_i,B^{[e]}_{-1}]=0$ falls out as a **by-product** ($1+qt$ vanishes at $t=-q^{-1}$).
  The proof nowhere uses it, so this is a genuinely independent proof of the level-1
  first-Heisenberg-mode commutation, not a circular restatement.
- (P1), (P2) and "every entry of $[x_i,P_e]$ is $\pm q^m(q-q^{-1})$" go from
  **`computed` to `proved`**. They had ~10k checks and 0 exceptions behind them; now
  they are corollaries of one boxed formula.
- Every entry of $[x_i,C_e^{(1)}]$ is $0$ or $\pm q^m$ — explicitly
  $-\varepsilon(-1)^s q^{k+s+1}$.

Verification is two-sided (the test loops over the union of predicted and computed
supports, so a *missing* prediction fails exactly like a spurious one): **7328 nonzero
entries, $e\le9$, $|\lambda|\le14$, 0 mismatches**, every support of size 2. Plus the
conjugation symmetry above, confirmed on 858 instances, which is an independent
structural check since it comes from a different theorem (yesterday's $\Omega$-result).

## What this opens, and what I owe

**Q63 (new).** The bead-move classification is not obviously level-1-specific. At Uglov
level $\ell$ a bead move happens on one of $\ell$ runners and the telescope lemma
acquires $\ell$ terms. Does the closed form survive to $\ell\ge2$? That front is
unblocked now (Uglov Prop 3.16's source is on disk), and this is the first tool I have
that might be level-agnostic rather than level-1 machinery in disguise.

**Q61 answered, with a third option.** Yesterday's BROWSE found the shape
$\varepsilon q^kt^b(1+qt)$ in three unconnected arenas and asked which known mechanism
was mine — Zhang's sign-reversing involution, or Wildon–Grinberg's Jacobi–Trudi index
collision. **Neither.** Mine is path-overlap counting. Three mechanisms produce the same
rigid factor, which makes the coincidence more interesting rather than less.

**Owed, and not done** — this was a prove session under a no-email/no-browsing rule, so
PROVE.md's Phase 0 did not happen: fetching Lyra's `route1-crosscheck` results table
from GitHub and diffing it line-for-line against my own `iijima_Bminus1.py` run, then
telling her the answer. **She is explicitly waiting and said she would not ask again
until pinged.** First item of the next wake cycle.

— Clio
