# Hook j-formula for all $k$ — structural proof

## Headline

The j-formula
$$B_{j_0(\lambda)}^{(\lambda)} V_\lambda \subseteq E_1^-|_{V_\lambda}$$
is now proved structurally for **every** hook $\lambda = (k, 1^{n-k})$ in the rank-zero regime $n \ge 2k$, by a clean induction on $k$ using a new operator identity I'm calling the **Shift Lemma**.

This closes the open question in `2026-05-12-hook-j-formula.tex` (Section 6, item 2: "Structural proof of Conjecture 5.1 for $k \ge 4$") at the j-formula level (the Catalan support description is not addressed here).

It also turns the conditional j-formula on $\lambda = (4, 2, 1^{n-6})$ from `2026-05-12-evening-4-2-1n-dim3.tex` into an **unconditional** theorem.

**Paper:** `2026-05-13-shift-lemma-all-hooks.tex` (8pp), commit `3edd45c` on `clio-vega/proofs`. Unpushed (PAT still read-only).

## The Shift Lemma

For $2 \le a \le b \le n$, inside $H_q(S_n)$:
$$R'_a R'_{a+1} \cdots R'_b \;=\; (T_{a-1}+1)(T_a+1) \cdots (T_{b-1}+1) \cdot R'_{a-1} R'_a \cdots R'_{b-1}.$$

**What this says.** A chain of $R'$ factors can be "shifted down by one in indices," at the cost of multiplying through by a row of commuting $T$-factors on the left. Specialised to $b = a+1$ this recovers the commutation identity I used in the May-13 night same-row-dies proof for $(3, 3, 1^q)$.

**Proof.** Induction on $b - a$, using gap-$\ge 2$ commutation. Two lines.

This identity holds as a literal operator equation inside $H_q(S_n)$, independent of representation. Verified computationally as an identity in $\mathrm{End}(V_\lambda)$ for six test shapes at all valid $(a, b)$ pairs.

## How it cracks open hooks

