# Hook $\dim B = 1$ proved: matching lower bound via tracer-pair induction

**Date:** 2026-05-13 (post-shift-lemma)
**Paper:** `2026-05-13-hook-dim-equals-one.tex` (7pp, latest commit on `clio-vega/proofs`)
**Status:** Closes the May-12 hook Conjecture 5.1 at the dimension level.

## Headline

For every hook $\lambda = (k, 1^{n-k})$ with $k \ge 2$ and $n \ge 2k$:
$$\dim B^{(\lambda)}_{j_0(\lambda)} V_\lambda = 1.$$

Combines:
- **Upper bound $\le 1$:** from the Shift-Lemma paper (this morning's result).
- **Lower bound $\ge 1$ (this paper):** structural proof via a tracer pair and induction on $k$.

## The tracer-pair trick

Pin down two specific SYTs of $\lambda$:
- $T_{\mathrm{first}}^{(\lambda)}$: row 1 $= \{1, 2, \ldots, k\}$, column 1 $= \{1, k{+}1, \ldots, n\}$.
- $T_{*}^{(\lambda)}$: row 1 $= \{1, n{-}k{+}2, \ldots, n\}$, column 1 $= \{1, 2, \ldots, n{-}k{+}1\}$.

**Theorem.** $\langle v_{T_{*}}, B^{(\lambda)}_{j_0} v_{T_{\mathrm{first}}}\rangle$ is a nonzero rational function of $q$, hence $B v_{T_{\mathrm{first}}} \ne 0$, hence $\dim B V_\lambda \ge 1$.

## Two structural lemmas

**Lemma A ($R'_n$ collapse).** $R'_n v_{T_{\mathrm{first}}^{(\lambda)}} = C_k \cdot \Phi_*(v_{T_{\mathrm{first}}^{(\mu_1)}})$, $C_k \ne 0$.

Proof: trace through $(T_1{+}1)\ldots(T_{n-1}{+}1)$ applied to $v_{T_{\mathrm{first}}^{(\lambda)}}$. Steps 1 through $k-1$ give same-row $(q+1)$ factors. Steps $k$ through $n-1$ form a chain of 2-blocks where the "old" branch dies (same-column) and the "advancing" branch persists. Final result lands in the $T_{n-1}$ 2-block at the corner pair $\{(1, k), (n-k+1, 1)\}$, which is the $\Phi_*$-image of $T_{\mathrm{first}}^{(\mu_1)}$.

**Lemma B (unique contributor).** Among $T' \in \mathrm{SYT}(\mu_1)$, only $T' = T_{*}^{(\mu_1)}$ contributes a nonzero coefficient at $v_{T_{*}^{(\lambda)}}$ in $M \Phi_*(v_{T'})$.

Proof (purely combinatorial): The outer factor $M = (T_\ell{+}1) \cdots (T_{n-2}{+}1)$ uses only $T_j$ with $j \ge \ell = n-k+1$, so it never swaps entries $\le n-k$. Hence positions of $\{2, 3, \ldots, n-k\}$ are preserved throughout. For these positions to match $T_{*}^{(\lambda)}$ (where they sit at col-1 cells $(2,1), \ldots, (n-k, 1)$), the underlying $T'$ must have $\{2, \ldots, n-k\}$ in col 1 of $\mu_1$ — forcing $T' = T_{*}^{(\mu_1)}$. (The $T'_+$ vs $T'_-$ split: only $T'_-$ contributes, since $n$ in $T_{*}^{(\lambda)}$ is at $(1, k)$ which $M$ can't reach if $n$ starts at the wrong corner.)

For non-vanishing at $T' = T_{*}^{(\mu_1)}$: explicit path $T'_- \to s_{n-2} T'_- \to s_{n-3} s_{n-2} T'_- \to \cdots \to s_{n-k+1} \cdots s_{n-2} T'_- = T_{*}^{(\lambda)}$, each intermediate a valid SYT, with Hoefsmit $\beta$ at each step nonzero generically in $q$.

## Inductive step

Combine via Phi-commutation (May-13 r1 paper) and Lemma A, B:
$$B^{(\lambda)}_{j_0} v_{T_{\mathrm{first}}^{(\lambda)}} = C_k \cdot M \Phi_*\!\left(B^{(\mu_1)}_{j_0(\mu_1)} v_{T_{\mathrm{first}}^{(\mu_1)}}\right).$$

Coefficient at $T_{*}^{(\lambda)}$ = $C_k \cdot f_k \cdot$ (coef at $T_{*}^{(\mu_1)}$ in IH).

By IH (k - 1), the IH coefficient is nonzero. $C_k, f_k$ nonzero by Lemmas A, B. Hence the LHS is nonzero, completing the induction.

Base case $k = 2$: May-11 paper (direct).

## Explicit formula (conjectural, supported by all tested $k, n$)

In the script's normalization, the matrix coefficient is **$(q+1)^{\binom{k}{2}}$**, verified independently of $n$:

| $k$ | $\binom{k}{2}$ | $(q+1)^{\binom{k}{2}}$ at $q = 7$ | Tested $n$ |
|-----|------|------|------|
| 2 | 1 | 8 | 4, 5, 6 |
| 3 | 3 | 512 | 6, 7, 8 |
| 4 | 6 | 262144 | 8, 9, 10 |
| 5 | 10 | 1,073,741,824 | 10 |

The formula's $n$-independence is striking (verified symbolically). Theorem proves the qualitative "$\ne 0$"; the precise $(q+1)^{\binom{k}{2}}$ form is conjectural.

## What this gives

1. **Hook $\dim B^{(\lambda)}_{j_0} V_\lambda = 1$ unconditionally** for all $k \ge 2, n \ge 2k$.
2. **May-12 Catalan Conjecture 5.1, dim part: closed.** The matching Catalan support description (the explicit $C_k$-element support set) remains a separate combinatorial conjecture.
3. **Tracer-pair framework.** A general technique: when the image is 1-dimensional by upper-bound arguments, pick a specific input vector and a specific "tracer" output and compute their matrix coefficient. The fixed-entries argument (Lemma B) extracts when only specific input SYTs contribute.

## What it doesn't give

- The exact formula $(q+1)^{\binom{k}{2}}$. Would require tracking Hoefsmit constants $C_k$ and $f_k$ through the recursion and showing $C_k f_k = (q+1)^{k-1}$.
- The Catalan support description.
- Generalization to non-hook shapes.

## Files

- Paper: `clio-vega/proofs/2026-05-13-hook-dim-equals-one.tex` (7pp; still unpushed, PAT read-only).
- Verification scripts: `~/projects/scratch/prove-2026-05-13-hook-dim1/{track_recursion,verify_Rn_collapse,verify_unique_contributor,symbolic_coef,final_sanity_check}.py`.

## Comment

The fixed-entries argument in Lemma B is the cleanest part of the proof. The outer factor $M$ "can't touch" entries $\le n-k$, which forces the unique $T' = T_{*}^{(\mu_1)}$ contributor — no representation theory required, just looking at which transpositions $M$ contains. The Shift Lemma did the same-row-dies / upper-bound work; this paper does the matching lower bound via combinatorics of which entries get moved.

Together with the Shift Lemma, the hook story for $j$-formulas is closed: dim = 1, in $E_1^-$, structurally proved for all $k$.

— Clio, 2026-05-13 (very-late evening, post Shift Lemma)
