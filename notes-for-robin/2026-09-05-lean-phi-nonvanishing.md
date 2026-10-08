# Q83's load-bearing sentence is now machine-checked — and it has one hypothesis fewer than the paper claims

2026-09-05, LEAN session (cycle 2).

## What I formalised

`proofs/2026-09-05-Q83-sharpness-all-k.tex`, Theorem "main", closes Q83 by reducing the whole
equivalence to a single sentence:

> "each $1-x^{e_i}\ne0$ in the integral domain $\mathbb Z[x]$, so $\Phi_{\vec e}\ne0$."

That sentence, and the degree bound in the sentence after it, are now Lean 4 / Mathlib
theorems. Sorry-free, standard three axioms.

**Files.**
- Lean: https://github.com/clio-vega/tworow_d4_kernel/blob/main/TworowD4Kernel/PhiNonvanishing.lean (commit `d41c0c5`)
- Write-up: https://github.com/clio-vega/proofs/blob/main/2026-09-05-lean-phi-nonvanishing.md (commit `e9ec565`)

## The two theorems

```lean
theorem Phi_ne_zero   (hab : a < b) (he : ∀ m ∈ e, 1 ≤ m) : Phi a b e ≠ 0
theorem Phi_natDegree (hab : a < b) (he : ∀ m ∈ e, 1 ≤ m) :
    (Phi a b e).natDegree = (b - 1) + e.sum
```

with `a = min(e_{k-1}, e_k)`, `b = max(e_{k-1}, e_k)`, `e = [e_1, …, e_{k-2}]`. The second is
the paper's $\deg\Phi = e_{\max}-1+\sum_{i\le k-2}e_i = E-e_{\min}-1$.

I did not formalise the quotient $\frac{x^a-x^b}{1-x}$. For $a<b$ it *is* the geometric sum
$x^a+\dots+x^{b-1}$, and that sum is what the paper's own window derivation produces three
lines earlier, before contracting it into a fraction. So the sum is the definition.

## The thing worth telling you

The sentence reads like one appeal to one fact. **It is two nonvanishing arguments with
disjoint witnesses**, and each factor is zero at the point that certifies the other:

| factor | nonzero because | at the other point |
|---|---|---|
| $1-X^m$ | $\mathrm{eval}\,0 = 1$ | $\mathrm{eval}\,1 = 0$ |
| $\sum_{i<b-a}X^{a+i}$ | $\mathrm{eval}\,1 = b-a$ | $\mathrm{eval}\,0 = 0$ (unless $a=0$) |

There is no single evaluation point that sees both. `mul_ne_zero` over `IsDomain (Polynomial ℤ)`
glues them. This is invisible in the prose and unmissable in Lean — which is, I think, the
honest answer to "why formalise something that is certainly true".

## A correction to the paper's bookkeeping

`thm:main` hypothesises $e_1,\dots,e_k\ge2$ throughout. **The nonvanishing step needs only
$e_i\ge1$.** $m\ge1$ is exactly what makes $\mathrm{eval}\,0\,(1-X^m)=1$; $m\ge2$ buys nothing.
The Lean statement is at $1\le m$ and is strictly stronger than the paper's.

The $\ge2$ *is* a real hypothesis of the theorem — it gives $e_{\min}\ge2$, which is what the
degree window in the next sentence uses — so nothing in Q83 changes. But it is not a hypothesis
of this step, and carrying it in would have put a pinned parameter inside a lemma that does not
need it. That is the failure mode I have been hunting all week from the other direction.

## Where the off-by-one would have hidden, and didn't

$\deg\Phi$ is the step that guarantees the witness $j_0$ is a legal hook index at all
($0\le j_0\le E-1$), so it is where I expected trouble. It came out as an **equality**, not the
weaker bound I had authorised myself to fall back on: the window tops out at $b-1$, not $b$.

Cross-checked against your own worked example in the paper, $(e_1,e_2,e_3)=(4,2,3)$: Lean
computes $\Phi = X^2 - X^6$ from the definition and returns degree $6$, which independently
equals $E-e_{\min}-1 = 9-2-1$. Two routes, same number, neither fitted.

## What is *not* checked

Equation (phi) itself — that $[x^j]\Phi_{\vec e}$ *is* the matrix entry — is untouched, as is
the valuation conclusion. So `thm:main` stays `proved` in the registry, not `lean-verified`;
the two new Lean nodes are children of it, not a re-grade of it.

Also: `Polynomial ℤ` is `noncomputable`, so none of this can be exercised by the `#guard` test
driver. Coverage is `lake build` plus `#print axioms`, and I have recorded that in the registry
so no later reader infers otherwise.

CI run `33992891516` was still in progress when the session ended (green runs on `main` take
35–43 minutes), so I am not reporting it as passing. Local evidence: `lake build` succeeded
(2977 jobs), and `#print axioms` returns `[propext, Classical.choice, Quot.sound]` for all six
declarations.
