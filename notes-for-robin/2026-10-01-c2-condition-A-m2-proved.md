# Condition (A) at m=2 is proved — and the inequality you asked me to prove is false

**1 October 2026, c2 prove session.**
**Pushed, so you can read it:**
- Paper (PDF): https://github.com/clio-vega/proofs/blob/main/2026-10-01-c2-inter-region-inequality.pdf
- Paper (source): https://github.com/clio-vega/proofs/blob/main/2026-10-01-c2-inter-region-inequality.tex
- Registry: https://github.com/clio-vega/proofs/blob/main/registry/cylindric-lorentzian.json
- Verification code: https://github.com/clio-vega/proofs/tree/main/code-q256-m2-radial

## Short version

The brief asked for inequality (G), the one remaining gap of the 30 September paper. Step 0
of the brief — extend the verification range before proving anything — **refuted it in the
first computation of the session.** But the refutation's mechanism handed me the theorem, so
the session's deliverable is not a counterexample report: **condition (A) at m=2 is now
proved in full**, for every slice, by a route that does not use (G) at all.

## (G) is false

Witness: `n=10`, `μ=(0,5)`, `λ=(5,12)`, `b=4`. Two region partial sums land on the *same*
support `[10,16]`:

```
G_I   = (1, 3, 6, 7, 6, 3, 1)
G_III = (1, 1, 1, 1, 1, 1, 1)
```

At `s=11` the inequality reads `2·3·1 = 6 ≥ 7 = 1·1 + 6·1`. False.

The part worth your attention is not the witness but **where it was available all along.**
If one sequence is *constant* `c>0` across a window containing three consecutive points of
the other's support, then the pairwise inequality `(*)` for that pair is **literally
concavity** of the other — both sides are `c` times the concavity inequality. And §"Concavity
is false" of the very paper that posed (G) proves concavity false, **with the same sequence
`(1,3,6,7,6,3,1)`**. So (G) was refutable from a fact printed four pages after it, in the
same document, by a two-line lemma.

The `525/525` verification score did not catch it because the configuration requires a
non-concave region sum sitting *beside a flat one*, and the smallest such slice has `n=10`,
`d=12` — outside the birth range `n≤8, d≤10`. This is the same generator as the `k(·,b)`
concavity kill: **a perfect score on the discovery set.** Census over `n≤11, d≤14` (201147
slices, 37672 pairs): 92 failures, every one of them the pair I–III, every one with three
regions nonempty. Condition (A) itself fails in none of the 201147.

A free correction while I was there: **regions II and IV are never both nonempty** (II needs
`τ₁≤τ₂`, IV needs `τ₂<τ₁`), so at most three regions ever occur and they form a chain. The
brief's recommended first target — "attack II–IV first, the shared-`H` case" — is vacuous.

## The proof

The regions are the wrong cut. Cut by **layer** instead.

**Step 1 (the whole content).** Two identities, each spending one hypothesis exactly once:

```
a_t + d_t = t + D        (uses A = D-n+1)
b_t + c_t = u + B - t    (uses C = B+1)
```

Each one makes a `max`/`min` pair agree **on both branches**, not merely at the breakpoint.
This is strictly stronger than the paper's observation that the four endpoint functions share
only two breakpoints: it says the two *crossed* sums are globally affine in `t`.

**Step 2 (concentricity).** Adding and subtracting gives
`(a_t+c_t)+(b_t+d_t) = u+B+D` and `n_t - m_t = u+B-D-2t`. So **every trapezoid in the slice
sum is symmetric about the same centre** `σ₀ = (u+λ₁+λ₂)/2`, independently of `t`. The
antichain the paper kept running into along `t` is, along the orthogonal direction, a nested
chain of concentric intervals.

**Step 3 (radial form).** Therefore `G(s) = γ(|s-σ₀|)` where `γ(y) = Σ_{r≥y} β(r)` is the
**upper tail** of the layer profile `β(r) = #{t ∈ T : δ_t ≤ r ≤ L_t}`, with `δ_t = |t-t₀|`
and `L_t = (n_t+m_t-2)/2` a concave tent in `t`.

**Step 4.** `β` is the positive part of an explicit concave integer function, hence PF₂ by
`lem:trunc` — which is already Lean-verified from the 30 September work.

**Step 5 (key lemma).** *The upper tail of a PF₂ sequence is log-concave.* With
`Δ = β(y-1) - β(y)`,
`γ(y)² - γ(y-1)γ(y+1) = β(y-1)β(y) - Δ·γ(y)`, and log-concavity forces geometric decay
`β(y+k) ≤ β(y)qᵏ` with `q = β(y)/β(y-1)`, so `γ(y) ≤ β(y)/(1-q) = β(y-1)β(y)/Δ`. Done.
This is the discrete form of the classical "log-concave pmf ⇒ log-concave survival function";
I prove it because it is three lines and because I want the hypothesis visible.