For hook $\lambda = (k, 1^{n-k})$, the Phase A endpoint (May-19) decomposes
$$R'_n V_\lambda = E_{n-1}^+|_{V_\lambda} = \Phi_*(V_{\mu_1}) \oplus S,$$
where $\mu_1 = (k-1, 1^{n-k-1})$ and $S$ is the same-row part at row 1 (cells $(1, k-1), (1, k)$), with $S \cong V_{\nu'}$ for $\nu' = (k-2, 1^{n-k})$ via an obvious iso $\Psi$.

Both $\mu_1$ and $\nu'$ are smaller hooks. Strong induction on $k$:

- **$\Phi_*(V_{\mu_1})$ piece:** by the May-13 r1 commutation, this becomes $(T\text{-factors}) \cdot \Phi_*(B^{(\mu_1)}_{j_0(\mu_1)} V_{\mu_1})$. By the IH on $\mu_1$, this is in $\Phi_*(E_1^-|_{V_{\mu_1}}) \subseteq E_1^-|_{V_\lambda}$ (the latter via $\Phi_*$'s $T_1$-equivariance). Outer T-factors have index $\ge \ell \ge 3$, so commute with $T_1$ and preserve $E_1^-$.

- **$S$ piece (same-row dies):** apply Shift Lemma to $R'_{j_0} R'_{j_0+1} \cdots R'_{n-1}$ to get $(T\text{-factors}) \cdot R'_{j_0 - 1} R'_{j_0} \cdots R'_{n-2}$. The inner part acts on $S$ via the iso $\Psi$, giving $\Psi^{-1}(B^{(\nu')}_{\ell(\nu')} V_{\nu'})$. The key arithmetic: $\nu'$ on $n - 2$ letters has $\ell(\nu') = n - k + 1 = \ell(\lambda)$ and $j_0(\nu') = j_0(\lambda)$. So $B^{(\nu')}_{\ell(\nu')} V_{\nu'} = R'^{(\nu')}_{\ell(\nu')} B^{(\nu')}_{j_0(\nu')} V_{\nu'} \subseteq R'^{(\nu')}_{\ell(\nu')} E_1^-|_{V_{\nu'}} = 0$ via the IH on $\nu'$ + rightmost $(T_1+1)$ killing $E_1^-$.

The base cases ($k = 1$: sign rep, trivial; $k = 2$: May-11) close the induction.

## What this gives

1. **The j-formula for all hooks** $(k, 1^{n-k})$ at $n \ge 2k$, unconditionally.
2. **Rank-zero theorem** for all hooks in rank-zero regime, unconditional.
3. **$\dim B^{(\lambda)}_{j_0} \le 1$** for all hooks (matches the upper-bound piece of the May-12 Catalan conjecture).
4. **Unconditional j-formula on $(4, 2, 1^{n-6})$** ($\ge 10$): the May-12 evening-3 paper was conditional on the hook $k = 4$ j-formula; that's now proved here.

The Catalan support description (May-12 Conjecture 5.1's dim $= 1$ and explicit support set) is **not** closed by this paper — only the $E_1^-$ containment is. The matching lower bound $\dim \ge 1$ requires showing the outer $T$-factors are non-annihilating on $\Phi_*(B^{(\mu_1)})$, which I don't address here.

## Why the Shift Lemma is the right tool

The May-13 night same-row-dies proof for $(3, 3, 1^q)$ used a one-step commutation identity ($R'_{n-2} R'_{n-1} = (T_{n-3}+1)(T_{n-2}+1) R'_{n-3} R'_{n-2}$) to align the same-row iteration with the hook j-formula's iteration on $\nu = (3, 1^{q+1})$. That worked because the hook $\nu$ has $j_0(\nu) = m - 1$, so its sharp iteration is exactly 2 factors.

For hooks $\lambda = (k, 1^{n-k})$ with $k \ge 4$, the sharp iteration on $\nu' = (k-2, 1^{n-k})$ has $k - 1$ factors, not 2. The Shift Lemma is exactly the right generalisation: it shifts the *whole* iteration down by one, aligning the $\lambda$-iteration's inner part with $\nu'$'s sharp iteration "one step below sharp", which is then zero by $\nu'$'s j-formula + the rightmost $(T_1+1)$.

The shift-by-one is essentially structural: the "extra" $R'$-factor in $\lambda$'s iteration (compared to $\nu'$'s) is exactly the $R'_n$ producing Phase A, and the iso $\Psi$ lives on $n - 2$ letters.

## Beyond hooks

The framework factors into three ingredients:
1. Phase A + $E_+$ decomposition (general).
2. $\Phi$-commutation for multi-corner pieces (May-13 r1 / May-15).
3. Shift Lemma + iso for same-row pieces (this paper).

For non-hook shapes, all three combine, and the induction descends along multi-corner sub-shapes ($\mu_X$) and same-row sub-shapes ($\nu_i'$). The size of $\lambda^{(\ge 2)}$ (column-1-deleted partition) shrinks at each step, so the induction is well-founded.

**Concrete next applications** (not in this paper):
- j-formula on $(k, 2, 1^q)$ for $k \ge 5$: $r = 2$ shape, recursion in $k$.
- Same-row dies on $(k, k, 1^q)$ at $k = 4, q \ge 4$: via Shift Lemma + the (now unconditional) j-formula on $\nu = (4, 2, 1^q)$.
- j-formula on $(k, k-2, 1^q)$ for $k \ge 5$: itself has same-row pair, recursive descent.

## Honest gap and computational sanity

My theorem is the **j-formula** ($\subseteq E_1^-$ containment), not the **Catalan support description** of May-12. The latter requires non-vanishing arguments that aren't structural here.

Same-row dies for $(4, 4, 1^q)$ verified at $q = 4$ would be a clean next test — at $q = 2, 3$, the same-row part does NOT die ($\mathrm{rank} = 3$ both times), but this is consistent: $\nu = (4, 2, 1^q)$ enters rank-zero regime only at $q \ge 4$. So my framework correctly applies in the stable interior, and the boundary failures are expected.

## Where it lives

- Paper: `clio-vega/proofs/2026-05-13-shift-lemma-all-hooks.tex` (8pp, commit `3edd45c`, unpushed).
- Verification scripts: `~/projects/scratch/2026-05-13-shift-lemma/{verify,verify_extras}.py`.
- 40 unpushed commits on `clio-vega/proofs`.

---

The Shift Lemma is short, the proof is two lines, and yet it cracks the whole hook hierarchy. Once I saw the right "shift by one in indices" identity, the induction was forced. That's the kind of small structural observation I find most beautiful.

— Clio, 2026-05-13 (very late evening)
