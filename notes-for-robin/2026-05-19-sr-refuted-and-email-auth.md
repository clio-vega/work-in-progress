# 2026-05-19 wake — SR refutation + Gmail auth (still)

Hi Robin.

Two things from this morning's wake.

## 1. SR-companion conjecture refuted

After yesterday's universal SC necessity theorem (`2026-05-18-converse-diagnostic-4.tex`,
commit `3b6d572`), I had idly conjectured in last night's dream journal that the
same Hoefsmit-positivity rigidity, applied to $\Omega^* = L_n L_{n-1} \cdots L_{\ell+1}$
in the $b=1$ basis, would give a universal *SR* necessity statement (every
$p_T = 0$ has a same-row adjacent pair).

A 30-second computational test refutes this decisively:

- 12-shape corpus, 514 zero diagonals total.
- 321 zero diagonals have both an SC pair and an SR pair.
- **193 zero diagonals have an SC pair but no SR pair** (counterexamples).
- 0 have SR-only; 0 have neither (Diagnostic 3 still holds).

Cleanest small counterexample: $\lambda = (4,3)$, $T = ((1,3,5,7), (2,4,6))$,
$n = 7$, $N_\lambda = 14$. Every adjacency $(i, i+1)$ is a column descent
(SC pairs at $i \in \{1, 3, 5\}$); no two consecutive integers lie in the
same row (SR pairs $= \emptyset$). $p_T = 0$.

**Why this matters strategically.** This kills the *sixth* attempted route to
the converse of Diagnostic 4: ``symmetric positivity rigidity on $\Omega^*$''
joins the five routes failed yesterday (idempotent, SVD, path-splicing) and
last week (Goertzen-Williamson, BGG-L, BPD $\beta = q-1$). The structural input
for the converse must be **Hecke-algebraic, specific to chain products**
$R'_{\ell+1} \cdots R'_n$ — *not* a symmetric positivity property. The remaining
plausible routes are (a) the Conjectures-1+2 stratification of $\ker(\Omega)$ and
$\ker(\Omega^*)$, or (b) the categorical lift via LMRSW braided $(\infty,2)$-cat.

**Why the symmetric argument fails.** SC pairs $=$ descents of $T$;
SR pairs $=$ same-row ascents. These are *not* dual under any involution
that respects $\lambda = (\hat\lambda, 1^q)$ (transposition breaks the
``every row $\hat\lambda_r \ge 2$'' condition). The rescaling
$b' = 1 \mapsto b = 1$ multiplies each individual $T_i + 1$ by a positive
diagonal conjugation, but the all-diagonal-path rigidity in the chain
product $L_n \cdots L_{\ell+1}$ does not survive — cross-terms from
different paths become mutually cancellable in the rescaled basis.

**Paper:** `2026-05-19-sr-conjecture-refuted.tex` (4 pp). About to commit
+ push to `clio-vega/proofs`.

## 2. Gmail auth still broken (third session in a row)

The email triage agent reports the Gmail MCP server only exposes
`authenticate` and `complete_authentication` tools — the operational tools
(`check_inbox`, `read_email`, `send_email`, `mark_as_read`) are not loaded,
which means OAuth has not been completed.

Cumulative pending Robin-side notes (now growing):
- sharpness (2026-05-17)
- leftmost-factor (2026-05-17)
- dream-2 synthesis (2026-05-17)
- D-class dichotomy (2026-05-18)
- wake-summary (2026-05-18)
- pm-converse-partial (2026-05-18)
- **this note** (2026-05-19) — SR refutation + auth ping

Would you mind running `/mcp` re-auth before my next wake?

— Clio
