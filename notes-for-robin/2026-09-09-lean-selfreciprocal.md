# Q105 Lemma 3.3 is machine-checked — and formalising it simplified the printed proof

**2026-09-09, LEAN session.**

`clio-vega/tworow-d4-kernel@4ab399c`, module
[`TworowD4Kernel/SelfReciprocal.lean`](https://github.com/clio-vega/tworow-d4-kernel/blob/main/TworowD4Kernel/SelfReciprocal.lean).
Snapshot note: `proofs/2026-09-09-lean-selfreciprocal-order-parity.md`.

## What is verified

> If $0 \neq \Pi \in \mathbb{Q}[t]$ satisfies $\Pi(t) = t^N \Pi(1/t)$, then
> $\operatorname{mult}_{t=-1} \Pi \equiv N \pmod 2$.

Sorry-free. 12 declarations, every one on exactly `{propext, Classical.choice, Quot.sound}`.
`lake build` and `lake test` both exit 0. No `decide`, no `native_decide`.

This is the step that turns "palindromic" into "the order at $t=-1$ has a *fixed parity*", which
is what makes the vertex-side order function $(m+n) \bmod 2$ instead of an unstructured integer.
That parity is the separator the whole Q105 "distinct" decision rests on, so this certifies the
half of that crown that was carried by a hand proof.

## The thing I actually want to tell you

**Planning the formalisation produced a better proof than the one I published.**

My printed proof factors over $\overline{\mathbb{Q}}$, pairs the roots $\{\rho, 1/\rho\}$, and then
runs a separate argument that the multiplicity at $t=+1$ is even. That route wants an algebraic
closure and root multisets — expensive in Lean, and, it turns out, unnecessary. The induction is:

- $N$ odd $\Rightarrow$ $P(-1) = (-1)^N P(-1) = -P(-1)$, so $P(-1) = 0$. One substitution.
- $P = (t+1)Q$ $\Rightarrow$ $Q$ is self-reciprocal with $N-1$, by cancelling $(t+1)$.
- Induct.

**Consequence for the paper:** the preliminary reduction to $\Pi(0) \neq 0$ (writing
$\Pi = t^\alpha Q$) is *removable*. Step (b) goes through verbatim when the constant term
vanishes. That is a simplification of a printed proof of mine, found by asking what the theorem
costs to state rather than what it costs to believe.

Generality came free: it holds over any commutative ring with no zero divisors in which
$2 \neq 0$. The $\mathbb{Q}$ and $\mathbb{Z}$ statements are both corollaries.

## One thing the formalisation caught

"$\Pi(t) = t^N\Pi(1/t)$" does **not** translate to `reflect N P = P` on its own. Mathlib's
`revAt N` fixes every index above $N$, so that condition is blind there: $t^2$ satisfies it at
$N=1$ and has multiplicity $0$ at $t=-1$, the wrong parity. The degree bound $\deg\Pi\le N$ — which
is *implied* by the Laurent identity, and which I had never written down separately — is
load-bearing. It is a field of the definition now, and the counterexample is proved, not asserted.

## What this is NOT

**This is Lemma 3.3 only.** Lemma 3.2 (self-reciprocality of $\Pi_{\nu\lambda}$ itself) and
Theorem B(i) (the power-sum order computation) are *not* formalised — they need the ring of
symmetric functions and plethysm, which this repository does not have. The registry node is a
*premise* of `Q105-vertex-order-is-parity-of-m-plus-n`, which stays at `proved`. Please do not
read this as "Theorem B is verified".

CI run `34322729509` was still in progress when the session ended, so its result is unknown
rather than green. Local build/test/axiom evidence is all above.

## A question for you, not a change I should make

The repo is called `tworow-d4-kernel` and now holds cross-rank ribbon commutators and a general
polynomial lemma about palindromes. The name stopped describing the contents a while ago. I have
*not* renamed it: every PDF I have sent under PROTOCOL §2.3 cites a commit hash in that repo, and
a rename breaks all of them. Do you want it split, renamed with redirects, or left alone?
