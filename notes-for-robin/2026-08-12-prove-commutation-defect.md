# For Robin — PROVE 2026-08-12: Chevalley annihilation at $q=1$, $(q-1)$-defect at generic $q$

## TL;DR

Yesterday's WAKE proposed a naive strict theorem
$$
e_i \cdot v_{k',e} \;=\; 0 \quad \text{(at generic $q$)}
$$
as a candidate structural direction for Conjecture 10, based on the Uglov Fock
tensor decomposition $\mathcal F_e \cong V(\Lambda_0) \otimes \mathcal H$
(Heisenberg-commutant reframing).

**Today's PROVE session refuted this at generic $q$** but proved its $q=1$
specialization (classical Frenkel-Kac). Along the way, discovered a stronger
empirical structural statement (Conjecture C4 below) verified in 84 instances.

**Files landed:**
- `proofs/2026-08-12-commutation-defect.tex` (7pp, compiled — 320KB PDF)
- Three probes in `probes/2026-08-12-commutation-defect/` (all pass)

**GitHub push:** not yet pushed. If you want to review, tell me and I'll push
to https://github.com/clio-claude/proofs.

## What I proved (T1--T3)

**T1--T2 (Frenkel-Kac at $q=1$).** For all $e \ge 2$ and $i \in \mathbb Z/e\mathbb Z$:
$$
[e_i, P_e]\big|_{q=1} \;=\; 0 \quad\text{as operators on $\mathcal F_e|_{q=1} \cong \Lambda$.}
$$
**Proof:** Farahat identifies $P_e|_{q=1}$ with multiplication by $p_e$;
Kac 1990 Cor.\ 14.10 gives the tensor decomposition
$V(\Lambda_0) \otimes \mathbb Q[p_e, p_{2e}, \ldots]$ where the $\widehat{\mathfrak{sl}_e}$-action
is trivial on the second factor. Hence $p_e$ commutes with $e_i^{\text{cl}}$.
By induction on $k'$ (base case $e_i|\emptyset\rangle = 0$),
$(e_i \cdot v_{k',e})|_{q=1} = 0$.

**T3 ($(q-1)$-divisibility at generic $q$).**
$e_i \cdot v_{k',e} = (q - 1) \cdot R_{i,k',e}^{(1)}$ for an explicit Fock
vector $R^{(1)}$. Immediate from T1--T2 plus: any Laurent polynomial in $q$
vanishing at $q=1$ is divisible by $(q-1)$.

## What I discovered (empirical Conjecture C4)

$$
[e_i, P_e] \;=\; (q - q^{-1}) \cdot X_i \quad\text{as operators on $\mathcal F_e$}
$$

for some operator $X_i \in \operatorname{End}(\mathcal F_e)$. **Verified in every
tested case:**
- 84 $(e, i, \lambda)$-triples for $\lambda$ ranging over small partitions at
  $e \in \{2, 3, 4\}$ (`probe_commutator.log`)
- 17 $(e, k', i)$-triples for $ek' \le 12$ verifying the induced $e_i v_{k',e}$
  divisibility (`probe_q1.log`)

By induction, C4 implies $e_i \cdot v_{k',e} = (q - q^{-1}) R_{i,k',e}$, the
sharper (second-order) version of T3.

**Why C4 should be true (heuristic).** Clio's $P_e$ is the naive ribbon-sign
operator $\sum (-q)^h |\mu\rangle$. Uglov's exact quantum-commuting-Heisenberg
generator $B_1^{[e]}$ satisfies $[e_i, B_1^{[e]}] = 0$ strictly (Uglov 1999).
Numerically, $P_e$ and $B_1^{[e]}$ agree at $q = 1$ (both are multiplication by
$p_e$, via Farahat) and I conjecture agree to order $(q - q^{-1})^0$ in a
sense that produces
$$
P_e - B_1^{[e]} \;=\; (q - q^{-1}) \cdot C_e^{(1)}
$$
for some operator $C_e^{(1)}$. If so, C4 is immediate: $[e_i, P_e] = [e_i, B_1^{[e]}] + (q - q^{-1})[e_i, C_e^{(1)}] = 0 + (q-q^{-1}) X_i$.

To prove C4 rigorously I'd need Uglov's explicit formula for $B_1^{[e]}$ on the
standard basis. This is a **reading task, not a PROVE task** — worth a browse
or expository session before the next PROVE attempt.

## Where I broke the naive theorem candidate

The reframing's chain of reasoning:
1. $\mathcal F_e \cong V(\Lambda_0) \otimes \mathcal H$ (Uglov 1999 at level 1). ✓
2. $\mathcal H$ commutes with $U_q(\widehat{\mathfrak{sl}_e})$. ✓
3. $P_e^{k'}|\emptyset\rangle$ is a pure Heisenberg descendant. ✗ (this is
   where the wheels come off — Clio's $P_e$ is not literally in $\mathcal H$
   at generic $q$)
4. Therefore $e_i \cdot v_{k',e} = 0$ at generic $q$. ✗

Step 3 assumed $P_e = B_1^{[e]}$ at generic $q$. False. Concrete
counterexample (Example 4.2 of the writeup):
$$
[e_1, P_3]|\emptyset\rangle \;=\; (q^2 - 1) |(1,1)\rangle \;\ne\; 0
$$
at generic $q$. Nonzero at generic $q$ but vanishes at $q = \pm 1$ — the
$(q^2 - 1) = q(q - q^{-1})$ divisibility that C4 says holds always.

## Status for Conjecture 10 ($\varepsilon_i(v_{k',e}) = 1$)

**Not resolved.** Kashiwara operators $\tilde e_i$ live at $q = 0$; the T1--T3
+ C4 machinery lives at $q$ generic / $q = 1$. The bridge is Conjecture C5 in
the writeup:
$$
\tilde e_i (v_{k',e} \bmod q\mathcal L) \;=\; \text{class of } R_{i,k',e} \text{ in } \mathcal L/q\mathcal L,
$$
which would give $\varepsilon_i \le 1$ if combined with a $\tilde e_i R = 0$
statement one step down.

This is now the cleaner target: instead of a shopping list of "attack surfaces"
we have a specific bridge to prove. But it requires Kashiwara lattice /
crystal-basis theory on level-1 Uglov Fock, which I don't yet have. Prep
would be reading Ariki-Kleshchev + Kashiwara 1993 in a BROWSE / expository
session.

## What this means for v1

The Q34 WAKE-of-today reframing was **correct** about the lens (tensor
decomposition is the right structure) and **wrong** about the specific
operator. §7's footnote should update from
> "Conjecture 11 has candidate structural direction (Heisenberg commutant)."

to something more honest:
> "The $q=1$ Chevalley-Heisenberg commutation is classical (Kac Cor.\ 14.10)
> and gives $(e_i \cdot v_{k',e})|_{q=1} = 0$; empirically, at generic $q$ the
> defect is $(q-q^{-1})$-divisible at the operator level (verified over 84
> instances at $e \le 4$), consistent with Clio's $P_e$ differing from Uglov's
> exact commuting-Heisenberg generator $B_1^{[e]}$ by an $O(q-q^{-1})$
> correction. Bridging this to the Kashiwara $\varepsilon_i$-value at $q=0$
> remains open."

Stronger than yesterday: we now have a **proved** classical statement plus a
**precise empirical conjecture**, rather than a heuristic "structural
direction." Still doesn't close Conjecture 10, but the target is much sharper.

## Container-health notes

- **Metabolism win:** the WAKE-of-today reframing was refuted by PROVE-of-today
  in the same container-day. This is exactly the metabolism the P5--P7
  principles predict — always test empirically before committing to a
  "structural direction."
- **The refutation strengthened the picture, not weakened it.** The naive
  theorem was aesthetically nice but ambiguous about which operator was
  meant; today's C4 pins it down and turns the vague "structural direction"
  into a testable operator identity.
- **Sage still not installed.** I checked again; `sage --version` fails. All
  my PROVE work today ran on plain Python 3.

## What I'd like from you (optional)

- **Sanity-check on the classical proof.** The Frenkel-Kac argument in
  Theorem 1 uses Kac's Cor.\ 14.10 as a black box. If you have access to
  Kac 1990 or can confirm the statement (basic $\widehat{\mathfrak{sl}_e}$-rep
  $V(\Lambda_0)$, decomposed as tensor product with $\mathbb Q[p_e, p_{2e},\ldots]$
  where the second factor is $\widehat{\mathfrak{sl}_e}$-trivial), that would
  be reassuring.
- **Uglov reference confirmation.** I cite Uglov 2000 (Progress in Math 191)
  = arXiv:math/9905196 for the level-1 commuting Heisenberg generator
  $B_1^{[e]}$. If you know a cleaner reference for its explicit formula on
  the standard basis of $\mathcal F_e$, that's the missing ingredient for
  proving C4.
- **Kashiwara-side reading pointer.** If Conjecture C5 is close to something
  you've seen (Ariki-Kleshchev? Grojnowski? Kleshchev's book?), pointer would
  save a BROWSE session.
