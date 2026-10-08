# For Robin — the determinant crown split (a correction), and a paper that mirrors your cylindric thesis

*2026-07-11 dream. Follows up my 07-08 note "route1-negative-names-the-order-law's-determinant" — which the
deep reads have since partly corrected. I'd rather flag the correction than let the earlier note stand.*

## The honest correction first

My 07-08 note told you the order law's Content Lemma and the spectral order law were **one determinant read at
two specialisations** (Di Francesco–Vu's Cauchy determinant `t^{C(|J|,2)}`). I read both source papers in full
since, and the claim splits:

- **Order-law half — still real, but with a gap I own.** Di Francesco–Vu (2606.12796) Thm B.1 genuinely has a
  triangular exponent `t^{C(|J|,2)}` in the right integrable universe. **But** they assume distinct variables and
  never take the coincidence limit `x_i→x_j` — so the step that would turn that constant exponent into a
  *vanishing order* `τ(τ+1)/2` is **absent from the paper**. It's mine to prove, not a literature import. That
  one lemma (set `x_i=x_j(1+ε)`, read the leading ε-power) is now the crux, and it's a one-script check.
- **Content-Lemma half — I was wrong about the object.** The paper I'd tagged as its determinantal home
  (Gatzweiler–Krattenthaler 2502.06032) is **not a determinant at all** — no LGV, and `q=−1`/`Φ₂` is never
  singled out. That was an extraction hallucination that survived two cycles because nothing carried it back to
  the source. I've corrected it and banked the discipline: a shape-match is a probe, never a result.

The *theme* you and I liked — cancellation is the enemy, positivity is the resolution — is untouched and, if
anything, stronger.

## The better news: `τ(τ+1)/2` is a triangular number in THREE frameworks now

Off the determinant thread, the order law's triangular shape `C(k,2)` turned up independently three times:
Cauchy determinant (rank), **box-ball KKR rigging** `C(ℓ+1,2)` (soliton length), and **affine dual
Jacobi–Trudi** staircase. That third one is `t=−1` Hall–Littlewood — the natural home for the even-valuation
lemmas — and it is genuinely *cylindric/affine*, i.e. your thesis path, not the non-cylindric Cauchy route.

## The paper you should see: Korff–Stroppel 1110.6356 (2011)

"Cylindric versions of specialised Macdonald functions and a deformed Verlinde algebra." Cylindric HL/Macdonald
functions sitting in the **coproduct** of a spherical-Hecke Frobenius algebra; at `q=0` the structure constants
become **sl(n) Verlinde fusion** coefficients; and the functions are **Yang–Baxter vertex-model partition
functions**. That is cylindric partitions + Hall–Littlewood + fusion + YBE + Hopf coproduct in one object — the
closest external mirror of the whole Baxterised-Ω program, and it's built on exactly your cylindric-plane-partition
machinery. I'd never opened it. **Could you point me at whether this is already in your thesis' orbit?** If it is,
the "order law = fusion-multiplicity vanishing order at a root of unity" reading might be almost off-the-shelf.

## Two asks

1. **Still open (7+ dreams): a Sage MN cross-check of the closed-form `G_j`.** My in-container MN engine can't
   reproduce the physical `G_j` (it fails even accepted c=3 values). Everything downstream is 2-adically
   self-consistent, but the link "my closed form = the true `G_j`" rests on the prove-session `mn.py`. A short
   Sage run would retire this debt.
2. **Next wake target I'm queuing:** the **KKR-rigging probe** — build box-ball / rigged-config data for small
   three-row shapes and test `|rigging| = τ(τ+1)/2`. If it holds, IMSS's connectivity theorem (2606.17525) is a
   *uniformity-across-families* engine, which is exactly what my case-by-case content lemmas lack. Cheap Sage.

Everything is in `connections/2026-07-11-tau-triangular-three-frameworks.md` and today's dream journal.
