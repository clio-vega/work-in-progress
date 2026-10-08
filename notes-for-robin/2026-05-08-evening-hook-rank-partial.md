# Hook rank formula — partial proof

**Date:** 2026-05-08 evening prove session
**Writeup:** `~/projects/proofs/2026-05-08-hook-rank-formula.tex` (8pp, partial result)

## What I have

**Claim.** For the staircase Bott-Samelson Π^{S_n} acting on the standard module V_(n-1, 1):
$$\mathrm{rank}\,\Pi^{S_n}|_{V_{(n-1,1)}} = \lceil (n-2)/2 \rceil$$

**Status:** Conjectural in general. Rigorously proved for n=4. Computationally verified for n ≤ 8.

## What's rigorous

1. **Lemma 4 (D_n image, rigorous for all n):** R_n'(V_(n-1,1)) = span(v_2, v_3, ..., v_{n-2}, u_{n-1}), where v_k is the seminormal SYT with k in row 2, and u_{n-1} = α_{n-1} v_{n-1} + β_{n-1} v_n is the +q-eigenvector of T_{n-1}. Dim n-2. Proof: iterative image tracking through each (T_i+1) factor.

2. **Proposition 7 (n=4 rigorous):** rank Π^{S_4} on V_(3, 1) = 1 = ⌈(4-2)/2⌉. Direct trace.

## What's computational

Dimension sequence dim D_k = max(⌈(n-2)/2⌉, k-2) for n ≤ 8, where D_k = R_k' R_{k+1}' ... R_n'(V). The drops occur at R_k' for k ∈ [⌈n/2⌉+1, n] (exactly ⌊n/2⌋ drops), then dim stays.

## Where the proof gets stuck

The general inductive step requires either:

**(a) Detailed image tracking** — prove the structural invariant: D_k has form "free v_2 ⊕ tied chain in E_1^+" for k > ⌈n/2⌉, "tied v_2 in E_1^+" for k ≤ ⌈n/2⌉. The pattern is clear computationally but requires many lines of careful case analysis through each R_k' block.

**(b) Branching dichotomy:** rank Π^{S_n} on V_(n-1,1) = ⌈(n-3)/2⌉ + 1 - δ(n) where δ(n) = 1 iff "v_{n-1}^* annihilates ker Π^{S_{n-1}}|_{V_(n-2,1)}". The needed dichotomy:

> δ(n) = 1 iff n even.

Or equivalently (m = n-1):

> v_m^* annihilates ker Π^{S_m}|_{V_(m-1,1)} iff m odd.

I verified this for m ≤ 7 but did not find a structural proof. The dichotomy alternates with each step of induction, which is intriguing but I don't see why structurally.

## Why I stopped here

The proof of Lemma 4 (D_n) is clean and rigorous. The recursion onwards is complicated by the dichotomy at each step. Time-wise, I chose to write up what I have honestly and identify the specific gap, rather than push through a tedious case analysis that might still have holes.

## Why this matters

This would be the **first family of partitions for which a closed-form non-zero rank formula has been structurally proved**. The morning's writeup (rank-Pi-structural.tex) gave structural rank-1 for V_(2,2,1) and V_(3,1,1) at S_5 specifically; the rank-zero theorem covers all rank-0 cases. Closing this would extend the rank story to an infinite family of rank > 0 cases.

The dichotomy itself is interesting: if true, it means the standard module's "Π^{S_m}-image structure" alternates with parity of m, which I haven't seen elsewhere.

## Next steps if you want to push

1. **Try the dichotomy directly.** Compute ker Π^{S_m} on V_(m-1, 1) for m = 4, 5, 6 explicitly and look for a pattern. The thing to spot: why does v_m^* "alternate" between zero/nonzero on ker?

2. **Try the iterative-image case analysis.** Tedious but feels mechanical. Each R_k' block transforms the previous form; the transition at k = ⌈n/2⌉+1 is the interesting one.

3. **Try other hook families.** V_(n-2, 2) has conjectured rank n-3. Same iterative-image technique should apply but the SYTs are now indexed by pairs of cells.

## Files

- `~/projects/proofs/2026-05-08-hook-rank-formula.tex` — main writeup.
- `~/projects/scratch/2026-05-08-hook-rank/verify_hook_rank.py` — dimension survey.
- `~/projects/scratch/2026-05-08-hook-rank/check_image_columns.py` — explicit Π v_k columns.

## Push status

Read-only PAT remains a blocker — these will sit local until pushed. Now 11 unpushed commits if I count this one (see standing PROVE.md notice).
