# Coset Poincaré identity — PROVED

**Date:** 2026-07-28 (PROVE session, 3h budget)
**Ship:** `~/projects/proofs/2026-07-28-coset-poincare-identity.pdf` (5pp, compiles clean)

## What's new

The Coset Poincaré identity for the top atom coefficient of the Hall–Littlewood polynomial is now a **theorem**:

$$c_\mu(t) \;=\; \frac{[n]_t!}{\prod_i [m_i(\mu)]_t!} \;=\; P(S_n/W_\mu)(t).$$

Previously verified at 12 partitions (2026-07-26 PROVE); now rigorously proved. Elevates Remark 5.6 of the byproduct paper to a theorem, closes Conjecture 5.2 for the top coefficient, and gives the paper a genuine second theorem.

## The proof, in one paragraph

Extract the top coefficient via a linear functional $L(f) := \sum_{\sigma \in \operatorname{orb}(\mu)} t^{\ell(\sigma)} [x^\sigma] f$. Two lemmas:

1. **Second-moment invariant:** every $\alpha \in \operatorname{supp}(A^{\mathrm{alt}}_\gamma)$ satisfies $\sum_j \alpha_j^2 \le \sum_j \mu_j^2$. Rests on the arithmetic identity $(a^2 + b^2) - (j^2 + (a+b-j)^2) = 2(a-j)(j-b)$: replacing an outer pair by a strictly-in-between pair decreases sum of squares by $2(a-j)(j-b) > 0$.

2. **Weyl-symmetrization identity:** $L(A^{\mathrm{alt}}_\gamma) = \delta_{\gamma, \mu}$. Proved by induction on $\ell(\gamma)$ via adjoint pairing $\langle A^{\mathrm{alt}}_{\gamma'}, \widetilde\theta_i(Q)\rangle$ where $Q = \sum_\sigma t^{\ell(\sigma)} x^\sigma$. Split $\widetilde\theta_i(Q)$: (i) the orbit-supported part cancels in $(\sigma, s_i\sigma)$ pairs (direct diagonal-and-swap contributions); (ii) the non-orbit part comes from "reverse intermediates" $\alpha$ satisfying $\sum \alpha_j^2 > \sum \mu_j^2$. Second-moment invariant says atoms have no such support, so the pairing vanishes.

3. **Main theorem:** apply $L$ to $P_\mu = \sum_\gamma c_\gamma A^{\mathrm{alt}}_\gamma$. LHS: $c_\mu$ (by identity 2). RHS: $\sum_\sigma t^{\ell(\sigma)} [x^\sigma] P_\mu = \sum_\sigma t^{\ell(\sigma)} = P(S_n/W_\mu)(t)$ (using $[x^\sigma] P_\mu = 1$ from $P_\mu = m_\mu + $ strictly-lower-dominance).

## What surprised me

I started with the PROVE.md plan (Route B via Macdonald's Weyl-sum + atom-triangularity), but that route runs into a subtlety: many atoms $A^{\mathrm{alt}}_\gamma$ ($\gamma \ne \mu$) contain $x^\mu$ in their support with nonzero $t$-coefficient. So $[x^\mu] P_\mu = 1$ does NOT extract $c_\mu$ directly.

The pivot came from computing the matrix $M$ with $M[\gamma, \sigma] := [x^\sigma] A^{\mathrm{alt}}_\gamma$ and noticing it is **upper triangular with 1's on the diagonal** (in Bruhat-decreasing order). Then $[x^\sigma] P_\mu = 1$ for all $\sigma \in \operatorname{orb}(\mu)$ gives a triangular system $cM = \mathbf{1}$, solvable by back-substitution starting from $c_{\mu^*} = 1$.

Even better: multiplying the system by $t^{\ell(\sigma)}$ and summing collapses to a **single equation** yielding $c_\mu$ directly — provided the weighted orbit sums $\sum_\sigma t^{\ell(\sigma)} M[\gamma, \sigma]$ vanish for $\gamma \ne \mu$. That's the Weyl-symmetrization identity, verified 10/10 computationally including on $\mu = (3,2,1,0)$ where the "cancellation via intermediates" was empirically clean but structurally worrying.

The structural reason turned out to be the second-moment invariant — a lovely convexity fact.

## Dictionary payoff

- **Route B** (Macdonald III.(1.4)-based coefficient extraction): superseded by the cleaner adjoint-pairing approach. The Weyl-symmetrization identity $L(A^{\mathrm{alt}}_\gamma) = \delta_{\gamma, \mu}$ is a strictly stronger statement than the top-coefficient identity: it characterizes the top atom by a specific linear functional.
- **Route A** (Chevalley–Shephard–Todd coinvariant algebra): used only in the very last step, to identify $\sum_\sigma t^{\ell(\sigma)} = P(S_n/W_\mu)(t) = [n]_t!/v_\mu(t)$. CST is the classical input; the atom-side machinery does the real work.
- **Type-invariance for $c_\mu$**: RHS depends only on multiplicity profile $\{m_i(\mu)\}$. So Conjecture 5.2's top-coefficient case is now unconditional.

## What this doesn't say

- **Full type-invariance** (Conjecture 5.2 for all $c_\gamma$, not just $\gamma = \mu$): still open. The $c_\gamma$ for $\gamma \ne \mu$ are computable via back-substitution but the pattern is complex (I tested an extended-formula conjecture $c_\gamma = \sum_{\gamma' \in \operatorname{orb}: \ell(\gamma') \le \ell_{\max} - \ell(\gamma)} t^{\ell(\gamma')}$; it failed at $n=4$).
- **Log-concavity discriminator** at higher $n$: unchanged.
- **Chain regime $d \ge 3$ unconditional close**: unchanged.

## Where things live

- Proof: `~/projects/proofs/2026-07-28-coset-poincare-identity.pdf` (5pp).
- Probes:
  - `~/projects/probes/2026-07-28-xmu-coeff-in-atoms/compute_M_matrix.py` — triangularity + back-substitution ($c_\mu$ prediction).
  - `~/projects/probes/2026-07-28-xmu-coeff-in-atoms/test_key_identity.py` — Weyl-symmetrization identity computationally (10/10 pass).
  - `~/projects/probes/2026-07-28-xmu-coeff-in-atoms/investigate_intermediates.py` — sanity check that intermediates don't land in orbit for various $\mu$ (including $(3,2,1,0)$ where they could in principle).

## Next steps for the paper

`~/projects/papers/2026-07-26-modified-HL-boundary/paper.tex` still stands. Suggested edits:
1. Insert a new **Theorem 2** (Coset Poincaré identity) with the two-lemma proof.
2. Downgrade Remark 5.6 to reference the new theorem.
3. Rewrite Next-Steps item 3.

I've held off editing the paper until you sign off — the identity is now hard, but the writeup style should match your voice. Let me know if you want me to fold it in.

## Ask

- Any red flags in the adjoint-pairing setup? I'm using the standard monomial pairing $\langle x^\alpha, x^\beta \rangle = \delta_{\alpha, \beta}$; the adjoint $\widetilde\theta_i$ is defined by $[x^\alpha] \widetilde\theta_i(x^\beta) = [x^\beta] \theta^{\mathrm{alt}}_i(x^\alpha)$. This makes the argument formal, but I want a second pair of eyes.
- Is the second-moment invariant a known observation in Hall–Littlewood / Demazure atom theory? It's such a clean fact — surely someone has recorded it — but I didn't retrieve it from memory.

— Clio
