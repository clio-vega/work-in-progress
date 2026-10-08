# For Robin — 2026-06-07 prove session: two routes closed, law verified to n≤20

Hi Robin,

Honest session: no theorem *proved positive*, but I **settled two open routing questions decisively**
(both negative), which is exactly the kind of progress that saves future cycles from chasing ghosts.

## 1. PRIMARY target settled — residual is NOT a function of the 4-quotient (Outcome 3)
The Gap-A plan was: `v_π(G_λ) = v₂(f^λ) + [v_π(G_{4core}) − v₂(f^{4core})] + residual(λ)`, hoping
`residual = f(4-quotient)`. **It isn't.** Smallest counterexample at n=10: `(1,1,1,1,1,1)` and `(4,4,2)`
share the 4-quotient `((),(),(1,),())` but have residuals 0 and 1. The residual genuinely depends on the
**4-core** (and even on *which abacus runner* the quotient box sits on). So that route to the full
fiber law is dead as stated. The near-miss is interesting though: residual *is* a function of
`(v_π(G_core), v₂(f_core), quotient)` for 775 of 787 groups — it fails only at one large-core class.
The right next object is a direct `v_π(G_λ)` formula with a finite core×quotient **interaction term**.

## 2. Two-row fast-path closed — Q_b is NOT a classical orthogonal polynomial
Browse was excited that `Q_b` "looks binary-Krawtchouk." I checked: **no match** to Krawtchouk, Meixner,
Hahn, dual Hahn, Chebyshev, or the MO#286705 family (up to scalar + affine), and the discriminants are
non-square with no pattern. It was a generating-function *resemblance*, not an identity. So there is no
known irreducibility theorem to import — (♦) ("Q_b has no rational root") is a genuinely new,
self-contained Diophantine problem. The 2-adic route was already dead; now the OP-import route is too.

## 3. The law itself is rock-solid
`G_λ(i) = 0 ⟺ λ = (2,2)` verified for **all** shapes `λ ⊢ 2m`, `n ≤ 20` (unique vanisher), and the
two-row `I_b(m) ≠ 0` for integer `m ≥ b` confirmed to `b ≤ 40`, `m ≤ 3b²`. The `core=(2,2)` mechanism
(finite π-depth ⟺ nonempty quotient) holds with 0 violations across 163 shapes. We *believe* it
completely; we just don't yet have the uniform proof.

## Where I'd point next
- Gap A: chase the interaction-term formula for `v_π(G_λ)` — characterise the 12 exceptions to the
  near-formula, then aim only for *finiteness* of the interaction (enough for `G=0 ⟺ (2,2)`).
- (♦): it's pure number theory now (no rep-theory, no OP catalogue). Multi-prime Newton polygon at an
  *odd* prime, or a Galois-image argument on this new family.

Writeups: `proofs/2026-06-07-residual-not-quotient-function.md`, `code/FINDINGS-4core-residual.md`,
data in `code/results/residual-vs-4quotient.csv`.

— Clio
