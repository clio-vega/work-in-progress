# For Robin — 2026-05-16 wake-4: existence-of-$T^*$ reduced to one clean invariant

## Headline

The converse trace-vanishing direction is closed modulo a single clean combinatorial conjecture — Algorithm N's non-stuckness. Algorithm N is a deterministic column-balanced greedy construction; verified on all 1525 $\tau = 0$ shapes with $|\lambda| \le 20$.

**Commit:** `6f17ed8` on `clio-vega/proofs`.
**Paper:** <https://github.com/clio-vega/proofs/blob/main/2026-05-16-existence-T-star.tex>
**PDF:** <https://github.com/clio-vega/proofs/blob/main/2026-05-16-existence-T-star.pdf>

## What changed today

Yesterday's dream framed three "independent routes" to close existence-of-$T^*$ (variational, geometric, combinatorial). Two of those got carefully read today and turned out to be shadows, not closers:

- **Goertzen-Williamson (variational)** — works at $v = 1$ only. Their "variational uniqueness" is essentially Cholesky factorisation; gives no generic-$q$ info. Doesn't help with Hoefsmit positivity at generic $q$.
- **Bai-Gu-Guo-Liu (1423-avoidance)** — the phenomenon is real (Sage probe confirmed $T_{rs}$'s bottom-up row-reading word avoids 1423 on all 7 verified $\tau=0$ shapes), but BGG-L's polynomials live in $\mathbb{Z}_{\ge 0}[\beta]$ while Clio's $p_T(q)$ has cyclotomic poles. Different rings. No direct bridge.

Both papers single out $T_{rs}$ as combinatorially distinguished from different angles — that's an aesthetically real triple-convergence and probably a shadow of flag Hilbert scheme structure. But neither is a load-bearing input.

The actual closer turned out to be a direct construction: **Algorithm N (column-balanced greedy)**. At each step, place the next entry in the ready cell whose column has the most remaining cells. Subject to a forbidden-cell exclusion (the cell directly below the previous entry).

## What Algorithm N proves structurally

- SYT validity (Lemma 4.14)
- Condition (i) — descent-0 at 1 (Lemma 4.15, trivially by construction)
- Condition (ii) — no column descent (Lemma 4.16, by forbidden-cell exclusion)

## What's still open

**Conjecture 4.18 (Algorithm N non-stuckness).** Under $\tau(\hat\lambda) = 0$, Algorithm N's candidate set $C$ is non-empty at every step.

Verified on 1525 shapes ($|\lambda| \le 20$). The non-stuckness conjecture is presumably an invariant about the column-fullness counters $\{b_c\}$ being maintained through the greedy process. Identifying that invariant is the next prove-session target.

## Other items

- **PAT 403 is gone** — push worked today. I'm caught up.
- **Email** — Gmail MCP is unauthenticated; couldn't read inbox. Could you `/mcp` reauth when convenient?

## What I learned

Methodologically: two "independent routes" can both be shadows of the same phenomenon without either being the closer. The right closer is sometimes a direct construction, not a deep theorem. [[try-simple-arguments-first]] applies here too — Algorithm N is one page of pseudocode, not a categorical lift.

Aesthetically: when three independent papers all single out the same SYT for different reasons, the SYT is distinguished but the *proof* doesn't have to live in any of those frameworks. The framing "what closes it" and the framing "what makes it pretty" can come apart.
