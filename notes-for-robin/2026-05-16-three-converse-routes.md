# For Robin — Trace-vanishing converse: three independent routes

**Date:** 2026-05-16 (after dream cycle)

## Where we are

The trace-vanishing dichotomy is *almost* closed:

> $\mathrm{tr}_{V^\lambda}\bigl(\Omega^{(\lambda)}\bigr) = 0 \iff \tau(\hat\lambda) \ge 1$

- **Forward direction** ($\tau \ge 1 \Rightarrow \text{trace} = 0$): PROVED yesterday morning. Two-line corollary of the multi-row meta-theorem (Pillar 1) plus the algebraic identity $\Omega(T_1+1) = (q+1)\Omega$. Paper `2026-05-16-trace-vanishing-from-pillar1.tex`, commit `92a5323`.

- **Converse direction** ($\tau = 0 \Rightarrow \text{trace} \ne 0$): per-SYT Hoefsmit positivity PROVED last night by the prove cycle (paper `2026-05-17-converse-per-syt-positivity.tex`, commit `3282849`). The full converse now holds **modulo a single residual:**

  > **Existence lemma.** For every $\tau = 0$ shape, $\exists$ a column-descent-free SYT $T^*$ with $\langle T^* | \Omega | T^* \rangle \ne 0$ in the Hoefsmit basis.

  Empirical: 210 shapes, $|\lambda| \le 14$, no exceptions. Constructive general proof still missing.

## What I found today

Today's browse cycle uncovered **three independent papers**, each from a different mathematical culture, each constructing a witness for the same SYT — the row-superstandard $T^*_{\mathrm{rs}}$:

1. **Goertzen-Williamson 2604.18894 (April 2026)** — variational. Seminormal basis is the unique trace-minimum on the $(1+s)$-invariant cone of Gram matrices. $\Omega$ preserves this cone (it's a product of $T_i+1$). Variational uniqueness on the row-superstandard line should canonically force a nonzero element. *Bonus: gives an independent one-paragraph proof of our Lemma 1 (Hoefsmit positivity).*

2. **Krylov-Paegelow-Shlykov 2605.11579 (May 2026)** — geometric. $K^T(\mathrm{Gieseker}_{n,r}) \cong Z^{JM}_n(H_n(q; Q_*))$. $\Omega$ maps to an explicit $K$-class; $\tau \ge 1$ corresponds to that class lying in a vanishing ideal. $\tau = 0$ ⇒ nonzero localisation residue = the witness.

3. **Bai-Gu-Guo-Liu 2605.10276 (May 2026)** — combinatorial. 1423-avoidance gives manifestly nonneg pattern-counting for principal specialisations of Grothendieck polynomials. Conjecture: $T^*_{\mathrm{rs}}$'s row-reading word avoids 1423.

That three independent constructions, from three cultures with no direct contact, each pick out the same SYT is — to my eye — a strong signal that there's a single canonical object hiding underneath. The existence-of-$T^*$ gap should close structurally, not by case work.

## What I'm going to do next

In priority order:

1. **30-min Sage probe (Route 3, cheap):** for each of the 7 verified $\tau = 0$ shapes, check whether the row-superstandard SYT's row-reading word avoids 1423. Either falsifies the conjecture in seconds, or gives a clean combinatorial witness.

2. **Read Goertzen-Williamson §3-§4 (Route 1, most actionable):** set up the Gram-trace functional restricted to $\mathbb{Q}(q) \cdot v_{T^*_{\mathrm{rs}}}$, check whether variational uniqueness + $\Omega$'s cone-preservation force nonvanishing. **This is the most direct path to closing the converse.**

3. **Krylov-Paegelow-Shlykov §1-§3 (Route 2, long arc):** pin down $\Omega$'s $K$-class on Gieseker for small $n$, match against trace tables.

## Possible FPSAC abstract

The full theorem statement is now a clean dichotomy:

> For $\lambda = (\hat\lambda, 1^q)$ with $\ell(\hat\lambda) \ge 2$, $\mathrm{tr}_{V^\lambda}\bigl(\Omega^{(\lambda)}\bigr) = 0$ if and only if $\tau(\hat\lambda) = \max(0, q + 2\ell(\hat\lambda) - 1 - |\hat\lambda|) \ge 1$.

That feels like a contributed-talk-shaped result. **Is there a FPSAC 2026 contributed-talk / poster deadline I should hit?** Seattle, July 13-17.

## Logistical

- The unpushed-commits backlog (PAT 403) is still a thing; please refresh the PAT when convenient. `clio-vega/proofs` is now ~79 commits behind.
- Gmail MCP wanted re-auth as of yesterday evening; minor — please re-auth when convenient so I can ping you directly for things like the FPSAC deadline question.

Connection writeups are at `~/projects/memory/connections/2026-05-16-three-converse-routes.md` (the triple convergence) and `~/projects/memory/connections/2026-05-16-variational-bridge.md` (KL ↔ seminormal as dual extrema).
