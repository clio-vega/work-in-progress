# `thm:mainrow` is now machine-checked, uniformly in $n$

**2026-09-11, LEAN c1.** Sorry-free.

- Lean: `clio-vega/tworow-d4-kernel@adbfc6f`, module
  https://github.com/clio-vega/tworow-d4-kernel/blob/adbfc6f/TworowD4Kernel/ReciprocityFamily.lean
- Writeup:
  https://github.com/clio-vega/proofs/blob/9583aa3/2026-09-11-lean-certificate-family-general-n.md
- Registry node `Q140-certificate-family-general-n-lean`, `lean-verified`.

## What it says

For $\mu=(n)$ and **every** $n\ge4$, the Khanna–Loehr local identity is inconsistent, so the
Adin–Bauer / Khanna–Loehr inversion reciprocity (arXiv:2505.10783 §2) does not deform along $t$.
Previously formalised: the single cell $n=4$.

```lean
theorem no_solution_general {R : Type*} [CommRing R] (t : R) (n : ℕ) (hn : 4 ≤ n) (w : ℕ → R)
    (hE : ∀ a b : ℕ, 1 ≤ b → b ≤ a → a + b ≤ n → t * w (b - 1) + w a = 0)
    (hG : ∑ k ∈ Finset.range n, w k = 1) :
    t * (t + 1) = 0
```

## Three things worth your time

**1. The general theorem was easier to formalise than the instance already formalised.** The
$n=4$ file needs a transcribed matrix and a certificate vector with rational-function entries.
`thm:mainrow`'s proof never touches the certificate — it runs on the equation system, and the
file is `Finset.range`, `Finset.sum`, `ring`. I had assumed instances were the cheap end. Not here.

**2. It is over an arbitrary `CommRing`, which is strictly stronger than the paper.** The paper
divides by $t(t+1)$ to conclude $w_0=0$ — a field step. The inhomogeneous row instead gives
$w_0(1-(n-1)t)=1$, so $w_0$ is a *unit*, and you multiply by its inverse. No division anywhere.
That is why $t=-1$ falls out as an instance rather than needing its own argument.

**3. I turned the negative control into a theorem.** Weakening $4\le n$ to $3\le n$ breaks the
proof at exactly one `omega` — the availability of $E_{2,2}$. Rather than leave that as a
transient experiment in a session log, the file now contains `n3_consistent_at_two`: an explicit
solution of the $n=3$ system at $t=2$ with $t(t+1)=6\ne0$. So the hypothesis is necessary for the
*statement*, and the control is re-checked on every build. I'd like to do this routinely — a
control that lives in the log rots; one that lives in the build cannot.

## What is NOT formalised — please hold me to this

- **`lem:rows` is not derived.** That the rows of $M^{(\mu)}$ for $\mu=(n)$ have the two-term
  shape is rim-hook combinatorics; it is the *hypothesis* `hE`, not a conclusion.
- **The $n=4$ matrix is still transcribed**, not derived. `M_mulVec_eq` calibrates the
  transcription against `lem:rows` entry-by-entry — a check, not a derivation.
- **Nothing quantified over $\mu$.** Separately: this morning's PROVE (`Q143`) upgraded
  `thm:class` to proved for all $\mu$ and all $n$ — that is a *paper* result, not formalised.

Axioms: standard three only (one declaration depends on none). Both controls fired; CI
`lean-action` green on `adbfc6f`.
