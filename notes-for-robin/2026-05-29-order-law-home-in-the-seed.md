# The order law's home might be in the seed, not abroad — a fourth proof route to test

**2026-05-29 (dream cycle — a strategic note, not a result)**

Robin — a reorientation worth flagging, on top of today's two results (Fujita = 10th shadow;
forward backbone collapse proved).

## The pattern I finally saw

For about eight sessions I've been hunting the "home" of my order law
`ord_{x=q²} Z_λ = τ(τ+1)/2` in **foreign rings** — Fujita's quiver E-invariants, Trinh's
Hecke-character trace, Q-operators, Petrov's tilted Toeplitz minors, p-curvature. Every single
one came back the same way: *the number matches, the functional dependence matches, but there's
no transferable theorem.* Grammar, not machine. Ten shadows.

Today's browse swung deliberately **back to the seed proper**, and that's where I found the
deepest-overlapping candidate — **Bump–Hardt–Scrimshaw, "Factorial Fock free fermions"
(arXiv:2410.06582)**. It is *not* a foreign ring. It lives inside the exact formalism
`transfer_operators.py` already implements: fermionic Fock space, with factorial Schur (the
Molev seed) as the deformation, and — the key — its **half vertex operators ARE the six-vertex
row transfer matrices** (Naprienko's model), with images solving the **2D Toda lattice**
(tau functions).

## Why this could be the actual machine

My `Z_λ(x)` is a **trace of a transfer matrix**. In the Fock/vertex-operator picture, that is
a **tau function**. So `ord_{x=q²} Z_λ` becomes a **Plücker–Hirota-computable order of
vanishing** — a count of fermion modes that collapse at the degenerate spectral point.

And it rhymes with something I already proved: `τ+1` is the **column-1 box-charge**, and in the
boson–fermion correspondence **column reading = fermion modes**. So "τ as a charge" and "the
tau-function vanishing order as a fermion-mode count" may be *the same object viewed twice*.

Crucially, the ten shadows each failed for a reason internal to the foreign ring (Fujita: my
system is A₁, where self-E ≡ 0; Petrov: no vanishing-*order* theorem exists there at all). BHS
has none of those obstructions — same Fock space, same transfer matrix. **If any home carries a
transferable machine, this is the one.**

## The cheap test (next wake session)

1. Read Naprienko 2301.12110 + the BHS transfer-matrix section.
2. Build the dictionary: which spectral parameter is my `x`, where `x=q²` sits in the Toda flow.
3. Test on data I already have (exact `Z_λ` on ~13 shapes): does `Z_λ(x)` match a ratio of
   factorial-Schur / tau functions at `x=q²`, with the order counting collapsing fermion modes?

If it clicks, it's a **fourth, seed-native proof route** — complementing the chip-firing
min-degree proof (hooks) and the operator min-support / Strong Pillar 1 line — and it might
sidestep the merged-junction gap entirely. If it fails it's either an 11th shadow (the first on
the *Fock* side) or a precise reason factorial Schur ≠ my Hecke-Baxterised Ω. Either way I learn
something sharp.

No action needed from you — just wanted you to see the shift before I spend a session on it.
— Clio
