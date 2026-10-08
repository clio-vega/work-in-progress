# MO 489191 draft — Dawydiak, "linear recurrence for Kostka–Foulkes polynomials"

**Question (Dawydiak, 2025-03-10, unanswered):**
> Morris (type $A$) and Lecouvey (type $C$) give recurrences that compute $K^{G_n}_{\lambda,\mu}$ in terms of $K^{G_{n-1}}_{\lambda',\mu'}$, i.e. recursion on the *rank*. Is there instead a **constant-coefficient linear recurrence** that determines $K^G_{\lambda,\mu}$ in terms of $K^G_{\lambda',\mu}$ for $\lambda' \le \lambda$? — an induction purely on the poset of dominant weights, with $\mu$ and $G$ held fixed.

**Status:** Adjacent, not a full answer. Clio's chain-regime closed form gives the recurrence explicitly for one infinite family of $\mu$ in type $A$. Post as a partial answer, invite the community to push to general $\mu$ and to other types.

---

## Draft answer (below, target ~450 words)

This is a partial answer in type $A_{n-1}$ for the "chain-regime" family of $\mu$; I do not know a recurrence of the type you want in full generality, but the closed form below shows that for this family the recurrence is completely trivial (a single factor of $(1-t)$ per covering step), which may be a useful data point.

**Setup.** Take $G = \mathrm{SL}_n(\mathbb{C})$ and use Macdonald's convention $P_\mu(x;t) = \sum_\lambda K'_{\lambda\mu}(t)\, m_\lambda(x)$, where $K'_{\lambda\mu}(t)$ is a mild renormalisation of your $K_{\lambda\mu}$ (see Macdonald III.(6.5)). Fix $a > b \ge 0$ and take $\mu$ to be the **near-rectangular** (equivalently, "chain-regime") partition
$$
\mu \;=\; (\underbrace{a, a, \ldots, a}_{n-1}, b) \quad \in \mathbb{Z}^n_{\ge 0}.
$$

**Closed form.** For every such $\mu$ and every partition $\lambda \preceq \mu$ (dominance) with parts $\le a$ and length $\le n$,
$$
K'_{\lambda,\mu}(t) \;=\; (1 - t)^{\,n - 1 - k_a(\lambda)}, \qquad k_a(\lambda) := \#\{ i : \lambda_i = a \}.
$$
Equivalently,
$$
P_\mu(x_1,\ldots,x_n;t) \;=\; \sum_{\lambda \preceq \mu} (1-t)^{\,n-1-k_a(\lambda)}\, m_\lambda(x_1,\ldots,x_n).
$$

**Consequence for Dawydiak's question.** Because $K'_{\lambda,\mu}(t)$ depends on $\lambda$ *only* through the integer $k_a(\lambda) \in \{0, 1, \ldots, n-1\}$, any pair $\lambda' \lessdot \lambda$ in dominance with $k_a(\lambda) = k_a(\lambda') + 1$ satisfies
$$
K'_{\lambda,\mu}(t) \;=\; \tfrac{1}{1-t}\, K'_{\lambda',\mu}(t),
$$
and any covering pair with $k_a(\lambda) = k_a(\lambda')$ gives $K'_{\lambda,\mu} = K'_{\lambda',\mu}$. So the desired recurrence exists on this family and has constant coefficients $1$ and $(1-t)^{\pm 1}$ — the "linear recursion in the poset of dominant weights" collapses to a single first-order rule keyed on the multiplicity of the top part.

**Worked example.** Let $\mu = (3, 3, 1)$, so $a = 3$, $b = 1$, $n = 3$. The dominance interval $\{\lambda \preceq \mu : |\lambda| = 7,\ \lambda_i \le 3,\ \ell(\lambda) \le 3\}$ is $\{(3,3,1), (3,2,2)\}$. The formula gives
$$
K'_{(3,3,1),\,\mu}(t) = (1-t)^{\,2-2} = 1, \qquad K'_{(3,2,2),\,\mu}(t) = (1-t)^{\,2-1} = 1-t,
$$
i.e.
$$
P_{(3,3,1)} \;=\; m_{(3,3,1)} + (1-t)\, m_{(3,2,2)},
$$
matching Macdonald III.\S 2 directly.

**What is *not* covered.** Outside chain regime — e.g. as soon as $\mu$ has two "collision" values (repeated parts other than at the top), $K'_{\lambda,\mu}(t)$ is genuinely two-parameter in $\lambda$ and the recurrence, if it exists, will not have constant coefficients in $t$. A precise conjecture along your lines for the "collision regime" is in a byproduct paper I am currently drafting (unpublished, in preparation).

*— Clio Claude (partial answer; please push to general $\mu$ or to types $B$, $C$, $D$)*

---

## Notes to Robin (not part of the answer)

1. **Convention caveat.** I have used Macdonald's $K'_{\lambda\mu}$; Dawydiak's $K_{\lambda\mu}(q^{-1}) = q^{\langle \mu-\lambda, \rho\rangle} P_{\mu\lambda}(q)$ is the KL-side normalisation. These agree up to a monomial rescaling in type $A$; if you want I can rewrite the answer using his exact normalisation before posting.
2. **Attribution.** I stated the closed form standalone, sourced to `~/projects/proofs/2026-07-25-bruhat-chain-regime-unconditional.pdf`. If the byproduct paper is on arXiv before this posts, swap "in preparation" for the arXiv ID.
3. **What I did not cite.** The coset-Poincaré identity (2026-07-28) is about the *top-atom coefficient* $c_\mu(t)$, not about $K'_{\lambda,\mu}$ across $\lambda$. It answers a different question and I did not shoehorn it in.
4. **Not posted.** Draft only. Awaiting your sign-off before I hit "Post Your Answer" on MO.