**Step 6.** Radial + symmetric + `γ` nonincreasing log-concave ⇒ `G` is PF₂. □

## Why both negative results were inevitable

One identity explains them:

```
2γ(y) - γ(y-1) - γ(y+1) = β(y) - β(y-1).
```

So `G` fails concavity **exactly** on the strictly decreasing part of `β` — and `β` is `c₊`
for `c` concave, so it decreases unless it is constant. For §"Concavity is false"'s witness
`(1,3,6,7,6,3,1)`: `γ=(7,6,3,1)`, `β=(1,3,2,1)`, `β(2)-β(1) = -1`, failure at `y=2`, which
is precisely the recorded `2·3 < 1+6`. Concavity is not nearly true; it is false by an
identity. And since `(*)` against a flat partner *is* concavity, (G) is dead with no
quantifier left to shrink — it is not "unverified outside a range" and not "true with a side
condition".

## What this does and does not settle

- **Settles:** condition (A) at `m=2`, all slices. Replaces the 79.9% single-region criterion.
- **Does not settle:** Lemma T in its stated generality. Concentricity uses the cylindric
  alignment; for arbitrary concave/convex 1-Lipschitz `Φ,Ψ` the trapezoids need not share a
  centre. Lemma T is now known to be **strictly stronger than `m=2` needs**, and remains open.
  My framing on 30 September — "prove Lemma T and `m=2` closes by any route" — was true but
  backwards in value.
- **Does not touch:** condition (B) (`conj-B-logsubmodular`), still `computed`.
- **Next for `m≥3`:** the one-line generalisation of concentricity. Is
  `Σ_i (L_i(ν) + R_i(ν))` independent of `ν` on each slice? That is the first thing I would
  check, and it is cheap.

## Two things I got wrong in my own instruments, recorded because they were near misses

1. **A frightening number shaped exactly like a finding.** My first structural sweep reported
   **9616 mismatches** of `G = γ(|s-σ₀|)`. All spurious: my tail accumulator built `γ` only
   down to `min supp β`, so `γ(0)` was never computed when `β(0)=0`. Smallest exposing case
   `n=4, μ=(0,1), λ=(0,3), b=0`, where `G=(1,1,1)` and the reconstruction dropped the middle
   entry. After the fix: 0 mismatches on 27522.

2. **A refusal control that would not fire was telling me about the theorem, not the
   instrument.** My first proof of the key lemma assumed `β` *truncated-concave*. The control
   for that hypothesis — `β` log-concave but not truncated-concave — gave **0 failures in 5578
   trials**. I nearly filed that as "control passed". It was saying the hypothesis was not
   load-bearing: only log-concavity is needed, and that proof is shorter. The corrected control
   (interval support, *not* log-concave) refuses 82.6% of 374527 inputs. I think this is a
   general rule worth keeping: **a control that will not fire is evidence that the hypothesis
   it varies is too strong**, i.e. that a weaker theorem is hiding behind the one I wrote.

## Verification

- Crossed-sum identities and concentricity: **0 violations / 292290 slices** (`n≤12, d≤14`).
- Radial form: **0 mismatches / 27522** after the accumulator fix.
- `β` PF₂, and the explicit concave formula: **27522/27522**. The clamp in that formula is
  load-bearing — removing it gives the wrong `β` in 7245/13761 — and is *active* in
  14490/27522.
- Key lemma: 0 failures on 161771 random PF₂ sequences plus an exhaustive enumeration of all
  9654 PF₂ sequences in `{0..7}^L, L≤6`.
- Condition (A): **0 failures / 201147 slices** (`n≤11, d≤14`); then extended by the direct
  trapezoid sum, *not* using the radial shortcut, to `n≤16, d≤20` — **0 failures / 89366**.
- **Estimand check.** `G(u+a) = k(a,b)` confirmed by an *independent* chain enumeration
  `μ≺ν≺κ≺λ` built on the vendored `code-q254/cyl.py` primitives, never touching
  `a_t,b_t,c_t,d_t`: **3427/3427**, with the `k(a,b)=k(b,a)` symmetry control at 4908/4908.
  I ran this because yesterday I had to withdraw a result for proving something true about the
  wrong object.
- `trustcheck` on the updated registry: **OK, exit 0** — and I planted a boundary violation
  first (demoted a genuine premise to `computed`) and confirmed it **refuses**, before
  believing the OK.
- `tracecheck` flagged my estimand `verify` event as **circular, and was right about what I
  wrote** — I put the verification target in `inputs` again, the same defect as 26 September.
  Re-emitted correctly; the original is left flagged in the record rather than rewritten.

— Clio
