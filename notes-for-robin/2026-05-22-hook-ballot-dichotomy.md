# Hooks: the trace `tr_{V^{(k,1^m)}}(Ω)` is governed by a ballot condition

*Clio, 2026-05-22 prove session. Paper: `~/projects/proofs/2026-05-22-hook-transfer-chain.tex`
(6pp, compiles). Scripts: `~/projects/scratch/2026-05-23-hook-transfer-chain/`.*

Robin — I took the "content-graded transfer chain" prove target and did NOT build the YBE
transfer matrix. Instead I found the simple per-tableau combinatorics the transfer picture was
standing on top of, and I think it's cleaner and gets us further on the actual open questions
(converse + min-degree for hooks).

## The one-line phenomenon

In the Hoefsmit seminormal basis, index a hook SYT by its **leg set**
`L={l_1<…<l_m}` (entries below the corner). Then

> **`⟨T|Ω|T⟩ ≠ 0  ⟺  l_i ≥ 2i+1 for every i`**  (a corner-rooted ballot/Dyck condition).

Verified for every tableau of every hook with `n ≤ 9`. Everything else falls out of this.

## What I proved (fully, modulo the two gaps below)

- **Prefix factorisation** `Ω = R_2R_3⋯R_n`, `R_k=(T_{k−1}+1)⋯(T_1+1)`, so
  `Ω_n=Ω_j·(R_{j+1}⋯R_n)` with `Ω_j∈H_j`. Lets me cut a tableau at the first lattice-path
  return and land on a smaller hook.
- **Reduction:** a non-ballot tableau has its *entire row* `⟨T|Ω=0`. The first return at `j`
  forces the sub-tableau on `{1..j}` to be a boundary hook `(t,1^t)`, and `Ω_j` kills it.
- **Strong vanishing:** for `m≥k+1`, `Ω` is the **zero operator** on `V^{(k,1^m)}` (branching
  induction; bases are the sign-rep column where `T_i+1=0`, plus the boundary hook). So
  `c_m=0` for `m≥k` — stronger than trace-zero. (The bare `c_m=0` also follows from our prior
  forward theorem, commit 92a5323.)
- **Threshold, combinatorially:** a ballot tableau exists iff `m<k`. Clean.
- **Converse (the prize), `m<k`:** non-ballot diagonals vanish; among ballot ones the **unique**
  smallest-valuation diagonal is the arm-first tableau `T*` (row `{1..k}`, leg `{k+1..n}`),
  with `val = m(m+1)/2 = n(λ)` and **leading coefficient exactly 1**. Hence
  `c_m = q^{m(m+1)/2}(1+O(q))`, so `c_m ≠ 0`. This is the open converse `m<k ⇒ c_m≠0`
  **for hooks**, and the min-degree law with explicit leading coefficient.

## The two gaps (precisely located, both verified `n≤9`)

1. **Boundary Lemma:** `Ω = 0` on `V^{(t,1^t)}`. It is the linchpin — both the strong-vanishing
   base AND the non-ballot reduction need it. It reduces to a clean linear-algebra statement:
   `im(Π_{U_2}∘R_{2t}) ⊆ ker(Ω on V^{(t,1^{t-1})})`, i.e. the full rake `R_{2t}` rotates the
   leg-block into the kernel of the smaller Ω. This is exactly the "channel closes" step of the
   transfer picture, now isolated to the `C_{t−1}` ballot-until-the-end tableaux. **I think this
   is the right thing to attack next** — it's small and concrete (the `t=2` case is a 3×3
   verification).
2. **Valuation lower bound** = hook case of our standing **Core Lemma**: for ballot `T≠T*`,
   `val⟨T|Ω|T⟩ = m(m+1)/2 + Σ_i((k+i)−l_i) > m(m+1)/2`. The deficiency formula is dead-on for
   all ballot tableaux I checked.

## One honest surprise

The "obvious" all-stay (pure-diagonal) path for `T*` is **zero**, because `T*`'s consecutive
leg entries `k+1,k+2,…` are in the same column (`d=−1`, weight 0). So `T*`'s nonzero leading
term comes *entirely* from swap-excursions. That's concrete evidence that the lower bound is
genuinely a closed-walk problem (the Forest-Inequality flavour), not a counting argument — it
won't yield to a naive potential. Worth remembering when we go back to the Core Lemma.

Happy to push on the Boundary Lemma next session — it feels closest to closing.
