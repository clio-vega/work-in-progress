# 2026-07-20 · Demazure re-entry cycle — Cherednik–Ram verified, cylindric extension conjectured

**Context.** Your 07-05 steer OFF number theory and ONTO Demazure operators / warnaar-loop. Today's 3h PROVE cycle. Full write-up: `projects/proofs/2026-07-20-demazure-basics-and-cherednik-ram-verification.md`.

## What I did

1. Re-built the Demazure toolbox from scratch in Python + sympy (no Sage in the container). Proved `π_i² = π_i` cleanly via the free `R^{s_i}`-module basis argument (short + illuminating). Verified braid relations computationally.
2. Cross-checked Kostka–Foulkes `K_{λμ}(t)` (my Macdonald-III-symmetrizer computation vs Lascoux–Schützenberger charge statistic) — 0 mismatches on all `|λ| = |μ| ≤ 4`.
3. **Verified the Cherednik–Ram identity** `∑_{w ∈ S_n} T_w(x^{\bar μ}) = v_μ(t) P_μ(x; t)` on 21 cases (n = 2, 3, 4; partitions of size ≤ 4). This is a KNOWN theorem — but having it verified with MY infrastructure is what buys me next-cycle trust.
4. Compared transfer-op vs Demazure builds of `s_{(2,1)}, s_{(3,1)}` side by side. Verdict: they don't intertwine at intermediate steps — different underlying state spaces (partition-kets with polynomial coefficients vs polynomials). They meet at the crystal `B(λ)`, which is where both positivity stories live.

## The sharp conjecture (my deliverable)

**Affine Cherednik–Ram.** For dominant `k`-bounded `μ` and affine Demazure–Lusztig operators `\widetilde{T}_i` (i.e. add `T_0` for the affine reflection):
$$\sum_{w ∈ \widetilde{S}_n^{(k)} / \text{Stab}(\bar μ^{[k]})} \widetilde{T}_w(x^{\bar μ^{[k]}}) \stackrel{?}{=} v_μ(t) \cdot P^{(c, k)}_μ(x_1, ..., x_n; t)$$
where `P^{(c, k)}_μ` is the cylindric Hall–Littlewood polynomial at level `k` and `\bar μ^{[k]}` is the cylindric antipartition.

**Verified:** the linear special case (large-`k`) — 21 cases via Cherednik–Ram.

**Open:** the actual cylindric case (`k ≤ μ_1`). I do NOT have cylindric-HL infrastructure yet — that's the next PROVE cycle.

## Why it matters (why this is a warnaar-loop conjecture)

If the identity holds, `P^{(c, k)}_μ(x; t)` gets a *manifestly positive* expression from the RHS: `\widetilde{T}_w(x^{\bar μ^{[k]}})` empirically lives in `ℕ[t][x]`, and the sum preserves positivity. That is a **Demazure-crystal positive object computing a cylindric HL coefficient** — exactly the pattern your 07-05 email flagged as the target ("[a manifestly positive Demazure-crystal object] computes it"). The bridge to Warnaar's A₂ Andrews–Gordon is: the LHS of A₂ AG is a cylindric-partition multisum; giving its coefficients a positive Demazure-crystal formula is the "climb to the positive object before valuing" move that has worked for the 2-adic capstone in a different key.

## What I did NOT do

- Read your `RaggedR/warnaar-loop-experiment` or `warnaar-glue` code. If findings from the CODE phase are on disk somewhere I missed, please point me — a search for "warnaar-loop" turned up only external Warnaar arXiv papers under `/home/clio/data/`, not code.
- Verify the cylindric case of my conjecture. That requires cylindric-HL implementation, ~1 PROVE cycle's worth of work.
- Verify D2 (braid) from scratch. Only computational verification to degree 5 in `n = 3`; taken as classical.

## What I'd like from you

- Sanity check the conjecture statement — does the affine Cherednik–Ram formulation look right to you? I'm reasoning by analogy with the linear case; if Sanderson (2000) or Ion (2003) already stated something equivalent, please tell me so I don't duplicate.
- Confirm the pathway direction: is next PROVE cycle "build cylindric-HL and test the conjecture on 3 cases" the right move, or should I instead do the affine `\widetilde{T}_i` implementation first and test in the small-cylinder limit `k → ∞`?
- Robin's ask on 07-05 was "one sharp conjecture with ≥3 verified cases." The 3 verified cases I have are all in the LINEAR (large-`k`) regime — that's the special case, not the target. Is that acceptable for this cycle, or should I extend the budget to verify a genuinely cylindric case before landing?

## Loose ends (already in memory)

- SageMath is not installed in the container (contra `CLAUDE.md` tools list). Please install, or update `CLAUDE.md`. I did everything in Python + sympy today; slower but works.

## Pointers

- Proof / report: `projects/proofs/2026-07-20-demazure-basics-and-cherednik-ram-verification.md`
- Scratch: `projects/scratch/prove-demazure-2026-07-20.md`
- Python engine: `projects/scratch/{demazure_engine,demazure_verify,hall_littlewood_engine,hecke_HL,hecke_HL_confirm,transfer_vs_demazure}.py`

— Clio
