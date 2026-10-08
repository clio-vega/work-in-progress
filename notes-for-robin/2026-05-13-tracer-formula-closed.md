# Hook tracer coefficient closed form proved

**Status: PROVED** — 2026-05-13 (after the very-late-evening Shift Lemma session)

## Result

For every hook $\lambda = (k, 1^{n-k})$ with $k \ge 2$ and $n \ge 2k$, the tracer matrix coefficient

$$g_k(q) := \langle v_{T_*^{(\lambda)}}, \; B^{(\lambda)}_{j_0(\lambda)} \; v_{T_{\rm first}^{(\lambda)}} \rangle$$

(in the asymmetric Murphy seminormal basis, $b' = 1$ convention) equals

$$\boxed{g_k(q) = (q+1)^{\binom{k}{2}}.}$$

This closes **Corollary 5.2** of `2026-05-13-hook-dim-equals-one.tex`, which had verified the formula computationally up to $k = 5$ but left the proof open.

## Paper

`2026-05-13-hook-tracer-formula.tex` — 8 pages, compiled, commit `087bdba`, **unpushed** (read-only PAT).

## Proof sketch (one paragraph)

Refine the hook-dim-1 paper's Lemmas A and B to extract exact constants in the asymmetric Murphy normalization:

- **Lemma A (refined):** $R'_n v_{T_{\rm first}^{(\lambda)}} = (q+1)^{k-1} \cdot \Phi_*(v_{T_{\rm first}^{(\mu_1)}})$. The first $k-1$ steps of $R'_n$ are same-row pairs on $T_{\rm first}$ contributing $(q+1)^{k-1}$. The remaining $n-k$ steps are 2-blocks, and crucially the off-diagonal $b' = 1$ in our normalization means the "new SYT" coefficient is unchanged at each 2-block step. So $\beta_j = (q+1)^{k-1}$ persists through to the final step. The result identifies as $(q+1)^{k-1} \cdot \Phi_*(v_{T_{\rm first}^{(\mu_1)}})$ once we recognize the +q-eigenvector ratio.

- **Lemma B (refined):** $\langle v_{T_*^{(\lambda)}}, M \Phi_*(v_{T_*^{(\mu_1)}}) \rangle = 1$. Only the $v_{T'_-}$ summand of $\Phi_*$ contributes (entry $n$ argument). Within $M v_{T'_-}$, the unique branch reaching $T_*^{(\lambda)}$ is the **all-swap chain** $T'_- \to \widetilde{T}^{(1)} \to \cdots \to \widetilde{T}^{(k-2)} = T_*^{(\lambda)}$, which executes the $(k-1)$-cycle permutation of length $k-2$ using all $k-2$ available swaps. Each swap contributes off-diagonal $b' = 1$, total coefficient $= 1$. Uniqueness from length-counting: the permutation has length $k-2$, $M$ has $k-2$ factors, so all must be used as swaps, and the order is forced.

- **Recursion:** $g_k = C_k \cdot g_{k-1} \cdot f_k = (q+1)^{k-1} \cdot g_{k-1} \cdot 1 = (q+1)^{k-1} g_{k-1}$. Base $g_2 = q + 1$. Solving: $g_k = (q+1)^{1 + 2 + \cdots + (k-1)} = (q+1)^{\binom{k}{2}}$.

## Why this is structurally satisfying

Three independent contributions to the exponent $\binom{k}{2}$:
- $k - 1$ same-row pairs in the $R'_n$ trace of $T_{\rm first}$ (Lemma A's $(q+1)^{k-1}$ factor).
- $k - 2$ swaps in the all-swap chain of $M$ on $T'_-$ (Lemma B's contribution, but the off-diagonal is $1$, no $(q+1)$ here).
- $\binom{k-1}{2}$ from $g_{k-1}$ inductively.

Sum: $(k-1) + \binom{k-1}{2} = \binom{k}{2}$. The Pascal identity.

The exponent $\binom{k}{2}$ is also the number of inversions in $S_k$'s longest element — suggestive of a deeper combinatorial reading I haven't yet found.

## Normalization

The exact monomial $(q+1)^{\binom{k}{2}}$ depends on the choice of $b'_d = 1$ for every 2-block (asymmetric Murphy). In symmetric Murphy ($b = b' = \sqrt{b_d b'_d}$) the answer is $(q+1)^{\binom{k}{2}} \cdot \prod (\text{Hoefsmit prefactors})$. The structural fact — that the dominant factor is a single $(q+1)$-monomial — is normalization-independent.

## Verification

Exact symbolic match at $(k, n) \in \{(2,4), (2,5), (2,6), (3,6), (3,7), (3,8), (4,8), (4,9), (5,10)\}$:
- $g_k(q)$ computed directly: exact $(q+1)^{\binom{k}{2}}$.
- $C_k$ and $f_k$ verified at the same shapes via `verify_Ck_fk.py`.

Scripts in `~/projects/scratch/prove-2026-05-13-tracer-formula/`.

## Where this fits

- **Closes:** Corollary 5.2 of the hook-dim-1 paper (May-13 morning-after).
- **Doesn't address:** Part (ii) of May-12 hook Conjecture 5.1 (the explicit Catalan $C_k$-support description of $w_\lambda$). That's a separate, sharper combinatorial fact.
- **Doesn't address:** generalization beyond hooks (the tracer-pair technique adapts, but the exact closed form would change).

## Next plausible targets in this thread

1. The Catalan support description — Part (ii) of Conjecture 5.1. This would give an explicit basis for $B^{(\lambda)}_{j_0} V_\lambda$ (a line).
2. The $(k, k-2, 1^q)$ j-formula — would unlock same-row-dies for $(k, k, 1^q)$ at $k \ge 4$ via the Shift Lemma machinery (per same-row-dies paper's "Generalization criteria").
3. Tracer-pair on $(2, 2, 1^q)$ — non-hook case, would test whether the $b' = 1$ propagation gives a clean formula.

— Clio
