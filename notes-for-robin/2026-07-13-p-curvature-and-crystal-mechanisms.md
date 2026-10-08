# Two new mechanisms for the order law — one of them is on your cylindric path

*Clio, 2026-07-13 (container clock 07-05). Browse-level, not results — both crown papers are read at
abstract/agent-summary level, flagged deep-read-before-load-bearing. But the shape is worth your eye.*

Two browses this week each handed the order law `ord_{x=q²}Z_λ = τ(τ+1)/2` a genuinely new candidate
mechanism, from opposite directions. Together with the three determinantal frameworks from last week,
that makes **five** — and they don't compete, they stratify:

1. **Combinatorial layer** — `τ(τ+1)/2 = C(k,2)` as a triangular number in three frameworks (Cauchy
   determinant rank, box-ball KKR rigging, affine dual Jacobi–Trudi).
2. **Arithmetic-geometric layer (NEW, 07-12)** — **Koroteev–Smirnov 2412.19383**: the quantum
   K-theory of a Nakajima variety at a root of unity `q=ζ_p` is governed by a **Grothendieck–Katz
   p-curvature / Frobenius spectrum**. This is the first thing I've seen in the literature that could
   explain *why the 2-adic shadow exists at all* — and, crucially, it's the only one of the five that
   predicts the **mod-4 structure** of `J*` (the `{0,2}`/`{0,4}` toggle), not just the order. A
   Frobenius spectrum is exactly the kind of object whose arithmetic is periodic mod a prime power,
   which is what my gen-4 resonance `v₂(c)+v₂(c−4)` (period 4) looks like.
3. **Representation-theoretic layer (NEW, 07-13)** — crystal operators directly on 5-vertex states
   (**Johnston–Nguyen–Schilling 2606.02972**): read the order off an *uncrowding-chain depth*, never
   constructing a signed alternant. The cleanest instance of the theme I keep circling —
   *cancellation is the enemy, positivity is the resolution.*

**The one for you specifically:** **Korff–Stroppel "Quantum cohomology... cylindric" (1110.6356)** keeps
surfacing as the closest external mirror of the whole program — cylindric Macdonald/HL functions in a
**coproduct**, `q=0` → **Verlinde fusion**, functions = **YB vertex-model** partition functions. That
is four seed threads in one object, and the coproduct + cylindric setting is *your* thesis territory.
I have never fully read it (the PDF didn't parse). If you have a spare hour, it may be the single paper
that ties my Baxterised-Ω order law to your cylindric-partition machinery.

Also, small but real: this week's Lean cycle made the c=4 boundary + interior formalisation **durable**
— it was tracked by no git repo. It's now committed and pushed to `clio-vega/proofs` under
`lean-src/tworow_d4_kernel/`, 0 sorry, standard axioms only. (Separate note:
`for-robin/2026-07-05-lean-multiplicative-redundancy-witness.md`.)

Nothing here is proved yet — the discriminating test (does the p-curvature spectrum reproduce my mod-4
box?) is the next thing I'd chase, and it needs a proper read of Koroteev–Smirnov first.
