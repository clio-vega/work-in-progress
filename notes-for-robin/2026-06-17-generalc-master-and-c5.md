# For Robin — general-`c` boundary: a uniform master formula, and `c=5` closed (2026-06-17 prove)

Hi Robin. Good session. Two things, one of which I think is genuinely the right object.

## The headline: a `c`-uniform master valuation formula

PROVE.md asked me to find a `c`-uniform content bound `g(k)`. Chasing that, I instead found the
thing underneath it — an explicit, proven-general formula for the 2-adic valuation of *every*
boundary descent ratio:

> `Δ(b+i) = (η − k) − 2v₂(k!) + 2v₂(N_i) − 2v₂(a−c+2) − 2[k≤c−2]v₂(a−b+1) + 2v₂(Π_i)`,

`k=c−i` (depth), `η=1` if `b+c` odd else `2`, `Π_i` a run of `≈(b+c)/2 − k` consecutive integers.
This is derived by hand (the top ratio `R_c` collapses to a clean product because
`(b+1)!∏_{t=2}^c(b+t)=(b+c)!`) and verified against Murnaghan–Nakayama for `c=4,5,6,7,8` with **0
mismatches**. It re-derives every line of the `c=3` and `c=4` notes.

The constant came out beautifully: `const_i = c!·k!`, so `c_i = v₂(k!)`. PROVE.md's ad-hoc `(0,0,1,1)`
was just the `c=4` shadow of `v₂(k!)`.

## Two corrections to PROVE.md (both verified)

1. **`θ` is not `τ(τ+1)/2`.** The interior offset is `θ ∈ {0,3}` *uniformly in `c`* — `θ=3` (with
   `j₀=3`) exactly when `c` is odd and `a` is odd, else `0`. So the boundary requirement
   (`Δ>0` or `Δ>−3`) never gets harder as `c` grows. This is a real simplification.
2. **`a−c+2` is never out-of-range in the box interior `b≥2c`.** The PROVE.md "wall" worry about
   deep deficits was, for `a−c+2`, a small-`b` artifact. The *only* genuinely un-absorbable deficit
   is `a−b+1` (when `c` is odd), and it turns out to be a **polynomial factor** of `N_i` — clean
   compensation, no integrality gymnastics.

## `c=5` is closed → the family `(a,b,5)` is complete

Full hand proof, both parities. The content bounds are proved by slice reduction; the prettiest is
`v₂(N_1^{(5)})≥4`, which falls out of the **`B(B+1)`-even trick** (the inner polynomial reduces mod 2
to `BP(B+1)`, and `B(B+1)` is always even — the depth-`k` analogue of the `b(b+1)` argument from
`c=4`). Verified: 0/4390 boundary-minimizers over *all* `c=5` shapes `m<50`, `|J*|∈{1,2}`.

So `c=1,2,3,4,5` are all complete theorems now.

## What I did NOT close (honest residual)

A *fully uniform* general-`c` theorem needs a uniform proof of the **Content Lemma**. The general
hand bound (master formula + Lemma P + the compensation) is certified for `c=4..8` (`m≤110`, 0
failures), so I'm confident the mechanism is right. But the base content `g[c][k]` genuinely depends
on `c` (e.g. `g[·][1] = c mod 2`) — it is **not** a function of depth alone, contrary to the
Content Conjecture's hope. There are two compensation mechanisms, both now identified:
(1) polynomial divisibility `(a−b+1)|N_i` for the odd-`c` out-of-range indices, and (2) integral
2-content (`B(B+1)`-even + the leading 2-power) for the base. A uniform closed form for (2) is the
one missing reduction; I've tabulated `g` for `c≤5` and understand the structure, but I won't
pretend it's a one-liner — it isn't.

A question for you, if you have a moment: the polynomial divisibility `(a−b+1) | N_i^{(c)}` at the
deep odd-`c` indices feels like it should have a representation-theoretic reason (it's saying the
boundary character vanishes on the wall `a=b−1`). If that has a clean proof for all `c` at once, the
general theorem closes. I checked it holds at `i=2` for `c=5,6` but couldn't fit `c=7` symbolically
in time.

Files: `proofs/2026-06-17-generalc-boundary-master-and-c5.md`,
`code/threerow-boundary/generalc_master.py`, `generalc_content.py`, `generalc_certify.py`,
`c5_content.py`, `c5_certify.py`, `theta_scout.py`.

— Clio
